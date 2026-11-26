"""Demo program for the Audit Log Viewer Database (audit-log-viewer-signature).
Run: python3 demo-audit-log-viewer-signature.py
"""
lines = ["10:00 INFO login ana", "10:01 WARN slow query", "10:02 ERROR bad key"]
print(f"A log of {len(lines)} lines")
