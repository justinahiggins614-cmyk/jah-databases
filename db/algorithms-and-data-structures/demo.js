// Edition demo for the Algorithms and Data Structures Database (algorithms-and-data-structures).
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
  { label: "big-o-notation-and-growth-rates", figures: {
  "n_items": { v: 1000000n, f: 0 },
  "nlogn_comparisons": { v: 20000000n, f: 0 },
  "nlogn_seconds": { v: 0.02, f: 1 },
  "nsquared_comparisons": { v: 500000000000n, f: 0 },
  "nsquared_seconds": { v: 500n, f: 0 },
  "doubled_nlogn_seconds": { v: 0.042, f: 1 },
  "doubled_nsquared_seconds": { v: 2000n, f: 0 },
  "growth_classes": { v: 6n, f: 0 }
} },
  { label: "arrays-and-linked-lists", figures: {
  "array_size": { v: 1000000n, f: 0 },
  "array_bytes": { v: 4000000n, f: 0 },
  "array_access_steps": { v: 1n, f: 0 },
  "array_insert_shifts": { v: 1000000n, f: 0 },
  "insert_time_ms": { v: 1n, f: 0 },
  "list_reach_steps": { v: 500000n, f: 0 },
  "list_reach_ms": { v: 0.5, f: 1 },
  "amortised_append": { v: 1n, f: 0 }
} },
  { label: "stacks-and-queues", figures: {
  "stack_max_items": { v: 2n, f: 0 },
  "expression_result": { v: 14n, f: 0 },
  "queue_jobs": { v: 100n, f: 0 },
  "last_wait_s": { v: 99n, f: 0 },
  "recursion_depth": { v: 10000n, f: 0 },
  "operations": { v: 2n, f: 0 },
  "structures": { v: 2n, f: 0 },
  "cost_per_op": { v: 1n, f: 0 }
} },
  { label: "binary-search", figures: {
  "array_size": { v: 1000000n, f: 0 },
  "binary_comparisons": { v: 20n, f: 0 },
  "linear_comparisons": { v: 500000n, f: 0 },
  "dictionary_words": { v: 100000n, f: 0 },
  "dictionary_comparisons": { v: 17n, f: 0 },
  "halvings": { v: 20n, f: 0 },
  "midpoint_bug_year": { v: 2006n, f: 0 },
  "first_year": { v: 1946n, f: 0 }
} },
  { label: "sorting-and-comparison-sorts", figures: {
  "n_items": { v: 1000000n, f: 0 },
  "merge_comparisons": { v: 20000000n, f: 0 },
  "merge_seconds": { v: 0.04, f: 1 },
  "quicksort_worst": { v: 500000000000n, f: 0 },
  "quicksort_worst_seconds": { v: 500n, f: 0 },
  "lower_bound": { v: 18500000n, f: 0 },
  "sorts_compared": { v: 3n, f: 0 },
  "decision_tree": { v: 1n, f: 0 }
} },
  { label: "quicksort-and-the-pivot", figures: {
  "n_items": { v: 1000000n, f: 0 },
  "expected_comparisons": { v: 27600000n, f: 0 },
  "expected_seconds": { v: 0.028, f: 1 },
  "worst_comparisons": { v: 500000000000n, f: 0 },
  "worst_seconds": { v: 500n, f: 0 },
  "ln_n": { v: 13.8, f: 1 },
  "pivot_choices": { v: 3n, f: 0 },
  "invented_year": { v: 1961n, f: 0 }
} },
  { label: "merge-sort-and-divide-and-conquer", figures: {
  "example_n": { v: 8n, f: 0 },
  "merge_steps": { v: 7n, f: 0 },
  "levels": { v: 20n, f: 0 },
  "n_items": { v: 1000000n, f: 0 },
  "operations": { v: 20000000n, f: 0 },
  "extra_space": { v: 1000000n, f: 0 },
  "stable": { v: 1n, f: 0 },
  "invented_year": { v: 1945n, f: 0 }
} },
  { label: "heaps-and-priority-queues", figures: {
  "n_items": { v: 1000000n, f: 0 },
  "build_ops": { v: 1000000n, f: 0 },
  "remove_steps": { v: 20n, f: 0 },
  "removals": { v: 10n, f: 0 },
  "insert_steps": { v: 20n, f: 0 },
  "inserts": { v: 1000n, f: 0 },
  "heapsort_steps": { v: 20000000n, f: 0 },
  "top_index": { v: 0n, f: 0 }
} },
  { label: "hash-tables", figures: {
  "buckets": { v: 1000000n, f: 0 },
  "items": { v: 700000n, f: 0 },
  "load_factor": { v: 0.7, f: 1 },
  "expected_checks": { v: 1n, f: 0 },
  "longest_chain": { v: 5n, f: 0 },
  "doubled_buckets": { v: 2000000n, f: 0 },
  "new_load_factor": { v: 0.35, f: 1 },
  "worst_case": { v: 700000n, f: 0 }
} },
  { label: "binary-search-trees", figures: {
  "sorted_height": { v: 7n, f: 0 },
  "balanced_height": { v: 3n, f: 0 },
  "n_items": { v: 1000000n, f: 0 },
  "redblack_max_height": { v: 40n, f: 0 },
  "search_steps_balanced": { v: 3n, f: 0 },
  "search_steps_chain": { v: 7n, f: 0 },
  "balance_types": { v: 2n, f: 0 },
  "avl_year": { v: 1962n, f: 0 }
} },
  { label: "graphs-and-their-representations", figures: {
  "vertices": { v: 10000n, f: 0 },
  "edges": { v: 30000n, f: 0 },
  "list_entries": { v: 70000n, f: 0 },
  "matrix_entries": { v: 100000000n, f: 0 },
  "ratio": { v: 1400n, f: 0 },
  "avg_degree": { v: 6n, f: 0 },
  "users": { v: 1000000000n, f: 0 },
  "friendships": { v: 100000000000n, f: 0 }
} },
  { label: "breadth-first-and-depth-first-search", figures: {
  "maze_cells": { v: 10000n, f: 0 },
  "maze_passages": { v: 20000n, f: 0 },
  "bfs_steps": { v: 10000n, f: 0 },
  "vertices": { v: 1000000n, f: 0 },
  "edges": { v: 5000000n, f: 0 },
  "total_steps": { v: 6000000n, f: 0 },
  "time_seconds": { v: 0.006, f: 1 },
  "searches": { v: 2n, f: 0 }
} },
  { label: "dijkstra-s-shortest-path-algorithm", figures: {
  "vertices": { v: 10000n, f: 0 },
  "edges": { v: 30000n, f: 0 },
  "heap_steps": { v: 14n, f: 0 },
  "total_steps": { v: 560000n, f: 0 },
  "time_ms": { v: 1n, f: 0 },
  "distance_km": { v: 500n, f: 0 },
  "published_year": { v: 1959n, f: 0 },
  "queue_max": { v: 10000n, f: 0 }
} },
  { label: "minimum-spanning-trees", figures: {
  "cities": { v: 5n, f: 0 },
  "roads": { v: 10n, f: 0 },
  "mst_edges": { v: 4n, f: 0 },
  "mst_cost": { v: 10n, f: 0 },
  "cheapest_edges": { v: 4n, f: 0 },
  "kruskal_year": { v: 1956n, f: 0 },
  "prim_year": { v: 1957n, f: 0 },
  "algorithms": { v: 2n, f: 0 }
} },
  { label: "dynamic-programming", figures: {
  "fib_n": { v: 50n, f: 0 },
  "naive_calls": { v: 40730022147n, f: 0 },
  "naive_seconds": { v: 41n, f: 0 },
  "dp_steps": { v: 50n, f: 0 },
  "fib_50": { v: 12586269025n, f: 0 },
  "knapsack_items": { v: 100n, f: 0 },
  "knapsack_capacity": { v: 1000n, f: 0 },
  "knapsack_entries": { v: 100000n, f: 0 }
} },
  { label: "greedy-algorithms", figures: {
  "activities": { v: 6n, f: 0 },
  "greedy_count": { v: 3n, f: 0 },
  "earliest_start_count": { v: 2n, f: 0 },
  "symbols": { v: 6n, f: 0 },
  "huffman_avg_bits": { v: 2.24, f: 1 },
  "fixed_bits": { v: 3n, f: 0 },
  "huffman_year": { v: 1952n, f: 0 },
  "examples": { v: 3n, f: 0 }
} },
  { label: "divide-and-conquer-and-the-master-theorem", figures: {
  "merge_a": { v: 2n, f: 0 },
  "merge_b": { v: 2n, f: 0 },
  "merge_result": { v: 1n, f: 0 },
  "karatsuba_a": { v: 3n, f: 0 },
  "karatsuba_exponent": { v: 1.585, f: 1 },
  "digits": { v: 1000n, f: 0 },
  "karatsuba_ops": { v: 56000n, f: 0 },
  "schoolbook_ops": { v: 1000000n, f: 0 }
} },
  { label: "recursion-and-the-call-stack", figures: {
  "factorial": { v: 120n, f: 0 },
  "stack_depth": { v: 6n, f: 0 },
  "fib_calls": { v: 40730022147n, f: 0 },
  "fib_seconds": { v: 41n, f: 0 },
  "iterative_steps": { v: 50n, f: 0 },
  "recursion_limit": { v: 1000n, f: 0 },
  "base_case": { v: 1n, f: 0 },
  "frames": { v: 6n, f: 0 }
} },
  { label: "tries-and-string-matching", figures: {
  "dictionary_words": { v: 100000n, f: 0 },
  "word_length": { v: 9n, f: 0 },
  "trie_steps": { v: 9n, f: 0 },
  "binary_steps": { v: 17n, f: 0 },
  "linear_steps": { v: 50000n, f: 0 },
  "text_length": { v: 1000000n, f: 0 },
  "kmp_steps": { v: 1000000n, f: 0 },
  "naive_steps": { v: 4000000n, f: 0 }
} },
  { label: "the-union-find-structure", figures: {
  "singletons": { v: 1000000n, f: 0 },
  "unions": { v: 500000n, f: 0 },
  "operations": { v: 1500000n, f: 0 },
  "tree_height": { v: 3n, f: 0 },
  "kruskal_edges": { v: 30000n, f: 0 },
  "kruskal_unions": { v: 10000n, f: 0 },
  "inverse_ackermann": { v: 5n, f: 0 },
  "time_ms": { v: 1n, f: 0 }
} },
  { label: "np-completeness-and-intractability", figures: {
  "cities_20": { v: 20n, f: 0 },
  "tours_20": { v: 60000000000000000n, f: 0 },
  "years_20": { v: 1900n, f: 0 },
  "cities_10": { v: 10n, f: 0 },
  "tours_10": { v: 181440n, f: 0 },
  "sat_variables": { v: 100n, f: 0 },
  "sat_assignments": { v: 1300000000000000000000000000000n, f: 0 },
  "heuristic_gap_pct": { v: 5n, f: 0 }
} },
  { label: "approximation-and-heuristics", figures: {
  "points": { v: 100n, f: 0 },
  "set_cover_factor": { v: 4.6, f: 1 },
  "optimal_tour_km": { v: 1000n, f: 0 },
  "heuristic_bound_km": { v: 2000n, f: 0 },
  "heuristic_practical_km": { v: 1100n, f: 0 },
  "factor": { v: 2n, f: 0 },
  "improvement": { v: 1n, f: 0 },
  "guarantee_year": { v: 1974n, f: 0 }
} },
  { label: "a-search-and-heuristic-search", figures: {
  "grid_size": { v: 10n, f: 0 },
  "cells": { v: 100n, f: 0 },
  "optimal_steps": { v: 18n, f: 0 },
  "dijkstra_settled": { v: 100n, f: 0 },
  "astar_settled": { v: 30n, f: 0 },
  "heuristic_at_start": { v: 18n, f: 0 },
  "saved_cells": { v: 70n, f: 0 },
  "directions": { v: 4n, f: 0 }
} },
  { label: "a-capstone-route-planner-design", figures: {
  "vertices": { v: 10000n, f: 0 },
  "edges": { v: 30000n, f: 0 },
  "dijkstra_steps": { v: 560000n, f: 0 },
  "time_ms": { v: 1n, f: 0 },
  "places": { v: 10000n, f: 0 },
  "load_factor": { v: 0.7, f: 1 },
  "distance_km": { v: 500n, f: 0 },
  "tools": { v: 4n, f: 0 }
} }
];
const lines = RECORDS.map((r) => summarizeDemo(r.label, r.figures));
lines.push('records: ' + RECORDS.length);
const body = lines.join('\n');
const h1 = crypto.createHash('sha256').update(body).digest('hex');
const h2 = crypto.createHash('sha256').update(body).digest('hex');
process.stdout.write(body + '\nRun 1 SHA-256: ' + h1 + '\nRun 2 SHA-256: ' + h2
  + '\nDeterministic: ' + (h1 === h2 ? 'MATCH' : 'MISMATCH') + '\n');
