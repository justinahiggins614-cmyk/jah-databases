(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK121-";
var KIND="traversal method";
var TOOLNAME="Directory Tree Traverser";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Depth-first traversal", "d": "DFS descends each branch fully before backtracking, using a stack (or recursion). It needs memory proportional to tree depth, not tree size. DFS suits 'find the first match down this path' exploration.", "c": "fundamentals", "r": 1, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'docs': {'a.txt': None, 'sub': {'b.txt': None}}, 'img': {'c.png': None}}"}}, {"t": "Breadth-first traversal", "d": "BFS visits level by level using a queue, finding the shallowest matches first. Its memory grows with tree width, which can be large. BFS suits 'find the nearest match' queries.", "c": "algorithms", "r": 1, "p": {"MODE": "bfs", "LIMIT": "8", "TREE": "{'docs': {'a.txt': None, 'sub': {'b.txt': None}}, 'img': {'c.png': None}}"}}, {"t": "Cycle-safe traversal", "d": "Symlinks and mounts can cycle; traversers track visited (device, inode) pairs to avoid infinite loops. Revisited directories are reported once and skipped. Cycle safety is mandatory on real filesystems.", "c": "implementation", "r": 1, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'a': {'b': {}}, 'c': {}}"}}, {"t": "Pruning subtrees", "d": "Pruners skip branches by name pattern ('.git', 'node_modules') or by predicate. Skipping early avoids descending into huge irrelevant subtrees. Pruning is the biggest traversal speedup in practice.", "c": "optimization", "r": 1, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'src': {'main.py': None}, '.git': {'objects': {'x': None}}, 'docs': {'r.md': None}}"}}, {"t": "Permission-error handling", "d": "Unreadable directories raise errors; robust traversers log and continue instead of aborting. Error callbacks let callers decide per failure. Graceful degradation keeps partial results useful.", "c": "evaluation", "r": 1, "p": {"MODE": "bfs", "LIMIT": "8", "TREE": "{'ok': {'f.txt': None}, 'locked': {}, 'more': {'g.txt': None}}"}}, {"t": "Parallel traversal", "d": "Independent subtrees traverse in parallel with a work-stealing queue. Speedup is limited by disk seeks on spinning media but excellent on SSDs. Parallel walkers saturate modern storage.", "c": "fundamentals", "r": 2, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'a': {'1.txt': None, '2.txt': None}, 'b': {'3.txt': None}}"}}, {"t": "Incremental re-traversal", "d": "Watchers record modification times; re-traversal visits only changed subtrees. Snapshots of the previous walk diff against the new one. Incremental walks keep huge trees fresh cheaply.", "c": "algorithms", "r": 2, "p": {"MODE": "bfs", "LIMIT": "8", "TREE": "{'docs': {'new.txt': None}, 'old': {'o.txt': None}}"}}, {"t": "Depth limiting", "d": "Max-depth bounds keep traversals out of pathological nesting. Depth limits also implement 'two levels down' UI expansions. Bounded depth guarantees termination time.", "c": "implementation", "r": 2, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'l1': {'l2': {'l3': {'deep.txt': None}}}, 'top.txt': None}"}}, {"t": "File-type filtering", "d": "Filters select entries by extension, magic bytes, or size during the walk. Filtering at traversal time avoids materializing unwanted entries. Type filters focus crawls on relevant content.", "c": "optimization", "r": 2, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'a.txt': None, 'b.png': None, 'sub': {'c.txt': None}}"}}, {"t": "Sorted versus fast order", "d": "Sorted traversal gives deterministic output at the cost of readdir sorting. Unsorted traversal is faster but nondeterministic across runs. Determinism matters for tests and diffs.", "c": "evaluation", "r": 2, "p": {"MODE": "bfs", "LIMIT": "8", "TREE": "{'b': {'f.txt': None}, 'a': {'g.txt': None}}"}}, {"t": "Symlink policies", "d": "Policies choose: follow, list-as-link, or skip symlinks. Following risks cycles; listing keeps structure honest. Explicit policy prevents surprise behavior.", "c": "fundamentals", "r": 3, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'real': {'f.txt': None}, 'link': {}}"}}, {"t": "Traversal statistics", "d": "Walkers count files, directories, total bytes, and depth histograms in one pass. Statistics feed capacity planning and progress bars. One pass beats separate du/find invocations.", "c": "algorithms", "r": 3, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'a': {'1.txt': None, '2.txt': None}, 'b': {'sub': {'3.txt': None}}}"}}, {"t": "Resumable walks", "d": "Checkpoints record the walk frontier so interrupted traversals resume instead of restarting. Frontier serialization must survive process restarts. Resumability matters for week-long crawls.", "c": "implementation", "r": 3, "p": {"MODE": "bfs", "LIMIT": "8", "TREE": "{'a': {'x.txt': None}, 'b': {'y.txt': None}, 'c': {'z.txt': None}}"}}, {"t": "Comparing two trees", "d": "Diff walks traverse both trees in lockstep, reporting added, removed, and changed entries. Sorted order on both sides makes the merge linear. Tree diff underlies backup verification and sync.", "c": "optimization", "r": 3, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'keep.txt': None, 'new.txt': None}"}}, {"t": "Traversal as a stream", "d": "Streaming walkers yield entries one at a time instead of building a full list. Constant memory lets walks cover billions of entries. Streams compose with filters and sinks in pipelines.", "c": "evaluation", "r": 3, "p": {"MODE": "dfs", "LIMIT": "8", "TREE": "{'s1': {'a.txt': None}, 's2': {'b.txt': None}}"}}];
var DEMO="# Directory tree traversal: DFS and BFS over a nested directory mapping.\ntree = %%TREE%%\ndef dfs(node, path=\"\"):\n    out = []\n    for name, sub in sorted(node.items()):\n        p = path + \"/\" + name\n        out.append(p)\n        if isinstance(sub, dict):\n            out += dfs(sub, p)\n    return out\ndef bfs(node):\n    out, queue = [], [(\"\", node)]\n    while queue:\n        path, cur = queue.pop(0)\n        for name, sub in sorted(cur.items()):\n            p = path + \"/\" + name\n            out.append(p)\n            if isinstance(sub, dict):\n                queue.append((p, sub))\n    return out\nmode = \"%%MODE%%\"\npaths = dfs(tree) if mode == \"dfs\" else bfs(tree)\nprint(mode.upper(), \"order:\")\nfor p in paths[:%%LIMIT%%]:\n    print(\" \", p)\nprint(\"total entries:\", len(paths))\n";
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
  if(!new RegExp("^JAH\\-ATK121\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-directory-tree-traverser-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-directory-tree-traverser",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
