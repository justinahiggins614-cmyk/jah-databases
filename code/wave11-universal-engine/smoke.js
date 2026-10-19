// Wave-11 generator smoke test.
// usage: node smoke.js <genfile>
// Generates seeds, validates, drift-checks, and emits the demo programs
// so the Python build can machine-execute them.
(function(){
'use strict';
var path = process.argv[2];
var g = require(path);
var out = [];
[1, 2, 3].forEach(function(seed){
  var r = g.generate(seed, {});
  var v = g.validate(r);
  var d = g.driftCheck(r, []);
  out.push({
    seed: seed,
    ok: !!(v.ok && d.ok),
    errors: (v.errors || []).concat(d.errors || []),
    id: r.id,
    title: r.title,
    demo: r.demo && r.demo.program
  });
});
// field-pinning path
try {
  var rf = g.generate(7, {field: g.fields[0]});
  out.push({fieldPin: rf.field === g.fields[0], ok: rf.field === g.fields[0], seed: 7});
} catch(e){ out.push({fieldPin: false, ok: false, seed: 7, errors: [String(e)]}); }
// determinism path: same seed twice must match
try {
  var a = g.generate(42, {}), b = g.generate(42, {});
  var same = a.title === b.title && a.id === b.id && a.demo.program === b.demo.program;
  out.push({deterministic: same, ok: same, seed: 42});
} catch(e){ out.push({deterministic: false, ok: false, seed: 42, errors: [String(e)]}); }
console.log(JSON.stringify(out));
})();
