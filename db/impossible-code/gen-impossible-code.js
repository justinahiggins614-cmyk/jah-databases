(function(){'use strict';
/* JAH Impossible Code Database generator — jahdb-impossible-code-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IC-";
var FIELDS=["algorithms","data-structures","search-and-sort","parsing","encoding","reliability-patterns"];
var TOPICS={
 "algorithms": [
  "Toposort \u2014 topological sort (Kahn)",
  "Kahnsort \u2014 topological sort (Kahn)",
  "Dagsort \u2014 topological sort (Kahn)",
  "Toposort \u2014 topological sort (Kahn) (2)",
  "Ordersort \u2014 topological sort (Kahn)",
  "Toposort \u2014 topological sort (Kahn) (3)",
  "Intervalmerge \u2014 interval merging",
  "Rangemerge \u2014 interval merging",
  "Intervalmerge \u2014 interval merging (2)",
  "Spanmerge \u2014 interval merging",
  "Intervalmerge \u2014 interval merging (3)",
  "Ivmerge \u2014 interval merging"
 ],
 "data-structures": [
  "Lrucache \u2014 LRU cache (capacity 2)",
  "Lrucache \u2014 LRU cache (capacity 3)",
  "Lrucache \u2014 LRU cache (capacity 4)",
  "Lrucache \u2014 LRU cache (capacity 5)",
  "Lrucache \u2014 LRU cache (capacity 8)",
  "Lrucache \u2014 LRU cache (capacity 10)",
  "Unionfind \u2014 disjoint-set union-find",
  "Disjointset \u2014 disjoint-set union-find",
  "Dsu \u2014 disjoint-set union-find",
  "Unionfind \u2014 disjoint-set union-find (2)",
  "Partitions \u2014 disjoint-set union-find",
  "Unionfind \u2014 disjoint-set union-find (3)"
 ],
 "search-and-sort": [
  "Astar \u2014 A* grid pathfinding",
  "Gridastar \u2014 A* grid pathfinding",
  "Pathfind \u2014 A* grid pathfinding",
  "Astar \u2014 A* grid pathfinding (2)",
  "Routefind \u2014 A* grid pathfinding",
  "Astar \u2014 A* grid pathfinding (3)",
  "Binsearch \u2014 binary search bounds",
  "Bisectbounds \u2014 binary search bounds",
  "Binsearch \u2014 binary search bounds (2)",
  "Rangefind \u2014 binary search bounds",
  "Binsearch \u2014 binary search bounds (3)",
  "Sortedcount \u2014 binary search bounds"
 ],
 "parsing": [
  "Expreval \u2014 arithmetic expression evaluator",
  "Mathexpr \u2014 arithmetic expression evaluator",
  "Expreval \u2014 arithmetic expression evaluator (2)",
  "Formulaparse \u2014 arithmetic expression evaluator",
  "Expreval \u2014 arithmetic expression evaluator (3)",
  "Calcexpr \u2014 arithmetic expression evaluator"
 ],
 "encoding": [
  "Rlecodec \u2014 run-length codec",
  "Rlecodec \u2014 run-length codec (2)",
  "Runlength \u2014 run-length codec",
  "Rlecodec \u2014 run-length codec (3)",
  "Rlezip \u2014 run-length codec",
  "Rlecodec \u2014 run-length codec (4)",
  "Varint \u2014 varint codec",
  "Varintcodec \u2014 varint codec",
  "Varint \u2014 varint codec (2)",
  "Uvarint \u2014 varint codec",
  "Varint \u2014 varint codec (3)",
  "Vintcodec \u2014 varint codec"
 ],
 "reliability-patterns": [
  "Retry \u2014 retry decorator with backoff",
  "Backoff \u2014 retry decorator with backoff",
  "Retry \u2014 retry decorator with backoff (2)",
  "Retrypolicy \u2014 retry decorator with backoff",
  "Retry \u2014 retry decorator with backoff (3)",
  "Resilient \u2014 retry decorator with backoff"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Impossible Code — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — code module record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A code module record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"module-tester",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-impossible-code-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('impossible-code',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
