(function(){'use strict';
/* JAH The Karate Combat Database generator — jahdb-combat-karate-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBK-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Zenkutsu-dachi (Front Stance) - Foundations",
  "Kiba-dachi (Horse Stance) - Foundations",
  "Kamae (Fighting Guard) - Foundations",
  "Choku-zuki (Straight Punch) - Foundations",
  "Kokutsu-dachi (Back Stance) - Foundations",
  "Neko-ashi-dachi (Cat Stance) - Foundations",
  "Age-uke (Rising Block) - Foundations",
  "Soto-uke (Outside Block) - Foundations",
  "Uchi-uke (Inside Block) - Foundations",
  "Gedan-barai (Downward Sweeping Block) - Foundations",
  "Shuto-uchi (Knife-Hand Strike) - Foundations",
  "Mae-geri (Front Kick) - Foundations",
  "Kiai (Spirit Shout) - Foundations",
  "Ibuki (Power Breathing) - Foundations",
  "Gyaku-zuki (Reverse Punch) - Foundations",
  "Oi-zuki (Lunge Punch) - Foundations",
  "Uraken-uchi (Back-Fist Strike) - Foundations",
  "Mawashi-geri (Roundhouse Kick) - Foundations",
  "Yoko-geri (Side Kick) - Foundations",
  "Ura-mawashi-geri (Hook Kick) - Foundations",
  "Ushiro-geri (Back Kick) - Foundations",
  "Hiza-geri (Knee Strike) - Foundations",
  "Shuto-uke (Knife-Hand Block) - Foundations",
  "Morote-uke (Augmented Block) - Foundations",
  "Heian Shodan (First Peaceful Mind Kata) - Foundations",
  "Heian Nidan (Second Peaceful Mind Kata) - Foundations"
 ],
 "Compounded": [

 ],
 "Advanced": [
  "Tekki Shodan (First Iron Horse Kata) - Advanced",
  "Hangetsu (Half Moon Kata) - Advanced",
  "Bunkai (Kata Application Analysis) - Advanced",
  "Kumite (Sparring Method) - Advanced",
  "Tai-sabaki (Body Shifting) - Advanced",
  "Atemi Waza (Vital-Point Striking Principles) - Advanced",
  "Sanchin (Three Battles Kata) - Advanced",
  "Kanku Dai (Viewing the Sky Kata) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Karate Technique Study — "+safe+"\n"
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
    name:topic+' — karate technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A karate technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"karate-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-karate-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-karate',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
