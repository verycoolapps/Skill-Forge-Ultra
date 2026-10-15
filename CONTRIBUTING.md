# Contributing

PRs welcome — especially new domain quality gates, templates, and example skills.

1. Fork and branch.
2. Keep the core `SKILL.md` lean. New bulky knowledge goes into `references/` with a one-line pointer saying *when* to read it.
3. Example skills go in `examples/<kebab-name>/SKILL.md` and must pass the validator.
4. Run before opening a PR:
   ```bash
   python -m unittest discover tests
   python skill-forge-ultra/scripts/validate_skill.py skill-forge-ultra
   ```
5. Describe the behavior change, not just the text change: what output gets better, and how you checked.

House rules: no unverifiable claims ("10x better"), no fabricated benchmarks, scripts stay stdlib-only.
