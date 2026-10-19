(function(){'use strict';
/* JAH Nepal Travel Guide Database generator — "jahdb-guide-nepal-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GNEP-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Nepal: Orientation and First Impressions", "Best Time to Visit Nepal", "Getting to Nepal", "Getting Around Nepal", "Where to Stay in Nepal", "Money, Costs, and Budgeting for Nepal", "Language Essentials for Nepal", "Safety and Health in Nepal", "Customs and Etiquette in Nepal", "What to Pack for Nepal", "Your First Day in Nepal: A Walking Route", "Tourist Information and Emergency Numbers for Nepal"], "Compounded": ["Nepal: Sagarmatha (Everest)", "Nepal: Kathmandu Valley", "Nepal: Pokhara", "Nepal: Chitwan", "Nepal: The National Museum", "Nepal: The Patan Museum", "Nepal Neighborhood Deep-Dive: Thamel (Kathmandu)", "Nepal Neighborhood Deep-Dive: Pokhara", "Nepal Neighborhood Deep-Dive: Bhaktapur", "Eating in Nepal: Dishes You Must Try", "Markets and Shopping in Nepal", "Parks, Water, and Green Escapes in Nepal"], "Advanced": ["Hidden Gems of Nepal", "Nepal in Three Days: The Essential Itinerary", "Nepal in Five Days: The Deep Itinerary", "Day Trip from Nepal: Bhaktapur from Kathmandu", "Day Trip from Nepal: Nagarkot from Kathmandu", "Photography and Viewpoints in Nepal", "Nightlife and Evenings in Nepal", "Festivals and Events Calendar for Nepal", "Nepal with Kids", "Living Like a Local: The Extended Stay in Nepal"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-nepal demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-nepal-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-nepal",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
