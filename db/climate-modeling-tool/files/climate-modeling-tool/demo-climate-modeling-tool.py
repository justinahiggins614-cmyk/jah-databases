"""Demo program for the Climate Modeling Tool Database (climate-modeling-tool).
Run: python3 demo-climate-modeling-tool.py
"""
incoming, albedo = 340, 0.3
absorbed = round(incoming * (1 - albedo), 1)
print(f"340 watts per square metre in, albedo 0.3: {absorbed} absorbed")
