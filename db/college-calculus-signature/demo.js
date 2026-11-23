// Edition demo for the The Signature Calculus I-III Database (college-calculus-signature).
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
  { label: "a-signature-limit-microscope-design", figures: {
  "zoom_levels": { v: 3n, f: 0 },
  "values_checked": { v: 6n, f: 0 },
  "limit_value": { v: 2n, f: 0 },
  "value_at_0.1_left": { v: 1.9, f: 1 },
  "value_at_0.1_right": { v: 2.1, f: 1 },
  "value_at_0.001": { v: 1.999, f: 1 },
  "jump_flagged": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-tangent-line-tracer-design", figures: {
  "secants_shown": { v: 3n, f: 0 },
  "slope_at_2.1": { v: 4.1, f: 1 },
  "slope_at_2.01": { v: 4.01, f: 1 },
  "slope_at_2.001": { v: 4.001, f: 1 },
  "derivative_at_2": { v: 4n, f: 0 },
  "derivative_at_0": { v: 0n, f: 0 },
  "tangents_drawn": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-differentiation-rule-machine-design", figures: {
  "steps": { v: 2n, f: 0 },
  "rules_used": { v: 1n, f: 0 },
  "derivative_at_1": { v: 24n, f: 0 },
  "numerical_check": { v: 24n, f: 0 },
  "functions_differentiated": { v: 1n, f: 0 },
  "corrections_offered": { v: 1n, f: 0 },
  "rules_named": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-optimisation-workbench-design", figures: {
  "perimeter": { v: 40n, f: 0 },
  "optimal_side": { v: 10n, f: 0 },
  "max_area": { v: 100n, f: 0 },
  "critical_points": { v: 1n, f: 0 },
  "endpoints": { v: 2n, f: 0 },
  "second_derivative": { v: -2n, f: 0 },
  "candidates_tested": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-related-rates-simulator-design", figures: {
  "ladder": { v: 5n, f: 0 },
  "pause_1_foot": { v: 3n, f: 0 },
  "pause_1_top": { v: 4n, f: 0 },
  "pause_1_rate": { v: 0.375, f: 1 },
  "pause_2_foot": { v: 4n, f: 0 },
  "pause_2_top": { v: 3n, f: 0 },
  "pause_2_rate": { v: 0.6667, f: 1 },
  "foot_speed": { v: 0.5, f: 1 }
} },
  { label: "a-signature-riemann-sum-builder-design", figures: {
  "exact_integral": { v: 2.6667, f: 1 },
  "sum_4": { v: 3.75, f: 1 },
  "sum_10": { v: 2.87, f: 1 },
  "sum_100": { v: 2.6867, f: 1 },
  "error_4": { v: 1.0833, f: 1 },
  "error_10": { v: 0.2033, f: 1 },
  "error_100": { v: 0.02, f: 1 },
  "rules_offered": { v: 3n, f: 0 }
} },
  { label: "a-signature-antiderivative-finder-design", figures: {
  "functions_tested": { v: 2n, f: 0 },
  "verifications": { v: 2n, f: 0 },
  "integral_1": { v: 15n, f: 0 },
  "integral_2": { v: 1n, f: 0 },
  "endpoint_values_1": { v: 16n, f: 0 },
  "endpoint_values_2": { v: 1n, f: 0 },
  "table_entries": { v: 20n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-substitution-workbench-design", figures: {
  "integral_value": { v: 1.71828, f: 1 },
  "limits_changed": { v: 2n, f: 0 },
  "substitutions": { v: 1n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "lower_limit": { v: 0n, f: 0 },
  "upper_limit": { v: 1n, f: 0 },
  "e_value": { v: 2.71828, f: 1 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-integration-by-parts-workbench-design", figures: {
  "integral_value": { v: 1n, f: 0 },
  "choices_tried": { v: 2n, f: 0 },
  "choices_flagged": { v: 1n, f: 0 },
  "boundary_term": { v: 2.71828, f: 1 },
  "subtracted": { v: 1.71828, f: 1 },
  "parts_applied": { v: 1n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-series-convergence-laboratory-design", figures: {
  "ratio_limit": { v: 0n, f: 0 },
  "partial_sum_5": { v: 2.70833, f: 1 },
  "e_value": { v: 2.71828, f: 1 },
  "tests_applied": { v: 4n, f: 0 },
  "series_tested": { v: 2n, f: 0 },
  "inconclusive_count": { v: 1n, f: 0 },
  "terms_shown": { v: 5n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-taylor-approximator-design", figures: {
  "degree_4_value": { v: 1.648437, f: 1 },
  "true_value": { v: 1.648721, f: 1 },
  "error_4": { v: 0.000284, f: 1 },
  "bound_4": { v: 0.00043, f: 1 },
  "degree_6_value": { v: 1.648721, f: 1 },
  "degrees_tried": { v: 2n, f: 0 },
  "x_value": { v: 0.5, f: 1 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-multivariable-explorer-design", figures: {
  "fx_at_1_2": { v: 2n, f: 0 },
  "fy_at_1_2": { v: 4n, f: 0 },
  "height_at_1_2": { v: 5n, f: 0 },
  "gradient_length": { v: 4.4721, f: 1 },
  "fx_at_0_0": { v: 0n, f: 0 },
  "fy_at_0_0": { v: 0n, f: 0 },
  "points_shown": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-volume-builder-design", figures: {
  "volume": { v: 3n, f: 0 },
  "orders_tried": { v: 2n, f: 0 },
  "rectangle_area": { v: 2n, f: 0 },
  "inner_result_at_2": { v: 2.5, f: 1 },
  "integral_of_x": { v: 2n, f: 0 },
  "integral_of_y": { v: 1n, f: 0 },
  "slices_shown": { v: 10n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-vector-field-studio-design", figures: {
  "line_integral": { v: 3.14159, f: 1 },
  "area": { v: 3.14159, f: 1 },
  "curl": { v: 1n, f: 0 },
  "arrows_drawn": { v: 25n, f: 0 },
  "curve_points": { v: 100n, f: 0 },
  "theorems_shown": { v: 3n, f: 0 },
  "fields_drawn": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-improper-integral-tester-design", figures: {
  "value_at_1": { v: 0.63212, f: 1 },
  "value_at_5": { v: 0.99326, f: 1 },
  "value_at_10": { v: 0.99995, f: 1 },
  "limit_value": { v: 1n, f: 0 },
  "divergent_at_e2": { v: 2.30259, f: 1 },
  "divergent_at_e4": { v: 4.60517, f: 1 },
  "cutoffs_shown": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-growth-equation-laboratory-design", figures: {
  "rate": { v: 2n, f: 0 },
  "starting_value": { v: 3n, f: 0 },
  "y_at_1": { v: 22.167, f: 1 },
  "doubling_time": { v: 0.3466, f: 1 },
  "second_start": { v: 1n, f: 0 },
  "second_y_at_1": { v: 7.389, f: 1 },
  "runs": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-constraint-optimiser-design", figures: {
  "optimal_x": { v: 5n, f: 0 },
  "optimal_y": { v: 5n, f: 0 },
  "max_value": { v: 25n, f: 0 },
  "multiplier": { v: 5n, f: 0 },
  "constraint_sum": { v: 10n, f: 0 },
  "endpoint_value": { v: 0n, f: 0 },
  "curves_drawn": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-mean-value-demonstrator-design", figures: {
  "average_rate": { v: 2n, f: 0 },
  "theorem_point": { v: 1n, f: 0 },
  "distance_km": { v: 120n, f: 0 },
  "time_hours": { v: 2n, f: 0 },
  "average_speed": { v: 60n, f: 0 },
  "interval_length": { v: 2n, f: 0 },
  "tests_run": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-curve-sketcher-design", figures: {
  "critical_points": { v: 2n, f: 0 },
  "local_max": { v: 2n, f: 0 },
  "local_min": { v: -2n, f: 0 },
  "inflection_points": { v: 1n, f: 0 },
  "roots": { v: 3n, f: 0 },
  "root_1": { v: -1.732, f: 1 },
  "root_3": { v: 1.732, f: 1 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-solid-of-revolution-builder-design", figures: {
  "volume": { v: 25.1327, f: 1 },
  "methods": { v: 2n, f: 0 },
  "upper_x": { v: 4n, f: 0 },
  "radius_at_4": { v: 2n, f: 0 },
  "disk_integral": { v: 25.1327, f: 1 },
  "shell_integral": { v: 25.1327, f: 1 },
  "slices_shown": { v: 20n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-arc-length-measurer-design", figures: {
  "length_3_segments": { v: 4.55, f: 1 },
  "length_10_segments": { v: 4.66, f: 1 },
  "length_100_segments": { v: 4.6666, f: 1 },
  "exact_length": { v: 4.6667, f: 1 },
  "straight_distance": { v: 4.5826, f: 1 },
  "segment_counts": { v: 3n, f: 0 },
  "upper_x": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-polar-rose-plotter-design", figures: {
  "petals": { v: 4n, f: 0 },
  "petal_area": { v: 1.5708, f: 1 },
  "total_area": { v: 6.2832, f: 1 },
  "radius_max": { v: 2n, f: 0 },
  "maxima": { v: 4n, f: 0 },
  "theta_range": { v: 6.2832, f: 1 },
  "curves_traced": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-limit-at-infinity-viewer-design", figures: {
  "value_x1": { v: 0.833, f: 1 },
  "value_x10": { v: 3.048, f: 1 },
  "value_x1000": { v: 3.002, f: 1 },
  "limit": { v: 3n, f: 0 },
  "n_terms": { v: 100n, f: 0 },
  "approx_e": { v: 2.7048, f: 1 },
  "e_true": { v: 2.71828, f: 1 },
  "error": { v: 0.0135, f: 1 }
} },
  { label: "a-signature-calculus-capstone-board-design", figures: {
  "parts": { v: 3n, f: 0 },
  "volume": { v: 0.41888, f: 1 },
  "intersections": { v: 2n, f: 0 },
  "integral_value": { v: 0.13333, f: 1 },
  "pi_factor": { v: 0.41888, f: 1 },
  "lower_limit": { v: 0n, f: 0 },
  "upper_limit": { v: 1n, f: 0 },
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
