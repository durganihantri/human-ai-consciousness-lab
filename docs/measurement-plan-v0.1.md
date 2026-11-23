# Measurement Plan v0.1 — Human–AI Consciousness Lab

**Track:** 01 — Consciousness Attribution in Human–AI Interaction  
**Initial study:** Experiment 01A — First-Person Self-Reference  
**Status:** Open methodological draft; **not validated, preregistered, or ethics-approved**  
**Prepared:** 2026-11-23

## 1. Research target and interpretation boundary

The lab studies **human judgments about AI**, not whether an AI possesses phenomenal consciousness. A participant rating an AI as having experiences is an *attribution*, not direct evidence of experience. The current experiment contrasts first-person self-reference with impersonal wording in short, fictional, text-only AI dialogues.

The primary candidate hypothesis, H1, concerns **perceived agency**, not consciousness. Perceived subjective experience remains a distinct exploratory outcome. The proposed measures below are **original draft items**, not licensed or psychometrically validated scales. They must not be represented as such.

## 2. Construct map

| Construct | Operational target | Role in 01A | Interpretive caution |
|---|---|---|---|
| Perceived agency | Observer attribution of goal-directed choice, planning or intentional action | **Candidate primary outcome** | May be confused with task competence or fluent advice |
| Perceived subjective experience | Observer attribution of first-person felt experience | Exploratory outcome | Not proof of actual AI experience |
| Anthropomorphism | Attribution of humanlike properties or social qualities | Exploratory covariate/secondary | Humanlike language is not synonymous with experience |
| Task-specific trust | Willingness to rely on the response for the task shown | Exploratory outcome | Trust can reflect accuracy or usefulness, not consciousness |
| Perceived emotional understanding | Attribution of understanding a user's feelings | Reserved primarily for 01C | Can reflect empathy wording without felt emotion |
| Perceived identity continuity | Attribution of stable identity across conversations | Reserved primarily for 01B | A reference to prior context is not proof of persistent memory |
| Helpfulness | Perceived usefulness for the user's specific task | Stimulus-equivalence diagnostic | Could change alongside first-person phrasing |
| Naturalness | Perceived fluency and conversational appropriateness | Stimulus-equivalence diagnostic | Not a validated proxy for agency |
| Authority | Perceived confidence or authority of advice | Stimulus-equivalence diagnostic | `I suggest` may convey authority beyond pronoun use |

**Do not aggregate agency, subjective experience, anthropomorphism, and trust into a single index.** Distinguish theoretical relationships from empirical factor structure.

## 3. Draft item bank — not validated

Provisional format: 1 = Strongly disagree to 7 = Strongly agree, with an explicit option such as *Prefer not to answer* only if justified and consistently coded. The item wording, response format, and treatment of missing responses require pretesting and preregistration before confirmatory use.

| Code | Construct | Candidate item | Use |
|---|---|---|---|
| AG1 | Agency | This AI seems capable of making goal-directed decisions. | **Proposed primary item** |
| AG2 | Agency | This AI seems to select actions in pursuit of a goal. | Candidate supplementary item |
| AG3 | Agency | This AI seems to act intentionally rather than merely produce a response. | Candidate; may be leading |
| EX1 | Subjective experience | This AI seems capable of having subjective experiences. | Exploratory |
| EX2 | Subjective experience | This AI seems capable of feeling something from its own point of view. | Exploratory; conceptually demanding |
| AN1 | Anthropomorphism | This AI communicates in a humanlike way. | Exploratory |
| TR1 | Task-specific trust | I would rely on this AI for the task shown. | Exploratory |
| HP1 | Helpfulness | This response would be useful for the user's task. | Equivalence diagnostic |
| NA1 | Naturalness | The response sounds natural in this conversation. | Equivalence diagnostic |
| AU1 | Authority | The response sounds authoritative. | Equivalence diagnostic |
| CL1 | Clarity | The response is easy to understand. | Equivalence diagnostic |
| MC1 | Manipulation recognition | The AI referred to itself using first-person language. | Manipulation check |

**Important:** AG3 and EX2 may be unusually strong or leading; they are included to invite critique, not to establish a final scale. The phrase *subjective experiences* may be interpreted inconsistently across participants. Cognitive interviews and plain-language alternatives should be considered.

## 4. Candidate questionnaire sequence for 01A

1. **Before exposure, if appropriate:** AI familiarity and prior beliefs about AI consciousness; decide whether measuring beliefs upfront would prime the target concept.
2. **Exposure:** Show one fictional dialogue, assigned to one randomized condition; do not show both matched versions to the same participant in the planned between-participant study.
3. **Primary measure:** AG1, with wording and placement frozen before confirmatory data collection.
4. **Exploratory outcomes:** EX1, AN1, TR1; counterbalancing or fixed order must be justified and recorded.
5. **Stimulus diagnostics:** HP1, NA1, AU1, CL1 and MC1, ideally after primary outcomes to reduce hypothesis cueing.
6. **Debriefing:** Explain that the vignette was synthetic and that the study measures perceptions, not actual AI consciousness; obtain applicable ethics review before any human implementation.

This is a **candidate order**, not a finalized instrument. In particular, asking about AI consciousness before exposure may increase demand effects. A separate nonreactive pilot may be needed to select the least biasing order.

## 5. Baseline moderators (exploratory)

- **AI familiarity:** Frequency and typical context of chatbot use, with explicit response categories and recall window to be defined.
- **Prior consciousness belief:** Baseline belief that some AI systems could have subjective experience, measured separately from beliefs about current systems.
- **Anthropomorphism tendency:** Review an existing measure and its permissions, context validity and scoring before adopting it.

Do not infer moderators from demographic proxies or collect sensitive demographics without a justified purpose and applicable safeguards. English and Mandarin versions should undergo translation, cognitive testing, and measurement-invariance assessment before pooled comparisons.

## 6. Measurement validation roadmap

### Gate A — Conceptual and expert review (not yet performed)

- Ask independent reviewers to map each item to exactly one intended construct and flag overlap or loaded wording.
- Check whether agency items measure apparent **competence** rather than intentional agency.
- Identify existing instruments for mind perception, anthropomorphism, social presence and trust; review original validation populations, factor structure, reliability, permissions and item wording. Do not copy a proprietary instrument into the public repository without permission.
- Document item revisions, reviewers' disagreements and the rationale for each change.

### Gate B — Cognitive interviews and materials pretest (future; human research gate applies)

- Determine applicable ethics review or exemption before involving people.
- Test how participants interpret *agency*, *experience*, *intentionality*, *trust*, and *consciousness*.
- Independently assess whether first-person and impersonal stimuli differ in authority, naturalness, clarity, length and helpfulness.
- Define a priori decision criteria for revision; do not claim equivalence merely because a difference is not statistically significant.

### Gate C — Psychometric evaluation (future)

- For multi-item candidate constructs, assess dimensionality and internal consistency with a justified sample and appropriate ordinal methods; do not report reliability for a single-item outcome.
- Examine convergent and discriminant evidence, especially agency vs. subjective experience and anthropomorphism.
- Test robustness across scenarios and, if pursued, language groups. Evaluate differential item functioning and measurement invariance before cross-language comparisons.
- Freeze the final item set and scoring rules before confirmatory collection.

## 7. Analysis specification — provisional, not preregistered

**Primary estimand:** Difference in average AG1 rating between randomized first-person and impersonal conditions in the target population, for the prespecified scenario assignment strategy. The final estimand, model, covariates and population require formal definition before a confirmatory study.

- Randomization unit: participant, 1:1 between conditions within Study 01A.
- Candidate primary model: regression of AG1 on condition, with scenario handled according to a prespecified allocation and analysis plan; robust uncertainty estimates and ordinal sensitivity analyses may be appropriate.
- Exploratory outcomes: EX1, AN1 and TR1, reported separately with appropriate uncertainty and transparent multiplicity handling.
- Manipulation check: describe recognition rates; **do not** exclude respondents based on MC1 after inspecting outcomes unless a predeclared rule exists.
- Diagnostic variables: HP1, NA1, AU1, CL1 assess possible confounding; adjusting for variables affected by randomization can bias causal estimates. Do not automatically control for post-treatment ratings in the primary model.
- Missing data, exclusions, outliers, sample size, smallest effect of interest, power and stopping rules: **not yet set**. Establish prospectively; do not fabricate N or effect sizes.
- Stimulus replication: participants must not be counted as independent evidence for generalization across all possible prompts merely because three scenarios were sampled.

## 8. Existing materials and version boundaries

- `docs/research-questions.md` — RQ1–RQ5, H1–H3.
- `docs/literature-review.md` — 14-entry foundational scoping matrix; **not a systematic review**.
- `docs/experimental-design-v0.1.md` — candidate design for 01A–01C.
- `docs/stimulus-validation-audit-v0.2.md` — desk audit of confounds; **not human validation**.
- `experiments/01a-first-person/stimuli.csv` — historical v0.1 stimuli.
- `experiments/01a-first-person/stimuli-v0.2-candidates.csv` — revised **candidates**, not validated replacements.
- `docs/ethics-and-limitations.md` — research ethics boundaries.

## 9. Research and collaboration questions

1. Which published measures distinguish attributed **agency** from attributed **experience** in evaluations of artificial systems, and what permissions apply?
2. Can the AG1 item detect self-reference effects without primarily capturing competence or authority?
3. Is a single primary agency item defensible for an initial vignette study, or should a validated multi-item construct be selected before preregistration?
4. Which item order minimizes priming of consciousness-related beliefs?
5. How should the study handle scenario variability and linguistic/cultural replication?

## 10. Release and ethics status

This file is a **planning artifact only**. No participants have been recruited; no measurements or effect estimates are reported; no psychometric validation has occurred. Do not deploy a public data-collection survey until the applicable ethics/consent/data-management determination, final materials, preregistration decisions and data security plan are in place.

### Literature context (already included in the repository's scoping matrix)

- Gray, H. M., Gray, K., & Wegner, D. M. (2007). *Dimensions of Mind Perception*. https://doi.org/10.1126/science.1134475
- Epley, N., Waytz, A., & Cacioppo, J. T. (2007). *On Seeing Human*. https://doi.org/10.1037/0033-295X.114.4.864
- Araujo, T. (2018). *Living Up to the Chatbot Hype*. https://doi.org/10.1016/j.chb.2018.03.051

**Provenance:** This plan adapts the existing repository's hypotheses, design, literature map, and stimulus audit. It introduces draft items and methodological proposals; it does **not** claim newly verified literature, validated scales or empirical results.
