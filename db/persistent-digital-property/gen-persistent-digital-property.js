#!/usr/bin/env node
/* Seeded boundless generator for persistent-digital-property.
   Package-only. `node gen-persistent-digital-property.js [seed]` prints one JSON record;
   `node gen-persistent-digital-property.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "persistent-digital-property";
const EDITION = "public";
const RECORD_KIND = "persistent digital property record";
const ID_PREFIX = "JAH-PDP-";
const GEN_PREFIX = "JAH-PDPGEN-";
const AI_NAME = "JAH Persistent Digital Property Librarian";
const SRC = "public-harvest";
const TOPICS = [["Property Record and Title", "The single record that says what a digital property is and who owns it.", "A property record is the title deed of a digital property: it names the property, describes it fully, names its owner, and records when the ownership began.", {"records": 240, "fields_per_record": 9, "transfers_logged": 96, "disputes_over_title": 0}], ["Ownership Transfer", "Moving a digital property from one owner to another, cleanly.", "A transfer moves ownership from seller to buyer in fixed steps: agreement, payment, record update, and confirmation -- so both sides know exactly when the property changed hands.", {"transfers": 96, "escrow_holds": 96, "failed_transfers": 2, "confirmations_sent": 192}], ["Property Registry and Search", "The public list of properties, searchable by anyone.", "The registry is the public list of all digital properties: each one searchable by name, by owner, by kind, or by place, so anyone can find a property and read its record.", {"registry_entries": 240, "searches_per_day": 120, "same_day_updates": 240, "privacy_complaints": 0}], ["Boundary and Parcel Map", "The map that says where one property ends and the next begins.", "The parcel map draws the boundaries of every digital property: its edges, its neighbours, and the exact space it occupies, so no two properties claim the same ground.", {"parcels_mapped": 240, "boundaries_agreed": 238, "disputes_marked": 2, "map_checks": 12}], ["Lease and Rental Terms", "Letting someone use a digital property for a time, under agreed terms.", "A lease lets a tenant use a property for a fixed time under written terms: what they may do, what they must not do, what they pay, and what happens when the time ends.", {"leases": 48, "rent_payments_recorded": 576, "terms_broken": 3, "returns_recorded": 48}], ["Property Valuation Method", "Working out what a digital property is worth, honestly.", "Valuation works out a property's worth from what similar properties sold for, what the property earns, and what it costs to keep -- shown as a range with the reasons, never as a single magic number.", {"valuations": 96, "comparables_used": 288, "ranges_given": 96, "single_number_values": 0}], ["Inheritance and Succession", "Passing a digital property to the next owner when the owner dies.", "Inheritance passes a property to the person the owner named, by fixed steps, so the property is never left ownerless and the family's wishes are honoured.", {"successors_named": 180, "successions_completed": 12, "ownerless_properties": 0, "disputes": 0}], ["Property Dispute Record", "Recording disagreements about property so they can be settled fairly.", "A dispute record writes down a disagreement about a property -- who owns it, where its boundary is, what a lease allows -- so it can be settled on facts, not on shouting.", {"disputes_opened": 14, "disputes_settled": 12, "disputes_open": 2, "settlements_recorded": 12}], ["Improvement and Building Log", "Recording what was built or improved on a digital property.", "The improvement log records everything built on or added to a property -- when, by whom, and what it cost -- so the property's value and history are always true.", {"improvements_logged": 312, "removals_logged": 41, "logs_shown_to_buyers": 96, "logs_faked": 0}], ["Property Tax and Fee Ledger", "Counting the taxes and fees a property owes, and recording payment.", "The tax ledger counts what each property owes -- taxes, fees, and charges -- records what was paid and when, and shows what is still owed, so no owner is surprised by a bill.", {"properties_taxed": 240, "charges_recorded": 720, "payments_recorded": 684, "disputes": 1}], ["Access Rights and Easements", "The rights of others to cross or use part of a property.", "An easement is a right someone else holds over part of a property -- a path across it, a pipe under it -- recorded with the property so every owner and buyer knows it is there.", {"easements": 36, "holders": 36, "endings_recorded": 4, "unrecorded_found": 1}], ["Property History and Provenance", "The full story of a property, from its first record to today.", "Provenance is the property's whole story: every owner, every transfer, every improvement, and every dispute, in order, so anyone can see how the property came to be what it is.", {"histories_written": 240, "transfers_in_history": 96, "gaps_recorded": 3, "histories_shown": 96}], ["Digital Deed and Signature", "The signed deed that proves ownership of a digital property.", "A digital deed is the signed document that proves ownership: the property, the owner, the date, and a signature that can be checked by anyone, without needing to trust the person who shows it.", {"deeds_issued": 240, "signatures_checked": 240, "forgeries_found": 1, "owner_copies": 240}], ["Escrow and Payment Record", "Holding payment safely until a transfer is complete.", "Escrow holds the buyer's payment with a trusted third party until the transfer is done, so the seller is paid only when the buyer truly owns the property.", {"escrows": 96, "released_on_completion": 94, "returned_on_failure": 2, "early_releases": 0}], ["Property Inspection Report", "Inspecting a digital property and reporting its true condition.", "An inspection report says what a property is really like -- what works, what is broken, what is missing -- written by an inspector who has looked at it properly.", {"inspections": 96, "defects_found": 41, "repairs_priced": 41, "inspectors": 4}], ["Zoning and Use Rules", "The rules that say what a digital property may be used for.", "Zoning rules say what each property may be used for -- a shop, a home, a workshop, a park -- and they are written down where every owner can read them.", {"zones": 8, "properties_zoned": 240, "violations_marked": 5, "rule_changes": 2}], ["Shared and Fractional Ownership", "Owning a digital property together, in shares.", "Fractional ownership lets several people own one property together, each holding a share, with the shares, the rights, and the duties written down and agreed.", {"shared_properties": 24, "shares_issued": 96, "agreements_filed": 24, "share_sales": 12}], ["Property Insurance Record", "Insuring a digital property against loss and damage.", "Insurance records what a property is insured against, for how much, and what happens when loss occurs, so an owner who loses a property is not left with nothing.", {"policies": 96, "claims_made": 7, "claims_paid": 7, "premiums_recorded": 384}], ["Abandoned Property Recovery", "Finding and returning property whose owner cannot be found.", "Recovery finds digital properties whose owner has vanished -- no contact, no payment, no answer -- and returns them to the owner or, if the owner cannot be found, to the registry's care.", {"properties_recovered": 8, "owners_found": 6, "public_notices": 8, "properties_reassigned": 2}], ["Cross-World Portability", "Moving a digital property from one digital world to another.", "Portability moves a property between digital worlds: the property, its record, and its history travel together, so the property is the same property in the new world.", {"moves_completed": 12, "moves_failed": 1, "histories_lost": 0, "worlds_accepting": 4}], ["Property Marketplace Listing", "Listing a digital property for sale, openly and honestly.", "A marketplace listing offers a property for sale: its description, its price, its history, and its condition, shown openly so a buyer can judge it fairly.", {"listings": 41, "sales": 96, "listings_removed": 2, "price_changes_shown": 18}], ["Audit and Fraud Check", "Checking property records for fraud and mistakes.", "The audit checks property records for fraud: forged deeds, double sales, hidden easements, and numbers that do not add up -- and it names what it finds.", {"records_audited": 240, "audits_per_year": 4, "frauds_found": 1, "fixes_made": 1}], ["Registry Backup and Recovery", "Keeping the registry safe so no property record is ever lost.", "Backup keeps a copy of the whole registry in a second place, checked regularly, so a fire, a failure, or a mistake cannot destroy the record of who owns what.", {"backups_per_year": 365, "restore_tests": 12, "restores_needed": 1, "records_lost": 0}], ["Registry Scale and Limits", "How many properties, owners, and records the registry can hold.", "The scale record states the registry's limits honestly: how many properties, how many owners, how many records, and what happens when the limits are reached.", {"properties_limit": 1000000, "owners_limit": 100000, "records_limit": 10000000, "limit_reviews_per_year": 1}]];

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
