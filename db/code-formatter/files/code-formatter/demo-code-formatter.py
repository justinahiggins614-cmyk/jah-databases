"""Demo program for the Code Formatter Database (code-formatter).
Run: python3 demo-code-formatter.py
"""
messy = "x=1\ny=2\nz=3"
lines = messy.split("\n")
print(f"Formatting {len(lines)} lines of messy code gives {len(lines)} lines of neat code")
