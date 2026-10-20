# Range-ranking comparison

Rank by absolute low-to-high endpoint output span; one driver changes at a time; all others restored to BASE. Tied spans do not imply an economically meaningful ordering.

Original ranges match saved own-model sensitivity. Narrow-growth range is a controlled local comparison, not a confidence interval. Wider R&D/inventory ranges use existing model bounds as exploratory stresses, not independently established probabilities.

All values are model results, not evidence that the economic assumptions are true.

## original

| Driver | Low | High | 2031 EBIT span, $m | 2031 FCFF span, $m | Value/share span, $ |
|---|---:|---:|---:|---:|---:|
| growth_shift | -0.05 | 0.05 | 37,237.12 | 21,003.88 | 328.81 |
| rd_ratio | 0.18 | 0.22 | 6,984.32 | 5,587.45 | 74.71 |
| capex_shift | -0.02 | 0.02 | 0.00 | 5,406.45 | 21.69 |
| inventory_shift | -50.0 | 50.0 | 0.00 | 724.27 | 4.58 |

profit_2031: growth_shift > rd_ratio > capex_shift > inventory_shift

fcff_2031: growth_shift > rd_ratio > capex_shift > inventory_shift

per_share: growth_shift > rd_ratio > capex_shift > inventory_shift
## narrow_growth

| Driver | Low | High | 2031 EBIT span, $m | 2031 FCFF span, $m | Value/share span, $ |
|---|---:|---:|---:|---:|---:|
| growth_shift | -0.005 | 0.005 | 3,709.87 | 2,094.54 | 32.77 |
| rd_ratio | 0.18 | 0.22 | 6,984.32 | 5,587.45 | 74.71 |
| capex_shift | -0.02 | 0.02 | 0.00 | 5,406.45 | 21.69 |
| inventory_shift | -50.0 | 50.0 | 0.00 | 724.27 | 4.58 |

profit_2031: rd_ratio > growth_shift > capex_shift > inventory_shift

fcff_2031: rd_ratio > capex_shift > growth_shift > inventory_shift

per_share: rd_ratio > growth_shift > capex_shift > inventory_shift
## wide_rd_inventory

| Driver | Low | High | 2031 EBIT span, $m | 2031 FCFF span, $m | Value/share span, $ |
|---|---:|---:|---:|---:|---:|
| growth_shift | -0.05 | 0.05 | 37,237.12 | 21,003.88 | 328.81 |
| rd_ratio | 0.18 | 0.24 | 10,476.48 | 8,381.18 | 112.07 |
| capex_shift | -0.02 | 0.02 | 0.00 | 5,406.45 | 21.69 |
| inventory_shift | -50.0 | 100.0 | 0.00 | 1,086.41 | 6.86 |

profit_2031: growth_shift > rd_ratio > capex_shift > inventory_shift

fcff_2031: growth_shift > rd_ratio > capex_shift > inventory_shift

per_share: growth_shift > rd_ratio > capex_shift > inventory_shift

## Interpretation

These comparisons explicitly test range dependence. Narrowing growth changes its measured span without changing the model or investment evidence. Compare the recorded ranks rather than asserting a universal dominant driver. EBIT ignores the capex/inventory changes because these inputs have no direct feedback into the fixed operating-margin path; their zero EBIT spans are tied. Value and FCFF rankings need not match. Watch/defer and all base assumptions remain unchanged.
