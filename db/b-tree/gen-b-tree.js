(function(){'use strict';
/* JAH The B-Tree Database generator — jahdb-b-tree-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BTR-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "B-Tree overview level 1",
  "B-Tree overview level 2",
  "B-Tree overview level 3"
 ],
 "implementation": [
  "B-Tree in Python",
  "B-Tree in JavaScript",
  "B-Tree in Java",
  "B-Tree in C++"
 ],
 "operations": [
  "search \u2014 B-Tree",
  "insert + split \u2014 B-Tree",
  "delete + merge/borrow \u2014 B-Tree",
  "node split (full child) \u2014 B-Tree",
  "range scan \u2014 B-Tree",
  "bulk load \u2014 B-Tree"
 ],
 "analysis": [
  "B-Tree \u2014 analysis"
 ],
 "interview": [
  "Insert keys 10, 20, 5, 6, 12, 30, 7, 17 into an empty B-tree of minim\u2026",
  "Why do databases use B-trees instead of binary search trees for index\u2026",
  "For a B-tree of minimum degree t and height h, what are the minimum a\u2026",
  "How does a B+ tree improve range scans over a plain B-tree, and what \u2026",
  "Estimate the disk reads for a point lookup in a 100M-row table indexe\u2026"
 ],
 "variants": [
  "B+ Tree (The Database Standard) \u2014 B-Tree",
  "B* Tree (Higher Fill Factor) \u2014 B-Tree",
  "2-3 Tree / 2-3-4 Tree (The Teaching Bridge) \u2014 B-Tree"
 ],
 "uses": [
  "B-Tree \u2014 uses"
 ],
 "visualization": [
  "B-Tree \u2014 visualization"
 ],
 "pitfalls": [
  "B-Tree \u2014 pitfalls"
 ],
 "comparisons": [
  "B-Tree \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The B-Tree Database — "+safe+"\n"
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
    name:topic+' — b-tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A b-tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-b-tree-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('b-tree',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
