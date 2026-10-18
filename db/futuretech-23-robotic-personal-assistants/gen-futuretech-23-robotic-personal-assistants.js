(function(){'use strict';
/* JAH The Robotic Personal Assistants Future Technology Database generator — jahdb-"futuretech-23-robotic-personal-assistants"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT23-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The domestic servant robot in fiction",
    "Unimate: robots leave the lab",
    "The microwave: automation in the kitchen",
    "Dishwashers and washing machines",
    "Roomba: the first home robot",
    "Robot mops and mowers",
    "AIBO: the robot pet",
    "ASIMO visits homes (demos)",
    "Smart speakers: the voice in the home",
    "Robot vacuums get smart",
    "Pepper in stores and homes",
    "Jibo: the social robot attempt"
  ],
  "Compounded": [
    "Misty and developer robots",
    "Amazon Astro",
    "Samsung Ballie",
    "1X NEO for the home",
    "Figure 02 home trials",
    "Tesla Optimus household demos",
    "Assistive robots for disability",
    "Hello Robot Stretch: the mobile manipulator",
    "The robot that cooks (projection)",
    "Laundry, dishes, tidying: the full chore set",
    "The eldercare companion"
  ],
  "Advanced": [
    "Childcare robots: the debate",
    "Affordable home robots",
    "Privacy in the robot home",
    "The robot butler, perfected",
    "Multi-robot households",
    "Robots and pets",
    "The accessible home",
    "Working from home, with help",
    "The working robotic assistant",
    "The chore-free life",
    "What we do with the time"
  ]
};
function demoProgram(topic,field,seed){
  return "# Robotic Personal Assistants Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 robot assistant record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A robot assistant record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-23-robotic-personal-assistants",name:"The Robotic Personal Assistants Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-23-robotic-personal-assistants"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-23-robotic-personal-assistants",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
