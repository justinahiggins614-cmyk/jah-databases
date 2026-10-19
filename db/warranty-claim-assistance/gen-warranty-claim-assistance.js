(function(){'use strict';
/* JAH The Warranty Claim Assistance Database generator — jahdb-warranty-claim-assistance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WCA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Warranty Claim Assistance: Core Vocabulary and Plain Definitions — foundations",
  "Warranty Claim Assistance: The Five-Minute Daily Practice — foundations",
  "Warranty Claim Assistance: Common Beginner Mistakes — foundations",
  "Warranty Claim Assistance: Setting Up Your First Workspace — foundations",
  "Warranty Claim Assistance: Reading Labels, Notices, and Fine Print — foundations",
  "Warranty Claim Assistance: Asking Better Questions — foundations",
  "Warranty Claim Assistance: Building a Simple Checklist — foundations",
  "Warranty Claim Assistance: Tracking What You Spend and Save — foundations",
  "Warranty Claim Assistance: Finding Free and Low-Cost Help — foundations",
  "Warranty Claim Assistance: Documenting Everything That Matters — foundations",
  "Warranty Claim Assistance: Knowing When to Get Expert Help — foundations",
  "Warranty Claim Assistance: Teaching It to Family and Kids — foundations"
 ],
 "compounded": [
  "Warranty Claim Assistance: Comparing Two Real Options — compounded",
  "Warranty Claim Assistance: Negotiating Without Conflict — compounded",
  "Warranty Claim Assistance: Planning Around Deadlines — compounded",
  "Warranty Claim Assistance: Handling Paperwork Efficiently — compounded",
  "Warranty Claim Assistance: Measuring Whether It Worked — compounded",
  "Warranty Claim Assistance: Building the Habit Loop — compounded",
  "Warranty Claim Assistance: What the Professionals Know — compounded",
  "Warranty Claim Assistance: Seasonal and Yearly Rhythms — compounded",
  "Warranty Claim Assistance: Digital Tools That Actually Help — compounded",
  "Warranty Claim Assistance: Avoiding Scams and Bad Actors — compounded",
  "Warranty Claim Assistance: When Things Go Wrong: Recovery — compounded",
  "Warranty Claim Assistance: Explaining It to Officials — compounded"
 ],
 "advanced": [
  "Warranty Claim Assistance: Advanced: Optimizing for Long-Term Value — advanced",
  "Warranty Claim Assistance: Advanced: Handling Edge Cases — advanced",
  "Warranty Claim Assistance: Advanced: Teaching and Mentoring Others — advanced",
  "Warranty Claim Assistance: Advanced: Auditing Your Own System — advanced",
  "Warranty Claim Assistance: Advanced: Building Redundancy — advanced",
  "Warranty Claim Assistance: Advanced: Community and Collective Action — advanced",
  "Warranty Claim Assistance: Advanced: Staying Current Over Decades — advanced",
  "Warranty Claim Assistance: Advanced: Designing Your Own Method — advanced",
  "Warranty Claim Assistance: Advanced: Crisis Playbook — advanced",
  "Warranty Claim Assistance: Advanced: Passing Knowledge to the Next Generation — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Warranty Claim Assistance Database — structural study\n"
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
var gen={version:'jahdb-warranty-claim-assistance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('warranty-claim-assistance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
