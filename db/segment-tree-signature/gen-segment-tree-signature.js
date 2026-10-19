(function(){'use strict';
/* JAH The Segment Tree Signature Database generator — jahdb-segment-tree-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SGTS-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Segment Tree overview level 1",
  "Segment Tree overview level 2",
  "Segment Tree overview level 3"
 ],
 "implementation": [
  "Segment Tree in Python",
  "Segment Tree in JavaScript",
  "Segment Tree in Java",
  "Segment Tree in C++"
 ],
 "operations": [
  "build \u2014 Segment Tree",
  "range query \u2014 Segment Tree",
  "point update \u2014 Segment Tree",
  "range update (lazy) \u2014 Segment Tree",
  "lazy push / apply \u2014 Segment Tree",
  "array representation (4n) \u2014 Segment Tree"
 ],
 "analysis": [
  "Segment Tree \u2014 analysis"
 ],
 "interview": [
  "Range Sum Query \u2014 Mutable (LeetCode 307): support point updates and r\u2026",
  "Range minimum query with point updates over a static-size array.",
  "Count of smaller numbers after self (LeetCode 315): for each element,\u2026",
  "Range add + range sum with lazy propagation: support adding v to all \u2026",
  "Falling squares (LeetCode 699): squares fall left-to-right; each land\u2026"
 ],
 "variants": [
  "Lazy Segment Tree \u2014 Segment Tree",
  "Iterative Segment Tree \u2014 Segment Tree",
  "Sparse / Dynamic Segment Tree \u2014 Segment Tree"
 ],
 "uses": [
  "Segment Tree \u2014 uses"
 ],
 "visualization": [
  "Segment Tree \u2014 visualization"
 ],
 "pitfalls": [
  "Segment Tree \u2014 pitfalls"
 ],
 "comparisons": [
  "Segment Tree \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Segment Tree Signature Database — "+safe+"\n"
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
    name:topic+' — segment tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A segment tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-segment-tree-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('segment-tree-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
