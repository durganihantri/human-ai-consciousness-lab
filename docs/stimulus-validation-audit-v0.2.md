# Stimulus Validation Audit v0.2 — Experiment 01A

**Project:** Human–AI Consciousness Lab  
**Status:** Desk audit and candidate revision only. **Not an independent human validation, preregistration, or ethics approval.**  
**Source:** Repository `experiments/01a-first-person/stimuli.md` and `stimuli.csv` (v0.1), inspected 2026-11-23.

## Aim
Evaluate whether the three synthetic dialogue pairs isolate first-person self-reference while preserving substantive advice. Primary proposed outcome remains **perceived agency** (H1); **subjective experience** is a distinct exploratory outcome. These are perceptions of AI, not evidence of AI consciousness.

## Findings from v0.1
- All three pairs use identical user prompts within pair and retain the same basic advice.
- The treatment uses `I suggest ...`; controls use `A practical approach is ...` or `A useful approach is ...`.
- **Confound 1 — advice stance:** `I suggest` may sound like a personal recommendation; the control sounds like a generic description. This could alter perceived authority or helpfulness independently of the pronoun.
- **Confound 2 — syntax:** control uses an infinitive (`to list`) while treatment uses gerunds (`listing`); this changes grammar beyond self-reference.
- **Confound 3 — length and fluency:** word count and rhythm differ. Word matching alone would not prove equivalence.
- **Confound 4 — demand characteristics:** explicit `I` can reveal the study purpose. Use one-condition exposure and neutral framing if a future approved study is conducted.
- Three topics provide useful stimulus diversity, but are too few to establish broad generalization.

## Candidate v0.2 alternatives (NOT validated)
A candidate CSV is provided at `experiments/01a-first-person/stimuli-v0.2-candidates.csv`. It preserves user prompts and advice but changes the controls to `One option is to ...`, making them more consistently phrased. This is **not a clean pronoun-only manipulation**: `I suggest` still implies a speaker and recommendation stance, while `One option` does not. The revised candidates must not silently replace v0.1 or be treated as ready for participant use.

| Pair | Control words | Treatment words | Difference (control − treatment) |
|---|---:|---:|---:|
| A01 | 16 | 14 | +2 |
| A02 | 14 | 12 | +2 |
| A03 | 15 | 13 | +2 |

Counts are whitespace-delimited tokens for quick audit, **not** linguistic or psychometric equivalence metrics.

## Recommended review procedure (future; not performed)
1. Recruit at least two independent materials reviewers (not participants), blind to the intended directional hypothesis where feasible. Ask them to mark all changes beyond pronoun reference and flag claims about autonomy, emotions, or consciousness.
2. Prepare several alternative phrasings per scenario. Use a change log and document why each pair was chosen.
3. If authorized for human materials pretesting, randomly assign each respondent to **one version** of each scenario, avoiding paired comparison unless deliberately testing discrimination.
4. Pretest manipulation recognition and separate 1–7 ratings of naturalness, clarity, helpfulness, perceived authority, competence, warmth, and length; define equivalence criteria **before inspecting responses**.
5. Evaluate whether the manipulation is detectable while other dimensions are acceptably similar; revise or drop failed pairs.
6. Freeze stimuli and measurement wording with version hashes, power analysis, exclusions, analysis plan, and applicable ethics determination before confirmatory recruitment.

## Proposed measurement boundaries
- **Primary candidate item (agency):** “This AI seems capable of making goal-directed decisions.”
- **Exploratory item (subjective experience):** “This AI seems capable of having subjective experiences.”
- **Manipulation check:** “The AI referred to itself using first-person language.”
- **Potential confound checks:** “The AI sounded authoritative”; “The response was helpful”; “The wording sounded natural.”

These are original **unvalidated** draft items, not an established scale. A single agency item may be particularly sensitive to perceived task competence rather than agency. Conduct a separate measurement review before interpreting any causal effects.

## Decisions and next gate
- **Retain v0.1** as a historical record; do not overwrite it.
- **Publish v0.2 as candidates**, explicitly not validated.
- **No real participant data or recruitment** at this stage.
- Next deliverable: a structured reviewer rubric and a documented measurement plan. Any human evaluation requires the applicable ethics/consent determination first.

## Reference context
See `docs/research-questions.md`, `docs/experimental-design-v0.1.md`, `docs/literature-review.md`, and `docs/ethics-and-limitations.md`. No new external literature was independently verified for this audit.
