// Seeded boundless generator for the Multi-Robot Coordination Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-multi-robot-coordination.js [seed]  (prints one JSON record)
// or: node gen-multi-robot-coordination.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "multi-robot-coordination";
const RECORD_KIND = "multi-robot coordination record";
const ID_PREFIX = "JAH-MRCP-";
const AI_NAME = "JAH Multi-Robot Coordination Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Auction-Based Task Allocation for Robot Teams",
    "subject": "Market bidding that assigns each job to the robot that can do it cheapest.",
    "description": "Auction-Based Task Allocation for Robot Teams is a public record about Market bidding that assigns each job to the robot that can do it cheapest. In market-based allocation each robot bids a cost for each task, and the task goes to the lowest bidder, so the team splits work without a central planner dictating every move. The Contract Net Protocol, published by Reid Smith in 1980, is the classic form: a manager announces a task, contractors bid, and the manager awards the contract to the best bid. Auctions run in rounds, so when a new task appears or a robot fails, the team re-auctions the affe",
    "label": "multi-robot-coordination-000001",
    "figures": {
      "robots": 12,
      "tasks": 48,
      "bids": 576,
      "rounds": 6,
      "range_m": 50,
      "success_pct": 96
    }
  },
  {
    "title": "Consensus Algorithms for Robot Teams",
    "subject": "Agreement rules that let robots settle on one shared value without a leader.",
    "description": "Consensus Algorithms for Robot Teams is a public record about Agreement rules that let robots settle on one shared value without a leader. A consensus algorithm lets every robot in a team converge on the same number, such as a meeting point or a shared map coordinate, by repeatedly averaging what its neighbours believe. The classic result is that a connected communication graph is enough: if every robot can eventually hear from every other robot through some chain of neighbours, the team agrees. Consensus runs in rounds, and each round shrinks the disagreement, so after enough rounds all robot",
    "label": "multi-robot-coordination-000002",
    "figures": {
      "robots": 10,
      "rounds": 8,
      "messages": 320,
      "tolerance": 2,
      "range_m": 40,
      "success_pct": 98
    }
  },
  {
    "title": "Formation Control for Mobile Robot Teams",
    "subject": "Rules that hold a team of robots in a chosen shape while it moves.",
    "description": "Formation Control for Mobile Robot Teams is a public record about Rules that hold a team of robots in a chosen shape while it moves. Formation control keeps robots in a chosen shape, such as a line, a wedge or a grid, while the whole shape moves toward a goal, so the team can sweep an area or carry a load together. In leader-follower formation, one robot leads and the others hold fixed offsets from it; in virtual-structure formation, the robots hold offsets from a moving imaginary shape instead. Behaviour-based formation gives each robot simple rules, such as stay near your neighbour and avoid",
    "label": "multi-robot-coordination-000003",
    "figures": {
      "robots": 16,
      "spacing_m": 3,
      "shape_error_cm": 12,
      "speed_ms": 2,
      "waypoints": 24,
      "success_pct": 97
    }
  },
  {
    "title": "Coverage and Patrolling by Robot Teams",
    "subject": "Sweeping a whole area so no part is left unvisited or unwatched.",
    "description": "Coverage and Patrolling by Robot Teams is a public record about Sweeping a whole area so no part is left unvisited or unwatched. Coverage means visiting every part of an area, and patrolling means visiting it again and again, so robot teams use both to search fields, inspect warehouses and watch borders. A common method splits the area into cells, gives each robot a set of cells, and lets each robot sweep its cells in a back-and-forth lawnmower pattern. When the area is unknown, robots build a map as they go and mark cells visited, so the team can prove nothing was skipped once every cell is m",
    "label": "multi-robot-coordination-000004",
    "figures": {
      "robots": 8,
      "cells": 400,
      "area_m2": 2000,
      "sweep_min": 45,
      "max_wait_min": 9,
      "success_pct": 95
    }
  },
  {
    "title": "Flocking Rules for Robot Teams",
    "subject": "Three simple steering rules that turn a crowd of robots into a flock.",
    "description": "Flocking Rules for Robot Teams is a public record about Three simple steering rules that turn a crowd of robots into a flock. Craig Reynolds described flocking in 1987 with three rules: separation, steer away from neighbours that are too close; alignment, steer toward the average heading of neighbours; and cohesion, steer toward the average position of neighbours. Boids is the name of Reynolds' simulation, and the same three rules steer robot teams, drone shows and animated crowds today. Each robot only watches its nearby neighbours, so the flock needs no leader and no central map, yet the who",
    "label": "multi-robot-coordination-000005",
    "figures": {
      "robots": 20,
      "radius_m": 5,
      "speed_ms": 3,
      "neighbours": 6,
      "steps": 120,
      "success_pct": 94
    }
  },
  {
    "title": "Velocity Obstacles for Collision Avoidance",
    "subject": "Geometry that tells a robot which speeds would cause a crash, so it can pick a safe one.",
    "description": "Velocity Obstacles for Collision Avoidance is a public record about Geometry that tells a robot which speeds would cause a crash, so it can pick a safe one. A velocity obstacle is the set of velocities that would make a robot collide with a moving obstacle, so a robot that picks a velocity outside that set stays safe. The method was introduced by Fiorini and Shiller in 1998, and it works by drawing a cone of dangerous velocities from the robot toward each obstacle's future position. Reciprocal velocity obstacles share the avoiding work between two moving robots, so each one only changes its ve",
    "label": "multi-robot-coordination-000006",
    "figures": {
      "robots": 14,
      "obstacles": 22,
      "checks_per_s": 10,
      "min_gap_m": 2,
      "speed_ms": 2,
      "success_pct": 99
    }
  },
  {
    "title": "Distributed Mapping by Robot Teams",
    "subject": "Many robots building one shared map at the same time.",
    "description": "Distributed Mapping by Robot Teams is a public record about Many robots building one shared map at the same time. Simultaneous localization and mapping, called SLAM, means a robot builds a map of an unknown place while working out where it is inside that map, and a team does it together by sharing pieces. In distributed SLAM each robot maps its own area, then the robots exchange map pieces and stitch them into one shared map using landmarks both robots have seen. The hard part is recognising the same landmark from two robots' different viewpoints, which is called loop closure, and a wrong matc",
    "label": "multi-robot-coordination-000007",
    "figures": {
      "robots": 6,
      "landmarks": 180,
      "map_cells": 9000,
      "loop_closures": 14,
      "error_cm": 8,
      "success_pct": 96
    }
  },
  {
    "title": "Communication Graphs for Robot Teams",
    "subject": "The radio links between robots, treated as a graph that must stay connected.",
    "description": "Communication Graphs for Robot Teams is a public record about The radio links between robots, treated as a graph that must stay connected. A communication graph treats each robot as a dot and each radio link as a line, so the team's ability to share information becomes a question about the shape of the graph. The graph is connected when there is a path of links between every pair of robots, and most coordination methods fail if the graph splits into separate pieces. Algebraic connectivity is a single number that measures how well connected the graph is, and robot teams steer to keep it above a",
    "label": "multi-robot-coordination-000008",
    "figures": {
      "robots": 12,
      "links": 34,
      "connectivity": 3,
      "range_m": 60,
      "hops": 4,
      "success_pct": 97
    }
  },
  {
    "title": "Role Assignment in Robot Teams",
    "subject": "Deciding which robot plays which part in the team's plan.",
    "description": "Role Assignment in Robot Teams is a public record about Deciding which robot plays which part in the team's plan. Role assignment gives each robot a job, such as scout, carrier, guard or builder, so the team covers every needed job with the best-suited robot. A role has requirements, such as speed for a scout or lifting strength for a carrier, and the assignment matches robots to roles by scoring each robot against each role. Good assignments change during a mission: a carrier that finishes its load can become a scout, and a robot low on battery hands its role to a fresh robot. Role assignment",
    "label": "multi-robot-coordination-000009",
    "figures": {
      "robots": 11,
      "roles": 5,
      "scores": 55,
      "reassignments": 3,
      "battery_pct": 72,
      "success_pct": 95
    }
  },
  {
    "title": "Grid Path Planning for Robot Teams",
    "subject": "Finding the shortest route across a grid, one robot at a time.",
    "description": "Grid Path Planning for Robot Teams is a public record about Finding the shortest route across a grid, one robot at a time. A-star search, written A*, finds the shortest path across a grid by scoring each step with the distance travelled so far plus a straight-line guess of the distance left. A* was published by Hart, Nilsson and Raphael in 1968, and it is still the standard planner for grid maps because it is fast and its result is provably the shortest path. Robot teams plan one robot at a time and then fix conflicts: when two planned paths cross at the same time, the lower-priority robot wai",
    "label": "multi-robot-coordination-000010",
    "figures": {
      "robots": 10,
      "grid_cells": 2500,
      "path_m": 86,
      "waits": 7,
      "plan_ms": 42,
      "success_pct": 98
    }
  },
  {
    "title": "Sampling-Based Motion Planning for Robot Teams",
    "subject": "Growing random trees through free space until a path appears.",
    "description": "Sampling-Based Motion Planning for Robot Teams is a public record about Growing random trees through free space until a path appears. Rapidly-exploring random trees, called RRT, grow a tree of random samples through free space, so the tree explores quickly and finds a path even in cluttered rooms. RRT was introduced by LaValle and Kuffner in 1998, and RRT* improves it by rewiring the tree to shorten the path as more samples arrive. Robot teams grow one tree per robot and then check the trees against each other, so two robots never plan to occupy the same place at the same time. Sampling planne",
    "label": "multi-robot-coordination-000011",
    "figures": {
      "robots": 8,
      "samples": 4000,
      "tree_nodes": 3200,
      "path_m": 64,
      "plan_ms": 180,
      "success_pct": 93
    }
  },
  {
    "title": "The Robot Operating System 2 for Robot Teams",
    "subject": "The shared software layer that lets robots talk, share sensors and run the same code.",
    "description": "The Robot Operating System 2 for Robot Teams is a public record about The shared software layer that lets robots talk, share sensors and run the same code. The Robot Operating System, called ROS, is a set of software libraries and tools that help build robot programs, and ROS 2 is the newer version built for teams of robots and real-time control. ROS 2 uses the Data Distribution Service, called DDS, as its messaging layer, so robots discover each other on a network and exchange messages without a central server. A ROS 2 program is built from nodes, small programs that publish messages on named",
    "label": "multi-robot-coordination-000012",
    "figures": {
      "robots": 9,
      "nodes": 45,
      "topics": 18,
      "messages_per_s": 240,
      "latency_ms": 8,
      "success_pct": 97
    }
  },
  {
    "title": "Behaviour Trees for Robot Teams",
    "subject": "Tree-shaped plans that switch a robot between jobs as conditions change.",
    "description": "Behaviour Trees for Robot Teams is a public record about Tree-shaped plans that switch a robot between jobs as conditions change. A behaviour tree is a plan shaped like a tree: the leaves are actions such as drive or grasp, and the branches decide which action runs next based on what the robot senses. Behaviour trees tick from the root many times a second, so a robot can abandon a failing action and try another one immediately, which makes them tougher than fixed step-by-step scripts. Sequence branches run their children in order until one fails, while fallback branches try children in order u",
    "label": "multi-robot-coordination-000013",
    "figures": {
      "robots": 7,
      "tree_nodes": 36,
      "ticks_per_s": 10,
      "actions": 12,
      "fallbacks": 4,
      "success_pct": 96
    }
  },
  {
    "title": "Map Merging for Robot Teams",
    "subject": "Stitching the maps of several robots into one shared map.",
    "description": "Map Merging for Robot Teams is a public record about Stitching the maps of several robots into one shared map. Map merging takes the separate maps built by several robots and joins them into one map, so the team can plan on shared ground instead of each robot trusting only its own map. The merge searches for overlapping landmarks or shapes in two maps, then computes the rotation and shift that lines them up, which is the same geometry used to stitch photographs into a panorama. A wrong overlap can fold two different corridors into one, so merges are checked by how well the overlapped landmarks",
    "label": "multi-robot-coordination-000014",
    "figures": {
      "robots": 5,
      "maps": 5,
      "landmarks": 140,
      "overlap_pct": 38,
      "align_error_cm": 6,
      "success_pct": 95
    }
  },
  {
    "title": "Fault Tolerance in Robot Teams",
    "subject": "Keeping the mission going when a robot breaks, stalls or loses radio contact.",
    "description": "Fault Tolerance in Robot Teams is a public record about Keeping the mission going when a robot breaks, stalls or loses radio contact. Fault tolerance means the team still finishes its mission when a robot fails, by noticing the failure, reassigning its work and carrying on with the robots that remain. Robots watch each other with heartbeats, short messages sent on a schedule, and a robot that misses several heartbeats in a row is treated as failed. Redundancy is the price of tolerance: a team that needs four robots to do a job carries five or six, so one failure never leaves a job uncovered. G",
    "label": "multi-robot-coordination-000015",
    "figures": {
      "robots": 12,
      "heartbeats": 360,
      "failures": 2,
      "recovered_tasks": 9,
      "spare_robots": 2,
      "success_pct": 94
    }
  },
  {
    "title": "Heterogeneous Robot Teams",
    "subject": "Teams that mix different kinds of robots, each doing what it does best.",
    "description": "Heterogeneous Robot Teams is a public record about Teams that mix different kinds of robots, each doing what it does best. A heterogeneous team mixes different robot types, such as flying drones that scout from above, wheeled robots that carry loads, and legged robots that climb stairs, so each job goes to the type built for it. The hard part is a shared language: a drone measures the world in the air while a wheeled robot measures it on the floor, so the team needs one shared map and one shared task list. Heterogeneous teams are stronger than uniform teams for mixed missions, such as disaster",
    "label": "multi-robot-coordination-000016",
    "figures": {
      "robots": 15,
      "types": 3,
      "tasks": 60,
      "drones": 5,
      "carriers": 7,
      "success_pct": 96
    }
  },
  {
    "title": "Human-Swarm Interaction",
    "subject": "How one person guides, watches and trusts a whole swarm of robots.",
    "description": "Human-Swarm Interaction is a public record about How one person guides, watches and trusts a whole swarm of robots. Human-swarm interaction studies how a single operator guides many robots at once, since a person cannot steer fifty robots one by one. Operators usually command the swarm as a whole, by drawing an area to search or pointing at a goal, and the swarm's own rules turn that command into fifty individual movements. Good interfaces show the swarm as one shape with a health summary, rather than fifty separate dots, so the operator can see at a glance whether the swarm is working. Trust ",
    "label": "multi-robot-coordination-000017",
    "figures": {
      "robots": 50,
      "operators": 1,
      "commands": 8,
      "interventions": 3,
      "screen_items": 6,
      "success_pct": 93
    }
  },
  {
    "title": "Warehouse Robot Fleets",
    "subject": "Hundreds of small robots carrying shelves to pickers in a warehouse.",
    "description": "Warehouse Robot Fleets is a public record about Hundreds of small robots carrying shelves to pickers in a warehouse. Warehouse robot fleets carry shelves to stationary human pickers, so the picker never walks the aisles and the robots do all the travelling. Amazon Robotics, formerly Kiva Systems, made the model famous: small orange robots slide under shelves, lift them and carry them to picking stations, then return them to storage. A fleet manager assigns shelves to robots, plans paths on the warehouse grid and keeps robots from blocking each other in narrow aisles. Fleets scale by adding rob",
    "label": "multi-robot-coordination-000018",
    "figures": {
      "robots": 120,
      "shelves": 2400,
      "orders_per_h": 320,
      "aisles": 24,
      "stations": 16,
      "success_pct": 98
    }
  },
  {
    "title": "Search-and-Rescue Robot Teams",
    "subject": "Robot teams that search collapsed buildings and disaster zones for survivors.",
    "description": "Search-and-Rescue Robot Teams is a public record about Robot teams that search collapsed buildings and disaster zones for survivors. Search-and-rescue robot teams enter places too dangerous for people, such as collapsed buildings, and search for survivors with cameras, microphones and heat sensors. Teams mix ground robots that crawl through rubble, drones that map from above, and snake robots that slide through gaps, sharing one map of the disaster site. Time matters most: the team must cover the whole site quickly and report likely survivor locations, so coverage planning and fast communicati",
    "label": "multi-robot-coordination-000019",
    "figures": {
      "robots": 18,
      "area_m2": 1500,
      "survivor_flags": 6,
      "search_min": 38,
      "sensor_hits": 44,
      "success_pct": 92
    }
  },
  {
    "title": "Agricultural Robot Teams",
    "subject": "Robot teams that plant, tend and harvest crops field by field.",
    "description": "Agricultural Robot Teams is a public record about Robot teams that plant, tend and harvest crops field by field. Agricultural robot teams work fields in groups: some robots scan crops with cameras, others weed precisely, and others harvest, so each plant gets individual attention. Precision weeding robots tell crops from weeds by leaf shape and remove only the weeds, which cuts herbicide use and protects the soil. Teams share a field map with the position of every row, so a scanning robot can mark a sick plant and a treatment robot can drive straight to it later. Field robots must handle mud, ",
    "label": "multi-robot-coordination-000020",
    "figures": {
      "robots": 10,
      "rows": 80,
      "plants": 9600,
      "weeds_removed": 1450,
      "field_ha": 12,
      "success_pct": 95
    }
  },
  {
    "title": "Underwater Vehicle Teams",
    "subject": "Teams of underwater robots mapping the sea floor and inspecting pipes together.",
    "description": "Underwater Vehicle Teams is a public record about Teams of underwater robots mapping the sea floor and inspecting pipes together. Autonomous underwater vehicles, called AUVs, are robots that swim on their own, and teams of them map the sea floor, inspect pipelines and track ocean currents. Radio does not travel underwater, so AUV teams communicate with sound, called acoustic modems, which is slow and short-range, so the robots must plan long stretches without talking. Teams split the sea floor into lanes, each AUV maps its lanes with sonar, which is sound-based imaging, and the lanes are stitc",
    "label": "multi-robot-coordination-000021",
    "figures": {
      "robots": 6,
      "lanes": 24,
      "area_km2": 8,
      "depth_m": 120,
      "sonar_hits": 96,
      "success_pct": 94
    }
  },
  {
    "title": "Aerial Drone Teams",
    "subject": "Drone teams that fly in formation for shows, surveys and inspections.",
    "description": "Aerial Drone Teams is a public record about Drone teams that fly in formation for shows, surveys and inspections. Drone teams fly in formation for light shows, field surveys and bridge inspections, holding precise positions in the sky while a ground station watches them all. Light-show drones carry a bright light and a GPS receiver, and a choreographer program plans every drone's path so the team draws pictures in the sky. Survey drones fly lawnmower patterns over fields and construction sites, taking overlapping photographs that are stitched into maps. Safety rules keep drone teams away from ",
    "label": "multi-robot-coordination-000022",
    "figures": {
      "robots": 40,
      "flights": 120,
      "photos": 2400,
      "area_ha": 30,
      "show_min": 12,
      "success_pct": 97
    }
  },
  {
    "title": "Construction Robot Teams",
    "subject": "Robot teams that carry, place and check building materials on a construction site.",
    "description": "Construction Robot Teams is a public record about Robot teams that carry, place and check building materials on a construction site. Construction robot teams carry materials, place bricks and check measurements on building sites, working beside human builders rather than replacing them. Bricklaying robots place bricks with mortar in straight courses, following a digital plan of the wall, while carrier robots keep the bricks coming. Site robots use the same digital building model as the architects, called BIM, so the robot's plan and the human plan always agree. Construction sites are dusty, un",
    "label": "multi-robot-coordination-000023",
    "figures": {
      "robots": 9,
      "courses": 48,
      "bricks": 7200,
      "checks": 96,
      "site_m2": 1800,
      "success_pct": 93
    }
  },
  {
    "title": "Hospital Delivery Robot Teams",
    "subject": "Robot teams that carry medicine, samples and linen through hospitals.",
    "description": "Hospital Delivery Robot Teams is a public record about Robot teams that carry medicine, samples and linen through hospitals. Hospital delivery robots carry medicine, lab samples, linen and meals through hospital corridors, so nurses spend their time with patients instead of walking the building. The robots ride lifts, open automatic doors and wait politely in corridors, using maps of the hospital that mark wards, pharmacies and laboratories. A delivery robot locks its cargo compartment, so only the right ward can open it, which keeps medicine safe and records who received it. During disease ou",
    "label": "multi-robot-coordination-000024",
    "figures": {
      "robots": 8,
      "deliveries": 96,
      "wards": 12,
      "trips": 96,
      "lock_checks": 96,
      "success_pct": 98
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
