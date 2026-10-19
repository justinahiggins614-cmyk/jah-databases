(function(){'use strict';
/* JAH Signature Norway Travel Guide Database generator — "jahdb-guide-norway-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GNORS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Norway: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Norway (Signature Edition)", "Getting to Norway (Signature Edition)", "Getting Around Norway (Signature Edition)", "Where to Stay in Norway (Signature Edition)", "Money, Costs, and Budgeting for Norway (Signature Edition)", "Language Essentials for Norway (Signature Edition)", "Safety and Health in Norway (Signature Edition)", "Customs and Etiquette in Norway (Signature Edition)", "What to Pack for Norway (Signature Edition)", "Your First Day in Norway: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Norway (Signature Edition)"], "Compounded": ["Norway: Geirangerfjord (Signature Edition)", "Norway: Bergen (Signature Edition)", "Norway: The Lofoten (Signature Edition)", "Norway: Preikestolen (Signature Edition)", "Norway: The Fram Museum (Signature Edition)", "Norway: The Bryggens Museum (Signature Edition)", "Norway Neighborhood Deep-Dive: Oslo (Signature Edition)", "Norway Neighborhood Deep-Dive: Bergen (Signature Edition)", "Norway Neighborhood Deep-Dive: The Lofoten (Signature Edition)", "Eating in Norway: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Norway (Signature Edition)", "Parks, Water, and Green Escapes in Norway (Signature Edition)"], "Advanced": ["Hidden Gems of Norway (Signature Edition)", "Norway in Three Days: The Essential Itinerary (Signature Edition)", "Norway in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Norway: The Flåm Railway from Bergen (Signature Edition)", "Day Trip from Norway: The Hardangerfjord (Signature Edition)", "Photography and Viewpoints in Norway (Signature Edition)", "Nightlife and Evenings in Norway (Signature Edition)", "Festivals and Events Calendar for Norway (Signature Edition)", "Norway with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Norway (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-norway-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original travel guide record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original travel guide record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-guide-norway-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-norway-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
