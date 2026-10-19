(function(){'use strict';
/* JAH The Deque Database generator — jahdb-deque-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DQ-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Deque overview level 1",
  "Deque overview level 2",
  "Deque overview level 3"
 ],
 "implementation": [
  "Deque in Python",
  "Deque in JavaScript",
  "Deque in Java",
  "Deque in C++"
 ],
 "operations": [
  "push_back / push_front \u2014 Deque",
  "pop_back / pop_front \u2014 Deque",
  "peek front / back \u2014 Deque",
  "random access by index \u2014 Deque",
  "resize (grow) \u2014 Deque",
  "rotate by k \u2014 Deque",
  "array-deque vs linked-deque \u2014 Deque"
 ],
 "analysis": [
  "Deque \u2014 analysis"
 ],
 "interview": [
  "Sliding window maximum (LeetCode 239): given nums and k, return the m\u2026",
  "Implement a stack using queues \u2014 then explain why a deque makes it tr\u2026",
  "Check if a string is a palindrome using a deque.",
  "0-1 BFS: shortest path in a graph whose edges weigh 0 or 1. Solve in \u2026",
  "Zigzag level-order traversal of a binary tree using a deque."
 ],
 "variants": [
  "Array-Deque (Circular Buffer) \u2014 Deque",
  "Linked Deque (Doubly Linked Nodes) \u2014 Deque",
  "Chunked Deque (Block Map) \u2014 Deque"
 ],
 "uses": [
  "Deque \u2014 uses"
 ],
 "visualization": [
  "Deque \u2014 visualization"
 ],
 "pitfalls": [
  "Deque \u2014 pitfalls"
 ],
 "comparisons": [
  "Deque \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Deque Database — "+safe+"\n"
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
    name:topic+' — deque record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A deque record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-deque-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('deque',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
