(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK127-";
var KIND="traversal method";
var TOOLNAME="Graph Traversal Engine";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Breadth-first search", "d": "BFS explores in waves from the start, guaranteeing shortest-path discovery in unweighted graphs. A queue plus a visited set implements it in O(V + E). BFS answers 'how many hops apart'.", "c": "fundamentals", "r": 1, "p": {"START": "a", "GOAL": "d", "DEPTH": "5", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['d'], 'd': []}"}}, {"t": "Depth-first search", "d": "DFS plunges down each branch before backtracking, using a stack. It finds paths with minimal memory but no shortest-path guarantee. DFS suits exhaustive exploration.", "c": "algorithms", "r": 1, "p": {"START": "a", "GOAL": "d", "DEPTH": "5", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': [], 'd': []}"}}, {"t": "Shortest paths (Dijkstra)", "d": "Dijkstra's algorithm extends BFS to weighted edges with a priority queue. It settles nodes in order of true shortest distance. Dijkstra routes everything from road networks to dependency costs.", "c": "implementation", "r": 1, "p": {"START": "a", "GOAL": "d", "DEPTH": "5", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['d'], 'd': []}"}}, {"t": "Depth-limited search", "d": "Depth limits bound exploration to k hops, pruning deeper branches. Limits keep traversals tractable on dense graphs. 'Friends of friends' is depth-2 search.", "c": "optimization", "r": 1, "p": {"START": "a", "GOAL": "", "DEPTH": "1", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['e'], 'd': [], 'e': []}"}}, {"t": "Cycle handling", "d": "Visited sets prevent infinite loops on cyclic graphs. Path-sensitive variants allow revisiting nodes via different routes. Cycle safety is non-negotiable.", "c": "evaluation", "r": 1, "p": {"START": "a", "GOAL": "c", "DEPTH": "5", "GRAPH": "{'a': ['b'], 'b': ['a','c'], 'c': []}"}}, {"t": "Bidirectional search", "d": "Searching from both start and goal simultaneously meets in the middle. It cuts the explored space roughly to its square root. Bidirectional search shines on large uniform graphs.", "c": "fundamentals", "r": 2, "p": {"START": "a", "GOAL": "d", "DEPTH": "5", "GRAPH": "{'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': []}"}}, {"t": "Topological traversal", "d": "DAGs traverse in topological order: every node after its dependencies. Kahn's algorithm or DFS finishing-times compute the order. Build systems and schedulers run on topological order.", "c": "algorithms", "r": 2, "p": {"START": "a", "GOAL": "", "DEPTH": "5", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['d'], 'd': []}"}}, {"t": "Connected components", "d": "Repeated BFS/DFS from unvisited nodes labels each connected component. Components reveal isolated subgraphs. Component analysis is the first step in graph triage.", "c": "implementation", "r": 2, "p": {"START": "a", "GOAL": "", "DEPTH": "5", "GRAPH": "{'a': ['b'], 'b': ['a'], 'c': ['d'], 'd': ['c']}"}}, {"t": "Path enumeration", "d": "All simple paths between two nodes enumerate with pruning by length and visited sets. Counts explode combinatorially, so enumeration always bounds. Path lists explain 'how is X connected to Y'.", "c": "optimization", "r": 2, "p": {"START": "a", "GOAL": "d", "DEPTH": "4", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['d'], 'd': []}"}}, {"t": "Random walks", "d": "Random walks sample neighborhoods without exhaustive traversal. They underpin embeddings like node2vec. Walks scale to graphs too big to traverse fully.", "c": "evaluation", "r": 2, "p": {"START": "a", "GOAL": "", "DEPTH": "3", "GRAPH": "{'a': ['b','c'], 'b': ['a','d'], 'c': ['a'], 'd': ['b']}"}}, {"t": "Traversal with edge filters", "d": "Real traversals follow only edges matching type or weight predicates. Filtering at expansion time prunes the search. 'Only follows works-for edges' is a filtered traversal.", "c": "fundamentals", "r": 3, "p": {"START": "a", "GOAL": "d", "DEPTH": "5", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['d'], 'd': []}"}}, {"t": "Multi-source BFS", "d": "Starting BFS from many sources at once computes nearest-source regions. It answers 'closest facility' for all nodes simultaneously. Multi-source search powers Voronoi-style partitioning.", "c": "algorithms", "r": 3, "p": {"START": "a", "GOAL": "", "DEPTH": "5", "GRAPH": "{'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': []}"}}, {"t": "Iterative deepening", "d": "Iterative deepening repeats depth-limited DFS with growing limits. It gains BFS's shortest-path guarantee with DFS's memory. Classic choice for huge implicit graphs.", "c": "implementation", "r": 3, "p": {"START": "a", "GOAL": "d", "DEPTH": "3", "GRAPH": "{'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': []}"}}, {"t": "Traversal budgets", "d": "Budgets cap visited nodes, edges, or time; traversals stop gracefully at the cap. Partial results report coverage honestly. Budgets keep interactive graph exploration responsive.", "c": "optimization", "r": 3, "p": {"START": "a", "GOAL": "", "DEPTH": "5", "GRAPH": "{'a': ['b','c'], 'b': ['d'], 'c': ['e'], 'd': [], 'e': []}"}}, {"t": "Distributed traversal", "d": "Pregel-style systems traverse partitioned graphs with message passing between workers. Bulk-synchronous steps keep the computation coordinated. Distribution scales traversal to trillion-edge graphs.", "c": "evaluation", "r": 3, "p": {"START": "a", "GOAL": "d", "DEPTH": "5", "GRAPH": "{'a': ['b'], 'b': ['c'], 'c': ['d'], 'd': []}"}}];
var DEMO="# Graph traversal: BFS/DFS over an adjacency list with depth limit and path output.\ngraph = %%GRAPH%%\ndef bfs(start, goal=None, max_depth=%%DEPTH%%):\n    seen, queue = {start}, [(start, [start])]\n    order = []\n    while queue:\n        node, path = queue.pop(0)\n        order.append(node)\n        if node == goal: return order, path\n        if len(path) - 1 >= max_depth: continue\n        for nb in graph.get(node, []):\n            if nb not in seen: seen.add(nb); queue.append((nb, path + [nb]))\n    return order, None\norder, path = bfs(\"%%START%%\", \"%%GOAL%%\" or None)\nprint(\"BFS order:\", order)\nprint(\"path to goal:\", path or \"not reached\")\n";
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
  if(!new RegExp("^JAH\\-ATK127\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-graph-traversal-engine-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-graph-traversal-engine",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
