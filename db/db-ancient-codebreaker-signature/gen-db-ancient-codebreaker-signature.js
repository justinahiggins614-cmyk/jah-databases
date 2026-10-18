(function(){'use strict';
/* JAH The Ancient Codebreaker Signature Database generator — jahdb-db-ancient-codebreaker-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MACDS-";
var FIELDS=["Deciphered Scripts","Partially Read","Still Undeciphered"];
var TOPICS={
 "Deciphered Scripts": [
  "Egyptian Hieroglyphs (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Egyptian Hieroglyphs \u2014 Deciphered Scripts",
  "Linear B (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Linear B \u2014 Deciphered Scripts",
  "Cuneiform Deciphered (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Cuneiform Deciphered \u2014 Deciphered Scripts",
  "Maya Glyphs (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Maya Glyphs \u2014 Deciphered Scripts",
  "Ugaritic (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Ugaritic \u2014 Deciphered Scripts",
  "Brahmi (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Brahmi \u2014 Deciphered Scripts",
  "The Cherokee Syllabary (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for The Cherokee Syllabary \u2014 Deciphered Scripts",
  "Oracle Bone Script (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Oracle Bone Script \u2014 Deciphered Scripts",
  "The Ogham Alphabet (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for The Ogham Alphabet \u2014 Deciphered Scripts",
  "Demotic Egyptian (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for Demotic Egyptian \u2014 Deciphered Scripts",
  "How Decipherment Works (Signature Edition) \u2014 Deciphered Scripts",
  "The Signature Method for How Decipherment Works \u2014 Deciphered Scripts"
 ],
 "Partially Read": [
  "Meroitic (Signature Edition) \u2014 Partially Read",
  "The Signature Method for Meroitic \u2014 Partially Read",
  "The Etruscan Script (Signature Edition) \u2014 Partially Read",
  "The Signature Method for The Etruscan Script \u2014 Partially Read"
 ],
 "Still Undeciphered": [
  "Rongorongo (Signature Edition) \u2014 Still Undeciphered",
  "The Signature Method for Rongorongo \u2014 Still Undeciphered",
  "The Indus Script (Signature Edition) \u2014 Still Undeciphered",
  "The Signature Method for The Indus Script \u2014 Still Undeciphered",
  "The Phaistos Disc (Signature Edition) \u2014 Still Undeciphered",
  "The Signature Method for The Phaistos Disc \u2014 Still Undeciphered",
  "The Cascajal Block (Signature Edition) \u2014 Still Undeciphered",
  "The Signature Method for The Cascajal Block \u2014 Still Undeciphered"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Ancient Script Study — "+safe+"\n"
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
    name:topic+' — ancient script record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A ancient script record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-ancient-codebreaker-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-ancient-codebreaker-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
