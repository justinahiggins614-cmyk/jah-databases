(function(){'use strict';
/* JAH The Muay Thai Combat Database generator — jahdb-combat-muay-thai-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBMT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Muay Thai Fighting Stance - Foundations",
  "Muay Thai Footwork Basics - Foundations",
  "The Muay Thai High Guard - Foundations",
  "The Jab (Mat Trong) - Foundations",
  "Parry and Slip Defense in Muay Thai - Foundations",
  "Shadowboxing (Lom Muay) - Foundations",
  "The Cross (Mat Wiang San) - Foundations",
  "Roundhouse Kick Mechanics (Tae Tad) - Foundations",
  "The Teep Front Push Kick (Thip Trong) - Foundations",
  "Checking Kicks (Bang) - Foundations",
  "Heavy Bag Training for Muay Thai - Foundations",
  "Shin and Core Conditioning Basics - Foundations"
 ],
 "Compounded": [
  "The Hook Punch (Mat Wiang Kwat) - Compounded",
  "The Uppercut (Mat Soi Dao) - Compounded",
  "Horizontal Elbow Strike (Sok Tad) - Compounded",
  "Straight Knee Strike (Khao Trong) - Compounded",
  "Upward and Diagonal Elbow Strikes (Sok Ngat and Sok Chieng) - Compounded",
  "Curved Knee Strike (Khao Kong) - Compounded",
  "Clinch Entry and Inside Position (Chap Kho) - Compounded",
  "The Low Cut Kick (Tae Kod) - Compounded",
  "The Switch Kick (Tae Salap) - Compounded",
  "Clinch Control: Pummeling and Hip Position - Compounded",
  "Catching Kicks and Basic Dumps (Jap Kha) - Compounded",
  "Defensive Shell and Counter Basics - Compounded"
 ],
 "Advanced": [
  "Spinning Elbow (Sok Klap) - Advanced",
  "Flying Knee (Khao Loi) - Advanced",
  "Spinning Heel Kick (Tae Klap) - Advanced",
  "Elbow-Range Fighting in the Pocket - Advanced",
  "Clinch Throws (Thum) - Advanced",
  "Sweeping the Supporting Leg (Tad Kha) - Advanced",
  "Counter-Fighting: Timing and Interception - Advanced",
  "Combination Systems: Multi-Strike Flow - Advanced",
  "Ringcraft: Ring Control and Angles - Advanced",
  "Full Fight Camp Conditioning - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Muay Thai Study — "+safe+"\n"
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
    demo:{kind:"muay-thai-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-muay-thai-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-muay-thai',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
