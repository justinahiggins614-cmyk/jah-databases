(function(){'use strict';
/* JAH Ireland Travel Guide Database generator — "jahdb-guide-ireland-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GIRE-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Ireland: Orientation and First Impressions", "Best Time to Visit Ireland", "Getting to Ireland", "Getting Around Ireland", "Where to Stay in Ireland", "Money, Costs, and Budgeting for Ireland", "Language Essentials for Ireland", "Safety and Health in Ireland", "Customs and Etiquette in Ireland", "What to Pack for Ireland", "Your First Day in Ireland: A Walking Route", "Tourist Information and Emergency Numbers for Ireland"], "Compounded": ["Ireland: Cliffs of Moher", "Ireland: Ring of Kerry", "Ireland: Newgrange", "Ireland: The Burren", "Ireland: EPIC", "Ireland: The National Museum", "Ireland Neighborhood Deep-Dive: Dublin", "Ireland Neighborhood Deep-Dive: Galway", "Ireland Neighborhood Deep-Dive: Killarney", "Eating in Ireland: Dishes You Must Try", "Markets and Shopping in Ireland", "Parks, Water, and Green Escapes in Ireland"], "Advanced": ["Hidden Gems of Ireland", "Ireland in Three Days: The Essential Itinerary", "Ireland in Five Days: The Deep Itinerary", "Day Trip from Ireland: Newgrange from Dublin", "Day Trip from Ireland: Howth from Dublin", "Photography and Viewpoints in Ireland", "Nightlife and Evenings in Ireland", "Festivals and Events Calendar for Ireland", "Ireland with Kids", "Living Like a Local: The Extended Stay in Ireland"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-ireland demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — travel guide record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A travel guide record study. Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest-sample",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-guide-ireland-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-ireland",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
