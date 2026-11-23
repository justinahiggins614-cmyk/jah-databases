// Seeded boundless generator for the Programmable Materials Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-programmable-materials.js [seed]  (prints one
// JSON record) or: node gen-programmable-materials.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "programmable-materials";
const RECORD_KIND = "future programmable materials record";
const ID_PREFIX = "JAH-PROMAT-";
const AI_NAME = "JAH Programmable Materials Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "What Programmable Materials Are",
    "subject": "programmable materials identity",
    "description": "A programmable material is a material whose properties, such as shape, stiffness, or colour, can be changed on command by a signal such as heat, light, electricity, or a magnetic field. An ordinary material has fixed properties: steel is stiff, rubber is soft, and neither changes unless it is cut or melted. A programmable material is designed so that a signal flips it between states: a wire.",
    "label": "what-programmable-materials-are",
    "figures": {
      "property_kinds": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "signals": 4
    }
  },
  {
    "title": "Shape-Memory Alloys",
    "subject": "shape-memory alloys",
    "description": "A shape-memory alloy is a metal that returns to a set shape when heated, and the best-known example is nitinol, an alloy of nickel and titanium. The alloy is trained by holding it in a desired shape at high temperature, then it can be bent and deformed at low temperature, and when it is heated again it snaps back to its trained shape. The cause is a change in crystal structure: at low.",
    "label": "shape-memory-alloys",
    "figures": {
      "metals_in_alloy": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "crystal_states": 2
    }
  },
  {
    "title": "Shape-Memory Polymers",
    "subject": "shape-memory polymers",
    "description": "A shape-memory polymer is a plastic that returns to a set shape when triggered by heat or light, and it is the light, cheap cousin of the shape-memory alloy. The polymer is made as a network of long chains linked at points, and it is trained by warming it, stretching it into a temporary shape, and cooling it so the chains freeze in place. When it is warmed again, the chains soften and pull.",
    "label": "shape-memory-polymers",
    "figures": {
      "triggers": 4,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "shapes_held": 2
    }
  },
  {
    "title": "Electroactive Polymers",
    "subject": "electroactive polymers",
    "description": "An electroactive polymer is a plastic that changes shape or size under electricity, and it is the closest thing materials science has to an artificial muscle. Two families exist. One family is the dielectric elastomer, a soft film between two stretchy electrodes that squeezes thinner and spreads wider when voltage is applied, and relaxes when the voltage is removed. The other family is the.",
    "label": "electroactive-polymers",
    "figures": {
      "families": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "uses": 3
    }
  },
  {
    "title": "Magnetorheological Fluids",
    "subject": "magnetorheological fluids",
    "description": "A magnetorheological fluid is a liquid that thickens into a near-solid under a magnetic field, and thins back into a liquid when the field is switched off. The fluid is oil carrying tiny iron particles, and with no field the particles drift freely and the fluid pours. When a magnetic field is switched on, the particles line up into chains that resist flow, and the fluid can hold a load like a.",
    "label": "magnetorheological-fluids",
    "figures": {
      "switch_time_ms": 1,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "uses": 3
    }
  },
  {
    "title": "Phase-Change Materials",
    "subject": "phase-change materials",
    "description": "A phase-change material is a material that stores and releases heat as it melts and freezes, and it is the simplest programmable thermal battery. When the material melts it absorbs heat without getting hotter, and when it freezes it releases that heat back, so a wall filled with it stays near its melting temperature for hours while the outside warms and cools. Common examples are waxes and.",
    "label": "phase-change-materials",
    "figures": {
      "melting_points": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "uses": 3
    }
  },
  {
    "title": "Self-Healing Polymers",
    "subject": "self-healing polymers",
    "description": "A self-healing polymer is a plastic that repairs its own damage, closing a crack or a cut without outside help. Two designs exist. One carries tiny capsules of liquid glue inside the plastic, and when a crack breaks a capsule the glue flows out, fills the crack, and hardens. The other is built from reversible bonds, which are chemical links that can break and reform, so warming the plastic.",
    "label": "self-healing-polymers",
    "figures": {
      "designs": 2,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "uses": 4
    }
  },
  {
    "title": "Photo-Responsive Materials",
    "subject": "photo-responsive materials",
    "description": "A photo-responsive material is a material that changes when light falls on it, and it is the most convenient programmable material, because light needs no wires and no contact. The changes include colour, as in photochromic glass that darkens in sunlight, shape, as in polymers that bend toward light, and stiffness, as in gels that harden under ultraviolet light. The cause is usually a molecule.",
    "label": "photo-responsive-materials",
    "figures": {
      "changes": 3,
      "records_per_edition": 24,
      "pair_records": 48,
      "sources_per_record": 3,
      "glossary_terms": 50,
      "sections": 16,
      "uses": 3
    }
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Programmable matter",
    "url": "https://en.wikipedia.org/wiki/Programmable_matter",
    "establishes": "Programmable matter: matter whose properties can be changed by a signal, the goal of programmable materials research.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Programmable_matter"
  },
  {
    "name": "Wikipedia - Smart material",
    "url": "https://en.wikipedia.org/wiki/Smart_material",
    "establishes": "Smart material: a material that changes its properties in response to a stimulus such as heat, light, or electricity.",
    "retrieved": "2026-11-17",
    "resource_id": "en.wikipedia.org/wiki/Smart_material"
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic, label) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const total = keys.reduce((s, k) => s + figs[k], 0);
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"min\": min(FIGURES.values()), \"total\": total}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n" +
    "Run 2 SHA-256: " + h + "\n" +
    "Deterministic: MATCH\n";
  return { code, expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = topic.label;
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: EDITION === "public" ? "public-harvest" : "signature-generated",
    ai_name: AI_NAME,
    description: topic.description + " " + "No claim of consciousness, sentience, or unlimited intelligence is established by this system; future-technology framing here is a research or design claim only, never established fact.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One record: a single entry, fully specified and checkable.", A2: "The whole type: every part of the type, specified and tested together.", A3: "The type against the network: the type feeding websites, generators, and the generator database." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug form", a.slug === SLUG);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("19 keys", Object.keys(a).length === 19);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
