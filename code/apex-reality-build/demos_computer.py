"""Concept-simulation demo archetypes for the Apex-Reality Computer databases.

Every demo is real, runnable, stdlib-only Python. Each one simulates the
CONCEPT MODEL described by its record - honestly labeled as simulation of a
speculative design, never as a real device.
"""
import json


def _q(s):
    return json.dumps(s)


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""' + name.replace('"""', '"') + ' - concept simulation demo.\n'
            'Record ' + rid + ' [' + group + '].\n'
            'CONCEPT SIMULATION: speculative Signature design by Justin Addam Higgins\n'
            '(A7 Signature Dominion). Not a real-world device. Not proven fact.\n"""\n')


def demo_numberline(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - the JAH-UALNS number line as a design concept.
Positions below are computed on the concept model, not measured reality."""
def line_position(value, lo, hi):
    return (value - lo) / (hi - lo)
def nearest_anchor(pos, anchors):
    return min(anchors, key=lambda a: abs(a[1] - pos))
def main():
    anchors = [("ORIGIN", 0.0), ("HARMONY", 0.25), ("THRESHOLD", 0.5),
               ("RADIANCE", 0.75), ("APEX", 1.0)]
    samples = [("plasma flux", 3.7), ("light coherence", 8.2),
               ("void depth", 1.1), ("bridge tension", 6.6)]
    lo, hi = 0.0, 10.0
    print("JAH-UALNS number line  range [%.1f, %.1f]  (concept model)" % (lo, hi))
    for label, v in samples:
        pos = line_position(v, lo, hi)
        aname, apos = nearest_anchor(pos, anchors)
        print("  %-15s value=%4.1f -> position %.3f  nearest anchor: %s (%.2f)"
              % (label, v, pos, aname, apos))
    assert 0.0 <= line_position(5.0, lo, hi) <= 1.0
    print("OK: %s mapped 4 readings onto the concept number line" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_protocol(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - the AUA-JM2 protocol as a design concept.
Frames below are built and parsed by the concept framing rules."""
STX, ETX = "\\x02", "\\x03"
def checksum(payload):
    return sum(payload.encode("utf-8")) % 256
def frame(sender, seq, payload):
    body = "%s|%04d|%s" % (sender, seq, payload)
    return STX + body + "|%02X" % checksum(body) + ETX
def parse(raw):
    assert raw.startswith(STX) and raw.endswith(ETX), "bad framing"
    body = raw[1:-1]
    parts = body.rsplit("|", 1)
    assert int(parts[1], 16) == checksum(parts[0]), "checksum mismatch"
    sender, seq, payload = parts[0].split("|", 2)
    return sender, int(seq), payload
def handshake():
    states, log = ["IDLE"], []
    for nxt, msg in [("HELLO", "HELLO apex-console"),
                     ("SYNC", "SYNC ualns-lock"), ("READY", "READY")]:
        states.append(nxt)
        log.append("%s -> %s : %s" % (states[-2], nxt, msg))
    return log
def main():
    print("AUA-JM2 handshake (concept):")
    for line in handshake():
        print("  " + line)
    msgs = [("console", 1, "boot warp-core"), ("swarm", 2, "form lattice"),
            ("bridge", 3, "anchor span 7")]
    print("framing round-trip:")
    for sender, seq, payload in msgs:
        f = frame(sender, seq, payload)
        s2, q2, p2 = parse(f)
        assert (s2, q2, p2) == (sender, seq, payload)
        print("  %-8s #%d %-16s cksum=%02X ok" % (s2, q2, p2, checksum("%s|%04d|%s" % (s2, q2, p2))))
    print("OK: %s framed and parsed 3 concept messages" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_swarm(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - nanobot swarm coordination as a design concept.
Agents below are simulated points converging on concept targets."""
import random
def step_agents(agents, targets, rate=0.2):
    for i, (x, y) in enumerate(agents):
        tx, ty = targets[i % len(targets)]
        agents[i] = (x + (tx - x) * rate, y + (ty - y) * rate)
def spread(agents, targets):
    return max(abs(x - targets[i % len(targets)][0]) +
               abs(y - targets[i % len(targets)][1])
               for i, (x, y) in enumerate(agents))
def main():
    rnd = random.Random(20261019)
    agents = [(rnd.uniform(-10, 10), rnd.uniform(-10, 10)) for _ in range(12)]
    targets = [(5.0, 5.0), (-5.0, 5.0), (0.0, -5.0)]
    print("swarm: 12 concept nanobots, 3 lattice targets (simulation)")
    steps = 0
    while spread(agents, targets) > 0.05 and steps < 500:
        step_agents(agents, targets)
        steps += 1
    print("  converged in %d steps, final spread %.4f" % (steps, spread(agents, targets)))
    assert steps < 500, "swarm did not converge"
    print("OK: %s coordinated a 12-agent concept swarm" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_portal(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - portal theory as a design concept.
Energy figures below come from the concept equation E = k*d^2/stability."""
def portal_energy(distance, stability, k=1.7):
    return k * distance ** 2 / max(stability, 0.01)
def verdict(energy, budget=100.0):
    if energy <= budget * 0.5:
        return "STABLE"
    if energy <= budget:
        return "MARGINAL"
    return "UNSTABLE"
def main():
    print("portal span analysis (concept model, k=1.7, budget=100.0):")
    spans = [("near hop", 2.0, 0.9), ("mid span", 5.0, 0.7),
             ("far span", 9.0, 0.5), ("deep span", 14.0, 0.4)]
    for label, d, s in spans:
        e = portal_energy(d, s)
        print("  %-9s d=%4.1f stability=%.1f -> E=%7.2f  %s" % (label, d, s, e, verdict(e)))
    assert verdict(portal_energy(2.0, 0.9)) == "STABLE"
    assert verdict(portal_energy(14.0, 0.4)) == "UNSTABLE"
    print("NOTE: concept equation only - no physical claim is made.")
    print("OK: %s evaluated 4 concept portal spans" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_warp(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - warp console harmonics as a design concept.
Coherence below is computed on the concept harmonic series."""
import math
def coherence(harmonics):
    return sum(amp * math.cos(phase)
               for _, amp, phase in harmonics) / max(len(harmonics), 1)
def main():
    print("warp field harmonic stack (concept model):")
    base_amp, coh = 1.0, None
    for n in range(1, 9):
        harmonics = [(k, base_amp / k, 0.15 * k) for k in range(1, n + 1)]
        coh = coherence(harmonics)
        print("  %d harmonic(s): coherence = %+.4f" % (n, coh))
    assert coh is not None and -1.0 <= coh <= 1.0
    print("NOTE: concept harmonic series only - no physical claim is made.")
    print("OK: %s computed warp coherence over 8 harmonics" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_bridge(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - the reality bridge as a design concept.
Spans below are evaluated by the concept feasibility rule."""
import math
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])
def feasible(d, anchors, max_span=10.0):
    return d <= max_span * (1 + 0.25 * (anchors - 2))
def main():
    anchors = {"ALPHA": (0.0, 0.0), "BETA": (7.0, 2.0), "GAMMA": (15.0, -3.0)}
    names = sorted(anchors)
    print("reality bridge anchor survey (concept model):")
    best = None
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            d = dist(anchors[a], anchors[b])
            ok = feasible(d, 2)
            print("  %s <-> %s : span %.2f  %s" % (a, b, d, "FEASIBLE" if ok else "TOO FAR"))
            if ok and (best is None or d > best[2]):
                best = (a, b, d)
    assert best is not None
    print("  longest feasible span: %s <-> %s (%.2f)" % best)
    print("NOTE: concept feasibility rule only - no physical claim is made.")
    print("OK: %s surveyed 3 concept bridge anchors" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_memory(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - the time-aware memory engine as a design concept.
Checkpoints below snapshot concept state; queries are answered from history."""
import copy
class TimeMemory:
    def __init__(self):
        self.log = []
        self.t = 0
    def record(self, event):
        self.t += 1
        self.log.append((self.t, event))
        return self.t
    def checkpoint(self):
        return (self.t, copy.deepcopy(self.log))
    def restore(self, cp):
        self.t, self.log = cp[0], copy.deepcopy(cp[1])
    def as_of(self, t):
        return [e for ts, e in self.log if ts <= t]
def main():
    mem = TimeMemory()
    mem.record("console boot")
    mem.record("ualns lock acquired")
    cp = mem.checkpoint()
    mem.record("warp trial 1")
    print("events as of t=2:", mem.as_of(2))
    mem.restore(cp)
    print("after restore, events as of t=3:", mem.as_of(3))
    assert mem.as_of(3) == ["console boot", "ualns lock acquired"]
    assert mem.t == 2
    print("OK: %s checkpointed and restored concept memory" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_console(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - the warp console command parser as a design concept.
The transcript below shows the concept command set being parsed."""
COMMANDS = {
    "boot": lambda a: "console boot sequence complete (concept)",
    "status": lambda a: "core=ONLINE swarm=12/12 bridge=ANCHORED (concept)",
    "scan": lambda a: "scan of '%s': no anomalies on the concept model" % (a[0] if a else "void"),
    "warp": lambda a: "warp factor %s spooled (concept - no physical effect)" % (a[0] if a else "1"),
    "help": lambda a: "commands: " + ", ".join(sorted(COMMANDS)),
}
def run(line):
    parts = line.strip().split()
    if not parts:
        return "(empty)"
    cmd, args = parts[0].lower(), parts[1:]
    if cmd in COMMANDS:
        return COMMANDS[cmd](args)
    return "unknown command '%s' - try help (concept)" % parts[0]
def main():
    print("apex-reality console transcript (concept simulator):")
    for line in ["boot", "status", "scan plasma", "warp 3", "help", "launch"]:
        print("  > " + line)
        print("    " + run(line))
    assert run("boot").startswith("console boot")
    assert "unknown command" in run("launch")
    print("OK: %s parsed 6 concept console commands" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_registry(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT MODEL - the A7 system registry as a design concept.
Uniqueness below is enforced on concept system names."""
class Registry:
    def __init__(self):
        self.systems = {}
        self.n = 0
    def register(self, sys_name, kind):
        key = sys_name.strip().lower()
        if key in self.systems:
            return None
        self.n += 1
        rid = "JAH-A7-SYS-%04d" % self.n
        self.systems[key] = {"id": rid, "name": sys_name, "kind": kind}
        return rid
    def lookup(self, sys_name):
        return self.systems.get(sys_name.strip().lower())
def main():
    reg = Registry()
    for sname, kind in [("UALNS Core", "number-line"), ("AUA-JM2 Hub", "protocol"),
                        ("Plasma Lattice", "nanobot"), ("UALNS Core", "number-line")]:
        rid = reg.register(sname, kind)
        print("  register %-14s -> %s" % (sname, rid if rid else "REJECTED (duplicate concept name)"))
    assert reg.lookup("aua-jm2 hub")["id"] == "JAH-A7-SYS-0002"
    assert len(reg.systems) == 3
    print("OK: %s ran the concept registry with uniqueness checks" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_sheet(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""Prints the concept file as a formatted concept sheet (documentation aid)."""
INFO = {
    "title": ''' + _q(name) + ''',
    "record": ''' + _q(rid) + ''',
    "group": ''' + _q(group) + ''',
    "key_points": ''' + _q(pts) + ''',
}
def main():
    print("=" * 64)
    print(INFO["title"])
    print("Record %s [%s] - CONCEPT FILE (speculative design)" % (INFO["record"], INFO["group"]))
    print("=" * 64)
    print("Key points:")
''' + "".join(('    print("  %d. %s")' % (i + 1, p.replace('"', "'"))) + "\n" for i, p in enumerate(pts)) + '''    print("OK: %s concept sheet printed" % INFO["title"])
if __name__ == "__main__":
    main()
'''


DEMOS_COMPUTER = {
    "numberline": demo_numberline, "protocol": demo_protocol, "swarm": demo_swarm,
    "portal": demo_portal, "warp": demo_warp, "bridge": demo_bridge,
    "memory": demo_memory, "console": demo_console, "registry": demo_registry,
    "sheet": demo_sheet,
}
