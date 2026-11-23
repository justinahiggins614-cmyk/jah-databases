// Seeded boundless generator for the Swarm Robotics Laboratory Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-swarm-robotics-laboratory.js [seed]  (prints one JSON record)
// or: node gen-swarm-robotics-laboratory.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "swarm-robotics-laboratory";
const RECORD_KIND = "swarm-robotics laboratory record";
const ID_PREFIX = "JAH-SWRB-";
const AI_NAME = "JAH Swarm Robotics Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Ant Colony Optimisation for Robot Swarms",
    "subject": "How ant trail-laying solves routing and search problems for robot teams.",
    "description": "Ant Colony Optimisation for Robot Swarms is a public record about How ant trail-laying solves routing and search problems for robot teams. Ant colony optimisation copies how ants find food: ants lay a scent trail, called pheromone, on their way home, and other ants follow the strongest scent, so the shortest path gets the most traffic and the strongest trail. Marco Dorigo introduced ant colony optimisation in 1992, and it is now a standard method for routing, scheduling and network design. In robot swarms, virtual pheromone is a number stored in a shared map or dropped as a digital marker, and",
    "label": "swarm-robotics-laboratory-000001",
    "figures": {
      "robots": 30,
      "paths": 120,
      "pheromone": 86,
      "rounds": 25,
      "best_path_m": 42,
      "success_pct": 95
    }
  },
  {
    "title": "Particle Swarm Optimisation for Robot Swarms",
    "subject": "How flocks of simple searchers find the best spot by copying their neighbours.",
    "description": "Particle Swarm Optimisation for Robot Swarms is a public record about How flocks of simple searchers find the best spot by copying their neighbours. Particle swarm optimisation copies how birds search for food: each searcher remembers its own best spot and watches the swarm's best spot, then steers between the two. Kennedy and Eberhart introduced particle swarm optimisation in 1995, and it is used to tune robot controllers, plan paths and place sensors. Each particle is just a candidate answer with a position and a velocity, so the method needs no gradients and works on rough, jagged problems.",
    "label": "swarm-robotics-laboratory-000002",
    "figures": {
      "robots": 40,
      "particles": 40,
      "rounds": 30,
      "best_score": 97,
      "search_area": 400,
      "success_pct": 94
    }
  },
  {
    "title": "Artificial Bee Colony Search for Robot Swarms",
    "subject": "How honeybee foraging finds good answers with employed, onlooker and scout bees.",
    "description": "Artificial Bee Colony Search for Robot Swarms is a public record about How honeybee foraging finds good answers with employed, onlooker and scout bees. The artificial bee colony algorithm copies honeybee foraging: employed bees work known food sources, onlooker bees choose among those sources by watching dances, and scout bees search for new sources. Karaboga introduced the artificial bee colony algorithm in 2005, and it is used for tuning, clustering and robot path planning. A food source that stops improving is abandoned, and its employed bee becomes a scout, so the swarm never gets stuck on",
    "label": "swarm-robotics-laboratory-000003",
    "figures": {
      "robots": 36,
      "sources": 24,
      "scouts": 6,
      "rounds": 40,
      "best_richness": 91,
      "success_pct": 93
    }
  },
  {
    "title": "The Kilobot Swarm Platform",
    "subject": "A thousand tiny cheap robots built for swarm experiments in the lab.",
    "description": "The Kilobot Swarm Platform is a public record about A thousand tiny cheap robots built for swarm experiments in the lab. The Kilobot is a small cheap robot built at Harvard for swarm research: it has three legs, vibrates to move, and talks to neighbours with infrared light, so a lab can afford hundreds of them. Kilobots cost a few tens of dollars each, which matters because swarm experiments need large numbers, and a thousand Kilobots can be run on one laboratory table. Each Kilobot is simple on purpose: it has no camera and no map, so any clever group behaviour must come from the swarm rules,",
    "label": "swarm-robotics-laboratory-000004",
    "figures": {
      "robots": 100,
      "cost_usd": 14,
      "table_m2": 2,
      "shape_robots": 92,
      "form_min": 9,
      "success_pct": 96
    }
  },
  {
    "title": "The e-puck Mobile Robot",
    "subject": "A small two-wheeled laboratory robot used to test swarm rules.",
    "description": "The e-puck Mobile Robot is a public record about A small two-wheeled laboratory robot used to test swarm rules. The e-puck is a small two-wheeled robot built for education and research, about the size of a hockey puck, with sensors for light, sound, distance and ground colour. It was developed at the Swiss Federal Institute of Technology in Lausanne, and it is a standard test robot for swarm and evolutionary robotics experiments. The e-puck carries a camera, a microphone array and eight infrared distance sensors, so it can see obstacles, hear sounds and follow lines on the floor. Because every",
    "label": "swarm-robotics-laboratory-000005",
    "figures": {
      "robots": 12,
      "sensors": 8,
      "arena_m2": 4,
      "runs": 20,
      "speed_cms": 13,
      "success_pct": 95
    }
  },
  {
    "title": "Stigmergy in Robot Swarms",
    "subject": "Coordination through marks left in the environment instead of direct messages.",
    "description": "Stigmergy in Robot Swarms is a public record about Coordination through marks left in the environment instead of direct messages. Stigmergy is coordination through the environment: one agent changes the world, and another agent reacts to that change, so no direct message is ever sent. The term was coined by Pierre-Paul Grasse in 1959 to explain termite building, where a termite adds mud where other termites have already added mud, and a mound grows without any termite holding a plan. Robot swarms use digital stigmergy: robots leave markers in a shared map or drop physical tokens, and other rob",
    "label": "swarm-robotics-laboratory-000006",
    "figures": {
      "robots": 25,
      "markers": 300,
      "fade_min": 5,
      "structures": 3,
      "rounds": 30,
      "success_pct": 94
    }
  },
  {
    "title": "Self-Assembly in Robot Swarms",
    "subject": "Small robots joining together into larger shapes and machines.",
    "description": "Self-Assembly in Robot Swarms is a public record about Small robots joining together into larger shapes and machines. Self-assembly is when small parts join into a larger structure without outside help, and robot swarms do it by docking together into chains, bridges and rafts. The classic demonstration is the s-bot, a robot that can grip its neighbours and form chains to pull loads and bridges to cross gaps. Self-assembling swarms are useful where one big robot cannot go: a chain of small robots can cross a ditch, and a raft of robots can float across water. The hard part is deciding when to j",
    "label": "swarm-robotics-laboratory-000007",
    "figures": {
      "robots": 18,
      "docks": 24,
      "bridge_m": 2,
      "gaps_crossed": 6,
      "split_s": 30,
      "success_pct": 92
    }
  },
  {
    "title": "Self-Organisation in Robot Swarms",
    "subject": "Order that appears from local rules with no central plan.",
    "description": "Self-Organisation in Robot Swarms is a public record about Order that appears from local rules with no central plan. Self-organisation is order that appears without a leader: each robot follows simple local rules, and the group as a whole shows patterns no single robot planned. Examples include synchronised flashing, where fireflies and robots blink together, and lane formation, where crowds sort themselves into walking lanes without signs. The key ingredients are local interaction, feedback and randomness: robots react to neighbours, good patterns get reinforced, and small random changes keep",
    "label": "swarm-robotics-laboratory-000008",
    "figures": {
      "robots": 40,
      "rules": 3,
      "form_min": 4,
      "recovery_s": 45,
      "patterns": 5,
      "success_pct": 95
    }
  },
  {
    "title": "Morphogenesis in Robot Swarms",
    "subject": "Growing robot shapes the way embryos grow body shapes.",
    "description": "Morphogenesis in Robot Swarms is a public record about Growing robot shapes the way embryos grow body shapes. Morphogenesis is how embryos grow shapes, and robot swarms borrow the idea: robots act like cells, following chemical-like signals to grow into a chosen shape. In swarm morphogenesis, a gradient signal spreads from a seed robot, and each robot reads the signal strength to decide where it belongs in the shape. The approach can grow shapes that repair themselves: if a robot fails, its neighbours sense the gap in the signal and move in to fill it. Morphogenesis research connects robotics ",
    "label": "swarm-robotics-laboratory-000009",
    "figures": {
      "robots": 50,
      "layers": 5,
      "shape_error_cm": 4,
      "repair_s": 60,
      "gradients": 3,
      "success_pct": 93
    }
  },
  {
    "title": "Pheromone Communication in Robot Swarms",
    "subject": "Scent-like signals that robots leave, follow and let fade.",
    "description": "Pheromone Communication in Robot Swarms is a public record about Scent-like signals that robots leave, follow and let fade. Pheromones are chemical scents that ants and bees use to mark trails, warn of danger and call for help, and robot swarms copy them with digital or physical markers. A robot pheromone has three properties: it is laid where something matters, it is followed in proportion to its strength, and it fades, so the swarm always tracks fresh information. Physical pheromone can be a glowing trail, a heat spot or a chemical puff, while digital pheromone is a number in a shared map. P",
    "label": "swarm-robotics-laboratory-000010",
    "figures": {
      "robots": 30,
      "trails": 8,
      "fade_s": 60,
      "followers": 22,
      "markers": 180,
      "success_pct": 94
    }
  },
  {
    "title": "Termite-Inspired Construction by Robot Swarms",
    "subject": "Building mounds and walls the way termites do, one pellet at a time.",
    "description": "Termite-Inspired Construction by Robot Swarms is a public record about Building mounds and walls the way termites do, one pellet at a time. Termites build mounds taller than a person by each carrying small pellets of mud and placing them where other termites have already built, with no architect and no blueprint. Harvard's TERMES project copied this with robots that carry foam bricks and place them by simple rules, building walls, stairs and castles without a central plan. The robots climb the structure they are building, so the building grows one layer at a time and the robots always work on ",
    "label": "swarm-robotics-laboratory-000011",
    "figures": {
      "robots": 12,
      "bricks": 400,
      "height_m": 2,
      "layers": 20,
      "build_min": 55,
      "success_pct": 92
    }
  },
  {
    "title": "Slime Mould Computing with Robot Swarms",
    "subject": "Solving mazes and networks the way a slime mould grows.",
    "description": "Slime Mould Computing with Robot Swarms is a public record about Solving mazes and networks the way a slime mould grows. Slime moulds are single cells that grow into networks of tubes, and they solve mazes by growing toward food and shrinking tubes that lead nowhere, which finds short paths without any brain. Researchers have used slime moulds to redesign road and rail networks, including a famous model of the Tokyo rail system that matched the real network's efficiency. Robot swarms copy the trick with growing and shrinking digital tubes: paths that carry traffic get reinforced, and paths tha",
    "label": "swarm-robotics-laboratory-000012",
    "figures": {
      "robots": 20,
      "paths": 60,
      "food_sources": 5,
      "prune_rounds": 12,
      "length_m": 38,
      "success_pct": 93
    }
  },
  {
    "title": "Firefly Synchronisation in Robot Swarms",
    "subject": "Robots blinking in unison the way fireflies flash together.",
    "description": "Firefly Synchronisation in Robot Swarms is a public record about Robots blinking in unison the way fireflies flash together. Fireflies in Southeast Asia flash in unison, thousands of them blinking at the same moment, and the mathematics of that synchrony also drives robot swarms. The model is simple: each firefly has an internal clock, and when it sees a neighbour flash, it nudges its own clock a little earlier, so the clocks drift together over time. Robot swarms use synchronised blinking to share timing without radio messages: a shared flash can mark the start of a task or the beat for a coo",
    "label": "swarm-robotics-laboratory-000013",
    "figures": {
      "robots": 45,
      "flashes": 90,
      "sync_s": 25,
      "error_ms": 40,
      "beats": 12,
      "success_pct": 96
    }
  },
  {
    "title": "Fish Schooling Models for Robot Swarms",
    "subject": "How fish schools stay together, dodge predators and save energy.",
    "description": "Fish Schooling Models for Robot Swarms is a public record about How fish schools stay together, dodge predators and save energy. Fish schools move as one body: each fish watches its neighbours and matches their speed and direction, which lets the school turn as a whole and confuse predators. Schooling saves energy because fish in the middle ride the water pushed by the fish ahead, and robot swarms copy this by drafting behind neighbours. The classic model uses three zones: a near zone for avoiding collisions, a middle zone for matching speed, and a far zone for staying with the group. Underwat",
    "label": "swarm-robotics-laboratory-000014",
    "figures": {
      "robots": 24,
      "zones": 3,
      "cohesion_pct": 91,
      "survey_m2": 1200,
      "energy_saved_pct": 18,
      "success_pct": 94
    }
  },
  {
    "title": "Bird Flocking Models for Robot Swarms",
    "subject": "How starling murmurations steer drone swarms.",
    "description": "Bird Flocking Models for Robot Swarms is a public record about How starling murmurations steer drone swarms. Starling murmurations are flocks of thousands of birds that swirl and fold in the sky, and each bird only watches about seven neighbours, yet the whole flock turns as one. The seven-neighbour rule was measured by researchers in Rome, and it explains how a flock can be both huge and fast to react: information spreads neighbour to neighbour in waves. Drone swarms copy the rule to fly in large formations that can dodge obstacles and reform, since each drone only needs to track a handful of",
    "label": "swarm-robotics-laboratory-000015",
    "figures": {
      "robots": 60,
      "neighbours": 7,
      "turn_deg_s": 45,
      "flock_m": 30,
      "splits": 1,
      "success_pct": 93
    }
  },
  {
    "title": "Swarm Simulation with ARGoS",
    "subject": "Simulating thousands of swarm robots faster than real time.",
    "description": "Swarm Simulation with ARGoS is a public record about Simulating thousands of swarm robots faster than real time. ARGoS is a simulator built for swarm robotics that can run thousands of robots at once by giving each robot a simple physics model and a fast update loop. It was built at the Universite Libre de Bruxelles, and it is used to test swarm rules on thousands of robots before buying or building any hardware. ARGoS runs faster than real time on a normal computer, so a researcher can test hundreds of rule variations in an afternoon. Simulators like ARGoS are the laboratory bench of swarm ro",
    "label": "swarm-robotics-laboratory-000016",
    "figures": {
      "robots": 1000,
      "steps": 5000,
      "sim_speed": 8,
      "rules_tested": 40,
      "arena_m2": 100,
      "success_pct": 95
    }
  },
  {
    "title": "Swarm Robotics Overview",
    "subject": "The whole field in one record: many simple robots, one shared result.",
    "description": "Swarm Robotics Overview is a public record about The whole field in one record: many simple robots, one shared result. Swarm robotics studies large groups of robots that cooperate through local rules, without a central controller, copying ants, bees, birds and fish. The field promises systems that are robust, because losing one robot changes little; scalable, because adding robots needs no new plan; and flexible, because the same robots can do many jobs. Swarm robots are used in research labs, and the ideas are moving into warehouses, farms and disaster response, where many cheap robots beat o",
    "label": "swarm-robotics-laboratory-000017",
    "figures": {
      "robots": 100,
      "rules": 24,
      "lab_runs": 60,
      "robustness_pct": 88,
      "scales": 4,
      "success_pct": 95
    }
  },
  {
    "title": "Robot Swarm Testbeds",
    "subject": "Laboratory arenas built to test swarms safely and repeatably.",
    "description": "Robot Swarm Testbeds is a public record about Laboratory arenas built to test swarms safely and repeatably. A swarm testbed is a laboratory arena with an overhead camera, a charging system and a way to reset the robots, so experiments can be repeated exactly. Testbeds range from tabletop Kilobots arenas to warehouse-sized halls with dozens of larger robots and motion-capture cameras. A good testbed records everything: every robot's position, every message and every failure, so a surprising result can be replayed and explained. Shared testbeds let different labs compare results fairly, since th",
    "label": "swarm-robotics-laboratory-000018",
    "figures": {
      "robots": 50,
      "cameras": 4,
      "runs": 30,
      "arena_m2": 25,
      "resets": 30,
      "success_pct": 96
    }
  },
  {
    "title": "Distributed Sensing by Robot Swarms",
    "subject": "Many robots sensing together to build one picture of the world.",
    "description": "Distributed Sensing by Robot Swarms is a public record about Many robots sensing together to build one picture of the world. Distributed sensing means many robots each sense a small part of the world, and their readings are combined into one picture that no single robot could see. A swarm can measure temperature, gas, sound or radio strength across a whole building by spreading out and sharing readings on a map. The challenge is fusion: readings arrive at different times and from different places, so the swarm must weight fresh, nearby readings more than old, distant ones. Distributed sensing ",
    "label": "swarm-robotics-laboratory-000019",
    "figures": {
      "robots": 32,
      "readings": 960,
      "area_m2": 800,
      "hot_spots": 5,
      "error_pct": 6,
      "success_pct": 94
    }
  },
  {
    "title": "Swarm Foraging by Robot Swarms",
    "subject": "Collecting scattered items and bringing them home as a team.",
    "description": "Swarm Foraging by Robot Swarms is a public record about Collecting scattered items and bringing them home as a team. Foraging is the swarm task of finding scattered items and carrying them to a nest, and it is the standard test for search, transport and teamwork. Ants forage by laying trails to food, and robot swarms copy this: a robot that finds an item lays a trail, and others follow it to collect the rest. The hard part is balance: too many robots on one trail wastes effort, while too few leaves items behind, so good foraging rules spread robots across trails by trail strength. Foraging tes",
    "label": "swarm-robotics-laboratory-000020",
    "figures": {
      "robots": 28,
      "items": 120,
      "collected": 108,
      "trails": 6,
      "forage_min": 30,
      "success_pct": 95
    }
  },
  {
    "title": "Swarm Aggregation by Robot Swarms",
    "subject": "Gathering scattered robots into one cluster on command.",
    "description": "Swarm Aggregation by Robot Swarms is a public record about Gathering scattered robots into one cluster on command. Aggregation is the swarm task of gathering scattered robots into one cluster, and it is the first step for many jobs, from building a structure to charging together. The simplest rule is to move toward the average position of neighbours, which pulls the swarm into a ball, though it can be slow when the swarm starts far apart. Better rules use a beacon: one robot or a light marks the meeting point, and the others steer toward it, which gathers the swarm faster and more reliably. Ag",
    "label": "swarm-robotics-laboratory-000021",
    "figures": {
      "robots": 36,
      "beacons": 1,
      "gather_s": 48,
      "radius_m": 2,
      "clusters": 1,
      "success_pct": 96
    }
  },
  {
    "title": "Swarm Dispersion by Robot Swarms",
    "subject": "Spreading robots evenly across an area to watch or sense it.",
    "description": "Swarm Dispersion by Robot Swarms is a public record about Spreading robots evenly across an area to watch or sense it. Dispersion is the opposite of aggregation: scattered robots spread out evenly, so each one watches its own patch and the swarm covers the whole area. The rule is simple: move away from your nearest neighbour until every robot has roughly the same distance to its neighbours, which is the same mathematics as spreading electrons on a sphere. Dispersion is used for sensor coverage, where a swarm must watch a field, and for search, where a swarm must not waste two robots on the sam",
    "label": "swarm-robotics-laboratory-000022",
    "figures": {
      "robots": 30,
      "gaps_m": 3,
      "coverage_pct": 92,
      "area_m2": 600,
      "spacing_m": 4,
      "success_pct": 94
    }
  },
  {
    "title": "Swarm Pattern Formation by Robot Swarms",
    "subject": "Robots arranging themselves into letters, shapes and grids.",
    "description": "Swarm Pattern Formation by Robot Swarms is a public record about Robots arranging themselves into letters, shapes and grids. Pattern formation is the swarm task of arranging robots into a chosen shape, such as a letter, a circle or a grid, using only local rules. One method gives each robot a target spot in the shape and lets robots sort themselves out, while another grows the shape from a seed, with robots joining the edge where they fit. Pattern formation is a benchmark for swarm control, because the shape shows at a glance whether the rules worked, and the error is easy to measure. Drone li",
    "label": "swarm-robotics-laboratory-000023",
    "figures": {
      "robots": 48,
      "shape_spots": 48,
      "error_cm": 9,
      "form_min": 6,
      "shapes": 4,
      "success_pct": 95
    }
  },
  {
    "title": "Swarm Fault Tolerance by Robot Swarms",
    "subject": "Swarms that keep working when individual robots fail.",
    "description": "Swarm Fault Tolerance by Robot Swarms is a public record about Swarms that keep working when individual robots fail. Swarm fault tolerance comes from numbers: in a swarm of a hundred robots, losing five changes the result only a little, while losing one robot from a team of two stops the mission. Swarms detect failures by watching neighbours: a robot that stops moving or stops signalling is routed around, and its work is picked up by others. The design rule is graceful degradation: the swarm should do slightly worse with each failure, never collapse suddenly, so operators can trust it in the f",
    "label": "swarm-robotics-laboratory-000024",
    "figures": {
      "robots": 80,
      "failures": 8,
      "score_before": 92,
      "score_after": 86,
      "recover_s": 20,
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
    src: "public-harvest",
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
