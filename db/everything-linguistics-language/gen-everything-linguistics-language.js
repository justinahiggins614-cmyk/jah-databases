(function(){'use strict';
/* JAH The Everything Linguistics and Language Database generator — jahdb-everything-linguistics-language-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVLL-";
var FIELDS=["Core Linguistics","Applied","Signature Linguistics"];
var TOPICS={
 "Core Linguistics": [
  "Phonetics: The Sounds of Speech \u2014 Core Linguistics",
  "Phonology: Sound Patterns and Rules \u2014 Core Linguistics",
  "Morphology: The Structure of Words \u2014 Core Linguistics",
  "Syntax: The Structure of Sentences \u2014 Core Linguistics",
  "Semantics: Meaning and Reference \u2014 Core Linguistics",
  "Writing Systems: Alphabets to Logograms \u2014 Core Linguistics"
 ],
 "Applied": [
  "Language Acquisition: How Children Learn Language \u2014 Applied",
  "Sociolinguistics: Language in Society \u2014 Applied"
 ],
 "Signature Linguistics": [
  "Signature Grammar Engine (Signature Edition) \u2014 Signature Linguistics",
  "Signature Sound Pattern Analyzer (Signature Edition) \u2014 Signature Linguistics",
  "Signature Translation Mapper (Signature Edition) \u2014 Signature Linguistics",
  "Signature Language Learning Optimizer (Signature Edition) \u2014 Signature Linguistics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Linguistics Language — "+safe+"\n"
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
    name:topic+' — linguistics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A linguistics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-linguistics-language-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-linguistics-language',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
