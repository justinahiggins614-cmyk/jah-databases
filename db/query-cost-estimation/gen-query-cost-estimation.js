(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["statistics", "operators", "planning", "resources", "distribution"];
var PREFIX='JAH-QCE-';
var USE="Used by database engineers tuning optimizers and by developers understanding slow queries.";
var FLD=[["component", "Component"], ["estimates", "Estimates"], ["unit", "Unit"]];
var DEMO="# {title} - cost estimate (python3)\nrows={d1}\nsel={d2}\ncost_per_1k={d3}\nest_rows=rows*sel\ncost=est_rows/1000.0*cost_per_1k\nprint(\"estimated rows: %.0f, estimated cost: %.1f\" % (est_rows, cost))\n";
var SIG=false;
var SRC="public-harvest";
var B=[["statistics", "Table Cardinality", "The number of rows per table, the foundation every other estimate builds on.", "Table Cardinality", "row counts", "rows", "1000000", "0.1", "2.5"], ["operators", "Selectivity Estimation", "The fraction of rows passing a predicate, estimated from histograms or samples.", "Selectivity Estimation", "filter fraction", "fraction", "1000000", "0.05", "2.5"], ["planning", "Index Lookup Cost", "Cost of traversing a B-tree plus fetching matching rows, growing with selectivity.", "Index Lookup Cost", "index probes", "page I/Os", "500000", "0.02", "3.0"], ["resources", "Sequential Scan Cost", "Cost of reading every page, the baseline that indexes must beat.", "Sequential Scan Cost", "full scans", "page I/Os", "2000000", "1.0", "1.0"], ["distribution", "Join Order", "The sequence of joins; wrong orders explode intermediate results exponentially.", "Join Order", "plan shape", "intermediate rows", "800000", "0.1", "2.0"], ["statistics", "Hash Join Build Cost", "Memory and CPU to build the hash table on the smaller input.", "Hash Join Build Cost", "build phase", "bytes hashed", "300000", "1.0", "1.5"], ["operators", "Sort Cost", "O(n log n) cost of ordering, with spill penalties when memory is exceeded.", "Sort Cost", "order by", "comparisons", "400000", "1.0", "2.0"], ["planning", "Aggregation Cost", "Grouping cost driven by group count and whether hashing or sorting is used.", "Aggregation Cost", "group by", "groups", "250000", "0.2", "1.8"], ["resources", "Network Transfer Cost", "Bytes moved between nodes in distributed queries, often the dominant cost.", "Network Transfer Cost", "shuffles", "bytes", "1000000", "0.3", "4.0"], ["distribution", "Predicate Evaluation Cost", "CPU per row for complex expressions, regexes, or UDF calls.", "Predicate Evaluation Cost", "filters", "ns per row", "1500000", "0.5", "0.8"], ["statistics", "Histogram Statistics", "Bucketed value distributions that power selectivity estimates.", "Histogram Statistics", "stats quality", "buckets", "1000000", "0.1", "0.5"], ["operators", "Sampling-based Estimation", "Runs the predicate on a sample to estimate selectivity directly.", "Sampling-based Estimation", "selectivity", "sample rows", "2000000", "0.08", "1.2"], ["planning", "Plan Cache Hit Rate", "Fraction of queries reusing cached plans, avoiding optimization overhead.", "Plan Cache Hit Rate", "cache", "hit ratio", "500000", "0.1", "0.3"], ["resources", "Parallelism Degree", "How many workers split the work; more is not always better past the knee.", "Parallelism Degree", "DOP", "workers", "1000000", "0.2", "1.0"], ["distribution", "Memory Grant", "Memory reserved per query; underestimates cause spills, overestimates waste.", "Memory Grant", "grants", "MB", "600000", "0.15", "1.1"], ["statistics", "Spill-to-disk Risk", "Probability intermediate results exceed memory and spill, multiplying cost.", "Spill-to-disk Risk", "spills", "probability", "400000", "0.1", "5.0"], ["operators", "Subquery Flattening", "Rewriting subqueries as joins so the optimizer sees the whole plan.", "Subquery Flattening", "rewrites", "plan nodes", "350000", "0.2", "0.6"], ["planning", "Materialized View Match", "Detecting when a precomputed view can answer the query directly.", "Materialized View Match", "matches", "saved I/O", "900000", "0.05", "0.4"], ["resources", "Partition Pruning", "Skipping partitions the predicate cannot match, the biggest distributed win.", "Partition Pruning", "pruned", "partitions skipped", "5000000", "0.2", "0.7"], ["distribution", "Skew Adjustment", "Correcting estimates when data skew makes averages lie about hot keys.", "Skew Adjustment", "skew factor", "ratio", "1200000", "0.25", "1.3"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-query-cost-estimation-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('query-cost-estimation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
