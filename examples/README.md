# Examples

Real skills in the format Skill Forge Ultra produces. Each folder passes `validate_skill.py` and can be packaged and installed as-is.

| Skill | Archetype | What it shows |
|---|---|---|
| [`prd-writer`](prd-writer/SKILL.md) | Generator | Vague goal ("good PRD") turned into measurable gates: ID'd requirements, P0 cap, FACT/ASSUMPTION labels |
| [`code-review-pro`](code-review-pro/SKILL.md) | Analyst | Priority-ordered criteria, line-referenced findings, verdict rule, "no manufactured criticism" |
| [`caption-umkm-id`](caption-umkm-id/SKILL.md) | Generator (Bahasa Indonesia) | Skill written in the user's language, platform-specific rules, anti-fake-testimonial rule |

Package any of them:

```bash
python skill-forge-ultra/scripts/package_skill.py examples/prd-writer dist/
```

---

## Prompts to try

```text
Turn this prompt into a skill: <paste any long prompt>
Bikin skill buat nulis caption TikTok untuk toko kopi aku
Make a skill that converts messy CSV exports from Shopify into clean monthly sales reports
Audit this SKILL.md: <paste>
My skill never triggers when I ask for invoices. Debug it: <paste>
Optimize this skill, it's way too long: <paste>
Merge these two skills into one: <paste both>
```

---

## Example: AUDIT mode output

Input — a typical "prompt-style" skill:

```markdown
---
name: Marketing Genius
description: A helpful marketing assistant.
---
You are the world's best marketer. Be creative, viral, and professional.
Always write amazing copy. Make it viral. Be professional at all times.
```

Output:

```
Verdict: rebuild — it will rarely trigger and gives no standard to meet.
Defects (most severe first):
- [critical] [frontmatter.name] "Marketing Genius" is not kebab-case → "marketing-copywriter"
- [critical] [frontmatter.description] No triggers or scope → "Writes conversion-focused ad, landing-page, and social copy… Use whenever the user wants copy, a caption, an ad, a headline…"
- [major] [body L1–2] "creative, viral, professional" are unmeasurable → audience + one conversion goal + differentiator + CTA + channel length limit
- [major] [body] No output contract → define variants count, structure, and format
- [major] [body] No reliability rule → forbid fabricated stats/testimonials
- [minor] [body L2–3] "viral"/"professional" stated twice → define once
Token savings available: ~40% (identity hype and repetition)
```

---

## Example: prompt → skill

| Raw prompt habit | What the forge does instead |
|---|---|
| "You are an elite, world-class expert…" | One-line mission naming the deliverable |
| "Be thorough and professional" | Observable gates ("every P0 has an acceptance criterion") |
| No `description` at all | Trigger-rich description incl. casual + non-English phrasings |
| 40 rules in one wall of text | Core rules in SKILL.md, bulk in `references/`, loaded on demand |
| "Double-check your work" | Concrete pre-delivery checklist + a validator script where mechanical |
| Same priority repeated 4 times | Each rule defined once, referenced by section |
