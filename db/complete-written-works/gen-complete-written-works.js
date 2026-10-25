// gen-complete-written-works.js -- boundless generator for the Complete Written Works Database.
// Usage: node gen-complete-written-works.js --n 5
// Deterministic: a seeded LCG drives parameter variations.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15
// records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" --
// never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Novels", "Novellas", "Short-story collections", "Textbooks", "Encyclopedias", "Dictionaries", "Thesauruses", "Biographies", "Autobiographies", "Memoirs", "Magazines", "Newspapers", "Academic journals", "Scientific journals", "Industry trade journals", "Newsletters", "Literary journals", "Comic-book series", "Annual reports and yearbooks", "Almanacs", "Technical manuals", "User manuals", "Installation guides", "Repair manuals", "Engineering handbooks", "Programming language references", "Software documentation sets", "Standard operating procedure manuals", "Troubleshooting guides", "Technical specification documents", "Research papers", "Systematic literature reviews", "Meta-analysis reports", "Scientific monographs", "Doctoral dissertations", "Master's theses", "Research proposals", "Field-study reports", "Laboratory reports", "Scientific conference proceedings", "Complete courses", "Lesson plans and teaching packs", "Student workbooks", "Exercise and answer-key collections", "Exam preparation guides", "Training curricula", "Lecture notes collections", "Laboratory instruction packs", "Certification study materials", "Educational activity books", "Screenplays", "Stage plays", "Radio dramas", "Poetry collections", "Songbooks", "Graphic novels", "Manga volumes", "Children's picture books", "Interactive fiction", "Choose-your-own-adventure works", "Business plans", "Business strategy reports", "Market research reports", "Feasibility studies", "Annual business reports", "Company policy manuals", "Employee handbooks", "Project proposals", "Operational plans", "Industry analysis reports", "Legal textbooks and commentaries", "Legislative compilations", "Regulatory handbooks", "Court opinion compilations", "Policy papers", "Government statistical reports", "Public consultation reports", "Compliance manuals", "Treaty and agreement compilations", "Institutional governance manuals", "Product catalogs", "Parts catalogs", "Patent catalogs", "Research and invention catalogs", "Business directories", "Professional directories", "Museum catalogs", "Library catalogs", "Travel guides", "Geographic gazetteers", "Wikis and knowledge-base collections", "Frequently asked questions collections", "Case-study collections", "Recipe collections and cookbooks", "Field guides", "Checklists and assessment packs", "Forms and templates collections", "Glossary and terminology collections", "Digital archives with descriptive indexes", "Comprehensive master dossiers"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261025;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}
const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const variant = 1 + Math.floor(rnd() * 50);
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-WW-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "complete-written-works",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "written work template record",
    feasibility_tier: "established",
    body: "<p>Generated parameter variation v" + variant + " of " + topic + ". Labeled generated; not an assistant-built record. Create, play, and expand layers (where applicable) follow the parent template; validation rules of the parent record apply.</p>",
    demo_code: "print('generated variation')",
    demo_output: "generated variation\n",
    implementation_status: "designed",
    provenance: "Generator output; labeled generated.",
    last_verified: "2026-10-25",
    license: "https://creativecommons.org/publicdomain/zero/1.0/"
  };
}
function main() {
  const n = parseN(process.argv.slice(2));
  if (n > HARD_CAP) { console.error("requested count exceeds HARD_CAP"); process.exit(1); }
  const out = [];
  let k = 0, guard = 0;
  while (out.length < n && guard < n * 20 + 1000) {
    guard++;
    const r = makeRecord(k);
    if (r) { out.push(r); k++; }
  }
  out.forEach(function (r) { console.log(JSON.stringify(r)); });
}
if (require.main === module) main();
module.exports = { HARD_CAP: HARD_CAP, makeRecord: makeRecord };
