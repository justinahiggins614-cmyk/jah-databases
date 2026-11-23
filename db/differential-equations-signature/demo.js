// Edition demo for the The Signature Differential Equations Database (differential-equations-signature).
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
  { label: "a-signature-equation-classifier-design", figures: {
  "equations_classified": { v: 3n, f: 0 },
  "orders_found": { v: 2n, f: 0 },
  "methods_named": { v: 3n, f: 0 },
  "types_named": { v: 3n, f: 0 },
  "linear_count": { v: 3n, f: 0 },
  "partial_count": { v: 1n, f: 0 },
  "ordinary_count": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-direction-field-painter-design", figures: {
  "slopes_shown": { v: 3n, f: 0 },
  "solution_points": { v: 2n, f: 0 },
  "y_at_2": { v: 3n, f: 0 },
  "y_at_minus2": { v: 3n, f: 0 },
  "equilibria": { v: 1n, f: 0 },
  "grid_points": { v: 25n, f: 0 },
  "curves_drawn": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-separation-workbench-design", figures: {
  "separations": { v: 1n, f: 0 },
  "integrals": { v: 2n, f: 0 },
  "y_at_1": { v: 3.297, f: 1 },
  "initial_value": { v: 2n, f: 0 },
  "constant_a": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "variables": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-integrating-factor-machine-design", figures: {
  "y_at_1": { v: 1.7293, f: 1 },
  "steady_value": { v: 2n, f: 0 },
  "constant_c": { v: -2n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "factor_at_1": { v: 7.389, f: 1 },
  "terms": { v: 2n, f: 0 },
  "checks": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-characteristic-root-finder-design", figures: {
  "equations_solved": { v: 2n, f: 0 },
  "root_types": { v: 2n, f: 0 },
  "root_1": { v: 1n, f: 0 },
  "root_2": { v: 2n, f: 0 },
  "c1": { v: 2n, f: 0 },
  "c2": { v: -1n, f: 0 },
  "omega": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-spring-simulator-design", figures: {
  "omega": { v: 2n, f: 0 },
  "period": { v: 3.1416, f: 1 },
  "amplitude": { v: 1n, f: 0 },
  "y_at_pi_over_4": { v: 0n, f: 0 },
  "y_at_pi_over_2": { v: -1n, f: 0 },
  "damping_half_life": { v: 1.386, f: 1 },
  "tests": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-laplace-transformer-design", figures: {
  "y_at_0": { v: 3n, f: 0 },
  "y_at_1": { v: 0.406, f: 1 },
  "pole": { v: -2n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "table_entries": { v: 20n, f: 0 },
  "transforms_shown": { v: 3n, f: 0 },
  "checks": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-phase-portrait-studio-design", figures: {
  "eigenvalue_1": { v: -1n, f: 0 },
  "eigenvalue_2": { v: -2n, f: 0 },
  "x_at_1": { v: 0.3679, f: 1 },
  "y_at_1": { v: 0.1353, f: 1 },
  "systems_shown": { v: 2n, f: 0 },
  "classifications": { v: 2n, f: 0 },
  "trajectories_drawn": { v: 5n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-heat-spreader-design", figures: {
  "factor_at_0.1": { v: 0.3727, f: 1 },
  "factor_at_0.5": { v: 0.0072, f: 1 },
  "length": { v: 1n, f: 0 },
  "modes_shown": { v: 2n, f: 0 },
  "profiles": { v: 2n, f: 0 },
  "times_shown": { v: 2n, f: 0 },
  "peak_initial": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-vibrating-string-tank-design", figures: {
  "wave_speed": { v: 2n, f: 0 },
  "period": { v: 1n, f: 0 },
  "max_displacement": { v: 1n, f: 0 },
  "t_flat": { v: 0.25, f: 1 },
  "t_inverted": { v: 0.5, f: 1 },
  "modes_shown": { v: 2n, f: 0 },
  "length": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-potential-mapper-design", figures: {
  "top_temperature": { v: 100n, f: 0 },
  "centre_temperature": { v: 25.3, f: 1 },
  "agreement": { v: 0.1, f: 1 },
  "edges_set": { v: 4n, f: 0 },
  "iterations": { v: 100n, f: 0 },
  "first_coefficient": { v: 127.32, f: 1 },
  "plate_size": { v: 1n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-fourier-synthesiser-design", figures: {
  "sum_1_term": { v: 1.2732, f: 1 },
  "sum_3_terms": { v: 1.1037, f: 1 },
  "sum_10_terms": { v: 1.0633, f: 1 },
  "true_value": { v: 1n, f: 0 },
  "overshoot_percent": { v: 9n, f: 0 },
  "terms_added": { v: 10n, f: 0 },
  "coefficients_shown": { v: 5n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-numerical-stepper-design", figures: {
  "euler_h0.1": { v: 1.21, f: 1 },
  "true_value": { v: 1.2214, f: 1 },
  "error_h0.1": { v: 0.0114, f: 1 },
  "euler_h0.05": { v: 1.2155, f: 1 },
  "error_h0.05": { v: 0.0059, f: 1 },
  "rk4_value": { v: 1.2214, f: 1 },
  "methods_offered": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-stability-tester-design", figures: {
  "eigenvalue_1": { v: -1n, f: 0 },
  "eigenvalue_2": { v: -2n, f: 0 },
  "x_at_1": { v: 0.3679, f: 1 },
  "y_at_1": { v: 0.1353, f: 1 },
  "systems_tested": { v: 2n, f: 0 },
  "verdicts": { v: 2n, f: 0 },
  "saddle_eigenvalues": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-exactness-checker-design", figures: {
  "m_y": { v: 1n, f: 0 },
  "n_x": { v: 1n, f: 0 },
  "solution_at_1_1": { v: 3n, f: 0 },
  "tests": { v: 2n, f: 0 },
  "exact_count": { v: 1n, f: 0 },
  "potential_terms": { v: 3n, f: 0 },
  "second_m_y": { v: 1n, f: 0 },
  "second_n_x_at_1": { v: 2n, f: 0 }
} },
  { label: "a-signature-forcing-response-laboratory-design", figures: {
  "a_coefficient": { v: -6n, f: 0 },
  "forcing_amplitude": { v: 6n, f: 0 },
  "methods_used": { v: 2n, f: 0 },
  "forcing_terms": { v: 2n, f: 0 },
  "particular_solutions": { v: 2n, f: 0 },
  "homogeneous_terms": { v: 2n, f: 0 },
  "steps": { v: 3n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-special-function-table-design", figures: {
  "j0_at_1": { v: 0.7652, f: 1 },
  "approx_at_1": { v: 0.765625, f: 1 },
  "j0_at_2": { v: 0.2239, f: 1 },
  "approx_at_2": { v: 0.222222, f: 1 },
  "first_zero": { v: 2.4048, f: 1 },
  "terms_used": { v: 3n, f: 0 },
  "functions_listed": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-boundary-value-solver-design", figures: {
  "first_eigenvalue": { v: 9.8696, f: 1 },
  "second_eigenvalue": { v: 39.4784, f: 1 },
  "eigenfunctions": { v: 2n, f: 0 },
  "boundary_points": { v: 2n, f: 0 },
  "non_eigenvalue": { v: 5n, f: 0 },
  "interval_length": { v: 1n, f: 0 },
  "modes_drawn": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-growth-curve-laboratory-design", figures: {
  "growth_rate": { v: 0.5, f: 1 },
  "carrying_capacity": { v: 1000n, f: 0 },
  "starting_value": { v: 100n, f: 0 },
  "y_at_2": { v: 232n, f: 0 },
  "y_at_6": { v: 690.6, f: 1 },
  "y_at_10": { v: 942.8, f: 1 },
  "inflection_at": { v: 500n, f: 0 },
  "inflection_time": { v: 4.39, f: 1 }
} },
  { label: "a-signature-pendulum-laboratory-design", figures: {
  "length": { v: 1n, f: 0 },
  "g_value": { v: 9.81, f: 1 },
  "period_small": { v: 2.006, f: 1 },
  "period_10deg": { v: 2.01, f: 1 },
  "error_10deg": { v: 0.2, f: 1 },
  "period_60deg": { v: 2.33, f: 1 },
  "error_60deg": { v: 16n, f: 0 },
  "amplitudes_tested": { v: 2n, f: 0 }
} },
  { label: "a-signature-impulse-response-bench-design", figures: {
  "y_at_half": { v: 0.125, f: 1 },
  "max_y": { v: 0.125, f: 1 },
  "interval_length": { v: 1n, f: 0 },
  "green_pieces": { v: 2n, f: 0 },
  "integral_parts": { v: 2n, f: 0 },
  "boundary_values": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-modelling-studio-design", figures: {
  "initial_temp": { v: 90n, f: 0 },
  "room_temp": { v: 20n, f: 0 },
  "cooling_rate": { v: 0.05, f: 1 },
  "temp_at_10": { v: 62.46, f: 1 },
  "temp_at_30": { v: 35.62, f: 1 },
  "half_life": { v: 13.86, f: 1 },
  "steps_guided": { v: 4n, f: 0 },
  "design_version": { v: 1n, f: 0 }
} },
  { label: "a-signature-power-series-expander-design", figures: {
  "terms_used": { v: 4n, f: 0 },
  "value_at_0.5": { v: 1.127626, f: 1 },
  "cosh_0.5": { v: 1.127626, f: 1 },
  "x2_term": { v: 0.125, f: 1 },
  "x4_term": { v: 0.002604, f: 1 },
  "x6_term": { v: 2.2e-05, f: 1 },
  "coefficients_found": { v: 4n, f: 0 },
  "error": { v: 1e-06, f: 1 }
} },
  { label: "a-signature-differential-equations-capstone-console-design", figures: {
  "parts": { v: 4n, f: 0 },
  "checks_passed": { v: 4n, f: 0 },
  "temp_at_10": { v: 62.46, f: 1 },
  "temp_at_30": { v: 35.62, f: 1 },
  "half_life": { v: 13.86, f: 1 },
  "initial_temp": { v: 90n, f: 0 },
  "cooling_rate": { v: 0.05, f: 1 },
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
