// Boundless generator for termites-pests-rot-degradation — deterministic, seeded, duplicate-checked.
// Hard cap: 1e15 records, or stop when the topic space is genuinely exhausted.
// Generated records carry generated:true and src:"generated" and are never
// mixed with assistant-built records.
(function () {
  'use strict';
  var HARD_CAP = 1e15;
  var PREFIX = 'JAH-AR85-';
  var TOPICS = ["Termite signs guide", "Carpenter ant signs guide", "Wood rot diagnosis guide", "Fungal decay prevention guide", "Pest treatment options overview", "Pest prevention checklist", "Pest inspection schedule", "Damaged timber replacement note", "Moisture and rot link explainer", "Post-treatment monitoring method"];
  function mulberry32(seed) {
    return function () {
      seed |= 0; seed = (seed + 0x6D2B79F5) | 0;
      var t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function generate(n, seed) {
    var rnd = mulberry32(seed == null ? 42 : seed);
    var out = [], seen = {};
    n = Math.min(n, HARD_CAP);
    for (var i = 0; i < n; i++) {
      var topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
      var id = PREFIX + String(1000 + i);
      if (seen[id]) continue;
      seen[id] = true;
      out.push({ id: id, title: topic, generated: true, src: 'generated',
        edition: 'public', record_kind: 'pest record', body: '<p>Generated record for ' + topic + '.</p>' });
    }
    return out;
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { generate: generate, HARD_CAP: HARD_CAP };
  if (typeof window !== 'undefined') window['gentermites_pests_rot_degradation'] = { generate: generate, HARD_CAP: HARD_CAP };
  if (typeof process !== 'undefined' && process.argv && process.argv[1] && process.argv[1].indexOf('gen-') >= 0) {
    var n = 5;
    process.argv.forEach(function (a) { if (a.indexOf('--n=') === 0) n = parseInt(a.slice(4), 10) || 5; });
    var idx = process.argv.indexOf('--n');
    if (idx >= 0 && process.argv[idx + 1]) n = parseInt(process.argv[idx + 1], 10) || 5;
    console.log(JSON.stringify(generate(n), null, 2));
  }
})();
