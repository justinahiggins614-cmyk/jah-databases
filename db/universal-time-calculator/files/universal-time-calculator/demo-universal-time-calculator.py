"""Demo program for the Universal Time Calculator Database (Public).
Run: python3 demo-universal-time-calculator.py
Every result below is computed by this program, not typed by hand.
"""
from datetime import date, datetime, timedelta

# 1. Unit conversion: 7,265 seconds
seconds = 7265
hours, rem = divmod(seconds, 3600)
minutes, secs = divmod(rem, 60)
print(f"{seconds} seconds = {hours}h {minutes}m {secs}s")

# 2. Minutes to days: 1,500 minutes
mins = 1500
h, _ = divmod(mins, 60)
d, hh = divmod(h, 24)
print(f"{mins} minutes = {d}d {hh}h ({h}h total)")

# 3. Elapsed time: 09:15 to 14:40
start = 9 * 60 + 15
end = 14 * 60 + 40
diff = end - start
print(f"09:15 to 14:40 = {diff // 60}h {diff % 60}m")

# 4. Speed, distance and time: 240 km at 80 km/h
distance, speed = 240, 80
print(f"{distance} km at {speed} km/h takes {distance / speed:g} hours")

# 5. Countdown: 2026-11-26 05:34 to 2027-01-01 00:00
cd = datetime(2027, 1, 1, 0, 0) - datetime(2026, 11, 26, 5, 34)
print(f"Countdown: {cd.days} days, {cd.seconds // 3600} hours and {(cd.seconds % 3600) // 60} minutes")

# 6. Business days: 2026-11-23 to 2026-11-30
first = date(2026, 11, 23)
days = [first + timedelta(days=i) for i in range(8)]
business = [x for x in days if x.weekday() < 5]
print(f"2026-11-23 to 2026-11-30: {len(business)} business days of {len(days)} calendar days")
