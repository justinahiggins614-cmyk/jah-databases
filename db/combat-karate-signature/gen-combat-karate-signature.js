(function(){'use strict';
/* JAH The Karate Combat Signature Database generator — jahdb-combat-karate-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBKS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Zenkutsu-dachi (Front Stance) (Signature Edition) - Foundations",
  "Kiba-dachi (Horse Stance) (Signature Edition) - Foundations",
  "Kamae (Fighting Guard) (Signature Edition) - Foundations",
  "Choku-zuki (Straight Punch) (Signature Edition) - Foundations",
  "Kokutsu-dachi (Back Stance) (Signature Edition) - Foundations",
  "Neko-ashi-dachi (Cat Stance) (Signature Edition) - Foundations",
  "Age-uke (Rising Block) (Signature Edition) - Foundations",
  "Soto-uke (Outside Block) (Signature Edition) - Foundations",
  "Uchi-uke (Inside Block) (Signature Edition) - Foundations",
  "Gedan-barai (Downward Sweeping Block) (Signature Edition) - Foundations",
  "Shuto-uchi (Knife-Hand Strike) (Signature Edition) - Foundations",
  "Mae-geri (Front Kick) (Signature Edition) - Foundations",
  "Kiai (Spirit Shout) (Signature Edition) - Foundations",
  "Ibuki (Power Breathing) (Signature Edition) - Foundations",
  "Gyaku-zuki (Reverse Punch) (Signature Edition) - Foundations",
  "Oi-zuki (Lunge Punch) (Signature Edition) - Foundations",
  "Uraken-uchi (Back-Fist Strike) (Signature Edition) - Foundations",
  "Mawashi-geri (Roundhouse Kick) (Signature Edition) - Foundations",
  "Yoko-geri (Side Kick) (Signature Edition) - Foundations",
  "Ura-mawashi-geri (Hook Kick) (Signature Edition) - Foundations",
  "Ushiro-geri (Back Kick) (Signature Edition) - Foundations",
  "Hiza-geri (Knee Strike) (Signature Edition) - Foundations",
  "Shuto-uke (Knife-Hand Block) (Signature Edition) - Foundations",
  "Morote-uke (Augmented Block) (Signature Edition) - Foundations",
  "Heian Shodan (First Peaceful Mind Kata) (Signature Edition) - Foundations",
  "Heian Nidan (Second Peaceful Mind Kata) (Signature Edition) - Foundations"
 ],
 "Compounded": [

 ],
 "Advanced": [
  "Tekki Shodan (First Iron Horse Kata) (Signature Edition) - Advanced",
  "Hangetsu (Half Moon Kata) (Signature Edition) - Advanced",
  "Bunkai (Kata Application Analysis) (Signature Edition) - Advanced",
  "Kumite (Sparring Method) (Signature Edition) - Advanced",
  "Tai-sabaki (Body Shifting) (Signature Edition) - Advanced",
  "Atemi Waza (Vital-Point Striking Principles) (Signature Edition) - Advanced",
  "Sanchin (Three Battles Kata) (Signature Edition) - Advanced",
  "Kanku Dai (Viewing the Sky Kata) (Signature Edition) - Advanced"
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
var gen={version:'jahdb-combat-karate-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-karate-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
