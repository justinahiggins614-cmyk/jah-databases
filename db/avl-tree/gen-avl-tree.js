(function(){'use strict';
/* JAH The AVL Tree Database generator — jahdb-avl-tree-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AVL-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "AVL Tree overview level 1",
  "AVL Tree overview level 2",
  "AVL Tree overview level 3"
 ],
 "implementation": [
  "AVL Tree in Python",
  "AVL Tree in JavaScript",
  "AVL Tree in Java",
  "AVL Tree in C++"
 ],
 "operations": [
  "insert \u2014 AVL Tree",
  "delete \u2014 AVL Tree",
  "search \u2014 AVL Tree",
  "balance factor maintenance \u2014 AVL Tree",
  "LL rotation (right rotate) \u2014 AVL Tree",
  "RR rotation (left rotate) \u2014 AVL Tree",
  "LR rotation (left-right double) \u2014 AVL Tree",
  "RL rotation (right-left double) \u2014 AVL Tree",
  "find min / max \u2014 AVL Tree"
 ],
 "analysis": [
  "AVL Tree \u2014 analysis"
 ],
 "interview": [
  "Insert 10, 20, 30, 40, 50, 25 into an empty AVL tree. Show the tree a\u2026",
  "Write a function that checks whether a binary tree is a valid AVL tre\u2026",
  "Find the kth smallest element in an AVL tree in O(log n).",
  "Convert a sorted array into a height-balanced BST (AVL-shaped) in O(n\u2026",
  "Lowest common ancestor of two values in a BST/AVL tree."
 ],
 "variants": [
  "AVL vs Red-Black: The Strictness Trade \u2014 AVL Tree",
  "Weight-Balanced Trees (BB[alpha]) \u2014 AVL Tree",
  "Scapegoat Tree (Rotation-Free Rebalancing) \u2014 AVL Tree"
 ],
 "uses": [
  "AVL Tree \u2014 uses"
 ],
 "visualization": [
  "AVL Tree \u2014 visualization"
 ],
 "pitfalls": [
  "AVL Tree \u2014 pitfalls"
 ],
 "comparisons": [
  "AVL Tree \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The AVL Tree Database — "+safe+"\n"
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
    name:topic+' — avl tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A avl tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-avl-tree-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('avl-tree',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
