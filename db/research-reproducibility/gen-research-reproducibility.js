(function(){'use strict';
/* JAH The Research Reproducibility Database generator — jahdb-research-reproducibility-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RR-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Research Reproducibility: Asking Answerable Questions — foundations",
  "Research Reproducibility: The Protocol First Rule — foundations",
  "Research Reproducibility: Literature Review That Works — foundations",
  "Research Reproducibility: Study Design Basics — foundations",
  "Research Reproducibility: Sampling Without Bias — foundations",
  "Research Reproducibility: Measurement You Can Trust — foundations",
  "Research Reproducibility: Data Collection Discipline — foundations",
  "Research Reproducibility: The Lab Notebook Standard — foundations",
  "Research Reproducibility: Basic Statistics Honestly — foundations",
  "Research Reproducibility: Avoiding p-Hacking — foundations",
  "Research Reproducibility: Visualizing Results Truthfully — foundations",
  "Research Reproducibility: Writing It Up — foundations"
 ],
 "compounded": [
  "Research Reproducibility: Peer Review Survival — compounded",
  "Research Reproducibility: Sharing Data and Code — compounded",
  "Research Reproducibility: Replication: The Gold Standard — compounded",
  "Research Reproducibility: Systematic Reviews — compounded",
  "Research Reproducibility: Ethics in Practice — compounded",
  "Research Reproducibility: Human Subjects Navigation — compounded",
  "Research Reproducibility: Collaborating Across Labs — compounded",
  "Research Reproducibility: Translating to Practice — compounded",
  "Research Reproducibility: Funding the Work — compounded",
  "Research Reproducibility: Communicating Science — compounded",
  "Research Reproducibility: Advanced: Advanced Design — compounded",
  "Research Reproducibility: Advanced: Bayesian Thinking — compounded"
 ],
 "advanced": [
  "Research Reproducibility: Advanced: Causal Inference — advanced",
  "Research Reproducibility: Advanced: Open Science at Scale — advanced",
  "Research Reproducibility: Advanced: Meta-Science — advanced",
  "Research Reproducibility: Advanced: Interdisciplinary Work — advanced",
  "Research Reproducibility: Advanced: Science Policy — advanced",
  "Research Reproducibility: Advanced: Running a Lab — advanced",
  "Research Reproducibility: Advanced: The 20-Year Program — advanced",
  "Research Reproducibility: Advanced: Citizen Science — advanced",
  "Research Reproducibility: Advanced: Teaching Research Methods — advanced",
  "Research Reproducibility: Advanced: The Future of the Field — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Research Reproducibility Database — structural study\n"
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
var gen={version:'jahdb-research-reproducibility-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-reproducibility',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
