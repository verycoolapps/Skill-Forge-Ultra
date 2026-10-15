# Modes Playbook

Detailed procedure per mode. Read only the section for the detected mode.

Contents: CREATE · IMPROVE · DEBUG · OPTIMIZE · MERGE · AUDIT · EXTEND · Converting a raw prompt

---

## CREATE

1. Extract: problem class (not the single instance), deliverable, audience, success signal.
2. Choose archetype (`references/templates.md`) — Generator, Transformer, Analyst, Workflow, or Persona.
3. Write frontmatter first. List 5 realistic trigger phrases (≥1 casual, ≥1 in the user's language) and make sure the description covers all of them.
4. Write body from the template; delete every section that would not change output.
5. Add domain gates from `references/quality-gates.md` §1, phrased as pre-delivery checks.
6. Decide scripts: only for deterministic, repeated, or mechanically checkable work.
7. Self-audit (SKILL.md §5) → validate → package → present.

Instance vs class: "write my bakery's Instagram caption" → skill = "Instagram caption writer for small F&B brands", with the bakery as an example input, not hardcoded.

## IMPROVE

1. Read the existing skill fully. Note its `name`, purpose, and any behavior the user relies on.
2. Diagnose against `references/quality-gates.md` §4 before editing.
3. Preserve `name` and folder name (installers match on it). Preserve every capability unless the user asks to drop it.
4. Upgrade in this order: description triggers → output contract → measurable gates → reliability rules → token cuts.
5. Deliver the full new version plus a ≤5-line changelog (what changed, why).

## DEBUG

1. Classify the failure: (a) does not trigger, (b) triggers wrongly, (c) triggers but wrong output, (d) breaks on tools/files.
2. Locate cause:
   - (a)/(b) → description wording, scope nouns, collisions with neighbor skills.
   - (c) → missing output contract, vague standard, conflicting rules, rule buried in prose.
   - (d) → wrong paths, missing files, unavailable tools, no fallback.
3. Patch the minimal set of lines that fixes the cause. Do not rewrite healthy sections.
4. Report: `Cause → Fix → How to verify` (one line each), then the corrected file.

## OPTIMIZE

1. Measure before: lines, characters, approximate tokens (chars ÷ 4).
2. Cut in this order: repetition → motivational/role-play prose → examples restating rules → inline bulk that belongs in `references/` → verbose phrasing.
3. Never cut: triggers, output contract, safety/reliability rules, edge cases that change results.
4. Report before/after size and list any behavior intentionally changed (should be none).

## MERGE

1. Inventory each source skill's capabilities and triggers in a table.
2. Resolve conflicts explicitly (pick one rule, note why).
3. One `name`, one description covering the union of triggers, deduped body.
4. If merged scope becomes incoherent (two unrelated problem classes), recommend keeping them separate instead.

## AUDIT

Score nothing numerically unless asked. Use the report format in SKILL.md §7. Check, in order:
1. Frontmatter validity and trigger quality.
2. Does the body produce the promised deliverable?
3. Contradictions, ambiguity, untestable standards.
4. Reliability (fabrication risk, untrusted input handling).
5. Missing/orphan files.
6. Token waste.
Severity: critical = wrong/unsafe output or never triggers; major = inconsistent or generic output; minor = waste or style.

## EXTEND

1. Add the capability as its own section or reference file.
2. Update the description to include the new triggers without diluting old ones.
3. Re-check that existing rules still hold; add a decision rule if old and new behaviors could conflict.

## Converting a raw prompt into a skill

Raw prompts (like long "You are an elite X" meta-prompts) are usually ~60% ceremony. Procedure:
1. Keep: objective, decision rules, output format, constraints, quality standards, safety rules.
2. Drop: identity hype, repeated priorities, motivational slogans, "think step by step" filler, instructions that restate default model behavior.
3. Convert adjectives into gates, paragraphs into tables or rules, long reference lists into `references/`.
4. Write a trigger-rich description — the raw prompt never has one, and without it the skill won't activate.
