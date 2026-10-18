(function(){'use strict';
/* JAH The Codebreaker Challenge Signature Database generator — jahdb-db-codebreaker-challenge-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CODCHAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Codebreaker: Caesar shift 3 (THE EAGLE HAS LANDED)",
  "Codebreaker: Caesar shift 3 (MEET AT DAWN)",
  "Codebreaker: Caesar shift 5 (ATTACK AT SUNRISE)",
  "Codebreaker: Caesar shift 1 (HELLO WORLD)",
  "Codebreaker: Caesar shift 7 (THE QUICK BROWN FOX)",
  "Codebreaker: Caesar shift 3 (SECRETS HIDE IN PLAI)",
  "Codebreaker: Caesar shift 10 (CODEBREAKERS NEVER Q)",
  "Codebreaker: Caesar shift 13 (ROT THIRTEEN HIDES N)",
  "Codebreaker: Caesar shift 4 (PATIENCE BREAKS CODE)",
  "Codebreaker: Caesar shift 8 (EVERY LETTER COUNTS)",
  "Codebreaker: Caesar shift 2 (SMALL STEPS WIN)"
 ],
 "Compounded": [
  "Codebreaker: Caesar shift 19 (THE LONG WAY ROUND)",
  "Codebreaker: Caesar shift 23 (ALMOST HOME FREE)",
  "Codebreaker: Atbash mirror (THE MIRROR CODE)",
  "Codebreaker: Atbash mirror (BACKWARDS ALPHABET)",
  "Codebreaker: Atbash mirror (ANCIENT AND ELEGANT)",
  "Codebreaker: Vigenere key KEY",
  "Codebreaker: Vigenere key CODE",
  "Codebreaker: mirror writing",
  "Codebreaker: Caesar shift 15 (FIFTEEN SHIFTS DEEP)",
  "Codebreaker: Caesar shift 17 (SEVENTEEN STEPS)",
  "Codebreaker: Caesar shift 21 (TWENTY ONE GUNS)",
  "Codebreaker: Atbash mirror (THE MIRROR HAS TWO F)"
 ],
 "Advanced": [
  "Codebreaker: Vigenere key JAH",
  "Codebreaker: Vigenere key PUZZLE",
  "Codebreaker: rail fence 3",
  "Codebreaker: rail fence 4",
  "Codebreaker: double lock",
  "Codebreaker: Vigenere key SIGNATURE",
  "Codebreaker: Vigenere key CODEBREAKER",
  "Codebreaker: rail fence 5",
  "Codebreaker: Atbash + Caesar double",
  "Codebreaker: reverse + Vigenere double",
  "Codebreaker: Caesar + rail double"
 ]
};
var DEMOKIND="cipher-roundtrip";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Codebreaker Study — "+safe+"\n"
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
    name:topic+' — codebreaker puzzle record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A codebreaker puzzle record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-codebreaker-challenge-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-codebreaker-challenge-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
