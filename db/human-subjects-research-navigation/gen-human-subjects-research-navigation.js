(function(){'use strict';
/* JAH The Human Subjects Research Navigation Database generator — jahdb-human-subjects-research-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HSRN-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Human Subjects Research Navigation: Asking Answerable Questions — foundations",
  "Human Subjects Research Navigation: The Protocol First Rule — foundations",
  "Human Subjects Research Navigation: Literature Review That Works — foundations",
  "Human Subjects Research Navigation: Study Design Basics — foundations",
  "Human Subjects Research Navigation: Sampling Without Bias — foundations",
  "Human Subjects Research Navigation: Measurement You Can Trust — foundations",
  "Human Subjects Research Navigation: Data Collection Discipline — foundations",
  "Human Subjects Research Navigation: The Lab Notebook Standard — foundations",
  "Human Subjects Research Navigation: Basic Statistics Honestly — foundations",
  "Human Subjects Research Navigation: Avoiding p-Hacking — foundations",
  "Human Subjects Research Navigation: Visualizing Results Truthfully — foundations",
  "Human Subjects Research Navigation: Writing It Up — foundations"
 ],
 "compounded": [
  "Human Subjects Research Navigation: Peer Review Survival — compounded",
  "Human Subjects Research Navigation: Sharing Data and Code — compounded",
  "Human Subjects Research Navigation: Replication: The Gold Standard — compounded",
  "Human Subjects Research Navigation: Systematic Reviews — compounded",
  "Human Subjects Research Navigation: Ethics in Practice — compounded",
  "Human Subjects Research Navigation: Human Subjects Navigation — compounded",
  "Human Subjects Research Navigation: Collaborating Across Labs — compounded",
  "Human Subjects Research Navigation: Translating to Practice — compounded",
  "Human Subjects Research Navigation: Funding the Work — compounded",
  "Human Subjects Research Navigation: Communicating Science — compounded",
  "Human Subjects Research Navigation: Advanced: Advanced Design — compounded",
  "Human Subjects Research Navigation: Advanced: Bayesian Thinking — compounded"
 ],
 "advanced": [
  "Human Subjects Research Navigation: Advanced: Causal Inference — advanced",
  "Human Subjects Research Navigation: Advanced: Open Science at Scale — advanced",
  "Human Subjects Research Navigation: Advanced: Meta-Science — advanced",
  "Human Subjects Research Navigation: Advanced: Interdisciplinary Work — advanced",
  "Human Subjects Research Navigation: Advanced: Science Policy — advanced",
  "Human Subjects Research Navigation: Advanced: Running a Lab — advanced",
  "Human Subjects Research Navigation: Advanced: The 20-Year Program — advanced",
  "Human Subjects Research Navigation: Advanced: Citizen Science — advanced",
  "Human Subjects Research Navigation: Advanced: Teaching Research Methods — advanced",
  "Human Subjects Research Navigation: Advanced: The Future of the Field — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Human Subjects Research Navigation Database — structural study\n"
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
var gen={version:'jahdb-human-subjects-research-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('human-subjects-research-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
