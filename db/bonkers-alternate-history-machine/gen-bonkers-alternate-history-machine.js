// Alternate History Machine — boundless generator (FICTION: comedy concepts, not real)
var META = {"slug": "bonkers-alternate-history-machine", "title": "Alternate History Machine", "num4": "0838", "idp": "JAH-BON-", "bits": ["changes", "chosen", "historical", "event", "fictional", "simulation", "follows", "hypothetical", "consequences", "alternate", "history", "machine"], "tagline": "Changes a chosen historical event in a fictional simulation and follows the hypothetical consequences."};
var ARCH = [{"t": "Alternate History Machine — Concept Profile", "k": "concept profile", "b": "The Alternate History Machine is a comedy concept tool: a fully fictional instrument for doing changes in the most ridiculous way the laws of this pretend universe allow. Changes a chosen historical event in a fictional simulation and follows the hypothetical consequences. It was, in the fictional backstory of this database, dreamed up by an inventor who had unlimited coffee, a supercomputer, and absolutely no adult supervision. The core loop is simple to describe and impossible to justify: feed it ordinary inputs, and it performs chosen, historical, and event with complete confidence and zero scientific basis. This record is the concept profile: what the tool claims to do, the fictional principles it claims to run on, and the three things it absolutely refuses to do (apologize, be normal, or explain itself twice).", "caps": ["Simulates changes at comedic scale", "Generates fictional chosen artifacts", "Runs on pure narrative logic"]}, {"t": "Alternate History Machine — Flagship Build", "k": "flagship build", "b": "Meet the Mark-1 Alternate History: the flagship fictional build of the Alternate History Machine. The chassis is forged from recycled plot holes and reinforced with chosen alloy, rated for up to 7859 simultaneous historical events. Power comes from a triple-redundant event dynamo that spins exclusively on dramatic timing. In benchmark trials (fictional), the Mark-1 achieved 39% more changes than the leading real-world equivalent, mostly because the leading real-world equivalent refuses to participate. Included accessories: one (1) ceremonial lever, a laminated card explaining nothing, and a warranty that expires the moment you feel proud of yourself.", "caps": ["Produces absurd chosen specifications", "Benchmarks against fictional rivals", "Includes ceremonial lever"]}, {"t": "Alternate History Machine — Operator's Manual, Page 47", "k": "operator manual excerpt", "b": "Excerpt from the fictional operator's manual of the Alternate History Machine, page 47: \"Step 12: Before initiating changes, confirm that all chosen have been flattered. Step 13: If the device begins to historical on its own, this is normal; applaud briefly and continue. Step 14: Never operate the Alternate History while sober-minded, sleep-deprived, or within earshot of an actual engineer. Step 15: In the event of spontaneous event, evacuate the immediate area and file Form 27-B (Request for a Better Universe). Troubleshooting: if nothing happens, the unit is working. If something happens, the unit is working too hard.\"", "caps": ["Guides operators through changes rituals", "Handles spontaneous historical gracefully", "Never apologizes"]}, {"t": "Alternate History Machine — Field Report: First Week", "k": "field report", "b": "Fictional field report, week one of operating the Alternate History Machine in a controlled comedy environment. Day 1: operators successfully performed changes with only minor dignity loss. Day 3: an unexpected chosen surge caused the machine to historical for forty-five minutes straight; morale improved. Day 5: the team discovered the event compartment, which had been labeled \"do not\". Nobody opened it. Nobody needed to. Conclusion: the Alternate History performs exactly as specified in the brochure, which is to say, exactly as unspecified. Recommendation: deploy everywhere, apologize nowhere.", "caps": ["Documents chosen surges in the field", "Improves morale via chaos", "Files Form 27-B automatically"]}, {"t": "Alternate History Machine — Absurd Spec Sheet", "k": "spec sheet", "b": "Official fictional specifications of the Alternate History Machine, measured in units nobody asked for. Changes throughput: 7982 per fortnight, plus or minus one existential crisis. Chosen capacity: rated for twelve (12) fully grown regrets. Historical latency: 896 milliseconds, or instantly, whichever is funnier. Maximum event: do not exceed the red line; the red line is decorative, but do not exceed it anyway. Compatibility: works with all fictional operating systems, most dreams, and one specific toaster. Compliance: complies with all regulations of the Republic of Make-Believe, chapter 7982.", "caps": ["Measures changes in unasked-for units", "Rates regrets up to twelve", "Respects decorative red lines"]}, {"t": "Alternate History Machine — Frequently Unasked Questions", "k": "comedy FAQ", "b": "Q: Is the Alternate History Machine real? A: No. It is fiction, a comedy concept, and this database says so on every page, including this one. Q: Can I buy one? A: You can imagine one, which the warranty covers. Q: What does it do with changes? A: It chosens them, then historicals them, then denies everything. Q: Why does the Alternate History have a event port? A: The Alternate History is mysterious and needs no reason. Q: Is this safe? A: Safer than thinking about it too hard.", "caps": ["Answers unasked questions definitively", "Denies everything on request", "Covers imaginations under warranty"]}, {"t": "Alternate History Machine — Sample Output Run", "k": "sample output", "b": "One complete fictional run of the Alternate History Machine, captured for the archive. Input: a Tuesday, three (3) cups of coffee, and one changes. Processing: the machine chosened for eleven seconds, made a sound like historicaling in a canyon, and produced the following artifact: \"EVENT, BUT TINY AND TWICE AS DRAMATIC.\" Operators rated the output 14% bonkers, with a margin of error of pure chaos. The artifact was framed, hung in the fictional lobby, and has since chosened two interns. A triumph.", "caps": ["Captures complete fictional runs", "Frames artifacts for the lobby", "Rates bonkers percentage"]}, {"t": "Alternate History Machine — The Seven-Rung Ladder", "k": "ladder assessment", "b": "This record maps the Alternate History Machine onto the seven-rung generator ladder. Simple: the Alternate History makes changes jokes. Competitive: the Alternate History makes changes jokes FASTER than any rival chosen device. Mix-and-match: the Alternate History combines chosen with historical for unpredictable results. Unmade: a version of the Alternate History that was never built, because the blueprints kept eventing. Top-notch-or-better: the Alternate History, but it apologizes beautifully afterward. Future-grade: the Alternate History, from the year 2149, where it is legally a citizen. God-mode: the Alternate History achieves full changes enlightenment and retires to a beach.", "caps": ["Maps concepts onto seven ladder rungs", "Retires tools to beaches at god-mode", "Enlightens changes"]}];
var HARD_CAP = 1000000000000000;
function bonkersPrng(seed){ var s = seed >>> 0; return function(){ s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
function bonkersRun(seed){
  var rnd = bonkersPrng(seed);
  function pick(a){ return a[Math.floor(rnd() * a.length)]; }
  var chaos = (Math.floor(rnd() * 900) + 100) / 10;
  var widgets = Math.floor(rnd() * 9999) + 1;
  var line = 'Unit ' + widgets + ': ' + pick(META.bits) + ' collided with ' + pick(META.bits) + ' during routine ' + pick(META.bits) + ' maintenance.';
  return { fiction: 'FICTION - comedy concept, not real', simulator: META.title, seed: seed, event: line, chaos_index: chaos, widgets_deployed: widgets };
}
function demoProgram(seed){
  return '// ' + META.title + ' — comedy simulation demo (FICTION: not real, for laughs only)\n' +
  'var BONKERS_NAME = ' + JSON.stringify(META.title) + ';\n' +
  'var BONKERS_BITS = ' + JSON.stringify(META.bits) + ';\n' +
  'function bonkersPrng(seed){ var s = seed >>> 0; return function(){ s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }\n' +
  'function bonkersRun(seed){\n' +
  '  var rnd = bonkersPrng(seed);\n' +
  '  function pick(a){ return a[Math.floor(rnd() * a.length)]; }\n' +
  '  var chaos = (Math.floor(rnd() * 900) + 100) / 10;\n' +
  '  var widgets = Math.floor(rnd() * 9999) + 1;\n' +
  '  var line = \'Unit \' + widgets + \': \' + pick(BONKERS_BITS) + \' collided with \' + pick(BONKERS_BITS) + \' during routine \' + pick(BONKERS_BITS) + \' maintenance.\';\n' +
  '  return { fiction: \'FICTION - comedy concept, not real\', simulator: BONKERS_NAME, seed: seed, event: line, chaos_index: chaos, widgets_deployed: widgets };\n' +
  '}\nconsole.log(JSON.stringify(bonkersRun(' + seed + ')));';
}
function generate(seed, opts){
  seed = seed >>> 0;
  var a = ARCH[seed % ARCH.length];
  var out = bonkersRun(seed);
  var ladder = ['simple','competitive','mix-and-match','unmade','top-notch-or-better','future-grade','god-mode'];
  return {
    id: META.idp + META.num4 + '-gen-' + seed,
    title: a.t, description: 'Generated run (seed ' + seed + '): ' + META.tagline, body: a.b,
    capabilities: a.caps,
    demo: { program: demoProgram(seed), output: JSON.stringify(out), language: 'javascript', runtime: 'node' },
    fiction: true, fiction_label: 'FICTION — comedy concept, not real',
    provenance: 'Signature-comedy original, generated by jahdb-' + META.slug + '-1.0.',
    licensing: 'Property of Justin Addam Higgins (JAH). Comedy concept; not a real product.',
    src: 'signature-generated-completion', edition: 'signature', built_by: 'assistant',
    record_kind: 'bonkers comedy concept record', ladder_rank: ladder[seed % ladder.length],
    generator: 'jahdb-' + META.slug + '-1.0', verification_status: 'generated',
    links: { database_page: 'https://justinahiggins614-cmyk.github.io/jah-databases/db/' + META.slug + '/' }
  };
}
function validate(r){
  var errors = [];
  if (!r || typeof r !== 'object') errors.push('not an object');
  else {
    if (r.fiction !== true) errors.push('fiction must be true');
    if (!r.demo || !r.demo.program) errors.push('missing demo program');
    if (!r.demo || !r.demo.output) errors.push('missing demo output');
    if (!r.id || String(r.id).indexOf(META.idp) !== 0) errors.push('bad id prefix');
    if (!r.title) errors.push('missing title');
  }
  return { ok: errors.length === 0, errors: errors };
}
function main(){
  var n = 8, seed = 1;
  var argv = (typeof process !== 'undefined' && process.argv) ? process.argv : [];
  for (var i = 0; i < argv.length; i++){
    if (argv[i] === '--n' && argv[i+1]) n = parseInt(argv[i+1], 10);
    if (argv[i] === '--seed' && argv[i+1]) seed = parseInt(argv[i+1], 10);
  }
  if (n > HARD_CAP) { console.error('refused: exceeds hard cap 10^15'); if (typeof process !== 'undefined') process.exit(1); return; }
  for (var j = 0; j < n; j++) console.log(JSON.stringify(generate(seed + j, {})));
}
if (typeof process !== 'undefined' && process.argv && process.argv[1] && process.argv[1].indexOf('gen-') >= 0) main();
if (typeof window !== 'undefined' && window.JAHDB && JAHDB.registerGenerator) JAHDB.registerGenerator(META.slug, { generate: generate, validate: validate });
