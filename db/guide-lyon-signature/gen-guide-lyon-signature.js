(function(){'use strict';
/* JAH Signature Lyon Travel Guide Database generator — "jahdb-guide-lyon-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GLYOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Lyon: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Lyon (Signature Edition)", "Getting to Lyon (Signature Edition)", "Getting Around Lyon (Signature Edition)", "Where to Stay in Lyon (Signature Edition)", "Money, Costs, and Budgeting for Lyon (Signature Edition)", "Language Essentials for Lyon (Signature Edition)", "Safety and Health in Lyon (Signature Edition)", "Customs and Etiquette in Lyon (Signature Edition)", "What to Pack for Lyon (Signature Edition)", "Your First Day in Lyon: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Lyon (Signature Edition)"], "Compounded": ["Lyon: Vieux Lyon (Signature Edition)", "Lyon: Fourvière Basilica (Signature Edition)", "Lyon: The traboules (Signature Edition)", "Lyon: Place Bellecour (Signature Edition)", "Lyon: Musée des Beaux-Arts (Signature Edition)", "Lyon: The Lumière Museum (Signature Edition)", "Lyon Neighborhood Deep-Dive: Vieux Lyon (Signature Edition)", "Lyon Neighborhood Deep-Dive: Presqu’île (Signature Edition)", "Lyon Neighborhood Deep-Dive: Croix-Rousse (Signature Edition)", "Eating in Lyon: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Lyon (Signature Edition)", "Parks, Water, and Green Escapes in Lyon (Signature Edition)"], "Advanced": ["Hidden Gems of Lyon (Signature Edition)", "Lyon in Three Days: The Essential Itinerary (Signature Edition)", "Lyon in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Lyon: Beaujolais (Signature Edition)", "Day Trip from Lyon: Pérouges (Signature Edition)", "Photography and Viewpoints in Lyon (Signature Edition)", "Nightlife and Evenings in Lyon (Signature Edition)", "Festivals and Events Calendar for Lyon (Signature Edition)", "Lyon with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Lyon (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-lyon-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-lyon-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-lyon-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
