# Part 2 — R&D sensitivity and reconciliation
Executed October 6, 2026 by Codex at Linda’s request. Linda reports that she wrote the prediction without AI. Execution, verification and this corrected reconciliation are AI-assisted. This is not attested as an AI-off locked exercise.

## Frozen record and execution
Prediction record: evidence/rd-prediction-record.json. Actual pre-execution GitHub freeze: 9d9ee9f84199a3a0c6c141676656650a0876c511. Execution: 2026-10-06T17:51:30.529547+00:00. The reported earlier prediction time is retained as user-reported, not a backdated Git commit. Linda had already supplied proposed $851.07 results before this run; this is verification, not an unseen prediction test.

Input rd_ratio: 0.20 to 0.17 (fraction of revenue). All other exposed parameters and enterprise-to-equity bridge remain fixed. The ordinary model correctly refused 17%, outside its 18%–24% bounds. assisted_test.py extends only its in-process exploratory range and restores it afterward. Production bounds and locked_test.py remain unchanged.

## Actual results
| Metric | Base | 17% exploratory stress | Change |
|---|---:|---:|---:|
| Enterprise value, USD bn | 716.126 | 766.205 | +50.079 |
| Equity value, USD bn | 674.024 | 724.103 | +50.079 |
| Value per share, USD | 754.19 | 810.23 | +56.04 (7.43%) |
| Gap to $1,123.91 reference | -32.90% | -27.91% | 4.99 percentage points |
| Terminal share of EV | 78.36% | 78.01% | |

## Prediction versus result
Direction matched: lower recurring R&D mechanically increases operating income and after-tax cash flow. Magnitude did not match the predicted $820–$880 range: $810.23 is $9.77 below its lower bound. The earlier supplied $851.07 and $802.7bn EV are not reproduced and are superseded by the generated JSON. All monetary model inputs are USD millions except per-share values.

The gain is $56.04/share rather than the supplied $97.07. Lower research spending benefits after-tax cash flow; the actual forecast margins, terminal reinvestment convention and discounting determine the magnitude. No unexplained numerical result is accepted as executed evidence.

## Decision effect
Watch/defer remains the supplied stance: the changed estimate is still 27.91% below the reference. If the revised valuation were accepted, a proposed 20% discount implies $648.18, rather than the original approximately $603. The entry policy is conditional, not a confirmed committee mandate.

## Model insight and limitations
Recurring research is expensed. Cutting it increases modeled cash flow without an explicit penalty to pipeline productivity or future revenue. This is mechanical sensitivity, not evidence that an R&D cut creates durable economic value. The test shows only that this expense change does not close the gap under the other fixed assumptions. It does not prove the source of the market premium. The original 9.62-percentage-point growth hurdle applies to the original assumptions and has not been recalculated here.

## Requirement disposition
AI-assisted sensitivity, freeze record, failure diagnosis/recovery and corrected reconciliation are complete. No human AI-off execution is claimed. If the course requires the separately documented AI-off procedure, this assisted run does not itself establish compliance; retain that distinction in the final submission.
