(function(){'use strict';
/* JAH Signature Dubai Travel Guide Database generator — "jahdb-guide-dubai-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GDUBS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Dubai: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Dubai (Signature Edition)", "Getting to Dubai (Signature Edition)", "Getting Around Dubai (Signature Edition)", "Where to Stay in Dubai (Signature Edition)", "Money, Costs, and Budgeting for Dubai (Signature Edition)", "Language Essentials for Dubai (Signature Edition)", "Safety and Health in Dubai (Signature Edition)", "Customs and Etiquette in Dubai (Signature Edition)", "What to Pack for Dubai (Signature Edition)", "Your First Day in Dubai: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Dubai (Signature Edition)"], "Compounded": ["Dubai: Burj Khalifa (Signature Edition)", "Dubai: Dubai Mall (Signature Edition)", "Dubai: The Gold Souk (Signature Edition)", "Dubai: Palm Jumeirah (Signature Edition)", "Dubai: Museum of the Future (Signature Edition)", "Dubai: Etihad Museum (Signature Edition)", "Dubai Neighborhood Deep-Dive: Downtown Dubai (Signature Edition)", "Dubai Neighborhood Deep-Dive: Dubai Marina (Signature Edition)", "Dubai Neighborhood Deep-Dive: Deira (Signature Edition)", "Eating in Dubai: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Dubai (Signature Edition)", "Parks, Water, and Green Escapes in Dubai (Signature Edition)"], "Advanced": ["Hidden Gems of Dubai (Signature Edition)", "Dubai in Three Days: The Essential Itinerary (Signature Edition)", "Dubai in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Dubai: Abu Dhabi (Signature Edition)", "Day Trip from Dubai: The desert (Signature Edition)", "Photography and Viewpoints in Dubai (Signature Edition)", "Nightlife and Evenings in Dubai (Signature Edition)", "Festivals and Events Calendar for Dubai (Signature Edition)", "Dubai with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Dubai (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-dubai-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-dubai-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-dubai-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
