"""Concept-experience demo archetypes for the Apex-Reality Federation databases.

Real, runnable, stdlib-only Python. Each simulates the CONCEPT EXPERIENCE
(registry, blueprint, persona, comms, missions) - honestly labeled as a
fictional-concept exercise, never as a real institution.
"""
import json


def _q(s):
    return json.dumps(s)


def _hdr(name, rid, group):
    return ('#!/usr/bin/env python3\n"""' + name.replace('"""', '"') + ' - federation concept demo.\n'
            'Record ' + rid + ' [' + group + '].\n'
            'CONCEPT EXPERIENCE: a fictional-concept exercise by Justin Addam Higgins\n'
            '(A7 Signature Dominion). Not a real registry or institution.\n"""\n')


def demo_shipreg(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - starship registry with uniqueness checks (fictional)."""
class ShipRegistry:
    RESERVED = {"apex one", "dominion prime", "signature dawn"}
    def __init__(self):
        self.ships = {}
        self.n = 0
    def commission(self, commander, ship):
        key = ship.strip().lower()
        if not commander.strip() or not key:
            return None, "name and ship are both required"
        if key in self.RESERVED or key in self.ships:
            return None, "name taken - choose a unique starship name"
        self.n += 1
        rid = "JAH-FED-REG-%04d" % self.n
        self.ships[key] = {"id": rid, "commander": commander.strip(),
                           "ship": ship.strip()}
        return rid, "commissioned"
def main():
    reg = ShipRegistry()
    tries = [("Mara Voss", "Starweaver"), ("Dax Ren", "Starweaver"),
             ("Dax Ren", "Void Lantern"), ("", "Nameless")]
    for commander, ship in tries:
        rid, msg = reg.commission(commander, ship)
        print("  %-10s / %-12s -> %s (%s)" % (commander or "-", ship, rid or "-", msg))
    assert reg.ships["starweaver"]["commander"] == "Mara Voss"
    assert len(reg.ships) == 2
    print("OK: %s commissioned ships with uniqueness checks" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_blueprint(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - patent-style starship blueprint generator (fictional)."""
def blueprint(ship, commander, klass, drive, crew):
    lines = []
    lines.append("CONCEPT BLUEPRINT - not a real patent, not a real starship")
    lines.append("Title: Starship %s (%s class)" % (ship, klass))
    lines.append("Designer of record: %s, A7 Signature Dominion (concept)" % commander)
    lines.append("")
    lines.append("[1] FIELD: speculative starship concept design.")
    lines.append("[2] BACKGROUND: the Federation needs one shared blueprint")
    lines.append("    language so every commander's ship can be described,")
    lines.append("    compared, and role-played consistently.")
    lines.append("[3] SUMMARY: a %s-class vessel, %s drive, crew of %d," % (klass, drive, crew))
    lines.append("    registered to Commander %s." % commander)
    lines.append("[4] DESCRIPTION: hull lines follow the %s-class concept" % klass)
    lines.append("    template; the %s drive is drawn from the concept" % drive)
    lines.append("    propulsion catalog; crew stations scale with complement.")
    lines.append("[5] CLAIMS (concept): 1) a shared blueprint format; 2) a")
    lines.append("    registry entry per ship; 3) honest speculative labeling.")
    return "\\n".join(lines)
def main():
    bp = blueprint("Starweaver", "Mara Voss", "Voyager", "plasma-sail", 12)
    print(bp)
    assert "CONCEPT BLUEPRINT" in bp and "Starweaver" in bp
    print("OK: %s generated a concept blueprint" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_persona(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - ship AI persona generator (fictional character)."""
import hashlib
TRAITS = ["steady", "wry", "precise", "warm", "bold", "patient", "curious", "dry-witted"]
VOICES = ["measured baritone", "bright alto", "soft tenor", "gravelly bass"]
def persona_for(ship):
    h = int(hashlib.sha256(ship.encode("utf-8")).hexdigest(), 16)
    core = ship.replace(" ", "")
    pname = core[:1].upper() + "ex" if len(core) > 2 else (core + "ex")
    return {
        "name": pname.upper() + "-P",
        "trait": TRAITS[h % len(TRAITS)],
        "voice": VOICES[(h >> 8) % len(VOICES)],
    }
def greet(ship, commander, p):
    return ("This is %s, the %s-voiced ship intelligence of the %s. "
            "Commander %s, all concept systems nominal. How shall we fly today? "
            "(I am a fictional persona for a concept experience.)"
            % (p["name"], p["voice"], ship, commander))
def main():
    for ship, commander in [("Starweaver", "Mara Voss"), ("Void Lantern", "Dax Ren")]:
        p = persona_for(ship)
        print("ship: %s  persona: %s (%s, %s)" % (ship, p["name"], p["trait"], p["voice"]))
        print("  " + greet(ship, commander, p))
    assert persona_for("Starweaver") == persona_for("Starweaver")
    print("OK: %s generated 2 deterministic ship personas" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_comms(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - inter-ship comms relay simulation (fictional)."""
def checksum(text):
    return sum(text.encode("utf-8")) % 256
def send(frm, to, text):
    return {"from": frm, "to": to, "text": text, "cksum": checksum(frm + to + text)}
def relay(packet, via):
    assert packet["cksum"] == checksum(packet["from"] + packet["to"] + packet["text"]), \\
        "corrupt packet"
    hops = [packet["from"]] + list(via) + [packet["to"]]
    return " -> ".join(hops), packet["text"]
def main():
    p = send("Starweaver", "Void Lantern", "Rendezvous at Beacon 7 (concept)")
    route, text = relay(p, ["Relay Kappa"])
    print("packet cksum=%02X route: %s" % (p["cksum"], route))
    print("delivered: '%s'" % text)
    bad = dict(p); bad["text"] = "tampered"
    try:
        relay(bad, [])
        raise SystemExit("corruption not caught")
    except AssertionError as e:
        print("tamper check: rejected (%s)" % e)
    print("OK: %s relayed a concept comms packet" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_mission(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - shared mission database (fictional missions)."""
class MissionDB:
    def __init__(self):
        self.missions = []
    def propose(self, title, region, ships_needed):
        mid = "JAH-FED-MSN-%03d" % (len(self.missions) + 1)
        self.missions.append({"id": mid, "title": title, "region": region,
                              "ships": ships_needed, "status": "open"})
        return mid
    def by_region(self, region):
        return [m for m in self.missions if m["region"] == region]
    def assign(self, mid):
        for m in self.missions:
            if m["id"] == mid:
                m["status"] = "underway"
def main():
    db = MissionDB()
    db.propose("Beacon 7 resupply run", "inner reach", 2)
    db.propose("Cartograph the Veil", "outer reach", 4)
    db.propose("Harbor watch rotation", "inner reach", 3)
    print("open missions in the inner reach (concept):")
    for m in db.by_region("inner reach"):
        print("  %s  %-24s ships=%d status=%s" % (m["id"], m["title"], m["ships"], m["status"]))
    db.assign("JAH-FED-MSN-001")
    assert db.missions[0]["status"] == "underway"
    print("OK: %s ran the concept mission database" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_fleet(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - fleet formation geometry (fictional positions)."""
import math
def ring_formation(ships, radius):
    n = len(ships)
    return {s: (radius * math.cos(2 * math.pi * i / n),
                radius * math.sin(2 * math.pi * i / n))
            for i, s in enumerate(ships)}
def main():
    ships = ["Starweaver", "Void Lantern", "Harbor Light", "Keelhaul"]
    pos = ring_formation(ships, 50.0)
    print("ring formation, radius 50 (concept coordinates):")
    for s in ships:
        print("  %-12s -> (%7.2f, %7.2f)" % (s, pos[s][0], pos[s][1]))
    d = math.hypot(pos["Starweaver"][0] - pos["Void Lantern"][0],
                   pos["Starweaver"][1] - pos["Void Lantern"][1])
    print("  Starweaver <-> Void Lantern separation: %.2f" % d)
    assert abs(d - 50.0 * math.sqrt(2)) < 0.01
    print("OK: %s computed a 4-ship concept formation" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_charter(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - federation charter article formatter (fictional)."""
ARTICLES = [
    ("I", "Name", "This fellowship of concept starships is the Apex-Reality Federation."),
    ("II", "Honesty", "Every ship, blueprint, and persona is labeled concept - never real."),
    ("III", "Registry", "No two ships share a name; the registry is the single record."),
    ("IV", "Conduct", "Commanders aid any ship in distress, concept or otherwise kind."),
    ("V", "Command", "The A7 control layer coordinates; it never coerces."),
]
def render(articles):
    out = ["THE FEDERATION CHARTER (concept - a fictional fellowship document)"]
    for num, title, text in articles:
        out.append("Article %s - %s: %s" % (num, title, text))
    return "\\n".join(out)
def main():
    print(render(ARTICLES))
    assert "concept" in render(ARTICLES).lower()
    print("OK: %s rendered the concept charter" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_control(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""CONCEPT EXPERIENCE - unified A7 control layer dispatch (fictional)."""
ORDERS = {"patrol": "Patrol route acknowledged", "rendezvous": "Course laid in",
          "standby": "Standing by", "resupply": "Resupply queued"}
def dispatch(order, ships):
    if order not in ORDERS:
        return [("A7-COMMAND", "unknown order '%s' - ignored" % order)]
    return [("A7-COMMAND -> " + s, "%s: %s (concept)" % (s, ORDERS[order]))
            for s in ships]
def main():
    ships = ["Starweaver", "Void Lantern"]
    for order in ["patrol", "resupply", "warp-now"]:
        print("order: %s" % order)
        for target, ack in dispatch(order, ships):
            print("  %-24s %s" % (target, ack))
    acks = dispatch("standby", ships)
    assert len(acks) == 2 and all("concept" in a for _, a in acks)
    print("OK: %s dispatched 3 concept orders" % ''' + _q(name) + ''')
if __name__ == "__main__":
    main()
'''


def demo_sheet(name, rid, group, pts, req):
    return _hdr(name, rid, group) + '''\
"""Prints the federation concept file as a formatted concept sheet."""
INFO = {
    "title": ''' + _q(name) + ''',
    "record": ''' + _q(rid) + ''',
    "group": ''' + _q(group) + ''',
}
def main():
    print("=" * 64)
    print(INFO["title"])
    print("Record %s [%s] - CONCEPT FILE (fictional fellowship exercise)" % (INFO["record"], INFO["group"]))
    print("=" * 64)
    print("Key points:")
''' + "".join(('    print("  %d. %s")' % (i + 1, p.replace('"', "'"))) + "\n" for i, p in enumerate(pts)) + '''    print("OK: %s concept sheet printed" % INFO["title"])
if __name__ == "__main__":
    main()
'''


DEMOS_FEDERATION = {
    "shipreg": demo_shipreg, "blueprint": demo_blueprint, "persona": demo_persona,
    "comms": demo_comms, "mission": demo_mission, "fleet": demo_fleet,
    "charter": demo_charter, "control": demo_control, "sheet": demo_sheet,
}
