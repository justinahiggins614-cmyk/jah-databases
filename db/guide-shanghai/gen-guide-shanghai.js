(function(){'use strict';
/* JAH Shanghai Travel Guide Database generator — "jahdb-guide-shanghai-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GSHA-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Shanghai: Orientation and First Impressions", "Best Time to Visit Shanghai", "Getting to Shanghai", "Getting Around Shanghai", "Where to Stay in Shanghai", "Money, Costs, and Budgeting for Shanghai", "Language Essentials for Shanghai", "Safety and Health in Shanghai", "Customs and Etiquette in Shanghai", "What to Pack for Shanghai", "Your First Day in Shanghai: A Walking Route", "Tourist Information and Emergency Numbers for Shanghai"], "Compounded": ["Shanghai: The Bund", "Shanghai: Yu Garden", "Shanghai: Shanghai Tower", "Shanghai: Jade Buddha Temple", "Shanghai: Shanghai Museum", "Shanghai: China Art Museum", "Shanghai Neighborhood Deep-Dive: The Bund", "Shanghai Neighborhood Deep-Dive: French Concession", "Shanghai Neighborhood Deep-Dive: Jing’an", "Eating in Shanghai: Dishes You Must Try", "Markets and Shopping in Shanghai", "Parks, Water, and Green Escapes in Shanghai"], "Advanced": ["Hidden Gems of Shanghai", "Shanghai in Three Days: The Essential Itinerary", "Shanghai in Five Days: The Deep Itinerary", "Day Trip from Shanghai: Suzhou", "Day Trip from Shanghai: Zhujiajiao", "Photography and Viewpoints in Shanghai", "Nightlife and Evenings in Shanghai", "Festivals and Events Calendar for Shanghai", "Shanghai with Kids", "Living Like a Local: The Extended Stay in Shanghai"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-shanghai demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-shanghai-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-shanghai",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
