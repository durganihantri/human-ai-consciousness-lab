# Published Measurement Instruments: Applicability Review v0.1

**Project:** Human–AI Consciousness Lab | **Study:** Experiment 01A — First-Person Self-Reference  
**Date:** 2026-11-23 | **Status:** Desk-based instrument appraisal, not a systematic review, license clearance, or psychometric validation.

## Decision summary

**Do not replace the draft AG1 primary item with a published scale yet.** The most relevant published framework separates *attributed agency* from *attributed experience*, but the original task and population differ substantially from a short text-only chatbot vignette. Retain AG1 provisionally, seek expert feedback, and conduct a targeted measure-selection and cognitive-testing phase before preregistration. Do not label the lab's draft items as validated.

## Source and instrument comparison

| Instrument | Source | What was established | Fit for 01A | Decision / caution |
|---|---|---|---|---|
| Dimensions of Mind Perception | Gray, Gray & Wegner (2007), DOI: 10.1126/science.1134475 | Online comparative judgments of 18 capacities across diverse targets yielded two dimensions: Agency (7 capacities) and Experience (11 capacities). | **High conceptual fit, uncertain measurement transfer.** Original target comparisons are not a ready-made validated scale for single-chatbot, single-vignette ratings. | Use as construct framework. Review original items, response format, and permissions; validate any adapted chatbot items independently. |
| Individual Differences in Anthropomorphism Questionnaire (IDAQ) | Waytz, Cacioppo & Epley (2010), DOI: 10.1177/1745691610369336 | Measures general individual tendency to anthropomorphize nonhuman targets; original authors provide item list and scoring instructions. | **Possible baseline moderator**, not the primary post-vignette outcome. Includes diverse targets and consciousness-related wording that may prime the experiment. | Consider only after examining length, priming, construct relevance, and reuse permissions. Do not paste full item set into repository. |
| Godspeed | Bartneck, Kulić, Croft & Zoghbi (2009), DOI: 10.1007/s12369-008-0001-3 | Five semantic-differential questionnaires for robot anthropomorphism, animacy, likeability, intelligence, and safety. | **Partial fit** for anthropomorphism, but developed for embodied robots; movement and appearance items are inappropriate for text-only vignettes. One anthropomorphism item explicitly contrasts unconscious/conscious, confounding our construct separation. | Do not use the unmodified total scale for 01A. A carefully justified subset would require new validation and permissions review. |
| Trust Perception Scale–HRI | Schaefer (2016), *Measuring Trust in Human Robot Interactions*, in *Robust Intelligence and Trust in Autonomous Systems* | A 40-item and abbreviated 14-item HRI trust instrument, focused on robot behaviors/capabilities. | **Low direct fit** for a brief fictional text exchange; trust in physical robot performance differs from reliance on a short answer. | Retain task-specific TR1 as exploratory and unvalidated; review HRI instruments only for conceptual guidance. |

## What can be concluded from source inspection

1. Gray et al. provide a **two-dimensional mind-attribution framework**, not proof that AI has subjective experience. Their original research compared diverse characters rather than testing first-person pronouns in LLM responses.
2. IDAQ is best viewed as a **person-level moderator candidate**. Its questions may expose consciousness concepts before stimulus presentation and thereby alter participants' judgments.
3. Godspeed contains overlapping anthropomorphism/animacy content and robot-specific features. Using its full score with text-only AI would threaten content validity.
4. Robot trust measures do not automatically validate a task-specific chatbot trust item. A separate text-based conversational-agent trust review is warranted.
5. A scale being published, or its items appearing online, **does not establish permission for redistribution or validity after adaptation**. Seek author/publisher clarification when necessary.

## Proposed construct-to-item mapping (original draft items only)

| Role | Construct | Current item ID | Status |
|---|---|---|---|
| Primary | Attributed agency | AG1 | Original, single-item candidate; **not validated** |
| Supplementary | Attributed agency | AG2, AG3 | Original candidates; AG3 risks leading wording |
| Exploratory | Attributed subjective experience | EX1, EX2 | Original candidates; avoid equating with actual AI experience |
| Exploratory | Anthropomorphism | AN1 | Original candidate; not IDAQ or Godspeed |
| Exploratory | Task-specific trust | TR1 | Original candidate; not TPS-HRI |
| Diagnostic | Helpfulness, naturalness, authority, clarity | HP1, NA1, AU1, CL1 | Original checks for possible confounds |
| Manipulation check | First-person reference recognition | MC1 | Original check; do not use for unplanned exclusions |

The lab should **not** calculate a single 'AI consciousness score' from these different constructs.

## Required validation and decision gates

**Gate 1 — Literature/permissions:** obtain full methods, scoring, validity evidence, intended populations, and any adaptation/reproduction permissions. Identify more recent **text-chatbot/LLM** measures; include conflicting findings. Log exact retrieval and permission status.

**Gate 2 — Independent expert item review:** at least two qualified reviewers map items to constructs and flag competence/agency overlap, leading phrasing, and readability. This is a proposed review step, not completed work.

**Gate 3 — Cognitive interviewing and stimulus pretesting:** only after applicable ethics determination and consent planning. Evaluate how people interpret 'goal-directed decisions' and 'subjective experiences' and whether wording changes authority, warmth, and helpfulness. Set decision criteria prospectively.

**Gate 4 — Psychometric and preregistration gate:** select primary outcome and scoring, sample-size rationale, analysis, missingness and exclusion rules; evaluate construct separation and scenario effects. Single-item AG1 cannot have internal-consistency reliability estimated.

**Gate 5 — Human recruitment:** only after relevant institutional/jurisdictional ethics review and a data-management plan. No participant data in public GitHub.

## References and source links (checked 2026-11-23)

- Gray, H. M., Gray, K., & Wegner, D. M. (2007). *Dimensions of mind perception*. *Science*, 315, 619. https://doi.org/10.1126/science.1134475 ; author-hosted article: https://dtg.sites.fas.harvard.edu/DANWEGNER/pub/Gray%2C%20Gray%2C%20%26%20Wegner%20%282007%29.pdf
- Waytz, A., Cacioppo, J., & Epley, N. (2010). *Who sees human?* *Perspectives on Psychological Science*, 5, 219–232. https://doi.org/10.1177/1745691610369336 ; author materials: https://www.adamwaytz.com/measures-and-materials/individual-differences-in-anthropomorphism-questionnaire-idaq
- Bartneck, C., Kulić, D., Croft, E., & Zoghbi, S. (2009). *Measurement instruments for the anthropomorphism, animacy, likeability, perceived intelligence, and perceived safety of robots*. *International Journal of Social Robotics*, 1, 71–81. https://doi.org/10.1007/s12369-008-0001-3
- Schaefer, K. E. (2016). *Measuring trust in human robot interactions: Development of the Trust Perception Scale–HRI*. In *Robust Intelligence and Trust in Autonomous Systems*. See https://hriscaledatabase.psychology.gmu.edu/trust/2024/10/31/trustschaefer.html
- HRI Scale Database: https://hriscaledatabase.psychology.gmu.edu/mind/agency%20perception/2025/01/06/GGW.html and https://hriscaledatabase.psychology.gmu.edu/attitudes/attributes/2024/10/31/Godspeed.html

**Verification boundary:** Sources were inspected for their stated constructs, original populations, and available instrument descriptions. This review does not claim independent replication of factor analyses, inspection of every supplementary file, or license clearance.
