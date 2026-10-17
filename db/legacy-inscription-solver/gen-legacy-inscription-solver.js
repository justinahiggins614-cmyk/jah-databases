(function(){'use strict';
/* JAH The Legacy Inscription Solver Database generator — jahdb-legacy-inscription-solver-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LIS-";
var FIELDS=["Deciphered Scripts","Partially Deciphered Scripts","Undeciphered Scripts"];
var TOPICS={
 "Deciphered Scripts": [
  "The Rosetta Stone - Deciphered Scripts",
  "Egyptian Hieroglyphs - Deciphered Scripts",
  "The Demotic Script - Deciphered Scripts",
  "Linear B - Deciphered Scripts",
  "The Behistun Inscription - Deciphered Scripts",
  "Cuneiform - the Wedge System - Deciphered Scripts",
  "Old Persian Cuneiform - Deciphered Scripts",
  "Hittite Cuneiform - Deciphered Scripts",
  "Mayan Glyphs - Deciphered Scripts",
  "Brahmi Script - Deciphered Scripts",
  "Ugaritic Script - Deciphered Scripts",
  "Oracle Bone Script - Deciphered Scripts"
 ],
 "Partially Deciphered Scripts": [
  "Luwian Hieroglyphs - Partially Deciphered Scripts",
  "The Etruscan Script Decipherment - Partially Deciphered Scripts",
  "Meroitic Script - Partially Deciphered Scripts",
  "Carian Script - Partially Deciphered Scripts",
  "Iberian Scripts - Partially Deciphered Scripts",
  "Linear Elamite - Partially Deciphered Scripts",
  "Epi-Olmec (Isthmian) Script - Partially Deciphered Scripts",
  "Zapotec Script - Partially Deciphered Scripts",
  "Khitan Scripts - Partially Deciphered Scripts",
  "Tangut Script - Partially Deciphered Scripts"
 ],
 "Undeciphered Scripts": [
  "Linear A - Undeciphered Scripts",
  "The Indus Script - Undeciphered Scripts",
  "Cretan Hieroglyphs - Undeciphered Scripts",
  "Proto-Elamite Script - Undeciphered Scripts",
  "Rongorongo - Undeciphered Scripts",
  "The Phaistos Disc - Undeciphered Scripts",
  "The Byblos Syllabary - Undeciphered Scripts",
  "Cypro-Minoan Script - Undeciphered Scripts",
  "The Voynich Cipher - Undeciphered Scripts",
  "The Rohonc Codex - Undeciphered Scripts",
  "The Vinca-Turdas Symbols - Undeciphered Scripts",
  "The Cascajal Block - Undeciphered Scripts"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Inscription Solution Study — "+safe+"\n"
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
    name:topic+' — inscription solution record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A inscription solution record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"inscription-solver-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-legacy-inscription-solver-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('legacy-inscription-solver',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
