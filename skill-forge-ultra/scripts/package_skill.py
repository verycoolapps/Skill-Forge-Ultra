#!/usr/bin/env python3
"""Package a skill folder into an installable <name>.skill (zip) file.

Usage:
    python package_skill.py <skill_dir> [output_dir]

Validates first (via validate_skill.py) and refuses to package on errors.
"""
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skill import validate  # noqa: E402

SKIP = {"__pycache__", ".git", "node_modules", ".DS_Store", "evals"}


def main(argv):
    if len(argv) not in (2, 3):
        print(__doc__)
        return 2
    root = Path(argv[1]).resolve()
    out_dir = Path(argv[2] if len(argv) == 3 else ".").resolve()
    errors, warnings, stats = validate(root)
    for w in warnings:
        print("WARN: ", w)
    if errors:
        for e in errors:
            print("ERROR:", e)
        print("Not packaged — fix errors first.")
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / f"{stats['name']}.skill"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob("*")):
            rel = p.relative_to(root)
            if p.is_file() and not (set(rel.parts) & SKIP):
                arc = Path(root.name) / rel
                z.write(p, arc.as_posix())
                print("  +", arc.as_posix())
    print(f"Packaged: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
