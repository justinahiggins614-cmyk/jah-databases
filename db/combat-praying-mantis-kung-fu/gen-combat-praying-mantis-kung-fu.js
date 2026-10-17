(function(){'use strict';
/* JAH Praying Mantis Kung Fu Combat Database generator — jahdb-combat-praying-mantis-kung-fu-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBPM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Mantis Salute (Tang Lang Quan Li)",
  "Mantis Hook Hand (Tang Lang Gou)",
  "The Relaxed Mantis Claw (Song Zhao)",
  "Horse Stance in the Mantis Method (Ma Bu)",
  "Bow Stance (Gong Bu)",
  "Empty Stance (Xu Bu)",
  "Golden Rooster Stands on One Leg (Jin Ji Du Li)",
  "Straight Punch (Chong Quan)",
  "Rolling Fist (Gun Quan)",
  "Mantis Palm Strike (Tui Zhang)",
  "Front Kick (Ti Tui)",
  "Side Kick (Ce Ti Tui)"
 ],
 "Compounded": [
  "Double Hook Hands (Shuang Tang Lang Gou)",
  "The Pluck (Zhai)",
  "Mantis Catches the Cicada (Tang Lang Bu Chan)",
  "Sticky Hands (Zhan Shou)",
  "Seizing and Joint Control (Qin Na)",
  "Seven Star Footwork (Qi Xing Bu)",
  "Monkey Steps (Hou Bu)",
  "The Swift Entry Drill (Jin Bu Lian Xi)",
  "Beng Bu (Crushing Step) - the First Form",
  "Lan Jie (Intercepting) - the Second Form",
  "Ba Zhou (Eight Elbows) - the Third Form",
  "Fan Che (Wheel Cart Fist) - the Fourth Form",
  "Zhai Yao (Abstraction) - the Fifth Form",
  "White Ape Steals the Peach (Bai Yuan Tou Tao)"
 ],
 "Advanced": [
  "The Eight Rigid and Twelve Flexible (Ba Gang Shi Er Rou)",
  "The Fourteen Seven-Star Strikes",
  "The Mantis Beak Peck (Zhuo)",
  "Mantis Sparring Method (San Da)",
  "Iron Body Conditioning (Tie Bu Shan)",
  "Hardening the Hook Hands (Pai Da)",
  "Flying and Sweeping Kicks (Teng Kong Tui Fa)",
  "From Form to Fight: The Mantis Path"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Praying Mantis Kung Fu Study — "+safe+"\n"
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
    demo:{kind:"praying-mantis-kung-fu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-praying-mantis-kung-fu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-praying-mantis-kung-fu',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
