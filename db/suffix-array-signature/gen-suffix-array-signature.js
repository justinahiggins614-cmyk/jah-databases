(function(){'use strict';
/* JAH The Suffix Array Signature Database generator — jahdb-suffix-array-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SUFA-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Suffix Array overview level 1",
  "Suffix Array overview level 2",
  "Suffix Array overview level 3"
 ],
 "implementation": [
  "Suffix Array in Python",
  "Suffix Array in JavaScript",
  "Suffix Array in Java",
  "Suffix Array in C++"
 ],
 "operations": [
  "construction (prefix-doubling) \u2014 Suffix Array",
  "construction (SA-IS / induced) \u2014 Suffix Array",
  "LCP array (Kasai) \u2014 Suffix Array",
  "substring search (binary search) \u2014 Suffix Array",
  "substring search (LCP-accelerated) \u2014 Suffix Array",
  "longest repeated substring \u2014 Suffix Array"
 ],
 "analysis": [
  "Suffix Array \u2014 analysis"
 ],
 "interview": [
  "Build the suffix array of 'banana' by hand using prefix-doubling. Sho\u2026",
  "Find the longest repeated substring using SA + LCP.",
  "Count the number of distinct substrings of a string.",
  "Find the longest common substring of two strings.",
  "Find all occurrences of a pattern P in text T using the suffix array."
 ],
 "variants": [
  "Suffix Automaton (SAM) \u2014 Suffix Array",
  "Suffix Trie (The Explicit View) \u2014 Suffix Array",
  "Enhanced Suffix Array (SA + LCP + Extras) \u2014 Suffix Array"
 ],
 "uses": [
  "Suffix Array \u2014 uses"
 ],
 "visualization": [
  "Suffix Array \u2014 visualization"
 ],
 "pitfalls": [
  "Suffix Array \u2014 pitfalls"
 ],
 "comparisons": [
  "Suffix Array \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Suffix Array Signature Database — "+safe+"\n"
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
    name:topic+' — suffix array record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A suffix array record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-suffix-array-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('suffix-array-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
