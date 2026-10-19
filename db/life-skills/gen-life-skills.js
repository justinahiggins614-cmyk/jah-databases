(function(){'use strict';
/* JAH The Life Skills Database generator — jahdb-life-skills-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Life Skills: Core Vocabulary and Plain Definitions — foundations",
  "Life Skills: The Five-Minute Daily Practice — foundations",
  "Life Skills: Common Beginner Mistakes — foundations",
  "Life Skills: Setting Up Your First Workspace — foundations",
  "Life Skills: Reading Labels, Notices, and Fine Print — foundations",
  "Life Skills: Asking Better Questions — foundations",
  "Life Skills: Building a Simple Checklist — foundations",
  "Life Skills: Tracking What You Spend and Save — foundations",
  "Life Skills: Finding Free and Low-Cost Help — foundations",
  "Life Skills: Documenting Everything That Matters — foundations",
  "Life Skills: Knowing When to Get Expert Help — foundations",
  "Life Skills: Teaching It to Family and Kids — foundations"
 ],
 "compounded": [
  "Life Skills: Comparing Two Real Options — compounded",
  "Life Skills: Negotiating Without Conflict — compounded",
  "Life Skills: Planning Around Deadlines — compounded",
  "Life Skills: Handling Paperwork Efficiently — compounded",
  "Life Skills: Measuring Whether It Worked — compounded",
  "Life Skills: Building the Habit Loop — compounded",
  "Life Skills: What the Professionals Know — compounded",
  "Life Skills: Seasonal and Yearly Rhythms — compounded",
  "Life Skills: Digital Tools That Actually Help — compounded",
  "Life Skills: Avoiding Scams and Bad Actors — compounded",
  "Life Skills: When Things Go Wrong: Recovery — compounded",
  "Life Skills: Explaining It to Officials — compounded"
 ],
 "advanced": [
  "Life Skills: Advanced: Optimizing for Long-Term Value — advanced",
  "Life Skills: Advanced: Handling Edge Cases — advanced",
  "Life Skills: Advanced: Teaching and Mentoring Others — advanced",
  "Life Skills: Advanced: Auditing Your Own System — advanced",
  "Life Skills: Advanced: Building Redundancy — advanced",
  "Life Skills: Advanced: Community and Collective Action — advanced",
  "Life Skills: Advanced: Staying Current Over Decades — advanced",
  "Life Skills: Advanced: Designing Your Own Method — advanced",
  "Life Skills: Advanced: Crisis Playbook — advanced",
  "Life Skills: Advanced: Passing Knowledge to the Next Generation — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Life Skills Database — structural study\n"
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
var gen={version:'jahdb-life-skills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('life-skills',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
