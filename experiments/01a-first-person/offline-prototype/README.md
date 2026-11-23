# Experiment 01A — Offline Demo v0.2

**For software demonstration only.** This prototype uses fictional prompts, draft unvalidated questions, and locally entered test ratings. It sends nothing to a server and has no storage, consent, recruitment, or data-management functionality. Do not deploy it as a participant survey.

## Run

Open `index.html` in a browser that supports JavaScript, or from the repository root run `python -m http.server 8000` and open `http://localhost:8000/experiments/01a-first-person/offline-prototype/`.

On iPad, the Files quick-look preview may display HTML but block scripts. A full browser or a hosted static preview may be necessary. The demo now uses a fallback if `crypto.getRandomValues` is unavailable, but **this has not been manually tested on iPad**.

## Known limitations

- Three scenario pairs are candidate stimuli, not validated or fully confound-matched.
- Random selection is a technical demo, not a validated experimental allocation procedure.
- Ratings are manually entered test values, not real or synthetic scientific evidence.
- No analytics, downloads, personal-data collection, or external dependencies.
- The original v0.1 demo remains available in Git history; v0.2 replaces the local HTML file after review.

