(function(){'use strict';
/* JAH The Critical Reading Challenge generator — jahdb-db-critical-reading-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CRRC-";
var FIELDS=["Arguments","Evidence","Fallacies"];
var TOPICS={
 "Arguments": [
  "What Is an Argument - Arguments",
  "Premises and Conclusions - Arguments",
  "Deductive vs Inductive - Arguments",
  "Strong vs Weak Arguments - Arguments",
  "Spotting the Conclusion - Arguments",
  "Assumptions: The Hidden Floor - Arguments",
  "Counterarguments: Steelman First - Arguments",
  "Qualifiers and Hedging - Arguments",
  "Analogies: Useful, Dangerous - Arguments",
  "Causal Arguments - Arguments",
  "Statistical Arguments - Arguments",
  "Expert Appeals: When to Trust - Arguments"
 ],
 "Evidence": [
  "What Counts as Evidence - Evidence",
  "Anecdotes vs Data - Evidence",
  "Correlation Is Not Causation - Evidence",
  "Sample Quality - Evidence",
  "Cherry-Picking - Evidence",
  "Base Rates Matter - Evidence",
  "Replication: Trust, Then Verify - Evidence",
  "Primary vs Secondary Sources - Evidence",
  "Graphs That Mislead - Evidence"
 ],
 "Fallacies": [
  "Ad Hominem Attacks - Fallacies",
  "Straw Man - Fallacies",
  "False Dilemma - Fallacies",
  "Slippery Slope - Fallacies",
  "Appeal to Authority (Bad) - Fallacies",
  "Bandwagon - Fallacies",
  "Begging the Question - Fallacies",
  "Hasty Generalization - Fallacies",
  "Red Herring - Fallacies",
  "Appeal to Emotion - Fallacies",
  "No True Scotsman - Fallacies",
  "The Fallacy Fallacy - Fallacies",
  "Reading Like a Detective - Fallacies"
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
var gen={version:'jahdb-db-critical-reading-challenge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-critical-reading-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
