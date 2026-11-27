"""Demo program for The Online Franchise Creator Database (online-franchise-creator).
Run: python3 demo-online-franchise-creator.py
General information only, not legal advice.
"""
# Worked example from record 4, Royalties: A Worked Example.
sales = 50000
rate = 0.06
royalty = sales * rate
print(f"Monthly royalty on {sales} sales at {rate:.0%}: {royalty:.0f}")
print(f"Yearly royalty from one location: {royalty * 12:.0f}")
print(f"Yearly royalty from 10 locations: {royalty * 12 * 10:.0f}")
