#!/usr/bin/env python3
"""Build the JAH Signature Binary System databases for JAH Databases
(Manon's order 2026-10-17 15:32 EDT, order #14).

Pipeline replicates code/component-parts-catalog-build/build.py for page
structure: dedupe-gated record authoring -> shard index + chunks ->
machine-executed demos -> db/<slug>/index.html + gen-<slug>.js (via the
numbering-build page builder and the db-page sweep).

CONCURRENCY: this build NEVER touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and NEVER git commits or
pushes. A merger handles those. It writes only:
  db/jah-binary-system/ + db/jah-binary-system-signature/ (index.html, gen-*.js)
  ~/workspace/jah-databases-data-1/data/jah-binary-system[-signature]/ (shards)
  ~/workspace/hidden_files/missing-builds/fragments/jah-binary-system.json
"""
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")
FRAGMENT = "/home/hatch/workspace/hidden_files/missing-builds/fragments/jah-binary-system.json"

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_jah_binary_system import ENTRIES, SIG_TAIL
from demos_jah_binary_system import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig_line = ("Signature originals - his original JAH Signature Binary "
                "System: the bit as the smallest oath, zero and one as the "
                "two witnesses, the byte as a sealed row of eight "
                "witnesses, the carry as the oath passed forward, parity "
                "and the CRC as the witness check, deterministic Signature "
                "coding as the stamp. Clearly labeled Signature-made, never "
                "presented as authentic public record.")
    pub_line = ("Public records - real, fact-checked computing: bits and "
                "binary counting, bits bytes nibbles and words, binary "
                "addition subtraction multiplication and division, ones "
                "and twos complement, signed versus unsigned integers, "
                "bitwise AND OR XOR NOT and masks, logical and arithmetic "
                "shifts, hexadecimal and octal, ASCII, Unicode and UTF-8, "
                "fixed-point fractions, IEEE 754 floating point, logic "
                "gates, half and full adders, carry lookahead, parity, "
                "Hamming codes, CRCs, Gray code, BCD, subnet masks, and CPU "
                "status flags - organized in the Signature system.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what binary is, counting in binary, bits bytes nibbles and "
              "words, binary addition and the carry, binary subtraction "
              "and borrowing, powers of two and data sizes, converting "
              "decimal to binary, converting binary to decimal) -> "
              "Compounded (binary multiplication, binary division, ones "
              "complement, twos complement, signed versus unsigned, "
              "bitwise AND, bitwise OR and XOR, bitwise NOT and masks, "
              "bit shifts, hexadecimal, octal and base conversion, ASCII, "
              "Unicode and UTF-8, fixed-point fractions, IEEE 754 "
              "floating point) -> Advanced (logic gates, compound gates, "
              "half and full adders, carry lookahead, parity, Hamming "
              "codes, CRCs, Gray code, BCD, subnet masks, CPU status "
              "flags).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if source == "signature" else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if source == "signature" else
                     "Public records organized in the Signature system"),
        "search_ph": "Search bits, binary counting, bytes, binary arithmetic, twos complement, bitwise operations, hex, ASCII, UTF-8, floating point, logic gates, adders, parity, Hamming codes, CRC, subnet masks...",
        "chat_ph": "Ask about binary systems...",
        "archive_blurb": ("Seeded %s binary system records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced."
                          % ("Signature-original" if source == "signature" else "public-record")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Generate clearly-labeled binary system studies. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about binary systems - from bits, counting, bytes, and binary arithmetic through complements, bitwise operations, hex, ASCII, UTF-8, and floating point, to logic gates, adders, parity, Hamming codes, CRCs, Gray code, BCD, subnet masks, and CPU flags." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "binary-system-study", "gen_demo_kind": "binary-system-demo",
        "source": source,
    }

CIT_PUB = ("Binary computing (standard references: Knuth DE. The Art of "
           "Computer Programming, Vol. 2: Seminumerical Algorithms. 3rd ed. "
           "Addison-Wesley; 1998; IEEE 754-2019 IEEE Standard for "
           "Floating-Point Arithmetic; ANSI X3.4-1986 / ISO/IEC 646:1991 "
           "7-bit ASCII; The Unicode Consortium. The Unicode Standard, "
           "Version 16.0; 2024; Hamming RW. Error detecting and error "
           "correcting codes. Bell System Technical Journal. "
           "1950;29(2):147-160; Patterson DA, Hennessy JL. Computer "
           "Organization and Design: The Hardware/Software Interface. "
           "RISC-V ed. Morgan Kaufmann; 2021; Tanenbaum AS, Austin T. "
           "Structured Computer Organization. 6th ed. Pearson; 2013; "
           "Stallings W. Computer Organization and Architecture. 11th ed. "
           "Pearson; 2022; Harris DM, Harris SL. Digital Design and "
           "Computer Architecture. 2nd ed. Morgan Kaufmann; 2013; Mogul J, "
           "Postel J. RFC 950: Internet Standard Subnetting Procedure. "
           "1985; Yergeau F. RFC 3629: UTF-8. 2003; Gray F. US Patent "
           "2,632,058; 1953).")
CIT_SIG = CIT_PUB + (" Signature editions are his original JAH Signature "
                     "Binary System - the bit as the smallest oath, the "
                     "byte as a sealed row of witnesses, deterministic "
                     "Signature coding as the stamp - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["jah-binary-system"] = _cfg(
    "jah-binary-system", "The JAH Signature Binary System Database",
    "Bits, binary arithmetic, logic gates, and encodings: real, "
    "fact-checked computing from the bit to the adder to the machine, "
    "taught progressively along the ladder.",
    "binary system record", "JAH-BINY-", "JAH Signature Binary System Archivist",
    "binary system archivist - bits, binary counting, bytes, binary "
    "arithmetic, complements and signed numbers, bitwise operations, hex "
    "and octal, ASCII, Unicode and UTF-8, fixed-point and IEEE 754 "
    "floating point, logic gates, adders, parity, Hamming codes, CRCs, "
    "Gray code, BCD, subnet masks, and CPU status flags; teaching "
    "progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - definition, example, "
    "analogy, application, history, math, how-to - using only archive "
    "data from this system",
    CIT_PUB, "public")
DBCFG["jah-binary-system-signature"] = _cfg(
    "jah-binary-system-signature", "The JAH Signature Binary System Signature Database",
    "His original JAH Signature Binary System: the bit as the smallest "
    "oath, zero and one as the two witnesses, the byte as a sealed row "
    "of eight witnesses, deterministic Signature coding as the stamp. "
    "The full ladder from what binary is through arithmetic, "
    "complements, bitwise operations, and encodings, to gates, adders, "
    "and error codes, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record.",
    "binary system record", "JAH-BINYS-", "JAH Signature Binary System Archivist (Signature)",
    "binary system archivist - Signature editions: his original JAH "
    "Signature Binary System, the bit as the smallest oath and the byte "
    "as a sealed row of witnesses, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively "
    "along the ladder from foundations through compounded to advanced; "
    "answers from many angles - definition, example, analogy, "
    "application, history, math, how-to - using only archive data from "
    "this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"


def build_records(slug, source):
    cfg = DBCFG[slug]
    sig = source == "signature"
    ordered = sorted(enumerate(ENTRIES), key=lambda p: (p[1]["ladder_rank"], p[0]))
    recs = []
    for _, e in ordered:
        name = e["name"]
        title = name + " (Signature Edition)" if sig else name
        if [h for h in base.GATE.check(slug, title) if h[0] != slug]:
            print("  gate refused (cross-db dupe): %s" % title, flush=True)
            continue
        rid = "%s%06d" % (cfg["prefix"], len(recs) + 1)
        if sig:
            description = ("Signature original interpretation. " + e["sig_lens"] + " "
                           + e["description"])
            how = e["sig_lens"] + " " + e["how_it_works"]
            citations = list(e["citations"]) + [SIG_TAIL]
        else:
            description = e["description"]
            how = e["how_it_works"]
            citations = list(e["citations"])
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "public-harvest",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python)."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def write_fragment():
    frag = {"public": {}, "signature": {}}
    for slug, key in (("jah-binary-system", "public"),
                      ("jah-binary-system-signature", "signature")):
        cfg = DBCFG[slug]
        idx = SHARD_BASE + "/data/" + slug + "/index.jsonl.gz"
        frag[key] = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["tagline"],
            "record_kind": cfg["record_kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": idx,
            "record_count": 34, "status": "live", "full_records": 34,
            "index": idx,
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "public-harvest" if key == "public" else "signature",
        }
    os.makedirs(os.path.dirname(FRAGMENT), exist_ok=True)
    with open(FRAGMENT, "w", encoding="utf-8") as f:
        json.dump(frag, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print("fragment: %s" % FRAGMENT, flush=True)


def main():
    sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
    spec = importlib.util.spec_from_file_location(
        "nb_build", os.path.join(REPO, "code", "numbering-build", "build.py"))
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    nb.DBCFG = DBCFG

    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)

    built = {}
    for slug in ("jah-binary-system", "jah-binary-system-signature"):
        source = "signature" if slug.endswith("-signature") else "public"
        built[slug] = build_records(slug, source)

    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        assert len(recs) == 34, "expected 34 records in %s, got %d" % (slug, len(recs))
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "ladder_rank", "ladder_tier", "demo"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            assert 1 <= r["ladder_rank"] <= 10, "ladder_rank out of range in %s" % r["id"]
            assert r["ladder_tier"] in ("foundations", "compounded", "advanced"), \
                "bad ladder_tier in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
                assert r["description"].startswith("Signature original interpretation.")
            else:
                assert r["src"] == "public-harvest"
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog],
                               capture_output=True, text=True, timeout=180)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-800:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "binary-encoding" not in page and "binary-tools" not in page, \
            "sibling slug leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        changed, notes = sweep.process_page(ppath)
        topics = {}
        for r in recs:
            topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
        gen_js = nb.build_gen_js(slug, topics, DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "synthetic intelligence" not in gen_js.lower(), "template leftover in gen js %s" % slug
        with open(os.path.join(ddir, "gen-%s.js" % slug), "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    write_fragment()

    # NOTE: manifest.json, api.json, restamp, commit, and push are owned by
    # the merger - this build stops here by design.
    print("records: %d public + %d signature = %d total" %
          (len(built["jah-binary-system"]), len(built["jah-binary-system-signature"]), total))
    print("DONE - awaiting merger (no manifest/api/commit/push by this build).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
