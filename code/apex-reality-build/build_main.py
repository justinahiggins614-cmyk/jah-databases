"""Record assembly, page injection, verification, main() for the Apex-Reality build."""
import gzip
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B
from demos_computer import DEMOS_COMPUTER
from demos_federation import DEMOS_FEDERATION
from demos_madewith import DEMOS_MADEWITH
import entries_computer
import entries_federation
import entries_madewith

FAMILY = {
    "apex-reality-computer": ("concept", entries_computer.ENTRIES, DEMOS_COMPUTER),
    "apex-reality-computer-signature": ("concept", entries_computer.ENTRIES, DEMOS_COMPUTER),
    "apex-reality-federation": ("federation", entries_federation.ENTRIES, DEMOS_FEDERATION),
    "apex-reality-federation-signature": ("federation", entries_federation.ENTRIES, DEMOS_FEDERATION),
    "made-with-databases": ("madewith", entries_madewith.ENTRIES, DEMOS_MADEWITH),
    "made-with-databases-signature": ("madewith", entries_madewith.ENTRIES, DEMOS_MADEWITH),
}

# ---------------------------------------------------------------- how_it_works

HOW_COMPUTER = {
 "numberline": "In operation, each raw reading is normalized against its documented range to a decimal position between 0.0 and 1.0, then reported three ways: absolute (the decimal), anchor-relative (nearest named anchor plus distance), and banded (which quarter of the line it falls in). The mapping is linear and reversible, so any position converts back to the original reading and unit. The record's demo program performs the full cycle - normalize, locate, name - on sample readings and prints each step.",
 "protocol": "In operation, a sender builds a frame as STX + sender + sequence + payload + checksum + ETX, and the receiver verifies the checksum before trusting a single byte of payload. Sessions open with the HELLO/SYNC/READY handshake, and thereafter frames flow in sequence order; duplicates are acknowledged but never re-executed. The record's demo program runs the handshake, frames three concept messages, parses them back, and verifies every checksum.",
 "swarm": "In operation, each concept nanobot moves a fixed fraction of the way toward its assigned lattice target every tick and shares its position with neighbors, so stragglers are detected and targets re-balanced. Convergence is declared when the maximum spread across the swarm drops below the concept threshold. The record's demo program simulates twelve bots against three targets with a seeded start and reports the steps to convergence.",
 "portal": "In operation, a proposed span's distance and lattice stability feed the concept energy equation E = k*d^2/stability, and the result is classified against the energy budget: STABLE below half budget, MARGINAL below full budget, UNSTABLE above it. Denser lattices raise stability and make farther spans affordable. The record's demo program prices four concept spans and prints each verdict with its arithmetic shown.",
 "warp": "In operation, the imagined warp field is modeled as harmonics 1 through N, each contributing amplitude 1/k at a phase offset, and field coherence is the mean of amplitude-times-cosine-of-phase across the stack. Operators add harmonics and watch coherence move in visible concept steps. The record's demo program stacks eight harmonics and prints coherence at each level.",
 "bridge": "In operation, candidate anchors are surveyed as named coordinates, every pairwise concept distance is computed, and each pair is tested against the feasibility rule (span within max span scaled by anchor count). The longest feasible pair is commissioned; the rest stay surveyed. The record's demo program surveys three concept anchors and commissions the longest feasible span.",
 "memory": "In operation, every concept event is appended to the log with the next sequence timestamp, checkpoints snapshot the full state under a timestamp, and restore returns the engine to a checkpoint exactly. Temporal queries ('as of time T') filter the log rather than reading live state. The record's demo program records events, checkpoints, records more, restores, and proves the restored history matches.",
 "console": "In operation, the console reads a command line, splits it into command and arguments, dispatches to the matching concept handler, and prints the handler's honest answer; unknown commands get guidance, not silence. The record's demo program runs a six-command transcript - boot, status, scan, warp, help, and one unknown command - showing the parser's behavior end to end.",
 "registry": "In operation, registration lowercases and trims the candidate name, refuses it if it collides with a reserved name or an existing entry, and otherwise issues the next sequential registry ID. Lookups are case-insensitive. The record's demo program registers four concept systems - one a deliberate duplicate - and proves the duplicate was refused and the original kept.",
 "sheet": "In operation, the concept sheet renders the record's own data - title, record ID, group, and key points - as a formatted document, the same shape every concept file takes when printed. The record's demo program prints its own sheet, so the documentation and the demonstration are never out of sync.",
}

HOW_FEDERATION = {
 "shipreg": "In the experience, commissioning runs four checks in order: commander name present and screened, ship name present and screened, ship name not reserved, ship name not already registered. Passing all four issues the next sequential registry ID and writes the permanent entry. The record's demo program commissions four ships - including a duplicate name and a blank commander - and proves the checks refused exactly the right ones.",
 "blueprint": "In the experience, the blueprint generator takes your parameters - ship, commander, class, drive, crew - and renders the six-section patent-style document: Title, Field, Background, Summary, Description, Claims, opened by the unmissable concept banner. The record's demo program generates a complete blueprint for a sample ship and verifies the banner and all six sections are present.",
 "persona": "In the experience, the persona generator hashes the ship name to pick a trait and voice deterministically - same ship, same persona, every session - then composes the greeting addressing you as commander with the fiction label attached. The record's demo program generates personas for two ships and proves determinism by generating twice.",
 "comms": "In the experience, sending wraps sender, recipient, text, and checksum into a packet; relays forward it hop by hop, each hop re-verifying the checksum; delivery shows the route the message took. Tampered packets are rejected with an explicit notice. The record's demo program relays one packet through a relay and proves a tampered packet is caught.",
 "mission": "In the experience, proposing writes a mission with ID, title, region, ships-needed, and open status; the board lists missions by region; assignment moves a mission to underway. The record's demo program proposes three missions, lists the inner-reach board, assigns one, and proves the status moved.",
 "fleet": "In the experience, a formation pattern is a named set of positions relative to the lead ship, computed as real coordinate geometry - the ring formation places N ships evenly on a circle of the chosen radius. The record's demo program computes a four-ship ring and verifies the separation math exactly.",
 "charter": "In the experience, the charter renderer prints the five articles - name, honesty, registry, conduct, command - as the fellowship's founding document, and commissioning records the commander's assent. The record's demo program renders the charter and verifies the honesty article is present and labeled.",
 "sheet": "In the experience, the concept sheet renders the record's own data - title, record ID, group, and key points - as a formatted document, the same shape every federation concept file takes when printed. The record's demo program prints its own sheet, so the documentation and the demonstration are never out of sync.",
 "control": "In the experience, the A7 layer takes a named order, dispatches it to each addressed ship, collects per-ship acknowledgements, and reports the operation; unknown orders are refused explicitly. The record's demo program dispatches three orders to two ships and proves every acknowledgement is labeled concept.",
}

HOW_MADEWITH = {
 "lineage": "The lineage demo traces the creation back to its source databases: it prints the creation's title and record ID, lists every database it was made with, and asserts the list is non-empty. Lineage is the archive's answer to 'what made this' - asked and answered for every record, in runnable form.",
 "catalog": "The catalog demo embeds the archive's full 34-entry creation index and searches it by keyword across titles and source-database names, printing hit counts and top matches. It proves the archive is navigable as data, not just readable as pages.",
 "stats": "The stats demo prints the network's milestone table - dates, events, counts - from archive facts, then computes the live-database growth between the October 15 and October 18 milestones and asserts the arithmetic. Milestones as data, growth as checked math.",
 "report": "The report demo prints the creation file as a formatted made-with report: title, record, group, the databases used, and the key points. The documentation and the demonstration stay in sync because the demo prints from the record's own fields.",
}

CITATIONS = {
 "concept-public": ("Signature concept design canon - A7 Signature Dominion design archive, "
                    "speculative throughout. No external sources cited; no website references."),
 "concept-signature": ("Signature concept design canon - A7 Signature Dominion design archive, "
                       "speculative throughout. Signature-stamped edition, in the designer's voice. "
                       "No external sources cited; no website references."),
 "federation-public": ("Apex-Reality Federation concept canon - A7 Signature Dominion registry archive, "
                       "speculative throughout. No external sources cited; no website references."),
 "federation-signature": ("Apex-Reality Federation concept canon - A7 Signature Dominion registry archive, "
                          "speculative throughout. Signature-stamped edition. "
                          "No external sources cited; no website references."),
 "madewith-public": "JAH Databases network build records, October 2026 (internal archive history).",
 "madewith-signature": ("JAH Databases network build records, October 2026 (internal archive history). "
                        "Signature-stamped edition, in the designer's voice."),
}

STANDARDS = {
 "concept": ["Honest labeling: every file carries the speculative-concept label (Manon's standing rule).",
             "Concept simulations only: stdlib-only Python, deterministic, labeled as simulation."],
 "federation": ["Honest labeling: every artifact carries the concept-experience label (Manon's standing rule).",
                "Screened participation: user text screened before entering the shared fiction."],
 "madewith": ["Archive facts only: every creation is from the network's real build history.",
              "Lineage required: every record names the databases it was made with."],
}

SRC_OF = {
 "apex-reality-computer": "signature-concept",
 "apex-reality-computer-signature": "signature",
 "apex-reality-federation": "signature-concept",
 "apex-reality-federation-signature": "signature",
 "made-with-databases": "public-harvest",
 "made-with-databases-signature": "signature",
}

CIT_KEY = {
 "apex-reality-computer": "concept-public",
 "apex-reality-computer-signature": "concept-signature",
 "apex-reality-federation": "federation-public",
 "apex-reality-federation-signature": "federation-signature",
 "made-with-databases": "madewith-public",
 "made-with-databases-signature": "madewith-signature",
}

PROVENANCE = {
 "concept": "Seeded concept archive - Signature concept design documentation (speculative).",
 "federation": "Seeded concept archive - Federation concept experience documentation (speculative).",
 "madewith": "Seeded archive - network build history record (archive fact).",
}

TIER_OF = {}
for _s, (_fam, _ents, _d) in FAMILY.items():
    _f = B.DBCFG[_s]["gen_fields"]
    TIER_OF[_s] = {_f[0]: "foundations", _f[1]: "compounded", _f[2]: "advanced"}


def build_records(slug):
    fam, entries, demos = FAMILY[slug]
    sig = slug.endswith("-signature")
    cfg = B.DBCFG[slug]
    src = SRC_OF[slug]
    how_map = {"concept": HOW_COMPUTER, "federation": HOW_FEDERATION, "madewith": HOW_MADEWITH}[fam]
    catalog = None
    if fam == "madewith":
        catalog = [{"title": t, "dbs": dbs} for (_g, t, _d, _p, _r, _k, dbs) in entries]
    recs = []
    for i, e in enumerate(entries):
        if fam == "madewith":
            g, title0, desc0, points, req, dkey, dbs = e
        else:
            g, title0, desc0, points, req, dkey = e
            dbs = None
        if sig:
            if fam == "madewith":
                title = title0 + " (Signature Edition)"
                desc = ("Signature edition - his own telling of what the network made. " + desc0)
            else:
                title = title0 + " (Signature Edition)"
                desc = ("Signature edition - Justin Addam Higgins's original Signature design writeup, "
                        "in his voice, under the Signature stamp. " + desc0 + " " + B.SPEC_TAG)
            how_extra = (" Told in his voice, under the Signature stamp, with the honest label "
                         "carried on every line.")
        else:
            title = title0
            if fam == "madewith":
                desc = desc0
            else:
                desc = desc0 + " " + B.SPEC_TAG
            how_extra = ""
        rid = "%s%06d" % (cfg["prefix"], i + 1)
        how = how_map[dkey] + how_extra
        fn = demos[dkey]
        if fam == "madewith":
            if dkey == "catalog":
                program = fn(title, rid, g, points, req, catalog)
            else:
                program = fn(title, rid, g, points, req, dbs)
            note = "Working demonstration program (real, runnable Python)."
        else:
            program = fn(title, rid, g, points, req)
            note = ("Working concept-simulation program (real, runnable Python - "
                    "simulates the concept model; not a real device).")
        recs.append({
            "id": rid, "t": title, "g": g, "name": title0, "title": title,
            "description": desc,
            "how_it_works": how,
            "key_points": list(points),
            "requirements": req,
            "standards": list(STANDARDS[fam]),
            "citations": CITATIONS[CIT_KEY[slug]],
            "src": src,
            "ladder_rank": i + 1,
            "ladder_tier": TIER_OF[slug][g],
            "demo": {"kind": "python", "language": "python", "program": program, "note": note},
            "provenance": PROVENANCE[fam] + (" Signature-stamped." if sig else ""),
            "last_verified": "2026-10-19",
        })
    return recs


def write_gz_jsonl(path, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_shard_db(slug, recs):
    base = os.path.join(B.SHARD, "data", slug)
    light = [{"id": r["id"], "t": r["t"], "g": r["g"]} for r in recs]
    write_gz_jsonl(os.path.join(base, "index.jsonl.gz"), light)
    for ci in range(0, len(recs), 100):
        write_gz_jsonl(os.path.join(base, "chunks", "chunk-%04d.jsonl.gz" % (ci // 100)),
                       recs[ci:ci + 100])
    return len(recs)


BANNED = ["facebook", "youtube", "bat belt"]


def check_record(r, slug):
    cfg = B.DBCFG[slug]
    assert r["id"].startswith(cfg["prefix"]), "prefix drift %s" % r["id"]
    for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
              "key_points", "requirements", "standards", "citations", "src",
              "ladder_rank", "ladder_tier", "demo", "provenance", "last_verified"):
        assert k in r, "missing %s in %s" % (k, r["id"])
    assert len(r["description"]) > 60, "stub description %s" % r["id"]
    assert len(r["how_it_works"]) > 60, "stub how_it_works %s" % r["id"]
    assert len(r["key_points"]) >= 4, "thin key_points %s" % r["id"]
    prog = r["demo"]["program"]
    assert prog and len(prog) > 200, "stub demo %s" % r["id"]
    compile(prog, r["id"], "exec")
    blob = json.dumps(r).lower()
    for b in BANNED:
        assert b not in blob, "banned %r in %s" % (b, r["id"])
    fam = FAMILY[slug][0]
    if fam in ("concept", "federation"):
        assert "concept" in blob, "honesty label missing in %s" % r["id"]
