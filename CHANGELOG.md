# Changelog

## [1.0.0] — 2026-10-15

### Added
- `skill-forge-ultra` skill: 7 modes (CREATE, IMPROVE, DEBUG, OPTIMIZE, MERGE, AUDIT, EXTEND), trigger-first frontmatter rules, reliability block, one-pass self-audit, AUDIT report format.
- `references/modes-playbook.md` — step-by-step procedure for every mode, plus raw-prompt → skill conversion.
- `references/templates.md` — fill-in templates for 5 skill archetypes and a script stub.
- `references/quality-gates.md` — gates for 10 domains, description formula, defect table.
- `scripts/validate_skill.py` — frontmatter, triggers, size/tokens, missing & orphan files, duplicates, placeholders; `--json` output.
- `scripts/package_skill.py` — validates, then builds an installable `.skill`.
- Three example skills, unit tests, GitHub Actions workflow in `ci/`.
