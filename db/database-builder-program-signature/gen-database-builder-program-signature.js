// Seeded boundless generator for the The Signature Database Builder Database database.
// Pair: database-builder-program-signature (signature edition). Hard stop: 1000000000 outputs per file.
// Outputs are generated on demand, never stored. Deterministic: the same
// seed always gives the same output. Throttle: 100 outputs per call.
"use strict";
const SLUG = "database-builder-program-signature";
const PREFIX = "JAH-DBBP-S-";
const HARD_STOP = 1000000000;
const THROTTLE = 100;

function nextRand(state) {
  // Linear congruential generator; state is a 32-bit integer.
  state = (state * 1103515245 + 12345) % 2147483648;
  return state;
}

function generate(seed, count) {
  if (!Number.isInteger(seed)) throw new Error("seed must be an integer");
  if (!Number.isInteger(count) || count < 0) throw new Error("count must be a non-negative integer");
  if (count > THROTTLE) throw new Error("throttle: at most " + THROTTLE + " outputs per call");
  if (count > HARD_STOP) throw new Error("hard stop: 1000000000 outputs per file");
  let state = (seed >>> 0) || 1;
  const out = [];
  for (let i = 0; i < count; i++) {
    state = nextRand(state);
    out.push({ id: PREFIX + "GEN-" + String(i + 1).padStart(6, "0"),
               seed: seed, value: state, slug: SLUG });
  }
  return out;
}

function runTests() {
  const a = generate(42, 5), b = generate(42, 5);
  if (JSON.stringify(a) !== JSON.stringify(b)) throw new Error("not deterministic");
  if (generate(42, 0).length !== 0) throw new Error("empty run failed");
  if (generate(7, 5)[0].slug !== SLUG) throw new Error("wrong slug");
  if (generate(7, 5)[0].id.indexOf(PREFIX + "GEN-") !== 0) throw new Error("wrong id prefix");
  let throttled = false;
  try { generate(1, THROTTLE + 1); } catch (e) { throttled = String(e.message).indexOf("throttle") === 0; }
  if (!throttled) throw new Error("throttle not enforced");
  return "PASS: deterministic, empty run ok, slug and prefix ok, throttle enforced";
}

if (require.main === module) {
  console.log(runTests());
  console.log(JSON.stringify(generate(42, 3), null, 2));
}

module.exports = { generate, runTests, SLUG, PREFIX, HARD_STOP, THROTTLE };
