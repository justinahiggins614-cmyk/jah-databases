(function(){'use strict';
/* JAH The Mystery Tournament Database generator — jahdb-db-mystery-tournament-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMTD-";
var FIELDS=["Formats","Rounds","Scoring"];
var TOPICS={
 "Formats": [
  "The Clue Relay \u2014 Formats",
  "The Clue Relay \u2014 Deep Dive \u2014 Formats",
  "The Deduction Debate \u2014 Formats",
  "The Deduction Debate \u2014 Deep Dive \u2014 Formats",
  "The Evidence Escape \u2014 Formats",
  "The Evidence Escape \u2014 Deep Dive \u2014 Formats",
  "The Suspect Draft \u2014 Formats",
  "The Suspect Draft \u2014 Deep Dive \u2014 Formats",
  "The Marathon Mystery \u2014 Formats",
  "The Marathon Mystery \u2014 Deep Dive \u2014 Formats",
  "The Season League \u2014 Formats",
  "The Season League \u2014 Deep Dive \u2014 Formats",
  "The Junior Sleuth Circuit \u2014 Formats",
  "The Junior Sleuth Circuit \u2014 Deep Dive \u2014 Formats"
 ],
 "Rounds": [
  "The Alibi Audit \u2014 Rounds",
  "The Alibi Audit \u2014 Deep Dive \u2014 Rounds",
  "The Timeline Trials \u2014 Rounds",
  "The Timeline Trials \u2014 Deep Dive \u2014 Rounds",
  "The Cipher Sprint \u2014 Rounds",
  "The Cipher Sprint \u2014 Deep Dive \u2014 Rounds",
  "Lightning Deductions \u2014 Rounds",
  "Lightning Deductions \u2014 Deep Dive \u2014 Rounds",
  "The Forgery Trial \u2014 Rounds",
  "The Forgery Trial \u2014 Deep Dive \u2014 Rounds",
  "The Witness Cross-Examination \u2014 Rounds",
  "The Witness Cross-Examination \u2014 Deep Dive \u2014 Rounds",
  "The Map Room \u2014 Rounds",
  "The Map Room \u2014 Deep Dive \u2014 Rounds",
  "The Tournament Codebreak \u2014 Rounds",
  "The Tournament Codebreak \u2014 Deep Dive \u2014 Rounds",
  "The Grand Interrogation \u2014 Rounds",
  "The Grand Interrogation \u2014 Deep Dive \u2014 Rounds"
 ],
 "Scoring": [
  "The Fair-Play Charter \u2014 Scoring",
  "The Fair-Play Charter \u2014 Deep Dive \u2014 Scoring"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mystery Tournament Study — "+safe+"\n"
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
    name:topic+' — mystery tournament record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mystery tournament record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-mystery-tournament-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mystery-tournament',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
