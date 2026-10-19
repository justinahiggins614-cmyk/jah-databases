(function(){'use strict';
/* JAH The Research Collaboration Directory Signature Database generator — jahdb-research-collaboration-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RCDS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Research Collaboration Directory (Signature): Asking Answerable Questions — foundations",
  "Research Collaboration Directory (Signature): The Protocol First Rule — foundations",
  "Research Collaboration Directory (Signature): Literature Review That Works — foundations",
  "Research Collaboration Directory (Signature): Study Design Basics — foundations",
  "Research Collaboration Directory (Signature): Sampling Without Bias — foundations",
  "Research Collaboration Directory (Signature): Measurement You Can Trust — foundations",
  "Research Collaboration Directory (Signature): Data Collection Discipline — foundations",
  "Research Collaboration Directory (Signature): The Lab Notebook Standard — foundations",
  "Research Collaboration Directory (Signature): Basic Statistics Honestly — foundations",
  "Research Collaboration Directory (Signature): Avoiding p-Hacking — foundations",
  "Research Collaboration Directory (Signature): Visualizing Results Truthfully — foundations",
  "Research Collaboration Directory (Signature): Writing It Up — foundations"
 ],
 "compounded": [
  "Research Collaboration Directory (Signature): Peer Review Survival — compounded",
  "Research Collaboration Directory (Signature): Sharing Data and Code — compounded",
  "Research Collaboration Directory (Signature): Replication: The Gold Standard — compounded",
  "Research Collaboration Directory (Signature): Systematic Reviews — compounded",
  "Research Collaboration Directory (Signature): Ethics in Practice — compounded",
  "Research Collaboration Directory (Signature): Human Subjects Navigation — compounded",
  "Research Collaboration Directory (Signature): Collaborating Across Labs — compounded",
  "Research Collaboration Directory (Signature): Translating to Practice — compounded",
  "Research Collaboration Directory (Signature): Funding the Work — compounded",
  "Research Collaboration Directory (Signature): Communicating Science — compounded",
  "Research Collaboration Directory (Signature): Advanced: Advanced Design — compounded",
  "Research Collaboration Directory (Signature): Advanced: Bayesian Thinking — compounded"
 ],
 "advanced": [
  "Research Collaboration Directory (Signature): Advanced: Causal Inference — advanced",
  "Research Collaboration Directory (Signature): Advanced: Open Science at Scale — advanced",
  "Research Collaboration Directory (Signature): Advanced: Meta-Science — advanced",
  "Research Collaboration Directory (Signature): Advanced: Interdisciplinary Work — advanced",
  "Research Collaboration Directory (Signature): Advanced: Science Policy — advanced",
  "Research Collaboration Directory (Signature): Advanced: Running a Lab — advanced",
  "Research Collaboration Directory (Signature): Advanced: The 20-Year Program — advanced",
  "Research Collaboration Directory (Signature): Advanced: Citizen Science — advanced",
  "Research Collaboration Directory (Signature): Advanced: Teaching Research Methods — advanced",
  "Research Collaboration Directory (Signature): Advanced: The Future of the Field — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Research Collaboration Directory Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-research-collaboration-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-collaboration-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
