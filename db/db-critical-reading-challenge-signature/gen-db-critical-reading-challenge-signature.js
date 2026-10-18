(function(){'use strict';
/* JAH The Critical Reading Challenge generator — jahdb-db-critical-reading-challenge-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRRCS-";
var FIELDS=["Arguments","Evidence","Fallacies"];
var TOPICS={
 "Arguments": [
  "What Is an Argument (Signature Edition) - Arguments",
  "Premises and Conclusions (Signature Edition) - Arguments",
  "Deductive vs Inductive (Signature Edition) - Arguments",
  "Strong vs Weak Arguments (Signature Edition) - Arguments",
  "Spotting the Conclusion (Signature Edition) - Arguments",
  "Assumptions: The Hidden Floor (Signature Edition) - Arguments",
  "Counterarguments: Steelman First (Signature Edition) - Arguments",
  "Qualifiers and Hedging (Signature Edition) - Arguments",
  "Analogies: Useful, Dangerous (Signature Edition) - Arguments",
  "Causal Arguments (Signature Edition) - Arguments",
  "Statistical Arguments (Signature Edition) - Arguments",
  "Expert Appeals: When to Trust (Signature Edition) - Arguments"
 ],
 "Evidence": [
  "What Counts as Evidence (Signature Edition) - Evidence",
  "Anecdotes vs Data (Signature Edition) - Evidence",
  "Correlation Is Not Causation (Signature Edition) - Evidence",
  "Sample Quality (Signature Edition) - Evidence",
  "Cherry-Picking (Signature Edition) - Evidence",
  "Base Rates Matter (Signature Edition) - Evidence",
  "Replication: Trust, Then Verify (Signature Edition) - Evidence",
  "Primary vs Secondary Sources (Signature Edition) - Evidence",
  "Graphs That Mislead (Signature Edition) - Evidence"
 ],
 "Fallacies": [
  "Ad Hominem Attacks (Signature Edition) - Fallacies",
  "Straw Man (Signature Edition) - Fallacies",
  "False Dilemma (Signature Edition) - Fallacies",
  "Slippery Slope (Signature Edition) - Fallacies",
  "Appeal to Authority (Bad) (Signature Edition) - Fallacies",
  "Bandwagon (Signature Edition) - Fallacies",
  "Begging the Question (Signature Edition) - Fallacies",
  "Hasty Generalization (Signature Edition) - Fallacies",
  "Red Herring (Signature Edition) - Fallacies",
  "Appeal to Emotion (Signature Edition) - Fallacies",
  "No True Scotsman (Signature Edition) - Fallacies",
  "The Fallacy Fallacy (Signature Edition) - Fallacies",
  "Reading Like a Detective (Signature Edition) - Fallacies"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Critical Reading Study — "+safe+"\n"
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
    name:topic+' — critical reading lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A critical reading lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"critical-reading-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-critical-reading-challenge-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-critical-reading-challenge-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
