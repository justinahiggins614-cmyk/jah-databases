(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK133-";
var KIND="traversal method";
var TOOLNAME="Nested Archive Traverser";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Recursive descent", "d": "Traversers descend into member archives recursively, treating each as a new root. Recursion naturally models nesting. Depth-first recursion matches archive structure.", "c": "fundamentals", "r": 1, "p": {"MAXD": "5", "TREE": "{'outer': {'inner': {'deep.txt': None}, 'a.txt': None}}"}}, {"t": "Depth caps", "d": "Nesting depth is capped (often 5-10) to bound adversarial 'zip bomb' chains. Caps turn exponential blowup into a clean error. Limits are a security control.", "c": "algorithms", "r": 1, "p": {"MAXD": "1", "TREE": "{'l1': {'l2': {'l3': {'f.txt': None}}}}"}}, {"t": "Cycle detection", "d": "Hard-linked or repeated archives can cycle; identity-based visited sets stop infinite descent. Cycles are rare but fatal without guards. Guards keep traversal total.", "c": "implementation", "r": 1, "p": {"MAXD": "5", "TREE": "{'a': {'b.txt': None}}"}}, {"t": "Virtual path naming", "d": "Members get virtual paths like outer.zip/inner.zip/file.txt. Virtual paths address nested content uniformly. Naming makes nesting addressable.", "c": "optimization", "r": 1, "p": {"MAXD": "5", "TREE": "{'box': {'inner': {'note.txt': None}}}"}}, {"t": "Lazy member loading", "d": "Inner archives load only when the user expands them. Laziness keeps huge nestings responsive. On-demand descent scales.", "c": "evaluation", "r": 1, "p": {"MAXD": "5", "TREE": "{'big': {'huge': {'f.txt': None}}, 'small.txt': None}"}}, {"t": "Size accounting", "d": "Traversers report logical (uncompressed) versus physical sizes per nesting level. Accounting reveals compression bombs before extraction. Sizes inform safety decisions.", "c": "fundamentals", "r": 2, "p": {"MAXD": "5", "TREE": "{'c': {'d.txt': None}}"}}, {"t": "Format-per-level", "d": "Each nesting level may use a different format (zip in tar in gz). Per-level parsers dispatch on magic bytes. Heterogeneous nesting is normal in the wild.", "c": "algorithms", "r": 2, "p": {"MAXD": "5", "TREE": "{'a.tar': {'b.zip': {'c.txt': None}}}"}}, {"t": "Selective deep extraction", "d": "Users extract one nested path without materializing siblings. Selectivity saves orders of magnitude on deep trees. Precision extraction is the goal.", "c": "implementation", "r": 2, "p": {"MAXD": "5", "TREE": "{'x': {'y': {'want.txt': None, 'skip.txt': None}}}"}}, {"t": "Integrity per level", "d": "Each level's checksums verify before descending further. Fail-fast per level localizes corruption. Layered verification isolates damage.", "c": "optimization", "r": 2, "p": {"MAXD": "5", "TREE": "{'ok': {'fine.txt': None}}"}}, {"t": "Quotas per traversal", "d": "Global quotas cap total extracted bytes across all levels. Quotas contain decompression bombs. Limits protect the host.", "c": "evaluation", "r": 2, "p": {"MAXD": "5", "TREE": "{'q': {'r.txt': None}}"}}, {"t": "Parallel level scans", "d": "Independent inner archives scan in parallel. Parallelism speeds broad, shallow nestings. Concurrency multiplies throughput.", "c": "fundamentals", "r": 3, "p": {"MAXD": "5", "TREE": "{'p1': {'a.txt': None}, 'p2': {'b.txt': None}}"}}, {"t": "Provenance chains", "d": "Provenance records the full nesting path per extracted file. Chains answer 'where did this come from'. Lineage survives extraction.", "c": "algorithms", "r": 3, "p": {"MAXD": "5", "TREE": "{'src': {'mid': {'leaf.txt': None}}}"}}, {"t": "Encrypted inner layers", "d": "Inner archives may be encrypted while outer ones are not. Traversers prompt per encrypted level. Layered encryption needs layered handling.", "c": "implementation", "r": 3, "p": {"MAXD": "5", "TREE": "{'open': {'locked': {'f.txt': None}}}"}}, {"t": "Traversal resume", "d": "Checkpoints record the descent stack for resumable deep walks. Resume avoids restarting expensive descents. Persistence suits massive archives.", "c": "optimization", "r": 3, "p": {"MAXD": "5", "TREE": "{'r1': {'r2': {'f.txt': None}}}"}}, {"t": "Visualization of nesting", "d": "Tree views render nesting depth with indentation and sizes. Visualization makes structure graspable. Good views beat raw lists.", "c": "evaluation", "r": 3, "p": {"MAXD": "5", "TREE": "{'v': {'w': {'x.txt': None}}, 'top.txt': None}"}}];
var DEMO="# Nested archive traversal: recursive container tree with depth cap and cycle guard.\ntree = %%TREE%%\ndef walk(node, depth=0, max_depth=%%MAXD%%, seen=None):\n    seen = seen or set()\n    indent = \"  \" * depth\n    for name, sub in sorted(node.items()):\n        is_arc = isinstance(sub, dict)\n        print(f\"{indent}{name}{'/' if is_arc else ''}\")\n        if is_arc and depth < max_depth and id(sub) not in seen:\n            seen.add(id(sub))\n            walk(sub, depth + 1, max_depth, seen)\nprint(\"nested traversal (depth cap %%MAXD%%):\")\nwalk(tree)\n";
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
  if(!new RegExp("^JAH\\-ATK133\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-nested-archive-traverser-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-nested-archive-traverser",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
