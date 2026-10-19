(function(){'use strict';
/* JAH The Practical Skills Assessment Database generator — jahdb-practical-skills-assessment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PSA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Practical Skills Assessment: Core Vocabulary and Plain Definitions — foundations",
  "Practical Skills Assessment: The Five-Minute Daily Practice — foundations",
  "Practical Skills Assessment: Common Beginner Mistakes — foundations",
  "Practical Skills Assessment: Setting Up Your First Workspace — foundations",
  "Practical Skills Assessment: Reading Labels, Notices, and Fine Print — foundations",
  "Practical Skills Assessment: Asking Better Questions — foundations",
  "Practical Skills Assessment: Building a Simple Checklist — foundations",
  "Practical Skills Assessment: Tracking What You Spend and Save — foundations",
  "Practical Skills Assessment: Finding Free and Low-Cost Help — foundations",
  "Practical Skills Assessment: Documenting Everything That Matters — foundations",
  "Practical Skills Assessment: Knowing When to Get Expert Help — foundations",
  "Practical Skills Assessment: Teaching It to Family and Kids — foundations"
 ],
 "compounded": [
  "Practical Skills Assessment: Comparing Two Real Options — compounded",
  "Practical Skills Assessment: Negotiating Without Conflict — compounded",
  "Practical Skills Assessment: Planning Around Deadlines — compounded",
  "Practical Skills Assessment: Handling Paperwork Efficiently — compounded",
  "Practical Skills Assessment: Measuring Whether It Worked — compounded",
  "Practical Skills Assessment: Building the Habit Loop — compounded",
  "Practical Skills Assessment: What the Professionals Know — compounded",
  "Practical Skills Assessment: Seasonal and Yearly Rhythms — compounded",
  "Practical Skills Assessment: Digital Tools That Actually Help — compounded",
  "Practical Skills Assessment: Avoiding Scams and Bad Actors — compounded",
  "Practical Skills Assessment: When Things Go Wrong: Recovery — compounded",
  "Practical Skills Assessment: Explaining It to Officials — compounded"
 ],
 "advanced": [
  "Practical Skills Assessment: Advanced: Optimizing for Long-Term Value — advanced",
  "Practical Skills Assessment: Advanced: Handling Edge Cases — advanced",
  "Practical Skills Assessment: Advanced: Teaching and Mentoring Others — advanced",
  "Practical Skills Assessment: Advanced: Auditing Your Own System — advanced",
  "Practical Skills Assessment: Advanced: Building Redundancy — advanced",
  "Practical Skills Assessment: Advanced: Community and Collective Action — advanced",
  "Practical Skills Assessment: Advanced: Staying Current Over Decades — advanced",
  "Practical Skills Assessment: Advanced: Designing Your Own Method — advanced",
  "Practical Skills Assessment: Advanced: Crisis Playbook — advanced",
  "Practical Skills Assessment: Advanced: Passing Knowledge to the Next Generation — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Practical Skills Assessment Database — structural study\n"
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
var gen={version:'jahdb-practical-skills-assessment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('practical-skills-assessment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
