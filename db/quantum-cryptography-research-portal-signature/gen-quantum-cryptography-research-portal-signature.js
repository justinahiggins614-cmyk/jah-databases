// Seeded boundless generator for the Quantum Cryptography Research Portal Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-quantum-cryptography-research-portal-signature.js [seed]  (prints one JSON record)
// or: node gen-quantum-cryptography-research-portal-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "quantum-cryptography-research-portal-signature";
const RECORD_KIND = "quantum cryptography research portal record";
const ID_PREFIX = "JAH-QCRP-S-";
const AI_NAME = "JAH Quantum Cryptography Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Photon Post",
    "subject": "A Signature design for a post office that sends keys by single photons.",
    "description": "The Photon Post is a Signature design-study: A Signature design for a post office that sends keys by single photons. The Photon Post is a Signature-made design: a post office that sends secret keys one photon at a time, so any interception shows as errors. Its novelty is an error bell that rings when the error rate passes the safe limit, throwing the key away before it is used. The Post is meant for links too sensitive for ordinary keys. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own ",
    "label": "quantum-cryptography-research-portal-signature-000001",
    "figures": {
      "robots": 0,
      "key_bits": 256,
      "photons": 10500,
      "error_pct": 2,
      "distance_km": 52,
      "success_pct": 95
    }
  },
  {
    "title": "The Four-Way Key",
    "subject": "A Signature design for a key made from four photon polarisations.",
    "description": "The Four-Way Key is a Signature design-study: A Signature design for a key made from four photon polarisations. The Four-Way Key is a Signature-made design: a key protocol using photons in four polarisations across two bases, after Bennett and Brassard 1984. Its novelty is a basis ledger that records which basis each bit used, so the key can be audited later. The Key is meant as the reference design every later protocol is measured against. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its o",
    "label": "quantum-cryptography-research-portal-signature-000002",
    "figures": {
      "robots": 0,
      "bases": 2,
      "polarisations": 4,
      "key_bits": 256,
      "error_pct": 3,
      "success_pct": 95
    }
  },
  {
    "title": "The Linked Pair",
    "subject": "A Signature design for keys shared by entangled photon pairs.",
    "description": "The Linked Pair is a Signature design-study: A Signature design for keys shared by entangled photon pairs. The Linked Pair is a Signature-made design: a key system built on entangled photon pairs, after Ekert 1991, where measuring one photon affects the other. Its novelty is a Bell check built into every exchange, so the entanglement itself is proven before the key is trusted. The Pair is meant for satellite links and the future quantum internet. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on",
    "label": "quantum-cryptography-research-portal-signature-000003",
    "figures": {
      "robots": 0,
      "pairs": 5200,
      "bell_score": 2,
      "key_bits": 256,
      "distance_km": 110,
      "success_pct": 93
    }
  },
  {
    "title": "The New Maths",
    "subject": "A Signature design for cryptography that survives quantum computers.",
    "description": "The New Maths is a Signature design-study: A Signature design for cryptography that survives quantum computers. The New Maths is a Signature-made design: a cryptography set built from problems even a quantum computer cannot easily solve. Its novelty is a risk register that lists every old system and its quantum danger, so migration is by risk, not by habit. The Maths is meant for data that must stay secret for decades. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its ",
    "label": "quantum-cryptography-research-portal-signature-000004",
    "figures": {
      "robots": 0,
      "systems": 13,
      "candidates": 4,
      "key_kb": 2,
      "migrated_pct": 42,
      "success_pct": 94
    }
  },
  {
    "title": "The Grid Lock",
    "subject": "A Signature design for a lock built on lattices in many dimensions.",
    "description": "The Grid Lock is a Signature design-study: A Signature design for a lock built on lattices in many dimensions. The Grid Lock is a Signature-made design: a lock built on lattices, grids of points in many dimensions, where finding the shortest vector is hard. Its novelty is a noise dial that tunes how much noise hides the secret, balancing safety against speed. The Lock is meant for encryption, signatures and computing on encrypted data. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own te",
    "label": "quantum-cryptography-research-portal-signature-000005",
    "figures": {
      "robots": 0,
      "dimension": 512,
      "noise": 3,
      "key_kb": 2,
      "speed_ms": 1,
      "success_pct": 95
    }
  },
  {
    "title": "The Open Contest",
    "subject": "A Signature design for a public contest that chooses cryptography standards.",
    "description": "The Open Contest is a Signature design-study: A Signature design for a public contest that chooses cryptography standards. The Open Contest is a Signature-made design: an open competition where cryptographers submit proposals and the world tries to break them. Its novelty is a public attack record: every attack and every fix is published, so the winners are trusted because they survived in the open. The Contest is meant for standards the whole world must adopt together. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product.",
    "label": "quantum-cryptography-research-portal-signature-000006",
    "figures": {
      "robots": 0,
      "proposals": 84,
      "rounds": 3,
      "standards": 3,
      "years": 8,
      "success_pct": 96
    }
  },
  {
    "title": "The Wrapped Key",
    "subject": "A Signature design for wrapping session keys in lattice mathematics.",
    "description": "The Wrapped Key is a Signature design-study: A Signature design for wrapping session keys in lattice mathematics. The Wrapped Key is a Signature-made design: a lattice key-wrapping mechanism, after Kyber, that exchanges keys safely against quantum computers. Its novelty is a wrap counter that tracks every key wrapped, so a reused key is caught at once. The Key is meant for the everyday traffic of the internet. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are",
    "label": "quantum-cryptography-research-portal-signature-000007",
    "figures": {
      "robots": 0,
      "key_bytes": 1568,
      "cipher_bytes": 1568,
      "speed_us": 40,
      "security_bits": 128,
      "success_pct": 96
    }
  },
  {
    "title": "The Lattice Pen",
    "subject": "A Signature design for a pen that signs with lattice proofs.",
    "description": "The Lattice Pen is a Signature design-study: A Signature design for a pen that signs with lattice proofs. The Lattice Pen is a Signature-made design: a signature pen, after Dilithium, that signs messages with lattice proofs a quantum computer cannot forge. Its novelty is a verification stamp that records every check, so a signature's history can be audited. The Pen is meant for software updates, documents and certificates. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether ",
    "label": "quantum-cryptography-research-portal-signature-000008",
    "figures": {
      "robots": 0,
      "sig_bytes": 2420,
      "key_bytes": 1312,
      "sign_us": 60,
      "verify_us": 30,
      "success_pct": 96
    }
  },
  {
    "title": "The True Coin",
    "subject": "A Signature design for a coin that flips on quantum randomness.",
    "description": "The True Coin is a Signature design-study: A Signature design for a coin that flips on quantum randomness. The True Coin is a Signature-made design: a random number generator that flips on quantum measurement, not on an algorithm. Its novelty is a bias watch that tests every batch of bits and discards any batch that leans. The Coin is meant for keys, passwords and nonces that must be unpredictable. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its ",
    "label": "quantum-cryptography-research-portal-signature-000009",
    "figures": {
      "robots": 0,
      "rate_mbps": 17,
      "bits": 1000000,
      "bias_pct": 0,
      "tests_passed": 15,
      "success_pct": 97
    }
  },
  {
    "title": "The Blind Device",
    "subject": "A Signature design for key distribution that trusts no device at all.",
    "description": "The Blind Device is a Signature design-study: A Signature design for key distribution that trusts no device at all. The Blind Device is a Signature-made design: a key system whose security comes from measurement statistics alone, trusting no device. Its novelty is a device test card that must be passed before any key is trusted, with the Bell score printed on it. The Device is meant for the strongest security, where even the hardware is suspect. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on ",
    "label": "quantum-cryptography-research-portal-signature-000010",
    "figures": {
      "robots": 0,
      "bell_score": 2,
      "detection_pct": 83,
      "key_bits": 128,
      "distance_m": 210,
      "success_pct": 92
    }
  },
  {
    "title": "The Long Relay",
    "subject": "A Signature design for a relay that carries entanglement across continents.",
    "description": "The Long Relay is a Signature design-study: A Signature design for a relay that carries entanglement across continents. The Long Relay is a Signature-made design: a chain of repeaters that carries entanglement across distances no single fibre can span. Its novelty is a memory gauge that shows how long each repeater can hold a photon's state. The Relay is meant for keys that must travel between continents. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clea",
    "label": "quantum-cryptography-research-portal-signature-000011",
    "figures": {
      "robots": 0,
      "segments": 4,
      "distance_km": 420,
      "memory_ms": 11,
      "key_rate_bps": 110,
      "success_pct": 93
    }
  },
  {
    "title": "The Shared Link",
    "subject": "A Signature design for a link that shares entanglement between distant places.",
    "description": "The Shared Link is a Signature design-study: A Signature design for a link that shares entanglement between distant places. The Shared Link is a Signature-made design: a link that shares entangled photon pairs between distant places, by fibre or by satellite. Its novelty is a fidelity meter that shows how close the shared pairs are to perfect entanglement. The Link is meant for the foundation of quantum networks. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules ",
    "label": "quantum-cryptography-research-portal-signature-000012",
    "figures": {
      "robots": 0,
      "pairs_per_s": 1100,
      "distance_km": 1250,
      "fidelity_pct": 92,
      "rate_hz": 11,
      "success_pct": 94
    }
  },
  {
    "title": "The Quantum Seal",
    "subject": "A Signature design for a seal whose security rests on physics, not maths.",
    "description": "The Quantum Seal is a Signature design-study: A Signature design for a seal whose security rests on physics, not maths. The Quantum Seal is a Signature-made design: a signature sealed with quantum states, so forging it would require copying the uncopyable. Its novelty is a copy alarm that sounds when a measurement disagrees with the seal's record. The Seal is meant for signatures that must survive the arrival of quantum computers. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: ",
    "label": "quantum-cryptography-research-portal-signature-000013",
    "figures": {
      "robots": 0,
      "sig_qubits": 1024,
      "forgery_prob": 1,
      "parties": 3,
      "distance_km": 22,
      "success_pct": 92
    }
  },
  {
    "title": "The Fair Toss",
    "subject": "A Signature design for a fair coin toss between parties who do not trust each other.",
    "description": "The Fair Toss is a Signature design-study: A Signature design for a fair coin toss between parties who do not trust each other. The Fair Toss is a Signature-made design: a coin toss by telephone that neither party can cheat, built on quantum states. Its novelty is a bias ledger that records every measured bias, so the protocol's fairness is public. The Toss is meant for voting and contract signing where fairness must be provable. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: w",
    "label": "quantum-cryptography-research-portal-signature-000014",
    "figures": {
      "robots": 0,
      "rounds": 110,
      "bias_pct": 8,
      "cheat_detected": 13,
      "parties": 2,
      "success_pct": 93
    }
  },
  {
    "title": "The Uncopyable Note",
    "subject": "A Signature design for a banknote that physics forbids copying.",
    "description": "The Uncopyable Note is a Signature design-study: A Signature design for a banknote that physics forbids copying. The Uncopyable Note is a Signature-made design: a banknote that stores value in photons with secret polarisations, after Wiesner 1983. Its novelty is a serial check that ties every note to a bank record, so a copied note fails the check even if it looks right. The Note is meant as a research design, since storing photons for years is still unsolved. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The desig",
    "label": "quantum-cryptography-research-portal-signature-000015",
    "figures": {
      "robots": 0,
      "photons": 100,
      "notes": 22,
      "forgeries": 0,
      "verify_s": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The Factoring Clock",
    "subject": "A Signature design for a clock that counts down to the day quantum computers break old keys.",
    "description": "The Factoring Clock is a Signature design-study: A Signature design for a clock that counts down to the day quantum computers break old keys. The Factoring Clock is a Signature-made design: a clock that tracks quantum computer size against the size needed to break today's keys. Its novelty is a migration alarm that rings for each system as its safety margin shrinks. The Clock is meant for organisations that must replace cryptography before the threat arrives. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design",
    "label": "quantum-cryptography-research-portal-signature-000016",
    "figures": {
      "robots": 0,
      "qubits_needed": 4000,
      "qubits_today": 1050,
      "key_bits": 2048,
      "systems_at_risk": 11,
      "success_pct": 94
    }
  },
  {
    "title": "The Migration Map",
    "subject": "A Signature design for a map that moves a whole organisation to quantum-safe cryptography.",
    "description": "The Migration Map is a Signature design-study: A Signature design for a map that moves a whole organisation to quantum-safe cryptography. The Migration Map is a Signature-made design: a staged map for moving every system in an organisation to post-quantum standards. Its novelty is a dual-running bridge that lets old and new algorithms work side by side during the change. The Map is meant for multi-year migrations that cannot stop the business. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on it",
    "label": "quantum-cryptography-research-portal-signature-000017",
    "figures": {
      "robots": 0,
      "systems": 62,
      "inventoried": 62,
      "migrated": 26,
      "years": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The Layered Net",
    "subject": "A Signature design for a net of quantum nodes in layers.",
    "description": "The Layered Net is a Signature design-study: A Signature design for a net of quantum nodes in layers. The Layered Net is a Signature-made design: a quantum network in layers, from photon sending to entanglement routing. Its novelty is a freshness rule: entanglement is consumed when used, so the net constantly grows new entanglement. The Net is meant for testbeds linking cities and laboratories. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its part",
    "label": "quantum-cryptography-research-portal-signature-000018",
    "figures": {
      "robots": 0,
      "nodes": 9,
      "links": 13,
      "rate_hz": 55,
      "layers": 3,
      "success_pct": 93
    }
  },
  {
    "title": "The Sky Key",
    "subject": "A Signature design for a key sent from a satellite to the ground.",
    "description": "The Sky Key is a Signature design-study: A Signature design for a key sent from a satellite to the ground. The Sky Key is a Signature-made design: a satellite key system that sends photons down during the few minutes of a pass. Its novelty is a pass planner that schedules every ground station's window, so no pass is wasted. The Key is meant for a global quantum network, since satellites can link any two points under the same sky. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: w",
    "label": "quantum-cryptography-research-portal-signature-000019",
    "figures": {
      "robots": 0,
      "passes": 7,
      "key_bits": 256,
      "distance_km": 1250,
      "pass_min": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The Flaw Finder",
    "subject": "A Signature design for a finder that attacks quantum devices to make them stronger.",
    "description": "The Flaw Finder is a Signature design-study: A Signature design for a finder that attacks quantum devices to make them stronger. The Flaw Finder is a Signature-made design: a defensive tester that attacks real QKD devices through their imperfections, such as blindable detectors. Its novelty is a fix-and-retest loop: every successful attack must be fixed and the device tested again before it ships. The Finder is meant for earning trust in quantum products. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is ",
    "label": "quantum-cryptography-research-portal-signature-000020",
    "figures": {
      "robots": 0,
      "attacks": 15,
      "blocked": 13,
      "open": 2,
      "devices": 4,
      "success_pct": 93
    }
  },
  {
    "title": "The Shared Secret",
    "subject": "A Signature design for a secret split so only the whole group can rebuild it.",
    "description": "The Shared Secret is a Signature design-study: A Signature design for a secret split so only the whole group can rebuild it. The Shared Secret is a Signature-made design: a secret split among parties in an entangled state, so only the required group can rebuild it. Its novelty is a threshold card that states plainly how many parties must agree, so no one person holds the whole secret. The Secret is meant for master keys and shared vaults. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own",
    "label": "quantum-cryptography-research-portal-signature-000021",
    "figures": {
      "robots": 0,
      "parties": 5,
      "threshold": 3,
      "shares": 5,
      "rebuilds": 11,
      "success_pct": 95
    }
  },
  {
    "title": "The Blind Computer",
    "subject": "A Signature design for a computer that cannot see what it computes.",
    "description": "The Blind Computer is a Signature design-study: A Signature design for a computer that cannot see what it computes. The Blind Computer is a Signature-made design: a remote quantum computer that runs a client's work without learning the input, the program or the result. Its novelty is a leakage meter that must read zero before the result is trusted. The Computer is meant for users of shared quantum clouds who want privacy. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether i",
    "label": "quantum-cryptography-research-portal-signature-000022",
    "figures": {
      "robots": 0,
      "qubits": 52,
      "instructions": 210,
      "leaked_bits": 0,
      "rounds": 22,
      "success_pct": 93
    }
  },
  {
    "title": "The Sealed Calculator",
    "subject": "A Signature design for a calculator that computes on sealed data.",
    "description": "The Sealed Calculator is a Signature design-study: A Signature design for a calculator that computes on sealed data. The Sealed Calculator is a Signature-made design: a quantum calculator that processes encrypted data without opening it. Its novelty is a check run: every sealed computation is checked against a plain computation on test data. The Calculator is meant for private cloud computing. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are clear, its parts",
    "label": "quantum-cryptography-research-portal-signature-000023",
    "figures": {
      "robots": 0,
      "qubits": 42,
      "gates": 125,
      "overhead": 8,
      "checks": 11,
      "success_pct": 92
    }
  },
  {
    "title": "The Entangled Web",
    "subject": "A Signature design for a web that shares entanglement the way the internet shares data.",
    "description": "The Entangled Web is a Signature design-study: A Signature design for a web that shares entanglement the way the internet shares data. The Entangled Web is a Signature-made design: a future network that shares entanglement between distant nodes, built in stages from key networks to full quantum computing networks. Its novelty is a stage map that shows every city link and its stage, so the web's growth is public. The Web is meant for quantum computers, sensors and keys working together. This is a Signature-made design, presented as a design study only, never as an established fact and never as ",
    "label": "quantum-cryptography-research-portal-signature-000024",
    "figures": {
      "robots": 0,
      "nodes": 7,
      "distance_km": 520,
      "fidelity_pct": 91,
      "rate_hz": 22,
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
    "name": "Quantum key distribution (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Quantum_key_distribution",
    "retrieved": "2026-11-18"
  },
  {
    "name": "Quantum cryptography (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Quantum_cryptography",
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
