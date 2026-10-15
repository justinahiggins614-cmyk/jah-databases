#!/usr/bin/env node
/* Regen helper: run a fixed gen-*.js under Node, emit candidates as JSON.
   Usage: node regen-one.js <gen-js-path> <n-seeds>
   Sets global.window={} shim. Outputs JSON array of {seed, ok, errors, record}. */
global.window = {};
const fs = require('fs');
const path = process.argv[2];
const n = parseInt(process.argv[3], 10) || 50;
const src = fs.readFileSync(path, 'utf-8');
// Run the gen file with shadowed module/window so its exports land where we can read them.
const fakeModule = {exports: {}};
const fakeWindow = {};
new Function('module', 'window', src)(fakeModule, fakeWindow);
let api = null;
const key = Object.keys(fakeWindow).find(k => k.indexOf('jahdb_') === 0);
if (key) api = fakeWindow[key];
if (!api && fakeModule.exports && fakeModule.exports.generate) api = fakeModule.exports;
if (!api && typeof JAHDB !== 'undefined' && JAHDB.getGenerator) {
  // fallback: try common slug derivation from filename
  const m = /gen-(.+)\.js$/.exec(path);
  if (m) api = JAHDB.getGenerator(m[1]);
}
if (!api) { console.error('no generator api found in ' + path); process.exit(1); }
const out = [];
for (let seed = 1; seed <= n; seed++) {
  try {
    const r = api.generate(seed, {});
    const v = api.validate(r);
    const ok = v && (v.ok === true || v === true);
    const errors = v && v.errors ? v.errors : (ok ? [] : ['validate failed']);
    out.push({seed, ok, errors, record: ok ? r : null});
  } catch (e) {
    out.push({seed, ok: false, errors: [String(e && e.message || e)], record: null});
  }
}
process.stdout.write(JSON.stringify(out));
