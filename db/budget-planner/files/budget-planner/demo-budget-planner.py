"""Demo program for the Budget Planner Database (budget-planner).
Run: python3 demo-budget-planner.py
"""
income = 1000
expenses = {'Rent': 400, 'Food': 300, 'Travel': 100}
spent = sum(expenses.values())
print(f'Income: {income}; spent: {spent}; left: {income-spent}')
