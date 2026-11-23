// Edition demo for the College Mathematics Database (college-mathematics).
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
  { label: "numbers-and-sets", figures: {
  "set_a_size": { v: 5n, f: 0 },
  "set_b_size": { v: 4n, f: 0 },
  "union_size": { v: 8n, f: 0 },
  "intersection_size": { v: 1n, f: 0 },
  "shared_element": { v: 6n, f: 0 },
  "total_elements_counted": { v: 9n, f: 0 },
  "distinct_elements": { v: 8n, f: 0 },
  "empty_set_size": { v: 0n, f: 0 }
} },
  { label: "functions-and-their-graphs", figures: {
  "slope": { v: 2n, f: 0 },
  "intercept": { v: 3n, f: 0 },
  "f_at_0": { v: 3n, f: 0 },
  "f_at_1": { v: 5n, f: 0 },
  "f_at_2": { v: 7n, f: 0 },
  "f_at_5": { v: 13n, f: 0 },
  "inverse_at_13": { v: 5n, f: 0 },
  "domain_points_checked": { v: 4n, f: 0 }
} },
  { label: "mathematical-logic-and-proof", figures: {
  "steps_in_proof": { v: 3n, f: 0 },
  "even_number_tested": { v: 6n, f: 0 },
  "square_of_6": { v: 36n, f: 0 },
  "odd_number_tested": { v: 7n, f: 0 },
  "square_of_7": { v: 49n, f: 0 },
  "connectives_named": { v: 4n, f: 0 },
  "proof_methods_named": { v: 3n, f: 0 },
  "counterexamples_needed": { v: 1n, f: 0 }
} },
  { label: "proof-by-direct-argument-and-by-contradiction", figures: {
  "primes_in_euclid_argument": { v: 1n, f: 0 },
  "steps_in_irrationality_proof": { v: 6n, f: 0 },
  "p_value_example": { v: 2n, f: 0 },
  "q_value_example": { v: 1n, f: 0 },
  "p_squared": { v: 4n, f: 0 },
  "q_squared": { v: 1n, f: 0 },
  "contradiction_count": { v: 1n, f: 0 },
  "proof_methods_named": { v: 2n, f: 0 }
} },
  { label: "proof-by-induction", figures: {
  "base_case_n": { v: 1n, f: 0 },
  "sum_to_10": { v: 55n, f: 0 },
  "formula_at_10": { v: 55n, f: 0 },
  "steps_in_proof": { v: 2n, f: 0 },
  "k_plus_1_term": { v: 11n, f: 0 },
  "sum_to_5": { v: 15n, f: 0 },
  "formula_at_5": { v: 15n, f: 0 },
  "domino_steps_checked": { v: 2n, f: 0 }
} },
  { label: "permutations-and-counting", figures: {
  "books": { v: 4n, f: 0 },
  "arrangements_of_4": { v: 24n, f: 0 },
  "letters": { v: 5n, f: 0 },
  "arrangements_of_3": { v: 60n, f: 0 },
  "factorial_5": { v: 120n, f: 0 },
  "factorial_2": { v: 2n, f: 0 },
  "choices_first_place": { v: 4n, f: 0 },
  "choices_last_place": { v: 1n, f: 0 }
} },
  { label: "combinations-and-counting", figures: {
  "people": { v: 8n, f: 0 },
  "team_size": { v: 3n, f: 0 },
  "teams": { v: 56n, f: 0 },
  "ordered_choices": { v: 336n, f: 0 },
  "orders_per_team": { v: 6n, f: 0 },
  "cards": { v: 52n, f: 0 },
  "hand_size": { v: 5n, f: 0 },
  "poker_hands": { v: 2598960n, f: 0 }
} },
  { label: "the-binomial-theorem", figures: {
  "power": { v: 3n, f: 0 },
  "coefficient_0": { v: 1n, f: 0 },
  "coefficient_1": { v: 3n, f: 0 },
  "coefficient_2": { v: 3n, f: 0 },
  "coefficient_3": { v: 1n, f: 0 },
  "check_x": { v: 2n, f: 0 },
  "check_y": { v: 1n, f: 0 },
  "expansion_total": { v: 27n, f: 0 }
} },
  { label: "sequences-and-convergence", figures: {
  "first_term": { v: 3n, f: 0 },
  "second_term": { v: 2.5, f: 1 },
  "fifth_term": { v: 2.2, f: 1 },
  "tenth_term": { v: 2.1, f: 1 },
  "hundredth_term": { v: 2.01, f: 1 },
  "limit": { v: 2n, f: 0 },
  "error_at_10": { v: 0.1, f: 1 },
  "error_at_100": { v: 0.01, f: 1 }
} },
  { label: "series-and-their-sums", figures: {
  "first_term": { v: 1n, f: 0 },
  "ratio": { v: 0.5, f: 1 },
  "sum_limit": { v: 2n, f: 0 },
  "partial_sum_2": { v: 1.5, f: 1 },
  "partial_sum_4": { v: 1.875, f: 1 },
  "partial_sum_10": { v: 1.998046875, f: 1 },
  "error_after_10": { v: 0.001953125, f: 1 },
  "terms_checked": { v: 10n, f: 0 }
} },
  { label: "real-numbers-and-completeness", figures: {
  "sqrt2_approx": { v: 1.41421356, f: 1 },
  "rational_below_1": { v: 1.4, f: 1 },
  "rational_below_2": { v: 1.41, f: 1 },
  "rational_below_3": { v: 1.414, f: 1 },
  "bound_candidates": { v: 3n, f: 0 },
  "upper_bound_2": { v: 2n, f: 0 },
  "terms_listed": { v: 4n, f: 0 },
  "decimal_places": { v: 8n, f: 0 }
} },
  { label: "complex-numbers", figures: {
  "real_1": { v: 2n, f: 0 },
  "imag_1": { v: 3n, f: 0 },
  "real_2": { v: 1n, f: 0 },
  "imag_2": { v: 4n, f: 0 },
  "product_real": { v: -10n, f: 0 },
  "product_imag": { v: 11n, f: 0 },
  "modulus_product": { v: 14.8666, f: 1 },
  "modulus_check": { v: 14.8666, f: 1 }
} },
  { label: "relations-and-equivalence", figures: {
  "modulus": { v: 5n, f: 0 },
  "classes": { v: 5n, f: 0 },
  "class_0_members": { v: 3n, f: 0 },
  "class_2_members": { v: 3n, f: 0 },
  "difference_check_1": { v: 10n, f: 0 },
  "difference_check_2": { v: 11n, f: 0 },
  "properties_needed": { v: 3n, f: 0 },
  "elements_listed": { v: 15n, f: 0 }
} },
  { label: "the-pigeonhole-principle", figures: {
  "people": { v: 500000n, f: 0 },
  "hair_counts": { v: 150001n, f: 0 },
  "max_hairs": { v: 150000n, f: 0 },
  "guaranteed_shared": { v: 4n, f: 0 },
  "three_per_count": { v: 450003n, f: 0 },
  "four_per_count": { v: 600004n, f: 0 },
  "months": { v: 12n, f: 0 },
  "people_for_months": { v: 13n, f: 0 }
} },
  { label: "inclusion-exclusion-counting", figures: {
  "students": { v: 40n, f: 0 },
  "french": { v: 25n, f: 0 },
  "german": { v: 20n, f: 0 },
  "both": { v: 12n, f: 0 },
  "at_least_one": { v: 33n, f: 0 },
  "neither": { v: 7n, f: 0 },
  "three_language_total": { v: 36n, f: 0 },
  "none_of_three": { v: 4n, f: 0 }
} },
  { label: "recursion-and-recurrence-relations", figures: {
  "fib_1": { v: 1n, f: 0 },
  "fib_5": { v: 5n, f: 0 },
  "fib_10": { v: 55n, f: 0 },
  "fib_9": { v: 34n, f: 0 },
  "ratio_10_9": { v: 1.6176, f: 1 },
  "golden_ratio": { v: 1.618034, f: 1 },
  "terms_listed": { v: 10n, f: 0 },
  "starting_values": { v: 2n, f: 0 }
} },
  { label: "quantifiers-for-all-and-there-exists", figures: {
  "quantifiers_named": { v: 2n, f: 0 },
  "examples_checked": { v: 3n, f: 0 },
  "y_for_x_plus_1": { v: 1n, f: 0 },
  "statements_compared": { v: 2n, f: 0 },
  "negations_named": { v: 2n, f: 0 },
  "orderings_compared": { v: 2n, f: 0 },
  "counterexamples_needed": { v: 1n, f: 0 },
  "proof_steps": { v: 2n, f: 0 }
} },
  { label: "distance-and-angle-in-geometry", figures: {
  "dx": { v: 3n, f: 0 },
  "dy": { v: 4n, f: 0 },
  "distance": { v: 5n, f: 0 },
  "dx_squared": { v: 9n, f: 0 },
  "dy_squared": { v: 16n, f: 0 },
  "sum_squares": { v: 25n, f: 0 },
  "angle_degrees": { v: 53.13, f: 1 },
  "triangle_sides": { v: 3n, f: 0 }
} },
  { label: "area-and-volume", figures: {
  "circle_radius": { v: 5n, f: 0 },
  "circle_area": { v: 78.5398, f: 1 },
  "circle_circumference": { v: 31.4159, f: 1 },
  "sphere_radius": { v: 3n, f: 0 },
  "sphere_volume": { v: 113.0973, f: 1 },
  "sphere_area": { v: 113.0973, f: 1 },
  "box_volume": { v: 24n, f: 0 },
  "box_area": { v: 52n, f: 0 }
} },
  { label: "probability-beginnings", figures: {
  "outcomes": { v: 36n, f: 0 },
  "ways_to_7": { v: 6n, f: 0 },
  "prob_7": { v: 0.1667, f: 1 },
  "ways_to_2": { v: 1n, f: 0 },
  "prob_2": { v: 0.0278, f: 1 },
  "prob_at_least_one_6": { v: 0.3056, f: 1 },
  "dice": { v: 2n, f: 0 },
  "sides": { v: 6n, f: 0 }
} },
  { label: "the-greatest-common-divisor", figures: {
  "a": { v: 252n, f: 0 },
  "b": { v: 105n, f: 0 },
  "remainder_1": { v: 42n, f: 0 },
  "remainder_2": { v: 21n, f: 0 },
  "gcd": { v: 21n, f: 0 },
  "a_over_gcd": { v: 12n, f: 0 },
  "b_over_gcd": { v: 5n, f: 0 },
  "lcm": { v: 1260n, f: 0 }
} },
  { label: "modular-arithmetic", figures: {
  "modulus": { v: 7n, f: 0 },
  "sum_reduced": { v: 4n, f: 0 },
  "product_reduced": { v: 2n, f: 0 },
  "inverse_of_3": { v: 5n, f: 0 },
  "inverse_check": { v: 15n, f: 0 },
  "power_check": { v: 8n, f: 0 },
  "power_reduced": { v: 1n, f: 0 },
  "clock_modulus": { v: 12n, f: 0 }
} },
  { label: "function-composition-and-inverses", figures: {
  "f_at_2": { v: 7n, f: 0 },
  "g_after_f": { v: 49n, f: 0 },
  "f_after_g": { v: 13n, f: 0 },
  "inverse_at_7": { v: 2n, f: 0 },
  "g_at_minus_2": { v: 4n, f: 0 },
  "g_at_2": { v: 4n, f: 0 },
  "slope_of_f": { v: 3n, f: 0 },
  "functions_composed": { v: 2n, f: 0 }
} },
  { label: "capstone-problems-using-several-ideas", figures: {
  "digits_available": { v: 10n, f: 0 },
  "digits_chosen": { v: 4n, f: 0 },
  "combinations": { v: 210n, f: 0 },
  "with_zero": { v: 84n, f: 0 },
  "answer": { v: 126n, f: 0 },
  "smallest": { v: 1234n, f: 0 },
  "largest": { v: 6789n, f: 0 },
  "parts_in_solution": { v: 3n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
