# Quality Gates & Skill Archetypes

Contents: 1. Domain quality gates · 2. Archetype skeletons · 3. Description patterns · 4. Common defects

## 1. Domain quality gates

Embed only the gates relevant to the target skill, phrased as checks the executing model runs before delivering.

| Domain | Gates (observable) |
|---|---|
| Coding | Runs/compiles; edge cases (empty, null, huge, unicode, concurrency) handled; tests included or proposed; no secrets/injection/unsafe eval; matches stated language/version; no invented APIs |
| Product spec / PRD / GDD | Every requirement has ID, priority, measurable acceptance criterion; user flows incl. failure/empty states; dependencies & constraints listed; assumptions labeled; non-goals stated |
| Marketing / copy | Audience & single conversion goal named; clear differentiator; claims verifiable (no fake stats/testimonials); CTA present; tone matches brand; length fits channel |
| Research / analysis | Sources cited and real; recency checked when it matters; conflicting evidence shown; confidence stated; claims traceable to sources |
| Design / UI-UX | Visual hierarchy; consistent tokens; accessibility (contrast ≥4.5:1, focus, alt text); responsive; feasible to implement |
| Business strategy | Assumptions explicit; unit economics add up; alternatives considered; risks with mitigations; measurable success metrics |
| Education | Objectives stated; prerequisite → advanced sequencing; worked examples; check-for-understanding/assessment |
| Data / automation | Input schema validated; idempotent where possible; errors logged not swallowed; results reproducible; numbers re-checked |
| Writing / docs | Audience fit; one idea per section; scannable structure; no filler; consistent terminology |
| Legal / medical / finance | Informational, not definitive advice; jurisdiction/context flagged; recommend professional review for consequential decisions |

Other domains: derive gates from "what would an expert reviewer reject this for?"

## 2. Archetype skeletons

Pick the closest; trim aggressively.

**Generator** (writes a document/asset): Mission → Inputs & assumptions → Structure template → Domain rules → Quality gates → Output contract.

**Transformer** (converts/cleans/reformats input): Accepted inputs → Transformation rules (table) → Edge cases → Validation (prefer a script) → Output format.

**Analyst / Reviewer** (evaluates something): Criteria with weights or severities → Procedure → Evidence rules → Report template → Verdict rule.

**Workflow / Agent** (multi-step, tools): Preconditions & tools → Steps with checkpoints → Failure/fallback per step → Completion criteria → What to report.

**Persona / Advisor** (domain expert voice): Expertise scope → Decision frameworks → When to ask vs assume → Boundaries/escalation → Answer shape.

## 3. Description patterns

Formula: `[What it does, with key nouns]. Use this skill whenever [contexts], including [casual phrasings, other-language phrasings], even if the user doesn't explicitly say [term]. [Optional: Do NOT use for X — use Y instead.]`

Good: "Writes complete, investor-ready pitch decks outlines with slide-by-slide content and speaker notes. Use whenever the user wants a pitch, investor presentation, fundraising story, or 'bikin pitch deck', even if they only describe their startup."

Bad: "A helpful skill for presentations." (no triggers, no scope)

## 4. Common defects (check during AUDIT/DEBUG)

| Symptom | Likely cause | Fix |
|---|---|---|
| Never triggers | Vague/short description, missing user phrasings | Rewrite with formula §3, add trigger phrases |
| Triggers on wrong tasks | Description too broad | Add scope nouns + "Do NOT use for" |
| Generic output | Adjectives instead of standards | Replace with measurable gates |
| Inconsistent output | No template/output contract | Add explicit structure |
| Hallucinated facts | No reliability rules | Add fact/assumption labeling + no-fabrication |
| Bloated, slow | Repetition, motivational prose, inline references | Dedupe, move bulk to references/ |
| Explains instead of doing | No "deliver the artifact" rule | Add output contract |
| Broken file refs | Mentions files that don't exist | Create them or remove references |
