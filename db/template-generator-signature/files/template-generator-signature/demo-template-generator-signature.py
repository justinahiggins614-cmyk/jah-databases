"""Demo program for the Template Generator Database (template-generator-signature).
Run: python3 demo-template-generator-signature.py
"""
template = "Dear {name},"
filled = template.format(name="Ana")
print(f"'{template}' with name Ana becomes '{filled}'")
