(function(){'use strict';
/* JAH The Robotic Personal Assistants Future Technology Database — Signature Edition generator — jahdb-"futuretech-23-robotic-personal-assistants-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT23-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The domestic servant robot in fiction (Signature Edition)",
    "Unimate: robots leave the lab (Signature Edition)",
    "The microwave: automation in the kitchen (Signature Edition)",
    "Dishwashers and washing machines (Signature Edition)",
    "Roomba: the first home robot (Signature Edition)",
    "Robot mops and mowers (Signature Edition)",
    "AIBO: the robot pet (Signature Edition)",
    "ASIMO visits homes (demos) (Signature Edition)",
    "Smart speakers: the voice in the home (Signature Edition)",
    "Robot vacuums get smart (Signature Edition)",
    "Pepper in stores and homes (Signature Edition)",
    "Jibo: the social robot attempt (Signature Edition)"
  ],
  "Compounded": [
    "Misty and developer robots (Signature Edition)",
    "Amazon Astro (Signature Edition)",
    "Samsung Ballie (Signature Edition)",
    "1X NEO for the home (Signature Edition)",
    "Figure 02 home trials (Signature Edition)",
    "Tesla Optimus household demos (Signature Edition)",
    "Assistive robots for disability (Signature Edition)",
    "Hello Robot Stretch: the mobile manipulator (Signature Edition)",
    "The robot that cooks (projection) (Signature Edition)",
    "Laundry, dishes, tidying: the full chore set (Signature Edition)",
    "The eldercare companion (Signature Edition)"
  ],
  "Advanced": [
    "Childcare robots: the debate (Signature Edition)",
    "Affordable home robots (Signature Edition)",
    "Privacy in the robot home (Signature Edition)",
    "The robot butler, perfected (Signature Edition)",
    "Multi-robot households (Signature Edition)",
    "Robots and pets (Signature Edition)",
    "The accessible home (Signature Edition)",
    "Working from home, with help (Signature Edition)",
    "The working robotic assistant (Signature Edition)",
    "The chore-free life (Signature Edition)",
    "What we do with the time (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature robot assistant Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature robot assistant record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature robot assistant record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-23-robotic-personal-assistants-signature",name:"The Robotic Personal Assistants Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-23-robotic-personal-assistants-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-23-robotic-personal-assistants-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
