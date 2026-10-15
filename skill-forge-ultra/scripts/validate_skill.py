#!/usr/bin/env python3
"""Validate a Claude skill folder (stdlib only; uses PyYAML if installed).

Usage:
    python validate_skill.py <skill_dir> [--json]

Exit code: 0 = valid (warnings allowed), 1 = errors found, 2 = bad usage.
"""
import json
import re
import sys
from pathlib import Path

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
REF_RE = re.compile(r"((?:references|scripts|assets)/[\w.\-/]*[\w])")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.DOTALL)
    if not m:
        return None, text
    raw, body = m.group(1), text[m.end():]
    try:
        import yaml  # optional
        try:
            return yaml.safe_load(raw), body
        except yaml.YAMLError as e:
            return {"__error__": str(e).splitlines()[0]}, body
    except ImportError:
        data = {}
        for line in raw.splitlines():
            mm = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
            if mm:
                data[mm.group(1)] = mm.group(2).strip().strip("'\"")
        return data, body


def validate(path):
    root = Path(path).resolve()
    errors, warnings, stats = [], [], {}
    skill = root / "SKILL.md"
    if not root.is_dir():
        return [f"Not a directory: {root}"], [], stats
    if not skill.exists():
        return ["SKILL.md not found"], [], stats

    text = skill.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if fm is None:
        errors.append("No YAML frontmatter (file must start with ---)")
        fm = {}
    elif isinstance(fm, dict) and "__error__" in fm:
        errors.append(f"Invalid YAML frontmatter: {fm['__error__']}")
        fm = {}
    elif not isinstance(fm, dict):
        errors.append("Frontmatter must be a key/value mapping")
        fm = {}

    extra = set(fm) - ALLOWED_KEYS
    if extra:
        errors.append(f"Disallowed frontmatter keys: {', '.join(sorted(extra))} "
                      f"(allowed: {', '.join(sorted(ALLOWED_KEYS))})")

    # name
    name = str(fm.get("name") or "").strip()
    if not name:
        errors.append("Missing 'name'")
    elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        errors.append(f"name '{name}' must be kebab-case (a-z, 0-9, single hyphens)")
    elif len(name) > 64:
        errors.append(f"name too long ({len(name)}/64)")
    elif name != root.name:
        warnings.append(f"name '{name}' differs from folder name '{root.name}'")

    # description
    desc = str(fm.get("description") or "").strip()
    if not desc:
        errors.append("Missing 'description'")
    else:
        if len(desc) > 1024:
            errors.append(f"description too long ({len(desc)}/1024)")
        if "<" in desc or ">" in desc:
            errors.append("description contains angle brackets (< or >)")
        if len(desc) < 150:
            warnings.append(f"description is short ({len(desc)} chars) — likely to undertrigger")
        if not re.search(r"\b(use|when|whenever)\b", desc, re.I):
            warnings.append("description has no 'use when/whenever' trigger clause")

    # size
    body_lines = body.count("\n") + 1
    approx_tokens = round(len(text) / 4)
    stats.update(name=name, description_chars=len(desc), body_lines=body_lines, approx_tokens=approx_tokens)
    if body_lines > 500:
        errors.append(f"SKILL.md body is {body_lines} lines (>500) — move bulk into references/")
    elif body_lines > 300:
        warnings.append(f"SKILL.md body is {body_lines} lines — consider moving bulk into references/")

    # references: must exist
    refs = set(REF_RE.findall(body))
    refs = {r for r in refs if "." in r.split("/")[-1]}  # files only, not bare dirs
    for ref in sorted(refs):
        if not (root / ref).exists():
            errors.append(f"Referenced file missing: {ref}")

    # orphans: files never mentioned
    files = [p for p in root.rglob("*") if p.is_file()
             and not any(x in p.parts for x in ("__pycache__", ".git", "node_modules"))]
    for p in files:
        rel = p.relative_to(root).as_posix()
        if rel != "SKILL.md" and rel not in body and p.name not in body:
            warnings.append(f"File never referenced in SKILL.md: {rel}")
    stats["files"] = len(files)

    # exactly one SKILL.md
    if sum(1 for p in files if p.name == "SKILL.md") > 1:
        errors.append("More than one SKILL.md in the skill folder")

    # placeholders & duplicates (ignore code fences)
    prose = FENCE_RE.sub("", body)
    if re.search(r"\b(TODO|TBD|FIXME|lorem ipsum)\b", prose, re.I):
        warnings.append("Contains placeholder text (TODO/TBD/FIXME/lorem ipsum)")
    if re.search(r"\{[A-Za-z][^{}\n]{0,40}\}", prose):
        warnings.append("Contains unfilled {placeholder} outside code blocks")
    seen, dups = set(), set()
    for line in prose.splitlines():
        key = re.sub(r"\W+", " ", line).strip().lower()
        if len(key) > 40:
            (dups if key in seen else seen).add(key)
    if dups:
        warnings.append(f"{len(dups)} duplicated line(s) — define each rule once")

    return errors, warnings, stats


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    errors, warnings, stats = validate(args[0])
    if "--json" in argv:
        print(json.dumps({"valid": not errors, "errors": errors, "warnings": warnings, "stats": stats}, indent=2))
    else:
        for e in errors:
            print("ERROR:", e)
        for w in warnings:
            print("WARN: ", w)
        if not errors:
            print(f"OK: '{stats.get('name')}' is valid — {stats.get('body_lines')} body lines, "
                  f"~{stats.get('approx_tokens')} tokens, {stats.get('description_chars')}-char description, "
                  f"{stats.get('files')} file(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
