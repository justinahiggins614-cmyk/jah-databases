#!/usr/bin/env node
/* Seeded boundless generator for persistent-digital-property-signature.
   Package-only. `node gen-persistent-digital-property-signature.js [seed]` prints one JSON record;
   `node gen-persistent-digital-property-signature.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "persistent-digital-property-signature";
const EDITION = "signature";
const RECORD_KIND = "persistent digital property record";
const ID_PREFIX = "JAH-PDPS-";
const GEN_PREFIX = "JAH-PDPSGEN-";
const AI_NAME = "JAH Persistent Digital Property Librarian (Signature)";
const SRC = "signature-generated";
const TOPICS = [["The Deed Chest", "A registry where every deed is kept in a chest with its key.", "In this design the property record is a deed kept in a chest: the chest holds the deed, the key is held by the owner, and the registry holds a copy of the lock. No deed can be changed without the key, and no key can be copied without the registry knowing. The design suits properties whose owners want their title to be as solid as paper.", {"chests": 240, "keys_held": 240, "locks_copied": 240, "deeds_changed": 0}], ["The Two Hands", "A transfer where buyer and seller shake hands over the record.", "In this design a transfer is two hands meeting over the record: the seller's hand gives, the buyer's hand takes, and the escrow holds the payment between them until both hands have met. The design suits transfers where trust matters and both sides want to see the moment ownership changes.", {"transfers": 96, "hands_met": 96, "payments_held": 96, "meetings_recorded": 96}], ["The Open Book", "A registry kept as an open book anyone may read.", "In this design the registry is an open book on a stand in the square: anyone may walk up, read any entry, and search by name, owner, kind, or place. The book is written in plain words and updated the same day a property changes. The design suits registries whose users believe openness is the best guard against fraud.", {"entries": 240, "readers_per_day": 120, "same_day_updates": 240, "complaints": 0}], ["The Fence Line", "A registry where boundaries are fences walked by neighbours.", "In this design the parcel map is a fence line: neighbours walk it together, agree where it runs, and mark it with stones. Where they disagree, the stones are painted red until the disagreement is settled. The design suits properties whose boundaries matter more than their contents.", {"parcels": 240, "stones_set": 238, "red_stones": 2, "walks": 12}], ["The Key and the Door", "A lease as a key lent for a time, returned when the time ends.", "In this design a lease is a key: the owner lends it, the tenant uses the door for the agreed time, and the key is returned when the time ends. The terms are written on a card tied to the key. The design suits leases where the return matters as much as the letting.", {"keys_lent": 48, "rent_payments": 576, "keys_returned": 48, "terms_broken": 3}], ["The Scales", "A valuation done on scales, with the working shown.", "In this design valuation is a set of scales: comparable sales on one side, income and cost on the other, and the value is where the scales balance -- shown as a range, never as a single weight. The design suits valuations where the buyer must be able to check the working.", {"valuations": 96, "weights_shown": 288, "ranges": 96, "single_weights": 0}], ["The Passing of the Torch", "An inheritance as a torch passed from hand to hand.", "In this design inheritance is a torch: the owner lights it, names who will carry it next, and when the owner dies the torch passes to the named hand. The passing is recorded, and the torch never goes out. The design suits families who want the passing to be certain and witnessed.", {"torches": 180, "passings": 12, "ownerless_torches": 0, "disputes": 0}], ["The Court of Two Chairs", "A dispute settled with both sides seated in two chairs.", "In this design a dispute is two chairs facing each other: both sides sit, state their case in plain words, and the record holds the evidence of both. The property is marked disputed until the chairs agree or a decision is made. The design suits disputes where fairness matters more than speed.", {"disputes": 14, "settlements": 12, "open_disputes": 2, "books_written": 12}], ["The Builder's Diary", "An improvement log kept as a diary by the owner.", "In this design the improvement log is a diary: every improvement is a page, with the date, the builder, and the cost, written by the owner as the work is done. The diary is shown to buyers before a sale. The design suits owners who take pride in what they built and want the buyer to know it.", {"diary_pages": 312, "removal_pages": 41, "diaries_shown": 96, "pages_faked": 0}], ["The Tax Box", "A ledger where every tax is a coin in a box.", "In this design the tax ledger is a box: every charge is a coin dropped in, every payment is a coin taken out, and the box is open so the owner can count what is owed. The design suits owners who want to see their taxes, not be surprised by them.", {"boxes": 240, "charge_coins": 720, "payment_coins": 684, "surprises": 0}], ["The Path Across", "An easement as a path worn across a field.", "In this design an easement is a path: it is worn by use, recorded with the property, and shown on the map so every buyer knows it is there. The path is walked, not just written. The design suits rights that are used daily and must be seen to be believed.", {"paths": 36, "walkers": 36, "endings": 4, "unrecorded_paths": 1}], ["The Family Album", "A property history kept as a family album.", "In this design provenance is an album: every owner is a photograph, every transfer a page, and the album is shown to buyers before a sale. Gaps are blank pages, labeled as gaps. The design suits properties whose story is part of their value.", {"albums": 240, "photographs": 240, "blank_pages": 3, "albums_shown": 96}], ["The Sealed Letter", "A deed as a sealed letter that only the right key opens.", "In this design the deed is a sealed letter: the property, the owner, and the date are written inside, the seal is a code made from the contents, and any change breaks the seal. The design suits deeds where a forgery must be visible at a glance.", {"letters": 240, "seals_checked": 240, "forgeries": 1, "glasses": 1}], ["The Third Hand", "An escrow as a third hand holding the payment.", "In this design escrow is a third hand: the buyer's hand gives the payment to the third hand, which holds it until the record shows the buyer's name, and only then passes it to the seller. The design suits transfers where neither side trusts the other yet, but both trust the third hand.", {"escrows": 96, "releases": 94, "returns": 2, "early_releases": 0}], ["The Inspector's Lens", "An inspection done through a lens that shows the truth.", "In this design inspection is a lens: the inspector looks through it at the property and sees what works, what is broken, and what is missing -- and the lens does not flatter. The report is written in plain words and given to the buyer before the sale. The design suits buyers who need the truth, not a sales talk.", {"inspections": 96, "defects_seen": 41, "repairs_priced": 41, "lenses": 4}], ["The Zone Map", "Zoning as a map coloured by use.", "In this design zoning is a coloured map: each area is coloured by what it may be used for, and the map hangs where every owner can read it. A property used against its colour is marked. The design suits areas where neighbours must know what to expect from each other.", {"zones": 8, "properties_coloured": 240, "violations": 5, "changes_announced": 2}], ["The Shared Table", "Fractional ownership as a table shared by many.", "In this design shared ownership is a table: each owner has a seat and a share, the agreement is the tablecloth, and decisions are made by the shares as the agreement says. The design suits properties owned together by people who must decide together.", {"tables": 24, "seats": 96, "agreements": 24, "share_sales": 12}], ["The Umbrella", "Insurance as an umbrella held over the property.", "In this design insurance is an umbrella: it is opened when the policy is bought, it covers the risks named on its ribs, and when rain falls -- loss, damage, theft -- the umbrella is what keeps the owner dry. The design suits owners who want to know exactly what is covered before the rain.", {"umbrellas": 96, "claims": 7, "claims_paid": 7, "premiums": 384}], ["The Lost and Found", "A registry office for properties whose owners vanished.", "In this design recovery is a lost-and-found office: properties whose owners cannot be found are brought here, the office searches every contact, waits, and posts a public notice. If the owner returns, the property is theirs again. The design suits registries that believe no property should be taken without a search and a notice.", {"properties_found": 8, "owners_returned": 6, "notices_posted": 8, "reassignments": 2}], ["The Travelling Chest", "A property that travels between worlds in a chest.", "In this design portability is a travelling chest: the property, its record, and its history are packed into the chest, the chest is carried to the new world, and unpacked only when the new world accepts it. The design suits properties that must move worlds without losing who they are.", {"moves": 12, "failures": 1, "histories_lost": 0, "worlds": 4}], ["The Shop Window", "A marketplace listing as a property in a shop window.", "In this design a listing is a shop window: the property is displayed with its description, its price, its history, and its inspection report, where every passer-by can judge it. A window that hides the defects is boarded up. The design suits markets where an honest window is the whole reputation.", {"windows": 41, "sales": 96, "boarded_windows": 2, "price_changes": 18}], ["The Magnifying Glass", "An audit done with a magnifying glass over every record.", "In this design the audit is a magnifying glass: the auditor holds it over a sample of every kind of record, compares each with its evidence, and publishes what the glass found. The design suits registries where trust is earned by being checked, not by asking to be believed.", {"records_examined": 240, "audits_per_year": 4, "frauds_found": 1, "fixes": 1}], ["The Spare Key", "A backup kept as a spare key to the whole registry.", "In this design the backup is a spare key: it is cut daily, kept apart from the registry, and tested monthly by opening a copy of the registry with it. The design suits registries where losing the record of who owns what would be the worst failure of all.", {"keys_cut": 365, "tests_per_year": 12, "uses": 1, "records_lost": 0}], ["The Fence Around the Registry", "A registry that knows its limits and fences them.", "In this design the registry's limits are a fence: measured, painted, and signed, and when a property would cross it, the registry says so plainly and offers a choice. The design suits registries whose keepers would rather be told no than silently drop a property.", {"properties_limit": 1000000, "owners_limit": 100000, "records_limit": 10000000, "silent_drops": 0}]];

function canon(v) {
  if (v === null || typeof v !== "object") return JSON.stringify(v);
  if (Array.isArray(v)) return "[" + v.map(canon).join(",") + "]";
  const keys = Object.keys(v).sort();
  return "{" + keys.map(k => JSON.stringify(k) + ":" + canon(v[k])).join(",") + "}";
}

function demoFor(figures) {
  const keys = Object.keys(figures).sort();
  const totalA = keys.reduce((a, k) => a + figures[k], 0);
  let totalB = 0;
  for (const k of keys) totalB += figures[k];
  const d1 = crypto.createHash("sha256").update(String(totalA)).digest("hex");
  const d2 = crypto.createHash("sha256").update(String(totalB)).digest("hex");
  return "total=" + totalA + "\ndigest_a=" + d1 + "\ndigest_b=" + d2 + "\nmatch=" + (d1 === d2) + "\n";
}

function makeRecord(seed) {
  const n = ((seed % 24) + 24) % 24;
  const t = TOPICS[n];
  const id = ID_PREFIX + String(n + 1).padStart(6, "0");
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: t[0],
    subject: t[1],
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: t[2],
    key_figures: t[3],
    demo: { code: "node demo: recomputes the figures twice and prints both SHA-256 digests" },
    expected_output: demoFor(t[3]),
    program: "RecordProgram with run() recomputing the same total and digest",
    sources: [{ name: "hashlib -- Python documentation", url: "https://docs.python.org/3/library/hashlib.html", retrieved: "2026-11-18", resource_id: "python-docs:hashlib" }],
    generator: { type: "seeded boundless generator", gen_id_prefix: GEN_PREFIX, hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI -- not stored files." },
    scales: { A1: "One record: " + t[0], A2: "The whole type: 24 records in the " + EDITION + " edition.", A3: "The type against the network." },
  };
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canon(rec)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function check(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = makeRecord(42), b = makeRecord(42), c = makeRecord(43);
  check("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  check("record_kind", a.record_kind === RECORD_KIND);
  check("slug form", a.slug === SLUG);
  check("id prefix", a.id.startsWith(ID_PREFIX));
  check("hard_stop 1000000000", a.generator.hard_stop === 1000000000);
  check("gen prefix", a.generator.gen_id_prefix === GEN_PREFIX);
  check("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = Object.assign({}, a); delete slim.jcc_key; delete slim.jcc_code;
  check("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canon(slim)).digest("hex").slice(0, 8));
  check("different seeds differ", JSON.stringify(a) !== JSON.stringify(c));
  check("19 keys", Object.keys(a).length >= 19);
  console.log(passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  if (process.argv[2] === "--test") { process.exit(runTests() ? 0 : 1); }
  const seed = parseInt(process.argv[2] || "1", 10);
  console.log(JSON.stringify(makeRecord(isNaN(seed) ? 1 : seed)));
}
module.exports = { makeRecord, runTests };
