// Edition demo for the Computer Architecture Database (computer-architecture).
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
  { label: "the-von-neumann-model-and-the-stored-program", figures: {
  "instructions": { v: 5n, f: 0 },
  "addresses_used": { v: 3n, f: 0 },
  "program_counter_start": { v: 0n, f: 0 },
  "program_counter_end": { v: 5n, f: 0 },
  "components": { v: 4n, f: 0 },
  "first_computer_year": { v: 1948n, f: 0 },
  "report_year": { v: 1945n, f: 0 },
  "memory_paths": { v: 1n, f: 0 }
} },
  { label: "the-central-processing-unit", figures: {
  "clock_GHz": { v: 3n, f: 0 },
  "cpi": { v: 1.5, f: 1 },
  "instructions_per_second": { v: 2000000000n, f: 0 },
  "mips": { v: 2000n, f: 0 },
  "program_instructions": { v: 1000000000n, f: 0 },
  "time_seconds": { v: 0.5, f: 1 },
  "first_cpu_year": { v: 1971n, f: 0 },
  "first_clock_kHz": { v: 740n, f: 0 }
} },
  { label: "instruction-set-architecture", figures: {
  "risc_instruction_bits": { v: 32n, f: 0 },
  "opcode_bits": { v: 7n, f: 0 },
  "register_bits": { v: 5n, f: 0 },
  "risc_instructions": { v: 3n, f: 0 },
  "cisc_instructions": { v: 1n, f: 0 },
  "risc_cycles": { v: 1n, f: 0 },
  "arm_devices_billions": { v: 200n, f: 0 },
  "isa_families": { v: 2n, f: 0 }
} },
  { label: "assembly-language-and-machine-code", figures: {
  "instructions": { v: 4n, f: 0 },
  "bytes": { v: 16n, f: 0 },
  "add_machine_code": { v: 6456115n, f: 0 },
  "loads": { v: 2n, f: 0 },
  "stores": { v: 1n, f: 0 },
  "adds": { v: 1n, f: 0 },
  "first_assembler_year": { v: 1949n, f: 0 },
  "opcode_bits": { v: 7n, f: 0 }
} },
  { label: "pipelining", figures: {
  "stages": { v: 5n, f: 0 },
  "instructions": { v: 100n, f: 0 },
  "pipelined_cycles": { v: 104n, f: 0 },
  "unpipelined_cycles": { v: 500n, f: 0 },
  "speedup": { v: 4.8, f: 1 },
  "hazard_stall": { v: 1n, f: 0 },
  "mispredict_cost": { v: 3n, f: 0 },
  "fill_cycles": { v: 5n, f: 0 }
} },
  { label: "caches-and-the-memory-hierarchy", figures: {
  "cache_KB": { v: 64n, f: 0 },
  "line_bytes": { v: 64n, f: 0 },
  "lines": { v: 1024n, f: 0 },
  "ways": { v: 4n, f: 0 },
  "sets": { v: 256n, f: 0 },
  "offset_bits": { v: 6n, f: 0 },
  "index_bits": { v: 8n, f: 0 },
  "tag_bits": { v: 18n, f: 0 }
} },
  { label: "main-memory-and-dram", figures: {
  "latency_ns": { v: 100n, f: 0 },
  "bandwidth_GBs": { v: 20n, f: 0 },
  "line_bytes": { v: 64n, f: 0 },
  "line_time_ns": { v: 103n, f: 0 },
  "sequential_us": { v: 50n, f: 0 },
  "random_ms": { v: 1.6, f: 1 },
  "slowdown": { v: 32n, f: 0 },
  "refresh_interval_ms": { v: 64n, f: 0 }
} },
  { label: "virtual-memory-and-paging", figures: {
  "page_size_KB": { v: 4n, f: 0 },
  "page_number": { v: 74565n, f: 0 },
  "offset": { v: 1656n, f: 0 },
  "frame": { v: 703710n, f: 0 },
  "tlb_hit_cycles": { v: 1n, f: 0 },
  "page_walk_cycles": { v: 100n, f: 0 },
  "fault_ms": { v: 10n, f: 0 },
  "fault_cycles": { v: 10000000n, f: 0 }
} },
  { label: "input-output-and-interrupts", figures: {
  "packet_interval_us": { v: 100n, f: 0 },
  "poll_interval_us": { v: 10n, f: 0 },
  "poll_waste": { v: 10n, f: 0 },
  "interrupt_overhead_pct": { v: 5n, f: 0 },
  "dma_speed_MBs": { v: 500n, f: 0 },
  "dma_time_ms": { v: 2n, f: 0 },
  "packet_size_KB": { v: 1n, f: 0 },
  "methods": { v: 3n, f: 0 }
} },
  { label: "parallelism-and-amdahl-s-law", figures: {
  "parallel_fraction": { v: 0.9, f: 1 },
  "cores": { v: 8n, f: 0 },
  "speedup_8": { v: 4.7, f: 1 },
  "speedup_infinite": { v: 10n, f: 0 },
  "serial_time_s": { v: 100n, f: 0 },
  "parallel_time_s": { v: 21n, f: 0 },
  "law_year": { v: 1967n, f: 0 },
  "max_with_20pct_serial": { v: 5n, f: 0 }
} },
  { label: "superscalar-and-out-of-order-execution", figures: {
  "issue_width": { v: 4n, f: 0 },
  "ipc": { v: 3n, f: 0 },
  "instructions": { v: 3000000000n, f: 0 },
  "cycles": { v: 1000000000n, f: 0 },
  "time_seconds": { v: 0.33, f: 1 },
  "rob_entries": { v: 128n, f: 0 },
  "miss_latency": { v: 100n, f: 0 },
  "mispredict_cost": { v: 15n, f: 0 }
} },
  { label: "branch-prediction", figures: {
  "loop_iterations": { v: 1000n, f: 0 },
  "taken": { v: 999n, f: 0 },
  "mispredictions": { v: 2n, f: 0 },
  "mispredict_cost": { v: 15n, f: 0 },
  "total_cost": { v: 30n, f: 0 },
  "overhead_pct": { v: 3n, f: 0 },
  "random_accuracy": { v: 0.5, f: 1 },
  "random_cost": { v: 7.5, f: 1 }
} },
  { label: "graphics-processing-units", figures: {
  "gpu_cores": { v: 10000n, f: 0 },
  "gpu_clock_GHz": { v: 1.5, f: 1 },
  "gpu_tflops": { v: 30n, f: 0 },
  "matrix_size": { v: 4096n, f: 0 },
  "operations": { v: 137400000000n, f: 0 },
  "gpu_time_ms": { v: 4.6, f: 1 },
  "cpu_tflops": { v: 1n, f: 0 },
  "cpu_time_ms": { v: 137n, f: 0 }
} },
  { label: "storage-disks-ssds-and-flash", figures: {
  "hdd_seek_ms": { v: 10n, f: 0 },
  "ssd_latency_ms": { v: 0.1, f: 1 },
  "random_blocks": { v: 1000n, f: 0 },
  "hdd_random_s": { v: 10n, f: 0 },
  "ssd_random_s": { v: 0.1, f: 1 },
  "speedup": { v: 100n, f: 0 },
  "hdd_seq_MBs": { v: 200n, f: 0 },
  "ssd_seq_MBs": { v: 500n, f: 0 }
} },
  { label: "networks-and-interconnection", figures: {
  "link_Gbps": { v: 100n, f: 0 },
  "one_GB_seconds": { v: 0.08, f: 1 },
  "fibre_us_per_km": { v: 5n, f: 0 },
  "distance_km": { v: 1000n, f: 0 },
  "one_way_ms": { v: 5n, f: 0 },
  "machines": { v: 10000n, f: 0 },
  "bisection_TBs": { v: 10n, f: 0 },
  "ny_london_ms": { v: 70n, f: 0 }
} },
  { label: "moore-s-law-and-the-end-of-dennard-scaling", figures: {
  "transistors_2005": { v: 1000000000n, f: 0 },
  "doubling_years": { v: 2n, f: 0 },
  "transistors_2023": { v: 100000000000n, f: 0 },
  "clock_1995_MHz": { v: 100n, f: 0 },
  "clock_2005_GHz": { v: 3n, f: 0 },
  "clock_now_GHz": { v: 5n, f: 0 },
  "cores_now": { v: 64n, f: 0 },
  "power_wall_W": { v: 300n, f: 0 }
} },
  { label: "risc-versus-cisc", figures: {
  "risc_instructions": { v: 4n, f: 0 },
  "cisc_instructions": { v: 1n, f: 0 },
  "cisc_cycles": { v: 3n, f: 0 },
  "cisc_bytes": { v: 6n, f: 0 },
  "risc_program": { v: 1000n, f: 0 },
  "risc_cpi": { v: 1n, f: 0 },
  "cisc_program": { v: 400n, f: 0 },
  "cisc_cpi": { v: 2.5, f: 1 }
} },
  { label: "the-memory-wall", figures: {
  "cpu_cycle_ns": { v: 0.33, f: 1 },
  "dram_latency_ns": { v: 100n, f: 0 },
  "latency_cycles": { v: 300n, f: 0 },
  "miss_rate": { v: 0.05, f: 1 },
  "avg_access_cycles": { v: 5.95, f: 1 },
  "peak_ops": { v: 3000000000n, f: 0 },
  "memory_bound_ops": { v: 10000000n, f: 0 },
  "slowdown": { v: 300n, f: 0 }
} },
  { label: "power-energy-and-dark-silicon", figures: {
  "capacitance_nF": { v: 1n, f: 0 },
  "voltage_V": { v: 1n, f: 0 },
  "frequency_GHz": { v: 3n, f: 0 },
  "power_per_block_W": { v: 3n, f: 0 },
  "blocks": { v: 30n, f: 0 },
  "total_power_W": { v: 90n, f: 0 },
  "half_voltage_power_W": { v: 0.75, f: 1 },
  "budget_W": { v: 100n, f: 0 }
} },
  { label: "reliability-ecc-and-fault-tolerance", figures: {
  "ram_TB": { v: 1n, f: 0 },
  "modules": { v: 128n, f: 0 },
  "module_GB": { v: 8n, f: 0 },
  "errors_per_month": { v: 128n, f: 0 },
  "errors_per_day": { v: 4n, f: 0 },
  "raid_disks": { v: 5n, f: 0 },
  "tolerated_failures": { v: 1n, f: 0 },
  "rebuild_hours": { v: 10n, f: 0 }
} },
  { label: "benchmarking-and-performance-measurement", figures: {
  "time_X_s": { v: 10n, f: 0 },
  "time_Y_s": { v: 8n, f: 0 },
  "speedup": { v: 1.25, f: 1 },
  "suite_mean": { v: 1.3, f: 1 },
  "instructions": { v: 2000000000n, f: 0 },
  "cpi_Y": { v: 1.2, f: 1 },
  "cpi_X": { v: 1.5, f: 1 },
  "clock_GHz": { v: 3n, f: 0 }
} },
  { label: "the-fetch-decode-execute-cycle-in-detail", figures: {
  "cycles": { v: 4n, f: 0 },
  "instruction_bytes": { v: 4n, f: 0 },
  "clock_GHz": { v: 3n, f: 0 },
  "time_ns": { v: 1.33, f: 1 },
  "stages": { v: 3n, f: 0 },
  "addresses": { v: 3n, f: 0 },
  "registers_used": { v: 2n, f: 0 },
  "report_year": { v: 1945n, f: 0 }
} },
  { label: "instruction-level-parallelism-and-vliw", figures: {
  "operations_per_iteration": { v: 4n, f: 0 },
  "scalar_cycles": { v: 4n, f: 0 },
  "superscalar_cycles": { v: 1n, f: 0 },
  "speedup": { v: 4n, f: 0 },
  "vliw_slots": { v: 4n, f: 0 },
  "dependent_cycles": { v: 4n, f: 0 },
  "typical_ilp": { v: 2.5, f: 1 },
  "issue_width": { v: 4n, f: 0 }
} },
  { label: "a-capstone-small-cpu-design", figures: {
  "clock_GHz": { v: 3n, f: 0 },
  "cpi": { v: 1.2, f: 1 },
  "program_instructions": { v: 1000000000n, f: 0 },
  "time_seconds": { v: 0.4, f: 1 },
  "pipeline_cycles": { v: 104n, f: 0 },
  "cache_KB": { v: 64n, f: 0 },
  "avg_access_cycles": { v: 5.95, f: 1 },
  "power_W": { v: 90n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
