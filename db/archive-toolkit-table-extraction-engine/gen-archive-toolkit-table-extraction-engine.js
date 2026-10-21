(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK142-";
var KIND="extraction method";
var TOOLNAME="Table Extraction Engine";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Grid-line detection", "d": "Border characters (+,-,|) reveal column boundaries in plain-text tables. Boundary positions split every row consistently. Geometry beats guessing.", "c": "fundamentals", "r": 1, "p": {"TABLE": "+-----+-----+\\n| a   | b   |\\n+-----+-----+\\n| 1   | 2   |\\n+-----+-----+"}}, {"t": "Header detection", "d": "Headers are the first row, often distinguished by position or styling. Detection separates labels from data. Headers name columns.", "c": "algorithms", "r": 1, "p": {"TABLE": "| name | age |\\n| amy  | 30  |\\n| bob  | 25  |"}}, {"t": "Merged cells", "d": "Spanning cells (colspan) need grid reconstruction to place values correctly. Spans complicate the simple grid model. Structure needs care.", "c": "implementation", "r": 1, "p": {"TABLE": "+-------+-----+\\n| name        | age |\\n+-------+-----+\\n| amy   | 30  |\\n+-------+-----+"}}, {"t": "Borderless tables", "d": "Whitespace-aligned tables infer columns from consistent gaps. Gap analysis replaces border detection. Alignment is the signal.", "c": "optimization", "r": 1, "p": {"TABLE": "name   age\\namy    30\\nbob     25"}}, {"t": "HTML table parsing", "d": "<table>/<tr>/<td> markup parses directly into grids. Colspan/rowspan attributes guide placement. Markup is explicit.", "c": "evaluation", "r": 1, "p": {"TABLE": "| a | b |\\n| 1 | 2 |"}}, {"t": "PDF table detection", "d": "PDFs lack table markup; detectors use ruling lines and text alignment. Line plus text evidence locates tables. Detection precedes extraction.", "c": "fundamentals", "r": 2, "p": {"TABLE": "+---+---+\\n| x | y |\\n+---+---+\\n| 1 | 2 |\\n+---+---+"}}, {"t": "Cell type inference", "d": "Cells infer types: numbers, dates, strings. Typed columns enable analysis. Types make tables usable.", "c": "algorithms", "r": 2, "p": {"TABLE": "| item | price |\\n| apple| 1.50  |\\n| pear | 2.00  |"}}, {"t": "Multi-page tables", "d": "Tables spanning pages need stitching with repeated headers removed. Continuity detection joins fragments. Stitching restores wholes.", "c": "implementation", "r": 2, "p": {"TABLE": "| h1 | h2 |\\n| a  | b  |"}}, {"t": "Nested tables", "d": "Tables inside cells recurse: extract inner first. Recursion handles nesting. Nesting is rare but real.", "c": "optimization", "r": 2, "p": {"TABLE": "+-----+\\n| out |\\n+-----+"}}, {"t": "Evaluation metrics", "d": "Cell-level precision/recall score extractors on labeled tables. Metrics need alignment-tolerant matching. Measurement guides tuning.", "c": "evaluation", "r": 2, "p": {"TABLE": "| a |\\n| 1 |"}}, {"t": "Spreadsheet export", "d": "Extracted tables export to CSV/Excel preserving types. Export makes data reusable. Interchange completes extraction.", "c": "fundamentals", "r": 3, "p": {"TABLE": "| n | v |\\n| x | 1 |"}}, {"t": "Footnote handling", "d": "Footnote markers detach from table cells into linked notes, keeping the grid itself clean. Separation preserves the table's structure while retaining the annotations readers need. Each note keeps an explicit link back to its cell so nothing is lost.", "c": "algorithms", "r": 3, "p": {"TABLE": "| a* | b |\\n| 1  | 2 |"}}, {"t": "Rotated headers", "d": "Vertical headers rotate back before reading. Orientation detection handles them. Rotation is layout noise.", "c": "implementation", "r": 3, "p": {"TABLE": "| a | b |\\n| 1 | 2 |"}}, {"t": "Confidence per cell", "d": "Cells extracted with low confidence are flagged for human review instead of silently entering the data. Triage focuses expensive human effort on exactly the cells that need it. Per-cell confidence is what lets table extraction scale without sacrificing trust.", "c": "optimization", "r": 3, "p": {"TABLE": "| a |\\n| 1 |"}}, {"t": "Streaming extraction", "d": "Streaming parsers emit rows without loading whole documents. Streams handle huge reports. Memory stays flat.", "c": "evaluation", "r": 3, "p": {"TABLE": "| a | b |\\n| 1 | 2 |\\n| 3 | 4 |"}}];
var DEMO="# Table extraction: detect grid lines in ASCII-art tables, split into rows/columns.\ntext = \"\"\"%%TABLE%%\"\"\".replace(\"\\\\n\", \"\\n\")\ndef extract(t):\n    lines = [l for l in t.splitlines() if l.strip()]\n    # find column boundaries from '+' intersections in border lines\n    bounds = None\n    for l in lines:\n        if set(l.strip()) <= set(\"+-\"):\n            b = [i for i, c in enumerate(l) if c == \"+\"]\n            if len(b) > 1: bounds = b; break\n    rows = []\n    for l in lines:\n        if set(l.strip()) <= set(\"+-\"): continue\n        if bounds and \"|\" in l:\n            cells = []\n            for a, b in zip(bounds, bounds[1:]):\n                cells.append(l[a+1:b].strip())\n            rows.append(cells)\n        elif \"|\" in l:\n            rows.append([c.strip() for c in l.strip().strip(\"|\").split(\"|\")])\n    return rows\nrows = extract(text)\nfor r in rows: print(r)\nprint(\"shape:\", len(rows), \"x\", (len(rows[0]) if rows else 0))\n";
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
  if(!new RegExp("^JAH\\-ATK142\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-table-extraction-engine-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-table-extraction-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
