# Lab 08 — Lilly peer P/E and DCF comparison

**Target:** Eli Lilly (NYSE: LLY). **Comparison date:** September 8, 2026. **Conditional call: watch-defer.** The two qualified peers imply **$468.02–$468.96 per LLY share**, versus the saved DCF scenario range of **$437.42–$1,394.70** (base $826.63). The narrow peer range does not establish fair value.

## Company and initial policy

Lilly earns revenue from developing and selling medicines. R&D, clinical approvals, patent protection, manufacturing capacity and payer access determine the returns from successful products. Mounjaro and Zepbound are major growth drivers. Reported FY2025 diluted EPS is positive at $22.95. Sources: [Lilly 2025 10-K][lly10k], Item 1, Business, and Item 7, Revenue by Product; [annual results][lly], diluted EPS table.

**Initial policy, retained without revision:** investigate listed operating companies whose main economics involve commercial prescription medicines, proprietary research, regulatory approval and finite exclusivity. Qualify differences in therapeutic mix, growth, geography, leverage, acquisitions and non-human-health exposure. Exclude businesses dominated by distribution, insurance, devices, generics or pre-revenue research. Nonpositive reported annual EPS or an unverifiable price prevents a numerical peer estimate; it does not erase the candidate investigation. Use the latest full-year reported GAAP diluted EPS available by the comparison date, with USD prices per U.S. common share. Do not substitute adjusted EPS or annualize a quarter.

Focused research question: do Merck and Pfizer share enough of Lilly's drug-development economics for their reported earnings multiples to be informative despite different product growth and earnings charges? Evidence of predominantly different operations, incompatible share bases or unusable earnings would reject a candidate. Similar brand recognition alone would not admit one.

This is an AI-assisted policy and analysis prepared for student review. It does not claim that the required before-AI policy, two independent AI conversations, or partner discussion occurred.

## Two candidate decisions

| Candidate | Decision | Opened primary-source evidence and section | Important difference and reasoning |
|---|---|---|---|
| Merck & Co. (NYSE: MRK) | Qualify; include | [FY2025 release][mrk], “Fourth-Quarter Sales Performance,” “Animal Health,” and “Research and Development Update”: commercial medicines/vaccines and an active development pipeline. | KEYTRUDA concentration and animal health differ from Lilly's incretin-led growth. The shared medicine-development model supports a qualified comparison, not an equal-growth assumption. |
| Pfizer (NYSE: PFE) | Qualify; include | [FY2025 release][pfe], “Quarterly Financial Highlights” (pp. 4–5), “Capital Allocation” (p. 3), and product revenue tables: medicines/vaccines and continuing R&D. | COVID-product declines and earnings charges weaken comparability. Positive annual reported EPS permits calculation, but the reported-versus-adjusted gap makes the multiple sensitive to earnings quality. |

Neither candidate is excluded; both require qualification. SEC 10-K starting points were also located for [Merck][mrk10k] and [Pfizer][pfe10k], Item 1 and the consolidated income/EPS statements. Their full SEC pages failed to load in this research session, so the decisions above rely on the opened company earnings releases, not an assertion that those 10-Ks were fully reviewed.

## Inputs and source trail

All EPS below cover **January 1–December 31, 2025**, the latest completed annual period public by September 8, 2026. All prices are the **September 8, 2026 Close** column, USD per NYSE common share. These are neither ADR prices nor dividend-adjusted total-return values; the EPS and price use the common-share basis.

| Company | Closing price and source | FY-end | Reported diluted EPS | Publication date; EPS source locator | Adjusted EPS, excluded from calculator |
|---|---|---|---:|---|---:|
| LLY | [$1,123.91][llyprice] | 2025-12-31 | $22.95 | 2026-02-04; [release][lly], “Consolidated Statements of Operations,” twelve months, diluted EPS | $24.21 |
| MRK | [$148.46][mrkprice] | 2025-12-31 | $7.28 | 2026-02-03; [release][mrk], “Financial Summary,” year ended Dec. 31, GAAP EPS; text specifies assuming dilution | $8.98 |
| PFE | [$27.79][pfeprice] | 2025-12-31 | $1.36 | 2026-02-03; [release][pfe], “Overall Results,” full-year reported diluted EPS; footnote 2 defines GAAP attributable to common shareholders | $3.22 |

Started at Nasdaq historical pages for [LLY](https://www.nasdaq.com/market-activity/stocks/lly/historical), [MRK](https://www.nasdaq.com/market-activity/stocks/mrk/historical) and [PFE](https://www.nasdaq.com/market-activity/stocks/pfe/historical); each returned “Data is currently not available.” The opened ChartExchange historical tables above supplied the dated closes. Sources accessed September 15, 2026; later price rows and later earnings are not inputs.

## Run and validate

[pe.py](pe.py) reuses the Lab 07 standard-library calculator with only Lilly and the two qualified peers. Edit inputs at the top; no packages or live data fetching. From the existing `LindaLi` course folder:

```powershell
.\.venv\Scripts\python.exe .\lab8\pe.py
```

From this repository alone, `python pe.py` also works.

| Calculation | Verified output |
|---|---:|
| LLY own P/E | 48.972113x |
| MRK P/E | 20.392857x |
| PFE P/E | 20.433824x |
| Peer median | 20.413340x |
| LLY implied minimum / median / maximum | $468.02 / $468.49 / $468.96 |
| Remove PFE: MRK reference; change from full estimate | $468.02; −$0.47 |
| Remove MRK: PFE reference; change from full estimate | $468.96; +$0.47 |

Independent arithmetic: `148.46 / 7.28 = 20.392857142857...`; multiplying by Lilly's `22.95` gives `$468.016071428571...`. With two peers, the median is the arithmetic midpoint of their multiples. Values remain unrounded until display.

Directional prediction: removing the higher-multiple PFE lowers the estimate. The leave-one-out output confirms a $0.47 decline. One remaining peer provides a reference, not a range; removing that sole usable peer leaves no estimate. Both peers stay admitted because this sensitivity is not new business evidence. Their very similar multiples explain the small change, not high confidence in Lilly's value. Invalid inputs, target exclusion, deduplication and one/zero-peer behavior were checked.

## Compare with the saved DCF

| Method | Lilly result and date | Main assumption or limitation |
|---|---|---|
| Saved course DCF | September 8, 2026: bear $437.42, base $826.63, bull $1,394.70 | Forecast growth, margins, reinvestment and discount rates; about 79.1% of base enterprise value is terminal value. |
| Peer P/E | September 8, 2026 close: $468.02–$468.96; median $468.49 | Transfers two qualified peers' FY2025 GAAP multiples to Lilly despite different growth and earnings quality. |

DCF provenance: existing [lab4 model](https://github.com/llindali/lab4/blob/main/valuation/dcf.py), [inputs](https://github.com/llindali/lab4/blob/main/valuation/inputs.json) and [analysis](https://github.com/llindali/lab4/blob/main/README.md). This is the available saved model, labeled Lab 4; a distinct Week 3 artifact was not identified. Base assumptions include 2027–31 revenue growth of 25%, 20%, 15%, 10%, 7%; 9% WACC; 3% terminal growth; and continued capital and working-capital investment. Bear/bull scenarios change growth, margins and discount assumptions together.

Both results value LLY common equity per share. The DCF forecasts future unlevered cash flows and then bridges enterprise value to equity. P/E applies an equity multiple directly to earnings: no cash/debt bridge. Its backward-looking earnings basis differs from the DCF forecast. Lilly's faster expected growth can explain a higher DCF without proving either estimate correct.

The saved DCF's market reference is $1,124.01 at 15:30:26 EDT; this lab uses $1,123.91 at the same day's close. The $0.10 timing difference is disclosed, not silently treated as identical. The DCF valuation and saved scenarios are unchanged.

## Skeptical review and conditional judgment

**AI criticism:** the weakest assumption is that similar drug-development economics justify transferring these historical multiples to Lilly. Pfizer's $1.36 reported EPS versus $3.22 adjusted EPS highlights denominator sensitivity; two nearly equal multiples cannot establish a tight fair-value interval. Also distinguish the saved Lab 4 artifact from the requested Week 3 provenance, and historical GAAP EPS from normalized forecast cash flows.

**Source-checked response (proposed for student review): accept.** Pfizer's “Overall Results” verifies the EPS gap; Lilly's 10-K product-revenue table shows the importance of Mounjaro and Zepbound. The DCF files verify a forward forecast and terminal-value dependence. These support qualifying the comparison and withholding a narrow fair-value claim. **Unresolved:** whether this saved model is the instructor's intended Week 3 submission. No range is invented or mechanically averaged.

**Skeptical question:** what evidence would justify paying Lilly's roughly 49x reported earnings when these peers trade near 20x?

**Answer and call: watch-defer.** A defensible premium needs evidence of durable incremental cash generation: prescription demand translating into revenue after discounts, capacity coming online, sustained margins after R&D, and enough pipeline success to replace declining products. The current comparison alone does not quantify that premium. The saved DCF's $437.42–$1,394.70 is an assumption-dependent scenario range; $468.02–$468.96 is a conditional peer calculation. I withhold a single combined fair-value range. Evidence of durable growth and cash conversion sufficient to support the price in a DCF with explicit reinvestment would most readily change this call; weaker demand, pricing or pipeline evidence would weaken it. Carry those questions into Week 5.

[lly10k]: https://www.sec.gov/Archives/edgar/data/59478/000005947826000013/lly-20251231.htm
[lly]: https://investor.lilly.com/news-releases/news-release-details/lilly-reports-fourth-quarter-2025-financial-results-and-provides
[mrk]: https://www.merck.com/news/merck-highlights-progress-advancing-broad-diverse-pipeline/
[pfe]: https://www.sec.gov/Archives/edgar/data/78003/000007800326000005/pfe-12312025xex99.htm
[mrk10k]: https://www.sec.gov/Archives/edgar/data/310158/000031015826000063/mrk-20251231.htm
[pfe10k]: https://www.sec.gov/Archives/edgar/data/78003/000007800326000026/pfe-20251231.htm
[llyprice]: https://chartexchange.com/symbol/nyse-lly/historical/
[mrkprice]: https://chartexchange.com/symbol/nyse-mrk/historical/
[pfeprice]: https://chartexchange.com/symbol/nyse-pfe/historical/
