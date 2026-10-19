(function(){'use strict';
/* JAH The Research Translation to Practice Database generator — jahdb-research-translation-to-practice-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RTTP-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Research Translation to Practice: Asking Answerable Questions — foundations",
  "Research Translation to Practice: The Protocol First Rule — foundations",
  "Research Translation to Practice: Literature Review That Works — foundations",
  "Research Translation to Practice: Study Design Basics — foundations",
  "Research Translation to Practice: Sampling Without Bias — foundations",
  "Research Translation to Practice: Measurement You Can Trust — foundations",
  "Research Translation to Practice: Data Collection Discipline — foundations",
  "Research Translation to Practice: The Lab Notebook Standard — foundations",
  "Research Translation to Practice: Basic Statistics Honestly — foundations",
  "Research Translation to Practice: Avoiding p-Hacking — foundations",
  "Research Translation to Practice: Visualizing Results Truthfully — foundations",
  "Research Translation to Practice: Writing It Up — foundations"
 ],
 "compounded": [
  "Research Translation to Practice: Peer Review Survival — compounded",
  "Research Translation to Practice: Sharing Data and Code — compounded",
  "Research Translation to Practice: Replication: The Gold Standard — compounded",
  "Research Translation to Practice: Systematic Reviews — compounded",
  "Research Translation to Practice: Ethics in Practice — compounded",
  "Research Translation to Practice: Human Subjects Navigation — compounded",
  "Research Translation to Practice: Collaborating Across Labs — compounded",
  "Research Translation to Practice: Translating to Practice — compounded",
  "Research Translation to Practice: Funding the Work — compounded",
  "Research Translation to Practice: Communicating Science — compounded",
  "Research Translation to Practice: Advanced: Advanced Design — compounded",
  "Research Translation to Practice: Advanced: Bayesian Thinking — compounded"
 ],
 "advanced": [
  "Research Translation to Practice: Advanced: Causal Inference — advanced",
  "Research Translation to Practice: Advanced: Open Science at Scale — advanced",
  "Research Translation to Practice: Advanced: Meta-Science — advanced",
  "Research Translation to Practice: Advanced: Interdisciplinary Work — advanced",
  "Research Translation to Practice: Advanced: Science Policy — advanced",
  "Research Translation to Practice: Advanced: Running a Lab — advanced",
  "Research Translation to Practice: Advanced: The 20-Year Program — advanced",
  "Research Translation to Practice: Advanced: Citizen Science — advanced",
  "Research Translation to Practice: Advanced: Teaching Research Methods — advanced",
  "Research Translation to Practice: Advanced: The Future of the Field — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Research Translation to Practice Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
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
var gen={version:'jahdb-research-translation-to-practice-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-translation-to-practice',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
