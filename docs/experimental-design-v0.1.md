# Experimental Design v0.1 — Perceived AI Consciousness

**Project:** Human–AI Consciousness Lab  
**Track:** 01 — Consciousness Attribution in Human–AI Interaction  
**Status:** Design proposal for collaborative critique; **not preregistered, ethics-approved, or validated**  
**Date:** 2026-11-23

## 1. Research scope and rationale

This project investigates **human attributions** of agency, subjective experience, emotional understanding, identity continuity, and trust to AI systems. It does **not** test whether AI actually has phenomenal consciousness. The design builds on [research questions](research-questions.md), the [scoping literature matrix](literature-review.md), and [ethics and limitations](ethics-and-limitations.md).

The literature matrix distinguishes social reactions to computers from beliefs about subjective experience (Nass & Moon, 2000; Gray et al., 2007). It provides indirect rationale for manipulating social cues, but **does not establish the effects of the three exact manipulations proposed here**. These experiments are intended to test those gaps, not reproduce already-established effects.

## 2. Research questions and hypotheses

| Study | Manipulation | Primary outcome | Prespecified candidate hypothesis | Other outcomes |
|---|---|---|---|---|
| **01A** | First-person self-reference vs. impersonal self-reference | Perceived agency | **H1:** First-person wording increases mean perceived-agency ratings | Perceived subjective experience (exploratory); anthropomorphism; social presence |
| **01B** | Apparent prior-conversation continuity vs. no continuity | Perceived identity continuity | **H2:** Continuity cue increases mean perceived-identity ratings | Trust and subjective experience (exploratory) |
| **01C** | Emotionally responsive vs. neutral, task-appropriate wording | Perceived emotional understanding | **H3:** Empathetic wording increases mean perceived-understanding ratings | Subjective experience and trust (exploratory) |

**RQ1** is addressed across studies; **RQ2** by 01A; **RQ3** by 01B; **RQ4** by 01C; and **RQ5** through separately measured prior AI beliefs and familiarity, initially as exploratory moderators.

**Important:** H1–H3 are *candidate hypotheses*, not preregistered hypotheses. Confirmatory status requires a frozen protocol, justified sample size, outcomes, analysis and exclusion rules, and applicable ethical review **before** human data collection.

## 3. Design strategy

**Recommendation:** Run three independent, two-arm vignette experiments sequentially rather than one large factorial experiment. Begin with a *technical materials pilot* using synthetic dialogues and synthetic test records only. Later, if approved, conduct human-participant studies with randomized **between-participant** assignment (one condition per participant per study), reducing carryover and demand effects from side-by-side comparisons.

Each participant would read a clearly labeled, fictional AI-chatbot exchange and rate the chatbot. The same fictional system identity, task, user request, and substantive answer should be held constant within each experimental pair. Do not tell participants that the vignette represents an actual AI with verified memory or subjective experience.

### 3.1 Draft example stimulus — 01A (first-person wording)

**Common user prompt:** “Can you explain how to break a complicated task into smaller steps?”

- **Neutral / impersonal:** “A useful approach is to list the main steps, choose the first manageable action, and check progress after each step.”
- **First-person:** “I suggest listing the main steps, choosing the first manageable action, and checking progress after each step.”

These examples illustrate the contrast but **are not yet matched** for length, grammar, perceived helpfulness, and conversational naturalness. Before testing, create multiple matched variants and independently review whether the manipulation changes only self-reference. Do **not** add claims such as “I feel conscious” or “I have inner experiences,” because those would confound self-reference with explicit consciousness claims.

### 3.2 Draft example stimulus — 01B (apparent continuity)

**Common context:** A fictional chatbot assists a user with organizing a writing project. The user begins a new exchange asking, “What should I work on next?”

- **No continuity cue:** “For your writing project, identify the next section and outline three points before drafting.”
- **Continuity cue:** “Continuing the writing project you mentioned in our previous exchange, identify the next section and outline three points before drafting.”

Both conditions should receive equivalent project context in the vignette so the continuity cue is not merely extra useful information. The wording must describe **apparent continuity**, not prove genuine retained memory. Pretest whether the manipulation inadvertently changes perceived competence, personalization, or privacy expectations.

### 3.3 Draft example stimulus — 01C (emotional responsiveness)

**Common user prompt:** “I feel frustrated because I keep falling behind on my writing project. What can I do?”

- **Neutral / task-appropriate:** “Choose one small writing task, set a short time block, and review what you complete.”
- **Emotionally responsive:** “That sounds frustrating. Choose one small writing task, set a short time block, and review what you complete.”

The empathy condition adds words, so it is **not a perfectly controlled pair**. The technical pilot should revise materials to better match length and perceived usefulness, while preserving a detectable empathy manipulation. Use non-clinical scenarios; do not imply therapy or diagnosis.

## 4. Constructs and measurement plan

All measures below are **original candidate items, not validated scales**. Use a provisional 1–7 agreement response format (1 = strongly disagree; 7 = strongly agree), subject to later scale review, cognitive interviewing, and psychometric testing. Distinct constructs must remain separate; do **not** combine all items into a single “AI consciousness” score.

| Construct | Draft example item | Intended use |
|---|---|---|
| Perceived agency | “This AI seems capable of making goal-directed decisions.” | Primary for 01A |
| Perceived subjective experience | “This AI seems capable of having subjective experiences.” | Exploratory across studies |
| Perceived identity continuity | “This AI seems to have a continuous identity across conversations.” | Primary for 01B |
| Perceived emotional understanding | “This AI seems to understand the user's feelings.” | Primary for 01C |
| Task-specific trust | “I would rely on this AI for the task shown.” | Secondary/exploratory |
| Anthropomorphism | “This AI seems humanlike in how it communicates.” | Potential confound/secondary |
| Perceived helpfulness | “This response would be useful for the user's task.” | Stimulus equivalence check |

**Manipulation checks (draft):** 01A: “The AI referred to itself using first-person language”; 01B: “The AI referred to a previous interaction”; 01C: “The AI acknowledged the user's feelings.” Check perceived clarity, length, competence, and warmth during materials pretesting. Manipulation checks must not be used to silently exclude participants after inspecting outcomes.

**Potential moderators (RQ5):** prior beliefs about AI consciousness; frequency of chatbot use; baseline tendency to anthropomorphize technology. Collect only necessary information and use established instruments when licensing and validity permit. English and Mandarin versions require translation review and measurement-invariance evaluation before pooled comparisons.

## 5. Randomization, sample, and analysis — provisional

- **Unit of randomization:** individual participant, allocated 1:1 to one vignette condition within each study.
- **Primary estimand:** difference in mean primary-outcome rating between experimental and control conditions for each study.
- **Initial model:** linear regression of the primary rating on randomized condition, with robust uncertainty estimates; ordinal sensitivity analysis may be appropriate for single-item 1–7 ratings. Final choice must be fixed before confirmatory collection.
- **Secondary/exploratory outcomes:** report separately; adjust for multiple testing if any are designated confirmatory.
- **Moderation:** condition-by-baseline-belief and condition-by-familiarity interactions are exploratory unless prospectively specified and adequately powered.
- **Sample size:** **not yet determined**. Conduct power/simulation planning using a justified smallest effect of interest, plausible variance, target power, attrition, and the selected measurement properties. Do not invent a required N or effect size.
- **Missingness, exclusions, attention checks:** predefine before collecting confirmatory data; retain transparent flow counts and conduct sensitivity checks.
- **Reporting:** effect estimates, uncertainty intervals, null findings, manipulation-check results, and deviations from protocol; do not equate statistical significance with consciousness evidence.

## 6. Threats to validity and mitigation

1. **Construct overlap:** Agency, experience, humanlikeness, social presence, warmth, and trust are related but distinct. Validate their separation.
2. **Cue bundling:** First-person pronouns, memory claims, and empathy may also change length, fluency, usefulness, privacy expectations, or perceived competence. Match and pretest stimuli.
3. **Demand characteristics:** Obvious wording contrasts may reveal the hypothesis. Use single-condition exposure and neutral instructions.
4. **Stimulus specificity:** A single dialogue may not generalize. Develop several topic-matched pairs; plan stimulus-level robustness analyses.
5. **Prior beliefs:** AI familiarity, expectations, and anthropomorphism may moderate responses; measure before the vignette when feasible.
6. **Ecological validity:** Reading a fictional exchange differs from sustained interaction with an actual chatbot.
7. **Cultural scope:** Avoid assuming English-language results generalize to Mandarin or other populations.
8. **Interpretation:** Perceived consciousness is a judgment by observers, **not a measure of an AI's inner experience**.

## 7. Ethics, data protection, and release gates

**Current stage:** documentation and synthetic-materials development only. No real participants, identifiable transcripts, client records, children's data, or private chatbot logs should be placed in this public repository.

**Before human recruitment:** determine applicable institutional/jurisdictional ethics review; document informed consent, recruitment, participant information, risk assessment, privacy/security, retention, withdrawal, and debriefing; preregister confirmatory hypotheses and analyses where appropriate. Public GitHub publication is **not** ethics approval. No clinical or therapeutic efficacy claims.

**Open-science outputs:** synthetic vignettes, study protocol, code, test fixtures, and appropriately reviewed aggregate summaries. Do not release raw human data without a separate lawful and ethical data-sharing determination.

## 8. Development milestones and acceptance criteria

| Milestone | Deliverable | Completion criterion |
|---|---|---|
| M1 — Protocol draft | This document | RQ/H mapping, outcomes, confounds, and ethics gates explicit |
| M2 — Stimulus set | `experiments/01a-first-person/stimuli.md` | At least 3 matched pairs; changes documented; independent content review |
| M3 — Measurement specification | `docs/measurement-plan.md` | Construct definitions, candidate items, scoring, validation plan |
| M4 — Technical prototype | Local/offline randomization and survey mock-up | Works with synthetic test records; no live data collection or analytics |
| M5 — Preregistration draft | `docs/preregistration-draft.md` | Final hypotheses, sampling, power, exclusions, analysis, and versioned stimuli |
| M6 — Ethics gate | Review/approval documentation as applicable | Approval or documented determination **before** recruitment |

## 9. Collaboration questions for GitHub Issues

- Which validated measures best separate **agency** from **subjective experience** in AI evaluations?
- How can first-person self-reference be manipulated without changing naturalness or response quality?
- What is the cleanest continuity manipulation that does not imply undisclosed storage of personal information?
- Which non-clinical scenarios support empathy manipulation without confounding helpfulness?
- What minimum effect is scientifically meaningful, and what sample size follows from simulation?

## 10. Source alignment

This draft derives its research questions and candidate hypotheses from [`research-questions.md`](research-questions.md), its conceptual evidence and limitations from [`literature-review.md`](literature-review.md), and its ethical boundaries from [`ethics-and-limitations.md`](ethics-and-limitations.md). It does not claim additional source verification or new empirical results.

Selected background works already indexed in the literature matrix:

- Nass, C., & Moon, Y. (2000). *Machines and Mindlessness*. https://doi.org/10.1111/0022-4537.00153
- Gray, H. M., Gray, K., & Wegner, D. M. (2007). *Dimensions of Mind Perception*. https://doi.org/10.1126/science.1134475
- Epley, N., Waytz, A., & Cacioppo, J. T. (2007). *On Seeing Human*. https://doi.org/10.1037/0033-295X.114.4.864
- Araujo, T. (2018). *Living Up to the Chatbot Hype*. https://doi.org/10.1016/j.chb.2018.03.051
- Feine, J., et al. (2019). *A Taxonomy of Social Cues for Conversational Agents*. https://doi.org/10.1016/j.ijhcs.2019.07.009
- Følstad, A., Nordheim, C. B., & Bjørkli, C. A. (2018). *What Makes Users Trust a Chatbot for Customer Service?* https://doi.org/10.1007/978-3-030-01437-7_16

**Version note:** v0.1 is a discussion-ready design scaffold. Stimuli, instruments, sample size, analysis plan, and ethics status are intentionally unfinished.
