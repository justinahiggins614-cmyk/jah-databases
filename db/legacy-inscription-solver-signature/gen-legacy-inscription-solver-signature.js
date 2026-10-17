(function(){'use strict';
/* JAH The Legacy Inscription Solver Signature Database generator — jahdb-legacy-inscription-solver-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LISS-";
var FIELDS=["Deciphered Scripts","Partially Deciphered Scripts","Undeciphered Scripts"];
var TOPICS={
 "Deciphered Scripts": [
  "The Rosetta Stone (Signature Edition) - Deciphered Scripts",
  "Egyptian Hieroglyphs (Signature Edition) - Deciphered Scripts",
  "The Demotic Script (Signature Edition) - Deciphered Scripts",
  "Linear B (Signature Edition) - Deciphered Scripts",
  "The Behistun Inscription (Signature Edition) - Deciphered Scripts",
  "Cuneiform - the Wedge System (Signature Edition) - Deciphered Scripts",
  "Old Persian Cuneiform (Signature Edition) - Deciphered Scripts",
  "Hittite Cuneiform (Signature Edition) - Deciphered Scripts",
  "Mayan Glyphs (Signature Edition) - Deciphered Scripts",
  "Brahmi Script (Signature Edition) - Deciphered Scripts",
  "Ugaritic Script (Signature Edition) - Deciphered Scripts",
  "Oracle Bone Script (Signature Edition) - Deciphered Scripts"
 ],
 "Partially Deciphered Scripts": [
  "Luwian Hieroglyphs (Signature Edition) - Partially Deciphered Scripts",
  "The Etruscan Script Decipherment (Signature Edition) - Partially Deciphered Scripts",
  "Meroitic Script (Signature Edition) - Partially Deciphered Scripts",
  "Carian Script (Signature Edition) - Partially Deciphered Scripts",
  "Iberian Scripts (Signature Edition) - Partially Deciphered Scripts",
  "Linear Elamite (Signature Edition) - Partially Deciphered Scripts",
  "Epi-Olmec (Isthmian) Script (Signature Edition) - Partially Deciphered Scripts",
  "Zapotec Script (Signature Edition) - Partially Deciphered Scripts",
  "Khitan Scripts (Signature Edition) - Partially Deciphered Scripts",
  "Tangut Script (Signature Edition) - Partially Deciphered Scripts"
 ],
 "Undeciphered Scripts": [
  "Linear A (Signature Edition) - Undeciphered Scripts",
  "The Indus Script (Signature Edition) - Undeciphered Scripts",
  "Cretan Hieroglyphs (Signature Edition) - Undeciphered Scripts",
  "Proto-Elamite Script (Signature Edition) - Undeciphered Scripts",
  "Rongorongo (Signature Edition) - Undeciphered Scripts",
  "The Phaistos Disc (Signature Edition) - Undeciphered Scripts",
  "The Byblos Syllabary (Signature Edition) - Undeciphered Scripts",
  "Cypro-Minoan Script (Signature Edition) - Undeciphered Scripts",
  "The Voynich Cipher (Signature Edition) - Undeciphered Scripts",
  "The Rohonc Codex (Signature Edition) - Undeciphered Scripts",
  "The Vinca-Turdas Symbols (Signature Edition) - Undeciphered Scripts",
  "The Cascajal Block (Signature Edition) - Undeciphered Scripts"
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
var gen={version:'jahdb-legacy-inscription-solver-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('legacy-inscription-solver-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
