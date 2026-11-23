// Seeded boundless generator for the Quantum Cryptography Research Portal Database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-quantum-cryptography-research-portal.js [seed]  (prints one JSON record)
// or: node gen-quantum-cryptography-research-portal.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "quantum-cryptography-research-portal";
const RECORD_KIND = "quantum cryptography research portal record";
const ID_PREFIX = "JAH-QCRP-";
const AI_NAME = "JAH Quantum Cryptography Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Quantum Key Distribution",
    "subject": "Sharing secret keys with light, so eavesdropping is caught by physics.",
    "description": "Quantum Key Distribution is a public record about Sharing secret keys with light, so eavesdropping is caught by physics. Quantum key distribution, called QKD, shares a secret key between two parties using single particles of light, called photons, and the laws of quantum physics expose any eavesdropper. Measuring a photon changes it, so if someone intercepts the key, the errors they cause are visible, and the two parties throw the key away and try again. QKD does not send the message itself: it sends the key, and the message is then encrypted with ordinary mathematics using that key. QKD links",
    "label": "quantum-cryptography-research-portal-000001",
    "figures": {
      "robots": 0,
      "key_bits": 256,
      "photons": 10000,
      "error_pct": 2,
      "distance_km": 50,
      "success_pct": 96
    }
  },
  {
    "title": "The BB84 Quantum Key Protocol",
    "subject": "The first quantum key protocol, published by Bennett and Brassard in 1984.",
    "description": "The BB84 Quantum Key Protocol is a public record about The first quantum key protocol, published by Bennett and Brassard in 1984. BB84 is the first quantum key distribution protocol, published by Charles Bennett and Gilles Brassard in 1984, and it uses photons polarised in two different bases. Alice sends photons in one of four polarisations, Bob measures each in a randomly chosen basis, and the two keep only the bits where their bases matched. An eavesdropper who measures a photon disturbs it, and the disturbance shows up as errors when Alice and Bob compare a sample of their key. BB84 is the",
    "label": "quantum-cryptography-research-portal-000002",
    "figures": {
      "robots": 0,
      "bases": 2,
      "polarisations": 4,
      "key_bits": 256,
      "error_pct": 3,
      "success_pct": 96
    }
  },
  {
    "title": "The E91 Entanglement Protocol",
    "subject": "Sharing keys with entangled photon pairs, proposed by Artur Ekert in 1991.",
    "description": "The E91 Entanglement Protocol is a public record about Sharing keys with entangled photon pairs, proposed by Artur Ekert in 1991. The E91 protocol, proposed by Artur Ekert in 1991, shares keys using entangled photon pairs, where two photons are linked so measuring one instantly affects the other. Alice and Bob each receive one photon from each pair and measure it, and the correlation between their results builds the key. E91 tests Bell's inequality, a statistical check that proves the photons were truly entangled, so an eavesdropper cannot fake the results without breaking the test. Entangleme",
    "label": "quantum-cryptography-research-portal-000003",
    "figures": {
      "robots": 0,
      "pairs": 5000,
      "bell_score": 2,
      "key_bits": 256,
      "distance_km": 100,
      "success_pct": 94
    }
  },
  {
    "title": "Post-Quantum Cryptography",
    "subject": "New mathematics for a world with quantum computers.",
    "description": "Post-Quantum Cryptography is a public record about New mathematics for a world with quantum computers. Post-quantum cryptography is cryptography built from mathematics that even a quantum computer cannot easily break, so it protects data against future quantum attacks. Today's public-key cryptography relies on factoring and discrete logarithms, which Shor's algorithm can break on a large enough quantum computer, so new systems are needed before such computers exist. Post-quantum systems use lattices, hash functions, codes and multivariate equations, and the United States National Institute of ",
    "label": "quantum-cryptography-research-portal-000004",
    "figures": {
      "robots": 0,
      "systems": 12,
      "candidates": 4,
      "key_kb": 2,
      "migrated_pct": 40,
      "success_pct": 95
    }
  },
  {
    "title": "Lattice-Based Cryptography",
    "subject": "Cryptography built on the hardness of finding short vectors in grids.",
    "description": "Lattice-Based Cryptography is a public record about Cryptography built on the hardness of finding short vectors in grids. Lattice-based cryptography builds security on lattices, which are regular grids of points in many dimensions, and on the difficulty of finding the shortest vector in a lattice. The learning-with-errors problem asks a solver to recover a secret from noisy equations on a lattice, and it is believed hard even for quantum computers. Lattice schemes are fast and versatile: they provide encryption, signatures and fully homomorphic encryption, which computes on encrypted data. The",
    "label": "quantum-cryptography-research-portal-000005",
    "figures": {
      "robots": 0,
      "dimension": 512,
      "noise": 3,
      "key_kb": 2,
      "speed_ms": 1,
      "success_pct": 96
    }
  },
  {
    "title": "NIST Post-Quantum Standardisation",
    "subject": "The open competition that chose the new quantum-safe standards.",
    "description": "NIST Post-Quantum Standardisation is a public record about The open competition that chose the new quantum-safe standards. The United States National Institute of Standards and Technology, called NIST, ran an open competition from 2016 to choose post-quantum cryptography standards. Dozens of proposals were submitted, attacked by cryptanalysts worldwide, and the survivors were standardised: ML-KEM for key exchange and ML-DSA and SLH-DSA for signatures. The competition was public, so every attack and every fix is on the record, which is why the standards are trusted. Standardisation matters beca",
    "label": "quantum-cryptography-research-portal-000006",
    "figures": {
      "robots": 0,
      "proposals": 82,
      "rounds": 3,
      "standards": 3,
      "years": 8,
      "success_pct": 97
    }
  },
  {
    "title": "CRYSTALS-Kyber Key Exchange",
    "subject": "The lattice key-exchange mechanism chosen as the ML-KEM standard.",
    "description": "CRYSTALS-Kyber Key Exchange is a public record about The lattice key-exchange mechanism chosen as the ML-KEM standard. CRYSTALS-Kyber, now standardised as ML-KEM, is a lattice-based key encapsulation mechanism for exchanging keys safely against quantum computers. Kyber is based on the module learning-with-errors problem, and it offers small keys and ciphertexts with fast operations, which is why it won the NIST competition. A key encapsulation mechanism works by generating a random key, wrapping it with the recipient's public key, and letting the recipient unwrap it with the private key. Kyber",
    "label": "quantum-cryptography-research-portal-000007",
    "figures": {
      "robots": 0,
      "key_bytes": 1568,
      "cipher_bytes": 1568,
      "speed_us": 40,
      "security_bits": 128,
      "success_pct": 97
    }
  },
  {
    "title": "CRYSTALS-Dilithium Signatures",
    "subject": "The lattice signature scheme chosen as the ML-DSA standard.",
    "description": "CRYSTALS-Dilithium Signatures is a public record about The lattice signature scheme chosen as the ML-DSA standard. CRYSTALS-Dilithium, now standardised as ML-DSA, is a lattice-based digital signature scheme that proves who signed a message, even against a quantum attacker. Dilithium is based on the module learning-with-errors and short-integer-solution problems, and it is fast to sign and verify, with moderate signature sizes. Digital signatures are used everywhere: software updates, identity documents, contracts and certificates all rely on signatures that must stay valid for years. Dilithium",
    "label": "quantum-cryptography-research-portal-000008",
    "figures": {
      "robots": 0,
      "sig_bytes": 2420,
      "key_bytes": 1312,
      "sign_us": 60,
      "verify_us": 30,
      "success_pct": 97
    }
  },
  {
    "title": "Quantum Random Number Generation",
    "subject": "True randomness from quantum measurement, not from an algorithm.",
    "description": "Quantum Random Number Generation is a public record about True randomness from quantum measurement, not from an algorithm. Quantum random number generators produce randomness from quantum physics, such as the time a photon arrives or which path it takes, rather than from a deterministic algorithm. Ordinary random number generators are algorithms that only look random, and if an attacker learns their starting seed, all future numbers can be predicted. True randomness matters for cryptography, because keys, nonces and passwords must be unpredictable, and a predictable key is no key at all. Quant",
    "label": "quantum-cryptography-research-portal-000009",
    "figures": {
      "robots": 0,
      "rate_mbps": 16,
      "bits": 1000000,
      "bias_pct": 0,
      "tests_passed": 15,
      "success_pct": 98
    }
  },
  {
    "title": "Device-Independent Quantum Key Distribution",
    "subject": "Key distribution that stays secure even if the devices are untrusted.",
    "description": "Device-Independent Quantum Key Distribution is a public record about Key distribution that stays secure even if the devices are untrusted. Device-independent quantum key distribution, called DI-QKD, proves security from the statistics of the measurements alone, without trusting the devices that made them. Ordinary QKD assumes the sender and receiver devices work as designed, but a compromised device could leak the key, so DI-QKD removes that trust. DI-QKD relies on a loophole-free Bell test, which proves the devices share genuine entanglement, and any cheating shows up as a failed test. DI-QKD",
    "label": "quantum-cryptography-research-portal-000010",
    "figures": {
      "robots": 0,
      "bell_score": 2,
      "detection_pct": 82,
      "key_bits": 128,
      "distance_m": 200,
      "success_pct": 92
    }
  },
  {
    "title": "Quantum Repeaters",
    "subject": "Relays that extend quantum links across continents.",
    "description": "Quantum Repeaters is a public record about Relays that extend quantum links across continents. Quantum repeaters extend quantum communication over long distances by storing entanglement in segments and joining them, so a key can travel further than one fibre span allows. Photons are lost in fibre, so a direct quantum link is limited to about a hundred kilometres, and repeaters break the distance into shorter hops. A repeater holds entangled pairs with its neighbours and swaps the entanglement, which links the far ends without ever sending a photon the whole way. Quantum repeaters need quantum ",
    "label": "quantum-cryptography-research-portal-000011",
    "figures": {
      "robots": 0,
      "segments": 4,
      "distance_km": 400,
      "memory_ms": 10,
      "key_rate_bps": 100,
      "success_pct": 93
    }
  },
  {
    "title": "Entanglement Distribution",
    "subject": "Sharing linked photon pairs between distant places.",
    "description": "Entanglement Distribution is a public record about Sharing linked photon pairs between distant places. Entanglement distribution shares entangled photon pairs between distant places, so two parties hold particles whose measurements are correlated in a way no classical system can copy. Entanglement is the resource behind QKD, quantum teleportation and distributed quantum computing, so distributing it well is the foundation of quantum networks. Distribution over fibre loses photons with distance, and distribution by satellite sends photons through the air, where the loss is lower over long dista",
    "label": "quantum-cryptography-research-portal-000012",
    "figures": {
      "robots": 0,
      "pairs_per_s": 1000,
      "distance_km": 1200,
      "fidelity_pct": 91,
      "rate_hz": 10,
      "success_pct": 94
    }
  },
  {
    "title": "Quantum Digital Signatures",
    "subject": "Signatures whose security rests on quantum physics, not on hard maths.",
    "description": "Quantum Digital Signatures is a public record about Signatures whose security rests on quantum physics, not on hard maths. Quantum digital signatures sign messages with quantum states, so the security rests on the laws of physics rather than on the difficulty of a maths problem. A quantum signature uses quantum one-way functions: signing is easy with the private key, but forging is hard because copying an unknown quantum state is impossible. Quantum signatures need a quantum network to distribute the keys, so they are a future technology, tested in laboratories today. The promise is signatures",
    "label": "quantum-cryptography-research-portal-000013",
    "figures": {
      "robots": 0,
      "sig_qubits": 1024,
      "forgery_prob": 1,
      "parties": 3,
      "distance_km": 20,
      "success_pct": 92
    }
  },
  {
    "title": "Quantum Coin Flipping",
    "subject": "A fair coin toss between two parties who do not trust each other.",
    "description": "Quantum Coin Flipping is a public record about A fair coin toss between two parties who do not trust each other. Quantum coin flipping lets two distant parties toss a fair coin by telephone, so neither can cheat the result, using quantum states that cannot be copied or measured without disturbance. Classical coin flipping by telephone is impossible to make fair, because either party can lie about the result, but quantum protocols limit how much either side can bias the outcome. The best quantum protocols still let a cheater bias the result a little, and the research question is how small that ",
    "label": "quantum-cryptography-research-portal-000014",
    "figures": {
      "robots": 0,
      "rounds": 100,
      "bias_pct": 8,
      "cheat_detected": 12,
      "parties": 2,
      "success_pct": 93
    }
  },
  {
    "title": "Quantum Money",
    "subject": "Banknotes that cannot be copied, protected by quantum physics.",
    "description": "Quantum Money is a public record about Banknotes that cannot be copied, protected by quantum physics. Quantum money is a banknote that cannot be counterfeited, because it stores value in quantum states that cannot be copied without disturbing them. Stephen Wiesner proposed quantum money in 1983, and the idea is that a banknote holds photons in secret polarisations, which the bank can check but a forger cannot copy. The no-cloning theorem proves that an unknown quantum state cannot be copied perfectly, so a forger's copy always differs from the original. Quantum money remains a research idea, b",
    "label": "quantum-cryptography-research-portal-000015",
    "figures": {
      "robots": 0,
      "photons": 100,
      "notes": 20,
      "forgeries": 0,
      "verify_s": 5,
      "success_pct": 94
    }
  },
  {
    "title": "Shor's Algorithm and the Quantum Threat",
    "subject": "The algorithm that would break today's public-key cryptography.",
    "description": "Shor's Algorithm and the Quantum Threat is a public record about The algorithm that would break today's public-key cryptography. Shor's algorithm, published by Peter Shor in 1994, factors large numbers and solves discrete logarithms exponentially faster than any known classical algorithm. Today's public-key cryptography, including RSA and elliptic-curve cryptography, relies on factoring and discrete logarithms being hard, so a large enough quantum computer running Shor's algorithm would break them. No quantum computer today is large enough to break real keys, but the threat drives the migratio",
    "label": "quantum-cryptography-research-portal-000016",
    "figures": {
      "robots": 0,
      "qubits_needed": 4000,
      "qubits_today": 1000,
      "key_bits": 2048,
      "systems_at_risk": 12,
      "success_pct": 95
    }
  },
  {
    "title": "Quantum-Safe Migration Planning",
    "subject": "Moving a whole organisation to quantum-safe cryptography without breaking it.",
    "description": "Quantum-Safe Migration Planning is a public record about Moving a whole organisation to quantum-safe cryptography without breaking it. Quantum-safe migration is the planned move from vulnerable cryptography to post-quantum standards, across every system in an organisation. Migration starts with a cryptography inventory: every system, library and protocol is listed with the algorithms it uses and the data it protects. Systems are then ranked by risk, and the highest-risk ones migrate first, often running old and new algorithms together during the changeover. The migration is a multi-year projec",
    "label": "quantum-cryptography-research-portal-000017",
    "figures": {
      "robots": 0,
      "systems": 60,
      "inventoried": 60,
      "migrated": 24,
      "years": 5,
      "success_pct": 94
    }
  },
  {
    "title": "Quantum Network Protocols",
    "subject": "The rules that let quantum nodes share entanglement and keys.",
    "description": "Quantum Network Protocols is a public record about The rules that let quantum nodes share entanglement and keys. Quantum network protocols are the rules that let quantum nodes share entanglement, distribute keys and run distributed quantum computing. The protocols stack in layers: a physical layer that sends photons, a link layer that shares entanglement between neighbours, and a network layer that routes entanglement across the network. Routing entanglement is different from routing data, because entanglement is consumed when it is used, so the network must constantly create fresh entanglemen",
    "label": "quantum-cryptography-research-portal-000018",
    "figures": {
      "robots": 0,
      "nodes": 8,
      "links": 12,
      "rate_hz": 50,
      "layers": 3,
      "success_pct": 93
    }
  },
  {
    "title": "Satellite Quantum Key Distribution",
    "subject": "Sharing keys from space, where photons travel further.",
    "description": "Satellite Quantum Key Distribution is a public record about Sharing keys from space, where photons travel further. Satellite quantum key distribution sends keys from a satellite to ground stations, because photons travel through space with far less loss than through fibre. China's Micius satellite, launched in 2016, shared keys with ground stations over more than a thousand kilometres and ran video calls secured by quantum keys. A satellite passes over a ground station for only a few minutes, so the key exchange must be fast and the timing precise. Satellite QKD is the path to a global quantum",
    "label": "quantum-cryptography-research-portal-000019",
    "figures": {
      "robots": 0,
      "passes": 6,
      "key_bits": 256,
      "distance_km": 1200,
      "pass_min": 5,
      "success_pct": 94
    }
  },
  {
    "title": "Quantum Hacking and Side Channels",
    "subject": "How real QKD devices can be attacked, and how they are defended.",
    "description": "Quantum Hacking and Side Channels is a public record about How real QKD devices can be attacked, and how they are defended. Quantum hacking studies how real quantum key distribution devices can be attacked through their imperfections, such as detectors that can be blinded by bright light. Theory says QKD is secure, but real devices have flaws, and attackers exploit the gap between the theory and the hardware. Defences include monitoring the detectors, randomising settings and testing devices against known attacks before deployment. Quantum hacking is defensive research: it finds the flaws so t",
    "label": "quantum-cryptography-research-portal-000020",
    "figures": {
      "robots": 0,
      "attacks": 14,
      "blocked": 12,
      "open": 2,
      "devices": 4,
      "success_pct": 93
    }
  },
  {
    "title": "Quantum Secret Sharing",
    "subject": "Splitting a secret so only the whole group can rebuild it.",
    "description": "Quantum Secret Sharing is a public record about Splitting a secret so only the whole group can rebuild it. Quantum secret sharing splits a secret among several parties so that only the whole group, or a set threshold of them, can rebuild it, and no smaller group can learn anything. The secret is encoded in an entangled state shared among the parties, and the reconstruction needs the measurements of all the required parties together. Classical secret sharing does the same with mathematics, but quantum secret sharing adds protection against an attacker with a quantum computer. Secret sharing is ",
    "label": "quantum-cryptography-research-portal-000021",
    "figures": {
      "robots": 0,
      "parties": 5,
      "threshold": 3,
      "shares": 5,
      "rebuilds": 10,
      "success_pct": 95
    }
  },
  {
    "title": "Blind Quantum Computing",
    "subject": "Running a computation on a remote quantum computer without revealing it.",
    "description": "Blind Quantum Computing is a public record about Running a computation on a remote quantum computer without revealing it. Blind quantum computing lets a client run a computation on a remote quantum computer without the server learning the input, the program or the result. The client sends qubits prepared in secret states, and the server measures them as instructed, but the instructions hide what is being computed. The protocol was proposed by Anne Broadbent, Joseph Fitzsimons and Elham Kashefi in 2009, and it protects privacy for users of future quantum clouds. Blind computing matters because ",
    "label": "quantum-cryptography-research-portal-000022",
    "figures": {
      "robots": 0,
      "qubits": 50,
      "instructions": 200,
      "leaked_bits": 0,
      "rounds": 20,
      "success_pct": 93
    }
  },
  {
    "title": "Quantum Homomorphic Encryption",
    "subject": "Computing on encrypted data with quantum computers.",
    "description": "Quantum Homomorphic Encryption is a public record about Computing on encrypted data with quantum computers. Quantum homomorphic encryption lets a quantum computer process encrypted data without decrypting it, so the data stays secret even while it is being used. Classical homomorphic encryption does the same with ordinary computers, and the quantum version extends it to quantum data and quantum programs. The challenge is that quantum operations disturb the data, so the encryption must survive the computation and still decrypt correctly. Homomorphic encryption is used for private cloud computin",
    "label": "quantum-cryptography-research-portal-000023",
    "figures": {
      "robots": 0,
      "qubits": 40,
      "gates": 120,
      "overhead": 8,
      "checks": 10,
      "success_pct": 92
    }
  },
  {
    "title": "The Quantum Internet",
    "subject": "A future network that shares entanglement the way today's internet shares data.",
    "description": "The Quantum Internet is a public record about A future network that shares entanglement the way today's internet shares data. The quantum internet is a future network that shares entanglement between distant nodes, so quantum computers, sensors and key distribution can work together. It will be built in stages: first trusted-node key networks, then entanglement distribution, then quantum memories and repeaters, and finally full quantum computing networks. The quantum internet will not replace the classical internet: the two will run together, with classical links carrying control messages and ",
    "label": "quantum-cryptography-research-portal-000024",
    "figures": {
      "robots": 0,
      "nodes": 6,
      "distance_km": 500,
      "fidelity_pct": 90,
      "rate_hz": 20,
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
