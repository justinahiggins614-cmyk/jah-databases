(function(){'use strict';
/* JAH The Taekwondo Combat Database generator — jahdb-combat-taekwondo-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBTKD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Taekwondo Is: The Way of Foot and Hand - Foundations",
  "Attention Stance and the Bow (Charyeot Seogi, Kyeong Rye) - Foundations",
  "Ready Stance (Junbi Seogi) - Foundations",
  "Front Stance (Ap Seogi / Ap Kubi Seogi) - Foundations",
  "Back Stance (Dwit Kubi Seogi) - Foundations",
  "Horse Riding Stance (Juchum Seogi) - Foundations",
  "Breathing and the Ki Hap Shout - Foundations",
  "Straight Punch (Jireugi) - Foundations",
  "Knife-Hand Strike (Sonkal Taerigi) - Foundations",
  "The Three Basic Blocks (Arae, Momtong, Olgul Maki) - Foundations",
  "Front Snap Kick (Ap Chagi) - Foundations"
 ],
 "Compounded": [
  "Roundhouse Kick (Dollyeo Chagi) - Compounded",
  "Side Kick (Yeop Chagi) - Compounded",
  "Back Kick (Dwit Chagi) - Compounded",
  "Axe Kick (Naeryeo Chagi) - Compounded",
  "Push Kick (Mireo Chagi) - Compounded",
  "Crescent Kicks (An Chagi and Bakkat Chagi) - Compounded",
  "Hook Kick (Huryeo Chagi) - Compounded",
  "Footwork: Stepping, Sliding, and Pivoting - Compounded",
  "Kick Combinations - Compounded",
  "Taegeuk Poomsae: The Eight Color-Belt Forms - Compounded",
  "Chon-Ji Tul: The First ITF Pattern - Compounded",
  "Sparring Fundamentals (Gyeorugi) - Compounded"
 ],
 "Advanced": [
  "Tornado Kick (Dolgae Chagi) - Advanced",
  "Spinning Hook Kick (Dwi Huryeo Chagi) - Advanced",
  "Jumping Kicks (Twio Chagi) - Advanced",
  "Double and Multiple Kicks - Advanced",
  "Koryo Poomsae and the Black Belt Forms - Advanced",
  "Dan-Gun Tul and the Higher ITF Patterns - Advanced",
  "Counter Techniques - Advanced",
  "Match Strategy, Timing, and Distance - Advanced",
  "Self-Defense Applications (Hosin Sul) - Advanced",
  "Breaking (Gyeokpa) - Advanced",
  "The Mastery Path: Belts, Testing, and Teaching - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Taekwondo Combat Study — "+safe+"\n"
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
    demo:{kind:"taekwondo-combat",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-taekwondo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-taekwondo',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
