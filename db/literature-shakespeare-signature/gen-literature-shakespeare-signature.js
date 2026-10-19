(function(){'use strict';
/* JAH Signature Shakespeare Database generator — "jahdb-literature-shakespeare-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LSHS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Hamlet (Signature Edition)", "Romeo and Juliet (Signature Edition)", "Macbeth (Signature Edition)", "Othello (Signature Edition)", "King Lear (Signature Edition)", "A Midsummer Night's Dream (Signature Edition)", "The Tempest (Signature Edition)", "Much Ado About Nothing (Signature Edition)", "Julius Caesar (Signature Edition)", "Henry V (Signature Edition)", "The Merchant of Venice (Signature Edition)", "Twelfth Night (Signature Edition)"], "Compounded": ["Richard III (Signature Edition)", "Henry IV, Part 1 (Signature Edition)", "As You Like It (Signature Edition)", "The Winter's Tale (Signature Edition)", "Coriolanus (Signature Edition)", "Antony and Cleopatra (Signature Edition)", "Measure for Measure (Signature Edition)", "The Taming of the Shrew (Signature Edition)", "Cymbeline (Signature Edition)", "Titus Andronicus (Signature Edition)", "The Comedy of Errors (Signature Edition)", "Love's Labour's Lost (Signature Edition)"], "Advanced": ["The Sonnets (Signature Edition)", "Venus and Adonis (Signature Edition)", "The Rape of Lucrece (Signature Edition)", "Troilus and Cressida (Signature Edition)", "Timon of Athens (Signature Edition)", "Pericles (Signature Edition)", "King John (Signature Edition)", "The Two Gentlemen of Verona (Signature Edition)", "All's Well That Ends Well (Signature Edition)", "The Authorship Question (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — literature-shakespeare-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Signature sample — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature-original literary record',
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature-original literary record study. Signature original samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-sample",
    sample:true,
    disclaimer:"Generated Signature sample \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-literature-shakespeare-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("literature-shakespeare-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
