(function(){'use strict';
/* JAH Signature Paris Travel Guide Database generator — "jahdb-guide-paris-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GPARS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Paris: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Paris (Signature Edition)", "Getting to Paris (Signature Edition)", "Getting Around Paris (Signature Edition)", "Where to Stay in Paris (Signature Edition)", "Money, Costs, and Budgeting for Paris (Signature Edition)", "Language Essentials for Paris (Signature Edition)", "Safety and Health in Paris (Signature Edition)", "Customs and Etiquette in Paris (Signature Edition)", "What to Pack for Paris (Signature Edition)", "Your First Day in Paris: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Paris (Signature Edition)"], "Compounded": ["Paris: Eiffel Tower (Signature Edition)", "Paris: The Louvre (Signature Edition)", "Paris: Notre-Dame (Signature Edition)", "Paris: Sacré-Cœur (Signature Edition)", "Paris: Musée d’Orsay (Signature Edition)", "Paris: Centre Pompidou (Signature Edition)", "Paris Neighborhood Deep-Dive: Le Marais (Signature Edition)", "Paris Neighborhood Deep-Dive: Saint-Germain-des-Prés (Signature Edition)", "Paris Neighborhood Deep-Dive: Montmartre (Signature Edition)", "Eating in Paris: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Paris (Signature Edition)", "Parks, Water, and Green Escapes in Paris (Signature Edition)"], "Advanced": ["Hidden Gems of Paris (Signature Edition)", "Paris in Three Days: The Essential Itinerary (Signature Edition)", "Paris in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Paris: Versailles (Signature Edition)", "Day Trip from Paris: Giverny (Signature Edition)", "Photography and Viewpoints in Paris (Signature Edition)", "Nightlife and Evenings in Paris (Signature Edition)", "Festivals and Events Calendar for Paris (Signature Edition)", "Paris with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Paris (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-paris-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-paris-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-paris-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
