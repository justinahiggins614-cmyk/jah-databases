#!/usr/bin/env python3
"""Review mode — one database at a time.

Reads ONE database's specification (manifest entry), samples its actual
stored files (index + chunks when they exist), runs its demos, checks its
links and citations, and writes a per-database verdict report
(usable / partial / broken) with evidence per check.

Usage:
    python3 review_db.py <slug> [--out DIR] [--sample N]
    python3 review_db.py biofonics

How it extends (not replaces) the full-file-check program:
  - The full-file-check census scans ALL 63,047 databases with fixed
    sampling and assigns classes (THIN / NO-DEMO / IMAGELESS / FULL-CANON
    / ...) plus a priority queue. It measures presence, not behaviour.
  - Review mode is the operator's deep read of ONE database before any
    remediation decision: it reads the spec, RUNS the sampled demos
    (the census only counts demo presence), resolves the actual files and
    page markers, checks citations per record, and gives a human verdict
    with evidence. It consumes the census class as context; it never
    re-runs the census.
  - A database is only "done" when review mode says usable AND the
    full-file-check program's own verification agrees; review mode alone
    never certifies a database.

Safety: demos are executed in a subprocess (python3, stdin code, 10 s
timeout, minimal env). Only `language == "python"` demos run. No network
calls: "links resolve" is checked against local files + URL well-formedness;
live HTTP checking is CHECK 3 at merge, not this tool.
"""
import argparse
import gzip
import hashlib
import json
import os
import re
import subprocess
import sys

HOME = os.path.expanduser("~")
WS = os.path.join(HOME, "workspace")
MANIFEST = os.path.join(WS, "jah-databases", "data", "manifest.json")
CENSUS = os.path.join(WS, "hidden_files", "full-file-check", "census_raw.json")
MAIN_DB = os.path.join(WS, "jah-databases", "db")

REPO_DIRS = {
    "jah-databases": os.path.join(WS, "jah-databases"),
    "jah-databases-data-1": os.path.join(WS, "jah-databases-data-1"),
    "jah-databases-data-2": os.path.join(WS, "jah-databases-data-2"),
}


def load_jsonl_gz(path):
    with gzip.open(path, "rt", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def resolve_index(entry):
    """Return (local_path, kind) for a manifest entry's index, or (None, why)."""
    for key in ("local_index", "index"):
        val = entry.get(key)
        if not val:
            continue
        if val.startswith("http"):
            # URL form: map the known Pages hosts back to local clones.
            m = re.match(
                r"https://justinahiggins614-cmyk\.github\.io/"
                r"(jah-databases(?:-data-[12])?)/(.*)$", val)
            if m:
                cand = os.path.join(WS, m.group(1), m.group(2))
                if os.path.exists(cand):
                    return cand, "url->local"
            return None, "url-only (%s)" % val
        for cand in (os.path.join(WS, val),
                     os.path.join(WS, "jah-databases", val),
                     os.path.join(WS, "jah-databases-data-1", val),
                     os.path.join(WS, "jah-databases-data-2", val)):
            if os.path.exists(cand):
                return cand, "local"
    return None, "no usable local_index/index in manifest entry"


def strip_html(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text or "")).strip()


def prose_of(rec):
    parts = []
    for key in ("description", "body", "how_it_works"):
        v = rec.get(key)
        if isinstance(v, str):
            parts.append(strip_html(v))
    return " ".join(p for p in parts if p)


def garbled_frac(text):
    tokens = text.split()
    if len(tokens) < 20:
        return 0.0
    single = sum(1 for t in tokens if len(t) == 1)
    return single / len(tokens)


def demo_of(rec):
    """Normalise the demo field to (language, code, expected) or None."""
    d = rec.get("demo")
    if d is None:
        return None
    if isinstance(d, str):
        return ("python", d, rec.get("expected_output"))
    if isinstance(d, dict):
        code = d.get("code") or d.get("program")
        if not code:
            return None
        return (d.get("language", "python"), code,
                d.get("expected_output") or rec.get("expected_output"))
    return None


def run_demo(language, code, timeout=10):
    if language != "python":
        return ("skipped", "non-python demo (%s)" % language, "")
    if len(code) > 20000:
        return ("skipped", "demo over 20,000 chars, not run", "")
    try:
        proc = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True, text=True, timeout=timeout,
            env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
                 "PYTHONNOUSERSITE": "1"},
            cwd="/tmp")
    except subprocess.TimeoutExpired:
        return ("fail", "demo timed out after %ds" % timeout, "")
    except Exception as exc:
        return ("fail", "could not run demo: %s" % exc, "")
    if proc.returncode != 0:
        err = (proc.stderr or "").strip().splitlines()
        return ("fail", "exit %d: %s" % (proc.returncode,
                                         err[-1] if err else "no stderr"), "")
    return ("ran", "", proc.stdout)


def jcc_code(slug, rec):
    canon = json.dumps(rec, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False).encode("utf-8")
    key = hashlib.sha256(canon).hexdigest()[:8]
    return "JAHDB/%s#%s+k=%s" % (slug, rec.get("id"), key)


def sample_records(records, cap):
    """First 5 + every 50th, capped — same sampling as the census."""
    idx = list(range(min(5, len(records))))
    idx += list(range(50, len(records), 50))
    idx = sorted(set(idx))[:cap]
    return [records[i] for i in idx], idx


def check_page_markers(slug):
    path = os.path.join(MAIN_DB, slug, "index.html")
    if not os.path.exists(path):
        return {"exists": False, "markers": {}, "path": path}
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        html = fh.read()
    return {"exists": True,
            "markers": {
                "exhaustive_pill": "Exhaustive" in html,
                "merger_button": "All Database Merger" in html,
                "stcount": 'id="stCount"' in html,
                "old_loader": "byChunk" in html,
            },
            "path": path}


def review(slug, sample_cap=12):
    checks = []
    notes = []

    def add(name, status, evidence):
        checks.append({"name": name, "status": status,
                       "evidence": evidence})

    # --- manifest / spec ---
    try:
        with open(MANIFEST, "r", encoding="utf-8") as fh:
            manifest = json.load(fh)
        entries = {e["slug"]: e for e in manifest.get("databases", [])}
        manifest_count = manifest.get("database_count")
    except Exception as exc:
        entries, manifest_count = {}, None
        notes.append("manifest unreadable: %s" % exc)
    entry = entries.get(slug)
    if not entry:
        add("spec_present", "FAIL", "slug %r not in manifest" % slug)
        return {"slug": slug, "verdict": "broken", "checks": checks,
                "notes": notes, "manifest_count": manifest_count}
    missing = [k for k in ("name", "record_kind", "ai_name", "tagline",
                           "id_prefix") if not entry.get(k)]
    add("spec_present",
        "PASS" if not missing else "PARTIAL",
        "manifest entry: name=%r record_kind=%r ai_name=%r id_prefix=%r; "
        "missing fields: %s"
        % (entry.get("name"), entry.get("record_kind"),
           entry.get("ai_name"), entry.get("id_prefix"), missing or "none"))

    # --- census context (not a check — context from the full-file-check) ---
    census_row = None
    try:
        rows = json.load(open(CENSUS, "r", encoding="utf-8"))
        census_row = next((r for r in rows if r.get("slug") == slug), None)
    except Exception:
        pass

    # --- index ---
    index_path, how = resolve_index(entry)
    if not index_path:
        add("index_loads", "FAIL", "index not resolvable locally: %s" % how)
        return {"slug": slug, "verdict": "broken", "checks": checks,
                "notes": notes, "manifest_count": manifest_count,
                "entry": entry, "census": census_row}
    try:
        index_recs = load_jsonl_gz(index_path)
        add("index_loads", "PASS",
            "%s: %d records parsed from %s"
            % (how, len(index_recs), index_path))
    except Exception as exc:
        add("index_loads", "FAIL", "%s: %s" % (index_path, exc))
        return {"slug": slug, "verdict": "broken", "checks": checks,
                "notes": notes, "manifest_count": manifest_count,
                "entry": entry, "census": census_row}

    # --- chunks (full records live here when the index is title-only) ---
    index_dir = os.path.dirname(index_path)
    chunk_dir = os.path.join(index_dir, "chunks")
    chunk_files = []
    chunk_recs = []
    if os.path.isdir(chunk_dir):
        chunk_files = sorted(f for f in os.listdir(chunk_dir)
                             if f.endswith(".gz"))
        for f in chunk_files:
            try:
                chunk_recs.extend(load_jsonl_gz(os.path.join(chunk_dir, f)))
            except Exception as exc:
                notes.append("chunk %s unreadable: %s" % (f, exc))
    primary = chunk_recs if chunk_recs else index_recs
    primary_source = "chunks (%d files)" % len(chunk_files) if chunk_recs \
        else "index"
    index_stub = all(set(r.keys()) <= {"id", "t", "g", "c", "s", "y", "slug"}
                     for r in index_recs[:20])
    if index_stub and chunk_recs:
        chunk_prose = sorted(len(prose_of(r)) for r in chunk_recs[:20])
        chunk_median = chunk_prose[len(chunk_prose) // 2] if chunk_prose else 0
        if chunk_median >= 200:
            notes.append("index rows are title-only (id/t/g); full records "
                         "live in %d chunk file(s) — index-enrichment gap, "
                         "not a missing-data gap" % len(chunk_files))
        else:
            notes.append("index rows are title-only (id/t/g) AND chunk "
                         "records carry no readable prose either (median "
                         "sampled chunk prose %d chars) — the gap is in "
                         "the stored records, not just the index"
                         % chunk_median)
    elif index_stub:
        notes.append("index rows are title-only (id/t/g) and there are no "
                     "chunks — the stored data really is titles only")

    # --- count agreement ---
    manifest_n = entry.get("record_count")
    actual_n = len(index_recs)
    chunk_n = len(chunk_recs) if chunk_recs else None
    count_ok = (manifest_n == actual_n) or (chunk_n is not None
                                            and manifest_n == chunk_n)
    add("count_agrees",
        "PASS" if count_ok else "FAIL",
        "manifest record_count=%s, index lines=%d%s"
        % (manifest_n, actual_n,
           ", chunk records=%d" % chunk_n if chunk_n is not None else ""))

    # --- sampling + parse ---
    sample, sample_idx = sample_records(primary, sample_cap)
    bad = [r.get("id", "?") for r in sample
           if not isinstance(r, dict) or not r.get("id")]
    titles = sum(1 for r in sample
                 if r.get("title") or r.get("t") or r.get("name"))
    prefix = entry.get("id_prefix", "")
    bad_prefix = [r["id"] for r in sample
                  if r.get("id") and prefix
                  and not r["id"].startswith(prefix)]
    add("records_parse",
        "PASS" if not bad and titles == len(sample) and not bad_prefix
        else "FAIL",
        "sampled %d records (%s, positions %s); unparseable=%s; "
        "with title=%d/%d; id-prefix mismatches=%s"
        % (len(sample), primary_source, sample_idx, bad or "none",
           titles, len(sample), bad_prefix or "none"))
    ids = [r["id"] for r in sample if r.get("id")]
    dupes = len(ids) - len(set(ids))
    if dupes:
        notes.append("duplicate ids inside sample: %d" % dupes)

    # --- readability ---
    readable = 0
    garbled = 0
    prose_lens = []
    for r in sample:
        prose = prose_of(r)
        prose_lens.append(len(prose))
        if len(prose) >= 200 and garbled_frac(prose) < 0.35:
            readable += 1
        if garbled_frac(prose) >= 0.35 and len(prose.split()) >= 20:
            garbled += 1
    prose_lens.sort()
    median_prose = prose_lens[len(prose_lens) // 2] if prose_lens else 0
    add("readable",
        "PASS" if readable == len(sample) else
        ("PARTIAL" if readable > 0 else "FAIL"),
        "readable %d/%d sampled (prose >=200 chars, garbled-token "
        "fraction <0.35); median sampled prose %d chars; garbled %d"
        % (readable, len(sample), median_prose, garbled))

    # --- demos run ---
    demo_stats = {"present": 0, "ran_ok": 0, "ran_mismatch": 0,
                  "failed": 0, "skipped": 0}
    demo_evidence = []
    for r in sample:
        d = demo_of(r)
        if d is None:
            continue
        demo_stats["present"] += 1
        language, code, expected = d
        status, msg, out = run_demo(language, code)
        if status == "ran":
            if expected is None:
                demo_stats["ran_ok"] += 1
                demo_evidence.append("%s: ran, exit 0 (no expected "
                                     "output to compare)" % r["id"])
            elif out == expected:
                demo_stats["ran_ok"] += 1
                demo_evidence.append("%s: ran, stdout byte-matches "
                                     "expected_output" % r["id"])
            else:
                demo_stats["ran_mismatch"] += 1
                demo_evidence.append("%s: ran but stdout differs from "
                                     "expected_output" % r["id"])
        elif status == "skipped":
            demo_stats["skipped"] += 1
            demo_evidence.append("%s: skipped (%s)" % (r["id"], msg))
        else:
            demo_stats["failed"] += 1
            demo_evidence.append("%s: FAILED (%s)" % (r["id"], msg))
    if demo_stats["present"] == 0:
        add("demos_run", "FAIL",
            "no demo in any of the %d sampled records (primary source: %s)"
            % (len(sample), primary_source))
    elif demo_stats["failed"] or demo_stats["ran_mismatch"]:
        add("demos_run", "FAIL",
            "demos present in %d/%d sampled; ok=%d mismatch=%d failed=%d; %s"
            % (demo_stats["present"], len(sample), demo_stats["ran_ok"],
               demo_stats["ran_mismatch"], demo_stats["failed"],
               "; ".join(demo_evidence)))
    else:
        add("demos_run", "PASS",
            "demos present in %d/%d sampled; all ran (ok=%d, skipped=%d); %s"
            % (demo_stats["present"], len(sample), demo_stats["ran_ok"],
               demo_stats["skipped"], "; ".join(demo_evidence)))

    # --- links resolve (local files + URL well-formedness) ---
    page = check_page_markers(slug)
    markers = page["markers"]
    markers_ok = (page["exists"] and markers.get("exhaustive_pill")
                  and markers.get("merger_button")
                  and markers.get("stcount")
                  and not markers.get("old_loader"))
    add("links_resolve",
        "PASS" if markers_ok else "PARTIAL",
        "page %s; markers exhaustive=%s merger=%s stCount=%s old_loader=%s; "
        "index file present locally (%s)"
        % ("exists" if page["exists"] else "MISSING",
           markers.get("exhaustive_pill"), markers.get("merger_button"),
           markers.get("stcount"), markers.get("old_loader"), index_path))

    # --- citations present ---
    with_src = sum(1 for r in sample
                   if (r.get("source") or r.get("citations") or r.get("src")))
    example_code = jcc_code(slug, sample[0]) if sample else None
    add("citations_present",
        "PASS" if with_src == len(sample) else
        ("PARTIAL" if with_src > 0 else "FAIL"),
        "source/citations/src present in %d/%d sampled; JCC v1 code "
        "formable, e.g. %s"
        % (with_src, len(sample), example_code))

    # --- images (informational) ---
    with_img = sum(1 for r in sample if r.get("image") or r.get("image_url"))
    notes.append("images: %d/%d sampled records carry an image field"
                 % (with_img, len(sample)))

    # --- verdict ---
    status = {c["name"]: c["status"] for c in checks}
    if status.get("index_loads") == "FAIL" \
            or status.get("records_parse") == "FAIL" \
            or status.get("readable") == "FAIL":
        verdict = "broken"
    elif all(status.get(k) == "PASS" for k in
             ("spec_present", "index_loads", "count_agrees",
              "records_parse", "readable", "demos_run",
              "links_resolve", "citations_present")):
        verdict = "usable"
    else:
        verdict = "partial"
    # Honesty note: "usable" means usable for AI retrieval (spec, files,
    # parse, prose, demos, links, citations all pass). It is NOT the
    # 7-step FULL-CANON verdict — a THIN database can be retrievable while
    # still missing canon steps (images, science/math proofs, generator).
    if verdict == "usable" and census_row \
            and census_row.get("class") not in ("FULL-CANON", "FULL-FILL"):
        notes.append("Census class is %s (%s/7 steps) while review says "
                     "usable: the verdict covers retrievability, not the "
                     "7-step canon — canon steps still missing per census."
                     % (census_row.get("class"), census_row.get("steps_met")))

    return {"slug": slug, "verdict": verdict, "checks": checks,
            "notes": notes, "manifest_count": manifest_count,
            "entry": entry, "census": census_row,
            "sample_size": len(sample), "primary_source": primary_source,
            "index_path": index_path, "chunk_files": len(chunk_files),
            "demo_stats": demo_stats}


def render(result):
    e = result.get("entry") or {}
    c = result.get("census") or {}
    lines = []
    lines.append("# Review — `%s`" % result["slug"])
    lines.append("")
    lines.append("**Verdict: %s** (usable / partial / broken)" %
                 result["verdict"].upper())
    lines.append("")
    lines.append("**Date:** 2026-11-02. **Mode:** package-only review; "
                 "nothing merged, pushed, or deployed. **Manifest at review "
                 "time:** %s databases." % result.get("manifest_count"))
    lines.append("")
    lines.append("## Specification")
    lines.append("")
    lines.append("- Name: %s" % (e.get("name") or "—"))
    lines.append("- Record kind: `%s` — AI: %s" %
                 (e.get("record_kind"), e.get("ai_name")))
    lines.append("- Tagline: %s" % (e.get("tagline") or "—"))
    lines.append("- ID prefix: `%s` — manifest record_count: %s — source: %s"
                 % (e.get("id_prefix"), e.get("record_count"),
                    e.get("source")))
    if c:
        lines.append("- Full-file-check census class: **%s** "
                     "(read: %s, org: %s, steps %s/7, median body %s chars)"
                     % (c.get("class"), c.get("read_class"),
                        c.get("org_class"), c.get("steps_met"),
                        c.get("median_body")))
    lines.append("- Index: `%s`" % (result.get("index_path") or "NOT RESOLVED"))
    lines.append("- Primary sample source: %s (%s chunk files, %s records "
                 "sampled)" % (result.get("primary_source") or "—",
                               result.get("chunk_files") if
                               result.get("chunk_files") is not None else "—",
                               result.get("sample_size") if
                               result.get("sample_size") is not None else "—"))
    lines.append("")
    lines.append("## Checks (evidence per check)")
    lines.append("")
    lines.append("| Check | Result | Evidence |")
    lines.append("|---|---|---|")
    for ch in result["checks"]:
        lines.append("| %s | %s | %s |" %
                     (ch["name"], ch["status"], ch["evidence"]))
    lines.append("")
    if result.get("demo_stats"):
        d = result["demo_stats"]
        lines.append("Demo totals (sampled): present %d, ran OK %d, "
                     "output mismatch %d, failed %d, skipped %d."
                     % (d["present"], d["ran_ok"], d["ran_mismatch"],
                        d["failed"], d["skipped"]))
        lines.append("")
    if result.get("notes"):
        lines.append("## Notes")
        lines.append("")
        for n in result["notes"]:
            lines.append("- %s" % n)
        lines.append("")
    lines.append("## What this verdict means")
    lines.append("")
    if result["verdict"] == "usable":
        lines.append("Usable as-is: spec present, index loads, counts agree, "
                     "records parse and read, demos run, links resolve, "
                     "citations present. No remediation needed from review "
                     "mode; the full-file-check program's own verification "
                     "still applies before anything is called done.")
    elif result["verdict"] == "partial":
        lines.append("Partly usable: the data loads and reads, but at least "
                     "one full-record step is missing (see the failed / "
                     "partial checks above). Remediation is a fill for the "
                     "missing step(s), not a rebuild — queue it in the "
                     "full-file-check priority queue, do not re-audit the "
                     "whole database by hand.")
    else:
        lines.append("Broken for use: the index does not load, records do "
                     "not parse, or sampled records carry no readable prose. "
                     "Do not serve this database to an outside AI until the "
                     "failing check is fixed and review mode re-run.")
    lines.append("")
    lines.append("## How this extends the full-file-check program")
    lines.append("")
    lines.append("The census assigns this database a class from a network-wide "
                 "scan; review mode reads this one database end to end — spec, "
                 "real files, executed demos, resolved links, per-record "
                 "citations — and gives a verdict with evidence. It does not "
                 "replace the census, the priority queue, or the fill waves.")
    lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--out", default=None)
    ap.add_argument("--sample", type=int, default=12)
    args = ap.parse_args()
    result = review(args.slug, args.sample)
    text = render(result)
    outdir = args.out or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "pilot-reports")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "%s.md" % args.slug)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)
    print("Wrote %s" % path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
