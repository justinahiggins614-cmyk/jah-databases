(function(){'use strict';
/* JAH Rio de Janeiro Travel Guide Database generator — "jahdb-guide-rio-de-janeiro-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GRIO-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Rio de Janeiro: Orientation and First Impressions", "Best Time to Visit Rio de Janeiro", "Getting to Rio de Janeiro", "Getting Around Rio de Janeiro", "Where to Stay in Rio de Janeiro", "Money, Costs, and Budgeting for Rio de Janeiro", "Language Essentials for Rio de Janeiro", "Safety and Health in Rio de Janeiro", "Customs and Etiquette in Rio de Janeiro", "What to Pack for Rio de Janeiro", "Your First Day in Rio de Janeiro: A Walking Route", "Tourist Information and Emergency Numbers for Rio de Janeiro"], "Compounded": ["Rio de Janeiro: Christ the Redeemer", "Rio de Janeiro: Sugarloaf", "Rio de Janeiro: Copacabana", "Rio de Janeiro: Ipanema", "Rio de Janeiro: Museum of Tomorrow", "Rio de Janeiro: Museu de Arte do Rio", "Rio de Janeiro Neighborhood Deep-Dive: Copacabana", "Rio de Janeiro Neighborhood Deep-Dive: Ipanema", "Rio de Janeiro Neighborhood Deep-Dive: Santa Teresa", "Eating in Rio de Janeiro: Dishes You Must Try", "Markets and Shopping in Rio de Janeiro", "Parks, Water, and Green Escapes in Rio de Janeiro"], "Advanced": ["Hidden Gems of Rio de Janeiro", "Rio de Janeiro in Three Days: The Essential Itinerary", "Rio de Janeiro in Five Days: The Deep Itinerary", "Day Trip from Rio de Janeiro: Ilha Grande", "Day Trip from Rio de Janeiro: Petrópolis", "Photography and Viewpoints in Rio de Janeiro", "Nightlife and Evenings in Rio de Janeiro", "Festivals and Events Calendar for Rio de Janeiro", "Rio de Janeiro with Kids", "Living Like a Local: The Extended Stay in Rio de Janeiro"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — guide-rio-de-janeiro demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
var gen={version:"jahdb-guide-rio-de-janeiro-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("guide-rio-de-janeiro",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
