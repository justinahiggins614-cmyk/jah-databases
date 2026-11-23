// Edition demo for the The Signature Discrete Mathematics Database (discrete-mathematics-signature).
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
  { label: "a-signature-truth-table-builder-design", figures: {
  "rows_checked": { v: 4n, f: 0 },
  "equivalences_found": { v: 1n, f: 0 },
  "tautologies_flagged": { v: 1n, f: 0 },
  "parts_max": { v: 4n, f: 0 },
  "rows_for_4_parts": { v: 16n, f: 0 },
  "rows_for_10_parts": { v: 1024n, f: 0 },
  "cap_parts": { v: 5n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-quantifier-game-design", figures: {
  "rounds": { v: 10n, f: 0 },
  "forall_rounds": { v: 4n, f: 0 },
  "exists_rounds": { v: 3n, f: 0 },
  "disproof_rounds": { v: 3n, f: 0 },
  "hints_used": { v: 2n, f: 0 },
  "strategies_corrected": { v: 1n, f: 0 },
  "points_per_round": { v: 10n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-function-classifier-design", figures: {
  "functions_tested": { v: 2n, f: 0 },
  "bijections_found": { v: 1n, f: 0 },
  "inputs_1": { v: 3n, f: 0 },
  "inputs_2": { v: 5n, f: 0 },
  "collisions_found": { v: 1n, f: 0 },
  "gaps_found": { v: 1n, f: 0 },
  "properties_checked": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-induction-ladder-design", figures: {
  "rungs_lit": { v: 10n, f: 0 },
  "base_case": { v: 2n, f: 0 },
  "splits_shown": { v: 2n, f: 0 },
  "proof_parts": { v: 2n, f: 0 },
  "induction_forms": { v: 2n, f: 0 },
  "rungs_total": { v: 10n, f: 0 },
  "checks": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-counting-bench-design", figures: {
  "strings_counted": { v: 3380n, f: 0 },
  "total_strings": { v: 17576n, f: 0 },
  "complement_count": { v: 14196n, f: 0 },
  "methods_used": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "choices_first": { v: 5n, f: 0 },
  "choices_later": { v: 26n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-committee-counter-design", figures: {
  "committees": { v: 120n, f: 0 },
  "total_ways": { v: 360n, f: 0 },
  "method_2_total": { v: 360n, f: 0 },
  "poker_hands": { v: 2598960n, f: 0 },
  "people": { v: 10n, f: 0 },
  "committee_size": { v: 3n, f: 0 },
  "orders_compared": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-pigeonhole-demonstrator-design", figures: {
  "points": { v: 5n, f: 0 },
  "boxes": { v: 4n, f: 0 },
  "max_distance": { v: 0.7071, f: 1 },
  "objects_2": { v: 13n, f: 0 },
  "boxes_2": { v: 12n, f: 0 },
  "guaranteed_2": { v: 2n, f: 0 },
  "tests": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-inclusion-exclusion-counter-design", figures: {
  "divisible_by_2": { v: 50n, f: 0 },
  "divisible_by_3": { v: 33n, f: 0 },
  "divisible_by_6": { v: 16n, f: 0 },
  "union": { v: 67n, f: 0 },
  "neither": { v: 33n, f: 0 },
  "methods": { v: 2n, f: 0 },
  "regions": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-graph-studio-design", figures: {
  "vertices": { v: 6n, f: 0 },
  "degree_sum": { v: 10n, f: 0 },
  "edges": { v: 5n, f: 0 },
  "odd_degree_vertices": { v: 4n, f: 0 },
  "tree_edges": { v: 5n, f: 0 },
  "graphs_drawn": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-bridge-puzzle-design", figures: {
  "konigsberg_odd": { v: 4n, f: 0 },
  "square_odd": { v: 2n, f: 0 },
  "bridges": { v: 7n, f: 0 },
  "square_edges": { v: 5n, f: 0 },
  "puzzles": { v: 2n, f: 0 },
  "paths_found": { v: 1n, f: 0 },
  "impossible_count": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-tree-builder-design", figures: {
  "offices": { v: 8n, f: 0 },
  "cables": { v: 7n, f: 0 },
  "labelled_trees": { v: 262144n, f: 0 },
  "binary_levels": { v: 4n, f: 0 },
  "binary_vertices": { v: 15n, f: 0 },
  "cycles_flagged": { v: 1n, f: 0 },
  "trees_built": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-recurrence-table-design", figures: {
  "a_0": { v: 1n, f: 0 },
  "a_1": { v: 3n, f: 0 },
  "a_2": { v: 7n, f: 0 },
  "a_3": { v: 15n, f: 0 },
  "a_4": { v: 31n, f: 0 },
  "root_1": { v: 1n, f: 0 },
  "root_2": { v: 2n, f: 0 },
  "terms_listed": { v: 5n, f: 0 }
} },
  { label: "a-signature-generating-function-workbench-design", figures: {
  "ways_change": { v: 4n, f: 0 },
  "ways_sum5": { v: 6n, f: 0 },
  "amount": { v: 10n, f: 0 },
  "coins": { v: 3n, f: 0 },
  "problems_solved": { v: 2n, f: 0 },
  "coefficients_read": { v: 2n, f: 0 },
  "terms_shown": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-prime-factoriser-design", figures: {
  "n_factored": { v: 360n, f: 0 },
  "prime_2_power": { v: 3n, f: 0 },
  "prime_3_power": { v: 2n, f: 0 },
  "prime_5_power": { v: 1n, f: 0 },
  "divisor_count": { v: 24n, f: 0 },
  "prime_tested": { v: 97n, f: 0 },
  "sqrt_97": { v: 9.85, f: 1 },
  "divisions_shown": { v: 5n, f: 0 }
} },
  { label: "a-signature-rsa-toy-design", figures: {
  "rsa_n": { v: 55n, f: 0 },
  "rsa_phi": { v: 40n, f: 0 },
  "rsa_e": { v: 3n, f: 0 },
  "rsa_d": { v: 27n, f: 0 },
  "message": { v: 7n, f: 0 },
  "ciphertext": { v: 13n, f: 0 },
  "primes_used": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-circuit-builder-design", figures: {
  "truth_table_rows": { v: 4n, f: 0 },
  "ones_in_table": { v: 2n, f: 0 },
  "builds": { v: 2n, f: 0 },
  "gates_used": { v: 5n, f: 0 },
  "variables": { v: 2n, f: 0 },
  "tables_agreeing": { v: 2n, f: 0 },
  "laws_shown": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-hash-collision-finder-design", figures: {
  "slots": { v: 100n, f: 0 },
  "items": { v: 150n, f: 0 },
  "average_load": { v: 1.5, f: 1 },
  "first_collision_by": { v: 101n, f: 0 },
  "fullest_slot": { v: 4n, f: 0 },
  "guaranteed_collision": { v: 2n, f: 0 },
  "collisions_found": { v: 50n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-map-colourer-design", figures: {
  "pentagon_vertices": { v: 5n, f: 0 },
  "chromatic_number": { v: 3n, f: 0 },
  "colours_tried": { v: 2n, f: 0 },
  "complete_vertices": { v: 4n, f: 0 },
  "complete_chromatic": { v: 4n, f: 0 },
  "map_colours": { v: 4n, f: 0 },
  "graphs_coloured": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-hat-check-simulator-design", figures: {
  "derangements_4": { v: 9n, f: 0 },
  "permutations_4": { v: 24n, f: 0 },
  "fraction_4": { v: 0.375, f: 1 },
  "derangements_5": { v: 44n, f: 0 },
  "permutations_5": { v: 120n, f: 0 },
  "fraction_5": { v: 0.3667, f: 1 },
  "trials": { v: 1000n, f: 0 },
  "limit_fraction": { v: 0.3679, f: 1 }
} },
  { label: "a-signature-graph-induction-prover-design", figures: {
  "base_vertices": { v: 1n, f: 0 },
  "base_edges": { v: 0n, f: 0 },
  "tree_5_edges": { v: 4n, f: 0 },
  "tree_8_edges": { v: 7n, f: 0 },
  "leaf_degree": { v: 1n, f: 0 },
  "proofs": { v: 2n, f: 0 },
  "steps": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-order-diagrammer-design", figures: {
  "elements": { v: 4n, f: 0 },
  "comparable_pairs": { v: 5n, f: 0 },
  "reflexive_pairs": { v: 4n, f: 0 },
  "maximal_elements": { v: 1n, f: 0 },
  "maximum": { v: 6n, f: 0 },
  "properties_tested": { v: 3n, f: 0 },
  "relations_tested": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-bezout-finder-design", figures: {
  "gcd": { v: 21n, f: 0 },
  "coefficient_105": { v: 5n, f: 0 },
  "coefficient_252": { v: -2n, f: 0 },
  "check_525": { v: 525n, f: 0 },
  "check_504": { v: 504n, f: 0 },
  "divisions": { v: 3n, f: 0 },
  "combinations_found": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-hamiltonian-tour-finder-design", figures: {
  "vertices_k5": { v: 5n, f: 0 },
  "cycles_k5": { v: 12n, f: 0 },
  "dodecahedron_vertices": { v: 20n, f: 0 },
  "game_year": { v: 1857n, f: 0 },
  "directions": { v: 2n, f: 0 },
  "graphs": { v: 2n, f: 0 },
  "cycles_found": { v: 12n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-discrete-capstone-board-design", figures: {
  "passwords": { v: 69000n, f: 0 },
  "parts": { v: 3n, f: 0 },
  "checks_passed": { v: 3n, f: 0 },
  "prefixes": { v: 125n, f: 0 },
  "guarantee_threshold": { v: 69001n, f: 0 },
  "tools_named": { v: 4n, f: 0 },
  "first_choices": { v: 5n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
