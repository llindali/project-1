"""Regenerate visible summaries, review documents and PDFs from executed outputs."""
from pathlib import Path
import json,html,hashlib,csv
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import model,peers
ROOT=Path(__file__).parent
out=model.all_outputs();pr=peers.calculate();v=out['base']['valuation'];years=out['base']['statements'];sc=out['scenarios'];rev=out['reverse_dcf']
f=lambda x:f'{x:,.2f}'
def save(name,text):
 (ROOT/'docs'/name).write_text(text)
 return text
memo=save('Decision-Memo.md',f'''# Eli Lilly — Investment committee memorandum
Linda Li | September 8, 2026 valuation | Prepared October 6, 2026 | REVIEW DRAFT: student confirmation pending

## Committee action: watch/defer
Do not initiate at the inherited $1,123.91 closing-price reference. The integrated FCFF scenarios imply approximately ${sc['downside']['per_share']:,.0f}–${sc['upside']['per_share']:,.0f} per share, with a ${v['per_share']:,.0f} base estimate. The base is {100*(v['per_share']/model.PRICE-1):.1f}% below the reference. These are conditional scenarios, not probabilities or a precise fair-value interval. Revisit after the next results release and evidence of realized pricing, capacity conversion and sustainable cash generation. Before adoption, verify spot dilution, committee hurdle and source conventions; dated closing prices have been rechecked.

## Evidence and operating case
FY2025 revenue was $65.179bn. August 2026 guidance put FY2026 revenue at $85–87bn; $86bn anchors the bridge. Five full forecasts cover 2027–2031; growth decelerates 25%, 20%, 15%, 10%, 7%, producing 2031 revenue ${years[-1]['revenue']/1000:.1f}bn. Recurring research is 20% of sales, with $4bn annual acquired IPR&D, and capex tapers to 8% by 2031. Inventory days fall gradually to 330. These are judgments anchored in prior labs and filings, not guidance.

## Valuation and expectation hurdle
FCFF comes directly from articulated statements, retaining research and reinvestment and removing borrowing/interest financing effects. A 9% nominal USD WACC scenario and 2.5% perpetual growth use 20% incremental terminal ROIC. EV is ${v['ev']/1000:.1f}bn; equity is ${v['equity']/1000:.1f}bn after June reported cash/investments less debt, divided by 893.7m diluted-average shares. Terminal value supplies {v['terminal_share']*100:.1f}% of EV. The reference price needs a {rev['growth_shift']*100:.2f}-percentage-point increase to every 2027–2031 growth rate, reaching ${rev['revenue_2031']/1000:.1f}bn sales, with other assumptions fixed. This is one conditional solution, not the market's unique forecast.

## Cross-check and disagreement
Qualified MRK/PFE FY2025 P/E implies ${min(pr['pe_range']):.0f}–${max(pr['pe_range']):.0f}; approximate EV/revenue implies ${min(pr['ev_revenue_range']):.0f}–${max(pr['ev_revenue_range']):.0f}. Mature peers have slower growth, different therapeutic mix and earnings charges; the revenue multiple omits margin differences. Peer EV uses FY2025 diluted-average share proxies and book claims, not exact September capitalization. DCF capitalizes faster future growth; multiples scale historical earnings/revenue. Do not average these methods: the disagreement identifies the growth premium needing evidence.

## Risks, reversal triggers and decision conditions
The downside combines slower growth, higher research/capacity spending, delayed inventory conversion and a 10% WACC. It supports moving from active watch to do-not-initiate if operating evidence confirms that path. The upside requires faster growth, 19% research intensity, 8% WACC and 3% terminal growth; it leaves only about {100*(sc['upside']['per_share']/model.PRICE-1):.1f}% upside. Initiation requires independently supported cash flows and at least a committee-approved margin of safety; a proposed 20% discount to the base implies a price near ${.8*v['per_share']:,.0f}, conditional on the thesis remaining intact. That threshold is analyst policy, not an observed market fact. Stop/rebuild if pricing erosion outpaces volume, capacity spending fails to translate into saleable inventory, or dilution/claims change materially.

## Limitations and accountability
The model uses aggregate growth rather than patient/product drivers; capex does not feed back into capacity or fixed expense margins. Annual statement cash is not rolled to the valuation date, acquired-asset accounting is simplified, and the remaining-2026 bridge prorates annual operating cash flows while excluding already-paid business acquisitions. WACC is illustrative, share counts approximate, and fixed nonoperating balances/claims can omit items. Research cuts do not automatically increase business value. See source ledger and Validation-and-AI-Use for independent checks and unfinished human evidence. No position size is proposed without portfolio constraints.

Sources: LLY FY2025 10-K pp.57–59/70; Q2 2026 10-Q pp.5–8; August 5 Q2 release; MRK/PFE FY2025 filings. Full URLs and definitions: docs/source-ledger.md.
''')
evolution=save('Research-Evolution.md',f'''# Research evolution — review package
## Status and provenance
Prepared October 6, 2026 with Codex (GPT-6) assistance. The original repository memo is reproduced unchanged below and separately as `Edition-A-original.md`. Its checkpoint field says pending. The Lab 03 screenshot documents a graded attempt, not the separate checkpoint receipt. Linda must confirm the exact submitted baseline and supply its receipt. This package does not attest to pre-AI authorship or reconstruct missing history.

## Edition A — preserved text
'''+(ROOT/'docs/Edition-A-original.md').read_text()+f'''

## Dated addendum — October 6, 2026
Retain September 1 Edition A unchanged. Final model date is September 8 to align the saved peer-price snapshot; statement history remains FY2025 and latest bridge balances June 2026. None of the later analysis is backdated. Prior $589 FCFE teaching result and $827 standalone FCFF result use different forecasts/timing and are not interchangeable with this integrated result. The prior Lab 4 $60m short-term-investments bridge addition is not separately identifiable on the Q2 balance sheet: reject it as an unsupported standalone asset, to avoid potential double counting.

## Edition B — conditional committee view
Watch/defer remains the proposed action, supported by the integrated base ${v['per_share']:.2f}, downside ${sc['downside']['per_share']:.2f}, upside ${sc['upside']['per_share']:.2f}. It is not a confirmed personal reflection until Linda reviews it. The preserved initial concern about the growth expectations embedded in price is quantified by the reverse DCF. Read the decision memo for triggers and limitations.

| Item | Edition A | Edition B | Cause and evidence |
|---|---|---|---|
| Action | Watch/defer, no demonstrated DCF support | Watch/defer pending stronger expected-return evidence | Mixed: original thesis, course-required valuation, integrated cash-flow outputs |
| Date/share basis | September 1; 899.3m annual EPS denominator | September 8; 893.7m Q2 diluted proxy for DCF | Primary filing update; spot dilution remains unknown |
| Model | Research plan and preliminary bridge | Six modeled annual statements, 2026 bridge plus five full FCFF years | Course requirement plus AI-assisted implementation; accounting tests |
| Valuation | Reference EV about $1.08tn, no fair-value target | Base EV ${v['ev']/1000:.1f}bn and causal scenarios | Reinvestment, taxes, operating forecast, discount timing |
| Peer challenge | Partner falsification question preserved | Prior inventory challenge retained as reported history, pending confirmation | No fabricated partner or timestamp evidence |
| Risks | Competition, pricing, capacity, pipeline | Same risks plus terminal share and fixed-driver feedback limitations | Sensitivities and reverse DCF; no material thesis reversal |

Student reflection: Linda must supply her own final account of what surprised her and which assumptions she would defend/revise. No fabricated experiential statement is provided.
''')
validation=save('Validation-and-AI-Use.md',f'''# Validation and AI use — review package
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
Terminal EV share {100*v['terminal_share']:.1f}%; WACC scenario rather than independently estimated CAPM. September 8 market closes were independently rechecked October 6; personal model/assumption review remains required. Product demand, pricing and capacity lack a separate causal patient model. Spending cuts do not alter modeled clinical/capacity success. Fixed margins include D&A so capex does not directly change modeled EBIT. Simplified acquisitions, fixed tax/other claims, liquidity backstop, year-end/proportional timing, average-share proxies and nonoperating investments constrain accuracy. Stop issuing a valuation if accounting, funding, domain or perpetuity checks fail; reconsider the action when downside evidence is corroborated.
''')
summary='# Visible executed results\n\nSeptember 8, 2026 · USD millions · review pending student confirmations\n\n'
summary+='| Scenario | Per share USD | EV USD bn | Terminal share |\n|---|---:|---:|---:|\n'
for n,r in sc.items():summary+=f"| {n} | {r['per_share']:.2f} | {r['ev']/1000:.2f} | {100*r['terminal_share']:.1f}% |\n"
summary+='\n## Five full forecasts\n\n| USD millions | '+' | '.join(str(y['year']) for y in years[1:])+' |\n|---|'+ '|'.join(['---:']*5)+'|\n'
for k in ['revenue','cogs','gross_profit','sga','rd','iprd','operating_income','interest','pretax','tax','net_income','cash','ar','inventory','other_current_assets','ppe','intangibles','other_assets','total_assets','debt','revolver','ap','rebates','other_current_liabilities','other_liabilities','equity','total_liabilities_equity','depreciation','amortization','delta_wc','capex','acquisitions','new_debt','dividends','buybacks','cfo','cfi','cff','cash_change','fcff']:summary+='| '+k+' | '+' | '.join(f(y[k]) for y in years[1:])+' |\n'
summary+='\n## WACC–growth sensitivity\n\n| WACC | Terminal growth | Value/share |\n|---:|---:|---:|\n'
for r in out['wacc_growth']:summary+=f"| {100*r['wacc']:.1f}% | {100*r['g']:.1f}% | {r['per_share']:.2f} |\n"
summary+=f"\nApproximate peer P/E range ${min(pr['pe_range']):.2f}–${max(pr['pe_range']):.2f}; EV/revenue range ${min(pr['ev_revenue_range']):.2f}–${max(pr['ev_revenue_range']):.2f}. These are qualified cross-checks, not averaged valuations.\n"
(ROOT/'output/visible_output.md').write_text(summary)
styles=getSampleStyleSheet()
font_path=Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
if font_path.exists():
 pdfmetrics.registerFont(TTFont('DejaVu',str(font_path)))
 for style in styles.byName.values():style.fontName='DejaVu'
styles['BodyText'].fontSize=10;styles['BodyText'].leading=14
styles['Heading1'].textColor=colors.HexColor('#183a65')
def pdf(name,text):
 flow=[]
 for line in text.splitlines():
  if not line.strip():flow.append(Spacer(1,6));continue
  style='Heading1' if line.startswith('# ') else 'Heading2' if line.startswith('## ') else 'BodyText'
  flow.append(Paragraph(html.escape(line.lstrip('# ')),styles[style]))
 SimpleDocTemplate(str(ROOT/'submission'/name),rightMargin=42,leftMargin=42,topMargin=36,bottomMargin=36).build(flow)
for n,t in [('Decision-Memo.pdf',memo),('Research-Evolution.pdf',evolution),('Validation-and-AI-Use.pdf',validation)]:pdf(n,t)
print('Generated review PDFs and visible summary')
