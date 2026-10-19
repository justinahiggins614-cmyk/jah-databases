(function(){'use strict';
/* JAH The Red-Black Tree Signature Database generator — jahdb-red-black-tree-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RBLS-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Red-Black Tree overview level 1",
  "Red-Black Tree overview level 2",
  "Red-Black Tree overview level 3"
 ],
 "implementation": [
  "Red-Black Tree in Python",
  "Red-Black Tree in JavaScript",
  "Red-Black Tree in Java",
  "Red-Black Tree in C++"
 ],
 "operations": [
  "insert + fix-up \u2014 Red-Black Tree",
  "delete + fix-up \u2014 Red-Black Tree",
  "search \u2014 Red-Black Tree",
  "color flip \u2014 Red-Black Tree",
  "left / right rotation \u2014 Red-Black Tree",
  "black-height maintenance \u2014 Red-Black Tree",
  "the five properties \u2014 Red-Black Tree"
 ],
 "analysis": [
  "Red-Black Tree \u2014 analysis"
 ],
 "interview": [
  "State the five red-black properties and prove the height bound h <= 2\u2026",
  "Why does inserting a RED node (not black) preserve the black-height?",
  "When would you choose a red-black tree over an AVL tree? Over a hash \u2026",
  "Explain the 2-3-4 tree correspondence: what does a color flip represe\u2026",
  "Count the black nodes on every root-to-leaf path and verify they are \u2026"
 ],
 "variants": [
  "Left-Leaning Red-Black (LLRB) \u2014 Red-Black Tree",
  "2-3-4 Tree (The Isomorphism) \u2014 Red-Black Tree",
  "AA Tree \u2014 Red-Black Tree"
 ],
 "uses": [
  "Red-Black Tree \u2014 uses"
 ],
 "visualization": [
  "Red-Black Tree \u2014 visualization"
 ],
 "pitfalls": [
  "Red-Black Tree \u2014 pitfalls"
 ],
 "comparisons": [
  "Red-Black Tree \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Red-Black Tree Signature Database — "+safe+"\n"
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
    name:topic+' — red-black tree record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A red-black tree record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-red-black-tree-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('red-black-tree-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
