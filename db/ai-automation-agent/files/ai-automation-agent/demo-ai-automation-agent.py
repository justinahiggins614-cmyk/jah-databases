"""Demo program for the AI Automation Agent Database (ai-automation-agent).
Run: python3 demo-ai-automation-agent.py
"""
trigger = "a new email arrives"
actions = ["file the email", "send a reply"]
print(f"An automation agent waits for '{trigger}' and then runs {len(actions)} actions")
