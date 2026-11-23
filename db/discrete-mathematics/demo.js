// Edition demo for the Discrete Mathematics Database (discrete-mathematics).
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
  { label: "propositional-logic", figures: {
  "rows_checked": { v: 4n, f: 0 },
  "equivalences_shown": { v: 2n, f: 0 },
  "connectives_named": { v: 5n, f: 0 },
  "tautology_rows": { v: 4n, f: 0 },
  "truth_values": { v: 2n, f: 0 },
  "statements_compared": { v: 2n, f: 0 },
  "laws_named": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 }
} },
  { label: "predicate-logic-and-quantifiers", figures: {
  "examples_checked": { v: 3n, f: 0 },
  "quantifiers_named": { v: 2n, f: 0 },
  "negations_named": { v: 2n, f: 0 },
  "orderings_compared": { v: 2n, f: 0 },
  "proof_steps": { v: 2n, f: 0 },
  "counterexamples_needed": { v: 1n, f: 0 },
  "integers_tested": { v: 3n, f: 0 },
  "checks": { v: 3n, f: 0 }
} },
  { label: "sets-functions-and-relations-in-discrete-mathematics", figures: {
  "function_value": { v: 10n, f: 0 },
  "inverse_value": { v: 5n, f: 0 },
  "properties_checked": { v: 2n, f: 0 },
  "sets_compared": { v: 2n, f: 0 },
  "pairs_named": { v: 3n, f: 0 },
  "relation_types": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 },
  "integers_tested": { v: 1n, f: 0 }
} },
  { label: "proof-by-induction-in-discrete-mathematics", figures: {
  "base_case": { v: 2n, f: 0 },
  "n_factored": { v: 12n, f: 0 },
  "prime_factors": { v: 3n, f: 0 },
  "steps_in_proof": { v: 2n, f: 0 },
  "induction_forms": { v: 3n, f: 0 },
  "cases_in_step": { v: 2n, f: 0 },
  "checks": { v: 1n, f: 0 },
  "factors_of_12": { v: 3n, f: 0 }
} },
  { label: "the-product-and-sum-rules-for-counting", figures: {
  "strings_total": { v: 17576n, f: 0 },
  "start_vowel": { v: 3380n, f: 0 },
  "end_vowel": { v: 3380n, f: 0 },
  "both_vowel": { v: 650n, f: 0 },
  "union": { v: 6110n, f: 0 },
  "neither": { v: 11466n, f: 0 },
  "alphabet_size": { v: 26n, f: 0 },
  "vowels": { v: 5n, f: 0 }
} },
  { label: "permutations-and-combinations", figures: {
  "committees": { v: 120n, f: 0 },
  "chair_choices": { v: 3n, f: 0 },
  "total_ways": { v: 360n, f: 0 },
  "method_2_chairs": { v: 10n, f: 0 },
  "method_2_others": { v: 36n, f: 0 },
  "poker_hands": { v: 2598960n, f: 0 },
  "people": { v: 10n, f: 0 },
  "committee_size": { v: 3n, f: 0 }
} },
  { label: "the-pigeonhole-principle", figures: {
  "points": { v: 5n, f: 0 },
  "boxes": { v: 4n, f: 0 },
  "max_distance": { v: 0.7071, f: 1 },
  "small_square_side": { v: 0.5, f: 1 },
  "diagonal": { v: 0.7071, f: 1 },
  "months": { v: 12n, f: 0 },
  "people_for_months": { v: 13n, f: 0 },
  "guaranteed": { v: 2n, f: 0 }
} },
  { label: "inclusion-exclusion-in-discrete-mathematics", figures: {
  "divisible_by_2": { v: 50n, f: 0 },
  "divisible_by_3": { v: 33n, f: 0 },
  "divisible_by_6": { v: 16n, f: 0 },
  "union": { v: 67n, f: 0 },
  "neither": { v: 33n, f: 0 },
  "blocks": { v: 16n, f: 0 },
  "per_block": { v: 4n, f: 0 },
  "remainder_qualifying": { v: 3n, f: 0 }
} },
  { label: "graphs-and-their-basics", figures: {
  "vertices": { v: 6n, f: 0 },
  "degree_sum": { v: 10n, f: 0 },
  "edges": { v: 5n, f: 0 },
  "odd_degree_vertices": { v: 4n, f: 0 },
  "tree_edges": { v: 5n, f: 0 },
  "complete_graph_vertices": { v: 5n, f: 0 },
  "complete_graph_edges": { v: 10n, f: 0 },
  "complete_degree": { v: 4n, f: 0 }
} },
  { label: "eulerian-and-hamiltonian-paths", figures: {
  "konigsberg_vertices": { v: 4n, f: 0 },
  "odd_degrees_konigsberg": { v: 4n, f: 0 },
  "square_odd_vertices": { v: 2n, f: 0 },
  "square_vertices": { v: 4n, f: 0 },
  "square_edges": { v: 5n, f: 0 },
  "hamiltonian_vertices": { v: 4n, f: 0 },
  "degrees_konigsberg": { v: 3n, f: 0 },
  "bridges": { v: 7n, f: 0 }
} },
  { label: "trees-in-graph-theory", figures: {
  "offices": { v: 8n, f: 0 },
  "cables_needed": { v: 7n, f: 0 },
  "labelled_trees": { v: 262144n, f: 0 },
  "binary_tree_levels": { v: 4n, f: 0 },
  "binary_tree_vertices": { v: 15n, f: 0 },
  "edges_in_tree": { v: 7n, f: 0 },
  "paths_between_vertices": { v: 1n, f: 0 },
  "cayley_exponent": { v: 6n, f: 0 }
} },
  { label: "recurrence-relations", figures: {
  "a_0": { v: 1n, f: 0 },
  "a_1": { v: 3n, f: 0 },
  "a_2": { v: 7n, f: 0 },
  "root_1": { v: 1n, f: 0 },
  "root_2": { v: 2n, f: 0 },
  "constant_a": { v: -1n, f: 0 },
  "constant_b": { v: 2n, f: 0 },
  "terms_checked": { v: 3n, f: 0 }
} },
  { label: "generating-functions", figures: {
  "ways_to_make_change": { v: 4n, f: 0 },
  "coins_used": { v: 3n, f: 0 },
  "amount": { v: 10n, f: 0 },
  "coefficient": { v: 4n, f: 0 },
  "generating_terms": { v: 3n, f: 0 },
  "denominations": { v: 3n, f: 0 },
  "fives_used_max": { v: 2n, f: 0 },
  "checks": { v: 1n, f: 0 }
} },
  { label: "number-theory-and-divisibility", figures: {
  "n_factored": { v: 360n, f: 0 },
  "prime_2_power": { v: 3n, f: 0 },
  "prime_3_power": { v: 2n, f: 0 },
  "prime_5_power": { v: 1n, f: 0 },
  "divisor_count": { v: 24n, f: 0 },
  "primes_used": { v: 3n, f: 0 },
  "check_product": { v: 360n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "modular-arithmetic-and-cryptography", figures: {
  "modulus": { v: 7n, f: 0 },
  "sum_reduced": { v: 4n, f: 0 },
  "product_reduced": { v: 2n, f: 0 },
  "inverse_of_3": { v: 5n, f: 0 },
  "rsa_n": { v: 55n, f: 0 },
  "rsa_e": { v: 3n, f: 0 },
  "rsa_d": { v: 27n, f: 0 },
  "ciphertext": { v: 13n, f: 0 }
} },
  { label: "boolean-algebra", figures: {
  "truth_table_rows": { v: 4n, f: 0 },
  "ones_in_table": { v: 2n, f: 0 },
  "terms_in_dnf": { v: 2n, f: 0 },
  "simplified_terms": { v: 2n, f: 0 },
  "variables": { v: 2n, f: 0 },
  "checks": { v: 4n, f: 0 },
  "laws_named": { v: 3n, f: 0 },
  "gates_named": { v: 3n, f: 0 }
} },
  { label: "the-pigeonhole-principle-in-algorithms", figures: {
  "slots": { v: 100n, f: 0 },
  "items": { v: 150n, f: 0 },
  "average_load": { v: 1.5, f: 1 },
  "guaranteed_collision": { v: 2n, f: 0 },
  "files_100bit": { v: 2n, f: 0 },
  "shorter_files": { v: 1n, f: 0 },
  "bits": { v: 100n, f: 0 },
  "checks": { v: 2n, f: 0 }
} },
  { label: "graph-colouring", figures: {
  "pentagon_vertices": { v: 5n, f: 0 },
  "chromatic_number": { v: 3n, f: 0 },
  "colours_tried": { v: 2n, f: 0 },
  "complete_graph_vertices": { v: 4n, f: 0 },
  "complete_chromatic": { v: 4n, f: 0 },
  "map_colours": { v: 4n, f: 0 },
  "theorem_year": { v: 1976n, f: 0 },
  "clique_size": { v: 4n, f: 0 }
} },
  { label: "derangements", figures: {
  "derangements_4": { v: 9n, f: 0 },
  "permutations_4": { v: 24n, f: 0 },
  "fraction_4": { v: 0.375, f: 1 },
  "derangements_5": { v: 44n, f: 0 },
  "permutations_5": { v: 120n, f: 0 },
  "fraction_5": { v: 0.3667, f: 1 },
  "limit_fraction": { v: 0.3679, f: 1 },
  "sum_terms": { v: 5n, f: 0 }
} },
  { label: "induction-for-graphs", figures: {
  "base_vertices": { v: 1n, f: 0 },
  "base_edges": { v: 0n, f: 0 },
  "tree_5_edges": { v: 4n, f: 0 },
  "tree_8_edges": { v: 7n, f: 0 },
  "leaf_degree": { v: 1n, f: 0 },
  "steps_in_proof": { v: 2n, f: 0 },
  "paths_endpoints": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 }
} },
  { label: "binary-relations-and-partial-orders", figures: {
  "elements": { v: 4n, f: 0 },
  "comparable_pairs": { v: 5n, f: 0 },
  "reflexive_pairs": { v: 4n, f: 0 },
  "maximal_elements": { v: 1n, f: 0 },
  "maximum": { v: 6n, f: 0 },
  "chains": { v: 2n, f: 0 },
  "levels": { v: 3n, f: 0 },
  "properties": { v: 3n, f: 0 }
} },
  { label: "counting-with-generating-functions", figures: {
  "ways_n5": { v: 6n, f: 0 },
  "ways_n10": { v: 11n, f: 0 },
  "fib_5": { v: 5n, f: 0 },
  "coefficient_formula": { v: 6n, f: 0 },
  "terms_shown": { v: 4n, f: 0 },
  "sequences_encoded": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 },
  "n_tested": { v: 5n, f: 0 }
} },
  { label: "the-euclidean-algorithm-and-bezout-s-identity", figures: {
  "gcd": { v: 21n, f: 0 },
  "coefficient_105": { v: 5n, f: 0 },
  "coefficient_252": { v: -2n, f: 0 },
  "check_525": { v: 525n, f: 0 },
  "check_504": { v: 504n, f: 0 },
  "divisions": { v: 3n, f: 0 },
  "remainders": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "capstone-counting-a-real-system", figures: {
  "passwords": { v: 69000n, f: 0 },
  "first_choices": { v: 5n, f: 0 },
  "second_choices": { v: 25n, f: 0 },
  "third_choices": { v: 24n, f: 0 },
  "fourth_choices": { v: 23n, f: 0 },
  "prefixes": { v: 125n, f: 0 },
  "guarantee_threshold": { v: 69001n, f: 0 },
  "tools_used": { v: 4n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
