#!/usr/bin/env node
/* JAH Databases — demo-engine execution test.
 * Builds demos for representative records through every kind path and
 * ACTUALLY EXECUTES each generated JavaScript program in a vm sandbox.
 * Any throw (ReferenceError, SyntaxError, ...) fails the test.
 * Regression guard for: solution display text ("x = 4") treated as code.
 */
'use strict';
var vm = require('vm');
var path = require('path');
var D = require(path.join(__dirname, '..', '..', 'core', 'jahdb-demo.js'));

var failures = [];
function fail(msg) { failures.push(msg); }
function execOK(label, program) {
  try {
    var n = 0;
    var sandbox = { console: {
      log: function () { if (++n > 2000) throw new Error('output cap'); },
      warn: function () {}, error: function () {}, info: function () {}
    }};
    vm.runInNewContext('"use strict";\n' + program, sandbox, { timeout: 2000 });
  } catch (e) {
    fail(label + ' THREW: ' + e.constructor.name + ': ' + e.message);
  }
}
function checkBuild(label, slug, rec, expect) {
  var d;
  try { d = D.build(slug, rec); }
  catch (e) { fail(label + ': build() threw: ' + e.message); return; }
  if (expect.kind && d.kind !== expect.kind)
    fail(label + ': expected kind ' + expect.kind + ', got ' + d.kind);
  if (expect.notKind && d.kind === expect.notKind)
    fail(label + ': must NOT take kind ' + expect.notKind + ' (got it)');
  if (!d.runnable) fail(label + ': demo not marked runnable');
  if ((d.language || 'javascript') === 'javascript') execOK(label + ' [kind=' + d.kind + ']', d.program);
  else if (typeof d.program !== 'string' || !d.program.length) fail(label + ': empty non-JS program');
  return d;
}

/* 1. Equation record: solution is DISPLAY TEXT — must never take the code path. */
checkBuild('equation/solution-text', 'equations', {
  id: 'JAH-EQ-00000001', title: 'Solve 2x + 3 = 11', type: 'linear',
  equation: '2x + 3 = 11',
  steps: ['2x + 3 = 11', '2x = 11 − 3 = 8', 'x = 8 / 2 = 4'],
  solution: 'x = 4', check: 'Substitute x = 4 ✓'
}, { notKind: 'code' });

/* 2. Record with real JavaScript code in `code` field — must stay a code demo. */
var dCode = checkBuild('real-js-code', 'code-database', {
  id: 'C-1', title: 'Adder', language: 'javascript',
  code: 'function add(a,b){return a+b;}\nconsole.log("sum="+add(2,3));'
}, { kind: 'code' });

/* 3. Genuine multi-line code stored in a `solution` field still detected. */
checkBuild('real-code-in-solution', 'code-problems', {
  id: 'CP-1', title: 'FizzBuzz',
  solution: 'function fizzbuzz(n){\n  var o=[];\n  for(var i=1;i<=n;i++){\n    o.push(i%15===0?"FizzBuzz":i%3===0?"Fizz":i%5===0?"Buzz":i);\n  }\n  return o;\n}\nconsole.log(fizzbuzz(5).join(","));'
}, { kind: 'code' });

/* 4. Text-heavy record — read/explore demo, must execute. */
checkBuild('long-text', 'essays', {
  id: 'T-1', title: 'On Engines',
  body: ('The engine turns fuel into motion. ' +
         'Every part has a purpose and a limit. ').repeat(40)
}, {});

/* 5. Numbers record — chart path. */
checkBuild('numbers', 'benchmarks', {
  id: 'N-1', title: 'Latency runs', p50: 12, p90: 31, p99: 88, samples: 1000
}, {});

/* 6. Steps record — simulate path. */
checkBuild('steps', 'recipes', {
  id: 'S-1', title: 'Bake bread',
  steps: ['Mix flour and water', 'Knead ten minutes', 'Bake at 220C for 30 minutes']
}, {});

/* 7. Python record — program carried, not executed here. */
var dPy = checkBuild('python-code', 'code-database', {
  id: 'P-1', title: 'Hello', language: 'python',
  code: 'def greet(n):\n    return "hi " + n\nprint(greet("jah"))'
}, {});
if (dPy && dPy.language !== 'python') fail('python-code: expected language python, got ' + dPy.language);

/* 8. Forced-kind path still guarded by the smoke test in Node. */
var dForced = D.buildKind('equations', {
  id: 'JAH-EQ-00000002', title: 'Solve x + 1 = 2', equation: 'x + 1 = 2',
  steps: ['x + 1 = 2', 'x = 1'], solution: 'x = 1'
}, 'code');
if ((dForced.language || 'javascript') === 'javascript')
  execOK('forced-code-kind [kind=' + dForced.kind + ']', dForced.program);

if (failures.length) {
  console.error('DEMO ENGINE TEST: FAIL (' + failures.length + ')');
  failures.forEach(function (f) { console.error('  - ' + f); });
  process.exit(1);
}
console.log('DEMO ENGINE TEST: PASS (8 scenarios, every JS program executed cleanly)');
