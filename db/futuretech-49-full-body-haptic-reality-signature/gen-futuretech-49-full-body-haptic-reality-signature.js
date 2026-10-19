(function(){'use strict';
/* JAH The Full-Body Haptic Reality Future Technology Database — Signature Edition generator — jahdb-"futuretech-49-full-body-haptic-reality-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT49-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Touch: the first sense (Signature Edition)",
    "Braille (Signature Edition)",
    "The telephone's vibration (Signature Edition)",
    "Force feedback: the first joysticks (Signature Edition)",
    "The Phantom haptic device (Signature Edition)",
    "Rumble packs (Signature Edition)",
    "DualShock (Signature Edition)",
    "Touchscreens: the haptic display (Signature Edition)",
    "HD haptics: Switch (Signature Edition)",
    "Tactile internet concepts (Signature Edition)",
    "Ultrasonic mid-air haptics (Signature Edition)",
    "Teslasuit (Signature Edition)"
  ],
  "Compounded": [
    "bHaptics TactSuit (Signature Edition)",
    "Haptic Gloves in Full-Body Virtual Reality (Signature Edition)",
    "Temperature haptics (Signature Edition)",
    "Exoskeleton force feedback (Signature Edition)",
    "Pin displays: Braille terminals (Signature Edition)",
    "The Novint Falcon (Signature Edition)",
    "Force-feedback steering wheels (Signature Edition)",
    "Surgical haptics: da Vinci (Signature Edition)",
    "The cutaneous rabbit illusion (Signature Edition)",
    "Haptic navigation belts (Signature Edition)",
    "The Hug Shirt (Signature Edition)"
  ],
  "Advanced": [
    "Tactile graphics (Signature Edition)",
    "Haptic gloves for surgery (Signature Edition)",
    "Haptic teleoperation for space (Signature Edition)",
    "Haptic holograms (Signature Edition)",
    "Haptic seatbelts and suits for drivers (Signature Edition)",
    "Neural haptics (projection) (Signature Edition)",
    "The full-body standard (Signature Edition)",
    "Haptics for the blind (Signature Edition)",
    "Remote touch: the handshake (Signature Edition)",
    "The working haptic reality (Signature Edition)",
    "The felt world (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature haptic reality Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature haptic reality record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature haptic reality record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-49-full-body-haptic-reality-signature",name:"The Full-Body Haptic Reality Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-49-full-body-haptic-reality-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-49-full-body-haptic-reality-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
