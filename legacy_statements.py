"""Lab 10: LLY FY2026-2030 three-statement teaching scenario; USD millions.

Run with Python 3, standard library only. See assumptions.md for all labels/reasons.
Gross profit, SG&A and R&D include D&A: never subtract D&A again from income.
"""
import json
import math
from pathlib import Path

HISTORY = json.loads(Path(__file__).with_name('history.json').read_text())
OPENING = dict(year=2025, revenue=65179., cash=7268., ar=17760.,
               inventory=13744., other_current_assets=16857., ppe=24675.,
               intangibles=6521., other_assets=25651., debt=42503.,
               ap=5379., rebates=17382., other_current_liabilities=10832.,
               other_liabilities=9845., equity=26535., revolver=0.)

# Guidance-derived first year; later growth is judgment.
GROWTH = (86000 / 65179 - 1, .25, .20, .15, .10)
MARGIN = (.84, .845, .85, .85, .845)  # judgment
SGA_GP = (.20, .19, .185, .18, .18)  # judgment
RD = (.20,) * 5  # judgment; Lilly-specific recurring research expense
IPRD = (5000., 4000., 4000., 4000., 4000.)  # judgment; cash = expense
CAPEX = (.13, .12, .11, .10, .09)  # judgment, fraction of revenue
DAYS = (400., 380., 365., 350., 330.)  # judgment, ending inventory / COGS
ACQUISITIONS = (10000., 0., 0., 0., 0.)  # judgment; capitalized separately
NEW_DEBT = (12500., 0., 0., 0., 0.)  # judgment; net refinancing proceeds
BUYBACKS = (4000., 0., 0., 0., 0.)  # judgment; fixed per-share denominator
DEPRECIATION_RATE = .07  # judgment on opening net PP&E
AMORTIZATION = 683.  # history: 2025 D&A 1,997 less depreciation 1,314
TAX, DEBT_RATE = .20, .035  # judgments; tax excludes deduction for acquired IPR&D
MIN_CASH, REVOLVER_LIMIT, REVOLVER_RATE = 5000., 5000., .06  # judgments
COST_OF_EQUITY, TERMINAL_GROWTH = .10, .025  # judgments
SHARES = 893.7  # history: Q2 2026 diluted weighted average, fixed proxy
PRICE, PRICE_DATE = 1188.87, '2026-09-24'


def assets(y):
    return sum(y[k] for k in ('cash', 'ar', 'inventory', 'other_current_assets',
                              'ppe', 'intangibles', 'other_assets'))


def liabilities_equity(y):
    return sum(y[k] for k in ('debt', 'ap', 'rebates', 'other_current_liabilities',
                              'other_liabilities', 'equity', 'revolver'))


def working_capital(y):
    return (y['ar'] + y['inventory'] + y['other_current_assets']
            - y['ap'] - y['rebates'] - y['other_current_liabilities'])


def project_year(p, i, rd_ratio=None, capex_ratio=None):
    y = dict(year=2026+i)
    y['revenue'] = p['revenue'] * (1 + GROWTH[i])
    y['gross_profit'] = y['revenue'] * MARGIN[i]
    y['cogs'] = y['revenue'] - y['gross_profit']
    y['sga'] = y['gross_profit'] * SGA_GP[i]
    y['rd'] = y['revenue'] * (RD[i] if rd_ratio is None else rd_ratio)
    y['iprd'] = IPRD[i]
    y['depreciation'] = p['ppe'] * DEPRECIATION_RATE
    y['amortization'] = min(AMORTIZATION, p['intangibles'])
    y['operating_income'] = y['gross_profit'] - y['sga'] - y['rd'] - y['iprd']
    y['interest'] = p['debt'] * DEBT_RATE + p['revolver'] * REVOLVER_RATE
    y['pretax'] = y['operating_income'] - y['interest']
    y['tax'] = max(0., y['pretax'] + y['iprd']) * TAX
    y['net_income'] = y['pretax'] - y['tax']
    y['capex'] = y['revenue'] * (CAPEX[i] if capex_ratio is None else capex_ratio)
    y['acquisitions'] = ACQUISITIONS[i]
    y['ppe'] = p['ppe'] + y['capex'] - y['depreciation']
    y['intangibles'] = p['intangibles'] + y['acquisitions'] - y['amortization']
    y['inventory'] = y['cogs'] * DAYS[i] / 365
    for key in ('ar', 'other_current_assets', 'rebates', 'other_current_liabilities'):
        y[key] = y['revenue'] * OPENING[key] / OPENING['revenue']
    y['ap'] = y['cogs'] * OPENING['ap'] / HISTORY['2025']['cogs']
    y['other_assets'], y['other_liabilities'] = p['other_assets'], p['other_liabilities']
    y['delta_wc'] = working_capital(y) - working_capital(p)
    # IPR&D is expensed, added back in CFO, and paid in CFI exactly once.
    y['cfo'] = y['net_income'] + y['depreciation'] + y['amortization'] + y['iprd'] - y['delta_wc']
    y['cfi'] = -y['capex'] - y['iprd'] - y['acquisitions']
    y['new_debt'] = NEW_DEBT[i]
    y['debt'] = p['debt'] + y['new_debt']  # maturity refinancing: zero net repayments
    y['fcfe_before_revolver'] = y['cfo'] + y['cfi'] + y['new_debt']
    y['dividends'], y['buybacks'] = 6500 * 1.05**i, BUYBACKS[i]
    y['equity'] = p['equity'] + y['net_income'] - y['dividends'] - y['buybacks']
    cash_before = p['cash'] + y['fcfe_before_revolver'] - y['dividends'] - y['buybacks']
    y['draw'] = min(max(0., MIN_CASH-cash_before), max(0., REVOLVER_LIMIT-p['revolver']))
    y['revolver_repayment'] = min(p['revolver'], max(0., cash_before-MIN_CASH))
    y['revolver'] = p['revolver'] + y['draw'] - y['revolver_repayment']
    y['fcfe'] = y['fcfe_before_revolver'] + y['draw'] - y['revolver_repayment']
    y['cff'] = y['new_debt'] + y['draw'] - y['revolver_repayment'] - y['dividends'] - y['buybacks']
    y['cash_change'] = y['cfo'] + y['cfi'] + y['cff']
    y['cash'] = p['cash'] + y['cash_change']  # cash is computed last
    return y


def checks(y, p):
    return {
        'Assets - liabilities - equity': assets(y)-liabilities_equity(y),
        'Cash roll-forward gap': y['cash']-p['cash']-y['cash_change'],
        'Cash flow statement gap': y['cash_change']-y['cfo']-y['cfi']-y['cff'],
        'PP&E roll-forward gap': y['ppe']-p['ppe']-y['capex']+y['depreciation'],
        'Intangibles roll-forward gap': y['intangibles']-p['intangibles']-y['acquisitions']+y['amortization'],
        'Debt roll-forward gap': y['debt']-p['debt']-y['new_debt'],
        'Revolver roll-forward gap': y['revolver']-p['revolver']-y['draw']+y['revolver_repayment'],
        'Equity roll-forward gap': y['equity']-p['equity']-y['net_income']+y['dividends']+y['buybacks'],
        'Income statement gap': y['net_income']-(y['gross_profit']-y['sga']-y['rd']-y['iprd']-y['interest']-y['tax']),
        'Working capital link gap': y['delta_wc']-working_capital(y)+working_capital(p),
        'CFO reconciliation gap': y['cfo']-y['net_income']-y['depreciation']-y['amortization']-y['iprd']+y['delta_wc'],
        'CFI reconciliation gap': y['cfi']+y['capex']+y['iprd']+y['acquisitions'],
        'FCFE reconciliation gap': y['fcfe']-y['cfo']-y['cfi']-y['new_debt']-y['draw']+y['revolver_repayment'],
        'Cash floor shortfall': min(0., y['cash']-MIN_CASH),
        'Revolver limit breach': max(0., y['revolver']-REVOLVER_LIMIT),
    }


def validate(years):
    if len(years) != 5:
        raise ValueError('Exactly five forecast years required')
    opening_gap = assets(OPENING)-liabilities_equity(OPENING)
    if abs(opening_gap) > .01:
        raise ValueError(f'FY2025 opening balance gap: {opening_gap:,.4f}')
    p = OPENING
    for y in years:
        for key, value in y.items():
            if not math.isfinite(value):
                raise ValueError(f"FY{y['year']} {key}: non-finite value")
        for name, gap in checks(y, p).items():
            if abs(gap) > .01:
                raise ValueError(f"FY{y['year']} {name}: {gap:,.4f}")
        p = y


def project(**kwargs):
    years, p = [], OPENING
    for i in range(5):
        p = project_year(p, i, **kwargs)
        years.append(p)
    return years


def value_equity(years, r=COST_OF_EQUITY, g=TERMINAL_GROWTH):
    validate(years)  # required before producing any valuation
    if not (math.isfinite(r) and math.isfinite(g) and r > g >= 0):
        raise ValueError('Require finite cost of equity > terminal growth >= 0')
    if years[-1]['fcfe'] <= 0:
        raise ValueError('Negative or zero terminal FCFE: no perpetuity valuation')
    # Lab convention: value only positive explicit cash flows; disclose if used.
    explicit = sum(max(0., y['fcfe'])/(1+r)**n for n, y in enumerate(years, 1))
    terminal = years[-1]['fcfe']*(1+g)/(r-g)/(1+r)**5
    # Opening excess cash only; future accumulated cash is already in FCFE.
    excess_cash = max(0., OPENING['cash']-MIN_CASH)
    equity = explicit + terminal + excess_cash
    return dict(equity=equity, per_share=equity/SHARES, terminal_share=terminal/equity,
                pv_explicit=explicit, pv_terminal=terminal, opening_excess_cash=excess_cash)


def print_table(title, years, rows):
    print('\n'+title)
    print(f"{'USD millions':<36}" + ''.join(f"{y['year']:>14}" for y in years))
    for label, key in rows:
        values = [key(y) if callable(key) else y[key] for y in years]
        print(f'{label:<36}'+''.join(f'{0 if abs(v)<.000001 else v:>14,.2f}' for v in values))


def main():
    years = project()
    result = value_equity(years)
    print('LLY | Lab 10 | FY2026-2030 | USD millions except per-share values')
    print('Annual teaching scenario; discount origin 2025-12-31; information checked 2026-09-24.')
    print_table('INCOME STATEMENT (D&A already included in operating expenses)', years,
                [(k.replace('_', ' ').title(), k) for k in ('revenue','cogs','gross_profit','sga','rd','iprd','operating_income','interest','pretax','tax','net_income')])
    print_table('BALANCE SHEET', years,
                [(k.replace('_', ' ').title(), k) for k in ('cash','ar','inventory','other_current_assets','ppe','intangibles','other_assets')]
                + [('Total assets', assets)]
                + [(k.replace('_', ' ').title(), k) for k in ('debt','revolver','ap','rebates','other_current_liabilities','other_liabilities','equity')]
                + [('Total liabilities and equity', liabilities_equity)])
    print_table('CASH FLOW STATEMENT AND FCFE (outflow lines shown as positive uses)', years,
                [(k.replace('_', ' ').title(), k) for k in ('net_income','depreciation','amortization','iprd','delta_wc','cfo','capex','acquisitions','cfi','new_debt','draw','revolver_repayment','dividends','buybacks','cff','cash_change','cash','fcfe')])
    check_rows = [dict(year=y['year'], **checks(y,p)) for y,p in zip(years,[OPENING]+years[:-1])]
    print_table('CHECK BLOCK: every gap must be zero; cash floor 5,000', check_rows,
                [(k,k) for k in check_rows[0] if k != 'year'])
    for y in years:
        if y['draw']:
            print(f"FY{y['year']} draws {y['draw']:,.2f} to fund investment/distributions and preserve the cash floor.")
        if y['fcfe'] < 0:
            print(f"FY{y['year']}: negative FCFE; excluded from value under lab convention.")
    for key, value in result.items():
        print(f'{key}: {value:,.6f}')
    print(f"Model: ${result['per_share']:,.2f}/share; market: ${PRICE:,.2f} on {PRICE_DATE}.")
    print(f'Same fixed diluted share proxy: {SHARES:,.1f} million; implied market equity ${PRICE*SHARES:,.2f} million.')
    print('Timing differs: course annual value is not a September 24 mark-to-market valuation.')
    print('Question: what growth, research productivity, and reinvestment would reconcile the gap?')


if __name__ == '__main__':
    main()
