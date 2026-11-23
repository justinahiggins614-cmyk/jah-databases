// Seeded boundless generator for the Robotics Research Exchange Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-robotics-research-exchange.js [seed]  (prints one JSON record)
// or: node gen-robotics-research-exchange.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "robotics-research-exchange";
const RECORD_KIND = "robotics research exchange record";
const ID_PREFIX = "JAH-RREX-";
const AI_NAME = "JAH Robotics Research Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "arXiv for Robotics Research",
    "subject": "The preprint server where robotics papers appear before formal review.",
    "description": "arXiv for Robotics Research is a public record about The preprint server where robotics papers appear before formal review. arXiv is an open-access archive of scientific preprints, and robotics researchers post papers there so others can read them months before a journal or conference publishes them. Paul Ginsparg started arXiv in 1991 for physics preprints, and it now covers computer science, mathematics and robotics, with thousands of papers posted every month. Robotics papers on arXiv are usually also submitted to a conference, so the preprint is an early draft and the conference version is",
    "label": "robotics-research-exchange-000001",
    "figures": {
      "robots": 0,
      "papers": 240,
      "months_early": 6,
      "comments": 18,
      "citations": 42,
      "success_pct": 96
    }
  },
  {
    "title": "The IEEE Robotics and Automation Society",
    "subject": "The professional society that organises robotics research worldwide.",
    "description": "The IEEE Robotics and Automation Society is a public record about The professional society that organises robotics research worldwide. The IEEE Robotics and Automation Society, called RAS, is the professional society for robotics within the Institute of Electrical and Electronics Engineers. RAS sponsors the two largest robotics conferences, ICRA and IROS, and publishes the leading journals, including the Transactions on Robotics. The society runs technical committees on topics from marine robotics to soft robotics, so researchers in a niche can find each other. Membership is open to students a",
    "label": "robotics-research-exchange-000002",
    "figures": {
      "robots": 0,
      "members": 15000,
      "committees": 30,
      "conferences": 2,
      "journals": 4,
      "success_pct": 97
    }
  },
  {
    "title": "Robotics Science and Systems Conference",
    "subject": "The conference where new robotics science is argued in the open.",
    "description": "Robotics Science and Systems Conference is a public record about The conference where new robotics science is argued in the open. Robotics: Science and Systems, called RSS, is a conference that focuses on the science of robotics: new algorithms, new proofs and new understanding, rather than product demonstrations. RSS uses single-track sessions, so every attendee hears every talk, which makes the discussion sharper than in conferences with many parallel rooms. Papers at RSS are reviewed by at least three experts, and the acceptance rate is low, so a paper there carries weight in the field. The",
    "label": "robotics-research-exchange-000003",
    "figures": {
      "robots": 0,
      "papers": 120,
      "reviewers": 3,
      "accept_pct": 28,
      "workshops": 12,
      "success_pct": 95
    }
  },
  {
    "title": "The ICRA Robotics Conference",
    "subject": "The largest annual robotics research conference in the world.",
    "description": "The ICRA Robotics Conference is a public record about The largest annual robotics research conference in the world. The International Conference on Robotics and Automation, called ICRA, is the largest annual robotics conference, with thousands of papers and attendees from every country. ICRA is sponsored by the IEEE Robotics and Automation Society, and it covers every part of robotics, from manipulation and locomotion to perception and learning. The conference includes an exhibition where companies show robots, and competitions where student teams test their machines against each other. A pape",
    "label": "robotics-research-exchange-000004",
    "figures": {
      "robots": 0,
      "papers": 1200,
      "attendees": 5000,
      "days": 5,
      "exhibitors": 80,
      "success_pct": 96
    }
  },
  {
    "title": "The IROS Robotics Conference",
    "subject": "The international conference on intelligent robots and systems.",
    "description": "The IROS Robotics Conference is a public record about The international conference on intelligent robots and systems. The International Conference on Intelligent Robots and Systems, called IROS, is one of the two largest robotics conferences, and it focuses on intelligent robots that perceive, plan and act. IROS is sponsored by IEEE and partners in Japan, and it rotates between Asia, Europe and the Americas, so researchers worldwide can attend. The conference covers robot learning, human-robot interaction, field robotics and medical robotics, among many other topics. IROS also runs forums on t",
    "label": "robotics-research-exchange-000005",
    "figures": {
      "robots": 0,
      "papers": 1100,
      "attendees": 4500,
      "days": 5,
      "regions": 3,
      "success_pct": 96
    }
  },
  {
    "title": "Open Robotics Datasets",
    "subject": "Shared datasets that let every lab test on the same robot data.",
    "description": "Open Robotics Datasets is a public record about Shared datasets that let every lab test on the same robot data. Open robotics datasets are collections of sensor readings, images and maps that labs share, so a new algorithm can be tested on the same data as the old ones. The KITTI dataset, for example, gives camera and lidar recordings from a car driving through Karlsruhe, and it is the standard test for self-driving perception. Good datasets are large, labelled and public, so results can be compared fairly and no lab needs to collect the same data twice. Datasets also reveal weaknesses: an alg",
    "label": "robotics-research-exchange-000006",
    "figures": {
      "robots": 0,
      "datasets": 24,
      "records": 15000,
      "labels": 8,
      "splits": 3,
      "success_pct": 95
    }
  },
  {
    "title": "Robot Benchmarking",
    "subject": "Fair tests that rank robot algorithms on the same tasks.",
    "description": "Robot Benchmarking is a public record about Fair tests that rank robot algorithms on the same tasks. A benchmark is a fixed task with a fixed score, so different algorithms can be ranked fairly, and robotics benchmarks cover grasping, navigation, manipulation and learning. Benchmarks need a task, a dataset or simulator, and a scoring rule, and the best ones are run by an independent party so no team can tune the test to its own algorithm. The danger of benchmarks is overfitting: teams tune their algorithm to the benchmark task and it fails on the real task, so good benchmarks rotate tasks and ",
    "label": "robotics-research-exchange-000007",
    "figures": {
      "robots": 0,
      "benchmarks": 12,
      "entries": 60,
      "tasks": 8,
      "scores": 60,
      "success_pct": 94
    }
  },
  {
    "title": "Reproducibility in Robotics Research",
    "subject": "Making sure a published robot result can be repeated by others.",
    "description": "Reproducibility in Robotics Research is a public record about Making sure a published robot result can be repeated by others. Reproducibility means another lab can repeat a published result with the same code, data and hardware, and robotics struggles with it because robots, rooms and lighting all differ. The fixes are sharing code, sharing datasets, using standard simulators, and reporting the exact hardware and settings, so a reader can rebuild the experiment. Some conferences now award badges to papers whose results were reproduced, and some require code with every submission. Reproducibili",
    "label": "robotics-research-exchange-000008",
    "figures": {
      "robots": 0,
      "papers": 50,
      "repeated": 38,
      "code_shared": 44,
      "badges": 12,
      "success_pct": 93
    }
  },
  {
    "title": "Robot Simulation Benchmarks",
    "subject": "Testing robot algorithms in simulation before trusting them on hardware.",
    "description": "Robot Simulation Benchmarks is a public record about Testing robot algorithms in simulation before trusting them on hardware. Simulation benchmarks test robot algorithms in a virtual world, where the same test can be repeated exactly and a failure costs nothing. Simulators such as Gazebo and PyBullet model physics, sensors and collisions, so an algorithm can be tested on thousands of virtual runs before it touches a real robot. The gap between simulation and reality is the key risk: an algorithm that only works in the simulator is useless, so benchmarks include noise, delays and imperfect sens",
    "label": "robotics-research-exchange-000009",
    "figures": {
      "robots": 0,
      "simulators": 4,
      "trials": 1000,
      "gap_pct": 12,
      "benchmarks": 8,
      "success_pct": 94
    }
  },
  {
    "title": "Open Source Robotics Hardware",
    "subject": "Robot designs anyone can build, fix and improve.",
    "description": "Open Source Robotics Hardware is a public record about Robot designs anyone can build, fix and improve. Open source robotics hardware means robot designs published with drawings, parts lists and software, so anyone can build, repair and improve them. The Open Source Robotics Foundation, now part of the Open Robotics community, supports the Robot Operating System and the Gazebo simulator, which are the field's shared tools. Open hardware cuts costs for students and small labs, and it spreads good designs faster than patents and products do. The trade is support: open hardware comes with a commu",
    "label": "robotics-research-exchange-000010",
    "figures": {
      "robots": 0,
      "designs": 18,
      "parts": 240,
      "builds": 60,
      "cost_usd": 350,
      "success_pct": 93
    }
  },
  {
    "title": "RoboCup Robot Soccer",
    "subject": "The competition where robot teams play football to push research forward.",
    "description": "RoboCup Robot Soccer is a public record about The competition where robot teams play football to push research forward. RoboCup is a competition where robot teams play football, and its stated goal is that by 2050 a team of robots will beat the human world champions. The competition has leagues for small robots, humanoid robots, simulation and rescue, so different skills are tested in different leagues. RoboCup pushes research because football needs perception, planning, teamwork and fast reactions all at once, and the rules change every year to keep it hard. Many ideas first shown at RoboCup,",
    "label": "robotics-research-exchange-000011",
    "figures": {
      "robots": 11,
      "teams": 40,
      "goals": 12,
      "matches": 8,
      "leagues": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The DARPA Robotics Challenge",
    "subject": "The disaster-response robot competition run by DARPA.",
    "description": "The DARPA Robotics Challenge is a public record about The disaster-response robot competition run by DARPA. The DARPA Robotics Challenge was a competition run by the United States Defense Advanced Research Projects Agency, where robots had to drive a vehicle, open doors, climb stairs and turn valves in a simulated disaster. The challenge pushed humanoid robots forward, because the tasks were chosen from real disaster response, such as the Fukushima accident. Teams had to handle falls, dust and poor radio links, and the robots that finished showed that humanoids could work in real disaster site",
    "label": "robotics-research-exchange-000012",
    "figures": {
      "robots": 0,
      "teams": 24,
      "tasks": 8,
      "finalists": 11,
      "falls": 6,
      "success_pct": 92
    }
  },
  {
    "title": "The International Journal of Robotics Research",
    "subject": "The journal where the field's longest, most careful papers appear.",
    "description": "The International Journal of Robotics Research is a public record about The journal where the field's longest, most careful papers appear. The International Journal of Robotics Research, called IJRR, is one of the oldest and most respected robotics journals, publishing long papers with full proofs and experiments. IJRR papers are reviewed for months, and the acceptance rate is low, so a paper there is a mark of careful, lasting work. The journal covers theory and practice, from robot kinematics and control to perception and planning, and its archives are the field's memory. Reading IJRR is how",
    "label": "robotics-research-exchange-000013",
    "figures": {
      "robots": 0,
      "papers": 60,
      "review_months": 6,
      "accept_pct": 22,
      "citations": 180,
      "success_pct": 95
    }
  },
  {
    "title": "Science Robotics Journal",
    "subject": "The journal where robotics meets the wider world of science.",
    "description": "Science Robotics Journal is a public record about The journal where robotics meets the wider world of science. Science Robotics is a journal from the American Association for the Advancement of Science that publishes robotics work with broad scientific impact. It covers medical robots, soft robots, bio-inspired robots and robots for exploration, and its papers are written for scientists outside robotics as well as inside it. A paper in Science Robotics reaches a wide audience, so it must explain why the work matters beyond the robotics lab. The journal also publishes perspectives on the ethics",
    "label": "robotics-research-exchange-000014",
    "figures": {
      "robots": 0,
      "papers": 48,
      "fields": 8,
      "reviewers": 4,
      "citations": 240,
      "success_pct": 95
    }
  },
  {
    "title": "Robot Ethics Research",
    "subject": "Studying what robots should and should not be allowed to do.",
    "description": "Robot Ethics Research is a public record about Studying what robots should and should not be allowed to do. Robot ethics studies the moral questions raised by robots: who is responsible when a robot harms someone, how much a robot should decide on its own, and what jobs robots should not take. The field covers military robots, care robots, autonomous vehicles and workplace robots, and it brings together engineers, philosophers and lawyers. A central question is responsibility: if a self-driving car crashes, the blame may fall on the owner, the maker, the software writer or nobody, and the law ",
    "label": "robotics-research-exchange-000015",
    "figures": {
      "robots": 0,
      "papers": 36,
      "questions": 12,
      "standards": 4,
      "debates": 8,
      "success_pct": 93
    }
  },
  {
    "title": "Robotics Education Exchange",
    "subject": "Sharing courses, labs and robots for teaching robotics.",
    "description": "Robotics Education Exchange is a public record about Sharing courses, labs and robots for teaching robotics. Robotics education exchange shares courses, lab exercises and robot kits, so a teacher anywhere can teach robotics without building everything from scratch. Shared labs use cheap robots and simulators, so students can experiment at home and in class, and competitions give them a reason to improve. The exchange includes teacher training, since a good robotics course needs a teacher who can fix robots and debug code. Open courseware from universities is a large part of the exchange, and i",
    "label": "robotics-research-exchange-000016",
    "figures": {
      "robots": 0,
      "courses": 20,
      "students": 800,
      "labs": 40,
      "kits": 120,
      "success_pct": 96
    }
  },
  {
    "title": "The KITTI Vision Dataset",
    "subject": "The driving dataset that became the standard test for robot cars.",
    "description": "The KITTI Vision Dataset is a public record about The driving dataset that became the standard test for robot cars. KITTI is a dataset of camera and lidar recordings from a car driving around Karlsruhe in Germany, and it is the standard test for self-driving car perception. It was collected by the Karlsruhe Institute of Technology and the Toyota Technological Institute at Chicago, and it includes stereo images, lidar point clouds and GPS positions. KITTI provides labelled benchmarks for stereo vision, optical flow, object detection and tracking, so a new method can be scored against every publ",
    "label": "robotics-research-exchange-000017",
    "figures": {
      "robots": 0,
      "images": 15000,
      "lidar_scans": 15000,
      "benchmarks": 8,
      "methods": 200,
      "success_pct": 95
    }
  },
  {
    "title": "Learning from Demonstration in Robotics",
    "subject": "Teaching robots by showing them how, instead of programming every step.",
    "description": "Learning from Demonstration in Robotics is a public record about Teaching robots by showing them how, instead of programming every step. Learning from demonstration means teaching a robot by showing it the task, so a person performs the motion and the robot learns to repeat it. The robot records the demonstrator's movements and generalises them, so it can repeat the task from a new starting position or with a slightly different object. The method is used for assembly, pouring, wiping and surgery assistance, where writing a program by hand is hard but showing the motion is easy. The risk is cop",
    "label": "robotics-research-exchange-000018",
    "figures": {
      "robots": 0,
      "demos": 24,
      "tasks": 6,
      "trials": 120,
      "success_trials": 108,
      "success_pct": 94
    }
  },
  {
    "title": "Shared Autonomy Research",
    "subject": "Humans and robots sharing control of one machine.",
    "description": "Shared Autonomy Research is a public record about Humans and robots sharing control of one machine. Shared autonomy means a human and a robot share control of one machine, such as a wheelchair or a robot arm, with the robot helping and the human deciding. The robot assists with the hard parts, such as avoiding obstacles or holding a steady grasp, while the human keeps the goal and the judgement. The research question is how to split the work: too much robot help and the human feels useless; too little and the human is overloaded. Shared autonomy is used in assistive robots, surgery and teleope",
    "label": "robotics-research-exchange-000019",
    "figures": {
      "robots": 0,
      "users": 30,
      "tasks": 5,
      "trials": 150,
      "satisfaction": 88,
      "success_pct": 93
    }
  },
  {
    "title": "Robotics Safety Standards",
    "subject": "The ISO rules that keep industrial robots from harming people.",
    "description": "Robotics Safety Standards is a public record about The ISO rules that keep industrial robots from harming people. ISO 10218 is the international safety standard for industrial robots, and it sets rules for guarding, stopping distances and safe speeds. The standard requires risk assessment for every robot cell, so the hazards are listed and the guards, sensors and procedures that control them are chosen on purpose. Collaborative robots, called cobots, follow the related standard ISO/TS 15066, which limits the force a robot may apply to a person. Safety standards are written by committees of mak",
    "label": "robotics-research-exchange-000020",
    "figures": {
      "robots": 0,
      "standards": 6,
      "hazards": 14,
      "controls": 14,
      "tests": 40,
      "success_pct": 97
    }
  },
  {
    "title": "Collaborative Robots in Research",
    "subject": "Robots designed to work beside people without fences.",
    "description": "Collaborative Robots in Research is a public record about Robots designed to work beside people without fences. Collaborative robots, called cobots, are robots designed to work beside people without safety fences, using force limits and sensors to stop before they hurt anyone. Cobots are lighter and slower than industrial robots, and they are programmed by guiding them by hand, so a worker can teach a cobot a task in minutes. Research on cobots covers safe contact, shared workspaces, and how people trust a robot that works inches from their hands. Cobots are used in assembly, packing and labor",
    "label": "robotics-research-exchange-000021",
    "figures": {
      "robots": 0,
      "cobots": 10,
      "tasks": 8,
      "force_n": 120,
      "trials": 80,
      "success_pct": 95
    }
  },
  {
    "title": "Soft Robotics Research",
    "subject": "Robots made of rubber and fabric instead of metal and motors.",
    "description": "Soft Robotics Research is a public record about Robots made of rubber and fabric instead of metal and motors. Soft robotics builds robots from flexible materials such as rubber, fabric and gels, so the robot bends and squeezes instead of moving on stiff joints. Soft robots are safe to touch and can handle fruit, organs and fragile objects, because they spread their grip over a soft surface instead of pinching with hard fingers. A soft gripper is often driven by air: pumping air into chambers makes the fingers curl, and releasing the air lets them relax. The research problems are control and se",
    "label": "robotics-research-exchange-000022",
    "figures": {
      "robots": 0,
      "grippers": 6,
      "objects": 20,
      "pressure_kpa": 80,
      "trials": 100,
      "success_pct": 93
    }
  },
  {
    "title": "Robot Manipulation Datasets and Benchmarks",
    "subject": "Shared objects, grasps and scores for robot hands.",
    "description": "Robot Manipulation Datasets and Benchmarks is a public record about Shared objects, grasps and scores for robot hands. Robot manipulation benchmarks test how well a robot hand grasps and moves objects, using shared object sets such as the YCB set, which gives every lab the same cups, boxes and tools to grasp. The YCB object set was published in 2015, and it lets a grasping result in one lab be compared with a result in another, because the objects are identical. Manipulation benchmarks score success rate, time and gentleness, so a hand that crushes the cup fails even if it lifts it. Shared man",
    "label": "robotics-research-exchange-000023",
    "figures": {
      "robots": 0,
      "objects": 77,
      "grasps": 200,
      "trials": 400,
      "success_grasps": 352,
      "success_pct": 93
    }
  },
  {
    "title": "Humanoid Research Exchange",
    "subject": "Sharing what works in building robots shaped like people.",
    "description": "Humanoid Research Exchange is a public record about Sharing what works in building robots shaped like people. Humanoid robots are shaped like people, with a head, torso, two arms and two legs, so they can use tools, doors and stairs built for humans. Research exchange on humanoids covers balance, walking, grasping and face interaction, since a humanoid must do all of them to be useful. The hardest problem is balance: a humanoid that falls can break itself, so walking controllers are tested in simulation thousands of times before a real step. Humanoids are used in research, entertainment and ca",
    "label": "robotics-research-exchange-000024",
    "figures": {
      "robots": 0,
      "humanoids": 4,
      "sim_steps": 5000,
      "real_steps": 800,
      "falls": 3,
      "success_pct": 92
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
    "name": "arXiv (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/ArXiv",
    "retrieved": "2026-11-18"
  },
  {
    "name": "Robotics (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Robotics",
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
