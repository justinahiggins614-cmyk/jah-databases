(function(){'use strict';
/* JAH The Fenwick Tree Database generator — jahdb-fenwick-tree-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FWK-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Fenwick Tree overview level 1",
  "Fenwick Tree overview level 2",
  "Fenwick Tree overview level 3"
 ],
 "implementation": [
  "Fenwick Tree in Python",
  "Fenwick Tree in JavaScript",
  "Fenwick Tree in Java",
  "Fenwick Tree in C++"
 ],
 "operations": [
  "point update (add v at i) \u2014 Fenwick Tree",
  "prefix sum query (sum[1..i]) \u2014 Fenwick Tree",
  "range sum [l, r] \u2014 Fenwick Tree",
  "build \u2014 Fenwick Tree",
  "LSB trick (i & -i) \u2014 Fenwick Tree",
  "find-kth (binary lifting) \u2014 Fenwick Tree"
 ],
 "analysis": [
  "Fenwick Tree \u2014 analysis"
 ],
 "interview": [
  "Range Sum Query \u2014 Mutable with a Fenwick tree (LeetCode 307, BIT vers\u2026",
  "Count inversions in an array in O(n log n) with a Fenwick tree.",
  "Support range-add (add v to all of [l,r]) and point-query with a Fenw\u2026",
  "Find the smallest index i with prefix sum >= k (order statistics) in \u2026",
  "2D range sum: point updates and rectangle-sum queries on a grid."
 ],
 "variants": [
  "Dual BIT (Range-Update / Point-Query) \u2014 Fenwick Tree",
  "Two-BIT Range-Update / Range-Query \u2014 Fenwick Tree",
  "2D Fenwick Tree \u2014 Fenwick Tree"
 ],
 "uses": [
  "Fenwick Tree \u2014 uses"
 ],
 "visualization": [
  "Fenwick Tree \u2014 visualization"
 ],
 "pitfalls": [
  "Fenwick Tree \u2014 pitfalls"
 ],
 "comparisons": [
  "Fenwick Tree \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Fenwick Tree Database — "+safe+"\n"
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
    name:topic+' — fenwick tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fenwick tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fenwick-tree-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fenwick-tree',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
