#!/usr/bin/env python3
"""Phase-Q run: assemble records, write shards, build pages, update manifest."""
import sys, os, json, gzip, subprocess, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "phone-compound-build"))
import build as BASE
_qbspec = importlib.util.spec_from_file_location("qbuild", os.path.join(HERE, "build.py"))
_qb = importlib.util.module_from_spec(_qbspec)
_qbspec.loader.exec_module(_qb)
(pub_record, sig_record, write_new_shard, append_shard) = (_qb.pub_record, _qb.sig_record, _qb.write_new_shard, _qb.append_shard)
(CIT_PUBLIC_DB, CIT_DTYPE, CIT_TOOL, CIT_TAXON, CIT_BIZARRE) = (_qb.CIT_PUBLIC_DB, _qb.CIT_DTYPE, _qb.CIT_TOOL, _qb.CIT_TAXON, _qb.CIT_BIZARRE)
(MANIFEST, API, HUB, DATA1) = (_qb.MANIFEST, _qb.API, _qb.HUB, _qb.DATA1)
from qplan import build_plan, taxon_desc, target_for
from qnewdbs import ALL_NEW, BY_SLUG
from qmap import TOOL_DBS
from qpages import write_db_files

GATE = BASE.GATE
SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"

KIND_LABEL = {
    "dbprod": "database product record", "dtype": "data type record",
    "tool": "tool record", "taxon": "taxonomy term record", "bizarre": "software record",
}
CIT = {"dbprod": CIT_PUBLIC_DB, "dtype": CIT_DTYPE, "tool": CIT_TOOL,
       "taxon": CIT_TAXON, "bizarre": CIT_BIZARRE}

report = {"filed": {}, "dupes": 0, "new_dbs": [], "appended": {}}

def check_admit(slug, title):
    hits = GATE.check(slug, title)
    if hits:
        report["dupes"] += 1
        return False
    return True

def build_pub(prefix, idx, entry, kind, group):
    e = entry
    name = e["name"]
    if e["family"] == "taxon":
        desc = taxon_desc(name, e["group"], e.get("sub", ""))
    elif e["family"] == "tool" and e["extra"].get("pub"):
        desc = e["extra"]["pub"]
    else:
        desc = e["desc"]
    title = name
    # gate on title
    return pub_record(prefix, idx, name, title, desc, KIND_LABEL[kind], CIT[kind], group)

def build_sig(prefix, idx, entry, kind, group):
    e = entry
    name = e["name"]
    if e["family"] == "taxon":
        desc = taxon_desc(name, e["group"], e.get("sub", ""))
    elif e["family"] == "tool" and e["extra"].get("sig"):
        desc = e["extra"]["sig"]
    else:
        desc = e["desc"]
    return sig_record(prefix, idx, name, name, desc, KIND_LABEL[kind], CIT[kind], group)

def main():
    plan, stats, unmapped = build_plan()
    print("plan families:", stats, "| target slugs:", len(plan), flush=True)
    manifest = json.load(open(MANIFEST))
    mdb = {x["slug"]: x for x in manifest["databases"]}

    new_cfgs = {c["slug"]: c for c in ALL_NEW}
    # group plan items: new slugs vs append slugs
    new_items = {s: items for s, items in plan.items() if s in new_cfgs}
    append_items = {s: items for s, items in plan.items() if s not in new_cfgs}

    # ---- 1. NEW databases (public + signature)
    for cfg in ALL_NEW:
        slug = cfg["slug"]
        items = new_items.get(slug, [])
        if cfg.get("signature"):
            pub_slug = slug[:-len("-signature")]
            pub_items = new_items.get(pub_slug, [])
            items = pub_items  # mirror the same source entries
        records = []
        idx = 0
        for entry, kind in items:
            if cfg.get("signature"):
                rec = build_sig(cfg["prefix"], idx + 1, entry, kind, entry["group"])
            else:
                rec = build_pub(cfg["prefix"], idx + 1, entry, kind, entry["group"])
            if not check_admit(slug, rec["title"]):
                continue
            idx += 1
            rec["id"] = "%s%06d" % (cfg["prefix"], idx)
            records.append(rec)
            GATE.admit(slug, rec["title"], rec["id"])
            report["filed"][entry["family"]] = report["filed"].get(entry["family"], 0) + 1
        n = write_new_shard(slug, records)
        report["new_dbs"].append((slug, n))
        print("new %s: %d records" % (slug, n), flush=True)

    # ---- 2. APPENDS to existing DBs (+ their signatures)
    for slug, items in sorted(append_items.items()):
        for edition, eslug in (("pub", slug), ("sig", slug + "-signature")):
            if eslug not in mdb:
                print("SKIP append, no such DB:", eslug, flush=True)
                continue
            base = mdb[eslug]["record_count"]
            prefix = mdb[eslug]["id_prefix"]
            records = []
            idx = base
            for entry, kind in items:
                rec = build_sig(prefix, idx + 1, entry, kind, entry["group"]) if edition == "sig" \
                    else build_pub(prefix, idx + 1, entry, kind, entry["group"])
                if not check_admit(eslug, rec["title"]):
                    continue
                idx += 1
                rec["id"] = "%s%06d" % (prefix, idx)
                records.append(rec)
                GATE.admit(eslug, rec["title"], rec["id"])
                report["filed"][entry["family"]] = report["filed"].get(entry["family"], 0) + 1
            n = append_shard(eslug, records)
            mdb[eslug]["record_count"] = n
            mdb[eslug]["full_records"] = n
            report["appended"][eslug] = len(records)
            print("append %s: +%d = %d" % (eslug, len(records), n), flush=True)

    # ---- 3. pages + gen-js for new DBs
    for cfg in ALL_NEW:
        slug = cfg["slug"]
        items = new_items.get(slug if not cfg.get("signature") else slug[:-len("-signature")], [])
        topics = {}
        for entry, kind in items:
            f = (entry["group"] or "general")[:40]
            topics.setdefault(f, [])
            if len(topics[f]) < 12 and entry["name"] not in topics[f]:
                topics[f].append(entry["name"])
        if not topics:
            topics = {"general": ["General Study"]}
        cfg = dict(cfg); cfg["fields"] = sorted(topics.keys())
        write_db_files(cfg, topics)
    print("pages built for %d new DBs" % len(ALL_NEW), flush=True)

    # ---- 4. manifest + api updates
    new_manifest, new_api = [], []
    for cfg in ALL_NEW:
        slug = cfg["slug"]
        n = dict(report["new_dbs"])[slug]
        me = {
            "slug": slug, "name": cfg["name"], "tagline": cfg["desc"][:140],
            "record_kind": cfg["kind"], "id_prefix": cfg["prefix"],
            "ai_name": cfg["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": n, "status": "live", "full_records": n,
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": "signature" if cfg.get("signature") else "public",
        }
        new_manifest.append(me)
        new_api.append({
            "slug": slug, "name": cfg["name"], "tagline": cfg["desc"][:140],
            "record_kind": cfg["kind"], "record_count": n, "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        })
    manifest["databases"].extend(new_manifest)
    manifest["database_count"] = len(manifest["databases"])
    json.dump(manifest, open(MANIFEST, "w"), indent=1, ensure_ascii=False)
    api = json.load(open(API))
    api["databases"].extend(new_api)
    api["database_count"] = len(api["databases"])
    json.dump(api, open(API, "w"), indent=1, ensure_ascii=False)
    print("manifest now:", len(manifest["databases"]), flush=True)

    # ---- 5. demo compile+execute sampling (one per demo archetype used)
    import tempfile
    kinds_done = set()
    for cfg in ALL_NEW[:6]:
        slug = cfg["slug"]
        p = os.path.join(DATA1, "data", slug, "chunks", "chunk-0000.jsonl.gz")
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                k = r["demo"]["kind"]
                if k in kinds_done: break
                kinds_done.add(k)
                with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tf:
                    tf.write(r["demo"]["program"]); tfp = tf.name
                pr = subprocess.run([sys.executable, tfp], capture_output=True, text=True, timeout=30)
                os.unlink(tfp)
                status = "OK" if pr.returncode == 0 else "FAIL: " + pr.stderr[:200]
                print("demo %s/%s: %s" % (slug, k, status), flush=True)
                break
    json.dump(report, open(os.path.join(HERE, "report.json"), "w"), indent=1)
    print("REPORT:", json.dumps({k: (len(v) if isinstance(v, list) else v) for k, v in report.items()}, indent=1))

if __name__ == "__main__":
    main()
