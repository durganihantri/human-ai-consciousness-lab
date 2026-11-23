# Reproducibility and Release Checklist — Draft v0.3

**Status:** technical prototype only; not preregistered, validated, or approved for human recruitment.

## Reproduce the technical work

1. Use Python 3.10+ (standard library only).
2. From the repository root, run `python -m unittest discover -s tests -v`.
3. Run `python analysis/synthetic_pipeline.py --output /tmp/hacl-demo` to generate **synthetic** records and descriptive summaries.
4. Open `experiments/01a-first-person/offline-prototype/index.html` in a browser that executes local JavaScript, or use `python -m http.server 8000` at repository root and visit `http://localhost:8000/experiments/01a-first-person/offline-prototype/`. Local HTTP server is a convenience, not a participant-facing deployment.

## Before public prototype announcement

- [ ] Verify tests pass on the current commit in GitHub Actions.
- [ ] Manually test the browser flow in Safari, Chrome, and one desktop browser; log browser versions and failures.
- [ ] Confirm no analytics, external scripts, forms posting to servers, or persistent storage.
- [ ] Verify stimuli and question wording are labeled unvalidated.
- [ ] Review accessibility (keyboard navigation, contrast, screen-reader labels).
- [ ] Decide and document separate software and documentation licenses; **none are granted by default**.
- [ ] Update the root README with current status and links only after checks pass.

## Before any real human-participant study

- [ ] Obtain applicable ethics review/determination and approved consent/privacy materials.
- [ ] Independently review stimulus equivalence and measurement construct validity.
- [ ] Justify sample size, primary outcome, exclusions, missing-data rules and analysis plan.
- [ ] Preregister confirmatory work where appropriate.
- [ ] Build and review secure data collection; this demo does not qualify.

**Interpretation:** the project measures *human attributions*, not actual AI consciousness. Synthetic results are engineering fixtures, not scientific findings.
