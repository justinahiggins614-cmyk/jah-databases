"""Demo program for the AI Debugging Tool Database (ai-debugging-tool-signature).
Run: python3 demo-ai-debugging-tool-signature.py
"""
trace = ["line 1: ok", "line 2: ok", "line 3: ZeroDivisionError"]
print(f"A trace of {len(trace)} lines fails at line {len(trace)}")
