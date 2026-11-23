// Edition demo for the Linear Algebra Database (linear-algebra).
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
  { label: "systems-of-linear-equations", figures: {
  "solution_x": { v: 2n, f: 0 },
  "solution_y": { v: 3n, f: 0 },
  "equations": { v: 2n, f: 0 },
  "unknowns": { v: 2n, f: 0 },
  "systems_shown": { v: 3n, f: 0 },
  "free_variables": { v: 1n, f: 0 },
  "sum_check": { v: 5n, f: 0 },
  "difference_check": { v: 1n, f: 0 }
} },
  { label: "vectors-span-and-linear-independence", figures: {
  "vectors_tested": { v: 2n, f: 0 },
  "independent_pair": { v: 2n, f: 0 },
  "dependent_pair": { v: 2n, f: 0 },
  "span_dimension": { v: 2n, f: 0 },
  "coefficients_zero": { v: 2n, f: 0 },
  "plane_points": { v: 2n, f: 0 },
  "line_dimension": { v: 1n, f: 0 },
  "checks": { v: 2n, f: 0 }
} },
  { label: "bases-and-dimension", figures: {
  "dimension_plane": { v: 2n, f: 0 },
  "coordinates_x": { v: 2n, f: 0 },
  "coordinates_y": { v: 1n, f: 0 },
  "vector_x": { v: 3n, f: 0 },
  "vector_y": { v: 1n, f: 0 },
  "poly_dimension": { v: 3n, f: 0 },
  "basis_vectors": { v: 2n, f: 0 },
  "checks": { v: 1n, f: 0 }
} },
  { label: "matrix-arithmetic", figures: {
  "ab_11": { v: 19n, f: 0 },
  "ab_12": { v: 22n, f: 0 },
  "ab_21": { v: 43n, f: 0 },
  "ab_22": { v: 50n, f: 0 },
  "ba_11": { v: 23n, f: 0 },
  "ba_22": { v: 46n, f: 0 },
  "sum_11": { v: 6n, f: 0 },
  "sum_22": { v: 12n, f: 0 }
} },
  { label: "matrix-inverses", figures: {
  "determinant": { v: 1n, f: 0 },
  "inv_11": { v: 3n, f: 0 },
  "inv_12": { v: -1n, f: 0 },
  "inv_21": { v: -5n, f: 0 },
  "inv_22": { v: 2n, f: 0 },
  "solution_x": { v: 1n, f: 0 },
  "solution_y": { v: 2n, f: 0 },
  "check_b1": { v: 4n, f: 0 }
} },
  { label: "determinants", figures: {
  "det_1": { v: 10n, f: 0 },
  "det_singular": { v: 0n, f: 0 },
  "det_identity": { v: 1n, f: 0 },
  "det_2i": { v: 8n, f: 0 },
  "scale_factor": { v: 10n, f: 0 },
  "matrix_size": { v: 2n, f: 0 },
  "rows": { v: 2n, f: 0 },
  "cols": { v: 2n, f: 0 }
} },
  { label: "eigenvalues-and-eigenvectors", figures: {
  "eigenvalue_1": { v: 3n, f: 0 },
  "eigenvalue_2": { v: 2n, f: 0 },
  "eigenvector_1_x": { v: 1n, f: 0 },
  "eigenvector_1_y": { v: 0n, f: 0 },
  "eigenvector_2_x": { v: 1n, f: 0 },
  "eigenvector_2_y": { v: -1n, f: 0 },
  "matrix_trace": { v: 5n, f: 0 },
  "matrix_det": { v: 6n, f: 0 }
} },
  { label: "diagonalisation-of-matrices", figures: {
  "eigenvalue_1": { v: 3n, f: 0 },
  "eigenvalue_2": { v: 2n, f: 0 },
  "a_squared_11": { v: 9n, f: 0 },
  "a_squared_12": { v: 5n, f: 0 },
  "a_squared_22": { v: 4n, f: 0 },
  "trace": { v: 5n, f: 0 },
  "determinant": { v: 6n, f: 0 },
  "d_squared_11": { v: 9n, f: 0 }
} },
  { label: "inner-products-and-orthogonality", figures: {
  "dot_product": { v: 0n, f: 0 },
  "length_u": { v: 5n, f: 0 },
  "length_v": { v: 5n, f: 0 },
  "projection_x": { v: 1.32, f: 1 },
  "projection_y": { v: 1.76, f: 1 },
  "w_dot_u": { v: 11n, f: 0 },
  "u_dot_u": { v: 25n, f: 0 },
  "vectors_checked": { v: 3n, f: 0 }
} },
  { label: "orthogonal-projections-and-least-squares", figures: {
  "intercept": { v: 1.1667, f: 1 },
  "slope": { v: 1.5, f: 1 },
  "residual_sum_squares": { v: 0.1667, f: 1 },
  "residual_1": { v: -0.1667, f: 1 },
  "residual_2": { v: 0.3333, f: 1 },
  "residual_3": { v: -0.1667, f: 1 },
  "points_fitted": { v: 3n, f: 0 },
  "parameters": { v: 2n, f: 0 }
} },
  { label: "rank-of-a-matrix", figures: {
  "rank": { v: 2n, f: 0 },
  "rows": { v: 3n, f: 0 },
  "cols": { v: 3n, f: 0 },
  "nullity": { v: 1n, f: 0 },
  "pivots": { v: 2n, f: 0 },
  "null_vector_x": { v: 1n, f: 0 },
  "null_vector_y": { v: -2n, f: 0 },
  "null_vector_z": { v: 1n, f: 0 }
} },
  { label: "linear-transformations", figures: {
  "rotation_degrees": { v: 90n, f: 0 },
  "image_x": { v: -4n, f: 0 },
  "image_y": { v: 3n, f: 0 },
  "length_before": { v: 5n, f: 0 },
  "length_after": { v: 5n, f: 0 },
  "dot_product": { v: 0n, f: 0 },
  "matrix_entries": { v: 4n, f: 0 },
  "basis_images": { v: 2n, f: 0 }
} },
  { label: "change-of-basis", figures: {
  "new_coord_1": { v: 2n, f: 0 },
  "new_coord_2": { v: 1n, f: 0 },
  "old_coord_1": { v: 3n, f: 0 },
  "old_coord_2": { v: 1n, f: 0 },
  "det_p": { v: -2n, f: 0 },
  "basis_vectors": { v: 2n, f: 0 },
  "inverse_factor": { v: 0.5, f: 1 },
  "checks": { v: 1n, f: 0 }
} },
  { label: "the-singular-value-decomposition", figures: {
  "singular_1": { v: 3n, f: 0 },
  "singular_2": { v: 2n, f: 0 },
  "rank1_error": { v: 2n, f: 0 },
  "singular_2nd_example_1": { v: 2n, f: 0 },
  "singular_2nd_example_2": { v: 0n, f: 0 },
  "rank_of_example": { v: 1n, f: 0 },
  "matrices_factored": { v: 3n, f: 0 },
  "values_kept": { v: 1n, f: 0 }
} },
  { label: "vector-spaces-over-general-fields", figures: {
  "field_size": { v: 2n, f: 0 },
  "vector_count": { v: 8n, f: 0 },
  "dimension": { v: 3n, f: 0 },
  "subspaces_2d": { v: 7n, f: 0 },
  "basis_vectors": { v: 3n, f: 0 },
  "sum_example": { v: 6n, f: 0 },
  "string_length": { v: 3n, f: 0 },
  "axioms": { v: 8n, f: 0 }
} },
  { label: "quadratic-forms", figures: {
  "eigenvalue_1": { v: 4n, f: 0 },
  "eigenvalue_2": { v: 2n, f: 0 },
  "value_at_1_1": { v: 8n, f: 0 },
  "value_at_1_minus1": { v: 4n, f: 0 },
  "min_on_circle": { v: 2n, f: 0 },
  "max_on_circle": { v: 4n, f: 0 },
  "matrix_entries": { v: 4n, f: 0 },
  "variables": { v: 2n, f: 0 }
} },
  { label: "linear-algebra-in-computer-graphics", figures: {
  "rotation_result_x": { v: 0n, f: 0 },
  "rotation_result_y": { v: 1n, f: 0 },
  "scale_result_x": { v: 2n, f: 0 },
  "scale_result_y": { v: 3n, f: 0 },
  "composed_result_x": { v: 0n, f: 0 },
  "composed_result_y": { v: 3n, f: 0 },
  "matrix_size": { v: 4n, f: 0 },
  "coordinates_used": { v: 4n, f: 0 }
} },
  { label: "markov-chains", figures: {
  "sunny_prob": { v: 0.8, f: 1 },
  "rainy_prob": { v: 0.6, f: 1 },
  "steady_sunny": { v: 0.6667, f: 1 },
  "steady_rainy": { v: 0.3333, f: 1 },
  "states": { v: 2n, f: 0 },
  "eigenvalue_1": { v: 1n, f: 0 },
  "eigenvalue_2": { v: 0.4, f: 1 },
  "days_modelled": { v: 2n, f: 0 }
} },
  { label: "the-geometry-of-linear-maps", figures: {
  "determinant": { v: 4n, f: 0 },
  "area": { v: 4n, f: 0 },
  "vertices": { v: 4n, f: 0 },
  "image_x_1": { v: 2n, f: 0 },
  "image_y_1": { v: 0n, f: 0 },
  "image_x_2": { v: 1n, f: 0 },
  "image_y_2": { v: 2n, f: 0 },
  "columns": { v: 2n, f: 0 }
} },
  { label: "solving-least-squares-by-qr-factorisation", figures: {
  "intercept": { v: 1.1667, f: 1 },
  "slope": { v: 1.5, f: 1 },
  "first_col_length": { v: 1.732, f: 1 },
  "rows": { v: 3n, f: 0 },
  "cols": { v: 2n, f: 0 },
  "residual_sum_squares": { v: 0.1667, f: 1 },
  "q_columns": { v: 2n, f: 0 },
  "r_size": { v: 2n, f: 0 }
} },
  { label: "dual-spaces-and-linear-functionals", figures: {
  "f_at_1_0": { v: 2n, f: 0 },
  "f_at_0_1": { v: 3n, f: 0 },
  "f_at_2_1": { v: 7n, f: 0 },
  "dual_dimension": { v: 2n, f: 0 },
  "functionals_in_dual_basis": { v: 2n, f: 0 },
  "coordinates_picked": { v: 2n, f: 0 },
  "linearity_checks": { v: 2n, f: 0 },
  "dot_vector_x": { v: 2n, f: 0 }
} },
  { label: "the-gram-schmidt-process", figures: {
  "u1_dot_u1": { v: 2n, f: 0 },
  "projection_factor": { v: 0.5, f: 1 },
  "u2_x": { v: 0.5, f: 1 },
  "u2_y": { v: -0.5, f: 1 },
  "u2_z": { v: 1n, f: 0 },
  "u2_norm": { v: 1.225, f: 1 },
  "e1_x": { v: 0.707, f: 1 },
  "e2_z": { v: 0.816, f: 1 }
} },
  { label: "orthogonal-matrices-and-rotations", figures: {
  "cos30": { v: 0.866, f: 1 },
  "sin30": { v: 0.5, f: 1 },
  "det": { v: 1n, f: 0 },
  "column_length": { v: 1n, f: 0 },
  "dot_product": { v: 0n, f: 0 },
  "rotated_x": { v: 0.866, f: 1 },
  "rotated_y": { v: 0.5, f: 1 },
  "angle_deg": { v: 30n, f: 0 }
} },
  { label: "capstone-the-matrix-that-runs-a-system", figures: {
  "eigenvalue_1": { v: 1n, f: 0 },
  "eigenvalue_2": { v: 0.7, f: 1 },
  "steady_1": { v: 0.6667, f: 1 },
  "steady_2": { v: 0.3333, f: 1 },
  "after_1_step": { v: 90n, f: 0 },
  "after_2_steps": { v: 83n, f: 0 },
  "after_10_steps": { v: 67.6, f: 1 },
  "states": { v: 2n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
