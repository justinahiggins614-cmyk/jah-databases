"""Demo program for the Phishing Awareness Tester Database (phishing-awareness-tester).
Run: python3 demo-phishing-awareness-tester.py
"""
signs = ["prize", "urgent", "password", "account", "click", "free", "winner", "verify"]
message = "Claim your prize now"
flags = sum(1 for s in signs if s in message.lower())
print(f"The test message trips {flags} of {len(signs)} warning signs")
