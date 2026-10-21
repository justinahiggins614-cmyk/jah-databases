(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK145-";
var KIND="extraction method";
var TOOLNAME="Spreadsheet Analyzer";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Cell grid model", "d": "Worksheets are sparse grids addressed A1-style; only non-empty cells store. Sparse storage keeps huge sheets light. Grids are the canvas.", "c": "fundamentals", "r": 1, "p": {"CELLS": "{'A1': 10, 'A2': 20, 'A3': '=SUM(A1:A2)'}"}}, {"t": "Formula parsing", "d": "Formulas parse into expression trees with cell references as variables. Parsers handle ranges, functions, and operators. Trees evaluate.", "c": "algorithms", "r": 1, "p": {"CELLS": "{'B1': 5, 'B2': '=B1*2'}"}}, {"t": "Dependency graphs", "d": "References form a dependency DAG; evaluation follows topological order. Graph order guarantees inputs compute first. DAGs schedule.", "c": "implementation", "r": 1, "p": {"CELLS": "{'A1': 1, 'B1': '=A1+1', 'C1': '=B1+1'}"}}, {"t": "Cycle detection", "d": "Circular references break the DAG; detectors report the cycle path. Detection prevents infinite evaluation. Cycles are errors.", "c": "optimization", "r": 1, "p": {"CELLS": "{'A1': 1, 'A2': 2}"}}, {"t": "Function library", "d": "SUM, AVG, VLOOKUP and hundreds more implement spreadsheet semantics. Faithful semantics need the full library. Functions are the vocabulary.", "c": "evaluation", "r": 1, "p": {"CELLS": "{'A1': 4, 'A2': 6, 'A3': '=AVG(A1:A2)'}"}}, {"t": "Type coercion", "d": "Sheets coerce text-numbers in arithmetic with defined rules. Rules differ subtly between engines. Coercion needs specification.", "c": "fundamentals", "r": 2, "p": {"CELLS": "{'A1': '5', 'B1': '=A1*2'}"}}, {"t": "Multiple worksheets", "d": "Workbooks hold sheets; references qualify with sheet names. Cross-sheet edges join the dependency graph. Names scope.", "c": "algorithms", "r": 2, "p": {"CELLS": "{'A1': 7}"}}, {"t": "Table detection", "d": "Header rows plus contiguous data blocks form logical tables. Detection lifts grids into records. Tables structure.", "c": "implementation", "r": 2, "p": {"CELLS": "{'A1': 'name', 'B1': 'age', 'A2': 'amy', 'B2': 30}"}}, {"t": "Conditional formatting", "d": "Format rules are predicates over cell values. Extractors list rules as data. Formats encode meaning.", "c": "optimization", "r": 2, "p": {"CELLS": "{'A1': 99}"}}, {"t": "Pivot analysis", "d": "Pivot tables aggregate by categories; analyzers reconstruct the grouping. Aggregation logic is extractable. Pivots summarize.", "c": "evaluation", "r": 2, "p": {"CELLS": "{'A1': 'x', 'B1': 10, 'A2': 'x', 'B2': 20}"}}, {"t": "Data validation rules", "d": "Validation rules list the allowed values per cell, from dropdown lists to numeric ranges and custom formulas. Rules document the sheet author's intent so future editors understand the constraints. Extracted validation metadata guides data entry and flags violations automatically.", "c": "fundamentals", "r": 3, "p": {"CELLS": "{'A1': 'yes'}"}}, {"t": "Change tracking", "d": "Tracked changes log who edited which cell and when, preserving the full edit history of a workbook. Change logs make collaboration auditable, showing exactly how a sheet evolved. Extractors surface this history for review and compliance.", "c": "algorithms", "r": 3, "p": {"CELLS": "{'A1': 'v2'}"}}, {"t": "External links", "d": "Formulas can reference other workbooks. Links create cross-file dependencies. Links need resolution.", "c": "implementation", "r": 3, "p": {"CELLS": "{'A1': 3}"}}, {"t": "Performance profiling", "d": "Profilers find volatile functions and heavy recalculation chains. Optimization targets the hot paths. Speed needs measurement.", "c": "optimization", "r": 3, "p": {"CELLS": "{'A1': 1, 'B1': '=A1'}"}}, {"t": "Export to records", "d": "Analyzers export detected tables as JSON/CSV records. Export bridges sheets and databases. Records are portable.", "c": "evaluation", "r": 3, "p": {"CELLS": "{'A1': 'id', 'A2': 1, 'A3': 2}"}}];
var DEMO="# Spreadsheet analysis: evaluate formulas (SUM/AVG/refs) over a cell grid.\nimport re\ncells = %%CELLS%%\ndef val(addr, seen=None):\n    seen = seen or set()\n    if addr in seen: raise ValueError(\"circular ref \" + addr)\n    seen.add(addr)\n    raw = cells[addr]\n    if not isinstance(raw, str) or not raw.startswith(\"=\"):\n        return raw\n    expr = raw[1:]\n    def rng(m):\n        a, b = m.group(1), m.group(2)\n        cols = [chr(c) for c in range(ord(a[0]), ord(b[0])+1)]\n        return [c + str(r) for c in cols for r in range(int(a[1:]), int(b[1:])+1)]\n    expr = re.sub(r\"([A-Z]+\\d+):([A-Z]+\\d+)\", lambda m: \"[\" + \",\".join(rng(m)) + \"]\", expr)\n    expr = re.sub(r\"\\bSUM\\b\", \"sum\", expr); expr = re.sub(r\"\\bAVG\\b\", \"avg\", expr)\n    expr = re.sub(r\"\\b([A-Z]+\\d+)\\b\", lambda m: repr(val(m.group(1), set(seen))), expr)\n    avg = lambda xs: sum(xs)/len(xs)\n    return eval(expr, {\"__builtins__\": {}}, {\"sum\": sum, \"avg\": avg})\nfor addr in sorted(cells):\n    print(f\"  {addr} = {cells[addr]!r:16} -> {val(addr)}\")\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK145\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-spreadsheet-analyzer-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-spreadsheet-analyzer",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
