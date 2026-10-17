(function(){'use strict';
/* JAH Japanese Jiu-Jitsu Combat Database generator — jahdb-combat-japanese-jiu-jitsu-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBJJJ-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Shisei: The Ready Stances of Jujutsu - Foundations",
  "Maai: Distance and Timing in Jujutsu - Foundations",
  "Mushin and Zanshin: Mind States of the Fighter - Foundations",
  "Kumiuchi: Classical Grappling Engagement - Foundations",
  "Ukemi on Hard Ground: Jujutsu Falling Principles - Foundations",
  "Taihenjutsu: Rolling and Body Changing - Foundations",
  "Kyusho: The Vital-Point Map of the Body - Foundations",
  "Tehodoki: Wrist-Grab Releases - Foundations",
  "Ryote Mochi Hazushi: Two-Hand Grab Escape - Foundations"
 ],
 "Compounded": [
  "Kata Mochi Hazushi: Lapel-Grab Defense - Compounded",
  "Empi Uchi: Elbow Strikes in the Clinch - Compounded",
  "Shotei Uchi: Palm-Heel Strikes - Compounded",
  "Ude Garami: The Entangled Armlock - Compounded",
  "Kote Gaeshi: The Wrist-Turn Throw - Compounded",
  "Waki Gatame: The Armpit Armlock - Compounded",
  "Hiji Kannuki: The Elbow Bolt Lock - Compounded",
  "Ashi Garami: The Leg-Entanglement Lock - Compounded",
  "Kubi Nage: The Neck Throw - Compounded",
  "Tani Otoshi: The Valley Drop - Compounded",
  "Yama Arashi: The Mountain Storm Throw - Compounded",
  "Kata Gatame: The Shoulder Hold - Compounded",
  "Yoko Shiho Gatame: Side Four-Quarter Hold - Compounded",
  "Tate Shiho Gatame: Mounted Four-Quarter Hold - Compounded",
  "Okuri Eri Jime: The Sliding Lapel Strangle - Compounded",
  "Kata Ha Jime: Single-Wing Strangle - Compounded"
 ],
 "Advanced": [
  "Gyaku Juji Jime: Reverse Cross Strangle - Advanced",
  "Hadaka Jime: The Naked Strangle - Advanced",
  "Sumi Otoshi: The Corner Drop - Advanced",
  "Uki Otoshi: The Floating Drop - Advanced",
  "Tomoe Nage: The Stomach Circle Throw - Advanced",
  "Ushiro Ryote Mochi: Rear Two-Hand Grab Defense - Advanced",
  "Kaeshi Waza: Counter Techniques - Advanced",
  "Renraku Waza: Combination Attacks - Advanced",
  "Muto Dori: Unarmed Defense Against the Sword - Advanced"
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
var gen={version:'jahdb-combat-japanese-jiu-jitsu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-japanese-jiu-jitsu',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
