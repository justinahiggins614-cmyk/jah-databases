(function(){'use strict';
/* JAH The Job Training Assistance Signature Database generator — jahdb-job-training-assistance-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JTAS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Job Training Assistance (Signature): Knowing What Exists — foundations",
  "Job Training Assistance (Signature): Eligibility in Plain Terms — foundations",
  "Job Training Assistance (Signature): The Big Four Documents — foundations",
  "Job Training Assistance (Signature): Applying Without Errors — foundations",
  "Job Training Assistance (Signature): Interviews and Verifications — foundations",
  "Job Training Assistance (Signature): When You Are Denied — foundations",
  "Job Training Assistance (Signature): Renewals and Reporting Changes — foundations",
  "Job Training Assistance (Signature): Combining Multiple Programs — foundations",
  "Job Training Assistance (Signature): Emergency Help Fast — foundations",
  "Job Training Assistance (Signature): Help for Seniors — foundations",
  "Job Training Assistance (Signature): Help for Families With Kids — foundations",
  "Job Training Assistance (Signature): Help for People With Disabilities — foundations"
 ],
 "compounded": [
  "Job Training Assistance (Signature): Help for Veterans — compounded",
  "Job Training Assistance (Signature): Rural Access Strategies — compounded",
  "Job Training Assistance (Signature): Language Access — compounded",
  "Job Training Assistance (Signature): Avoiding Benefit Scams — compounded",
  "Job Training Assistance (Signature): Working While Receiving Help — compounded",
  "Job Training Assistance (Signature): Childcare Specifics — compounded",
  "Job Training Assistance (Signature): Housing-Adjacent Help — compounded",
  "Job Training Assistance (Signature): Food-Adjacent Help — compounded",
  "Job Training Assistance (Signature): Health Coverage Navigation — compounded",
  "Job Training Assistance (Signature): Transportation to Services — compounded",
  "Job Training Assistance (Signature): Advanced: Appeals Mastery — compounded",
  "Job Training Assistance (Signature): Advanced: Overpayment Defense — compounded"
 ],
 "advanced": [
  "Job Training Assistance (Signature): Advanced: Coordinating a Case — advanced",
  "Job Training Assistance (Signature): Advanced: Policy Change Tracking — advanced",
  "Job Training Assistance (Signature): Advanced: Helping Others Apply — advanced",
  "Job Training Assistance (Signature): Advanced: Community Needs Assessment — advanced",
  "Job Training Assistance (Signature): Advanced: Building a Help Network — advanced",
  "Job Training Assistance (Signature): Advanced: Data and Dignity — advanced",
  "Job Training Assistance (Signature): Advanced: Disaster Response — advanced",
  "Job Training Assistance (Signature): Advanced: Systems Advocacy — advanced",
  "Job Training Assistance (Signature): Advanced: Running a Nonprofit Program — advanced",
  "Job Training Assistance (Signature): Advanced: Lifetime Safety Net Planning — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Job Training Assistance Signature Database — structural study\n"
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
var gen={version:'jahdb-job-training-assistance-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('job-training-assistance-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
