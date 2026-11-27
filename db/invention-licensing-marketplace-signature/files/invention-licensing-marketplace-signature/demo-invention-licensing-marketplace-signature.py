"""Demo program for the Invention Licensing Marketplace Database (invention-licensing-marketplace-signature).
Run: python3 demo-invention-licensing-marketplace-signature.py
All invention examples are fictional; figures are worked examples, not real transactions.
General information only, not legal advice.
"""
listings = [
    {"invention": "Self-Watering Herb Pot", "model": "Exclusive", "rate": 7, "sales": 400000},
    {"invention": "Insulated Soup Flask", "model": "Royalty", "rate": 5, "sales": 800000},
    {"invention": "Solar Trail Lantern", "model": "Overview", "rate": 5, "sales": 200000},
]
for item in listings:
    royalty = item["sales"] * item["rate"] / 100
    print(f"{item['invention']} [{item['model']}]: royalty ${royalty:,.0f} on ${item['sales']:,} at {item['rate']}%")
