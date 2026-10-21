(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK149-";
var KIND="extraction method";
var TOOLNAME="Scientific Paper Extractor";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Section segmentation", "d": "Headings (Abstract, Methods, Results) partition papers into typed sections. Segmentation structures the paper. Sections organize.", "c": "fundamentals", "r": 1, "p": {"PAPER": "Abstract\\nWe study X.\\nMethods\\nWe measured.\\nResults\\nIt worked.\\nReferences\\n[1] Y.", "SNIP": "60"}}, {"t": "Abstract extraction", "d": "Abstracts summarize; extractors isolate them for indexing. Abstracts represent papers. Summaries index.", "c": "algorithms", "r": 1, "p": {"PAPER": "Abstract\\nThis paper shows Z.\\nIntroduction\\nBackground.", "SNIP": "60"}}, {"t": "Method identification", "d": "Method sections describe the procedures, apparatus, and protocols behind a study's claims, and identifying them precisely is what makes replication possible. Extractors locate methods by heading patterns and characteristic vocabulary, separating them from background and results. Methods sections get the most scrutiny because reproducibility lives there.", "c": "implementation", "r": 1, "p": {"PAPER": "Methods\\nWe used surveys.\\nResults\\nScores rose.", "SNIP": "60"}}, {"t": "Result extraction", "d": "Results sections hold the paper's claims together with their supporting numbers, tables, and statistical tests. Extractors pair each quantitative finding with the claim sentence it supports, preserving units and conditions. Structured results feed meta-analysis and claim verification.", "c": "optimization", "r": 1, "p": {"PAPER": "Results\\nAccuracy reached 95%.\\nDiscussion\\nThis matters.", "SNIP": "60"}}, {"t": "Reference parsing", "d": "References parse into authors, year, title, venue. Parsed citations build graphs. Citations connect.", "c": "evaluation", "r": 1, "p": {"PAPER": "References\\n[1] Smith, J. 2020. On X.\\n[2] Lee, K. 2021. On Y.", "SNIP": "60"}}, {"t": "Figure extraction", "d": "Figures extract together with their captions as image-text pairs, since the caption carries the interpretation the image alone cannot. Extractors crop figure regions from page geometry and link each to its numbered caption. Paired figures and captions feed visual question answering over the literature.", "c": "fundamentals", "r": 2, "p": {"PAPER": "Results\\nSee Figure 1.\\nFigure 1: Growth chart.", "SNIP": "60"}}, {"t": "Table extraction", "d": "Result tables extract with their headers preserved, because a column of numbers is meaningless without its labels and units. Extractors reconstruct the grid from ruling lines and text alignment, then type each column. Structured tables turn published findings into analyzable data.", "c": "algorithms", "r": 2, "p": {"PAPER": "Results\\n| cond | acc |\\n| A | 90 |", "SNIP": "60"}}, {"t": "Math extraction", "d": "Equations extract as MathML or LaTeX rather than flat text, preserving operators, fractions, and subscripts as structure. Formula-aware extraction keeps mathematics searchable and convertible instead of degrading into unreadable symbol soup. In technical papers, the math often carries the core contribution.", "c": "implementation", "r": 2, "p": {"PAPER": "Methods\\nWe optimize L = sum(x).\\nResults\\nDone.", "SNIP": "60"}}, {"t": "Citation contexts", "d": "Sentences citing a reference (citances) characterize its contribution. Contexts summarize influence. Citations have context.", "c": "optimization", "r": 2, "p": {"PAPER": "Introduction\\nAs shown [1], X holds.\\nReferences\\n[1] Y.", "SNIP": "60"}}, {"t": "Supplementary materials", "d": "Supplementary materials link the datasets, code, and extended figures that complete a paper beyond its page limit. Extractors collect supplement links and file lists so downstream users can actually find the data behind the claims. Supplements are where reproducibility artifacts live.", "c": "evaluation", "r": 2, "p": {"PAPER": "Methods\\nData at link.\\nReferences\\n[1] Z.", "SNIP": "60"}}, {"t": "Peer-review metadata", "d": "Extractors capture received/accepted dates and versions. Metadata tracks provenance. History informs.", "c": "fundamentals", "r": 3, "p": {"PAPER": "Abstract\\nWe report.\\nReferences\\n[1] A.", "SNIP": "60"}}, {"t": "Claim extraction", "d": "Atomic claims extract as (subject, predicate, object) triples. Claims feed knowledge graphs. Claims are knowledge.", "c": "algorithms", "r": 3, "p": {"PAPER": "Results\\nDrug X reduces Y.\\nDiscussion\\nImplications.", "SNIP": "60"}}, {"t": "Reproducibility signals", "d": "Code/data availability statements extract as badges. Signals predict reproducibility. Openness enables trust.", "c": "implementation", "r": 3, "p": {"PAPER": "Methods\\nCode available.\\nResults\\nOK.", "SNIP": "60"}}, {"t": "Multi-format input", "d": "Papers arrive as PDF, LaTeX, or XML (JATS). Format-specific parsers converge on one model. Inputs vary; output unifies.", "c": "optimization", "r": 3, "p": {"PAPER": "Abstract\\nUnified.\\nMethods\\nParsed.", "SNIP": "60"}}, {"t": "Evaluation corpora", "d": "Labeled paper corpora score section and reference extraction. Benchmarks drive quality. Tests ensure truth.", "c": "evaluation", "r": 3, "p": {"PAPER": "Abstract\\nTest.\\nReferences\\n[1] B.", "SNIP": "60"}}];
var DEMO="# Paper extraction: split into sections by headings, pull abstract/methods/results/references.\ntext = \"\"\"%%PAPER%%\"\"\".replace(\"\\\\n\", \"\\n\")\nimport re\nheads = [\"abstract\", \"introduction\", \"methods\", \"results\", \"discussion\", \"conclusion\", \"references\"]\nsecs, cur = {}, None\nfor line in text.splitlines():\n    low = line.strip().lower()\n    hit = next((h for h in heads if low == h or low.startswith(h + \":\")), None)\n    if hit:\n        cur = hit; secs[cur] = []\n    elif cur:\n        secs[cur].append(line)\nfor h in heads:\n    if h in secs:\n        body = \" \".join(secs[h])[:%%SNIP%%]\n        print(f\"[{h.upper()}] {body}\")\nrefs = [l for l in secs.get(\"references\", []) if l.strip()]\nprint(f\"references found: {len(refs)}\")\n";
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
  if(!new RegExp("^JAH\\-ATK149\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-scientific-paper-extractor-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-scientific-paper-extractor",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
