"""Demo program for the Operating System Simulator Database (operating-system-simulator).
Run: python3 demo-operating-system-simulator.py
"""
bursts = [120, 80, 40]
waits = [0, bursts[0], bursts[0] + bursts[1]]
print(f"The simulator runs {len(bursts)} processes: waits of {waits[0]}, {waits[1]} and {waits[2]} milliseconds")
