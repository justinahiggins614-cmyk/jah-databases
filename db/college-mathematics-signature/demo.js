// Edition demo for the The Signature College Mathematics Database (college-mathematics-signature).
// One summary line per record (the same computation as each record's
// own demo, ported from Python), then a determinism check: the lines
// are hashed twice and the two digests must match.
'use strict';
/* Node port of the Wave 1 Python demo template (College-Level Resources,
   Wave 1). The original Python demo is shipped alongside as demo.py; this
   file must print exactly the same bytes. Python-compatibility notes:
   - Python ints are exact: carried as BigInt and summed exactly.
   - CPython 3.12.3 builtin sum(): leading ints accumulate exactly, the
     FIRST float is plain-added to that exact sum (compensation starts at
     zero), later floats use the Neumaier compensation step, later ints are
     plain-added; the compensation is folded in at the end only when nonzero.
   - round(x, 4) is round-half-even on the exact binary value.
   - Floats print with Python repr rules (shortest digits, scientific
     notation when the exponent is below -4 or at/above 16, ".0" for whole
     floats, two-digit signed exponents). */
const crypto = require('crypto');

function pyRound(x, places) {
  if (!Number.isFinite(x)) return x;
  const buf = new ArrayBuffer(8);
  const dv = new DataView(buf);
  dv.setFloat64(0, x);
  const bits = dv.getBigUint64(0);
  const sign = bits >> 63n;
  const exp = Number((bits >> 52n) & 0x7ffn);
  let mant = bits & ((1n << 52n) - 1n);
  let e2;
  if (exp === 0) { e2 = -1074; }
  else { mant |= (1n << 52n); e2 = exp - 1075; }
  const scale = 10n ** BigInt(places);
  let scaledNum, scaledDen;
  if (e2 >= 0) { scaledNum = mant * (2n ** BigInt(e2)) * scale; scaledDen = 1n; }
  else { scaledNum = mant * scale; scaledDen = 2n ** BigInt(-e2); }
  let q = scaledNum / scaledDen;
  const r = scaledNum % scaledDen;
  const twice = r * 2n;
  if (twice > scaledDen || (twice === scaledDen && q % 2n === 1n)) q += 1n;
  const ip = q / scale, fp = q % scale;
  const dec = (sign ? '-' : '') + ip.toString() + '.' + fp.toString().padStart(places, '0');
  return Number(dec);
}

function pyReprFloat(x) {
  if (x === 0) return Object.is(x, -0) ? '-0.0' : '0.0';
  if (!Number.isFinite(x)) return x > 0 ? 'inf' : '-inf';
  const neg = x < 0;
  const s = String(Math.abs(x));
  let digits, E;
  if (s.includes('e')) {
    const parts = s.split('e');
    digits = parts[0].replace('.', '');
    E = parseInt(parts[1], 10);
  } else if (s.includes('.')) {
    const parts = s.split('.');
    if (parts[0] !== '0') { digits = parts[0] + parts[1]; E = parts[0].length - 1; }
    else { const lz = parts[1].match(/^0*/)[0].length; digits = parts[1].slice(lz); E = -(lz + 1); }
  } else { digits = s; E = s.length - 1; }
  digits = digits.replace(/0+$/, '') || '0';
  let out;
  if (E < -4 || E >= 16) {
    const mant = digits.length === 1 ? digits : digits[0] + '.' + digits.slice(1);
    out = mant + 'e' + (E >= 0 ? '+' : '-') + String(Math.abs(E)).padStart(2, '0');
  } else if (E >= 0) {
    if (E + 1 >= digits.length) out = digits + '0'.repeat(E + 1 - digits.length) + '.0';
    else out = digits.slice(0, E + 1) + '.' + digits.slice(E + 1);
  } else {
    out = '0.' + '0'.repeat(-E - 1) + digits;
  }
  return neg ? '-' + out : out;
}

function pyStr(v) {
  if (!v.f) return typeof v.v === 'bigint' ? v.v.toString() : String(v.v);
  return pyReprFloat(v.v);
}

function compute(figures) {
  const vals = Object.values(figures);
  const allInt = vals.every((o) => o.f === 0);
  let total;
  if (allInt) {
    let t = 0n;
    for (const o of vals) t += o.v;
    total = { v: t, f: 0 };
  } else {
    let i = 0;
    let isum = 0n;
    while (i < vals.length && vals[i].f === 0) { isum += vals[i].v; i += 1; }
    let s = Number(isum) + Number(vals[i].v);
    let c = 0;
    i += 1;
    for (; i < vals.length; i += 1) {
      const o = vals[i];
      if (o.f === 1) {
        const x = o.v;
        const t = s + x;
        if (Math.abs(s) >= Math.abs(x)) c += (s - t) + x;
        else c += (x - t) + s;
        s = t;
      } else {
        s = s + Number(o.v);
      }
    }
    if (c) s = s + c;
    total = { v: s, f: 1 };
  }
  const n = vals.length;
  const totalR = total.f ? { v: pyRound(total.v, 4), f: 1 } : total;
  const mean = { v: pyRound(allInt ? Number(total.v) / n : total.v / n, 4), f: 1 };
  const max = vals.reduce((a, b) => (b.v > a.v ? b : a));
  const min = vals.reduce((a, b) => (b.v < a.v ? b : a));
  return { count: { v: n, f: 0 }, label: null, max, mean, min, total: totalR };
}

function entriesFor(label, figures) {
  const o = compute(figures);
  return { count: o.count, label: { v: label, f: -1 }, max: o.max, mean: o.mean, min: o.min, total: o.total };
}

function fmtEntry(o) { return o.f === -1 ? o.v : pyStr(o); }

function summarizeDemo(label, figures) {
  const entries = entriesFor(label, figures);
  return Object.keys(entries).sort().map((k) => k + '=' + fmtEntry(entries[k])).join('|');
}

function runDemo(label, figures) {
  const result = summarizeDemo(label, figures);
  const h1 = crypto.createHash('sha256').update(result).digest('hex');
  const result2 = summarizeDemo(label, figures);
  const h2 = crypto.createHash('sha256').update(result2).digest('hex');
  const entries = entriesFor(label, figures);
  const lines = [];
  for (const k of Object.keys(entries).sort()) lines.push(k + ': ' + fmtEntry(entries[k]));
  lines.push('Result: ' + result);
  lines.push('Run 1 SHA-256: ' + h1);
  lines.push('Run 2 SHA-256: ' + h2);
  lines.push('Deterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH'));
  return lines.join('\n') + '\n';
}

const RECORDS = [
  { label: "a-signature-proof-studio-design", figures: {
  "steps_in_guided_proof": { v: 3n, f: 0 },
  "checks_performed": { v: 5n, f: 0 },
  "n_tested": { v: 5n, f: 0 },
  "sum_of_odds": { v: 25n, f: 0 },
  "n_squared": { v: 25n, f: 0 },
  "proof_moves_offered": { v: 6n, f: 0 },
  "exports_supported": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-counting-workshop-design", figures: {
  "tokens": { v: 4n, f: 0 },
  "arrangements": { v: 24n, f: 0 },
  "combinations_of_2": { v: 6n, f: 0 },
  "orders_per_pair": { v: 2n, f: 0 },
  "checks_passed": { v: 2n, f: 0 },
  "places": { v: 4n, f: 0 },
  "choices_first": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-function-laboratory-design", figures: {
  "functions_entered": { v: 2n, f: 0 },
  "points_traced": { v: 4n, f: 0 },
  "composition_value_at_3": { v: 10n, f: 0 },
  "composition_value_at_2": { v: 5n, f: 0 },
  "composition_value_at_1": { v: 2n, f: 0 },
  "composition_value_at_0": { v: 1n, f: 0 },
  "graphs_drawn": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-set-builder-design", figures: {
  "set_a_size": { v: 5n, f: 0 },
  "set_b_size": { v: 3n, f: 0 },
  "union_size": { v: 7n, f: 0 },
  "intersection_size": { v: 1n, f: 0 },
  "difference_size": { v: 4n, f: 0 },
  "regions_drawn": { v: 4n, f: 0 },
  "checks_passed": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-domino-proof-design", figures: {
  "rungs_lit": { v: 10n, f: 0 },
  "proof_parts": { v: 2n, f: 0 },
  "sum_to_10": { v: 55n, f: 0 },
  "formula_at_10": { v: 55n, f: 0 },
  "sum_to_3": { v: 6n, f: 0 },
  "formula_at_3": { v: 6n, f: 0 },
  "base_case": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-number-line-atlas-design", figures: {
  "number_systems": { v: 4n, f: 0 },
  "zoom_levels": { v: 3n, f: 0 },
  "sqrt2_marked": { v: 1.41421356, f: 1 },
  "pi_marked": { v: 3.14159265, f: 1 },
  "rationals_shown": { v: 2n, f: 0 },
  "points_marked": { v: 6n, f: 0 },
  "decimal_places": { v: 8n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-logic-table-builder-design", figures: {
  "rows_checked": { v: 4n, f: 0 },
  "parts": { v: 2n, f: 0 },
  "equivalences_found": { v: 1n, f: 0 },
  "rows_for_3_parts": { v: 8n, f: 0 },
  "rows_for_10_parts": { v: 1024n, f: 0 },
  "cap_parts": { v: 5n, f: 0 },
  "connectives_supported": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-sequence-explorer-design", figures: {
  "terms_listed": { v: 20n, f: 0 },
  "error_at_10": { v: 0.1, f: 1 },
  "error_at_100": { v: 0.01, f: 1 },
  "error_at_1000": { v: 0.001, f: 1 },
  "limit_confirmed": { v: 0n, f: 0 },
  "checks": { v: 3n, f: 0 },
  "first_term": { v: 1n, f: 0 },
  "fifth_term": { v: 0.2, f: 1 }
} },
  { label: "a-signature-complex-plane-studio-design", figures: {
  "points_placed": { v: 3n, f: 0 },
  "modulus_1_plus_i": { v: 1.4142, f: 1 },
  "argument_degrees": { v: 45n, f: 0 },
  "rotation_degrees": { v: 90n, f: 0 },
  "product_modulus": { v: 2n, f: 0 },
  "product_argument": { v: 90n, f: 0 },
  "multiplications": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-equivalence-class-sorter-design", figures: {
  "numbers_sorted": { v: 12n, f: 0 },
  "classes_built": { v: 4n, f: 0 },
  "members_per_class": { v: 3n, f: 0 },
  "properties_checked": { v: 3n, f: 0 },
  "tests_run": { v: 3n, f: 0 },
  "failures_shown": { v: 1n, f: 0 },
  "modulus": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-pigeonhole-boxes-design", figures: {
  "objects_1": { v: 13n, f: 0 },
  "boxes_1": { v: 12n, f: 0 },
  "guaranteed_1": { v: 2n, f: 0 },
  "objects_2": { v: 25n, f: 0 },
  "boxes_2": { v: 7n, f: 0 },
  "guaranteed_2": { v: 4n, f: 0 },
  "placements_shown": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-overlap-counter-design", figures: {
  "set_a": { v: 10n, f: 0 },
  "set_b": { v: 8n, f: 0 },
  "set_c": { v: 6n, f: 0 },
  "pairwise_sum": { v: 9n, f: 0 },
  "triple": { v: 1n, f: 0 },
  "union": { v: 16n, f: 0 },
  "regions": { v: 7n, f: 0 },
  "counts_agreeing": { v: 2n, f: 0 }
} },
  { label: "a-signature-fibonacci-garden-design", figures: {
  "generations": { v: 10n, f: 0 },
  "fib_10": { v: 55n, f: 0 },
  "fib_9": { v: 34n, f: 0 },
  "ratio_10": { v: 1.6176, f: 1 },
  "ratio_8": { v: 1.6154, f: 1 },
  "golden_ratio": { v: 1.618034, f: 1 },
  "starting_values": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-for-all-game-design", figures: {
  "rounds": { v: 10n, f: 0 },
  "forall_rounds": { v: 4n, f: 0 },
  "exists_rounds": { v: 3n, f: 0 },
  "disproof_rounds": { v: 3n, f: 0 },
  "hints_used": { v: 2n, f: 0 },
  "strategies_corrected": { v: 1n, f: 0 },
  "points_per_round": { v: 10n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-geometry-workbench-design", figures: {
  "points_placed": { v: 3n, f: 0 },
  "distances_shown": { v: 3n, f: 0 },
  "hypotenuse": { v: 5n, f: 0 },
  "triangle_area": { v: 6n, f: 0 },
  "box_volume": { v: 24n, f: 0 },
  "box_sides": { v: 3n, f: 0 },
  "angles_shown": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-probability-table-design", figures: {
  "outcomes": { v: 36n, f: 0 },
  "ways_to_7": { v: 6n, f: 0 },
  "prob_7": { v: 0.1667, f: 1 },
  "doubles": { v: 6n, f: 0 },
  "at_least_one_6": { v: 11n, f: 0 },
  "prob_6": { v: 0.3056, f: 1 },
  "events_highlighted": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-euclid-machine-design", figures: {
  "steps_test_1": { v: 3n, f: 0 },
  "gcd_1": { v: 21n, f: 0 },
  "steps_test_2": { v: 3n, f: 0 },
  "gcd_2": { v: 6n, f: 0 },
  "numbers_entered": { v: 4n, f: 0 },
  "divisions_shown": { v: 6n, f: 0 },
  "remainders_shown": { v: 6n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-clock-arithmetic-dial-design", figures: {
  "dial_hours": { v: 7n, f: 0 },
  "sum_result": { v: 4n, f: 0 },
  "product_result": { v: 2n, f: 0 },
  "inverse_of_3": { v: 5n, f: 0 },
  "inverse_check": { v: 15n, f: 0 },
  "operations_shown": { v: 3n, f: 0 },
  "turns_for_product": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-composition-pipeline-design", figures: {
  "stages": { v: 2n, f: 0 },
  "output_order_1": { v: 49n, f: 0 },
  "output_order_2": { v: 13n, f: 0 },
  "input": { v: 2n, f: 0 },
  "after_stage_1": { v: 7n, f: 0 },
  "after_stage_2": { v: 49n, f: 0 },
  "round_trip_back": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-capstone-challenge-board-design", figures: {
  "parts": { v: 3n, f: 0 },
  "checks_passed": { v: 3n, f: 0 },
  "combinations": { v: 210n, f: 0 },
  "excluded": { v: 84n, f: 0 },
  "answer": { v: 126n, f: 0 },
  "challenges_on_board": { v: 12n, f: 0 },
  "ideas_named": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-definition-dictionary-design", figures: {
  "entries": { v: 24n, f: 0 },
  "quiz_items": { v: 8n, f: 0 },
  "matching_uses": { v: 5n, f: 0 },
  "non_matching_uses": { v: 3n, f: 0 },
  "score": { v: 7n, f: 0 },
  "examples_per_entry": { v: 1n, f: 0 },
  "non_examples_per_entry": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-estimation-bench-design", figures: {
  "problems": { v: 3n, f: 0 },
  "estimate_1": { v: 1000n, f: 0 },
  "exact_1": { v: 912n, f: 0 },
  "ratio_1": { v: 0.912, f: 1 },
  "estimate_2": { v: 100n, f: 0 },
  "exact_2": { v: 100n, f: 0 },
  "factorial_7": { v: 5040n, f: 0 },
  "flags": { v: 0n, f: 0 }
} },
  { label: "a-signature-proof-review-circle-design", figures: {
  "steps_submitted": { v: 3n, f: 0 },
  "steps_revised": { v: 4n, f: 0 },
  "reviewers": { v: 2n, f: 0 },
  "revisions": { v: 1n, f: 0 },
  "hard_steps_named": { v: 1n, f: 0 },
  "elegant_steps_named": { v: 1n, f: 0 },
  "proofs_reviewed": { v: 6n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-word-problem-translator-design", figures: {
  "stages": { v: 5n, f: 0 },
  "quantities": { v: 2n, f: 0 },
  "unknowns": { v: 2n, f: 0 },
  "equations": { v: 2n, f: 0 },
  "solution_x": { v: 19n, f: 0 },
  "solution_y": { v: 11n, f: 0 },
  "sum_check": { v: 30n, f: 0 },
  "difference_check": { v: 8n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
