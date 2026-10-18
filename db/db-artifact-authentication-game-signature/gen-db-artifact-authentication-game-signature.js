(function(){'use strict';
/* JAH The Artifact Authentication Game Signature Database generator — jahdb-db-artifact-authentication-game-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAAGS-";
var FIELDS=["The Tests","The Tells","The Verdicts"];
var TOPICS={
 "The Tests": [
  "The Patina Test (Signature Edition) \u2014 The Tests",
  "The Signature Method for The Patina Test \u2014 The Tests",
  "The Wear Test (Signature Edition) \u2014 The Tests",
  "The Signature Method for The Wear Test \u2014 The Tests",
  "The Style Test (Signature Edition) \u2014 The Tests",
  "The Signature Method for The Style Test \u2014 The Tests",
  "The Material Test (Signature Edition) \u2014 The Tests",
  "The Signature Method for The Material Test \u2014 The Tests",
  "The Provenance Test (Signature Edition) \u2014 The Tests",
  "The Signature Method for The Provenance Test \u2014 The Tests"
 ],
 "The Tells": [
  "The Tooled Tell (Signature Edition) \u2014 The Tells",
  "The Signature Method for The Tooled Tell \u2014 The Tells",
  "The Painted Tell (Signature Edition) \u2014 The Tells",
  "The Signature Method for The Painted Tell \u2014 The Tells",
  "The Repaired Tell (Signature Edition) \u2014 The Tells",
  "The Signature Method for The Repaired Tell \u2014 The Tells",
  "The Cast Tell (Signature Edition) \u2014 The Tells",
  "The Signature Method for The Cast Tell \u2014 The Tells",
  "The Signed Tell (Signature Edition) \u2014 The Tells",
  "The Signature Method for The Signed Tell \u2014 The Tells"
 ],
 "The Verdicts": [
  "The Genuine Article (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Genuine Article \u2014 The Verdicts",
  "The Honest Replica (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Honest Replica \u2014 The Verdicts",
  "The Altered Original (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Altered Original \u2014 The Verdicts",
  "The Frankenstein (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Frankenstein \u2014 The Verdicts",
  "The Fantasy Piece (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Fantasy Piece \u2014 The Verdicts",
  "The Modern Fake (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Modern Fake \u2014 The Verdicts",
  "The Connoisseur's Eye (Signature Edition) \u2014 The Verdicts",
  "The Signature Method for The Connoisseur's Eye \u2014 The Verdicts"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Artifact Authentication Study — "+safe+"\n"
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
    name:topic+' — artifact authentication record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A artifact authentication record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-artifact-authentication-game-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-artifact-authentication-game-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
