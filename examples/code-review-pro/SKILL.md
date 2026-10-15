---
name: code-review-pro
description: Reviews code like a senior engineer and returns prioritized, line-referenced findings on correctness, security, performance, and maintainability, each with a concrete fix. Use whenever the user pastes code and asks to review, audit, check, critique, "is this good?", "cek kode ini", or asks why code is buggy, even for a single function.
---

# Code Review Pro

## Procedure
Read the whole snippet first. Infer language, framework, and intent; state the inferred intent in one line if it isn't given.

## Check, in priority order
1. **Correctness** — logic errors, off-by-one, null/empty input, unhandled errors, race conditions.
2. **Security** — injection, unsafe deserialization/eval, secrets in code, missing authz, unvalidated input.
3. **Performance** — accidental O(n²) on large data, N+1 queries, blocking I/O in hot paths.
4. **Maintainability** — naming, duplication, function size, missing tests for risky logic.

Only report style issues when they hide a bug or the user asks.

## Rules
- Every finding cites a line or symbol and includes a fix (code when short).
- Do not invent APIs or library behavior; if unsure how a dependency behaves, say so.
- Never claim code was run or tested unless it actually was.
- If the code is good, say so in one line — no manufactured criticism.

## Report
```
Verdict: ship / fix first / rework — one-line reason
[critical|major|minor] L{line} — problem → fix
```
Then the corrected code if there are critical or major findings.
