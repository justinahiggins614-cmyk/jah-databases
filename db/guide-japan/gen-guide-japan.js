(function(){'use strict';
/* JAH Japan Travel Guide Database generator — "jahdb-guide-japan-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GJAP-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Japan: Orientation and First Impressions", "Best Time to Visit Japan", "Getting to Japan", "Getting Around Japan", "Where to Stay in Japan", "Money, Costs, and Budgeting for Japan", "Language Essentials for Japan", "Safety and Health in Japan", "Customs and Etiquette in Japan", "What to Pack for Japan", "Your First Day in Japan: A Walking Route", "Tourist Information and Emergency Numbers for Japan"], "Compounded": ["Japan: Kyoto", "Japan: Mt. Fuji", "Japan: Miyajima", "Japan: Nara", "Japan: Tokyo National Museum", "Japan: The Hiroshima Peace Memorial", "Japan Neighborhood Deep-Dive: Tokyo", "Japan Neighborhood Deep-Dive: Kyoto", "Japan Neighborhood Deep-Dive: Osaka", "Eating in Japan: Dishes You Must Try", "Markets and Shopping in Japan", "Parks, Water, and Green Escapes in Japan"], "Advanced": ["Hidden Gems of Japan", "Japan in Three Days: The Essential Itinerary", "Japan in Five Days: The Deep Itinerary", "Day Trip from Japan: Nikko from Tokyo", "Day Trip from Japan: Nara from Kyoto", "Photography and Viewpoints in Japan", "Nightlife and Evenings in Japan", "Festivals and Events Calendar for Japan", "Japan with Kids", "Living Like a Local: The Extended Stay in Japan"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-japan demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-japan-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-japan",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
