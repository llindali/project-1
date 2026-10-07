# Partner discussion record

Linda Li reports an in-person discussion with Annika Rao on October 7, 2026. Company: Eli Lilly. Valuation date: September 8, 2026. Starting and concluding recommendation: watch/defer. This is an edited summary of Linda’s supplied notes, not a verbatim transcript or an independently witnessed meeting.

## Partner’s challenge
Annika challenged a constant 20% recurring R&D ratio: at approximately $174.6bn of 2031 revenue, this implies approximately $34.9bn recurring R&D plus $4bn acquired IPR&D. She asked whether the model understates operating leverage as established products scale. She proposed 17%, with a discussion range of 16%–18%.

Linda reports that Annika cited mature-pharma peer R&D leverage and possible Lilly scale benefits. The claimed Merck/Pfizer 15%–18% benchmarks have not been independently sourced here. Peer years, recurring versus acquired research definitions, and commercial/pipeline differences require verification before using those percentages as forecast evidence. Product approval/commercial status was not established by this discussion.

## Linda’s response
Linda partly accepted the possibility of R&D leverage, but retained 20% in the base because sustained pipeline replacement and competition may require substantial research investment. Lower expense mechanically raises model margins without reducing future growth or pipeline productivity; it is not evidence that cutting research creates durable value. Specific patent timing requires primary-source verification.

Linda referred to the original reverse DCF: one conditional solution adds 9.62 percentage points to each 2027–2031 growth rate, reaching approximately $260.9bn revenue with other original assumptions fixed. That hurdle is not the market’s unique forecast and was not recalculated at 17% R&D.

## Sensitivity evidence and correction
Exact model input: rd_ratio. Units: fraction of revenue. Base 0.20; exploratory change 0.17. Other exposed inputs and the EV bridge held fixed.

The verified October 6 sensitivity, available before this October 7 discussion, produced $754.19 to $810.23/share: +$56.04 (+7.43%). Changed EV was $766.205bn and equity $724.103bn. The estimate remained 27.91% below the $1,123.91 reference. See output/rd-assisted-test-result.json and docs/Part-2-Reconciliation.md.

Linda’s supplied discussion notes instead listed $851.07 and described a locked-protocol execution. Those claims are not supported by the verified record and are corrected here. The actual run was the previously documented assisted exploratory stress, including normal refusal at 17% and an isolated range extension. Ordinary interface bounds remain 18%–24%; 16%–18% was a proposed discussion range, not a newly executed range sweep. No separate October 7 execution record was supplied.

## Range discussion
Linda reports that she and Annika regarded growth as the main concern. This is their qualitative conclusion, not a verified cross-driver ranking. A single R&D change does not show how changing tested range widths affects rankings. Driver importance must be compared using stated, defensible ranges and actual output spans. The discussion does support that this particular R&D reduction alone fails to close the valuation gap.

## Outcome and reconsideration conditions
Linda retained the 20% base and watch/defer recommendation. The 17% case remains an explicit exploratory appendix sensitivity; production assumptions and controls are unchanged.

The proposed original 20% discount to base is approximately $603. If adopting the $810.23 stress valuation instead, the corresponding discount is $648.18; it is a conditional analyst policy, not a verified committee requirement. A lower price warrants reconsideration only with intact fundamentals. Stronger demand, realized pricing, cash conversion and supported pipeline economics could also justify rebuilding the forecast; clinical success alone does not prove manufacturing yields, access or cash margins.

## Follow-up evidence and model improvements
- Verify peer R&D benchmarks from filings with consistent research definitions and years.
- Check reported net pricing, product sales, inventory and manufacturing disclosures; do not treat clinical phase 3 updates as direct manufacturing-yield evidence.
- Separate patient/volume/net-price forecasts by product or indication, with clinical probabilities and competitive/patent scenarios.
- Investigate a defensible relationship between research spending and future pipeline productivity rather than an arbitrary decay curve.
- Test driver rankings over clearly documented ranges before claiming their stability.
