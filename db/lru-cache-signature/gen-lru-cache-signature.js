(function(){'use strict';
/* JAH The LRU Cache Signature Database generator — jahdb-lru-cache-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LRC-";
var FIELDS=["overview", "implementation", "operations", "analysis", "interview", "variants", "uses", "visualization", "pitfalls", "comparisons"];
var TOPICS={
 "overview": [
  "LRU Cache overview level 1",
  "LRU Cache overview level 2",
  "LRU Cache overview level 3"
 ],
 "implementation": [
  "LRU Cache in Python",
  "LRU Cache in JavaScript",
  "LRU Cache in Java",
  "LRU Cache in C++"
 ],
 "operations": [
  "get(k) \u2014 LRU Cache",
  "put(k, v) \u2014 LRU Cache",
  "evict (tail removal) \u2014 LRU Cache",
  "move-to-front on hit \u2014 LRU Cache",
  "hash map + list wiring \u2014 LRU Cache",
  "capacity management \u2014 LRU Cache"
 ],
 "analysis": [
  "LRU Cache \u2014 analysis"
 ],
 "interview": [
  "Implement an LRU cache with O(1) get and put (LeetCode 146).",
  "Design an LFU (Least Frequently Used) cache. How does it differ from \u2026",
  "Add TTL (time-to-live) expiration to an LRU cache.",
  "Why does LRU perform terribly on sequential scans larger than the cac\u2026",
  "Design a thread-safe LRU cache for high concurrency."
 ],
 "variants": [
  "LFU Cache (Frequency Over Recency) \u2014 LRU Cache",
  "ARC (Adaptive Replacement Cache) \u2014 LRU Cache",
  "CLOCK / Second-Chance (Approximate LRU) \u2014 LRU Cache"
 ],
 "uses": [
  "LRU Cache \u2014 uses"
 ],
 "visualization": [
  "LRU Cache \u2014 visualization"
 ],
 "pitfalls": [
  "LRU Cache \u2014 pitfalls"
 ],
 "comparisons": [
  "LRU Cache \u2014 comparisons"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The LRU Cache Signature Database — "+safe+"\n"
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
    name:topic+' — lru cache record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A lru cache record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-lru-cache-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('lru-cache-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
