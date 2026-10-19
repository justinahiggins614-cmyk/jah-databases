(function(){'use strict';
/* JAH The Circular Queue Database generator — jahdb-circular-queue-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CQU-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Circular Queue overview level 1",
  "Circular Queue overview level 2",
  "Circular Queue overview level 3"
 ],
 "implementation": [
  "Circular Queue in Python",
  "Circular Queue in JavaScript",
  "Circular Queue in Java",
  "Circular Queue in C++"
 ],
 "operations": [
  "enqueue \u2014 Circular Queue",
  "dequeue \u2014 Circular Queue",
  "peek / front \u2014 Circular Queue",
  "is_full / is_empty \u2014 Circular Queue",
  "size \u2014 Circular Queue",
  "resize (grow the ring) \u2014 Circular Queue",
  "head/tail wrap arithmetic \u2014 Circular Queue",
  "overwrite-oldest mode \u2014 Circular Queue"
 ],
 "analysis": [
  "Circular Queue \u2014 analysis"
 ],
 "interview": [
  "Implement a circular queue (LeetCode 622): MyCircularQueue(k) with en\u2026",
  "Design a moving average over the last N values of a data stream (Leet\u2026",
  "Simulate the Josephus problem with a circular queue: n people in a ci\u2026",
  "Design a hit counter counting hits in the last 5 minutes (LeetCode 36\u2026",
  "Explain the three ways to distinguish full from empty when head == ta\u2026"
 ],
 "variants": [
  "Fixed Ring Buffer (No Growth) \u2014 Circular Queue",
  "Overwriting Ring (Latest-N Window) \u2014 Circular Queue",
  "Double-Ended Ring (Deque on a Circle) \u2014 Circular Queue"
 ],
 "uses": [
  "Circular Queue \u2014 uses"
 ],
 "visualization": [
  "Circular Queue \u2014 visualization"
 ],
 "pitfalls": [
  "Circular Queue \u2014 pitfalls"
 ],
 "comparisons": [
  "Circular Queue \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Circular Queue Database — "+safe+"\n"
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
    name:topic+' — circular queue record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A circular queue record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-circular-queue-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('circular-queue',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
