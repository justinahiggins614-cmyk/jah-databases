(function(){'use strict';
/* JAH Toronto Travel Guide Database generator — "jahdb-guide-toronto-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GTOR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Toronto: Orientation and First Impressions", "Best Time to Visit Toronto", "Getting to Toronto", "Getting Around Toronto", "Where to Stay in Toronto", "Money, Costs, and Budgeting for Toronto", "Language Essentials for Toronto", "Safety and Health in Toronto", "Customs and Etiquette in Toronto", "What to Pack for Toronto", "Your First Day in Toronto: A Walking Route", "Tourist Information and Emergency Numbers for Toronto"], "Compounded": ["Toronto: CN Tower", "Toronto: Toronto Islands", "Toronto: Distillery District", "Toronto: Casa Loma", "Toronto: Royal Ontario Museum", "Toronto: Art Gallery of Ontario", "Toronto Neighborhood Deep-Dive: Downtown Core", "Toronto Neighborhood Deep-Dive: Queen West", "Toronto Neighborhood Deep-Dive: The Distillery", "Eating in Toronto: Dishes You Must Try", "Markets and Shopping in Toronto", "Parks, Water, and Green Escapes in Toronto"], "Advanced": ["Hidden Gems of Toronto", "Toronto in Three Days: The Essential Itinerary", "Toronto in Five Days: The Deep Itinerary", "Day Trip from Toronto: Niagara Falls", "Day Trip from Toronto: Niagara-on-the-Lake", "Photography and Viewpoints in Toronto", "Nightlife and Evenings in Toronto", "Festivals and Events Calendar for Toronto", "Toronto with Kids", "Living Like a Local: The Extended Stay in Toronto"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-toronto demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-toronto-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-toronto",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
