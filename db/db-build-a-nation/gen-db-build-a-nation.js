(function(){'use strict';
/* JAH The Build a Nation Database generator — jahdb-db-build-a-nation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBND-";
var FIELDS=["The Land","The Law","The Life"];
var TOPICS={
 "The Land": [
  "The Meridian Republic \u2014 The Land",
  "The Meridian Republic \u2014 Deep Dive \u2014 The Land",
  "The Alpine Confederacy \u2014 The Land",
  "The Alpine Confederacy \u2014 Deep Dive \u2014 The Land",
  "The Saharan Federation \u2014 The Land",
  "The Saharan Federation \u2014 Deep Dive \u2014 The Land",
  "The Boreal Kingdom \u2014 The Land",
  "The Boreal Kingdom \u2014 Deep Dive \u2014 The Land",
  "The Delta Commonwealth \u2014 The Land",
  "The Delta Commonwealth \u2014 Deep Dive \u2014 The Land"
 ],
 "The Law": [
  "The Steppe Khanate \u2014 The Law",
  "The Steppe Khanate \u2014 Deep Dive \u2014 The Law",
  "The Archipelago Union \u2014 The Law",
  "The Archipelago Union \u2014 Deep Dive \u2014 The Law",
  "The City-State of Vela \u2014 The Law",
  "The City-State of Vela \u2014 Deep Dive \u2014 The Law",
  "The River Federation \u2014 The Law",
  "The River Federation \u2014 Deep Dive \u2014 The Law",
  "The Nation Builder's Kit \u2014 The Law",
  "The Nation Builder's Kit \u2014 Deep Dive \u2014 The Law"
 ],
 "The Life": [
  "The Highland Republic \u2014 The Life",
  "The Highland Republic \u2014 Deep Dive \u2014 The Life",
  "The Coast of Lights \u2014 The Life",
  "The Coast of Lights \u2014 Deep Dive \u2014 The Life",
  "The Plains Democracy \u2014 The Life",
  "The Plains Democracy \u2014 Deep Dive \u2014 The Life",
  "The Jungle Communes \u2014 The Life",
  "The Jungle Communes \u2014 Deep Dive \u2014 The Life",
  "The Tundra Collective \u2014 The Life",
  "The Tundra Collective \u2014 Deep Dive \u2014 The Life",
  "The Volcanic Isles \u2014 The Life",
  "The Volcanic Isles \u2014 Deep Dive \u2014 The Life",
  "The Oasis Republic \u2014 The Life",
  "The Oasis Republic \u2014 Deep Dive \u2014 The Life"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nation Design Study — "+safe+"\n"
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
    name:topic+' — nation design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A nation design record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-build-a-nation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-build-a-nation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
