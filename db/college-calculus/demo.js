// Edition demo for the Calculus I-III Database (college-calculus).
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
  { label: "limits-of-functions", figures: {
  "limit_value": { v: 2n, f: 0 },
  "value_at_0.9": { v: 1.9, f: 1 },
  "value_at_0.99": { v: 1.99, f: 1 },
  "value_at_1.01": { v: 2.01, f: 1 },
  "value_at_1.1": { v: 2.1, f: 1 },
  "points_checked": { v: 4n, f: 0 },
  "sides_checked": { v: 2n, f: 0 },
  "factor_terms": { v: 2n, f: 0 }
} },
  { label: "the-derivative-as-a-rate-of-change", figures: {
  "derivative_at_3": { v: 6n, f: 0 },
  "derivative_at_0": { v: 0n, f: 0 },
  "function_at_3": { v: 9n, f: 0 },
  "power_n": { v: 2n, f: 0 },
  "coefficient": { v: 2n, f: 0 },
  "points_checked": { v: 2n, f: 0 },
  "limit_steps": { v: 3n, f: 0 },
  "definition_parts": { v: 2n, f: 0 }
} },
  { label: "the-product-quotient-and-chain-rules", figures: {
  "h_at_1": { v: 8n, f: 0 },
  "h_prime_at_1": { v: 24n, f: 0 },
  "chain_factors": { v: 2n, f: 0 },
  "product_terms": { v: 2n, f: 0 },
  "quotient_terms": { v: 2n, f: 0 },
  "rules_named": { v: 3n, f: 0 },
  "x_checked": { v: 1n, f: 0 },
  "derivative_value": { v: 24n, f: 0 }
} },
  { label: "optimisation-with-derivatives", figures: {
  "fence_total": { v: 100n, f: 0 },
  "optimal_x": { v: 25n, f: 0 },
  "parallel_side": { v: 50n, f: 0 },
  "max_area": { v: 1250n, f: 0 },
  "second_derivative": { v: -4n, f: 0 },
  "critical_points": { v: 1n, f: 0 },
  "endpoints_checked": { v: 2n, f: 0 },
  "derivative_zero_at": { v: 25n, f: 0 }
} },
  { label: "related-rates", figures: {
  "ladder_length": { v: 5n, f: 0 },
  "foot_distance": { v: 3n, f: 0 },
  "top_height": { v: 4n, f: 0 },
  "foot_speed": { v: 0.5, f: 1 },
  "top_speed": { v: -0.375, f: 1 },
  "triangle_sides": { v: 3n, f: 0 },
  "relation_terms": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "the-definite-integral-and-area", figures: {
  "integral_value": { v: 2.6667, f: 1 },
  "rectangles_4": { v: 3.75, f: 1 },
  "rectangles_10": { v: 2.87, f: 1 },
  "upper_limit": { v: 2n, f: 0 },
  "antiderivative_at_2": { v: 2.6667, f: 1 },
  "width_4": { v: 0.5, f: 1 },
  "terms_4": { v: 4n, f: 0 },
  "terms_10": { v: 10n, f: 0 }
} },
  { label: "the-fundamental-theorem-of-calculus", figures: {
  "integral_value": { v: 15n, f: 0 },
  "antiderivative_at_4": { v: 16n, f: 0 },
  "antiderivative_at_1": { v: 1n, f: 0 },
  "trapezoid_heights_sum": { v: 10n, f: 0 },
  "width": { v: 3n, f: 0 },
  "area_check": { v: 15n, f: 0 },
  "lower_limit": { v: 1n, f: 0 },
  "upper_limit": { v: 4n, f: 0 }
} },
  { label: "integration-by-substitution", figures: {
  "integral_value": { v: 1.71828, f: 1 },
  "e_value": { v: 2.71828, f: 1 },
  "lower_u": { v: 0n, f: 0 },
  "upper_u": { v: 1n, f: 0 },
  "substitution_terms": { v: 2n, f: 0 },
  "limits_changed": { v: 2n, f: 0 },
  "check_value": { v: 1.71828, f: 1 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "integration-by-parts", figures: {
  "integral_value": { v: 1n, f: 0 },
  "e_value": { v: 2.71828, f: 1 },
  "boundary_term": { v: 2.71828, f: 1 },
  "subtracted_integral": { v: 1.71828, f: 1 },
  "integrand_at_half": { v: 0.824, f: 1 },
  "limits": { v: 2n, f: 0 },
  "parts_applied": { v: 1n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "integration-by-partial-fractions", figures: {
  "constant_a": { v: 0.3333, f: 1 },
  "constant_b": { v: -0.3333, f: 1 },
  "factors": { v: 2n, f: 0 },
  "terms": { v: 2n, f: 0 },
  "coefficient_sum": { v: 0n, f: 0 },
  "check_numerator": { v: 1n, f: 0 },
  "x_test_1": { v: 1n, f: 0 },
  "x_test_2": { v: -2n, f: 0 }
} },
  { label: "convergence-tests-for-series", figures: {
  "ratio_limit": { v: 0n, f: 0 },
  "sum_limit": { v: 1.71828, f: 1 },
  "partial_sum_5": { v: 2.70833, f: 1 },
  "e_value": { v: 2.71828, f: 1 },
  "terms_used": { v: 5n, f: 0 },
  "tests_named": { v: 4n, f: 0 },
  "harmonic_diverges": { v: 1n, f: 0 },
  "ratio_at_n5": { v: 0.1667, f: 1 }
} },
  { label: "taylor-series-and-approximation", figures: {
  "approximation": { v: 1.648437, f: 1 },
  "true_value": { v: 1.648721, f: 1 },
  "error": { v: 0.000284, f: 1 },
  "next_term": { v: 0.00026, f: 1 },
  "error_bound": { v: 0.00043, f: 1 },
  "terms_used": { v: 5n, f: 0 },
  "x_value": { v: 0.5, f: 1 },
  "degree": { v: 4n, f: 0 }
} },
  { label: "partial-derivatives", figures: {
  "fx_at_2_1": { v: 7n, f: 0 },
  "fy_at_2_1": { v: 16n, f: 0 },
  "gradient_x": { v: 7n, f: 0 },
  "gradient_y": { v: 16n, f: 0 },
  "point_x": { v: 2n, f: 0 },
  "point_y": { v: 1n, f: 0 },
  "variables": { v: 2n, f: 0 },
  "partials_computed": { v: 2n, f: 0 }
} },
  { label: "multiple-integrals", figures: {
  "integral_value": { v: 3n, f: 0 },
  "rectangle_area": { v: 2n, f: 0 },
  "integral_of_x": { v: 2n, f: 0 },
  "integral_of_y": { v: 1n, f: 0 },
  "x_upper": { v: 2n, f: 0 },
  "y_upper": { v: 1n, f: 0 },
  "average_x": { v: 1n, f: 0 },
  "average_y": { v: 0.5, f: 1 }
} },
  { label: "vector-calculus-and-its-great-theorems", figures: {
  "area_of_unit_circle": { v: 3.14159, f: 1 },
  "curl_value": { v: 1n, f: 0 },
  "line_integral": { v: 3.14159, f: 1 },
  "t_upper": { v: 6.28318, f: 1 },
  "field_components": { v: 2n, f: 0 },
  "theorems_named": { v: 3n, f: 0 },
  "dimensions": { v: 2n, f: 0 },
  "check_agrees": { v: 1n, f: 0 }
} },
  { label: "improper-integrals", figures: {
  "integral_value": { v: 1n, f: 0 },
  "value_at_5": { v: 0.99326, f: 1 },
  "value_at_10": { v: 0.99995, f: 1 },
  "p_test_threshold": { v: 1n, f: 0 },
  "harmonic_diverges": { v: 1n, f: 0 },
  "lower_limit": { v: 0n, f: 0 },
  "steps": { v: 2n, f: 0 },
  "limit_points_checked": { v: 2n, f: 0 }
} },
  { label: "differential-equations-from-calculus", figures: {
  "c_value": { v: 3n, f: 0 },
  "y_at_1": { v: 22.167, f: 1 },
  "doubling_time": { v: 0.3466, f: 1 },
  "growth_rate": { v: 2n, f: 0 },
  "y_at_0": { v: 3n, f: 0 },
  "derivative_check": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "initial_condition": { v: 3n, f: 0 }
} },
  { label: "lagrange-multipliers", figures: {
  "optimal_x": { v: 5n, f: 0 },
  "optimal_y": { v: 5n, f: 0 },
  "max_value": { v: 25n, f: 0 },
  "multiplier": { v: 5n, f: 0 },
  "constraint_sum": { v: 10n, f: 0 },
  "endpoint_value": { v: 0n, f: 0 },
  "candidates": { v: 1n, f: 0 },
  "constraints": { v: 1n, f: 0 }
} },
  { label: "the-mean-value-theorem", figures: {
  "distance_km": { v: 120n, f: 0 },
  "time_hours": { v: 2n, f: 0 },
  "average_speed": { v: 60n, f: 0 },
  "theorem_point": { v: 1n, f: 0 },
  "average_rate": { v: 2n, f: 0 },
  "interval_length": { v: 2n, f: 0 },
  "function_at_2": { v: 4n, f: 0 },
  "hypotheses": { v: 2n, f: 0 }
} },
  { label: "curve-sketching-with-derivatives", figures: {
  "critical_x_1": { v: -1n, f: 0 },
  "critical_x_2": { v: 1n, f: 0 },
  "local_max": { v: 2n, f: 0 },
  "local_min": { v: -2n, f: 0 },
  "inflection_x": { v: 0n, f: 0 },
  "root_1": { v: -1.732, f: 1 },
  "root_2": { v: 0n, f: 0 },
  "root_3": { v: 1.732, f: 1 }
} },
  { label: "volumes-of-revolution", figures: {
  "volume": { v: 25.1327, f: 1 },
  "pi_times_8": { v: 25.1327, f: 1 },
  "upper_x": { v: 4n, f: 0 },
  "radius_at_4": { v: 2n, f: 0 },
  "shell_check": { v: 25.1327, f: 1 },
  "methods_used": { v: 2n, f: 0 },
  "disk_radius_squared": { v: 4n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "arc-length-and-surface-area", figures: {
  "arc_length": { v: 4.6667, f: 1 },
  "straight_distance": { v: 4.5826, f: 1 },
  "upper_x": { v: 3n, f: 0 },
  "y_at_3": { v: 3.464, f: 1 },
  "integrand_at_3": { v: 2n, f: 0 },
  "curve_points": { v: 2n, f: 0 },
  "formula_terms": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "parametric-curves-and-polar-coordinates", figures: {
  "petal_area": { v: 1.5708, f: 1 },
  "total_area": { v: 6.2832, f: 1 },
  "petals": { v: 4n, f: 0 },
  "radius_max": { v: 2n, f: 0 },
  "circle_area": { v: 12.566, f: 1 },
  "theta_range": { v: 1.5708, f: 1 },
  "integrand_factor": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 }
} },
  { label: "a-capstone-modelling-problem-using-calculus", figures: {
  "volume": { v: 32n, f: 0 },
  "side_m": { v: 3.174, f: 1 },
  "height_m": { v: 3.174, f: 1 },
  "surface_area": { v: 60.5, f: 1 },
  "hemisphere_volume": { v: 16.755, f: 1 },
  "taylor_e0.1": { v: 1.10517, f: 1 },
  "true_e0.1": { v: 1.1051702, f: 1 },
  "parts": { v: 3n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
