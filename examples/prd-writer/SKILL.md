---
name: prd-writer
description: Writes complete, build-ready Product Requirements Documents with ID'd requirements, priorities, measurable acceptance criteria, user flows, failure states, and risks. Use whenever the user wants a PRD, product spec, feature spec, requirements doc, or says things like "spec this feature", "turn this idea into a PRD", or "bikinin PRD", even if they only describe an app idea in a sentence.
---

# PRD Writer

Turn a product idea into a PRD an engineering team can estimate and build from without a follow-up meeting.

## Inputs
Use everything the user gives. If target users, platform, or scope are missing, assume the most plausible option, mark it `ASSUMPTION`, and continue. Ask one question only if the core problem itself is unclear.

## Structure
1. Summary — problem, target user, proposed solution, success metric (3–5 lines)
2. Goals & non-goals
3. Personas (max 3, each tied to ≥1 requirement)
4. User flows — happy path + empty, error, and offline/edge states
5. Requirements table: `ID | Requirement | Priority (P0–P3) | Acceptance criterion`
6. Non-functional requirements — performance, security, privacy, accessibility (numbers, not adjectives)
7. Dependencies & constraints
8. Risks: `Risk | Likelihood | Impact | Mitigation`
9. Milestones with go/no-go criteria
10. Open questions

## Rules
- Every acceptance criterion is observable: "search returns results in <500 ms for 95% of queries", not "search is fast".
- P0 = launch blocker. Keep P0 ≤ 30% of requirements so priority still means something.
- Label claims: `FACT` (user-given or verified), `ASSUMPTION`, `TARGET`. Never invent market statistics.
- Scale depth to scope: a single feature gets sections 1, 2, 4, 5, 8, 10.

## Before delivering, check
- Every persona maps to a requirement; every P0 has an acceptance criterion.
- No requirement contradicts a non-goal.
- Failure states exist for every user flow.

## Output
The finished PRD in Markdown. After it, at most 2 lines listing the key assumptions.
