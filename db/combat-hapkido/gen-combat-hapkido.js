(function(){'use strict';
/* JAH Hapkido Combat Database generator — jahdb-combat-hapkido-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBHAP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Stances: The Foundation Postures (Seogi) - Foundations",
  "Breakfalls: Falling Safely (Nakbeop) - Foundations",
  "Footwork and Stepping (Balgeoreum) - Foundations",
  "Straight Punch (Jireugi) - Foundations",
  "Front Kick (Ap Chagi) - Foundations",
  "Roundhouse Kick (Dollyeo Chagi) - Foundations",
  "Basic Blocks (Makgi) - Foundations",
  "The Circular Motion Principle (Wonui) - Foundations",
  "Abdominal Breathing (Danjeon Hoheup) - Foundations",
  "The Principle of Softness (Yu) - Foundations",
  "Wrist Escape (Sonmok Geodeureo) - Foundations",
  "Basic Wrist Lock (Sonmok Kkokki) - Foundations"
 ],
 "Compounded": [
  "Elbow Lock (Palkkumchi Kkokki) - Compounded",
  "Side Kick (Yeop Chagi) - Compounded",
  "Finger Locks (Songarak Kkokki) - Compounded",
  "Knife-Hand Strike (Sudo Chigi) - Compounded",
  "Shoulder Lock (Eokkae Kkokki) - Compounded",
  "Back Kick (Dwi Chagi) - Compounded",
  "Leg Sweep (Balgeolgi) - Compounded",
  "Lapel Grab Defense (Otdong Japgi) - Compounded",
  "Shoulder Throw (Eokkae Mechi) - Compounded",
  "Hip Throw (Heori Mechi) - Compounded",
  "Elbow Strike (Palkkumchi Chigi) - Compounded",
  "Knee Strike (Mureup Chagi) - Compounded",
  "Leg Hook Takedown (Dari Geolgo) - Compounded",
  "Front Choke Defense (Mok Joreugi) - Compounded"
 ],
 "Advanced": [
  "Pressure Point Strikes (Gyeonghyeol Chigi) - Advanced",
  "Spinning Back Kick (Dwi Dollyeo Chagi) - Advanced",
  "Jump Front Kick (Twieo Ap Chagi) - Advanced",
  "Knife Defense (Dando Daebi) - Advanced",
  "Long Staff Defense (Jangbong Daebi) - Advanced",
  "Short Stick Techniques (Danbong Sul) - Advanced",
  "Sword Basics (Geom Sul) - Advanced",
  "Breaking (Gyeokpa) - Advanced"
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
var gen={version:'jahdb-combat-hapkido-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-hapkido',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
