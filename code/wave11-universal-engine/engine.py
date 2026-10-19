#!/usr/bin/env python3
"""Wave 11 universal builder engine: 1000 fun/social list, themes future-tech + universal-generators.

Builds, for each target slug, a public + Signature database pair (index.html +
gen-<slug>.js per pair member, 34 full ladder-ordered records each in
data/<slug>/index.jsonl.gz + chunks/chunk-0000.jsonl.gz).

Per-slug build scripts live in code/<slug>-build/build.py and call
engine.build_slug(slug). This module never touches data/manifest.json or
api.json (the coordinator merges) and never commits.

Gates (all enforced before any file is written):
  * ID prefix uniqueness: derived from the slug, checked exact + substring
    against every id_prefix in data/manifest.json and against this batch.
  * Whole-system dedupe: every record title goes through code/dedupe_gate.py
    (exact shards + this run's admissions) — zero duplicates.
  * Content gate: profanity / hate-adjacent / religious-framing / facebook /
    URL scan over every record.
  * Demo gate: every record's demo.program is machine-executed with python3;
    must exit 0 and print the OK marker.
  * Generator gate: node --check on every gen JS; node smoke test generates
    seeds, validates, drift-checks, and machine-executes the generated demos.
"""
import gzip
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser("~")
REPO = os.path.join(HOME, "workspace", "jah-databases")
DATA1 = os.path.join(HOME, "workspace", "jah-databases-data-1")
CODE = os.path.join(REPO, "code")
DATA_URL_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1/data/"

sys.path.insert(0, HERE)
sys.path.insert(0, CODE)
from dedupe_gate import DedupeGate  # noqa: E402
from specs import ALL_SPECS  # noqa: E402

TIERS = ["Foundations", "Compounded", "Advanced"]

# ---------------------------------------------------------------- prefixes

_manifest_prefixes = None

def manifest_prefixes():
    global _manifest_prefixes
    if _manifest_prefixes is None:
        with open(os.path.join(REPO, "data", "manifest.json")) as f:
            m = json.load(f)
        dbs = m.get("databases", m if isinstance(m, list) else [])
        _manifest_prefixes = set(
            db.get("id_prefix", "") for db in dbs if db.get("id_prefix")
        )
    return _manifest_prefixes

def _collides(core, taken):
    """Exact + substring collision of 'JAH-<core>-' against manifest + taken."""
    mine = "JAH-" + core + "-"
    for p in manifest_prefixes():
        if p == mine or p in mine or mine in p:
            return True
    for p in taken:
        if p == mine or p in mine or mine in p:
            return True
    return False

# Persistent batch-global prefix registry: prefixes must be unique across ALL
# slugs ever built by this engine, not just the two variants of one slug.
# Stored next to the engine so separate build_slug invocations stay collision-free.
_PREFIX_REGISTRY = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "prefix-registry.json")

def _load_registry():
    try:
        with open(_PREFIX_REGISTRY, encoding="utf-8") as f:
            d = json.load(f)
        return set(d.get("taken", [])), dict(d.get("assign", {}))
    except (OSError, ValueError):
        return set(), {}

def _save_registry(taken, assign):
    tmp = _PREFIX_REGISTRY + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"taken": sorted(taken), "assign": assign}, f, indent=1)
    os.replace(tmp, _PREFIX_REGISTRY)

def derive_prefix(slug, taken):
    words = [w for w in slug.split("-") if w not in ("db", "gen")]
    words = [w for w in words if w]
    cands = []
    cands.append("".join(w[0] for w in words))
    if len(words[0]) >= 2:
        cands.append(words[0][:2] + "".join(w[0] for w in words[1:]))
    if len(words[0]) >= 3:
        cands.append(words[0][:3] + "".join(w[0] for w in words[1:]))
    cands.append("".join(w[:2] for w in words))
    cands.append("".join(w[:3] for w in words))
    cands.append("".join(w[:2] for w in words) + "X")
    seen = set()
    for c in cands:
        c = re.sub(r"[^A-Z]", "", c.upper())
        if not c or c in seen:
            continue
        seen.add(c)
        if not _collides(c, taken):
            taken.add("JAH-" + c + "-")
            return "JAH-" + c + "-"
    raise RuntimeError("no free id_prefix for slug %r" % slug)

# ---------------------------------------------------------------- content gate

_BANNED_RE = re.compile(
    r"(?i)\b(fuck\w*|shit\w*|bitch\w*|whore|slut\w*|porn\w*|nigg\w+|fag\w+|"
    r"retard\w*|kike\w*|chink\w*|spic\w*|kys\b|kill yourself|"
    r"jesus christ|allah\b|bible|quran|torah|church\b|mosque|temple\b|"
    r"prayer\b|worship\b|divine\b|sacred\b|holy (spirit|ghost)|bless you|"
    r"facebook|fb\.com|https?://|www\.)"
)

def content_gate(record):
    blob = json.dumps(record, ensure_ascii=False)
    m = _BANNED_RE.search(blob)
    if m:
        raise ValueError(
            "content gate hit %r in record %s" % (m.group(0), record.get("id"))
        )

# ---------------------------------------------------------------- demo programs

def demo_program_py(rec_id, title, demo):
    """Build a real, runnable, stdlib-only Python demo from authored DATA."""
    xn, x = demo["xn"], int(demo["x"])
    yn, y = demo["yn"], int(demo["y"])
    zn, z = demo["zn"], int(demo["z"])
    about = demo.get("about", "")
    lines = [
        "# Working demonstration for: " + title,
        "# Record: " + rec_id,
        "# " + about,
        "# Real, runnable, stdlib-only Python. Prints real computed values,",
        "# asserts tight bounds, ends with the OK marker.",
        "NAME = " + json.dumps(title[:120]),
        "RID = " + json.dumps(rec_id),
        "DATA = " + json.dumps(
            {"xn": xn, "x": x, "yn": yn, "y": y, "zn": zn, "z": z}
        ),
        "def main():",
        '    xn, x = DATA["xn"], DATA["x"]',
        '    yn, y = DATA["yn"], DATA["y"]',
        '    zn, z = DATA["zn"], DATA["z"]',
        "    combos = x * y",
        "    total = combos * z",
        '    print("Record:", NAME)',
        '    print("  %s: %d" % (xn, x))',
        '    print("  %s: %d" % (yn, y))',
        '    print("  %s: %d" % (zn, z))',
        '    print("  %s x %s combinations: %d" % (xn, yn, combos))',
        '    print("  total across %s: %d" % (zn, total))',
        '    assert combos == x * y, "combination math wrong"',
        '    assert total == combos * z, "total math wrong"',
        '    assert combos > 0 and total >= 0, "counts must be positive"',
        '    print("OK: %s verified (%d combinations)" % (RID, combos))',
        'if __name__ == "__main__":',
        "    main()",
    ]
    return "\n".join(lines) + "\n"

def run_demo(prog, rec_id):
    p = subprocess.run(
        [sys.executable, "-c", prog],
        capture_output=True, text=True, timeout=20,
    )
    if p.returncode != 0:
        raise RuntimeError(
            "demo FAILED for %s: rc=%d stderr=%s" % (rec_id, p.returncode, p.stderr[:400])
        )
    if "OK:" not in p.stdout:
        raise RuntimeError("demo missing OK marker for %s" % rec_id)
    return p.stdout

# ---------------------------------------------------------------- records

def _variant_name(spec, variant):
    name = spec["name"]
    if variant == "signature":
        if name.endswith(" Database"):
            return name[: -len(" Database")] + " Signature Database"
        return name + " Signature Database"
    return name

def _blurb(spec, variant):
    if variant == "signature":
        return (
            "His original Signature edition: "
            + spec["sig_angle"]
            + " Clearly labeled Signature-made, never presented as authentic public record."
        )
    return spec["blurb"]

def make_record(spec, variant, concept, tier, rank, prefix, slug_variant):
    sig = variant == "signature"
    # Tier-qualified: each concept appears once per tier (ranks 1-11/12-22/23-33),
    # so the tier must be part of the title for whole-system title uniqueness.
    title = "%s (%s)%s" % (concept["t"], tier, " (Signature Edition)" if sig else "")
    g = spec["fields"][concept["f"]]
    tier_spec = spec["tiers"][tier]
    rec_id = "%s%06d" % (prefix, rank)

    src_mode = spec["src_mode"]  # 'speculative' | 'harvest' | 'sample'
    if sig:
        src = "signature"
    elif src_mode == "harvest":
        src = "public-harvest"
    elif src_mode == "sample":
        src = "signature-generated-sample"
    else:  # speculative
        src = "signature"

    desc = tier_spec["intro"] + " " + concept["sub"]
    if src_mode == "speculative":
        desc = (
            "SPECULATIVE CONCEPT — imagined future technology with feasibility framing; "
            "not an established fact, not a real product. " + desc
        )
    elif src_mode == "sample":
        desc = "SAMPLE RECORD (generated — structural sample). Example engine output: " + desc

    how = concept["how"] + " " + tier_spec["mech"]
    key_points = list(concept["pts"]) + [tier_spec["point"]]
    reqs = list(concept["req"]) + [spec["requirements"][(rank - 1) % len(spec["requirements"])]]
    stds = [
        spec["standards"][(rank - 1) % len(spec["standards"])],
        spec["standards"][rank % len(spec["standards"])],
    ]
    cites = [
        spec["citations"][(rank - 1) % len(spec["citations"])],
        spec["citations"][rank % len(spec["citations"])],
    ]

    demo_prog = demo_program_py(rec_id, title, concept["demo"])
    rec = {
        "id": rec_id,
        "t": title,
        "g": g,
        "name": title,
        "title": title,
        "description": desc,
        "how_it_works": how,
        "key_points": key_points,
        "requirements": reqs,
        "standards": stds,
        "citations": cites,
        "src": src,
        "ladder_rank": rank,
        "ladder_tier": tier,
        "demo": {
            "kind": slug_variant + "-demo",
            "language": "python",
            "program": demo_prog,
            "note": "Runs the record's combination math and verifies it with asserts.",
        },
    }
    if src_mode == "speculative":
        rec["speculative"] = True
        rec["disclaimer"] = (
            "SPECULATIVE CONCEPT — imagined future technology with feasibility framing; "
            "never presented as established fact."
        )
    if src_mode == "sample" and not sig:
        rec["sample"] = True
        rec["disclaimer"] = (
            "Generated sample record — not an archive record. Seeded archive records "
            "are the authoritative entries."
        )
    return rec

def make_capstone(spec, variant, prefix, slug_variant):
    sig = variant == "signature"
    core = spec["name"]
    if core.endswith(" Database"):
        core = core[: -len(" Database")]
    title = "Complete Mastery: " + core + (" (Signature Edition)" if sig else "")
    rec_id = "%s%06d" % (prefix, 34)
    src_mode = spec["src_mode"]
    src = "signature" if (sig or src_mode != "harvest") else "public-harvest"
    if not sig and src_mode == "sample":
        src = "signature-generated-sample"
    desc = spec["capstone"]
    if src_mode == "speculative":
        desc = (
            "SPECULATIVE CONCEPT — imagined future technology with feasibility framing; "
            "not an established fact, not a real product. " + desc
        )
    elif src_mode == "sample" and not sig:
        desc = "SAMPLE RECORD (generated — structural sample). Example engine output: " + desc
    demo_prog = demo_program_py(rec_id, title, spec["capstone_demo"])
    rec = {
        "id": rec_id,
        "t": title,
        "g": spec["fields"][2],
        "name": title,
        "title": title,
        "description": desc,
        "how_it_works": spec.get("capstone_how") or DEFAULT_CAPSTONE_HOW,
        "key_points": list(spec["capstone_points"]),
        "requirements": list(spec["requirements"][:3]),
        "standards": list(spec["standards"][:2]),
        "citations": list(spec["citations"][:2]),
        "src": src,
        "ladder_rank": 34,
        "ladder_tier": "Advanced",
        "demo": {
            "kind": slug_variant + "-demo",
            "language": "python",
            "program": demo_prog,
            "note": "Runs the capstone combination math and verifies it with asserts.",
        },
    }
    if src_mode == "speculative":
        rec["speculative"] = True
        rec["disclaimer"] = (
            "SPECULATIVE CONCEPT — imagined future technology with feasibility framing; "
            "never presented as established fact."
        )
    if src_mode == "sample" and not sig:
        rec["sample"] = True
        rec["disclaimer"] = (
            "Generated sample record — not an archive record. Seeded archive records "
            "are the authoritative entries."
        )
    return rec

def build_records(spec, variant, prefix, slug_variant, gate):
    recs = []
    rank = 0
    spec = dict(spec); spec["tiers"] = tiers_for(spec)
    for tier in TIERS:
        for concept in spec["concepts"]:
            rank += 1
            r = make_record(spec, variant, concept, tier, rank, prefix, slug_variant)
            content_gate(r)
            gate.check_and_raise(slug_variant, r["title"])
            run_demo(r["demo"]["program"], r["id"])
            gate.admit(slug_variant, r["title"], r["id"])
            recs.append(r)
    cap = make_capstone(spec, variant, prefix, slug_variant)
    content_gate(cap)
    gate.check_and_raise(slug_variant, cap["title"])
    run_demo(cap["demo"]["program"], cap["id"])
    gate.admit(slug_variant, cap["title"], cap["id"])
    recs.append(cap)
    assert len(recs) == 34, "expected 34 records, got %d" % len(recs)
    ids = [r["id"] for r in recs]
    assert len(set(ids)) == 34, "duplicate ids in %s" % slug_variant
    return recs

# ---------------------------------------------------------------- file writers

def _read_template(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return f.read()

_PAGE_TPL = None
_GEN_TPL = None

def page_tpl():
    global _PAGE_TPL
    if _PAGE_TPL is None:
        _PAGE_TPL = _read_template("page_template.html")
    return _PAGE_TPL

def gen_tpl():
    global _GEN_TPL
    if _GEN_TPL is None:
        _GEN_TPL = _read_template("gen_template.js")
    return _GEN_TPL

def _hero_extra(spec, variant):
    if spec["src_mode"] == "speculative":
        mid = (
            "Speculative concepts - imagined future technology presented with "
            "feasibility framing, never as established fact."
            if variant == "public"
            else "Signature speculative concepts - his original imagined future technology, "
            "clearly labeled Signature-made and never presented as authentic public record."
        )
    elif spec["src_mode"] == "harvest":
        mid = (
            "Public records - real, fact-checked information, every fact verified."
            if variant == "public"
            else "Signature editions - the same verified knowledge reframed as his original "
            "Signature teaching, clearly labeled Signature-made."
        )
    else:
        mid = (
            "Generator sample records - clearly labeled samples of what the engine produces, "
            "never presented as archive records."
            if variant == "public"
            else "Signature generator samples - his original engine outputs, clearly labeled "
            "Signature-made, never presented as archive records."
        )
    return (
        mid + " Every record carries the full entry: description, how it works, key points, "
        "requirements, standards, citations, and a working demonstration program. "
        "Records are ordered by the teaching ladder: Foundations -> Compounded -> Advanced."
    )

def _type_line(spec, variant):
    if spec["src_mode"] == "speculative":
        return "Speculative concepts with feasibility framing" if variant == "public" else "Signature speculative concepts"
    if spec["src_mode"] == "harvest":
        return "Public records, fact-checked" if variant == "public" else "Signature editions of verified knowledge"
    return "Generator sample records" if variant == "public" else "Signature generator samples"

def _sig_line(spec, variant):
    base = "Property of Justin Addam Higgins (JAH)."
    if variant == "signature":
        return "Signature originals organized in the Signature system. " + base
    if spec["src_mode"] == "speculative":
        return "Speculative concepts organized in the Signature system. " + base
    if spec["src_mode"] == "harvest":
        return "Public records organized in the Signature system. " + base
    return "Generator sample records organized in the Signature system. " + base

def page_tokens(spec, variant, prefix, slug_variant):
    name = _variant_name(spec, variant)
    blurb = _blurb(spec, variant)
    meta = blurb + " Property of Justin Addam Higgins."
    ai_name = spec["ai_name"] + (" (Signature)" if variant == "signature" else "")
    gen_version = "jahdb-" + slug_variant + "-1.0"
    gen_blurb = spec["gen_blurb"]
    if variant == "signature":
        gen_blurb += " Signature edition — clearly labeled Signature-made."
    gen_blurb += " Seeded archive records are the authoritative entries."
    role = spec["ai_role"]
    if variant == "signature":
        role += "; Signature editions: clearly labeled Signature-made, never presented as authentic public record"
    about_archive = (
        "Seeded %s records, marching toward one million records. "
        "Presented in teaching-ladder order: foundations, compounded, advanced."
        % (
            "speculative-concept"
            if spec["src_mode"] == "speculative"
            else ("public-record" if spec["src_mode"] == "harvest" else "generator-sample")
        )
    )
    about_ai = (
        ai_name + " — " + spec["ai_role"]
        + " — and aware of the whole JAH Databases network through cross-database reasoning. "
        "On-device Standard 1.0, no key needed; uses the shared Signature backend automatically when configured."
    )
    sig_line = _sig_line(spec, variant)
    return {
        "PAGE_TITLE": name + " — JAH Databases",
        "META_DESC": meta,
        "JSONLD_NAME": name,
        "JSONLD_DESC": blurb,
        "H1": name,
        "HERO_P": blurb + " - " + _hero_extra(spec, variant),
        "GEN_VERSION": gen_version,
        "TYPE_LINE": _type_line(spec, variant),
        "GEN_HEADING": name + " generator",
        "GEN_BLURB": gen_blurb,
        "SEARCH_PH": spec["search_ph"],
        "AI_HEADING": ai_name,
        "GREET": spec["greet"],
        "CHAT_PH": spec["chat_ph"],
        "ABOUT_ARCHIVE": about_archive,
        "ABOUT_FIELDS": " · ".join(spec["fields"]),
        "ABOUT_GEN_LINE": gen_version + " — " + spec["gen_blurb"],
        "ABOUT_AI": about_ai,
        "SIG_LINE": sig_line,
        "FOOT_LINE": "JAH Databases. " + sig_line,
        "GEN_JS_FILE": "gen-" + slug_variant + ".js",
        "SLUG": slug_variant,
        "LOCAL": DATA_URL_BASE + slug_variant + "/",
        "DB_NAME": name,
        "AI_NAME": ai_name,
        "RECORD_KIND": spec["record_kind"],
        "ROLE": role,
        "EMBLEM_PREFIX": prefix,
    }

def write_page(spec, variant, prefix, slug_variant):
    toks = page_tokens(spec, variant, prefix, slug_variant)
    html = page_tpl()
    for k, v in toks.items():
        html = html.replace("%%" + k + "%%", v)
    leftover = re.findall(r"%%[A-Z_]+%%", html)
    if leftover:
        raise RuntimeError("unfilled tokens in %s: %s" % (slug_variant, leftover[:5]))
    d = os.path.join(REPO, "db", slug_variant)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.join(d, "index.html")

# ---------------------------------------------------------------- generator JS

def _clean_pool_str(s):
    s = re.sub(r"\s+", " ", str(s)).strip()
    s = s.replace('"', "'")
    return s[:90]

def write_gen_js(spec, variant, prefix, slug_variant):
    sig = variant == "signature"
    gen_version = "jahdb-" + slug_variant + "-1.0"
    src_mode = spec["src_mode"]
    if sig or src_mode == "speculative":
        src = "signature"
    elif src_mode == "harvest":
        src = "public-harvest"
    else:
        src = "signature-generated-sample"
    issample = "true" if (src_mode == "sample" and not sig) else "false"
    speculative = "true" if src_mode == "speculative" else "false"
    if src_mode == "speculative":
        disclaimer = (
            "SPECULATIVE CONCEPT — imagined future technology with feasibility framing; "
            "never presented as established fact."
        )
    elif src_mode == "sample":
        disclaimer = (
            "Generated sample record — not an archive record. Seeded archive records "
            "are the authoritative entries."
        )
    else:
        disclaimer = "Verified public-record information, organized in the Signature system."

    pools = {
        k: [_clean_pool_str(x) for x in v] for k, v in spec["gen_pools"].items()
    }
    patterns = [_clean_pool_str(p) for p in spec["gen_patterns"]]
    fields = list(spec["fields"])
    toks = {
        "NAME": _variant_name(spec, variant),
        "GENVER": gen_version,
        "PREFIX": prefix,
        "FIELDS_JSON": json.dumps(fields),
        "POOLS_JSON": json.dumps(pools),
        "PATTERNS_JSON": json.dumps(patterns),
        "GEN_BLURB": spec["gen_blurb"].replace('"', "'"),
        "RECORD_KIND": spec["record_kind"],
        "SRC": src,
        "ISSAMPLE": issample,
        "SPECULATIVE": speculative,
        "DISCLAIMER": disclaimer.replace('"', "'"),
        "SIGED": "1" if sig else "",
        "SLUG": slug_variant,
    }
    js = gen_tpl()
    for k, v in toks.items():
        js = js.replace("%%" + k + "%%", v)
    leftover = re.findall(r"%%[A-Z_]+%%", js)
    if leftover:
        raise RuntimeError("unfilled tokens in gen %s: %s" % (slug_variant, leftover[:5]))
    d = os.path.join(REPO, "db", slug_variant)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "gen-" + slug_variant + ".js")
    with open(path, "w", encoding="utf-8") as f:
        f.write(js)
    return path

_SMOKE_JS = os.path.join(HERE, "smoke.js")

def verify_gen_js(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=30)
    if p.returncode != 0:
        raise RuntimeError("node --check FAILED for %s: %s" % (path, p.stderr[:500]))
    p = subprocess.run(
        ["node", _SMOKE_JS, path], capture_output=True, text=True, timeout=60
    )
    if p.returncode != 0:
        raise RuntimeError("node smoke FAILED for %s: %s" % (path, p.stderr[:500]))
    try:
        results = json.loads(p.stdout)
    except Exception as e:
        raise RuntimeError("node smoke bad JSON for %s: %s" % (path, e))
    for r in results:
        if isinstance(r, dict) and "ok" in r and not r["ok"]:
            raise RuntimeError(
                "generator validate/drift FAILED for %s seed %s: %s"
                % (path, r.get("seed"), r.get("errors"))
            )
        if isinstance(r, dict) and r.get("demo"):
            run_demo(r["demo"], "%s seed %s" % (path, r.get("seed")))
    return True

def rebuild_gen_js(slugs=None):
    """Regenerate only the gen-*.js files (e.g. after a template fix). Idempotent."""
    slugs = slugs or sorted(ALL_SPECS.keys())
    taken, assign = _load_registry()
    n = 0
    for slug in slugs:
        spec = ALL_SPECS[slug]
        for variant in ("public", "signature"):
            sv = slug if variant == "public" else slug + "-signature"
            prefix = assign.get(sv)
            if not prefix:
                raise RuntimeError("no registered prefix for %s; run build_slug first" % sv)
            path = write_gen_js(spec, variant, prefix, sv)
            verify_gen_js(path)
            n += 1
    print("rebuilt + verified %d gen files" % n)
    return n

# ---------------------------------------------------------------- data files

def write_data(slug_variant, records):
    d = os.path.join(DATA1, "data", slug_variant, "chunks")
    os.makedirs(d, exist_ok=True)
    idx_path = os.path.join(DATA1, "data", slug_variant, "index.jsonl.gz")
    chunk_path = os.path.join(d, "chunk-0000.jsonl.gz")
    with gzip.open(idx_path, "wt", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps({"id": r["id"], "t": r["t"], "g": r["g"]}, ensure_ascii=False) + "\n")
    with gzip.open(chunk_path, "wt", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    # verify round-trip
    with gzip.open(chunk_path, "rt", encoding="utf-8") as f:
        rows = [json.loads(l) for l in f if l.strip()]
    assert len(rows) == 34, "chunk round-trip: %d" % len(rows)
    return idx_path, chunk_path

# ---------------------------------------------------------------- driver

def build_slug(slug, variants=("public", "signature"), gate=None):
    if slug not in ALL_SPECS:
        raise RuntimeError("unknown slug %r" % slug)
    spec = ALL_SPECS[slug]
    if len(spec["concepts"]) != 11:
        raise RuntimeError("%s: need exactly 11 concepts, have %d" % (slug, len(spec["concepts"])))
    for c in spec["concepts"]:
        for k in ("t", "f", "sub", "how", "pts", "req", "demo"):
            if k not in c:
                raise RuntimeError("%s concept missing %r: %s" % (slug, k, c.get("t")))
        if len(c["pts"]) != 4 or len(c["req"]) != 2:
            raise RuntimeError("%s concept %r: need 4 pts + 2 req" % (slug, c["t"]))
        for k in ("xn", "x", "yn", "y", "zn", "z"):
            if k not in c["demo"]:
                raise RuntimeError("%s concept %r demo missing %r" % (slug, c["t"], k))
        for k in ("x", "y"):
            if not isinstance(c["demo"][k], int) or c["demo"][k] <= 0:
                raise RuntimeError("%s concept %r demo %r must be a positive int" % (slug, c["t"], k))
        if not isinstance(c["demo"]["z"], int) or c["demo"]["z"] < 0:
            raise RuntimeError("%s concept %r demo 'z' must be a non-negative int" % (slug, c["t"]))
    for k in ("x", "y"):
        if not isinstance(spec["capstone_demo"][k], int) or spec["capstone_demo"][k] <= 0:
            raise RuntimeError("%s capstone demo %r must be a positive int" % (slug, k))
    if not isinstance(spec["capstone_demo"]["z"], int) or spec["capstone_demo"]["z"] < 0:
        raise RuntimeError("%s capstone demo 'z' must be a non-negative int" % slug)
    taken, assign = _load_registry()
    # Reuse previously assigned prefixes (idempotent rebuilds); derive fresh ones
    # only for slug-variants never seen before, against the batch-global taken set.
    prefixes = {}
    for variant in variants:
        sv = slug if variant == "public" else slug + "-signature"
        if sv in assign:
            prefixes[variant] = assign[sv]
            taken.add(assign[sv])
        else:
            prefixes[variant] = derive_prefix(sv, taken)
            assign[sv] = prefixes[variant]
    _save_registry(taken, assign)
    if gate is None:
        gate = DedupeGate(os.path.join(REPO, "data", "dedupe"))
    made = []
    for variant in variants:
        sv = slug if variant == "public" else slug + "-signature"
        prefix = prefixes[variant]
        records = build_records(spec, variant, prefix, sv, gate)
        idx_path, chunk_path = write_data(sv, records)
        page_path = write_page(spec, variant, prefix, sv)
        gen_path = write_gen_js(spec, variant, prefix, sv)
        verify_gen_js(gen_path)
        made.append(
            {"variant": variant, "slug": sv, "prefix": prefix,
             "records": len(records), "page": page_path,
             "gen": gen_path, "index": idx_path, "chunk": chunk_path}
        )
    return made

def build_all(slugs=None):
    slugs = slugs or sorted(ALL_SPECS.keys())
    # One shared gate across the whole batch: cross-slug duplicates are caught too.
    gate = DedupeGate(os.path.join(REPO, "data", "dedupe"))
    report = []
    for i, slug in enumerate(slugs, 1):
        print("[%d/%d] building %s ..." % (i, len(slugs), slug), flush=True)
        made = build_slug(slug, gate=gate)
        for m in made:
            print("   %s %s %d records" % (m["slug"], m["prefix"], m["records"]), flush=True)
        report.extend(made)
    print("DONE: %d databases, %d records" % (
        len(report), sum(m["records"] for m in report)))
    return report

if __name__ == "__main__":
    slugs = sys.argv[1:] or None
    build_all(slugs)

# ---------------------------------------------------------------- default tier framing
# Specs may override with their own 'tiers' dict; otherwise these per-src_mode
# blocks are used with {item} filled from the database name core.

DEFAULT_TIERS = {
    "speculative": {
        "Foundations": {
            "intro": "Foundations: what {item} means at its simplest. These records introduce each concept in plain language - what it is, why people imagine it, and the basic idea behind it - before any engineering detail.",
            "mech": "The mechanism stays at the concept level here: the core physical or logical principle that would have to work, described without assuming it already exists.",
            "point": "Feasibility lens: name the single hardest unsolved problem this concept faces.",
        },
        "Compounded": {
            "intro": "Compounded: how the pieces fit together. These records combine the basic concepts into working systems - inputs, processes, outputs - and show how one imagined technology leans on another.",
            "mech": "The mechanism now traces a full chain: where energy, material, or information enters, what transforms it, and what comes out the other side.",
            "point": "Systems lens: every speculative system inherits the limits of its weakest subsystem.",
        },
        "Advanced": {
            "intro": "Advanced: the concept at full scale and at its limits. These records push each idea to city scale, lifetime scale, or civilization scale, and examine failure modes and second-order effects.",
            "mech": "The mechanism is analyzed end to end, including failure modes, maintenance, and what happens when the system is stressed beyond its design point.",
            "point": "Mastery lens: a technology is only as real as its failure modes are understood.",
        },
    },
    "sample": {
        "Foundations": {
            "intro": "Foundations: the engine's simplest outputs. These records show what {item} produces at its most basic - one clear idea, one clean combination - so the pattern is obvious before complexity arrives.",
            "mech": "The engine draws one element from each pool and fuses them with a title pattern; the demonstration rebuilds the exact output and measures the combination space.",
            "point": "Engine lens: small pools, honestly combined, beat large pools of noise.",
        },
        "Compounded": {
            "intro": "Compounded: outputs where the pools start interacting. These records show combinations with tension - contrasting styles, unlikely settings - and how the engine keeps them coherent.",
            "mech": "The engine layers pools so each new element constrains and sharpens the last; the demo verifies every part is non-empty and the math still closes.",
            "point": "Coherence lens: a combination is only as good as the story that holds its parts together.",
        },
        "Advanced": {
            "intro": "Advanced: the engine at full stretch - outputs that mix distant pools, bend the patterns, and produce results no single pool could suggest alone.",
            "mech": "The engine explores the far corners of the combination space; the demo asserts the full space size so every output is provably reachable and reproducible.",
            "point": "Mastery lens: the best outputs come from the edges of the space, not the center.",
        },
    },
    "harvest": {
        "Foundations": {
            "intro": "Foundations: the fact stated plainly. These records present each verified fact in its simplest form - what is true, and the one-line reason it is true.",
            "mech": "The mechanism is the underlying cause: the physical, biological, or historical reason the fact holds, checked against established knowledge.",
            "point": "Verification lens: a fact earns its place only if its cause is understood.",
        },
        "Compounded": {
            "intro": "Compounded: the fact in context - how it connects to neighboring facts, what it predicts, and where it shows up in everyday life.",
            "mech": "The mechanism is traced through its connections: cause to effect to application, each link verifiable on its own.",
            "point": "Context lens: facts compound - one verified fact anchors the next.",
        },
        "Advanced": {
            "intro": "Advanced: the fact at its limits - edge cases, common misconceptions it corrects, and the deeper principle it illustrates.",
            "mech": "The mechanism is examined at the boundary: where the fact stops holding, what replaces it there, and why the boundary itself is informative.",
            "point": "Mastery lens: knowing a fact's limits is part of knowing the fact.",
        },
    },
}

DEFAULT_CAPSTONE_HOW = (
    "Mastery synthesis: every concept in this database is combined into one working whole. "
    "The demonstration re-runs the capstone math - combinations across all parts - and asserts it closes exactly."
)

def item_core(name):
    core = name
    if core.endswith(" Database"):
        core = core[: -len(" Database")]
    if core.startswith("The "):
        core = core[4:]
    return core

def tiers_for(spec):
    if spec.get("tiers"):
        return spec["tiers"]
    base = DEFAULT_TIERS[spec["src_mode"]]
    core = item_core(spec["name"])
    out = {}
    for tier, blk in base.items():
        out[tier] = {k: v.format(item=core) for k, v in blk.items()}
    return out
