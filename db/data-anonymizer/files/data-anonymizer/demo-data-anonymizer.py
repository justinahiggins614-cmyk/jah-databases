"""Demo program for the Data Anonymizer Database (data-anonymizer).
Run: python3 demo-data-anonymizer.py
"""
name = "Alex Rivers"
masked = name[0] + "*** " + name.split()[1][0] + "***"
print(f"Masking {name!r} gives {masked!r}")
