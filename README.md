# Project 1 — Eli Lilly valuation workbench

**Linda Li · FIN 43900 · Individual project · AI-assisted review package**

**Proposed decision: watch/defer.** Five-year statements feed an FCFF DCF, causal cases, sensitivity and a reverse DCF. Qualified MRK/PFE P/E and approximate EV/revenue supply market cross-checks. The locally runnable interface has bounded controls, base reset, live statements/value, and an intentional failing-check demonstration.

**Status: not yet ready for final Brightspace submission.** Edition A and the corrected assumption review are confirmed by Linda; the human AI-off prediction and three actual recordings/transcripts remain incomplete. See [remaining actions](docs/student-actions.md). No receipt, pre-run prediction, video or partner interaction is invented.

## Run

Python **3.10+**; standard library only for the tool, valuation and tests. No account, API key or network required.

```sh
python model.py
python peers.py
python -m unittest -v
python app.py
```

Open **http://127.0.0.1:8000** in your browser. Change a driver; compare with restored base; reset. Click **Demonstrate broken check**, then reset to recover. The simulated corruption demonstrates that accounting is locked; it does not rewrite saved data. Stop server with Ctrl+C.

Core dependencies: none. Optional PDF regeneration uses ReportLab (`python -m pip install reportlab`, then `python prepare_submission.py`). Included PDFs can be opened without that package. Run commands from this repository root.

## Inspect without running

- [Executed results and statements](output/visible_output.md), [full JSON](output/visible_output.json), [peer calculations](output/peers.json).
- [Decision memo](submission/Decision-Memo.pdf) — within two-page limit.
- [Research evolution](submission/Research-Evolution.pdf) — original memo preserved, checkpoint role and baseline match confirmed by Linda.
- [Validation and AI use](submission/Validation-and-AI-Use.pdf).
- [Source ledger](docs/source-ledger.md), [assumption challenges](docs/assumption-challenges.md), [historical mapping](docs/historical-source-map.md).
- [Tests](output/tests.log), [cold run](output/cold-run.log), [workbench API verification](output/interface-check.log).
- [Video rehearsal guides](docs/video-1-rehearsal.txt), [Video 2](docs/video-2-rehearsal.txt), [Video 3](docs/video-3-rehearsal.txt). These are not transcripts of recordings.
- [Submission manifest](submission/submission-manifest.csv), [remaining actions](docs/student-actions.md).

## Finance architecture

FY2025 actual balances initialize the statement engine; FY2026 is a modeled bridge, followed by five full annual forecasts **2027–2031**. September 8, 2026 year-end timing discounts only remaining cash flows. The bridge proportionally approximates remaining operating cash flow and excludes business acquisitions already paid in H1. Latest reported June cash/investments/debt supply the enterprise-to-equity bridge; they are not rolled to the price date.

All money is USD millions; shares millions; per-share USD. FCFF is EBIT minus unlevered cash tax plus D&A minus capex/change in operating NWC/capitalized business acquisitions. Purchased IPR&D is retained as expense/cash cost exactly once. Interest and financing flows are removed. Terminal growth reinvests g/20% incremental ROIC. Negative explicit FCFF is retained. Valuation checks reject incoherent inputs; there is no cash plug.

`legacy_statements.py` preserves the inherited Lab 10 engine for traceability. Its legacy `main`/FCFE valuation is not Project 1's final result. Use **model.py**. Original lab outputs are not merged or averaged.

WACC is a scenario required return rather than independently estimated CAPM; dilution uses an EPS weighted-average proxy. Operating leases remain expensed; additional debt-like claims are not independently modeled. Peer EV uses consistently disclosed FY2025 diluted-average shares and year-end book balances, so it approximates capitalization. Do not interpret spending cuts as free improvement: aggregate growth and fixed expense ratios omit clinical/capacity feedback. These limitations matter to the recommendation.

## Evidence and authorship

Original work reused from public llindali repositories lab4, lab8, lab10, lab11 and LLY---research. This build was AI-assisted in Codex/GPT-6 on October 6, 2026; finer model build version not exposed. Prior models' exact interaction versions/dates remain to confirm. Linda is responsible for review and final judgment. See Validation-and-AI-Use for material dispositions and independent checks.

Linda confirmed that the supplied Lab 03 screenshot serves as Edition A checkpoint evidence; see evidence/edition-a-confirmation.md. The locked-test script refuses missing/uncommitted human prediction; no retrospective account replaces it. Video transcripts must reflect actual recordings. The public checkpoint screenshot shows assignment results and no account identifiers; personal partner contact addresses are excluded.

## Part 2 verification
[Corrected R&D reconciliation](docs/Part-2-Reconciliation.md): AI-assisted 20% to 17% exploratory stress test yields $810.23/share, not the earlier proposed $851.07. Normal model bounds remain 18%–24%. Prediction provenance and actual freeze/execution times are disclosed; no human AI-off execution is claimed.
