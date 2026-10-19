(function(){'use strict';
/* JAH The Research Translation to Practice Signature Database generator — jahdb-research-translation-to-practice-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RTTPS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Research Translation to Practice (Signature): Asking Answerable Questions — foundations",
  "Research Translation to Practice (Signature): The Protocol First Rule — foundations",
  "Research Translation to Practice (Signature): Literature Review That Works — foundations",
  "Research Translation to Practice (Signature): Study Design Basics — foundations",
  "Research Translation to Practice (Signature): Sampling Without Bias — foundations",
  "Research Translation to Practice (Signature): Measurement You Can Trust — foundations",
  "Research Translation to Practice (Signature): Data Collection Discipline — foundations",
  "Research Translation to Practice (Signature): The Lab Notebook Standard — foundations",
  "Research Translation to Practice (Signature): Basic Statistics Honestly — foundations",
  "Research Translation to Practice (Signature): Avoiding p-Hacking — foundations",
  "Research Translation to Practice (Signature): Visualizing Results Truthfully — foundations",
  "Research Translation to Practice (Signature): Writing It Up — foundations"
 ],
 "compounded": [
  "Research Translation to Practice (Signature): Peer Review Survival — compounded",
  "Research Translation to Practice (Signature): Sharing Data and Code — compounded",
  "Research Translation to Practice (Signature): Replication: The Gold Standard — compounded",
  "Research Translation to Practice (Signature): Systematic Reviews — compounded",
  "Research Translation to Practice (Signature): Ethics in Practice — compounded",
  "Research Translation to Practice (Signature): Human Subjects Navigation — compounded",
  "Research Translation to Practice (Signature): Collaborating Across Labs — compounded",
  "Research Translation to Practice (Signature): Translating to Practice — compounded",
  "Research Translation to Practice (Signature): Funding the Work — compounded",
  "Research Translation to Practice (Signature): Communicating Science — compounded",
  "Research Translation to Practice (Signature): Advanced: Advanced Design — compounded",
  "Research Translation to Practice (Signature): Advanced: Bayesian Thinking — compounded"
 ],
 "advanced": [
  "Research Translation to Practice (Signature): Advanced: Causal Inference — advanced",
  "Research Translation to Practice (Signature): Advanced: Open Science at Scale — advanced",
  "Research Translation to Practice (Signature): Advanced: Meta-Science — advanced",
  "Research Translation to Practice (Signature): Advanced: Interdisciplinary Work — advanced",
  "Research Translation to Practice (Signature): Advanced: Science Policy — advanced",
  "Research Translation to Practice (Signature): Advanced: Running a Lab — advanced",
  "Research Translation to Practice (Signature): Advanced: The 20-Year Program — advanced",
  "Research Translation to Practice (Signature): Advanced: Citizen Science — advanced",
  "Research Translation to Practice (Signature): Advanced: Teaching Research Methods — advanced",
  "Research Translation to Practice (Signature): Advanced: The Future of the Field — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Research Translation to Practice Signature Database — structural study\n"
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
var gen={version:'jahdb-research-translation-to-practice-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-translation-to-practice-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
