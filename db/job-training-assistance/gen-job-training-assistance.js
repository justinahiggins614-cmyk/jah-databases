(function(){'use strict';
/* JAH The Job Training Assistance Database generator — jahdb-job-training-assistance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JTA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Job Training Assistance: Knowing What Exists — foundations",
  "Job Training Assistance: Eligibility in Plain Terms — foundations",
  "Job Training Assistance: The Big Four Documents — foundations",
  "Job Training Assistance: Applying Without Errors — foundations",
  "Job Training Assistance: Interviews and Verifications — foundations",
  "Job Training Assistance: When You Are Denied — foundations",
  "Job Training Assistance: Renewals and Reporting Changes — foundations",
  "Job Training Assistance: Combining Multiple Programs — foundations",
  "Job Training Assistance: Emergency Help Fast — foundations",
  "Job Training Assistance: Help for Seniors — foundations",
  "Job Training Assistance: Help for Families With Kids — foundations",
  "Job Training Assistance: Help for People With Disabilities — foundations"
 ],
 "compounded": [
  "Job Training Assistance: Help for Veterans — compounded",
  "Job Training Assistance: Rural Access Strategies — compounded",
  "Job Training Assistance: Language Access — compounded",
  "Job Training Assistance: Avoiding Benefit Scams — compounded",
  "Job Training Assistance: Working While Receiving Help — compounded",
  "Job Training Assistance: Childcare Specifics — compounded",
  "Job Training Assistance: Housing-Adjacent Help — compounded",
  "Job Training Assistance: Food-Adjacent Help — compounded",
  "Job Training Assistance: Health Coverage Navigation — compounded",
  "Job Training Assistance: Transportation to Services — compounded",
  "Job Training Assistance: Advanced: Appeals Mastery — compounded",
  "Job Training Assistance: Advanced: Overpayment Defense — compounded"
 ],
 "advanced": [
  "Job Training Assistance: Advanced: Coordinating a Case — advanced",
  "Job Training Assistance: Advanced: Policy Change Tracking — advanced",
  "Job Training Assistance: Advanced: Helping Others Apply — advanced",
  "Job Training Assistance: Advanced: Community Needs Assessment — advanced",
  "Job Training Assistance: Advanced: Building a Help Network — advanced",
  "Job Training Assistance: Advanced: Data and Dignity — advanced",
  "Job Training Assistance: Advanced: Disaster Response — advanced",
  "Job Training Assistance: Advanced: Systems Advocacy — advanced",
  "Job Training Assistance: Advanced: Running a Nonprofit Program — advanced",
  "Job Training Assistance: Advanced: Lifetime Safety Net Planning — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Job Training Assistance Database — structural study\n"
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
var gen={version:'jahdb-job-training-assistance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('job-training-assistance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
