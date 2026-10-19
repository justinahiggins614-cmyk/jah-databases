(function(){'use strict';
/* JAH Signature Florence Travel Guide Database generator — "jahdb-guide-florence-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GFLOS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Florence: Orientation and First Impressions (Signature Edition)", "Best Time to Visit Florence (Signature Edition)", "Getting to Florence (Signature Edition)", "Getting Around Florence (Signature Edition)", "Where to Stay in Florence (Signature Edition)", "Money, Costs, and Budgeting for Florence (Signature Edition)", "Language Essentials for Florence (Signature Edition)", "Safety and Health in Florence (Signature Edition)", "Customs and Etiquette in Florence (Signature Edition)", "What to Pack for Florence (Signature Edition)", "Your First Day in Florence: A Walking Route (Signature Edition)", "Tourist Information and Emergency Numbers for Florence (Signature Edition)"], "Compounded": ["Florence: Florence Cathedral (Duomo) (Signature Edition)", "Florence: Uffizi Gallery (Signature Edition)", "Florence: Accademia (Signature Edition)", "Florence: Ponte Vecchio (Signature Edition)", "Florence: Bargello Museum (Signature Edition)", "Florence: Palazzo Pitti (Signature Edition)", "Florence Neighborhood Deep-Dive: Centro Storico (Signature Edition)", "Florence Neighborhood Deep-Dive: Oltrarno (Signature Edition)", "Florence Neighborhood Deep-Dive: Santa Croce (Signature Edition)", "Eating in Florence: Dishes You Must Try (Signature Edition)", "Markets and Shopping in Florence (Signature Edition)", "Parks, Water, and Green Escapes in Florence (Signature Edition)"], "Advanced": ["Hidden Gems of Florence (Signature Edition)", "Florence in Three Days: The Essential Itinerary (Signature Edition)", "Florence in Five Days: The Deep Itinerary (Signature Edition)", "Day Trip from Florence: Siena (Signature Edition)", "Day Trip from Florence: Pisa (Signature Edition)", "Photography and Viewpoints in Florence (Signature Edition)", "Nightlife and Evenings in Florence (Signature Edition)", "Festivals and Events Calendar for Florence (Signature Edition)", "Florence with Kids (Signature Edition)", "Living Like a Local: The Extended Stay in Florence (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-florence-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-florence-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-florence-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
