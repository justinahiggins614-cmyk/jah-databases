// Seeded boundless generator for the Autonomous Logistics Control Center Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-autonomous-logistics-control-center-signature.js [seed]  (prints one JSON record)
// or: node gen-autonomous-logistics-control-center-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "autonomous-logistics-control-center-signature";
const RECORD_KIND = "autonomous logistics control center record";
const ID_PREFIX = "JAH-ALCC-S-";
const AI_NAME = "JAH Autonomous Logistics Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Guided Cart",
    "subject": "A Signature design for a cart that follows a wire and never gets lost.",
    "description": "The Guided Cart is a Signature design-study: A Signature design for a cart that follows a wire and never gets lost. The Guided Cart is a Signature-made design: a driverless cart that follows wires and laser marks through a warehouse. Its novelty is a crossing bell that rings before the cart enters a crossing, so other carts wait in time. The Cart is meant for routes that never change. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its parts fit toge",
    "label": "autonomous-logistics-control-center-signature-000001",
    "figures": {
      "robots": 26,
      "loads_per_h": 190,
      "paths_km": 6,
      "crossings": 19,
      "charge_min": 20,
      "success_pct": 96
    }
  },
  {
    "title": "The Free Roamer",
    "subject": "A Signature design for a warehouse robot that plans its own path every trip.",
    "description": "The Free Roamer is a Signature design-study: A Signature design for a warehouse robot that plans its own path every trip. The Free Roamer is a Signature-made design: a warehouse robot that navigates freely with maps and lidar, planning a fresh route for every trip. Its novelty is a courtesy rule that makes robots yield in narrow aisles by size, so the smallest never waits longest. The Roamer is meant for warehouses that change their layout. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its o",
    "label": "autonomous-logistics-control-center-signature-000002",
    "figures": {
      "robots": 64,
      "goals_per_h": 250,
      "map_m2": 12500,
      "detours": 38,
      "aisles": 32,
      "success_pct": 96
    }
  },
  {
    "title": "The Knowing Shelf",
    "subject": "A Signature design for a shelf that always knows where every item is.",
    "description": "The Knowing Shelf is a Signature design-study: A Signature design for a shelf that always knows where every item is. The Knowing Shelf is a Signature-made design: a warehouse brain that knows the place of every item and the best order to pick them. Its novelty is a freshness stamp on every location, so the system knows which locations it has not checked lately. The Shelf is meant for warehouses where the wrong item in the wrong box is the costliest error. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is ",
    "label": "autonomous-logistics-control-center-signature-000003",
    "figures": {
      "robots": 0,
      "items": 50000,
      "orders_per_day": 3300,
      "accuracy_pct": 99,
      "locations": 12500,
      "success_pct": 97
    }
  },
  {
    "title": "The Fleet Eye",
    "subject": "A Signature design for one eye that watches a whole robot fleet.",
    "description": "The Fleet Eye is a Signature design-study: A Signature design for one eye that watches a whole robot fleet. The Fleet Eye is a Signature-made design: a single screen that shows every robot's battery, place and job at once. Its novelty is a tiredness forecast that predicts which robot will need charging next, before it asks. The Eye is meant for fleets too big to watch robot by robot. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its parts fit toget",
    "label": "autonomous-logistics-control-center-signature-000004",
    "figures": {
      "robots": 84,
      "jobs_per_day": 2500,
      "utilisation_pct": 87,
      "charges": 126,
      "failures": 3,
      "success_pct": 95
    }
  },
  {
    "title": "The Route Weaver",
    "subject": "A Signature design for weaving the cheapest set of delivery routes each morning.",
    "description": "The Route Weaver is a Signature design-study: A Signature design for weaving the cheapest set of delivery routes each morning. The Route Weaver is a Signature-made design: a weaver that builds the cheapest set of routes for the day's deliveries before the vans leave. Its novelty is a re-weave button that rebuilds the routes in minutes when a rush order lands. The Weaver is meant for delivery fleets where the plan changes daily. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whe",
    "label": "autonomous-logistics-control-center-signature-000005",
    "figures": {
      "robots": 0,
      "vehicles": 19,
      "customers": 250,
      "routes": 19,
      "distance_km": 1280,
      "success_pct": 95
    }
  },
  {
    "title": "The Single Tour",
    "subject": "A Signature design for the shortest tour that visits every stop once.",
    "description": "The Single Tour is a Signature design-study: A Signature design for the shortest tour that visits every stop once. The Single Tour is a Signature-made design: a tour planner that finds the shortest route visiting every stop once and coming home. Its novelty is a segment-flip test that tries reversing every part of the tour, so no shortcut is missed. The Tour is meant for drivers, readers and repair crews with many stops. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether it",
    "label": "autonomous-logistics-control-center-signature-000006",
    "figures": {
      "robots": 0,
      "stops": 50,
      "tour_km": 98,
      "segments": 13,
      "improvement_pct": 19,
      "success_pct": 96
    }
  },
  {
    "title": "The Doorstep Runner",
    "subject": "A Signature design for a runner that owns the last mile to the door.",
    "description": "The Doorstep Runner is a Signature design-study: A Signature design for a runner that owns the last mile to the door. The Doorstep Runner is a Signature-made design: a last-mile plan that mixes robots, vans and lockers so the final step costs the least. Its novelty is a locker-first rule that serves many customers at one stop before sending any robot to a single door. The Runner is meant for neighbourhoods where the last mile costs more than the rest of the journey. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The",
    "label": "autonomous-logistics-control-center-signature-000007",
    "figures": {
      "robots": 16,
      "deliveries": 620,
      "lockers": 42,
      "cost_usd": 3,
      "stops": 185,
      "success_pct": 94
    }
  },
  {
    "title": "The Straight-Through Dock",
    "subject": "A Signature design for a dock where goods never stop moving.",
    "description": "The Straight-Through Dock is a Signature design-study: A Signature design for a dock where goods never stop moving. The Straight-Through Dock is a Signature-made design: a cross-dock where goods move from one truck to another without ever being stored. Its novelty is a dwell clock on every pallet that rings when a pallet has waited too long. The Dock is meant for fresh food and parcels where speed beats storage. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules a",
    "label": "autonomous-logistics-control-center-signature-000008",
    "figures": {
      "robots": 0,
      "pallets": 820,
      "dwell_min": 24,
      "docks": 13,
      "trucks": 42,
      "success_pct": 96
    }
  },
  {
    "title": "The Tall Fetcher",
    "subject": "A Signature design for a fetcher that climbs tall racks and brings any box in seconds.",
    "description": "The Tall Fetcher is a Signature design-study: A Signature design for a fetcher that climbs tall racks and brings any box in seconds. The Tall Fetcher is a Signature-made design: a rack crane and shuttle system that fetches any box from a tall, dense warehouse. Its novelty is a fast-front rule that keeps fast-moving boxes near the front, so the fetcher rarely climbs far. The Fetcher is meant for parts, medicines and online orders. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: w",
    "label": "autonomous-logistics-control-center-signature-000009",
    "figures": {
      "robots": 13,
      "boxes": 98000,
      "fetches_per_h": 410,
      "aisles": 8,
      "height_m": 24,
      "success_pct": 97
    }
  },
  {
    "title": "The Moving River",
    "subject": "A Signature design for a river of belts that carries goods without hands.",
    "description": "The Moving River is a Signature design-study: A Signature design for a river of belts that carries goods without hands. The Moving River is a Signature-made design: a conveyor river that carries goods through receiving, storage and shipping without hands. Its novelty is a jam watch that spots a slow lane and opens a relief lane before the river floods. The River is meant for parcel hubs where thousands of items move every hour. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whe",
    "label": "autonomous-logistics-control-center-signature-000010",
    "figures": {
      "robots": 0,
      "belts_km": 4,
      "items_per_h": 6200,
      "lanes": 17,
      "jams": 4,
      "success_pct": 96
    }
  },
  {
    "title": "The Chute Choir",
    "subject": "A Signature design for a choir of chutes that sings each parcel to the right truck.",
    "description": "The Chute Choir is a Signature design-study: A Signature design for a choir of chutes that sings each parcel to the right truck. The Chute Choir is a Signature-made design: a sorter that sings each parcel into the right chute at thousands per hour. Its novelty is a miss bell that rings the moment a parcel enters the wrong chute, so it can be caught at once. The Choir is meant for parcel hubs where one wrong chute means the wrong city. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own ter",
    "label": "autonomous-logistics-control-center-signature-000011",
    "figures": {
      "robots": 0,
      "parcels_per_h": 9200,
      "chutes": 62,
      "missorts": 8,
      "scanners": 13,
      "success_pct": 97
    }
  },
  {
    "title": "The Yard Conductor",
    "subject": "A Signature design for a conductor that runs the yard where trucks wait and dock.",
    "description": "The Yard Conductor is a Signature design-study: A Signature design for a conductor that runs the yard where trucks wait and dock. The Yard Conductor is a Signature-made design: a conductor that tells every truck which dock to use and when, so docks are never idle. Its novelty is a waiting clock that shows every driver's wait, so the longest wait is always served next. The Conductor is meant for yards where a waiting truck is wasted money. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own",
    "label": "autonomous-logistics-control-center-signature-000012",
    "figures": {
      "robots": 0,
      "trailers": 125,
      "docks": 25,
      "wait_min": 17,
      "shunt_trucks": 6,
      "success_pct": 94
    }
  },
  {
    "title": "The Quay Crane",
    "subject": "A Signature design for a crane that stacks containers with no one on the ground.",
    "description": "The Quay Crane is a Signature design-study: A Signature design for a crane that stacks containers with no one on the ground. The Quay Crane is a Signature-made design: an automated crane that lifts containers from ship to yard and stacks them so the right one is always on top. Its novelty is a top-of-stack promise: the software guarantees the next container needed is never buried. The Crane is meant for ports that cannot stop while they grow. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its",
    "label": "autonomous-logistics-control-center-signature-000013",
    "figures": {
      "robots": 42,
      "containers_per_day": 4100,
      "cranes": 13,
      "stacks": 62,
      "turnaround_h": 13,
      "success_pct": 95
    }
  },
  {
    "title": "The Sky Loader",
    "subject": "A Signature design for a loader that fills aircraft holds in under an hour.",
    "description": "The Sky Loader is a Signature design-study: A Signature design for a loader that fills aircraft holds in under an hour. The Sky Loader is a Signature-made design: a cargo loader that builds pallets in flight order and fills an aircraft hold before its turnaround ends. Its novelty is a left-behind alarm that lists any piece not yet loaded ten minutes before departure. The Loader is meant for airports where the aircraft cannot wait. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: ",
    "label": "autonomous-logistics-control-center-signature-000014",
    "figures": {
      "robots": 0,
      "pieces_per_day": 12500,
      "pallets": 250,
      "flights": 50,
      "on_time_pct": 95,
      "success_pct": 94
    }
  },
  {
    "title": "The Cold Watcher",
    "subject": "A Signature design for a watcher that never lets food or medicine warm up.",
    "description": "The Cold Watcher is a Signature design-study: A Signature design for a watcher that never lets food or medicine warm up. The Cold Watcher is a Signature-made design: a sensor net that watches the temperature of every truck, room and box in a cold chain. Its novelty is a warm-hour alarm that rings the moment any load leaves its safe range. The Watcher is meant for vaccines and fresh food, where one warm hour spoils everything. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: wheth",
    "label": "autonomous-logistics-control-center-signature-000015",
    "figures": {
      "robots": 0,
      "sensors": 500,
      "trucks": 62,
      "breaks": 2,
      "loads": 1250,
      "success_pct": 97
    }
  },
  {
    "title": "The Demand Reader",
    "subject": "A Signature design for a reader that predicts what customers will order next.",
    "description": "The Demand Reader is a Signature design-study: A Signature design for a reader that predicts what customers will order next. The Demand Reader is a Signature-made design: a forecaster that reads past sales, seasons and weather to predict what customers will order. Its novelty is an error mirror that shows the forecast's past mistakes next to the new forecast, so nobody trusts it blindly. The Reader is meant for warehouses that must stock before the orders arrive. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The de",
    "label": "autonomous-logistics-control-center-signature-000016",
    "figures": {
      "robots": 0,
      "products": 8200,
      "error_pct": 9,
      "safety_days": 3,
      "stockouts": 11,
      "success_pct": 93
    }
  },
  {
    "title": "The Just-Enough Store",
    "subject": "A Signature design for a store that holds just enough stock and no more.",
    "description": "The Just-Enough Store is a Signature design-study: A Signature design for a store that holds just enough stock and no more. The Just-Enough Store is a Signature-made design: an inventory plan that holds enough stock to meet demand and not a box more. Its novelty is a turns dial that shows how fast stock sells through, so slow stock is spotted before it gathers dust. The Store is meant for sellers who pay rent on every shelf. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whethe",
    "label": "autonomous-logistics-control-center-signature-000017",
    "figures": {
      "robots": 0,
      "products": 12500,
      "service_pct": 97,
      "turns": 9,
      "holding_cost": 230000,
      "success_pct": 94
    }
  },
  {
    "title": "The Mirror Warehouse",
    "subject": "A Signature design for a live mirror of a warehouse that sees jams coming.",
    "description": "The Mirror Warehouse is a Signature design-study: A Signature design for a live mirror of a warehouse that sees jams coming. The Mirror Warehouse is a Signature-made design: a live virtual copy of a warehouse that simulates the next hour and warns of jams before they form. Its novelty is a what-if lever: pull it and the mirror shows the effect of moving a shelf, before anyone moves it. The Mirror is meant for managers who would rather prevent a jam than clear one. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The d",
    "label": "autonomous-logistics-control-center-signature-000018",
    "figures": {
      "robots": 62,
      "sensors": 920,
      "horizon_min": 60,
      "jams_predicted": 15,
      "layouts": 7,
      "success_pct": 94
    }
  },
  {
    "title": "The Watch Tower",
    "subject": "A Signature design for a tower that watches a whole supply chain at once.",
    "description": "The Watch Tower is a Signature design-study: A Signature design for a tower that watches a whole supply chain at once. The Watch Tower is a Signature-made design: a central screen that watches a whole supply chain and turns late ships and storms into single alerts. Its novelty is a ripple map that shows how one delay spreads across hundreds of orders. The Tower is meant for shippers too big to watch one order at a time. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its",
    "label": "autonomous-logistics-control-center-signature-000019",
    "figures": {
      "robots": 0,
      "shipments": 9200,
      "alerts": 125,
      "reroutes": 50,
      "on_time_pct": 94,
      "success_pct": 93
    }
  },
  {
    "title": "The Fuel Train",
    "subject": "A Signature design for a train of trucks that saves fuel by drafting.",
    "description": "The Fuel Train is a Signature design-study: A Signature design for a train of trucks that saves fuel by drafting. The Fuel Train is a Signature-made design: a convoy of trucks linked by radio, drafting behind the leader to save fuel. Its novelty is a gap governor that widens the gap in rain and narrows it in calm air, so safety follows the weather. The Train is meant for long-haul routes where fuel is the biggest cost. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its ",
    "label": "autonomous-logistics-control-center-signature-000020",
    "figures": {
      "robots": 0,
      "trucks": 5,
      "gap_m": 12,
      "fuel_saved_pct": 11,
      "platoon_km": 850,
      "success_pct": 93
    }
  },
  {
    "title": "The Sky Courier",
    "subject": "A Signature design for a courier that flies parcels over the last few kilometres.",
    "description": "The Sky Courier is a Signature design-study: A Signature design for a courier that flies parcels over the last few kilometres. The Sky Courier is a Signature-made design: a drone courier that flies parcels in straight lines over the last few kilometres. Its novelty is a weather gate that holds the drone when the wind is too strong, so no parcel is risked to the sky. The Courier is meant for medicine and urgent parts where minutes matter. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own ",
    "label": "autonomous-logistics-control-center-signature-000021",
    "figures": {
      "robots": 11,
      "deliveries": 250,
      "flight_min": 6,
      "range_km": 12,
      "payload_kg": 2,
      "success_pct": 93
    }
  },
  {
    "title": "The Pavement Carrier",
    "subject": "A Signature design for a carrier that rolls along pavements at walking speed.",
    "description": "The Pavement Carrier is a Signature design-study: A Signature design for a carrier that rolls along pavements at walking speed. The Pavement Carrier is a Signature-made design: a small six-wheeled carrier that rolls along pavements with food and parcels. Its novelty is a kerb sense that stops the carrier before a kerb it cannot climb, instead of after. The Carrier is meant for campuses and neighbourhoods where a van is wasteful. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: wh",
    "label": "autonomous-logistics-control-center-signature-000022",
    "figures": {
      "robots": 22,
      "deliveries": 500,
      "speed_kmh": 6,
      "range_km": 4,
      "trips": 500,
      "success_pct": 94
    }
  },
  {
    "title": "The Three-Mode Box",
    "subject": "A Signature design for a box that travels by ship, train and truck unopened.",
    "description": "The Three-Mode Box is a Signature design-study: A Signature design for a box that travels by ship, train and truck unopened. The Three-Mode Box is a Signature-made design: a container plan where one box travels by ship, train and truck without ever being opened. Its novelty is a handover clock that counts the minutes at every change of vehicle, so a slow handover is visible at once. The Box is meant for long journeys where the vehicle changes but the cargo must not. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The",
    "label": "autonomous-logistics-control-center-signature-000023",
    "figures": {
      "robots": 0,
      "containers": 2500,
      "handovers": 7500,
      "modes": 3,
      "wait_h": 4,
      "success_pct": 94
    }
  },
  {
    "title": "The Bending Chain",
    "subject": "A Signature design for a chain that bends in a crisis instead of breaking.",
    "description": "The Bending Chain is a Signature design-study: A Signature design for a chain that bends in a crisis instead of breaking. The Bending Chain is a Signature-made design: a supply chain that keeps delivering when a supplier fails or a port closes. Its novelty is a stress-test bell that rings for the weakest link, so the chain is fixed where it is fragile, not where it is loud. The Chain is meant for a world where the next crisis is always coming. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on it",
    "label": "autonomous-logistics-control-center-signature-000024",
    "figures": {
      "robots": 0,
      "suppliers": 125,
      "routes": 62,
      "simulations": 190,
      "worst_delivery_pct": 83,
      "success_pct": 93
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
    "name": "Automated guided vehicle (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Automated_guided_vehicle",
    "retrieved": "2026-11-18"
  },
  {
    "name": "Supply chain (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Supply_chain",
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
