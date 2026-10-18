(function(){'use strict';
/* JAH The Secret Code Club Database generator — jahdb-db-secret-code-club-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSCC-";
var FIELDS=["Missions 1-6","Missions 7-12","Master Missions"];
var TOPICS={
 "Missions 1-6": [
  "Mission 1: The Caesar Shift \u2014 Missions 1-6",
  "Mission 1: The Caesar Shift \u2014 Deep Dive \u2014 Missions 1-6",
  "Mission 2: The Atbash Mirror \u2014 Missions 1-6",
  "Mission 2: The Atbash Mirror \u2014 Deep Dive \u2014 Missions 1-6",
  "Mission 3: The Pigpen Grid \u2014 Missions 1-6",
  "Mission 3: The Pigpen Grid \u2014 Deep Dive \u2014 Missions 1-6",
  "Mission 4: The Morse Tap \u2014 Missions 1-6",
  "Mission 4: The Morse Tap \u2014 Deep Dive \u2014 Missions 1-6",
  "Mission 5: The Scytale Staff \u2014 Missions 1-6",
  "Mission 5: The Scytale Staff \u2014 Deep Dive \u2014 Missions 1-6",
  "Mission 6: The Rail Fence \u2014 Missions 1-6",
  "Mission 6: The Rail Fence \u2014 Deep Dive \u2014 Missions 1-6"
 ],
 "Missions 7-12": [
  "Mission 7: The Vigenere Key \u2014 Missions 7-12",
  "Mission 7: The Vigenere Key \u2014 Deep Dive \u2014 Missions 7-12",
  "Mission 8: The Playfair Square \u2014 Missions 7-12",
  "Mission 8: The Playfair Square \u2014 Deep Dive \u2014 Missions 7-12",
  "Mission 9: The Book Cipher \u2014 Missions 7-12",
  "Mission 9: The Book Cipher \u2014 Deep Dive \u2014 Missions 7-12",
  "Mission 10: The Rotor Machine \u2014 Missions 7-12",
  "Mission 10: The Rotor Machine \u2014 Deep Dive \u2014 Missions 7-12",
  "Mission 11: The Acrostic Verse \u2014 Missions 7-12",
  "Mission 11: The Acrostic Verse \u2014 Deep Dive \u2014 Missions 7-12",
  "Mission 12: The Invisible Ink \u2014 Missions 7-12",
  "Mission 12: The Invisible Ink \u2014 Deep Dive \u2014 Missions 7-12"
 ],
 "Master Missions": [
  "Mission 13: The Frequency Masterclass \u2014 Master Missions",
  "Mission 13: The Frequency Masterclass \u2014 Deep Dive \u2014 Master Missions",
  "Mission 14: The One-Time Pad \u2014 Master Missions",
  "Mission 14: The One-Time Pad \u2014 Deep Dive \u2014 Master Missions",
  "Mission 15: The Public Key \u2014 Master Missions",
  "Mission 15: The Public Key \u2014 Deep Dive \u2014 Master Missions",
  "Mission 16: The Layered Drop \u2014 Master Missions",
  "Mission 16: The Layered Drop \u2014 Deep Dive \u2014 Master Missions",
  "Mission 17: Graduation Day \u2014 Master Missions",
  "Mission 17: Graduation Day \u2014 Deep Dive \u2014 Master Missions"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Codebreaking Study — "+safe+"\n"
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
    name:topic+' — codebreaking mission record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A codebreaking mission record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-secret-code-club-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-secret-code-club',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
