"""Demo program for the AI Writing Assistant Database (ai-writing-assistant).
Run: python3 demo-ai-writing-assistant.py
"""
draft = ['word'] * 200
polished = draft[:180]
print(f"A draft of {len(draft)} words is polished to {len(polished)} clearer words")
