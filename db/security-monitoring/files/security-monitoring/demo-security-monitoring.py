"""Demo program for the Security Monitoring Database (security-monitoring).
Run: python3 demo-security-monitoring.py
"""
events = ["login ok", "login fail", "login fail", "login fail", "logout"]
fails = sum(1 for e in events if "fail" in e)
print(f"{fails} of {len(events)} events are failures")
