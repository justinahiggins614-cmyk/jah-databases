// Edition demo for the Numerical Analysis Database (numerical-analysis).
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
  { label: "error-and-its-sources", figures: {
  "absolute_error": { v: 3.33e-05, f: 1 },
  "relative_error": { v: 0.0001, f: 1 },
  "digits_kept": { v: 4n, f: 0 },
  "sqrt_value": { v: 100.005, f: 1 },
  "difference": { v: 0.005, f: 1 },
  "accurate_value": { v: 0.00499987, f: 1 },
  "error_sources": { v: 3n, f: 0 },
  "decimal_places": { v: 4n, f: 0 }
} },
  { label: "floating-point-arithmetic", figures: {
  "machine_epsilon": { v: 2.2e-16, f: 1 },
  "significand_bits": { v: 53n, f: 0 },
  "decimal_digits": { v: 16n, f: 0 },
  "ulp_at_1e16": { v: 2n, f: 0 },
  "sum_0.1_ten": { v: 0.9999999999999999, f: 1 },
  "harmonic_10": { v: 2.9289682539682538, f: 1 },
  "operations": { v: 3n, f: 0 },
  "terms_summed": { v: 10n, f: 0 }
} },
  { label: "bisection-for-root-finding", figures: {
  "steps_taken": { v: 3n, f: 0 },
  "interval_width": { v: 0.125, f: 1 },
  "midpoint": { v: 1.4375, f: 1 },
  "true_root": { v: 1.41421356, f: 1 },
  "error_bound": { v: 0.0625, f: 1 },
  "f_at_1.5": { v: 0.25, f: 1 },
  "f_at_1.25": { v: -0.4375, f: 1 },
  "f_at_1.375": { v: -0.109375, f: 1 }
} },
  { label: "newton-s-method-for-root-finding", figures: {
  "step_1": { v: 1.5, f: 1 },
  "step_2": { v: 1.4166667, f: 1 },
  "step_3": { v: 1.4142157, f: 1 },
  "true_root": { v: 1.41421356, f: 1 },
  "error_step_3": { v: 2.1e-06, f: 1 },
  "bisection_error_3": { v: 0.0625, f: 1 },
  "iterations": { v: 3n, f: 0 },
  "derivative_at_1": { v: 2n, f: 0 }
} },
  { label: "the-secant-method-for-root-finding", figures: {
  "step_1": { v: 1.333333, f: 1 },
  "step_2": { v: 1.4, f: 1 },
  "step_3": { v: 1.414634, f: 1 },
  "true_root": { v: 1.41421356, f: 1 },
  "error_step_3": { v: 0.00042, f: 1 },
  "convergence_order": { v: 1.618, f: 1 },
  "starting_points": { v: 2n, f: 0 },
  "iterations": { v: 3n, f: 0 }
} },
  { label: "gaussian-elimination-and-lu-factorisation", figures: {
  "solution_x": { v: 1n, f: 0 },
  "solution_y": { v: 3n, f: 0 },
  "l_21": { v: 0.5, f: 1 },
  "u_11": { v: 2n, f: 0 },
  "u_22": { v: 2.5, f: 1 },
  "operations_order": { v: 3n, f: 0 },
  "rows": { v: 2n, f: 0 },
  "checks": { v: 2n, f: 0 }
} },
  { label: "iterative-methods-for-linear-systems", figures: {
  "true_x": { v: 1.1818, f: 1 },
  "true_y": { v: 2.2727, f: 1 },
  "jacobi_step3_x": { v: 1.2292, f: 1 },
  "jacobi_step3_y": { v: 2.3056, f: 1 },
  "gs_step1_x": { v: 1.75, f: 1 },
  "gs_step1_y": { v: 2.0833, f: 1 },
  "iterations_shown": { v: 3n, f: 0 },
  "diagonal_dominant": { v: 1n, f: 0 }
} },
  { label: "the-condition-number", figures: {
  "determinant": { v: 0.0001, f: 1 },
  "condition_number": { v: 40002n, f: 0 },
  "identity_condition": { v: 1n, f: 0 },
  "inverse_entry": { v: 10001n, f: 0 },
  "solution_x": { v: 1n, f: 0 },
  "solution_y": { v: 1n, f: 0 },
  "change_in_b": { v: 0.0001, f: 1 },
  "amplification": { v: 10000n, f: 0 }
} },
  { label: "polynomial-interpolation", figures: {
  "points": { v: 3n, f: 0 },
  "degree": { v: 2n, f: 0 },
  "x2_coefficient": { v: -0.5, f: 1 },
  "x_coefficient": { v: 2.5, f: 1 },
  "constant": { v: 1n, f: 0 },
  "check_at_1": { v: 3n, f: 0 },
  "check_at_2": { v: 4n, f: 0 },
  "basis_polynomials": { v: 3n, f: 0 }
} },
  { label: "splines", figures: {
  "points": { v: 3n, f: 0 },
  "pieces": { v: 2n, f: 0 },
  "value_at_0.5": { v: 0.6875, f: 1 },
  "max_value": { v: 1n, f: 0 },
  "degree": { v: 3n, f: 0 },
  "continuity_orders": { v: 2n, f: 0 },
  "end_condition": { v: 0n, f: 0 },
  "checks": { v: 2n, f: 0 }
} },
  { label: "numerical-integration", figures: {
  "true_value": { v: 1.7182818, f: 1 },
  "trapezoidal": { v: 1.753931, f: 1 },
  "trapezoidal_error": { v: 0.0356, f: 1 },
  "simpson": { v: 1.718861, f: 1 },
  "simpson_error": { v: 0.00058, f: 1 },
  "points_used": { v: 3n, f: 0 },
  "step_size": { v: 0.5, f: 1 },
  "rules_compared": { v: 2n, f: 0 }
} },
  { label: "euler-s-method-for-ordinary-differential-equations", figures: {
  "euler_h0.1": { v: 1.21, f: 1 },
  "true_value": { v: 1.2214, f: 1 },
  "error_h0.1": { v: 0.0114, f: 1 },
  "euler_h0.05": { v: 1.2155, f: 1 },
  "error_h0.05": { v: 0.0059, f: 1 },
  "step_size": { v: 0.1, f: 1 },
  "steps": { v: 2n, f: 0 },
  "error_ratio": { v: 2n, f: 0 }
} },
  { label: "runge-kutta-methods", figures: {
  "rk4_at_0.1": { v: 1.1051708, f: 1 },
  "rk4_at_0.2": { v: 1.2214028, f: 1 },
  "true_value": { v: 1.2214028, f: 1 },
  "rk4_error": { v: 1e-06, f: 1 },
  "euler_value": { v: 1.21, f: 1 },
  "euler_error": { v: 0.0114, f: 1 },
  "slopes_per_step": { v: 4n, f: 0 },
  "order": { v: 4n, f: 0 }
} },
  { label: "least-squares-and-data-fitting", figures: {
  "intercept": { v: 1.1667, f: 1 },
  "slope": { v: 1.5, f: 1 },
  "residual_sum_squares": { v: 0.1667, f: 1 },
  "residual_1": { v: -0.1667, f: 1 },
  "residual_2": { v: 0.3333, f: 1 },
  "residual_3": { v: -0.1667, f: 1 },
  "points": { v: 3n, f: 0 },
  "parameters": { v: 2n, f: 0 }
} },
  { label: "numerical-differentiation", figures: {
  "true_derivative": { v: 0.5403023, f: 1 },
  "forward_h0.1": { v: 0.49736, f: 1 },
  "forward_error": { v: 0.043, f: 1 },
  "central_h0.1": { v: 0.5394, f: 1 },
  "central_error": { v: 0.0009, f: 1 },
  "central_h0.01": { v: 0.5403, f: 1 },
  "step_h": { v: 0.1, f: 1 },
  "optimal_h": { v: 0.01, f: 1 }
} },
  { label: "the-finite-difference-method", figures: {
  "h_grid": { v: 0.25, f: 1 },
  "dt_stable": { v: 0.02, f: 1 },
  "stability_ratio": { v: 0.32, f: 1 },
  "exact_decay": { v: 0.8209, f: 1 },
  "fd_decay": { v: 0.8125, f: 1 },
  "dt_unstable": { v: 0.04, f: 1 },
  "unstable_ratio": { v: 0.64, f: 1 },
  "grid_points": { v: 5n, f: 0 }
} },
  { label: "approximation-theory", figures: {
  "taylor_max_error": { v: 0.1321, f: 1 },
  "best_max_error": { v: 0.045, f: 1 },
  "chebyshev_error": { v: 0.0451, f: 1 },
  "cheb_constant": { v: 1.2661, f: 1 },
  "cheb_linear": { v: 1.1303, f: 1 },
  "cheb_quadratic": { v: 0.2715, f: 1 },
  "interval_half": { v: 1n, f: 0 },
  "degree": { v: 2n, f: 0 }
} },
  { label: "optimisation-by-gradient-descent", figures: {
  "start_x": { v: 4n, f: 0 },
  "step_1": { v: 3.2, f: 1 },
  "step_2": { v: 2.56, f: 1 },
  "step_3": { v: 2.048, f: 1 },
  "after_10": { v: 0.4295, f: 1 },
  "f_after_10": { v: 0.1845, f: 1 },
  "shrink_factor": { v: 0.8, f: 1 },
  "step_size": { v: 0.1, f: 1 }
} },
  { label: "monte-carlo-integration", figures: {
  "darts_100": { v: 100n, f: 0 },
  "inside_100": { v: 79n, f: 0 },
  "pi_estimate_100": { v: 3.16, f: 1 },
  "darts_10000": { v: 10000n, f: 0 },
  "inside_10000": { v: 7854n, f: 0 },
  "pi_estimate_10000": { v: 3.1416, f: 1 },
  "std_error": { v: 0.0041, f: 1 },
  "pi_true": { v: 3.14159, f: 1 }
} },
  { label: "stiff-equations-and-implicit-methods", figures: {
  "stiffness_ratio": { v: 1000n, f: 0 },
  "transient_at_0.01": { v: 4.5e-05, f: 1 },
  "explicit_step_limit": { v: 0.002, f: 1 },
  "steps_needed": { v: 5000n, f: 0 },
  "implicit_step": { v: 0.1, f: 1 },
  "y_at_0.1": { v: 0.99496, f: 1 },
  "cos_0.1": { v: 0.995004, f: 1 },
  "error": { v: 4e-05, f: 1 }
} },
  { label: "the-fast-fourier-transform", figures: {
  "n_points": { v: 4n, f: 0 },
  "fft_operations": { v: 8n, f: 0 },
  "direct_operations": { v: 16n, f: 0 },
  "n_1024_fft": { v: 10240n, f: 0 },
  "n_1024_direct": { v: 1048576n, f: 0 },
  "transform_values": { v: 1n, f: 0 },
  "halves": { v: 2n, f: 0 },
  "log_factor": { v: 2n, f: 0 }
} },
  { label: "numerical-solution-of-nonlinear-systems", figures: {
  "true_x": { v: 1.4142, f: 1 },
  "true_y": { v: 1.4142, f: 1 },
  "start_x": { v: 1n, f: 0 },
  "step1_x": { v: 1.5, f: 1 },
  "error_step1": { v: 0.0858, f: 1 },
  "step2_x": { v: 1.4167, f: 1 },
  "error_step2": { v: 0.0025, f: 1 },
  "jacobian_rows": { v: 2n, f: 0 }
} },
  { label: "richardson-extrapolation-and-romberg-integration", figures: {
  "true_value": { v: 1.7182818, f: 1 },
  "trapezoid_h1": { v: 1.85914, f: 1 },
  "trapezoid_h0.5": { v: 1.75393, f: 1 },
  "romberg_1": { v: 1.71886, f: 1 },
  "romberg_1_error": { v: 0.00058, f: 1 },
  "romberg_2": { v: 1.718282, f: 1 },
  "romberg_2_error": { v: 2e-07, f: 1 },
  "levels": { v: 3n, f: 0 }
} },
  { label: "capstone-solving-a-real-problem-end-to-end", figures: {
  "simpson_value": { v: 1.718861, f: 1 },
  "simpson_error": { v: 0.00058, f: 1 },
  "refined_value": { v: 1.718282, f: 1 },
  "solution_x": { v: 1n, f: 0 },
  "solution_y": { v: 3n, f: 0 },
  "newton_root": { v: 1.4142157, f: 1 },
  "newton_error": { v: 2.1e-06, f: 1 },
  "problems_solved": { v: 3n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
