(function(){'use strict';
/* JAH The Doubly Linked List Signature Database generator — jahdb-doubly-linked-list-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DLLS-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Doubly Linked List overview level 1",
  "Doubly Linked List overview level 2",
  "Doubly Linked List overview level 3"
 ],
 "implementation": [
  "Doubly Linked List in Python",
  "Doubly Linked List in JavaScript",
  "Doubly Linked List in Java",
  "Doubly Linked List in C++"
 ],
 "operations": [
  "insert after / before a node \u2014 Doubly Linked List",
  "delete a node (given the node) \u2014 Doubly Linked List",
  "push front / push back \u2014 Doubly Linked List",
  "pop front / pop back \u2014 Doubly Linked List",
  "traverse forward / backward \u2014 Doubly Linked List",
  "find by value \u2014 Doubly Linked List",
  "reverse in place \u2014 Doubly Linked List",
  "sentinel node pattern \u2014 Doubly Linked List"
 ],
 "analysis": [
  "Doubly Linked List \u2014 analysis"
 ],
 "interview": [
  "Reverse a doubly linked list in place.",
  "A browser history supports visit(url), back(), forward(). Implement i\u2026",
  "Check whether a doubly linked list is a palindrome in O(n) time and O\u2026",
  "Insert a value into a sorted doubly linked list, keeping it sorted.",
  "Flatten a multilevel doubly linked list: each node may have a child p\u2026"
 ],
 "variants": [
  "Circular Doubly Linked List \u2014 Doubly Linked List",
  "XOR Linked List \u2014 Doubly Linked List",
  "Unrolled Linked List \u2014 Doubly Linked List"
 ],
 "uses": [
  "Doubly Linked List \u2014 uses"
 ],
 "visualization": [
  "Doubly Linked List \u2014 visualization"
 ],
 "pitfalls": [
  "Doubly Linked List \u2014 pitfalls"
 ],
 "comparisons": [
  "Doubly Linked List \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Doubly Linked List Signature Database — "+safe+"\n"
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
    name:topic+' — doubly linked list record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A doubly linked list record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-doubly-linked-list-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('doubly-linked-list-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
