// Seeded boundless generator for the Swarm Robotics Laboratory Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-swarm-robotics-laboratory-signature.js [seed]  (prints one JSON record)
// or: node gen-swarm-robotics-laboratory-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "swarm-robotics-laboratory-signature";
const RECORD_KIND = "swarm-robotics laboratory record";
const ID_PREFIX = "JAH-SWRB-S-";
const AI_NAME = "JAH Swarm Robotics Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Trail Layer",
    "subject": "A Signature design for laying scent trails that robot swarms can follow.",
    "description": "The Trail Layer is a Signature design-study: A Signature design for laying scent trails that robot swarms can follow. The Trail Layer is a Signature-made design: a trail system where robots lay digital scent on good paths and follow the strongest scent. Its novelty is a fade clock that weakens every trail on schedule, so the swarm never follows yesterday's news. The Layer is meant for search swarms in changing places. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its r",
    "label": "swarm-robotics-laboratory-signature-000001",
    "figures": {
      "robots": 32,
      "paths": 130,
      "scent": 88,
      "rounds": 26,
      "best_m": 40,
      "success_pct": 94
    }
  },
  {
    "title": "The Best-Spot Seeker",
    "subject": "A Signature design for a seeker that steers between its own best and the swarm's best.",
    "description": "The Best-Spot Seeker is a Signature design-study: A Signature design for a seeker that steers between its own best and the swarm's best. The Best-Spot Seeker is a Signature-made design: a search rule where each robot steers between its personal best spot and the swarm's best spot. Its novelty is a wander dial the operator can turn, so the swarm can be told to explore more or settle sooner. The Seeker is meant for tuning and placement jobs where the best spot is unknown. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product.",
    "label": "swarm-robotics-laboratory-signature-000002",
    "figures": {
      "robots": 42,
      "rounds": 32,
      "best_score": 98,
      "search_area": 420,
      "dial": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The Dance Floor",
    "subject": "A Signature design for a floor where robot bees dance to advertise good sources.",
    "description": "The Dance Floor is a Signature design-study: A Signature design for a floor where robot bees dance to advertise good sources. The Dance Floor is a Signature-made design: a foraging system where working robots dance to advertise rich sources and watchers choose by the dance. Its novelty is a retirement bell that rings for any source that stops improving, sending its workers out as scouts. The Floor is meant for foraging swarms that must never get stuck on a dry source. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. T",
    "label": "swarm-robotics-laboratory-signature-000003",
    "figures": {
      "robots": 38,
      "sources": 26,
      "scouts": 7,
      "rounds": 42,
      "richness": 93,
      "success_pct": 93
    }
  },
  {
    "title": "The Tabletop Thousand",
    "subject": "A Signature design for a thousand-robot tabletop swarm experiment.",
    "description": "The Tabletop Thousand is a Signature design-study: A Signature design for a thousand-robot tabletop swarm experiment. The Tabletop Thousand is a Signature-made design: a tabletop arena for a thousand tiny vibrating robots, each cheaper than a meal. Its novelty is a charging ceiling that powers the whole swarm from above, so no robot ever needs to leave the table. The Thousand is meant for experiments that need numbers no small team can give. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its ",
    "label": "swarm-robotics-laboratory-signature-000004",
    "figures": {
      "robots": 1000,
      "cost_usd": 14,
      "table_m2": 3,
      "joined": 940,
      "form_min": 10,
      "success_pct": 95
    }
  },
  {
    "title": "The Puck School",
    "subject": "A Signature design for a school of identical puck robots that test swarm rules.",
    "description": "The Puck School is a Signature design-study: A Signature design for a school of identical puck robots that test swarm rules. The Puck School is a Signature-made design: a school of identical puck-shaped robots for testing swarm rules fairly. Its novelty is a swap rule: any robot can be swapped for another without changing the experiment, so results repeat. The School is meant for classrooms and labs that need honest comparisons. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: wh",
    "label": "swarm-robotics-laboratory-signature-000005",
    "figures": {
      "robots": 14,
      "sensors": 8,
      "arena_m2": 5,
      "runs": 22,
      "speed_cms": 13,
      "success_pct": 94
    }
  },
  {
    "title": "The Marker Garden",
    "subject": "A Signature design for a garden of markers that robots plant and follow.",
    "description": "The Marker Garden is a Signature design-study: A Signature design for a garden of markers that robots plant and follow. The Marker Garden is a Signature-made design: a shared map where robots plant markers where they find something useful, and others follow them. Its novelty is a weeding rule that pulls up stale markers, so the garden always shows fresh information. The Garden is meant for swarms that must coordinate without radio links. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own ",
    "label": "swarm-robotics-laboratory-signature-000006",
    "figures": {
      "robots": 26,
      "markers": 320,
      "weeds": 60,
      "structures": 4,
      "rounds": 32,
      "success_pct": 93
    }
  },
  {
    "title": "The Docking Chain",
    "subject": "A Signature design for robots that link into chains and bridges.",
    "description": "The Docking Chain is a Signature design-study: A Signature design for robots that link into chains and bridges. The Docking Chain is a Signature-made design: a chain of robots that grip each other to cross gaps and pull loads. Its novelty is a split signal that tells the chain when to break apart, so the swarm never stays stiff when it should be free. The Chain is meant for rough ground where one robot alone cannot pass. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether it",
    "label": "swarm-robotics-laboratory-signature-000007",
    "figures": {
      "robots": 20,
      "docks": 26,
      "bridge_m": 2,
      "gaps": 7,
      "split_s": 28,
      "success_pct": 92
    }
  },
  {
    "title": "The Pattern Watcher",
    "subject": "A Signature design for watching order appear from local rules.",
    "description": "The Pattern Watcher is a Signature design-study: A Signature design for watching order appear from local rules. The Pattern Watcher is a Signature-made design: a watch post that measures how fast order appears in a swarm from local rules. Its novelty is a disturbance test: it pokes the swarm and times how fast the pattern returns. The Watcher is meant for researchers who need proof that a pattern is stable, not luck. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its ru",
    "label": "swarm-robotics-laboratory-signature-000008",
    "figures": {
      "robots": 42,
      "rules": 3,
      "form_min": 4,
      "recovery_s": 42,
      "patterns": 6,
      "success_pct": 94
    }
  },
  {
    "title": "The Gradient Gardener",
    "subject": "A Signature design for growing robot shapes from a seed signal.",
    "description": "The Gradient Gardener is a Signature design-study: A Signature design for growing robot shapes from a seed signal. The Gradient Gardener is a Signature-made design: a gardener that grows robot shapes from a seed, layer by layer, following a gradient signal. Its novelty is a repair reflex: when a robot fails, neighbours sense the gap in the signal and move in. The Gardener is meant for shapes that must heal themselves. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its r",
    "label": "swarm-robotics-laboratory-signature-000009",
    "figures": {
      "robots": 52,
      "layers": 5,
      "error_cm": 4,
      "repair_s": 55,
      "gradients": 3,
      "success_pct": 93
    }
  },
  {
    "title": "The Scent Map",
    "subject": "A Signature design for a map drawn in fading scent.",
    "description": "The Scent Map is a Signature design-study: A Signature design for a map drawn in fading scent. The Scent Map is a Signature-made design: a map where value is drawn in scent that fades, so the map always shows what is fresh. Its novelty is a strength scale that lets robots compare trails at a glance. The Map is meant for swarms that share knowledge without talking. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its parts fit together, and its checks ",
    "label": "swarm-robotics-laboratory-signature-000010",
    "figures": {
      "robots": 32,
      "trails": 9,
      "fade_s": 55,
      "followers": 24,
      "markers": 190,
      "success_pct": 94
    }
  },
  {
    "title": "The Mound Builder",
    "subject": "A Signature design for a termite-style builder that raises walls one pellet at a time.",
    "description": "The Mound Builder is a Signature design-study: A Signature design for a termite-style builder that raises walls one pellet at a time. The Mound Builder is a Signature-made design: a builder that raises walls by placing one brick where others have already built. Its novelty is a climbing rule that lets builders ride the wall they are raising, so work never stops at the top edge. The Builder is meant for shelters in places where people cannot yet go. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged ",
    "label": "swarm-robotics-laboratory-signature-000011",
    "figures": {
      "robots": 14,
      "bricks": 420,
      "height_m": 2,
      "layers": 22,
      "build_min": 58,
      "success_pct": 92
    }
  },
  {
    "title": "The Tube Pruner",
    "subject": "A Signature design for growing networks and pruning the useless tubes.",
    "description": "The Tube Pruner is a Signature design-study: A Signature design for growing networks and pruning the useless tubes. The Tube Pruner is a Signature-made design: a network grower that reinforces busy tubes and prunes idle ones, the way a slime mould does. Its novelty is a flow meter on every tube, so pruning is by measured traffic, not by guess. The Pruner is meant for network design where the efficient shape is unknown. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its ",
    "label": "swarm-robotics-laboratory-signature-000012",
    "figures": {
      "robots": 22,
      "paths": 64,
      "foods": 5,
      "prunes": 12,
      "length_m": 36,
      "success_pct": 93
    }
  },
  {
    "title": "The Blink Choir",
    "subject": "A Signature design for a choir of robots that blink in unison.",
    "description": "The Blink Choir is a Signature design-study: A Signature design for a choir of robots that blink in unison. The Blink Choir is a Signature-made design: a choir where each robot nudges its clock when it sees a neighbour flash, until all flash as one. Its novelty is a beat keeper that turns the shared flash into a start signal for joint tasks. The Choir is meant for swarms that need shared timing without radio messages. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its r",
    "label": "swarm-robotics-laboratory-signature-000013",
    "figures": {
      "robots": 48,
      "flashes": 96,
      "sync_s": 24,
      "error_ms": 38,
      "beats": 12,
      "success_pct": 95
    }
  },
  {
    "title": "The School Keeper",
    "subject": "A Signature design for keeping a robot school together while it surveys.",
    "description": "The School Keeper is a Signature design-study: A Signature design for keeping a robot school together while it surveys. The School Keeper is a Signature-made design: a keeper that holds a robot school together with three-zone steering while it surveys. Its novelty is a drafting gauge that measures the energy saved by swimming behind neighbours. The Keeper is meant for underwater surveys that must not scatter the wildlife. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether i",
    "label": "swarm-robotics-laboratory-signature-000014",
    "figures": {
      "robots": 26,
      "zones": 3,
      "cohesion_pct": 92,
      "survey_m2": 1300,
      "saved_pct": 19,
      "success_pct": 94
    }
  },
  {
    "title": "The Murmuration Rig",
    "subject": "A Signature design for a rig that flies drone flocks like starling murmurations.",
    "description": "The Murmuration Rig is a Signature design-study: A Signature design for a rig that flies drone flocks like starling murmurations. The Murmuration Rig is a Signature-made design: a rig that flies drone flocks on the seven-neighbour rule measured from starlings. Its novelty is a split alarm that warns when a sharp turn is about to divide the flock. The Rig is meant for large drone formations that must turn as one. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules a",
    "label": "swarm-robotics-laboratory-signature-000015",
    "figures": {
      "robots": 64,
      "neighbours": 7,
      "turn_deg_s": 42,
      "flock_m": 32,
      "splits": 1,
      "success_pct": 93
    }
  },
  {
    "title": "The Fast Bench",
    "subject": "A Signature design for a bench that simulates a thousand robots faster than real time.",
    "description": "The Fast Bench is a Signature design-study: A Signature design for a bench that simulates a thousand robots faster than real time. The Fast Bench is a Signature-made design: a simulator bench that runs a thousand swarm robots faster than real time. Its novelty is a rule library that stores every tested rule with its score, so no rule is ever tested twice. The Bench is meant for researchers who need hundreds of trials before lunch. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: ",
    "label": "swarm-robotics-laboratory-signature-000016",
    "figures": {
      "robots": 1000,
      "steps": 5200,
      "speed": 8,
      "rules": 42,
      "arena_m2": 100,
      "success_pct": 95
    }
  },
  {
    "title": "The Swarm Atlas",
    "subject": "A Signature design for an atlas that holds every swarm rule in one book.",
    "description": "The Swarm Atlas is a Signature design-study: A Signature design for an atlas that holds every swarm rule in one book. The Swarm Atlas is a Signature-made design: an atlas that collects every swarm rule with its test scale and its robustness score. Its novelty is a robustness stamp on each rule, earned by removing robots mid-run and measuring the damage. The Atlas is meant for engineers choosing a rule for a real job. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its ru",
    "label": "swarm-robotics-laboratory-signature-000017",
    "figures": {
      "robots": 100,
      "rules": 26,
      "runs": 64,
      "robustness_pct": 89,
      "scales": 4,
      "success_pct": 94
    }
  },
  {
    "title": "The Arena Keeper",
    "subject": "A Signature design for a laboratory arena that resets itself between experiments.",
    "description": "The Arena Keeper is a Signature design-study: A Signature design for a laboratory arena that resets itself between experiments. The Arena Keeper is a Signature-made design: an arena with a camera ceiling, chargers and a reset routine, so every experiment starts the same. Its novelty is a replay tape that records every position and message, so a surprising result can be watched again. The Keeper is meant for labs that must compare results fairly. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on ",
    "label": "swarm-robotics-laboratory-signature-000018",
    "figures": {
      "robots": 52,
      "cameras": 4,
      "runs": 32,
      "arena_m2": 26,
      "resets": 32,
      "success_pct": 95
    }
  },
  {
    "title": "The Sense Weaver",
    "subject": "A Signature design for weaving many small sensor readings into one picture.",
    "description": "The Sense Weaver is a Signature design-study: A Signature design for weaving many small sensor readings into one picture. The Sense Weaver is a Signature-made design: a weaver that fuses scattered sensor readings into one map of the world. Its novelty is a freshness weight that trusts new readings more than old ones, so the map never shows yesterday's weather. The Weaver is meant for leak hunting, heat mapping and wildlife tracking. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms",
    "label": "swarm-robotics-laboratory-signature-000019",
    "figures": {
      "robots": 34,
      "readings": 1000,
      "area_m2": 850,
      "hot_spots": 6,
      "error_pct": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The Harvest Trail",
    "subject": "A Signature design for a trail that leads a swarm to scattered items and home again.",
    "description": "The Harvest Trail is a Signature design-study: A Signature design for a trail that leads a swarm to scattered items and home again. The Harvest Trail is a Signature-made design: a foraging trail that recruits just enough robots to each find, and no more. Its novelty is a balance scale that weighs trail strength against robot count, so no trail is overstaffed. The Trail is meant for collection jobs where the score is items per hour. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms:",
    "label": "swarm-robotics-laboratory-signature-000020",
    "figures": {
      "robots": 30,
      "items": 130,
      "collected": 118,
      "trails": 7,
      "forage_min": 32,
      "success_pct": 94
    }
  },
  {
    "title": "The Cluster Bell",
    "subject": "A Signature design for a bell that gathers a scattered swarm into one cluster.",
    "description": "The Cluster Bell is a Signature design-study: A Signature design for a bell that gathers a scattered swarm into one cluster. The Cluster Bell is a Signature-made design: a beacon bell that calls a scattered swarm to one meeting point. Its novelty is a room rule that makes early arrivals step aside, so latecomers can always join. The Bell is meant for swarms that must gather before a joint job. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its parts",
    "label": "swarm-robotics-laboratory-signature-000021",
    "figures": {
      "robots": 38,
      "beacons": 1,
      "gather_s": 46,
      "radius_m": 2,
      "clusters": 1,
      "success_pct": 95
    }
  },
  {
    "title": "The Even Spreader",
    "subject": "A Signature design for spreading robots evenly so no patch is watched twice.",
    "description": "The Even Spreader is a Signature design-study: A Signature design for spreading robots evenly so no patch is watched twice. The Even Spreader is a Signature-made design: a spreader that pushes each robot away from its nearest neighbour until the spacing is even. Its novelty is a gap meter that reports the largest uncovered hole, so the operator knows the worst patch at a glance. The Spreader is meant for sensor coverage and search. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms:",
    "label": "swarm-robotics-laboratory-signature-000022",
    "figures": {
      "robots": 32,
      "gaps_m": 3,
      "coverage_pct": 93,
      "area_m2": 640,
      "spacing_m": 4,
      "success_pct": 94
    }
  },
  {
    "title": "The Shape Choir",
    "subject": "A Signature design for a choir that sings robots into letters and shapes.",
    "description": "The Shape Choir is a Signature design-study: A Signature design for a choir that sings robots into letters and shapes. The Shape Choir is a Signature-made design: a choir that arranges robots into letters, circles and grids from local rules alone. Its novelty is an error song: the average distance from target, sung as one number the operator can hear change. The Choir is meant for shows and benchmarks where the shape proves the rules. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own ter",
    "label": "swarm-robotics-laboratory-signature-000023",
    "figures": {
      "robots": 50,
      "spots": 50,
      "error_cm": 8,
      "form_min": 6,
      "shapes": 5,
      "success_pct": 95
    }
  },
  {
    "title": "The Graceful Degrader",
    "subject": "A Signature design for a swarm that fades gently instead of collapsing when robots fail.",
    "description": "The Graceful Degrader is a Signature design-study: A Signature design for a swarm that fades gently instead of collapsing when robots fail. The Graceful Degrader is a Signature-made design: a swarm rule that loses a little performance with each failure and never collapses suddenly. Its novelty is a degradation curve, published with the rule, so buyers know exactly what each lost robot costs. The Degrader is meant for field swarms where failures are certain. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design i",
    "label": "swarm-robotics-laboratory-signature-000024",
    "figures": {
      "robots": 84,
      "failures": 8,
      "score_before": 93,
      "score_after": 87,
      "recover_s": 18,
      "success_pct": 95
    }
  }
];

function canonical(o) {
  if (o === null || typeof o !== "object") return JSON.stringify(o);
  if (Array.isArray(o)) return "[" + o.map(canonical).join(",") + "]";
  return "{" + Object.keys(o).sort().map(k => JSON.stringify(k) + ":" + canonical(o[k])).join(",") + "}";
}

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function generate(seed) {
  const rnd = mulberry32(seed);
  const t = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const n = 1 + Math.floor(rnd() * 24);
  const id = ID_PREFIX + String(n).padStart(6, "0");
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: t.title,
    subject: t.subject,
    status: "generated",
    src: "signature-generated",
    ai_name: AI_NAME,
    description: t.description,
    label: t.label,
    figures: t.figures,
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

const SOURCES = [
  {
    "name": "Ant colony optimization algorithms (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms",
    "retrieved": "2026-11-18"
  },
  {
    "name": "Swarm robotics (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Swarm_robotics",
    "retrieved": "2026-11-18"
  }
];

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
  t("17 keys", Object.keys(a).length === 17);
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
