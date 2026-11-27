"""Demo program for the Business Value Calculator Database (business-value-calculator).
Run: python3 demo-business-value-calculator.py
General information only, not financial advice. These are example figures
for a made-up business, not a valuation of any real business.
"""
earnings, earnings_multiple = 200000, 4
revenue, revenue_multiple = 1000000, 1.5
ebitda, ebitda_multiple = 250000, 5
sde, sde_multiple = 150000, 2.5
flows, rate = [100000, 110000, 121000], 0.10
assets, liabilities = 900000, 400000
dcf = sum(f / (1 + rate) ** (i + 1) for i, f in enumerate(flows))
print(f"Earnings method: ${earnings:,} x {earnings_multiple} = ${earnings * earnings_multiple:,}")
print(f"Revenue method: ${revenue:,} x {revenue_multiple} = ${revenue * revenue_multiple:,.0f}")
print(f"EBITDA method: ${ebitda:,} x {ebitda_multiple} = ${ebitda * ebitda_multiple:,}")
print(f"SDE method: ${sde:,} x {sde_multiple} = ${sde * sde_multiple:,.0f}")
print(f"Discounted cash flow (3 years at 10%): ${dcf:,.2f}")
print(f"Asset-based value: ${assets:,} - ${liabilities:,} = ${assets - liabilities:,}")
