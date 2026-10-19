(function(){'use strict';
/* JAH The Eligibility Finder Database generator — jahdb-eligibility-finder-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EF-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Eligibility Finder: Core Vocabulary and Plain Definitions — foundations",
  "Eligibility Finder: The Five-Minute Daily Practice — foundations",
  "Eligibility Finder: Common Beginner Mistakes — foundations",
  "Eligibility Finder: Setting Up Your First Workspace — foundations",
  "Eligibility Finder: Reading Labels, Notices, and Fine Print — foundations",
  "Eligibility Finder: Asking Better Questions — foundations",
  "Eligibility Finder: Building a Simple Checklist — foundations",
  "Eligibility Finder: Tracking What You Spend and Save — foundations",
  "Eligibility Finder: Finding Free and Low-Cost Help — foundations",
  "Eligibility Finder: Documenting Everything That Matters — foundations",
  "Eligibility Finder: Knowing When to Get Expert Help — foundations",
  "Eligibility Finder: Teaching It to Family and Kids — foundations"
 ],
 "compounded": [
  "Eligibility Finder: Comparing Two Real Options — compounded",
  "Eligibility Finder: Negotiating Without Conflict — compounded",
  "Eligibility Finder: Planning Around Deadlines — compounded",
  "Eligibility Finder: Handling Paperwork Efficiently — compounded",
  "Eligibility Finder: Measuring Whether It Worked — compounded",
  "Eligibility Finder: Building the Habit Loop — compounded",
  "Eligibility Finder: What the Professionals Know — compounded",
  "Eligibility Finder: Seasonal and Yearly Rhythms — compounded",
  "Eligibility Finder: Digital Tools That Actually Help — compounded",
  "Eligibility Finder: Avoiding Scams and Bad Actors — compounded",
  "Eligibility Finder: When Things Go Wrong: Recovery — compounded",
  "Eligibility Finder: Explaining It to Officials — compounded"
 ],
 "advanced": [
  "Eligibility Finder: Advanced: Optimizing for Long-Term Value — advanced",
  "Eligibility Finder: Advanced: Handling Edge Cases — advanced",
  "Eligibility Finder: Advanced: Teaching and Mentoring Others — advanced",
  "Eligibility Finder: Advanced: Auditing Your Own System — advanced",
  "Eligibility Finder: Advanced: Building Redundancy — advanced",
  "Eligibility Finder: Advanced: Community and Collective Action — advanced",
  "Eligibility Finder: Advanced: Staying Current Over Decades — advanced",
  "Eligibility Finder: Advanced: Designing Your Own Method — advanced",
  "Eligibility Finder: Advanced: Crisis Playbook — advanced",
  "Eligibility Finder: Advanced: Passing Knowledge to the Next Generation — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Eligibility Finder Database — structural study\n"
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
var gen={version:'jahdb-eligibility-finder-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('eligibility-finder',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
