# API Repository Review

Repo: `Seedance-2.0-Gateway-Service`
Review date: 2026-06-14
API family: Seedance 2.0 video generation
Primary endpoint: `POST /v1/videos/generations`
Review mode: API repo audit + fix

## 1. Developer First-Run Verdict

- Can a developer get a key quickly? Yes.
- Can they run the first request in under 5 minutes? Yes after switching examples to `EVOLINK_API_KEY`.
- Can they retrieve the final asset without guessing? Fixed by adding complete-flow examples and response schema docs.
- Main blocker found: existing examples stopped after task creation and stale availability copy conflicted with "Now Available".

## 2. API Repo Template Compliance

| Area | Status | Notes |
|---|---|---|
| Quickstart | Fixed | README now points to complete flow and should use env-based auth |
| Complete async flow | Fixed | Added cURL, Python, and JavaScript complete-flow examples |
| Auth | Fixed | English and localized public code snippets now use `EVOLINK_API_KEY` |
| Request schema | Pass | Existing mode docs cover request fields |
| Response schema | Fixed | Added `docs/response-schema.md` |
| Error handling | Fixed | Added `docs/errors.md` |
| Callback/webhook | Fixed | Added `docs/callbacks.md` |
| Runnable examples | Fixed | Added complete-flow scripts |
| Pricing | Pass | Existing pricing section and docs cover formulas |
| Model/workflow choice | Pass | Existing comparison tables are useful |
| Production notes | Partial | URL expiry and regional availability exist; retry/backoff now covered in errors docs |
| Translations | Fixed for code/state drift | Public auth snippets and availability callouts were synced; natural-language localization QA can be done later |

## 3. Remaining Follow-Up

- Run a dedicated localization QA pass later if wording quality matters across all translated docs.
- Point "Read API Docs" to a Seedance-specific docs URL when a canonical public page exists.
