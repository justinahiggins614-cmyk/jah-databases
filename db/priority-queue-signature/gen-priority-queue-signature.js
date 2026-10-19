(function(){'use strict';
/* JAH The Priority Queue Signature Database generator — jahdb-priority-queue-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PQS-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Priority Queue overview level 1",
  "Priority Queue overview level 2",
  "Priority Queue overview level 3"
 ],
 "implementation": [
  "Priority Queue in Python",
  "Priority Queue in JavaScript",
  "Priority Queue in Java",
  "Priority Queue in C++"
 ],
 "operations": [
  "push / insert \u2014 Priority Queue",
  "pop / extract-min (extract-max) \u2014 Priority Queue",
  "peek \u2014 Priority Queue",
  "heapify / build-heap \u2014 Priority Queue",
  "decrease-key / increase-key \u2014 Priority Queue",
  "merge two heaps \u2014 Priority Queue",
  "comparator / custom ordering \u2014 Priority Queue"
 ],
 "analysis": [
  "Priority Queue \u2014 analysis"
 ],
 "interview": [
  "Find the kth largest element in an unsorted array in O(n log k).",
  "Merge k sorted linked lists into one sorted list (LeetCode 23).",
  "Top k frequent elements (LeetCode 347).",
  "Task scheduler (LeetCode 621): given tasks and cooldown n, find the m\u2026",
  "Find the median of a data stream (LeetCode 295): support addNum and f\u2026"
 ],
 "variants": [
  "d-Ary Heap \u2014 Priority Queue",
  "Fibonacci Heap (Amortized Royalty) \u2014 Priority Queue",
  "Pairing Heap (The Practitioner's Meldable) \u2014 Priority Queue"
 ],
 "uses": [
  "Priority Queue \u2014 uses"
 ],
 "visualization": [
  "Priority Queue \u2014 visualization"
 ],
 "pitfalls": [
  "Priority Queue \u2014 pitfalls"
 ],
 "comparisons": [
  "Priority Queue \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Priority Queue Signature Database — "+safe+"\n"
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
    name:topic+' — priority queue record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A priority queue record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-priority-queue-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('priority-queue-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
