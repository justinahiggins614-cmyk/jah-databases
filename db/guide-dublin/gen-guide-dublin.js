(function(){'use strict';
/* JAH Dublin Travel Guide Database generator — "jahdb-guide-dublin-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GDUB2-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Dublin: Orientation and First Impressions", "Best Time to Visit Dublin", "Getting to Dublin", "Getting Around Dublin", "Where to Stay in Dublin", "Money, Costs, and Budgeting for Dublin", "Language Essentials for Dublin", "Safety and Health in Dublin", "Customs and Etiquette in Dublin", "What to Pack for Dublin", "Your First Day in Dublin: A Walking Route", "Tourist Information and Emergency Numbers for Dublin"], "Compounded": ["Dublin: Trinity College", "Dublin: Guinness Storehouse", "Dublin: St Patrick’s Cathedral", "Dublin: Kilmainham Gaol", "Dublin: EPIC The Irish Emigration Museum", "Dublin: National Museum", "Dublin Neighborhood Deep-Dive: Temple Bar", "Dublin Neighborhood Deep-Dive: St Stephen’s Green", "Dublin Neighborhood Deep-Dive: Portobello", "Eating in Dublin: Dishes You Must Try", "Markets and Shopping in Dublin", "Parks, Water, and Green Escapes in Dublin"], "Advanced": ["Hidden Gems of Dublin", "Dublin in Three Days: The Essential Itinerary", "Dublin in Five Days: The Deep Itinerary", "Day Trip from Dublin: Howth", "Day Trip from Dublin: Newgrange", "Photography and Viewpoints in Dublin", "Nightlife and Evenings in Dublin", "Festivals and Events Calendar for Dublin", "Dublin with Kids", "Living Like a Local: The Extended Stay in Dublin"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-dublin demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-dublin-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-dublin",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
