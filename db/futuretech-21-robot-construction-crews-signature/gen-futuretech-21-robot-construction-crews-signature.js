(function(){'use strict';
/* JAH The Robot Construction Crews Future Technology Database — Signature Edition generator — jahdb-"futuretech-21-robot-construction-crews-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT21-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The crane: mechanical muscle (Signature Edition)",
    "Steam shovels dig the modern world (Signature Edition)",
    "The tower crane (Signature Edition)",
    "Prefabrication: building in factories (Signature Edition)",
    "The bricklaying robot concept (Signature Edition)",
    "Shimizu's automated building system (Signature Edition)",
    "Contour crafting: printing buildings (Signature Edition)",
    "D-Shape: large-scale printing (Signature Edition)",
    "MX3D's steel bridge (Signature Edition)",
    "ICON's printed homes (Signature Edition)",
    "Hadrian X: the bricklaying robot (Signature Edition)",
    "SAM: the semi-automated mason (Signature Edition)"
  ],
  "Compounded": [
    "Boston Dynamics Spot on sites (Signature Edition)",
    "Drone surveying standard (Signature Edition)",
    "Exoskeletons on jobsites (Signature Edition)",
    "Autonomous earthmovers (Signature Edition)",
    "Robot rebar tying (Signature Edition)",
    "AI site management (Signature Edition)",
    "Swarm-built pavilions (Signature Edition)",
    "Komatsu Smart Construction (Signature Edition)",
    "PERI's printed buildings in Europe (Signature Edition)",
    "The 24-hour house (projection) (Signature Edition)",
    "Robot crews for skyscrapers (Signature Edition)"
  ],
  "Advanced": [
    "Self-building bridges (Signature Edition)",
    "Lunar construction robots (Signature Edition)",
    "The fully automated jobsite (Signature Edition)",
    "Construction waste eliminated (Signature Edition)",
    "Affordable housing at scale (Signature Edition)",
    "Retrofitting cities by robot (Signature Edition)",
    "The city that builds itself (Signature Edition)",
    "Human-robot construction teams (Signature Edition)",
    "The working robot construction crew (Signature Edition)",
    "Building on Mars (Signature Edition)",
    "The end of the housing crisis (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature construction robot Study \u2014 "+topic+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+", 'src': 'signature'}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\n"
   + "print(summarize(record))\n"
   + "print('Signature-generated variant \u2014 not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 Signature construction robot record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature construction robot record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Signature-generated variant \u2014 not an archive record. Seeded archive records are the authoritative entries.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-21-robot-construction-crews-signature",name:"The Robot Construction Crews Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-21-robot-construction-crews-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-21-robot-construction-crews-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
