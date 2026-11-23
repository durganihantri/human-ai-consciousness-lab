# Synthetic Data Dictionary v0.1

The synthetic pipeline generates **invented records** for software testing only. These are not observations, participant responses, effect estimates, or a demonstration of the hypothesis.

| Field | Type | Meaning |
|---|---|---|
| `record_type` | string | Always `synthetic_test_only` |
| `test_id` | string | Non-identifying generated test label |
| `pair_id` | string | A01/A02/A03 scenario |
| `condition` | string | `impersonal` or `first_person` |
| `AG1` | integer 1–7 | Artificially generated agency rating |
| `EX1` | integer 1–7 | Artificially generated experience rating |
| `AN1` | integer 1–7 | Artificially generated anthropomorphism rating |
| `TR1` | integer 1–7 | Artificially generated task trust rating |

The generator intentionally samples ratings independently of condition. Do not use these records to infer a real effect, statistical power, or instrument reliability. No personal identifiers, timestamps, IP addresses, or browser fingerprints are generated.
