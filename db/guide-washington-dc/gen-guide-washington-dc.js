(function(){'use strict';
/* JAH Washington, D.C. Travel Guide Database generator — "jahdb-guide-washington-dc-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GWDC-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Washington, D.C.: Orientation and First Impressions", "Best Time to Visit Washington, D.C.", "Getting to Washington, D.C.", "Getting Around Washington, D.C.", "Where to Stay in Washington, D.C.", "Money, Costs, and Budgeting for Washington, D.C.", "Language Essentials for Washington, D.C.", "Safety and Health in Washington, D.C.", "Customs and Etiquette in Washington, D.C.", "What to Pack for Washington, D.C.", "Your First Day in Washington, D.C.: A Walking Route", "Tourist Information and Emergency Numbers for Washington, D.C."], "Compounded": ["Washington, D.C.: The National Mall", "Washington, D.C.: Lincoln Memorial", "Washington, D.C.: The White House", "Washington, D.C.: Washington Monument", "Washington, D.C.: National Air and Space", "Washington, D.C.: National Gallery", "Washington, D.C. Neighborhood Deep-Dive: Downtown/Penn Quarter", "Washington, D.C. Neighborhood Deep-Dive: Georgetown", "Washington, D.C. Neighborhood Deep-Dive: Capitol Hill", "Eating in Washington, D.C.: Dishes You Must Try", "Markets and Shopping in Washington, D.C.", "Parks, Water, and Green Escapes in Washington, D.C."], "Advanced": ["Hidden Gems of Washington, D.C.", "Washington, D.C. in Three Days: The Essential Itinerary", "Washington, D.C. in Five Days: The Deep Itinerary", "Day Trip from Washington, D.C.: Mount Vernon", "Day Trip from Washington, D.C.: Baltimore", "Photography and Viewpoints in Washington, D.C.", "Nightlife and Evenings in Washington, D.C.", "Festivals and Events Calendar for Washington, D.C.", "Washington, D.C. with Kids", "Living Like a Local: The Extended Stay in Washington, D.C."]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-washington-dc demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-washington-dc-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-washington-dc",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
