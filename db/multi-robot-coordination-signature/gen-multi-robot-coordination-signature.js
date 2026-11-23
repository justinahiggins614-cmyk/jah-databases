// Seeded boundless generator for the Multi-Robot Coordination Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-multi-robot-coordination-signature.js [seed]  (prints one JSON record)
// or: node gen-multi-robot-coordination-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "multi-robot-coordination-signature";
const RECORD_KIND = "multi-robot coordination record";
const ID_PREFIX = "JAH-MRCP-S-";
const AI_NAME = "JAH Multi-Robot Coordination Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Auctioneer Loom",
    "subject": "A Signature design for a market hall where robot teams trade tasks by bid.",
    "description": "The Auctioneer Loom is a Signature design-study: A Signature design for a market hall where robot teams trade tasks by bid. The Auctioneer Loom is a Signature-made design, not a built product: a market hall in software where every task is auctioned and every robot bids from its own costs. Its novelty is a fairness ledger that records every bid, so a robot that always loses can prove it and the team can rebalance the work. The Loom is meant for fleets that grow and shrink during the day, where a fixed plan would go stale within the hour. This is a Signature-made design, presented as a design st",
    "label": "multi-robot-coordination-signature-000001",
    "figures": {
      "robots": 14,
      "tasks": 56,
      "bids": 784,
      "rounds": 7,
      "ledger_entries": 56,
      "success_pct": 95
    }
  },
  {
    "title": "The Consensus Compass",
    "subject": "A Signature design for a compass that points a robot team at its agreed value.",
    "description": "The Consensus Compass is a Signature design-study: A Signature design for a compass that points a robot team at its agreed value. The Consensus Compass is a Signature-made design: a shared dial that shows the team's agreed value, such as a meeting point, and how far each robot still disagrees. Its novelty is a disagreement gauge that turns the spread of opinions into a single number the operator can read at a glance. The Compass is meant for teams that must agree before they act, such as survey teams choosing one map to trust. This is a Signature-made design, presented as a design study only, ",
    "label": "multi-robot-coordination-signature-000002",
    "figures": {
      "robots": 10,
      "rounds": 9,
      "messages": 360,
      "tolerance": 2,
      "gauge": 1,
      "success_pct": 96
    }
  },
  {
    "title": "The Shape-Keeper",
    "subject": "A Signature design for a guardian that holds a robot team in formation.",
    "description": "The Shape-Keeper is a Signature design-study: A Signature design for a guardian that holds a robot team in formation. The Shape-Keeper is a Signature-made design: a guardian program that watches a team's shape and nudges stray robots back into place. Its novelty is a shape memory that remembers the formation even when half the team is out of radio range. The Keeper is meant for survey and carrying teams that must hold a shape across rough ground. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on",
    "label": "multi-robot-coordination-signature-000003",
    "figures": {
      "robots": 16,
      "spacing_m": 3,
      "error_cm": 10,
      "nudges": 24,
      "waypoints": 20,
      "success_pct": 95
    }
  },
  {
    "title": "The Sweep Planner",
    "subject": "A Signature design for a planner that guarantees no ground is left unswept.",
    "description": "The Sweep Planner is a Signature design-study: A Signature design for a planner that guarantees no ground is left unswept. The Sweep Planner is a Signature-made design: a planner that divides any area into cells and proves every cell was visited. Its novelty is a coverage certificate, a signed list of visited cells the team can show to prove the sweep is complete. The Planner is meant for search and inspection teams where a missed patch is a failed mission. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design i",
    "label": "multi-robot-coordination-signature-000004",
    "figures": {
      "robots": 8,
      "cells": 500,
      "area_m2": 2500,
      "sweep_min": 50,
      "certificate": 1,
      "success_pct": 94
    }
  },
  {
    "title": "The Flock Tuner",
    "subject": "A Signature design for tuning flocking rules until a robot crowd moves as one.",
    "description": "The Flock Tuner is a Signature design-study: A Signature design for tuning flocking rules until a robot crowd moves as one. The Flock Tuner is a Signature-made design: a tuning bench that adjusts the three flocking weights until a robot crowd moves smoothly. Its novelty is a smoothness score that measures wobble, so the tuner can compare rule settings without watching hours of video. The Tuner is meant for drone shows and crowd robots, where a ragged flock looks broken. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product.",
    "label": "multi-robot-coordination-signature-000005",
    "figures": {
      "robots": 24,
      "weights": 3,
      "runs": 12,
      "wobble_score": 8,
      "tune_min": 15,
      "success_pct": 94
    }
  },
  {
    "title": "The Safe-Cone Navigator",
    "subject": "A Signature design for a navigator that steers only outside collision cones.",
    "description": "The Safe-Cone Navigator is a Signature design-study: A Signature design for a navigator that steers only outside collision cones. The Safe-Cone Navigator is a Signature-made design: a navigator that draws a cone of dangerous velocities around every obstacle and steers outside all of them. Its novelty is a shared-cone rule that splits the dodge between two robots, so neither swerves into the other. The Navigator is meant for busy fleets where robots cross each other's paths all day. This is a Signature-made design, presented as a design study only, never as an established fact and never as a bu",
    "label": "multi-robot-coordination-signature-000006",
    "figures": {
      "robots": 14,
      "obstacles": 26,
      "checks_per_s": 10,
      "min_gap_m": 2,
      "cones": 26,
      "success_pct": 97
    }
  },
  {
    "title": "The Map Stitcher",
    "subject": "A Signature design for stitching many small robot maps into one big map.",
    "description": "The Map Stitcher is a Signature design-study: A Signature design for stitching many small robot maps into one big map. The Map Stitcher is a Signature-made design: a stitching bench that joins the maps of many robots into one shared map. Its novelty is a confidence thread that marks how sure the stitch is at every seam, so planners trust strong seams and avoid weak ones. The Stitcher is meant for mapping teams in buildings and caves, where no single robot sees the whole place. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built p",
    "label": "multi-robot-coordination-signature-000007",
    "figures": {
      "robots": 6,
      "landmarks": 200,
      "seams": 10,
      "confidence_pct": 93,
      "error_cm": 7,
      "success_pct": 95
    }
  },
  {
    "title": "The Link Keeper",
    "subject": "A Signature design for a guardian that keeps a robot team's radio graph connected.",
    "description": "The Link Keeper is a Signature design-study: A Signature design for a guardian that keeps a robot team's radio graph connected. The Link Keeper is a Signature-made design: a guardian that watches the team's radio links and steers robots back before the graph splits. Its novelty is a connectivity dial that shows one number for the whole graph, so the operator sees trouble coming before the team splits. The Keeper is meant for teams that wander far, where a lost robot is a lost robot. This is a Signature-made design, presented as a design study only, never as an established fact and never as a b",
    "label": "multi-robot-coordination-signature-000008",
    "figures": {
      "robots": 12,
      "links": 36,
      "dial": 4,
      "range_m": 60,
      "warnings": 3,
      "success_pct": 96
    }
  },
  {
    "title": "The Role Wheel",
    "subject": "A Signature design for a wheel that spins roles around a robot team as the mission changes.",
    "description": "The Role Wheel is a Signature design-study: A Signature design for a wheel that spins roles around a robot team as the mission changes. The Role Wheel is a Signature-made design: a wheel that reassigns roles, such as scout and carrier, as the mission changes. Its novelty is a fatigue hand that passes a role to a fresh robot before the holder runs low, instead of after. The Wheel is meant for long missions where robots tire at different rates. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its",
    "label": "multi-robot-coordination-signature-000009",
    "figures": {
      "robots": 11,
      "roles": 5,
      "passes": 4,
      "scores": 55,
      "battery_pct": 70,
      "success_pct": 94
    }
  },
  {
    "title": "The Grid Runner",
    "subject": "A Signature design for a runner that plans grid paths and untangles crossings.",
    "description": "The Grid Runner is a Signature design-study: A Signature design for a runner that plans grid paths and untangles crossings. The Grid Runner is a Signature-made design: a path planner that runs A* for every robot and untangles the crossings. Its novelty is a crossing ledger that records every wait, so the fleet manager can see which crossings cost the most time. The Runner is meant for warehouse grids where crossings are the bottleneck. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own te",
    "label": "multi-robot-coordination-signature-000010",
    "figures": {
      "robots": 10,
      "grid_cells": 2500,
      "path_m": 88,
      "waits": 8,
      "ledger": 8,
      "success_pct": 96
    }
  },
  {
    "title": "The Tree Grower",
    "subject": "A Signature design for growing random trees through cluttered space until a path appears.",
    "description": "The Tree Grower is a Signature design-study: A Signature design for growing random trees through cluttered space until a path appears. The Tree Grower is a Signature-made design: a planner that grows sampling trees through clutter and rewires them shorter as samples arrive. Its novelty is a shared-forest rule that lets trees of different robots warn each other about crowded space. The Grower is meant for robot arms and cluttered rooms where grids fail. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is jud",
    "label": "multi-robot-coordination-signature-000011",
    "figures": {
      "robots": 8,
      "samples": 4200,
      "nodes": 3400,
      "path_m": 62,
      "rewires": 180,
      "success_pct": 93
    }
  },
  {
    "title": "The Node Choir",
    "subject": "A Signature design for a choir of software nodes that sing a robot team into step.",
    "description": "The Node Choir is a Signature design-study: A Signature design for a choir of software nodes that sing a robot team into step. The Node Choir is a Signature-made design: a ROS 2 ensemble where every function is a node and the nodes sing together over a shared network. Its novelty is a conductor score that lists every topic and who sings on it, so a new robot can join the choir by reading one page. The Choir is meant for mixed fleets where robots arrive from different makers. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built pro",
    "label": "multi-robot-coordination-signature-000012",
    "figures": {
      "robots": 9,
      "nodes": 48,
      "topics": 20,
      "messages_per_s": 260,
      "score_pages": 1,
      "success_pct": 96
    }
  },
  {
    "title": "The Branching Tree",
    "subject": "A Signature design for a behaviour tree that always has a backup plan ready.",
    "description": "The Branching Tree is a Signature design-study: A Signature design for a behaviour tree that always has a backup plan ready. The Branching Tree is a Signature-made design: a behaviour tree with a backup branch for every risky action. Its novelty is a fallback count on every branch, so the operator can see at a glance which actions have no backup. The Tree is meant for robots that work far from help, where a failed action must not end the mission. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on",
    "label": "multi-robot-coordination-signature-000013",
    "figures": {
      "robots": 7,
      "tree_nodes": 40,
      "ticks_per_s": 10,
      "fallbacks": 6,
      "actions": 14,
      "success_pct": 95
    }
  },
  {
    "title": "The Merge Table",
    "subject": "A Signature design for a table where robot maps are laid side by side and joined.",
    "description": "The Merge Table is a Signature design-study: A Signature design for a table where robot maps are laid side by side and joined. The Merge Table is a Signature-made design: a table where maps are laid out and joined by their overlapping landmarks. Its novelty is a mismatch alarm that rings when two maps claim the same corridor in different places. The Table is meant for teams mapping the same building from different doors. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether it",
    "label": "multi-robot-coordination-signature-000014",
    "figures": {
      "robots": 5,
      "maps": 5,
      "landmarks": 150,
      "overlaps": 8,
      "alarms": 1,
      "success_pct": 94
    }
  },
  {
    "title": "The Spare-Heart Monitor",
    "subject": "A Signature design for a monitor that hears a robot's heartbeat and calls in a spare.",
    "description": "The Spare-Heart Monitor is a Signature design-study: A Signature design for a monitor that hears a robot's heartbeat and calls in a spare. The Spare-Heart Monitor is a Signature-made design: a monitor that listens for every robot's heartbeat and sends a spare when one goes quiet. Its novelty is a quiet-count rule: three missed beats means failed, no earlier and no later, so the team never abandons a robot for one dropped message. The Monitor is meant for fleets where one failure must never stop the mission. This is a Signature-made design, presented as a design study only, never as an establis",
    "label": "multi-robot-coordination-signature-000015",
    "figures": {
      "robots": 12,
      "heartbeats": 400,
      "failures": 2,
      "spares": 2,
      "recovered": 9,
      "success_pct": 94
    }
  },
  {
    "title": "The Mixed Crew Board",
    "subject": "A Signature design for a board that assigns jobs across different robot types.",
    "description": "The Mixed Crew Board is a Signature design-study: A Signature design for a board that assigns jobs across different robot types. The Mixed Crew Board is a Signature-made design: a board that assigns each job to the robot type built for it, whether it flies, rolls or climbs. Its novelty is a translation frame that puts air, floor and stair positions on one shared map. The Board is meant for disaster and building missions where one type of robot is never enough. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The desig",
    "label": "multi-robot-coordination-signature-000016",
    "figures": {
      "robots": 15,
      "types": 3,
      "tasks": 64,
      "drones": 5,
      "carriers": 7,
      "success_pct": 95
    }
  },
  {
    "title": "The Swarm Whisperer",
    "subject": "A Signature design for a whisper that steers a whole swarm with one command.",
    "description": "The Swarm Whisperer is a Signature design-study: A Signature design for a whisper that steers a whole swarm with one command. The Swarm Whisperer is a Signature-made design: an interface that lets one operator steer fifty robots with a single drawn command. Its novelty is a health halo that shows the swarm as one glowing shape, so trouble is visible without counting dots. The Whisperer is meant for operators who must trust a swarm they cannot watch robot by robot. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The d",
    "label": "multi-robot-coordination-signature-000017",
    "figures": {
      "robots": 50,
      "operators": 1,
      "commands": 9,
      "interventions": 3,
      "halo": 1,
      "success_pct": 93
    }
  },
  {
    "title": "The Shelf River",
    "subject": "A Signature design for a river of shelves flowing to pickers and back.",
    "description": "The Shelf River is a Signature design-study: A Signature design for a river of shelves flowing to pickers and back. The Shelf River is a Signature-made design: a flow plan where shelves move like a river to the pickers and back to storage. Its novelty is a flow gauge that measures shelves per hour at every bend, so a slow bend can be widened before it floods. The River is meant for warehouses that grow shelf by shelf. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its r",
    "label": "multi-robot-coordination-signature-000018",
    "figures": {
      "robots": 120,
      "shelves": 2400,
      "orders_per_h": 330,
      "stations": 16,
      "bends": 8,
      "success_pct": 97
    }
  },
  {
    "title": "The Rubble Listener",
    "subject": "A Signature design for a listener that hears survivors through robot ears.",
    "description": "The Rubble Listener is a Signature design-study: A Signature design for a listener that hears survivors through robot ears. The Rubble Listener is a Signature-made design: a listening array carried by search robots that hears survivors under rubble. Its novelty is a heat-and-sound score that ranks every flagged spot, so rescuers dig where the score is highest first. The Listener is meant for disaster teams where minutes decide lives. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own term",
    "label": "multi-robot-coordination-signature-000019",
    "figures": {
      "robots": 18,
      "area_m2": 1600,
      "flags": 7,
      "score_top": 92,
      "search_min": 36,
      "success_pct": 92
    }
  },
  {
    "title": "The Field Gardener",
    "subject": "A Signature design for a gardener that tends every plant in a field individually.",
    "description": "The Field Gardener is a Signature design-study: A Signature design for a gardener that tends every plant in a field individually. The Field Gardener is a Signature-made design: a team plan where scanning, weeding and harvesting robots tend each plant on its own merits. Its novelty is a plant passport for every plant, recording its health, so treatment goes only where it is needed. The Gardener is meant for farms that want less spray and more care. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged o",
    "label": "multi-robot-coordination-signature-000020",
    "figures": {
      "robots": 10,
      "rows": 80,
      "plants": 9600,
      "passports": 9600,
      "weeds": 1500,
      "success_pct": 94
    }
  },
  {
    "title": "The Deep Lane Planner",
    "subject": "A Signature design for planning survey lanes for underwater robot teams.",
    "description": "The Deep Lane Planner is a Signature design-study: A Signature design for planning survey lanes for underwater robot teams. The Deep Lane Planner is a Signature-made design: a lane plan for underwater robots that cannot talk while they work. Its novelty is a surfacing clock that schedules every surfacing, so maps are shared on time and no robot is left unheard. The Planner is meant for sea-floor surveys and pipeline inspections. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: wh",
    "label": "multi-robot-coordination-signature-000021",
    "figures": {
      "robots": 6,
      "lanes": 26,
      "area_km2": 9,
      "depth_m": 130,
      "surfacings": 12,
      "success_pct": 93
    }
  },
  {
    "title": "The Sky Painter",
    "subject": "A Signature design for painting pictures in the sky with drone teams.",
    "description": "The Sky Painter is a Signature design-study: A Signature design for painting pictures in the sky with drone teams. The Sky Painter is a Signature-made design: a choreographer that paints pictures in the sky with light-carrying drones. Its novelty is a safety curtain that keeps every drone inside its own bubble of sky, so a fault never becomes a collision. The Painter is meant for shows and surveys where the pattern must be exact. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: w",
    "label": "multi-robot-coordination-signature-000022",
    "figures": {
      "robots": 44,
      "flights": 130,
      "photos": 2600,
      "area_ha": 32,
      "show_min": 13,
      "success_pct": 96
    }
  },
  {
    "title": "The Course Layer",
    "subject": "A Signature design for laying courses of bricks with robot teams on building sites.",
    "description": "The Course Layer is a Signature design-study: A Signature design for laying courses of bricks with robot teams on building sites. The Course Layer is a Signature-made design: a plan for bricklaying robots that lay straight courses from a shared digital model. Its novelty is a laser check after every course, so a crooked course is caught before the next one is laid. The Layer is meant for building sites where the plan and the wall must agree. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its ",
    "label": "multi-robot-coordination-signature-000023",
    "figures": {
      "robots": 9,
      "courses": 50,
      "bricks": 7500,
      "checks": 100,
      "site_m2": 1900,
      "success_pct": 92
    }
  },
  {
    "title": "The Ward Runner",
    "subject": "A Signature design for a runner that carries medicine through hospital corridors.",
    "description": "The Ward Runner is a Signature design-study: A Signature design for a runner that carries medicine through hospital corridors. The Ward Runner is a Signature-made design: a delivery plan for hospital robots that carry medicine in locked compartments. Its novelty is a handover seal that records who opened each compartment, so every dose is accounted for. The Runner is meant for hospitals where nurses' time belongs with patients. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whe",
    "label": "multi-robot-coordination-signature-000024",
    "figures": {
      "robots": 8,
      "deliveries": 100,
      "wards": 12,
      "seals": 100,
      "trips": 100,
      "success_pct": 97
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
    "name": "Multi-agent system (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Multi-agent_system",
    "retrieved": "2026-11-18"
  },
  {
    "name": "Multi-agent system (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Multi-agent_system",
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
