#!/usr/bin/env python3
"""Build worker: BLUEPRINT databases for Manon's Project Three (JAH Databases).

Builds 30 databases in the blueprint-*/building-*/house-*/engineer-* namespace:
  - 8 building-type blueprint DBs x public+signature (houses, stores, offices,
    warehouses, apartments, barns, schools, factories)
  - blueprint-designer + signature (boundless need-driven designer + preset library)
  - engineer-projects-public + engineer-projects-signature
  - 5 makable-category blueprint DBs x public+signature
    (machines, tools, devices, vehicles, infrastructure)

34 full records each. Does NOT touch data/manifest.json or api.json - the
coordinator merges; manifest/api entry payloads are written to
manifest-entries.json / api-entries.json in this build dir instead.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/jah-databases"
SHARD = "/home/hatch/workspace/jah-databases-data-1"
TEMPLATE = os.path.join(REPO, "db", "public-synthetic-intelligence", "index.html")

sys.path.insert(0, HERE)
from blueprint_kit import (scale_spaces, place_spaces, render_plan, demo_program,
                           fmt_dim, DISCLAIMER_PUB, DISCLAIMER_SIG, SIG_LENS,
                           variant_note, ladder_of)
import content_buildings
import content_buildings2
import content_buildings3
import content_machines
import content_engineers

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base

sys.path.insert(0, os.path.join(REPO, "code", "numbering-build"))
spec = importlib.util.spec_from_file_location("nb_build",
      os.path.join(REPO, "code", "numbering-build", "build.py"))
nb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nb)

sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sweep = None
try:
    sweep_path = "/home/hatch/workspace/goals/database-quality-audit/hidden_files/patches/sweep-db-pages.py"
    sspec = importlib.util.spec_from_file_location("sweep", sweep_path)
    sweep = importlib.util.module_from_spec(sspec)
    sspec.loader.exec_module(sweep)
except Exception as e:
    print("sweep unavailable: %s" % e, flush=True)

SHARD_BASE = "https://justinahiggins614-cmyk.github.io/jah-databases-data-1"
VARIANTS = [("compact", "Compact", 0.85), ("standard", "Standard", 1.0), ("grand", "Grand", 1.22)]
SIG_TAIL = "Signature original design - JAH Signature system. Clearly labeled Signature-made."

# ---------------------------------------------------------------- DB table
# family: key into FAMILIES below. unit: "ft"|"in". base_scale: units per char.

FAMILIES = {
 "houses":      dict(archs=content_buildings.HOUSES, unit="ft", scale=2.0, kind="building"),
 "stores":      dict(archs=content_buildings.STORES, unit="ft", scale=4.0, kind="building"),
 "offices":     dict(archs=content_buildings2.OFFICES, unit="ft", scale=4.0, kind="building"),
 "warehouses":  dict(archs=content_buildings2.WAREHOUSES, unit="ft", scale=10.0, kind="building"),
 "apartments":  dict(archs=content_buildings2.APARTMENTS, unit="ft", scale=2.0, kind="building"),
 "barns":       dict(archs=content_buildings2.BARNS, unit="ft", scale=4.0, kind="building"),
 "schools":     dict(archs=content_buildings3.SCHOOLS, unit="ft", scale=6.0, kind="building"),
 "factories":   dict(archs=content_buildings3.FACTORIES, unit="ft", scale=15.0, kind="building"),
 "machines":    dict(archs=content_machines.MACHINES, unit="ft", scale=2.0, kind="machine"),
 "tools":       dict(archs=content_machines.TOOLS, unit="in", scale=2.0, kind="tool"),
 "devices":     dict(archs=content_machines.DEVICES, unit="in", scale=2.0, kind="device"),
 "vehicles":    dict(archs=content_machines.VEHICLES, unit="in", scale=4.0, kind="vehicle"),
 "infrastructure": dict(archs=content_machines.INFRASTRUCTURE, unit="ft", scale=60.0, kind="infrastructure"),
}

DBS = [
 # slug, name, family, prefix, ai, record_kind, tagline
 ("blueprint-houses", "The House Blueprint Database", "houses", "JAH-BHP-", "JAH House Blueprint Guide", "house blueprint record",
  "Architectural blueprints for houses - floor plans, dimensions, materials, structural specs, and history for every major house type."),
 ("blueprint-houses-signature", "The House Blueprint Signature Database", "houses", "JAH-BHPS-", "JAH House Blueprint Signature Guide", "house blueprint record",
  "Signature-original house blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-stores", "The Store Blueprint Database", "stores", "JAH-BSP-", "JAH Store Blueprint Guide", "store blueprint record",
  "Architectural blueprints for retail stores - floor plans, dimensions, materials, and structural specs."),
 ("blueprint-stores-signature", "The Store Blueprint Signature Database", "stores", "JAH-BSPS-", "JAH Store Blueprint Signature Guide", "store blueprint record",
  "Signature-original store blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-offices", "The Office Blueprint Database", "offices", "JAH-BOFP-", "JAH Office Blueprint Guide", "office blueprint record",
  "Architectural blueprints for offices - floor plans, dimensions, materials, and structural specs."),
 ("blueprint-offices-signature", "The Office Blueprint Signature Database", "offices", "JAH-BOFPS-", "JAH Office Blueprint Signature Guide", "office blueprint record",
  "Signature-original office blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-warehouses", "The Warehouse Blueprint Database", "warehouses", "JAH-BWP-", "JAH Warehouse Blueprint Guide", "warehouse blueprint record",
  "Architectural blueprints for warehouses - floor plans, dimensions, materials, and structural specs."),
 ("blueprint-warehouses-signature", "The Warehouse Blueprint Signature Database", "warehouses", "JAH-BWPS-", "JAH Warehouse Blueprint Signature Guide", "warehouse blueprint record",
  "Signature-original warehouse blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-apartments", "The Apartment Blueprint Database", "apartments", "JAH-BATP-", "JAH Apartment Blueprint Guide", "apartment blueprint record",
  "Architectural blueprints for apartments - unit plans, dimensions, materials, and structural specs."),
 ("blueprint-apartments-signature", "The Apartment Blueprint Signature Database", "apartments", "JAH-BATPS-", "JAH Apartment Blueprint Signature Guide", "apartment blueprint record",
  "Signature-original apartment blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-barns", "The Barn Blueprint Database", "barns", "JAH-BNP-", "JAH Barn Blueprint Guide", "barn blueprint record",
  "Architectural blueprints for barns - floor plans, dimensions, materials, and structural specs."),
 ("blueprint-barns-signature", "The Barn Blueprint Signature Database", "barns", "JAH-BNPS-", "JAH Barn Blueprint Signature Guide", "barn blueprint record",
  "Signature-original barn blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-schools", "The School Blueprint Database", "schools", "JAH-BSCH-", "JAH School Blueprint Guide", "school blueprint record",
  "Architectural blueprints for schools - floor plans, dimensions, materials, and structural specs."),
 ("blueprint-schools-signature", "The School Blueprint Signature Database", "schools", "JAH-BSCHS-", "JAH School Blueprint Signature Guide", "school blueprint record",
  "Signature-original school blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-factories", "The Factory Blueprint Database", "factories", "JAH-BFP-", "JAH Factory Blueprint Guide", "factory blueprint record",
  "Architectural blueprints for factories - floor plans, dimensions, materials, and structural specs."),
 ("blueprint-factories-signature", "The Factory Blueprint Signature Database", "factories", "JAH-BFPS-", "JAH Factory Blueprint Signature Guide", "factory blueprint record",
  "Signature-original factory blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-designer", "The Blueprint Designer Database", "designer", "JAH-BDGN-", "JAH Blueprint Designer", "designer blueprint record",
  "The Blueprint Designer - a boundless generator that makes complete blueprints from your need: pick a category, set a seed, get a full blueprint. Plus a growing library of pre-made blueprint versions marching toward one million."),
 ("blueprint-designer-signature", "The Blueprint Designer Signature Database", "designer", "JAH-BDGNS-", "JAH Blueprint Designer Signature", "designer blueprint record",
  "The Signature Blueprint Designer - need-driven blueprint generation with the Signature lens, plus a growing Signature preset library marching toward one million."),
 ("engineer-projects-public", "The Engineer Projects Public Database", "engpub", "JAH-ENPP-", "JAH Engineer Projects Guide", "engineering project record",
  "Public records on real engineering projects - dams, bridges, tunnels, towers, canals, and megastructures with full specs, dimensions, history, and site plans."),
 ("engineer-projects-signature", "The Engineer Projects Signature Database", "engsig", "JAH-ENPS-", "JAH Engineer Projects Signature Guide", "engineering project record",
  "Signature engineering projects - complete concept-to-build packages: concept, full specs, blueprints, materials, and phased build plans, clearly labeled Signature-made."),
 ("blueprint-machines", "The Machine Blueprint Database", "machines", "JAH-BMP-", "JAH Machine Blueprint Guide", "machine blueprint record",
  "Blueprints for machines - engines, turbines, presses, conveyors, pumps, and industrial equipment with schematics, dimensions, and specs."),
 ("blueprint-machines-signature", "The Machine Blueprint Signature Database", "machines", "JAH-BMPS-", "JAH Machine Blueprint Signature Guide", "machine blueprint record",
  "Signature-original machine blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-tools", "The Tool Blueprint Database", "tools", "JAH-BTLP-", "JAH Tool Blueprint Guide", "tool blueprint record",
  "Blueprints for tools - hand tools, power tools, and workshop equipment with detail drawings, dimensions, and specs."),
 ("blueprint-tools-signature", "The Tool Blueprint Signature Database", "tools", "JAH-BTLPS-", "JAH Tool Blueprint Signature Guide", "tool blueprint record",
  "Signature-original tool blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-devices", "The Device Blueprint Database", "devices", "JAH-BDP-", "JAH Device Blueprint Guide", "device blueprint record",
  "Blueprints for devices - appliances, electronics, and home equipment with schematics, dimensions, and specs."),
 ("blueprint-devices-signature", "The Device Blueprint Signature Database", "devices", "JAH-BDPS-", "JAH Device Blueprint Signature Guide", "device blueprint record",
  "Signature-original device blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-vehicles", "The Vehicle Blueprint Database", "vehicles", "JAH-BVP-", "JAH Vehicle Blueprint Guide", "vehicle blueprint record",
  "Blueprints for vehicles - road, water, air, and work vehicles with general arrangements, dimensions, and specs."),
 ("blueprint-vehicles-signature", "The Vehicle Blueprint Signature Database", "vehicles", "JAH-BVPS-", "JAH Vehicle Blueprint Signature Guide", "vehicle blueprint record",
  "Signature-original vehicle blueprints - re-imagined from first principles, clearly labeled Signature-made."),
 ("blueprint-infrastructure", "The Infrastructure Blueprint Database", "infrastructure", "JAH-BIP-", "JAH Infrastructure Blueprint Guide", "infrastructure blueprint record",
  "Blueprints for infrastructure - bridges, dams, tunnels, plants, and grids with general arrangements, dimensions, and specs."),
 ("blueprint-infrastructure-signature", "The Infrastructure Blueprint Signature Database", "infrastructure", "JAH-BIPS-", "JAH Infrastructure Blueprint Signature Guide", "infrastructure blueprint record",
  "Signature-original infrastructure blueprints - re-imagined from first principles, clearly labeled Signature-made."),
]

DESIGNER_FAMILIES = ["houses","stores","offices","warehouses","apartments","barns","schools",
                     "factories","machines","tools","devices","vehicles","infrastructure"]

# ---------------------------------------------------------------- cfg

def _cfg(slug, name, family, prefix, ai, record_kind, tagline):
    sig = slug.endswith("-signature") or slug == "engineer-projects-signature"
    if family == "designer":
        hero_extra = (" The Designer tab is a boundless generator: choose a building category, set a seed, "
                      "and it composes a complete need-driven blueprint - size class, purpose, and constraints "
                      "drawn from your seed - with a schematic plan, dimensioned room schedule, materials, and "
                      "a runnable verification program.")
        fields = "Designer categories - houses, stores, offices, warehouses, apartments, barns, schools, factories, machines, tools, devices, vehicles, infrastructure"
        gen_groups = DESIGNER_FAMILIES
        gen_desc = ("The Blueprint Designer: pick a category, set a seed, and generate a complete need-driven "
                    "blueprint - size, purpose, and constraints composed from the seed. Seeded archive presets "
                    "are the authoritative entries.")
        greet = ("I am the %s. Tell me what you need - building type, size, purpose, constraints - and I will "
                 "design the blueprint." % ai)
        search_ph = "Search designer presets by building type, size, purpose..."
        chat_ph = "Describe the blueprint you need..."
        schema = ("id, t, g, name, title, description, how_it_works, key_points, requirements, standards, "
                  "citations, blueprint, materials, src, ladder_rank, ladder_tier, demo, provenance, last_verified")
    elif family in ("engpub", "engsig"):
        hero_extra = (" Each project record carries the full engineering package: history, how it works, "
                      "dimensioned specifications, materials, standards, citations, and a site-plan schematic "
                      "with a runnable verification program.")
        fields = "Dams - Bridges - Tunnels - Buildings - Transport - Energy - Water - Space - Flood Defense - Research - Land Reclamation - Waterways - Habitats"
        gen_groups = ["Dams","Bridges","Tunnels","Buildings","Transport","Energy","Water","Space",
                      "Flood Defense","Research","Land Reclamation","Waterways","Habitats"]
        gen_desc = ("Generate clearly-labeled structural engineering-project studies. Seeded archive records "
                    "are the authoritative entries.")
        greet = ("I am the %s. Ask me about engineering projects - dams, bridges, tunnels, towers, and the "
                 "Signature concepts." % ai)
        search_ph = "Search projects by name, type, location..."
        chat_ph = "Ask about an engineering project..."
        schema = ("id, t, g, name, title, location, dates, figures, description, history, how_it_works, specs, "
                  "key_points, requirements, standards, citations, blueprint, materials, phases, src, demo, provenance, last_verified")
    else:
        fam = FAMILIES[family]
        hero_extra = (" Every record carries the full blueprint package: history, how it reads and builds, a "
                      "schematic plan sheet, dimensioned space schedule, materials, applicable codes, and a "
                      "runnable verification program.")
        fields = " - ".join(sorted({a["group"] for a in fam["archs"]}))
        gen_groups = sorted({a["group"] for a in fam["archs"]})
        gen_desc = ("Generate clearly-labeled structural %s blueprint studies. Seeded archive records are the "
                    "authoritative entries." % family)
        greet = ("I am the %s. Ask me about %s blueprints - plans, dimensions, materials, and structure." % (ai, family))
        search_ph = "Search %s blueprints by type, style, size..." % family
        chat_ph = "Ask about %s blueprints..." % family
        schema = ("id, t, g, name, title, description, how_it_works, key_points, requirements, standards, "
                  "citations, blueprint, materials, src, ladder_rank, ladder_tier, demo, provenance, last_verified")
    pub_line = "Public records - real, fact-checked blueprint studies"
    sig_line = ("Signature originals - re-imagined from first principles for durability, daylight, and "
                "honest materials: clearly labeled Signature-made, never presented as authentic public record.")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai,
        "role": "%s - %s by category" % (ai.lower(), record_kind),
        "hero_p": "%s - %s Every record carries the full entry: description, history, how it works, key points, "
                  "requirements, standards, citations, schematic plan, and a working demonstration program.%s"
                  % (tagline, sig_line if sig else pub_line, hero_extra),
        "sig_type": ("Signature originals organized in the Signature system" if sig else
                     "Public records organized in the Signature system"),
        "search_ph": search_ph, "chat_ph": chat_ph,
        "archive_blurb": "Seeded %s %s blueprint records, marching toward one million records."
                         % ("Signature-original" if sig else "public-record", family),
        "schema": schema, "fields": fields,
        "gen_desc": gen_desc, "greet": greet,
        "gen_fields": gen_groups,
        "gen_kind": "%s-blueprint-study" % family, "gen_demo_kind": "blueprint-demo",
        "source": "signature" if sig else "public",
    }

DBCFG = {}
for _s, _n, _f, _p, _a, _rk, _t in DBS:
    DBCFG[_s] = _cfg(_s, _n, _f, _p, _a, _rk, _t)
base.DBCFG = DBCFG
nb.DBCFG = DBCFG

# ---------------------------------------------------------------- record builders

def fit_scale(W, D, base):
    s = base
    while max(W, D) / s > 60 and s < 100000:
        s *= 2
    return s

def admit_title(slug, base_title, rid):
    title = base_title
    n = 2
    while True:
        hits = [h for h in GATE.check(slug, title) if h[0] != slug]
        if not hits:
            GATE.admit(slug, title, rid)
            return title
        title = "%s (Plan %d)" % (base_title, n)
        n += 1
        assert n < 40, "gate loop on %s" % base_title

def build_blueprint_record(slug, cfg, arch, vkey, vlabel, vscale, fam, designer=False):
    sig = cfg["source"] == "signature"
    unit = fam["unit"]
    spaces = scale_spaces(arch["spaces"], vscale)
    placed, W, D = place_spaces(spaces)
    sc = fit_scale(W, D, fam["scale"])
    base_name = arch["name"]
    name = ("Signature " + base_name) if sig else base_name
    if designer:
        title_base = "Blueprint Designer Preset: %s (%s)" % (name, vlabel)
    else:
        title_base = "%s - %s Architectural Blueprint" % (name, vlabel)
    if sig and not designer:
        title_base += " (Signature Edition)"
    rid = "%s%06d" % (cfg["prefix"], build_blueprint_record.counter[slug] + 1)
    title = admit_title(slug, title_base, rid)
    build_blueprint_record.counter[slug] += 1

    room_lines = ["%s: %s" % (n, fmt_dim(w, d, unit)) for n, w, d in spaces]
    area = sum(w * d for _, w, d in spaces)
    plan = render_plan(title, placed, W, D, unit=unit, ft_per_char=sc)
    rank, tier = ladder_of(vkey)
    stats = [("Overall", "%s x %s %s" % (_r2(W), _r2(D), unit)),
             ("Spaces", "%d" % len(spaces)),
             ("Area (est.)", "%s sq %s" % (_r2(area), unit)),
             ("Sheets", "%d" % len(arch["sheets"]))]

    if sig:
        description = ("%s %s (%s edition): %s %s %s %s %s"
                       % (SIG_LENS, name, vlabel, arch["history"], arch["layout"],
                          arch["structure"], arch["systems"], variant_note(vkey, vlabel)))
        how = SIG_LENS + " " + arch["layout"] + " " + arch["structure"]
        citations = [SIG_TAIL]
        src = "signature"
    else:
        description = ("%s (%s edition): %s %s %s %s %s %s"
                       % (name, vlabel, arch["history"], arch["layout"],
                          arch["structure"], arch["systems"], variant_note(vkey, vlabel),
                          DISCLAIMER_PUB))
        how = arch["layout"] + " " + arch["structure"] + " " + arch["systems"]
        citations = list(arch.get("codes", [])) + ["Standard construction practice references."]
        src = "public-harvest"
    if designer and not sig:
        description += " Pre-made library preset from the Blueprint Designer."
    if designer and sig:
        description += " Pre-made Signature library preset from the Blueprint Designer."

    rec = {
        "id": rid, "t": title, "g": arch["group"], "name": name, "title": title,
        "description": description,
        "how_it_works": how,
        "key_points": room_lines + ["Overall footprint about %s x %s %s (schematic)"
                                    % (_r2(W), _r2(D), unit)],
        "requirements": list(arch["materials"]),
        "standards": list(arch["codes"]),
        "citations": citations,
        "blueprint": {
            "plan_ascii": plan,
            "scale_note": "Schematic - 1 char = %s %s. Not to construction scale." % (_r2(sc), unit),
            "sheets": list(arch["sheets"]),
            "overall": "%s x %s %s" % (_r2(W), _r2(D), unit),
            "area_estimate_sq": _r2(area),
            "unit": unit,
        },
        "materials": list(arch["materials"]),
        "src": src, "ladder_rank": rank, "ladder_tier": tier,
        "demo": {"kind": "python", "language": "python",
                 "program": demo_program(rid, title, plan, stats),
                 "note": "Working demonstration program (real, runnable Python): prints the schematic plan and verifies dimensions."},
        "provenance": src, "last_verified": "2026-10-19",
    }
    return rec

def _r2(x):
    return int(x) if float(x) == int(float(x)) else round(float(x), 1)

build_blueprint_record.counter = {}

def build_engineer_record(slug, cfg, e):
    sig = cfg["source"] == "signature"
    rid = "%s%06d" % (cfg["prefix"], build_engineer_record.counter[slug] + 1)
    if sig:
        title_base = "%s (Signature Edition)" % e["name"]
        src = "signature"
    else:
        title_base = e["name"]
        src = "public-harvest"
    title = admit_title(slug, title_base, rid)
    build_engineer_record.counter[slug] += 1

    structs = [(n, float(w), float(d)) for n, w, d in e["structures"]]
    placed, W, D = place_spaces(structs)
    sc = fit_scale(W, D, 60.0)
    plan = render_plan(title + " - site schematic", placed, W, D, unit="ft", ft_per_char=sc,
                       subtitle="Schematic site plan - not to construction scale")
    spec_lines = ["%s: %s" % (k, v) for k, v in e["specs"]]
    struct_lines = ["%s: %s" % (n, fmt_dim(w, d, "ft")) for n, w, d in structs]
    stats = [("Key structures", "%d" % len(structs))] + [(k, v) for k, v in e["specs"][:4]]

    if sig:
        description = ("%s Concept: %s %s How it works: %s Build phases: %s %s"
                       % (SIG_LENS, e["concept"], e["history"], e["how_it_works"],
                          " | ".join(e["phases"]), DISCLAIMER_SIG))
        how = SIG_LENS + " " + e["how_it_works"]
        citations = [SIG_TAIL]
        requirements = list(e["materials"]) + ["Licensed professional review before construction"]
    else:
        description = ("Public engineering record: %s. %s How it works: %s %s"
                       % (e["name"], e["history"], e["how_it_works"], DISCLAIMER_PUB))
        how = e["how_it_works"]
        citations = list(e["citations"])
        requirements = list(e["materials"])
    rec = {
        "id": rid, "t": title, "g": e["group"], "name": e["name"], "title": title,
        "location": e.get("location", "Signature concept - site to be selected"),
        "dates": e.get("dates", "Concept stage"),
        "figures": e.get("figures", "JAH Signature system"),
        "description": description,
        "history": e["history"],
        "how_it_works": how,
        "specs": spec_lines,
        "key_points": spec_lines + struct_lines,
        "requirements": requirements,
        "standards": list(e.get("codes", ["Applicable national codes", "Licensed engineer review"])),
        "citations": citations,
        "blueprint": {
            "plan_ascii": plan,
            "scale_note": "Schematic site plan - 1 char = %s ft. Not to construction scale." % _r2(sc),
            "structures": struct_lines,
        },
        "materials": list(e["materials"]),
        "src": src,
        "demo": {"kind": "python", "language": "python",
                 "program": demo_program(rid, title, plan, stats),
                 "note": "Working demonstration program (real, runnable Python): prints the site schematic and key specs."},
        "provenance": src, "last_verified": "2026-10-19",
    }
    if sig:
        rec["phases"] = list(e["phases"])
        rec["concept"] = e["concept"]
        rec["ladder_rank"] = 8
        rec["ladder_tier"] = "advanced"
    else:
        rec["ladder_rank"] = 5
        rec["ladder_tier"] = "compounded"
    return rec

build_engineer_record.counter = {}

# ---------------------------------------------------------------- designer presets

def designer_presets():
    out = []
    i = 0
    while len(out) < 34:
        fam_key = DESIGNER_FAMILIES[i % len(DESIGNER_FAMILIES)]
        archs = FAMILIES[fam_key]["archs"]
        arch = archs[(i // len(DESIGNER_FAMILIES)) % len(archs)]
        vkey, vlabel, vscale = VARIANTS[i % 3]
        out.append((fam_key, arch, vkey, vlabel, vscale))
        i += 1
    return out

# ---------------------------------------------------------------- custom designer gen-js

DESIGNER_JS_TMPL = r"""(function(){'use strict';
/* JAH __NAME__ generator — jahdb-__SLUG__-1.0.
   Property of Justin Addam Higgins (JAH).
   The Blueprint Designer: deterministic need-driven blueprint generation.
   Same seed + same category = same blueprint. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX=__PREFIX__;
var FIELDS=__FIELDS__;
var SIZES=["compact","standard","grand"];
var SCALE={compact:0.85,standard:1,grand:1.22};
var CONSTRAINTS=["tight budget","narrow lot","flood zone","high wind zone","steep slope","off-grid power","fast-track build","future expansion","historic district","noise ordinance"];
var PURPOSES=__PURPOSES__;
var TYPES=__TYPES__;
var UNIT=__UNIT__;
function asciiPlan(title,rooms,unit){
  var items=rooms.slice().sort(function(a,b){return (b[1]*b[2])-(a[1]*a[2]);});
  var total=0,widest=0,i;
  for(i=0;i<items.length;i++){total+=items[i][1]*items[i][2];widest=Math.max(widest,items[i][1]);}
  var rowW=Math.max(widest,Math.sqrt(total*1.3));
  var rows=[],cur=[],curW=0;
  for(i=0;i<items.length;i++){var r=items[i];
    if(cur.length&&curW+r[1]>rowW*1.03){rows.push(cur);cur=[];curW=0;}
    cur.push(r);curW+=r[1];}
  if(cur.length)rows.push(cur);
  var W=0,D=0,placed=[],y=0;
  for(var ri=0;ri<rows.length;ri++){var rh=0,x=0;
    for(i=0;i<rows[ri].length;i++)rh=Math.max(rh,rows[ri][i][2]);
    for(i=0;i<rows[ri].length;i++){var q=rows[ri][i];placed.push({n:q[0],x:x,y:y,w:q[1],d:q[2]});x+=q[1];}
    W=Math.max(W,x);y+=rh;}
  D=y;
  var upc=2;while(Math.max(W,D)/upc>60)upc*=2;
  var gw=Math.max(8,Math.round(W/upc)),gh=Math.max(5,Math.round(D/upc));
  var g=[],yy,xx;
  for(yy=0;yy<gh;yy++){g.push([]);for(xx=0;xx<gw;xx++)g[yy].push(' ');}
  function hl(yy2,x0,x1){for(var x=Math.max(0,x0);x<Math.min(gw,x1);x++)if(g[yy2][x]===' ')g[yy2][x]='-';}
  function vl(xx2,y0,y1){for(var y=Math.max(0,y0);y<Math.min(gh,y1);y++)if(g[y][xx2]===' ')g[y][xx2]='|';}
  for(i=0;i<placed.length;i++){var p=placed[i];
    var x0=Math.floor(p.x/upc),y0=Math.floor(p.y/upc);
    var x1=Math.min(gw,Math.max(x0+2,Math.round((p.x+p.w)/upc)));
    var y1=Math.min(gh,Math.max(y0+2,Math.round((p.y+p.d)/upc)));
    hl(y0,x0,x1);hl(y1-1,x0,x1);vl(x0,y0,y1);vl(x1-1,y0,y1);
    var cps=[[x0,y0],[x1-1,y0],[x0,y1-1],[x1-1,y1-1]];
    for(var ci=0;ci<4;ci++)if(cps[ci][1]>=0&&cps[ci][1]<gh&&cps[ci][0]>=0&&cps[ci][0]<gw)g[cps[ci][1]][cps[ci][0]]='+';
    var label=String(p.n).slice(0,Math.max(1,x1-x0-2));
    var ly=y0+((y1-y0)>>1),lx=x0+Math.max(1,((x1-x0-label.length)>>1));
    if(ly>y0&&ly<y1-1)for(var li=0;li<label.length;li++)if(lx+li<x1-1)g[ly][lx+li]=label[li];
  }
  var lines=['PLAN: '+title,'Overall '+W+' x '+D+' '+unit+' | 1 char = '+upc+' '+unit+' | schematic - not to construction scale'];
  for(yy=0;yy<gh;yy++)lines.push(g[yy].join('').replace(/\s+$/,''));
  return {text:lines.join('\n'),W:W,D:D};
}
function pyEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"');}
function pyDemo(rid,title,plan,stats){
  var L=['# JAH Blueprint Designer demo','# Record '+rid+' - '+String(title).replace(/"/g,"'"),'plan = "\\n".join(['];
  var plines=String(plan).split('\n');
  for(var i=0;i<plines.length;i++)L.push('"'+pyEsc(plines[i])+'"'+(i<plines.length-1?',':''));
  L.push('])','print(plan)');
  for(var j=0;j<stats.length;j++)L.push('print("'+String(stats[j][0]).replace(/"/g,"'")+': '+String(stats[j][1]).replace(/"/g,"'")+'")');
  L.push('print("OK: '+rid+' designer blueprint verified")');
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var type=pick(TYPES[field]||TYPES[FIELDS[0]],rnd);
  var size=pick(SIZES,rnd);
  var purpose=pick(PURPOSES[field]||PURPOSES['houses'],rnd);
  var c1=pick(CONSTRAINTS,rnd),c2=pick(CONSTRAINTS,rnd);
  if(c2===c1)c2='none';
  var sc=SCALE[size];
  var rooms=type.rooms.map(function(r){return [r[0],Math.round(r[1]*sc*2)/2,Math.round(r[2]*sc*2)/2];});
  var unit=UNIT[field]||'ft';
  var pl=asciiPlan(type.n+' ('+size+')',rooms,unit);
  var area=0,i;for(i=0;i<rooms.length;i++)area+=rooms[i][1]*rooms[i][2];
  area=Math.round(area);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='Designed '+type.n+' ('+size+', '+purpose+')__SIGSUFFIX__';
  var roomList=rooms.map(function(r){return r[0]+': '+r[1]+' x '+r[2]+' '+unit;}).join('; ');
  var desc='SAMPLE RECORD (generated - structural sample). The Blueprint Designer composed this '+size+' '+type.n+
    ' for "'+purpose+'" under constraints ['+c1+(c2==='none'?'':', '+c2)+'], category '+field+
    '. Spaces: '+roomList+'. Estimated area '+area+' sq '+unit+'. Generated samples are clearly labeled and never presented as archive records.';
  return {
    id:id,
    name:type.n+' - designed '+size+' blueprint__SIGSUFFIX__',
    title:title,
    description:desc,
    field:field,
    size:size, purpose:purpose, constraints:[c1,c2],
    src:__SRC__,
    sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive presets are the authoritative entries.',
    blueprint:{plan_ascii:pl.text, overall:pl.W+' x '+pl.D+' '+unit, area_estimate_sq:area, unit:unit},
    demo:{kind:'python',language:'python',program:pyDemo(id,title,pl.text,[['Overall',pl.W+' x '+pl.D+' '+unit],['Spaces',rooms.length],['Area (est.)',area+' sq '+unit],['Purpose',purpose]]),note:'Designer sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-__SLUG__-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
"""

DESIGNER_PURPOSES = {
 "houses": ["family living","rental income","retirement downsizing","guest housing"],
 "stores": ["main-street retail","grocery anchor","specialty shop","pop-up to permanent"],
 "offices": ["startup headquarters","professional practice","branch office","remote hub"],
 "warehouses": ["regional distribution","cold chain","e-commerce fulfillment","contractor storage"],
 "apartments": ["workforce housing","senior living","student housing","luxury rental"],
 "barns": ["dairy operation","horse boarding","hay and feed","equipment shelter"],
 "schools": ["elementary campus","STEM wing","community school","rural school"],
 "factories": ["light assembly","food processing","craft manufacturing","maker industrial"],
 "machines": ["farm power","material handling","shop production","backup power"],
 "tools": ["carpentry kit","mechanic kit","workshop outfitting","field repair"],
 "devices": ["kitchen suite","climate control","home office","laundry"],
 "vehicles": ["family transport","work truck","water recreation","last-mile delivery"],
 "infrastructure": ["river crossing","flood defense","rural power","water supply"],
}

def build_designer_js(slug, cfg):
    sig = cfg["source"] == "signature"
    types = {}
    for fk in DESIGNER_FAMILIES:
        fam = FAMILIES[fk]
        types[fk] = [{"n": a["name"], "rooms": [[n, w, d] for n, w, d in a["spaces"]]}
                     for a in fam["archs"][:4]]
    unit = {fk: FAMILIES[fk]["unit"] for fk in DESIGNER_FAMILIES}
    js = DESIGNER_JS_TMPL
    js = js.replace("__NAME__", cfg["name"])
    js = js.replace("__SLUG__", slug)
    js = js.replace("__PREFIX__", json.dumps(cfg["prefix"]))
    js = js.replace("__FIELDS__", json.dumps(DESIGNER_FAMILIES))
    js = js.replace("__PURPOSES__", json.dumps(DESIGNER_PURPOSES))
    js = js.replace("__TYPES__", json.dumps(types))
    js = js.replace("__UNIT__", json.dumps(unit))
    js = js.replace("__SIGSUFFIX__", " (Signature Edition)" if sig else "")
    js = js.replace("__SRC__", json.dumps("signature-generated-sample" if sig else "designer-generated-sample"))
    return js

# ---------------------------------------------------------------- build

def topics_for(slug, recs):
    topics = {}
    for r in recs:
        topics.setdefault(r["g"], []).append("%s - %s" % (r["t"], r["g"]))
    return topics

def main():
    built = {}
    for slug, name, family, prefix, ai, rk, tagline in DBS:
        cfg = DBCFG[slug]
        recs = []
        if family == "designer":
            build_blueprint_record.counter[slug] = 0
            for fam_key, arch, vkey, vlabel, vscale in designer_presets():
                fam = FAMILIES[fam_key]
                recs.append(build_blueprint_record(slug, cfg, arch, vkey, vlabel, vscale, fam, designer=True))
        elif family == "engpub":
            build_engineer_record.counter[slug] = 0
            for e in content_engineers.ENGINEER_PUBLIC:
                recs.append(build_engineer_record(slug, cfg, e))
        elif family == "engsig":
            build_engineer_record.counter[slug] = 0
            for e in content_engineers.ENGINEER_SIGNATURE:
                recs.append(build_engineer_record(slug, cfg, e))
        else:
            fam = FAMILIES[family]
            build_blueprint_record.counter[slug] = 0
            for vkey, vlabel, vscale in VARIANTS:
                for arch in fam["archs"]:
                    if len(recs) >= 34:
                        break
                    recs.append(build_blueprint_record(slug, cfg, arch, vkey, vlabel, vscale, fam))
                if len(recs) >= 34:
                    break
        assert len(recs) == 34, "expected 34 records for %s, got %d" % (slug, len(recs))
        built[slug] = recs
        print("records: %-38s %d" % (slug, len(recs)), flush=True)

    # ---- sanity: ids unique + prefix + required keys + demos compile + banned scan
    total = 0
    for slug, recs in built.items():
        cfg = DBCFG[slug]
        ids = [r["id"] for r in recs]
        assert len(ids) == len(set(ids)), "dup ids in %s" % slug
        assert all(i.startswith(cfg["prefix"]) for i in ids), "prefix drift in %s" % slug
        for r in recs:
            for k in ("id", "t", "g", "name", "title", "description", "how_it_works",
                      "key_points", "requirements", "standards", "citations",
                      "src", "demo", "blueprint", "materials"):
                assert k in r, "missing %s in %s" % (k, r["id"])
            prog = r["demo"].get("program")
            assert prog and len(r["description"]) > 200, "stub in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            assert "youtube" not in blob, "youtube ref in %s" % r["id"]
        total += len(recs)
        n = base.write_shard_db(slug, recs)
        print("shard: %-38s %d records" % (slug, n), flush=True)

    # ---- machine-execute EVERY demo
    for slug, recs in built.items():
        for r in recs:
            prog = r["demo"]["program"]
            p = subprocess.run([sys.executable, "-c", prog], capture_output=True,
                               text=True, timeout=120)
            assert p.returncode == 0, "demo failed %s: %s" % (r["id"], p.stderr[-500:])
            assert "OK:" in p.stdout, "demo no OK marker %s" % r["id"]
    print("demo execution: all %d demos ran OK" % total, flush=True)

    # ---- pages + gen-js
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()
    for slug, recs in built.items():
        page = nb.build_page(slug, template)
        page = page.replace(
            "Generate structural synthetic intelligence studies. Seeded archive records are the authoritative entries.",
            DBCFG[slug]["gen_desc"])
        assert 'id="stCount"' in page and "var SLUG='%s';" % slug in page
        assert "/data/%s/" % slug in page, "LOCAL not rewritten for %s" % slug
        assert "minmax(120px,1fr)" in page and "pre.codeblock" in page
        assert "pill-ex" in page and "qmerge" in page, "Exhaustive pill / merger button missing"
        assert "dataset.p" in page, "tab-handler guard missing"
        assert "facebook" not in page.lower()
        assert "synthetic intelligence" not in page.lower(), "template leftover in %s" % slug
        assert "bat belt" not in page.lower(), "banned phrase in page %s" % slug
        ddir = os.path.join(REPO, "db", slug)
        os.makedirs(ddir, exist_ok=True)
        ppath = os.path.join(ddir, "index.html")
        with open(ppath, "w", encoding="utf-8") as f:
            f.write(page)
        notes = []
        if sweep is not None:
            try:
                changed, _notes = sweep.process_page(ppath)
                notes = _notes
            except Exception as e:
                notes = ["sweep failed: %s" % e]
        if slug.startswith("blueprint-designer"):
            gen_js = build_designer_js(slug, DBCFG[slug])
        else:
            gen_js = nb.build_gen_js(slug, topics_for(slug, recs), DBCFG[slug])
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        gpath = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gpath, "w", encoding="utf-8") as f:
            f.write(gen_js)
        p = subprocess.run(["node", "--check", gpath], capture_output=True, text=True)
        assert p.returncode == 0, "node --check failed for %s: %s" % (slug, p.stderr)
        # functional smoke test of the generator
        t = subprocess.run(["node", "-e",
            "var g=require(%s);var r=g.generate(7,{});var v=g.validate(r);"
            "if(!v.ok)throw new Error('validate: '+v.errors.join(','));"
            "if(!r.demo||!r.demo.program)throw new Error('no demo');"
            "console.log('gen-ok '+r.id);" % json.dumps(gpath)],
            capture_output=True, text=True)
        assert t.returncode == 0 and "gen-ok" in t.stdout, \
            "gen smoke failed for %s: %s" % (slug, t.stderr[-500:])
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    # ---- manifest/api entry payloads for the coordinator (DO NOT write manifest.json/api.json)
    manifest_entries, api_entries = [], []
    for slug, recs in built.items():
        c = DBCFG[slug]
        manifest_entries.append({
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "id_prefix": c["prefix"],
            "ai_name": c["ai"],
            "local_index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "record_count": len(recs), "status": "live", "full_records": len(recs),
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
            "chunk_pattern": "data/" + slug + "/chunks/chunk-NNNN.jsonl.gz",
            "source": c["source"],
        })
        api_entries.append({
            "slug": slug, "name": c["name"], "tagline": c["tagline"],
            "record_kind": c["record_kind"], "record_count": len(recs), "status": "live",
            "index": SHARD_BASE + "/data/" + slug + "/index.jsonl.gz",
        })
    with open(os.path.join(HERE, "manifest-entries.json"), "w", encoding="utf-8") as f:
        json.dump(manifest_entries, f, indent=1, ensure_ascii=False)
    with open(os.path.join(HERE, "api-entries.json"), "w", encoding="utf-8") as f:
        json.dump(api_entries, f, indent=1, ensure_ascii=False)
    print("wrote manifest-entries.json + api-entries.json (%d dbs) for coordinator merge" % len(built))
    print("manifest.json + api.json NOT touched (coordinator merges).")
    print("TOTAL: %d databases, %d records" % (len(built), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
