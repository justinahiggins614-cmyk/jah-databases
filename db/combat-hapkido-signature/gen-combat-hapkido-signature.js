(function(){'use strict';
/* JAH Hapkido Combat Signature Database generator — jahdb-combat-hapkido-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBHAPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Stances: The Foundation Postures (Seogi) (Signature Edition) - Foundations",
  "Breakfalls: Falling Safely (Nakbeop) (Signature Edition) - Foundations",
  "Footwork and Stepping (Balgeoreum) (Signature Edition) - Foundations",
  "Straight Punch (Jireugi) (Signature Edition) - Foundations",
  "Front Kick (Ap Chagi) (Signature Edition) - Foundations",
  "Roundhouse Kick (Dollyeo Chagi) (Signature Edition) - Foundations",
  "Basic Blocks (Makgi) (Signature Edition) - Foundations",
  "The Circular Motion Principle (Wonui) (Signature Edition) - Foundations",
  "Abdominal Breathing (Danjeon Hoheup) (Signature Edition) - Foundations",
  "The Principle of Softness (Yu) (Signature Edition) - Foundations",
  "Wrist Escape (Sonmok Geodeureo) (Signature Edition) - Foundations",
  "Basic Wrist Lock (Sonmok Kkokki) (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Elbow Lock (Palkkumchi Kkokki) (Signature Edition) - Compounded",
  "Side Kick (Yeop Chagi) (Signature Edition) - Compounded",
  "Finger Locks (Songarak Kkokki) (Signature Edition) - Compounded",
  "Knife-Hand Strike (Sudo Chigi) (Signature Edition) - Compounded",
  "Shoulder Lock (Eokkae Kkokki) (Signature Edition) - Compounded",
  "Back Kick (Dwi Chagi) (Signature Edition) - Compounded",
  "Leg Sweep (Balgeolgi) (Signature Edition) - Compounded",
  "Lapel Grab Defense (Otdong Japgi) (Signature Edition) - Compounded",
  "Shoulder Throw (Eokkae Mechi) (Signature Edition) - Compounded",
  "Hip Throw (Heori Mechi) (Signature Edition) - Compounded",
  "Elbow Strike (Palkkumchi Chigi) (Signature Edition) - Compounded",
  "Knee Strike (Mureup Chagi) (Signature Edition) - Compounded",
  "Leg Hook Takedown (Dari Geolgo) (Signature Edition) - Compounded",
  "Front Choke Defense (Mok Joreugi) (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Pressure Point Strikes (Gyeonghyeol Chigi) (Signature Edition) - Advanced",
  "Spinning Back Kick (Dwi Dollyeo Chagi) (Signature Edition) - Advanced",
  "Jump Front Kick (Twieo Ap Chagi) (Signature Edition) - Advanced",
  "Knife Defense (Dando Daebi) (Signature Edition) - Advanced",
  "Long Staff Defense (Jangbong Daebi) (Signature Edition) - Advanced",
  "Short Stick Techniques (Danbong Sul) (Signature Edition) - Advanced",
  "Sword Basics (Geom Sul) (Signature Edition) - Advanced",
  "Breaking (Gyeokpa) (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hapkido Technique Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hapkido-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-hapkido-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-hapkido-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
