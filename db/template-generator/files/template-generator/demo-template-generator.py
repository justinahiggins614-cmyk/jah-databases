"""Demo program for the Template Generator Database (template-generator).
Run: python3 demo-template-generator.py
"""
template = "Dear {name},"
filled = template.format(name="Ana")
print(f"'{template}' with name Ana becomes '{filled}'")
