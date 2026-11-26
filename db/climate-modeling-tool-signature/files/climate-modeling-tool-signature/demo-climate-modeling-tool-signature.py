"""Demo program for the Climate Modeling Tool Database (climate-modeling-tool-signature).
Run: python3 demo-climate-modeling-tool-signature.py
"""
incoming, albedo = 340, 0.3
absorbed = round(incoming * (1 - albedo), 1)
print(f"340 watts per square metre in, albedo 0.3: {absorbed} absorbed")
