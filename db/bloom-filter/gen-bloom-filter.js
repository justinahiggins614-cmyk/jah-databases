(function(){'use strict';
/* JAH The Bloom Filter Database generator — jahdb-bloom-filter-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BF-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "Bloom Filter overview level 1",
  "Bloom Filter overview level 2",
  "Bloom Filter overview level 3"
 ],
 "implementation": [
  "Bloom Filter in Python",
  "Bloom Filter in JavaScript",
  "Bloom Filter in Java",
  "Bloom Filter in C++"
 ],
 "operations": [
  "add(x) \u2014 Bloom Filter",
  "query(x) / maybe-contains \u2014 Bloom Filter",
  "k hash functions (double hashing) \u2014 Bloom Filter",
  "false-positive estimation \u2014 Bloom Filter",
  "optimal sizing (m, k) \u2014 Bloom Filter",
  "union of filters \u2014 Bloom Filter"
 ],
 "analysis": [
  "Bloom Filter \u2014 analysis"
 ],
 "interview": [
  "Size a Bloom filter for n = 1 million URLs with a 1% false-positive r\u2026",
  "Why can't you delete from a standard Bloom filter? What are the worka\u2026",
  "Prove a Bloom filter has no false negatives.",
  "Design a spell checker / username-availability check for 100M entries\u2026",
  "An attacker can choose inputs to your Bloom filter. What breaks, and \u2026"
 ],
 "variants": [
  "Counting Bloom Filter \u2014 Bloom Filter",
  "Cuckoo Filter \u2014 Bloom Filter",
  "Xor / Ribbon Filters (Static) \u2014 Bloom Filter"
 ],
 "uses": [
  "Bloom Filter \u2014 uses"
 ],
 "visualization": [
  "Bloom Filter \u2014 visualization"
 ],
 "pitfalls": [
  "Bloom Filter \u2014 pitfalls"
 ],
 "comparisons": [
  "Bloom Filter \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Bloom Filter Database — "+safe+"\n"
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
    name:topic+' — bloom filter record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A bloom filter record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-bloom-filter-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bloom-filter',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
