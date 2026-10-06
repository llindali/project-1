# Validation and AI use — review package
Decision/user: investment committee; proposed watch/defer. Valuation cutoff September 8, 2026. Build date October 6, 2026. Exact code commit and output hashes are recorded in the repository and submission manifest after freeze.

## Finance conventions
USD millions and shares millions. Five full forecasts 2027–2031, proportional 2026 operating bridge; business-acquisition cash already spent in H1 excluded from stub. No negative FCFF clipping. FCFF = EBIT - unlevered cash tax + D&A - capex - change in operating NWC - capitalized acquisitions. Purchased research is already deducted in EBIT; no second cash deduction. Tax uses inherited 20% before nondeductible IPR&D, with the exact tax difference used to reconcile equity-side cash. Terminal NOPAT grows at g with reinvestment g/20% ROIC. June cash plus noncurrent investments minus debt; investments book-value/distributable assumption. Operating leases retained in expense; no separate verified pension adjustment. DCF Q2 diluted proxy differs from FY2025 diluted proxies used consistently in approximate peer EV.

## Validation register
- Published synthetic fixture independently reproduced: NOPAT 112.5, FCFF 77.5; EV 1,000 + cash 100 - debt 250 - NCI 20 - pension 10 = common equity 820; /100 shares = $8.20.
- Annual base-year mapping: assets 112,476 = liabilities plus equity 112,476; cash 7,268, inventory 13,744. Full mapping in historical-source-map. No cash plug.
- Six annual statement sets: balance sheet, cash roll-forward, CFO/CFI/CFF, PP&E/intangible/debt/equity checks; gaps below $0.01m. FCFF reconciles to CFO + CFI + interest + levered tax - unlevered tax.
- Directional checks: WACC 8% to 10% lowers value; higher bounded growth increases value; terminal growth 2% to 3% increases value at fixed ROIC. Automated tests written before execution by AI; these DO NOT count as the human locked prediction.
- Bridge: EV + cash + investments - debt = equity; positive shares; reverse DCF reprices snapshot within numerical tolerance.
- Highest-risk tests: incoherent perpetuity refused; corrupted cash causes balance/cash checks to fail; out-of-bound assumptions refused. Negative explicit FCFF remains a cash funding cost.
- Peer definitions: positive denominators; FY2025 GAAP EPS/revenue consistently used; annual diluted averages and book balances marked approximate; MRK/PFE differences qualified. Enterprise and equity multiples not averaged.
- Independent definition check: non-GAAP performance margin is not EBIT; direct Q2 primary filing verifies 893.7m Q2 dilution and 7,050 + 47,858 = 54,908 debt.
- Cold run: fresh environment without packages, regenerated model/peer outputs and tests; see output/cold-run.log. HTTP workbench API base/change/error recovery tested separately. Linda still must record her demonstration.

## Locked Changed-Input Record — INCOMPLETE
No AI-generated or retrospective prediction is claimed. `locked_test.py` refuses to execute without a complete committed human-prediction.json. Linda must write her own prediction with AI off, freeze it before the run, execute with AI off, and add actual output/decision effect plus reconciliation. Existing Lab 11 admits no timestamped pre-run record. No prior record is fabricated.

## Named AI use
| Tool / exposed model | Date | Material contribution | Check | Disposition |
|---|---|---|---|---|
| Codex / GPT-6, Work mode; finer build version not exposed | October 6, 2026 | Integrate statements with FCFF, timing, interface, tests, peer EV/revenue, prose/scripts | Primary LLY/MRK/PFE filings; manual synthetic arithmetic; accounting identities; clean run | Proposed accept/modify, pending Linda review |
| Prior Codex assistance; exact model/version not recorded in old README | Prior labs, actual interaction dates to confirm | Standalone DCF, statements, P/E and sensitivity documentation | Existing source trails and rerun outputs; no invented version/date | Qualified as inherited work |
| Prior Lab 4 short-term investment claim ($60m) | Reviewed October 6 | Extra asset in EV bridge | Q2 balance sheet shows only cash/current assets and 3,856 noncurrent investments; no separate line | Rejected as unsupported addition; integrated bridge omits it |

The independent evidence proves particular inputs/definitions, not all judgments. Passing AI-authored tests is not proof that the economic forecast is true. Linda remains responsible for sources, personal confirmations, originality boundary and explaining the system.

## Limits and stop rules
Terminal EV share 78.4%; WACC scenario rather than independently estimated CAPM. September 8 market closes were independently rechecked October 6; personal model/assumption review remains required. Product demand, pricing and capacity lack a separate causal patient model. Spending cuts do not alter modeled clinical/capacity success. Fixed margins include D&A so capex does not directly change modeled EBIT. Simplified acquisitions, fixed tax/other claims, liquidity backstop, year-end/proportional timing, average-share proxies and nonoperating investments constrain accuracy. Stop issuing a valuation if accounting, funding, domain or perpetuity checks fail; reconsider the action when downside evidence is corroborated.
