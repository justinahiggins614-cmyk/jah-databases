(function(){'use strict';
/* JAH Oslo Travel Guide Database generator — "jahdb-guide-oslo-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GOSL-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Oslo: Orientation and First Impressions", "Best Time to Visit Oslo", "Getting to Oslo", "Getting Around Oslo", "Where to Stay in Oslo", "Money, Costs, and Budgeting for Oslo", "Language Essentials for Oslo", "Safety and Health in Oslo", "Customs and Etiquette in Oslo", "What to Pack for Oslo", "Your First Day in Oslo: A Walking Route", "Tourist Information and Emergency Numbers for Oslo"], "Compounded": ["Oslo: Oslo Opera House", "Oslo: MUNCH", "Oslo: Holmenkollen", "Oslo: The Royal Palace", "Oslo: National Museum", "Oslo: Fram Museum", "Oslo Neighborhood Deep-Dive: Sentrum", "Oslo Neighborhood Deep-Dive: Grünerløkka", "Oslo Neighborhood Deep-Dive: Aker Brygge", "Eating in Oslo: Dishes You Must Try", "Markets and Shopping in Oslo", "Parks, Water, and Green Escapes in Oslo"], "Advanced": ["Hidden Gems of Oslo", "Oslo in Three Days: The Essential Itinerary", "Oslo in Five Days: The Deep Itinerary", "Day Trip from Oslo: Drøbak", "Day Trip from Oslo: Fredrikstad", "Photography and Viewpoints in Oslo", "Nightlife and Evenings in Oslo", "Festivals and Events Calendar for Oslo", "Oslo with Kids", "Living Like a Local: The Extended Stay in Oslo"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-oslo demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-oslo-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-oslo",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
