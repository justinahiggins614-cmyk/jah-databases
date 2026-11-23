// Edition demo for the Classical Mechanics Database (college-classical-mechanics).
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
  { label: "kinematics-and-the-description-of-motion", figures: {
  "initial_speed": { v: 20n, f: 0 },
  "max_height": { v: 22.4, f: 1 },
  "time_to_top": { v: 2.04, f: 1 },
  "total_time": { v: 4.18, f: 1 },
  "landing_speed": { v: 21n, f: 0 },
  "g_acceleration": { v: 9.8, f: 1 },
  "launch_height": { v: 2n, f: 0 },
  "velocity_zero_time": { v: 2.04, f: 1 }
} },
  { label: "newton-s-laws-of-motion", figures: {
  "mass_kg": { v: 2n, f: 0 },
  "force_N": { v: 10n, f: 0 },
  "acceleration": { v: 5n, f: 0 },
  "time_s": { v: 3n, f: 0 },
  "speed_after": { v: 15n, f: 0 },
  "distance_m": { v: 22.5, f: 1 },
  "weight_N": { v: 19.6, f: 1 },
  "laws_count": { v: 3n, f: 0 }
} },
  { label: "work-energy-and-power", figures: {
  "mass_kg": { v: 2n, f: 0 },
  "height_m": { v: 10n, f: 0 },
  "energy_J": { v: 196n, f: 0 },
  "speed_ms": { v: 14n, f: 0 },
  "power_W": { v: 98n, f: 0 },
  "engine_kW": { v: 100n, f: 0 },
  "g_acceleration": { v: 9.8, f: 1 },
  "time_s": { v: 2n, f: 0 }
} },
  { label: "momentum-and-impulse", figures: {
  "mass_A": { v: 2n, f: 0 },
  "speed_A": { v: 3n, f: 0 },
  "mass_B": { v: 3n, f: 0 },
  "total_momentum": { v: 6n, f: 0 },
  "combined_speed": { v: 1.2, f: 1 },
  "energy_before": { v: 9n, f: 0 },
  "energy_after": { v: 3.6, f: 1 },
  "energy_lost": { v: 5.4, f: 1 }
} },
  { label: "rotational-motion-and-torque", figures: {
  "moment_of_inertia": { v: 0.5, f: 1 },
  "torque_Nm": { v: 2n, f: 0 },
  "angular_acceleration": { v: 4n, f: 0 },
  "time_s": { v: 3n, f: 0 },
  "angular_velocity": { v: 12n, f: 0 },
  "rpm": { v: 115n, f: 0 },
  "spin_double_factor": { v: 2n, f: 0 },
  "axes": { v: 3n, f: 0 }
} },
  { label: "gravitation-and-kepler-s-laws", figures: {
  "mars_au": { v: 1.524, f: 1 },
  "mars_period_years": { v: 1.88, f: 1 },
  "leo_speed_kms": { v: 7.7, f: 1 },
  "leo_period_min": { v: 92n, f: 0 },
  "leo_altitude_km": { v: 400n, f: 0 },
  "g_constant": { v: 6.674e-11, f: 1 },
  "moon_g": { v: 3.3e-05, f: 1 },
  "laws_count": { v: 3n, f: 0 }
} },
  { label: "oscillations-and-the-harmonic-oscillator", figures: {
  "mass_kg": { v: 0.5, f: 1 },
  "stiffness": { v: 20n, f: 0 },
  "omega": { v: 6.32, f: 1 },
  "frequency_Hz": { v: 1.01, f: 1 },
  "period_s": { v: 0.99, f: 1 },
  "amplitude_m": { v: 0.1, f: 1 },
  "pendulum_period": { v: 2.01, f: 1 },
  "resonance_Hz": { v: 1.01, f: 1 }
} },
  { label: "waves-and-sound", figures: {
  "sound_speed": { v: 343n, f: 0 },
  "frequency_Hz": { v: 440n, f: 0 },
  "wavelength_m": { v: 0.78, f: 1 },
  "string_length": { v: 1n, f: 0 },
  "wave_speed": { v: 200n, f: 0 },
  "fundamental_Hz": { v: 100n, f: 0 },
  "harmonics": { v: 4n, f: 0 },
  "nodes_per_wavelength": { v: 2n, f: 0 }
} },
  { label: "lagrangian-mechanics", figures: {
  "length_m": { v: 1n, f: 0 },
  "mass_kg": { v: 1n, f: 0 },
  "g_acceleration": { v: 9.8, f: 1 },
  "period_s": { v: 2.01, f: 1 },
  "coordinates": { v: 1n, f: 0 },
  "equations": { v: 1n, f: 0 },
  "symmetries": { v: 1n, f: 0 },
  "conserved": { v: 1n, f: 0 }
} },
  { label: "hamiltonian-mechanics-and-phase-space", figures: {
  "mass_kg": { v: 1n, f: 0 },
  "stiffness": { v: 1n, f: 0 },
  "energy": { v: 2n, f: 0 },
  "phase_radius": { v: 2n, f: 0 },
  "phase_area": { v: 12.566, f: 1 },
  "equations": { v: 2n, f: 0 },
  "coordinates": { v: 1n, f: 0 },
  "dimensions": { v: 2n, f: 0 }
} },
  { label: "rigid-bodies-and-euler-s-equations", figures: {
  "moments": { v: 3n, f: 0 },
  "principal_axes": { v: 3n, f: 0 },
  "unstable_axis": { v: 2n, f: 0 },
  "stable_axes": { v: 2n, f: 0 },
  "euler_equations": { v: 3n, f: 0 },
  "moment_1": { v: 1n, f: 0 },
  "moment_2": { v: 2n, f: 0 },
  "moment_3": { v: 3n, f: 0 }
} },
  { label: "central-forces-and-orbital-motion", figures: {
  "radius_km": { v: 7000n, f: 0 },
  "speed_kms": { v: 7.5, f: 1 },
  "angular_momentum": { v: 52500n, f: 0 },
  "halved_speed": { v: 10.7, f: 1 },
  "transfer_type": { v: 1n, f: 0 },
  "conic_types": { v: 4n, f: 0 },
  "conserved": { v: 1n, f: 0 },
  "dimensions": { v: 2n, f: 0 }
} },
  { label: "non-inertial-frames-and-fictitious-forces", figures: {
  "omega": { v: 7.27e-05, f: 1 },
  "centrifugal_acc": { v: 0.034, f: 1 },
  "gravity_fraction": { v: 0.0035, f: 1 },
  "latitude_deg": { v: 40n, f: 0 },
  "precession_rate": { v: 4.67e-05, f: 1 },
  "precession_hours": { v: 37n, f: 0 },
  "earth_radius_km": { v: 6371n, f: 0 },
  "forces": { v: 3n, f: 0 }
} },
  { label: "fluids-at-rest-and-in-motion", figures: {
  "ship_displacement_t": { v: 10000n, f: 0 },
  "buoyant_force_MN": { v: 98n, f: 0 },
  "pipe_diameter_1": { v: 10n, f: 0 },
  "pipe_diameter_2": { v: 5n, f: 0 },
  "speed_1": { v: 1n, f: 0 },
  "speed_2": { v: 4n, f: 0 },
  "pressure_drop_Pa": { v: 7500n, f: 0 },
  "water_density": { v: 1000n, f: 0 }
} },
  { label: "elasticity-and-the-deformation-of-solids", figures: {
  "rod_length_m": { v: 2n, f: 0 },
  "cross_section_cm2": { v: 1n, f: 0 },
  "force_N": { v: 20000n, f: 0 },
  "stress_MPa": { v: 200n, f: 0 },
  "youngs_GPa": { v: 200n, f: 0 },
  "strain": { v: 0.001, f: 1 },
  "stretch_mm": { v: 2n, f: 0 },
  "deflection_factor": { v: 8n, f: 0 }
} },
  { label: "chaos-and-sensitive-dependence-on-initial-conditions", figures: {
  "angle_difference": { v: 0.001, f: 1 },
  "lyapunov": { v: 0.5, f: 1 },
  "separation_10s": { v: 0.148, f: 1 },
  "separation_20s": { v: 22n, f: 0 },
  "lorenz_lambda": { v: 0.9, f: 1 },
  "weather_horizon_days": { v: 14n, f: 0 },
  "systems": { v: 3n, f: 0 },
  "exponent_units": { v: 1n, f: 0 }
} },
  { label: "special-relativity-and-the-limits-of-newton", figures: {
  "speed_fraction": { v: 0.6, f: 1 },
  "gamma": { v: 1.25, f: 1 },
  "ship_time_s": { v: 10n, f: 0 },
  "earth_time_s": { v: 12.5, f: 1 },
  "ship_length_m": { v: 100n, f: 0 },
  "observed_length_m": { v: 80n, f: 0 },
  "kinetic_fraction": { v: 0.25, f: 1 },
  "newtonian_fraction": { v: 0.18, f: 1 }
} },
  { label: "the-three-body-problem", figures: {
  "l1_distance_km": { v: 1500000n, f: 0 },
  "l2_distance_km": { v: 1500000n, f: 0 },
  "lagrange_points": { v: 5n, f: 0 },
  "trojan_groups": { v: 2n, f: 0 },
  "bodies": { v: 3n, f: 0 },
  "special_solutions": { v: 2n, f: 0 },
  "jwst_location": { v: 2n, f: 0 },
  "years_since": { v: 1772n, f: 0 }
} },
  { label: "damped-and-driven-oscillations", figures: {
  "mass_kg": { v: 1n, f: 0 },
  "stiffness": { v: 100n, f: 0 },
  "omega": { v: 10n, f: 0 },
  "period_s": { v: 0.63, f: 1 },
  "damping_b": { v: 2n, f: 0 },
  "decay_rate": { v: 1n, f: 0 },
  "half_life_s": { v: 0.69, f: 1 },
  "critical_damping": { v: 20n, f: 0 }
} },
  { label: "the-pendulum-exact-and-approximate", figures: {
  "length_m": { v: 1n, f: 0 },
  "small_period_s": { v: 2.007, f: 1 },
  "amplitude_60_deg": { v: 60n, f: 0 },
  "factor_60": { v: 1.0685, f: 1 },
  "period_60_s": { v: 2.144, f: 1 },
  "factor_170": { v: 2.44, f: 1 },
  "period_170_s": { v: 4.9, f: 1 },
  "g_acceleration": { v: 9.8, f: 1 }
} },
  { label: "conservation-laws-and-noether-s-theorem", figures: {
  "symmetries": { v: 3n, f: 0 },
  "conserved_quantities": { v: 3n, f: 0 },
  "components": { v: 3n, f: 0 },
  "theorem_year": { v: 1918n, f: 0 },
  "kepler_law": { v: 2n, f: 0 },
  "energy_conserved": { v: 1n, f: 0 },
  "momentum_conserved": { v: 1n, f: 0 },
  "angular_conserved": { v: 1n, f: 0 }
} },
  { label: "the-calculus-of-variations-and-least-action", figures: {
  "brachistochrone_year": { v: 1696n, f: 0 },
  "least_time_year": { v: 1662n, f: 0 },
  "lagrange_year": { v: 1788n, f: 0 },
  "paths_compared": { v: 3n, f: 0 },
  "principles": { v: 2n, f: 0 },
  "equations": { v: 1n, f: 0 },
  "dimensions": { v: 3n, f: 0 },
  "cycloid": { v: 1n, f: 0 }
} },
  { label: "coupled-oscillators-and-normal-modes", figures: {
  "masses": { v: 2n, f: 0 },
  "springs": { v: 3n, f: 0 },
  "omega_1": { v: 3.16, f: 1 },
  "omega_2": { v: 5.48, f: 1 },
  "k_stiffness": { v: 10n, f: 0 },
  "mass_kg": { v: 1n, f: 0 },
  "beat_period_s": { v: 2.71, f: 1 },
  "modes": { v: 2n, f: 0 }
} },
  { label: "a-capstone-space-mission-design", figures: {
  "escape_speed_kms": { v: 11.2, f: 1 },
  "transfer_days": { v: 259n, f: 0 },
  "semi_major_axis_au": { v: 1.262, f: 1 },
  "transfer_period_years": { v: 1.42, f: 1 },
  "arrival_vinf_kms": { v: 2.6, f: 1 },
  "entry_speed_kms": { v: 5.7, f: 1 },
  "delta_v_earth": { v: 3.6, f: 1 },
  "delta_v_mars": { v: 2.6, f: 1 },
  "viking_year": { v: 1976n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
