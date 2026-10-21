(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK122-";
var KIND="traversal method";
var TOOLNAME="Database Table Traverser";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "Schema graph model", "d": "Tables are nodes; foreign keys are directed edges from child to parent. The schema graph reveals join paths without reading any data. Graph thinking turns schema navigation into path-finding.", "c": "fundamentals", "r": 1, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id', 'name']}, 'items': {'columns': ['id', 'order_id->orders.id']}}"}}, {"t": "Foreign-key discovery", "d": "Declared foreign keys come from the catalog; undeclared ones are inferred by name and type matching. 'customer_id' beside a 'customers(id)' table is a near-certain link. Discovery recovers structure in legacy databases.", "c": "algorithms", "r": 1, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id']}}"}}, {"t": "Join-path finding", "d": "Shortest paths in the schema graph become join chains between any two tables. BFS over the schema graph finds the minimal joins. Path-finding automates what analysts do by hand.", "c": "implementation", "r": 1, "p": {"START": "items", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id']}, 'items': {'columns': ['id', 'order_id->orders.id']}}"}}, {"t": "View dependency traversal", "d": "Views depend on tables and other views; dependency graphs order refreshes and impact analysis. Topological order tells which views rebuild first. Dependency traversal prevents stale-view surprises.", "c": "optimization", "r": 1, "p": {"START": "v_orders", "SCHEMA": "{'v_orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id']}}"}}, {"t": "Column lineage", "d": "Column-level lineage tracks which source columns feed each derived column. Lineage answers 'where did this number come from' for audits. Fine-grained lineage is the backbone of data governance.", "c": "evaluation", "r": 1, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'total', 'customer_id->customers.id']}, 'customers': {'columns': ['id', 'name']}}"}}, {"t": "Cardinality estimation", "d": "Traversers estimate fan-out per edge (one-to-many versus many-to-one) from statistics. Cardinality guides join order: filter the selective side first. Estimates keep generated queries fast.", "c": "fundamentals", "r": 2, "p": {"START": "customers", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id']}}"}}, {"t": "Self-referencing tables", "d": "Employee-manager tables reference themselves; traversal must bound recursion depth. Recursive CTEs walk these hierarchies in SQL. Cycle guards keep org-chart walks terminating.", "c": "algorithms", "r": 2, "p": {"START": "employees", "SCHEMA": "{'employees': {'columns': ['id', 'manager_id->employees.id']}}"}}, {"t": "Many-to-many bridges", "d": "Junction tables connect two entities; traversal expands them into direct many-to-many edges. Collapsing bridges simplifies the graph for path-finding. Bridge-aware traversal matches how users think about relationships.", "c": "implementation", "r": 2, "p": {"START": "students", "SCHEMA": "{'students': {'columns': ['id']}, 'enroll': {'columns': ['student_id->students.id', 'course_id->courses.id']}, 'courses': {'columns': ['id']}}"}}, {"t": "Schema diff traversal", "d": "Comparing two schema versions walks both graphs, flagging added/removed tables and columns. Diffs drive migration scripts. Version-aware traversal keeps evolution safe.", "c": "optimization", "r": 2, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id', 'total']}, 'customers': {'columns': ['id']}}"}}, {"t": "Sampling during traversal", "d": "Traversers sample rows per table to show real values alongside structure. Samples make abstract schemas concrete for explorers. Bounded sampling keeps traversal interactive.", "c": "evaluation", "r": 2, "p": {"START": "customers", "SCHEMA": "{'customers': {'columns': ['id', 'name']}, 'orders': {'columns': ['id', 'customer_id->customers.id']}}"}}, {"t": "Access-path auditing", "d": "Traversal logs which tables and columns were touched, supporting access reviews. Audit trails show data stewards exactly what was explored. Audited traversal satisfies compliance needs.", "c": "fundamentals", "r": 3, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id', 'ssn']}}"}}, {"t": "Cross-database links", "d": "Federated schemas link tables across database instances via declared mappings. Traversal follows links across connection boundaries. Cross-database graphs unify fragmented estates.", "c": "algorithms", "r": 3, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'ext_id->archive.orders.id']}, 'archive.orders': {'columns': ['id']}}"}}, {"t": "Orphan detection", "d": "Tables no view or query references are orphans, found by reachability from known roots. Orphan reports guide cleanup. Reachability analysis keeps schemas lean.", "c": "implementation", "r": 3, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id']}, 'legacy': {'columns': ['id']}}"}}, {"t": "Traversal budgets", "d": "Budgets cap tables visited, rows sampled, and time spent per exploration. Budgeted traversal degrades gracefully on huge schemas. Budgets keep interactive exploration responsive.", "c": "optimization", "r": 3, "p": {"START": "orders", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id']}}"}}, {"t": "Visual schema maps", "d": "Traversal output renders as entity-relationship diagrams for human browsing. Layouts cluster strongly-connected tables. Visual maps make schemas learnable.", "c": "evaluation", "r": 3, "p": {"START": "items", "SCHEMA": "{'orders': {'columns': ['id', 'customer_id->customers.id']}, 'customers': {'columns': ['id']}, 'items': {'columns': ['id', 'order_id->orders.id']}}"}}];
var DEMO="# Table traversal: walk schema (tables -> columns -> foreign keys), BFS from a table.\nschema = %%SCHEMA%%\ndef neighbors(table):\n    out = set()\n    for col in schema.get(table, {}).get(\"columns\", []):\n        if \"->\" in col:\n            out.add(col.split(\"->\")[1].rsplit(\".\", 1)[0])\n    for t, spec in schema.items():\n        for col in spec.get(\"columns\", []):\n            if col.endswith(\"->\" + table + \".id\") or (\"->\" in col and col.split(\"->\")[1].startswith(table + \".\")):\n                out.add(t)\n    return sorted(out)\nstart = \"%%START%%\"\nseen, queue, order = {start}, [start], []\nwhile queue:\n    t = queue.pop(0); order.append(t)\n    for nb in neighbors(t):\n        if nb not in seen: seen.add(nb); queue.append(nb)\nprint(\"Reachable from\", start, \":\", order)\nfor t in order:\n    print(f\"  {t}: {', '.join(schema[t]['columns'])}\")\n";
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
  if(!new RegExp("^JAH\\-ATK122\\-\\d+$").test(r.id||''))e.push('id');
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
var gen={version:"jahdb-archive-toolkit-database-table-traverser-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-database-table-traverser",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
