(function(){'use strict';
/* JAH Japanese Jiu-Jitsu Combat Signature Database generator — jahdb-combat-japanese-jiu-jitsu-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBJJJS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Shisei: The Ready Stances of Jujutsu (Signature Edition) - Foundations",
  "Maai: Distance and Timing in Jujutsu (Signature Edition) - Foundations",
  "Mushin and Zanshin: Mind States of the Fighter (Signature Edition) - Foundations",
  "Kumiuchi: Classical Grappling Engagement (Signature Edition) - Foundations",
  "Ukemi on Hard Ground: Jujutsu Falling Principles (Signature Edition) - Foundations",
  "Taihenjutsu: Rolling and Body Changing (Signature Edition) - Foundations",
  "Kyusho: The Vital-Point Map of the Body (Signature Edition) - Foundations",
  "Tehodoki: Wrist-Grab Releases (Signature Edition) - Foundations",
  "Ryote Mochi Hazushi: Two-Hand Grab Escape (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Kata Mochi Hazushi: Lapel-Grab Defense (Signature Edition) - Compounded",
  "Empi Uchi: Elbow Strikes in the Clinch (Signature Edition) - Compounded",
  "Shotei Uchi: Palm-Heel Strikes (Signature Edition) - Compounded",
  "Ude Garami: The Entangled Armlock (Signature Edition) - Compounded",
  "Kote Gaeshi: The Wrist-Turn Throw (Signature Edition) - Compounded",
  "Waki Gatame: The Armpit Armlock (Signature Edition) - Compounded",
  "Hiji Kannuki: The Elbow Bolt Lock (Signature Edition) - Compounded",
  "Ashi Garami: The Leg-Entanglement Lock (Signature Edition) - Compounded",
  "Kubi Nage: The Neck Throw (Signature Edition) - Compounded",
  "Tani Otoshi: The Valley Drop (Signature Edition) - Compounded",
  "Yama Arashi: The Mountain Storm Throw (Signature Edition) - Compounded",
  "Kata Gatame: The Shoulder Hold (Signature Edition) - Compounded",
  "Yoko Shiho Gatame: Side Four-Quarter Hold (Signature Edition) - Compounded",
  "Tate Shiho Gatame: Mounted Four-Quarter Hold (Signature Edition) - Compounded",
  "Okuri Eri Jime: The Sliding Lapel Strangle (Signature Edition) - Compounded",
  "Kata Ha Jime: Single-Wing Strangle (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Gyaku Juji Jime: Reverse Cross Strangle (Signature Edition) - Advanced",
  "Hadaka Jime: The Naked Strangle (Signature Edition) - Advanced",
  "Sumi Otoshi: The Corner Drop (Signature Edition) - Advanced",
  "Uki Otoshi: The Floating Drop (Signature Edition) - Advanced",
  "Tomoe Nage: The Stomach Circle Throw (Signature Edition) - Advanced",
  "Ushiro Ryote Mochi: Rear Two-Hand Grab Defense (Signature Edition) - Advanced",
  "Kaeshi Waza: Counter Techniques (Signature Edition) - Advanced",
  "Renraku Waza: Combination Attacks (Signature Edition) - Advanced",
  "Muto Dori: Unarmed Defense Against the Sword (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Japanese Jiu Jitsu Study — "+safe+"\n"
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
    demo:{kind:"japanese-jiu-jitsu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-japanese-jiu-jitsu-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-japanese-jiu-jitsu-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
