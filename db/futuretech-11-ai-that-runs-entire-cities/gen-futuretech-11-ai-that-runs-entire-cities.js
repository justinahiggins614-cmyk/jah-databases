(function(){'use strict';
/* JAH The AI That Runs Entire Cities Future Technology Database generator — jahdb-"futuretech-11-ai-that-runs-entire-cities"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT11-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The first electric traffic signal",
    "Computerized traffic control: Toronto",
    "SCATS and adaptive signal control",
    "Power grids get supervisory control",
    "GIS: cities mapped as data",
    "Smart meters and the smart grid",
    "Songdo: the built-from-scratch smart city",
    "Rio's Operations Center",
    "Waze and crowdsourced traffic",
    "Predictive policing experiments",
    "Sidewalk Labs' Quayside proposal",
    "AI traffic prediction at scale"
  ],
  "Compounded": [
    "Digital twins of cities",
    "AI dispatch for emergency services",
    "Smart water and waste networks",
    "Smart street lighting at city scale",
    "Autonomous public transit pilots",
    "City-scale energy orchestration",
    "AI urban planners",
    "Integrated city operating systems",
    "Algorithmic congestion pricing",
    "Self-optimizing traffic grids",
    "Predictive infrastructure maintenance"
  ],
  "Advanced": [
    "AI emergency managers",
    "The sentient intersection",
    "City AI and democratic oversight",
    "Climate-adaptive cities",
    "The 15-minute AI city",
    "Multi-city coordination",
    "Failure drills: when the city AI goes down",
    "Autonomous construction meets city AI",
    "The working city AI",
    "Cities that run themselves",
    "Planetary urban coordination"
  ]
};
function demoProgram(topic,field,seed){
  return "# AI That Runs Entire Cities Study \u2014 "+topic+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\n"
   + "print(summarize(record))\n"
   + "print('Generated variant \u2014 not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 city AI record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A city AI record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Generated variant \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Generated variant demo.'},
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-11-ai-that-runs-entire-cities",name:"The AI That Runs Entire Cities Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-11-ai-that-runs-entire-cities"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-11-ai-that-runs-entire-cities",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
