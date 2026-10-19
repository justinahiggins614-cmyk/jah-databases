#!/usr/bin/env python3
"""Build the Human Likeness DNA databases for JAH Databases
(Manon's 2026-10-17 16:15 order).

Verified 2026-10-17: RAW SWEEP over the full manifest (2,410 databases)
PLUS every shard index title in jah-databases-data-1 (785 index files,
1,132,237 index lines): zero 'human-likeness*' slugs/names; zero title
collisions for all 68 titles (dedupe pre-check before authoring: 68
checked, 0 refusals). ID prefixes JAH-HLDN- / JAH-HLDNS- verified free in
the manifest id_prefix values and in every shard index file.

So this build creates two NEW databases, 34 ladder-ordered records each:

  human-likeness-dna                - The Human Likeness DNA Database
                                      (the deterministic HLX-1 method plus
                                      synthetic illustrative sequences, each
                                      with its deterministically derived
                                      representation: trait-parameter vector,
                                      stylized abstract SVG glyph spec, and
                                      step-by-step derivation; every
                                      representation clearly labeled a
                                      Signature-generated deterministic
                                      model - a stylized parametric
                                      abstraction, never a real person's
                                      appearance; src
                                      'signature-generated-model')
  human-likeness-dna-signature      - The Human Likeness DNA Signature
                                      Database
                                      (the same ladder through the Signature
                                      lens; src 'signature', titles suffixed
                                      " (Signature Edition)", clearly
                                      labeled Signature-made, never
                                      presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced): method records -> single-
trait derivations -> full-likeness derivations (incl. the determinism
proof, the sensitivity check, the generator record).

The frozen HLX-1 algorithm is implemented twice, byte-identically: in the
Python record demos and in JavaScript (BigInt 64-bit arithmetic) appended
to each gen-*.js as the HLX1 pipeline module (input: one sequence string;
output: the deterministic representation). The build cross-checks both
implementations on every database sequence.

CONCURRENCY: this build never touches data/manifest.json, api.json,
index.html, README.md, or docs/AI_ACCESS.md, and never commits or pushes.
A merger handles those. It only writes db/human-likeness-dna[-signature]/
(index.html + gen-*.js), the shard data dirs, and (via the fragment step,
run separately) the missing-builds fragment.

Never the words "bat belt" anywhere. No website references. No Facebook.
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

sys.path.insert(0, os.path.join(REPO, "code", "phone-compound-build"))
import build as base
sys.path.insert(0, os.path.join(REPO, "code"))
from dedupe_gate import DedupeGate
base.GATE = DedupeGate(os.path.join(REPO, "data", "dedupe", "exact"))

sys.path.insert(0, HERE)
from entries_human_likeness_dna import ENTRIES, SIG_TAIL, MODEL_LABEL
from demos_human_likeness_dna import DEMOS

# ---------------------------------------------------------------- DB config

def _cfg(slug, name, tagline, record_kind, prefix, ai, role, citation, source):
    sig = source == "signature"
    sig_line = ("Signature originals - his original Signature reading of "
                "the likeness method: the sequence as a signature, the "
                "derivation as a covenant of steps, the abstract glyph as "
                "a seal. Clearly labeled Signature-made, never presented "
                "as authentic public record.")
    pub_line = ("The deterministic method plus synthetic illustrative "
                "sequences: every record carries the trait-parameter "
                "vector derived by the documented HLX-1 algorithm, the "
                "stylized abstract visualization spec, and the step-by-step "
                "derivation. Every representation is a Signature-generated "
                "deterministic model - a stylized parametric abstraction, "
                "never a real person's appearance; sequences are synthetic "
                "illustrations, never real DNA.")
    ladder = (" Records are ordered by the teaching ladder: Foundations "
              "(what the method is, the deterministic pipeline, sequence "
              "basics, seeded randomness, reading a sequence, the "
              "trait-parameter vector, the abstract visualization spec, "
              "the limits record, sequence hygiene, the verification "
              "procedure) -> Compounded (single-trait derivations, one "
              "trait from one synthetic sequence at a time: height band, "
              "build, skin-tone band, hair texture, hair shade, eye color, "
              "face width ratio, jaw angle, nose bridge, brow density, lip "
              "fullness, freckle density) -> Advanced (combining all "
              "traits, eight full likeness derivations, the determinism "
              "proof, the sensitivity check, the generator record).")
    return {
        "name": name, "tagline": tagline, "record_kind": record_kind,
        "prefix": prefix, "ai": ai, "role": role,
        "hero_p": "%s - %s Every record carries the full entry: description, how it works, "
                  "key points, requirements, standards, citations, and a working demonstration "
                  "program.%s" % (tagline, sig_line if sig else pub_line, ladder),
        "sig_type": ("Signature originals organized in the Signature system"
                     if sig else
                     "Signature-generated deterministic models organized in the Signature system"),
        "search_ph": "Search height band, build, skin band, hair texture, hair shade, eye color, face ratio, jaw angle, nose bridge, sequences, glyphs, determinism, pipeline...",
        "chat_ph": "Ask about the likeness method, traits, sequences, glyphs...",
        "archive_blurb": ("Seeded %s human likeness DNA records, marching toward one million records. "
                          "Presented in teaching-ladder order: foundations, compounded, advanced. "
                          "Every representation is a Signature-generated deterministic model - "
                          "a stylized parametric abstraction, never a real person's appearance."
                          % ("Signature-original" if sig else "deterministic-model")),
        "schema": ("id, t, g, name, title, description, how_it_works, key_points, requirements, "
                   "standards, citations, src, ladder_rank, ladder_tier, demo"),
        "fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
        "gen_desc": "Paste one synthetic DNA sequence to derive its deterministic representation with the built-in HLX-1 pipeline, or generate clearly-labeled structural samples. Seeded archive records are the authoritative entries.",
        "greet": "I am the %s. Ask me about the deterministic likeness method - from sequence validation and seeded randomness through the twelve trait draws to full representations, abstract glyphs, and the limits of the method." % ai,
        "gen_fields": ["Foundations", "Compounded", "Advanced"],
        "gen_kind": "human-likeness-study", "gen_demo_kind": "human-likeness-demo",
        "source": source,
    }

CIT_PUB = ("The HLX-1 deterministic pipeline as documented in 'The "
           "Deterministic Pipeline: Sequence to Representation' in this "
           "database (validate; FNV-1a 64-bit digest - Fowler G, Noll LC, "
           "Vo P; seeded xorshift64* - Vigna S, arXiv:1404.0390; twelve "
           "trait draws in fixed order; compact JSON vector; abstract "
           "glyph SVG spec). All sequences synthetic illustrations; every "
           "representation a Signature-generated deterministic model, "
           "never a real person's appearance.")
CIT_SIG = CIT_PUB + (" Signature editions are his original Signature "
                     "reading of the likeness method - the sequence as a "
                     "signature, the derivation as a covenant of steps, "
                     "the abstract glyph as a seal - clearly labeled "
                     "Signature-made.")

DBCFG = {}
DBCFG["human-likeness-dna"] = _cfg(
    "human-likeness-dna", "The Human Likeness DNA Database",
    "One DNA sequence at a time, deterministically derived: the frozen "
    "HLX-1 pipeline turns a synthetic sequence into a trait-parameter "
    "vector, a stylized abstract glyph, and a step-by-step derivation. "
    "Every representation is a Signature-generated deterministic model, "
    "never a real person's appearance.",
    "human likeness record", "JAH-HLDN-", "JAH Human Likeness Archivist",
    "human likeness archivist - deterministic sequence-to-representation derivation, trait-parameter vectors, abstract glyphs, and the limits of the method; teaching progressively along the ladder from foundations through compounded to advanced; answers from many angles - definition, example, analogy, application, history, math, how-to - using only archive data from this system",
    CIT_PUB, "public")
DBCFG["human-likeness-dna-signature"] = _cfg(
    "human-likeness-dna-signature", "The Human Likeness DNA Signature Database",
    "His original Signature reading of the likeness method: the sequence "
    "as a signature, the derivation as a covenant of steps, the abstract "
    "glyph as a seal. The full ladder from method foundations through "
    "single-trait derivations to full likenesses, the determinism proof, "
    "the sensitivity check, and the generator record, reframed as "
    "Signature science. Clearly labeled Signature-made, never presented "
    "as authentic public record.",
    "human likeness record", "JAH-HLDNS-", "JAH Human Likeness Archivist (Signature)",
    "human likeness archivist - Signature editions: his original Signature reading of the likeness method, the sequence as a signature and the derivation as a covenant of steps, clearly labeled Signature-made and never presented as authentic public record; teaches progressively along the ladder from foundations through compounded to advanced; answers from many angles - definition, example, analogy, application, history, math, how-to - using only archive data from this system",
    CIT_SIG, "signature")

base.DBCFG = DBCFG

assert set(DEMOS) == {e["key"] for e in ENTRIES}, "demo map misses entries"

# ---------------------------------------------------------------- HLX-1 JS pipeline
# The frozen HLX-1 algorithm in JavaScript (BigInt 64-bit arithmetic),
# appended to each gen-*.js as the HLX1 module: input one sequence string,
# output the deterministic representation. Must stay byte-identical with
# the Python implementation in demos_human_likeness_dna.py.

HLX1_JS = '''\
/* HLX-1 deterministic pipeline - JavaScript mirror of the frozen Python
   implementation. Input: one DNA sequence string (ACGT, 16-4096 bases).
   Output: the deterministic representation (model label, digests, trait
   vector JSON, abstract glyph SVG). Byte-identical with the Python demos.
   Every representation is a Signature-generated deterministic model - a
   stylized parametric abstraction, never a real person's appearance. */
(function(){
'use strict';
var MASK64 = (1n << 64n) - 1n;
var FNV_OFFSET = 14695981039346656037n;
var FNV_PRIME = 1099511628211n;
var XORMULT = 2685821657736338717n;
var ZERO_SEED = 0x9E3779B97F4A7C15n;
var HEIGHT = ["compact","below-average","average","above-average","tall"];
var BUILD = ["slight","lean","sturdy","broad"];
var HAIR_TEX = ["straight","wavy","curly","coily"];
var EYE = ["brown","hazel","green","blue","gray","amber"];
var NOSE = ["low","medium","high"];
var BROW = ["light","medium","full"];
var LIP = ["thin","medium","full"];
var FRECKLE = ["none","sparse","moderate","dense"];
var EYE_HEX = {"brown":"#6B4226","hazel":"#8A6D3B","green":"#4F7942",
  "blue":"#3B6EA5","gray":"#7D7D7D","amber":"#B8860B"};
var TRAIT_ORDER = ["height_band","build","skin_band","hair_texture",
  "hair_shade","eye_color","face_width_ratio","jaw_angle",
  "nose_bridge","brow_density","lip_fullness","freckle_density"];
var MODEL_LABEL = "Signature-generated deterministic model - a stylized " +
  "parametric abstraction. Never a real person's appearance.";
function validate(seq){
  if(typeof seq !== "string" || seq.length === 0)
    throw new Error("sequence must be a non-empty string");
  if(seq.length < 16) throw new Error("sequence too short (minimum 16 bases)");
  if(seq.length > 4096) throw new Error("sequence too long (maximum 4096 bases)");
  for(var i = 0; i < seq.length; i++){
    var c = seq.charAt(i);
    if(c !== "A" && c !== "C" && c !== "G" && c !== "T")
      throw new Error("invalid base: only A, C, G, T allowed");
  }
  return seq;
}
function fnv1a64(str){
  var h = FNV_OFFSET;
  for(var i = 0; i < str.length; i++){
    h ^= BigInt(str.charCodeAt(i));
    h = (h * FNV_PRIME) & MASK64;
  }
  return h;
}
function makeRng(seed){
  var s = (seed & MASK64) || ZERO_SEED;
  return {
    next64: function(){
      var x = s;
      x ^= x >> 12n; x &= MASK64;
      x ^= (x << 25n) & MASK64;
      x ^= x >> 27n;
      s = x & MASK64;
      return (s * XORMULT) & MASK64;
    },
    int: function(n){ return this.next64() % BigInt(n); }
  };
}
function deriveTraits(seq){
  validate(seq);
  var rng = makeRng(fnv1a64(seq));
  var hi = rng.int(5), bi = rng.int(4), si = rng.int(6), ti = rng.int(4),
      sh = rng.int(6), ei = rng.int(6), fq = rng.int(21), ja = rng.int(41),
      ni = rng.int(3), br = rng.int(3), li = rng.int(3), fi = rng.int(4);
  var traits = {
    height_band: HEIGHT[Number(hi)],
    build: BUILD[Number(bi)],
    skin_band: "band-" + (Number(si) + 1),
    hair_texture: HAIR_TEX[Number(ti)],
    hair_shade: "shade-" + (Number(sh) + 1),
    eye_color: EYE[Number(ei)],
    face_width_ratio: (72 + Number(fq)) / 100,
    jaw_angle: 100 + Number(ja),
    nose_bridge: NOSE[Number(ni)],
    brow_density: BROW[Number(br)],
    lip_fullness: LIP[Number(li)],
    freckle_density: FRECKLE[Number(fi)]
  };
  var idx = {height_idx: Number(hi), skin_idx: Number(si),
    texture_idx: Number(ti), face_q: Number(fq), jaw_angle: 100 + Number(ja),
    nose_idx: Number(ni), brow_idx: Number(br), freckle_idx: Number(fi)};
  return {traits: traits, idx: idx};
}
function svgSpec(traits, idx){
  var bgHue = (idx.skin_idx * 47 + idx.height_idx * 23) % 360;
  var discR = 52 + idx.face_q;
  var discHue = (bgHue + 180) % 360;
  var jawH = 20 + (idx.jaw_angle - 100);
  var noseH = 20 + idx.nose_idx * 15;
  var browH = 20 + idx.brow_idx * 15;
  var nArcs = idx.texture_idx + 1;
  var nFreck = idx.freckle_idx * 5;
  var eyeHex = EYE_HEX[traits.eye_color];
  var L = [];
  L.push('<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">');
  L.push('<rect width="240" height="240" fill="hsl(' + bgHue + ',45%,88%)"/>');
  L.push('<circle cx="120" cy="112" r="' + discR + '" fill="hsl(' + discHue +
    ',40%,72%)" stroke="#333333" stroke-width="2"/>');
  L.push('<rect x="56" y="' + (214 - jawH) + '" width="18" height="' + jawH + '" fill="#555555"/>');
  L.push('<rect x="86" y="' + (214 - noseH) + '" width="18" height="' + noseH + '" fill="#777777"/>');
  L.push('<rect x="116" y="' + (214 - browH) + '" width="18" height="' + browH + '" fill="#999999"/>');
  var top = 112 - discR - 8, a, y, d, style = idx.texture_idx;
  for(a = 0; a < nArcs; a++){
    y = top - a * 9;
    if(style === 0) d = "M " + (120 - discR) + " " + y + " L " + (120 + discR) + " " + y;
    else if(style === 1) d = "M " + (120 - discR) + " " + y + " Q 120 " + (y - 10) + " " + (120 + discR) + " " + y;
    else if(style === 2) d = "M " + (120 - discR) + " " + y +
      " Q " + (120 - Math.floor(discR / 2)) + " " + (y - 12) + " 120 " + y +
      " Q " + (120 + Math.floor(discR / 2)) + " " + (y + 12) + " " + (120 + discR) + " " + y;
    else d = "M " + (120 - discR) + " " + y +
      " L " + (120 - Math.floor(discR / 3)) + " " + (y - 10) +
      " L " + (120 + Math.floor(discR / 3)) + " " + (y + 10) +
      " L " + (120 + discR) + " " + y;
    L.push('<path d="' + d + '" stroke="#222222" stroke-width="2" fill="none"/>');
  }
  L.push('<circle cx="104" cy="106" r="6" fill="' + eyeHex + '"/>');
  L.push('<circle cx="136" cy="106" r="6" fill="' + eyeHex + '"/>');
  var f, fx, fy;
  for(f = 0; f < nFreck; f++){
    fx = 84 + (f * 37) % 72; fy = 96 + (f * 53) % 40;
    L.push('<circle cx="' + fx + '" cy="' + fy + '" r="1.6" fill="#4a3220"/>');
  }
  L.push('<text x="120" y="232" text-anchor="middle" font-size="8" fill="#333333">' +
    'HLX-1 abstract glyph - deterministic model, not a person</text>');
  L.push('</svg>');
  return L.join("\\n");
}
function hex16(h){
  var s = h.toString(16);
  while(s.length < 16) s = "0" + s;
  return s;
}
function represent(seq){
  var dt = deriveTraits(seq), traits = dt.traits, idx = dt.idx;
  var vec = {}, i;
  for(i = 0; i < TRAIT_ORDER.length; i++) vec[TRAIT_ORDER[i]] = traits[TRAIT_ORDER[i]];
  return {
    model_label: MODEL_LABEL,
    sequence_length: seq.length,
    digest_fnv1a64: hex16(fnv1a64(validate(seq))),
    trait_vector: vec,
    trait_vector_json: JSON.stringify(vec),
    svg_spec: svgSpec(traits, idx)
  };
}
var HLX1 = {version: "hlx-1", validate: validate, fnv1a64: fnv1a64,
  deriveTraits: deriveTraits, svgSpec: svgSpec, represent: represent,
  model_label: MODEL_LABEL};
if(typeof module !== "undefined" && module.exports) module.exports.HLX1 = HLX1;
if(typeof window !== "undefined") window.JAHDB_HLX1 = HLX1;
})();
'''

# ---------------------------------------------------------------- records

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
        if "signature-generated deterministic model" not in description.lower():
            description = description + " " + MODEL_LABEL
        rec = {
            "id": rid, "t": title, "g": e["group"], "name": name, "title": title,
            "description": description,
            "how_it_works": how,
            "key_points": list(e["key_points"]),
            "requirements": list(e["requirements"]),
            "standards": list(e["standards"]),
            "citations": citations,
            "src": "signature" if sig else "signature-generated-model",
            "ladder_rank": e["ladder_rank"],
            "ladder_tier": e["ladder_tier"],
        }
        demo_fn = DEMOS[e["key"]]
        program = demo_fn(base._hdr, name if not sig else title, rid, e["group"],
                          e["key_points"], "; ".join(e["requirements"]))
        rec["demo"] = {"kind": "python", "language": "python",
                       "program": program,
                       "note": "Working demonstration program (real, runnable Python): "
                               "the frozen HLX-1 pipeline on this record's synthetic "
                               "sequence, with machine-checked assertions."}
        base.GATE.admit(slug, title, rid)
        recs.append(rec)
    ranks = [r["ladder_rank"] for r in recs]
    assert ranks == sorted(ranks), "records not in ladder order for %s" % slug
    return recs


def _py_represent(seq):
    """Reference Python represent() for cross-language checks."""
    import hashlib
    MASK64 = (1 << 64) - 1
    FNV_OFFSET = 14695981039346656037
    FNV_PRIME = 1099511628211
    h = FNV_OFFSET
    for b in seq.encode("ascii"):
        h ^= b
        h = (h * FNV_PRIME) & MASK64
    s = (h & MASK64) or 0x9E3779B97F4A7C15
    def nxt():
        nonlocal s
        x = s
        x ^= (x >> 12); x &= MASK64
        x ^= (x << 25) & MASK64
        x ^= (x >> 27)
        s = x & MASK64
        return (s * 2685821657736338717) & MASK64
    draws = [nxt() % m for m in (5, 4, 6, 4, 6, 6, 21, 41, 3, 3, 3, 4)]
    HEIGHT = ["compact", "below-average", "average", "above-average", "tall"]
    BUILD = ["slight", "lean", "sturdy", "broad"]
    HAIR_TEX = ["straight", "wavy", "curly", "coily"]
    EYE = ["brown", "hazel", "green", "blue", "gray", "amber"]
    EYE_HEX = {"brown": "#6B4226", "hazel": "#8A6D3B", "green": "#4F7942",
               "blue": "#3B6EA5", "gray": "#7D7D7D", "amber": "#B8860B"}
    NOSE = ["low", "medium", "high"]
    BROW = ["light", "medium", "full"]
    LIP = ["thin", "medium", "full"]
    FRECKLE = ["none", "sparse", "moderate", "dense"]
    hi, bi, si, ti, sh, ei, fq, ja, ni, br, li, fi = draws
    traits = {
        "height_band": HEIGHT[hi], "build": BUILD[bi],
        "skin_band": "band-%d" % (si + 1), "hair_texture": HAIR_TEX[ti],
        "hair_shade": "shade-%d" % (sh + 1), "eye_color": EYE[ei],
        "face_width_ratio": (72 + fq) / 100.0, "jaw_angle": 100 + ja,
        "nose_bridge": NOSE[ni], "brow_density": BROW[br],
        "lip_fullness": LIP[li], "freckle_density": FRECKLE[fi]}
    order = ["height_band", "build", "skin_band", "hair_texture",
             "hair_shade", "eye_color", "face_width_ratio", "jaw_angle",
             "nose_bridge", "brow_density", "lip_fullness", "freckle_density"]
    vec_json = json.dumps({k: traits[k] for k in order},
                          separators=(",", ":"), ensure_ascii=True)
    bg_hue = (si * 47 + hi * 23) % 360
    disc_r = 52 + fq
    disc_hue = (bg_hue + 180) % 360
    jaw_h = 20 + ja; nose_h = 20 + ni * 15; brow_h = 20 + br * 15
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">',
        '<rect width="240" height="240" fill="hsl(%d,45%%,88%%)"/>' % bg_hue,
        '<circle cx="120" cy="112" r="%d" fill="hsl(%d,40%%,72%%)" stroke="#333333" stroke-width="2"/>' % (disc_r, disc_hue),
        '<rect x="56" y="%d" width="18" height="%d" fill="#555555"/>' % (214 - jaw_h, jaw_h),
        '<rect x="86" y="%d" width="18" height="%d" fill="#777777"/>' % (214 - nose_h, nose_h),
        '<rect x="116" y="%d" width="18" height="%d" fill="#999999"/>' % (214 - brow_h, brow_h),
    ]
    top = 112 - disc_r - 8
    for a in range(ti + 1):
        y = top - a * 9
        if ti == 0:
            d = "M %d %d L %d %d" % (120 - disc_r, y, 120 + disc_r, y)
        elif ti == 1:
            d = "M %d %d Q %d %d %d %d" % (120 - disc_r, y, 120, y - 10, 120 + disc_r, y)
        elif ti == 2:
            d = "M %d %d Q %d %d %d %d Q %d %d %d %d" % (
                120 - disc_r, y, 120 - disc_r // 2, y - 12, 120, y,
                120 + disc_r // 2, y + 12, 120 + disc_r, y)
        else:
            d = "M %d %d L %d %d L %d %d L %d %d" % (
                120 - disc_r, y, 120 - disc_r // 3, y - 10,
                120 + disc_r // 3, y + 10, 120 + disc_r, y)
        lines.append('<path d="%s" stroke="#222222" stroke-width="2" fill="none"/>' % d)
    lines.append('<circle cx="104" cy="106" r="6" fill="%s"/>' % EYE_HEX[traits["eye_color"]])
    lines.append('<circle cx="136" cy="106" r="6" fill="%s"/>' % EYE_HEX[traits["eye_color"]])
    for f in range(fi * 5):
        lines.append('<circle cx="%d" cy="%d" r="1.6" fill="#4a3220"/>' % (84 + (f * 37) % 72, 96 + (f * 53) % 40))
    lines.append('<text x="120" y="232" text-anchor="middle" font-size="8" fill="#333333">'
                 'HLX-1 abstract glyph - deterministic model, not a person</text>')
    lines.append('</svg>')
    return vec_json, "\n".join(lines)


XLANG_SEQS = [
    "ACGCGGACTCACCCGTAGCGGGCTAATTGATTAAAATTTACCGTATTGTCTGTCAGGGGGAAATGTAGGAGC",
    "GATCATGCTTACCCGGTCAGCAAGGTGTTCCGGGTGTGGACCGTTAGGGCGTTACTAGTTGCAATCGATCAC",
    "TCATAACTTAACGAAACAAATTGCGTGTATTGTGAATCCCCTGAAATAGTTACATGTCCTAGGTTTGTTTTC",
    "GTATGAATGGGGTTTTGACCGAATTGCTGATTTTTTGTCTCAGCTCCTGCTTTCTGGTGATGTTTACTATAT",
    "ATTGCACTTATACCTGTACTGTAGTCTGTAATGTCACAGTACTGGGCGGCGAAATACCCTTTGCTAACAAAT",
    "TGGTCGCGTGGCCTTATGGACAAATTACCGCGGACATGAGGGCCGTTTCCAACGAGAAACCACCGAACGTCT",
    "GTTTCTTTTTTATCGCCTACTTCTCACACCGGTGCCCGTGAATCGAGCTCGTCGACTTATTTCTACGACCGG",
    "GTTTCCTGGCAAGTGGTGCAAATAGAGTGTAGGTGAATGCGACACCTAGTTGCTACGACTTTAGATAAAAAG",
    "GGCACTGATTGCTTGGGCACCTATCCTAGAGACAGTGCTAATACAGGAAGTCGATCTCTAGTATAACGCCAA",
    "GAGGCTGCTAATCAACACGTACTTGAGTGACATGTCCTTCCTATCCCAATAAGAAGTCACGTCCCGCTAGAT",
    "CCATTCCCAGTTTAAGACGTGATGCCGGGATTGCGCTGAAGTGGGCGGAGGTTAGGGTGGAGAAGAGGGTCG",
    "ATACTTACAGCAGAATATTTGGAACCTGATTAGAATTTGGCTATTACAAAGTACCTGTCCCCTAGGAATCGC",
    "TCTTGCTCGACACCGTGCGCAACCTTAGTGCGGCCTATGTGCGTCTAAGCCGGCCGGGCTCTCTACTCCCAA",
    "GGAATACAGTAGCGACGCCCTAGTTGACAATCTAATCCTAGTCGTGTCTCGGCTGCGGTGCGCATGGAGAAC",
    "TCGCCTAAGGAAGTAGTTTACCCTGCATTATTTTGGCGCTGGCCCGCTTCCTGCCTACAGGAGATTTGAATT",
    "GGCAGCCTACCCGCCGCCTGTTGCGGTAAGTCTGGATAGGGCGTAAGAGGAACCGATCCCCAGCAAATAGTC",
    "GGACAAGCGGATGAGTTATTGGGCGAGGCAAAGGAGTCGTGTTCTGCTTCGTCGAATCCTGAATGATGGTCA",
    "GGGTAAGATTACTAGATAAATCAGAAATCCTAGATCACAAATCTCGCAAATGTATAAACGCGAACGTGGAGG",
    "CCTAGGGCTCAGCCAAGTTAGCAGTTTTGAAGTTCTGGCTGCCCCGAGTATTGCCACGGATCACATGTCACC",
    "ACGGGACAGCGACGTGAGCTAGTAGGTTTATGCGATTCGGCAATGTCAGGCGAGGTGTGTAAACCCCTAAGA",
    "CTAACAAATCATCGCTTTATACAACTCTGCTGGACCGTCGACAGCCAAAGACCAACAAGAGGAATTATCCGC",
]


def xlang_check(gen_js_path):
    """Run the JS HLX1 pipeline under node for every database sequence and
    compare trait_vector_json + svg_spec byte-for-byte with Python."""
    driver = (
        "var gen = require(%s);\n"
        "var out = {};\n"
        "var seqs = %s;\n"
        "for (var i = 0; i < seqs.length; i++) {\n"
        "  var r = gen.HLX1.represent(seqs[i]);\n"
        "  out[seqs[i]] = [r.trait_vector_json, r.svg_spec];\n"
        "}\n"
        "console.log(JSON.stringify(out));\n" % (json.dumps(gen_js_path), json.dumps(XLANG_SEQS)))
    p = subprocess.run(["node", "-e", driver], capture_output=True, text=True, timeout=120)
    assert p.returncode == 0, "node HLX1 driver failed: %s" % p.stderr[-2000:]
    js_out = json.loads(p.stdout)
    assert set(js_out) == set(XLANG_SEQS), "node missed sequences"
    for s in XLANG_SEQS:
        py_vec, py_svg = _py_represent(s)
        js_vec, js_svg = js_out[s]
        assert js_vec == py_vec, "vector mismatch for %s...: %s != %s" % (s[:12], js_vec, py_vec)
        assert js_svg == py_svg, "svg mismatch for %s..." % s[:12]
    print("xlang: JS HLX1 pipeline byte-identical with Python on %d sequences"
          % len(XLANG_SEQS), flush=True)


def node_check(path):
    p = subprocess.run(["node", "--check", path], capture_output=True, text=True, timeout=60)
    assert p.returncode == 0, "node --check failed for %s: %s" % (path, p.stderr[-2000:])


def node_check_inline_scripts(page_path):
    import re
    html = open(page_path, encoding="utf-8").read()
    blocks = []
    for m in re.finditer(r"<script([^>]*)>(.*?)</script>", html, flags=re.S):
        attrs, body = m.group(1), m.group(2)
        if "src=" in attrs:
            continue
        tm = re.search(r'type="([^"]+)"', attrs)
        if tm and "javascript" not in tm.group(1).lower():
            continue  # e.g. application/ld+json - not JavaScript
        if body.strip():
            blocks.append(body)
    assert blocks, "no inline JS found in %s" % page_path
    for i, b in enumerate(blocks):
        tmp = "/tmp/hldn_inline_%d.js" % i
        open(tmp, "w", encoding="utf-8").write(b)
        node_check(tmp)
    print("node --check: %d inline script blocks clean in %s" % (len(blocks), page_path), flush=True)


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
    for slug in ("human-likeness-dna", "human-likeness-dna-signature"):
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
            assert MODEL_LABEL.split(" - ")[0] in r["description"] or \
                "Signature-generated deterministic model" in r["description"], \
                "model label missing in %s" % r["id"]
            compile(prog, r["id"], "exec")
            blob = json.dumps(r).lower()
            assert "facebook" not in blob, "facebook ref in %s" % r["id"]
            assert "bat belt" not in blob, "banned phrase in %s" % r["id"]
            assert "synthetic intelligence" not in blob, "template phrase in %s" % r["id"]
            if slug.endswith("-signature"):
                assert "(signature edition)" in r["title"].lower(), "sig title missing suffix"
                assert r["src"] == "signature"
            else:
                assert r["src"] == "signature-generated-model"
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
        assert "universal build" not in page.lower(), "field leftover in %s" % slug
        assert "universal-build" not in page, "slug leftover in %s" % slug
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
        gen_js = gen_js + "\n" + HLX1_JS
        assert "facebook" not in gen_js.lower() and "bat belt" not in gen_js.lower()
        assert "universal build" not in gen_js.lower(), "field leftover in gen js %s" % slug
        gen_path = os.path.join(ddir, "gen-%s.js" % slug)
        with open(gen_path, "w", encoding="utf-8") as f:
            f.write(gen_js)
        print("page:  db/%s/index.html + gen-%s.js [%s]" % (slug, slug, ", ".join(notes)), flush=True)

    for slug in built:
        gen_path = os.path.join(REPO, "db", slug, "gen-%s.js" % slug)
        node_check(gen_path)
        print("node --check clean: db/%s/gen-%s.js" % (slug, slug), flush=True)
        node_check_inline_scripts(os.path.join(REPO, "db", slug, "index.html"))
        xlang_check(gen_path)

    # manifest + api.json are owned by the merger - intentionally untouched.
    print("manifest/api.json: SKIPPED (merger handles appends + restamp).")
    print("NEXT: merger runs code/restamp_counts.py, then commits + pushes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
