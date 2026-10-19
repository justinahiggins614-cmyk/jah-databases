(function(){'use strict';
/* JAH The The Humanoid Robot Boom Future Technology Database — Signature Edition generator — jahdb-"futuretech-16-the-humanoid-robot-boom-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT16-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Automata: the dream of the mechanical human (Signature Edition)",
    "Unimate: the first industrial robot (Signature Edition)",
    "WABOT-1: the first full-scale humanoid (Signature Edition)",
    "Honda P2 and the walking breakthrough (Signature Edition)",
    "ASIMO: the public face of humanoids (Signature Edition)",
    "Sony QRIO and the entertainment humanoid (Signature Edition)",
    "RoboCup: the 2050 goal (Signature Edition)",
    "DARPA Robotics Challenge (Signature Edition)",
    "Boston Dynamics Atlas: the athlete (Signature Edition)",
    "Nao and Pepper: social humanoids (Signature Edition)",
    "Tesla Bot / Optimus announced (Signature Edition)",
    "Figure 01 and the startup wave (Signature Edition)"
  ],
  "Compounded": [
    "Agility Digit in warehouses (Signature Edition)",
    "1X NEO: the home humanoid (Signature Edition)",
    "Humanoid pilots multiply (Signature Edition)",
    "The $20,000 humanoid (projection) (Signature Edition)",
    "Humanoids in eldercare (Signature Edition)",
    "The humanoid construction worker (Signature Edition)",
    "Humanoid dexterity: the hand problem (Signature Edition)",
    "Battery and power limits (Signature Edition)",
    "Safety certification for humanoids (Signature Edition)",
    "The humanoid in every warehouse (Signature Edition)",
    "Humanoids in the home, mainstream (Signature Edition)"
  ],
  "Advanced": [
    "Humanoid teleoperation at scale (Signature Edition)",
    "Open-source humanoids (Signature Edition)",
    "Humanoids in disaster zones (Signature Edition)",
    "The uncanny workforce (Signature Edition)",
    "Humanoid sports and culture (Signature Edition)",
    "Military humanoids: the question (Signature Edition)",
    "General-purpose: one robot, any job (Signature Edition)",
    "The working humanoid boom (Signature Edition)",
    "A billion humanoids (Signature Edition)",
    "Humans and humanoids: the new normal (Signature Edition)",
    "The humanoid century (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature humanoid robot Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature humanoid robot record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature humanoid robot record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-16-the-humanoid-robot-boom-signature",name:"The The Humanoid Robot Boom Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-16-the-humanoid-robot-boom-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-16-the-humanoid-robot-boom-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
