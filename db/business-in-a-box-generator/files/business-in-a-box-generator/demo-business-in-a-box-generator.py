"""Demo program for the Business-in-a-Box Generator Database (business-in-a-box-generator).
Run: python3 demo-business-in-a-box-generator.py
General business information only - not legal or financial advice.
"""
items = [("Stall table", 150), ("Jars and labels", 120), ("Licence", 60), ("Ingredients", 170)]
startup = sum(price for _, price in items)
price, cost, jars = 5, 3, 40
profit_per_jar = price - cost
weekly_profit = jars * profit_per_jar
fixed = 120
break_even = fixed // profit_per_jar
print(f"Startup budget: {startup} dollars")
print(f"Profit per jar: {profit_per_jar} dollars; weekly profit: {weekly_profit} dollars")
print(f"Break even: {break_even} jars a week")
