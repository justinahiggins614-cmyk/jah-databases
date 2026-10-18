(function(){'use strict';
/* JAH The Humanlike Androids Future Technology Database generator — jahdb-"futuretech-17-humanlike-androids"-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT17-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Vaucanson's androids",
    "Jaquet-Droz's writing boy",
    "The Turk: the fake android",
    "Capek coins 'robot'",
    "Metropolis: the machine human",
    "Asimov's robot stories",
    "Disney animatronics",
    "The uncanny valley",
    "Star Wars droids",
    "Blade Runner's replicants",
    "Ishiguro's Geminoid",
    "Actroid and Repliee"
  ],
  "Compounded": [
    "Sophia the robot citizen",
    "Ameca: expressive android",
    "Nadine: the professor android",
    "Android newscasters",
    "Figure 02 and lifelike workers",
    "Tesla Optimus Gen 2 hands",
    "Android actors and performers",
    "Synthetic skin and touch",
    "The companion android (projection)",
    "Androids in customer service",
    "The identity question"
  ],
  "Advanced": [
    "Android rights debates",
    "Deception and disclosure",
    "Androids and intimacy",
    "The workplace android",
    "Child-facing androids",
    "The indistinguishable android (projection)",
    "Android maintenance and repair",
    "Cultural androids: every face",
    "The working humanlike android",
    "Androids and the meaning of human",
    "Living with androids"
  ]
};
function demoProgram(topic,field,seed){
  return "# Humanlike Androids Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 humanlike android record (generated variant)',
    title:topic,
    description:'GENERATED VARIANT (boundless generator). A humanlike android record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-17-humanlike-androids",name:"The Humanlike Androids Future Technology Database"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-17-humanlike-androids"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-17-humanlike-androids",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
