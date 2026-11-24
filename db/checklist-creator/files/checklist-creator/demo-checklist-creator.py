"""Demo program for the Checklist Creator Database (checklist-creator).
Run: python3 demo-checklist-creator.py
"""
items = [f'Check {i}' for i in range(1, 10)]
print(f"A pre-flight checklist has {len(items)} items; all {len(items)} must be checked")
