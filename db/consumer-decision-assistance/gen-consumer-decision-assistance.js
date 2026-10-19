(function(){'use strict';
/* JAH The Consumer Decision Assistance Database generator — jahdb-consumer-decision-assistance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CDA-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Consumer Decision Assistance: Core Vocabulary and Plain Definitions — foundations",
  "Consumer Decision Assistance: The Five-Minute Daily Practice — foundations",
  "Consumer Decision Assistance: Common Beginner Mistakes — foundations",
  "Consumer Decision Assistance: Setting Up Your First Workspace — foundations",
  "Consumer Decision Assistance: Reading Labels, Notices, and Fine Print — foundations",
  "Consumer Decision Assistance: Asking Better Questions — foundations",
  "Consumer Decision Assistance: Building a Simple Checklist — foundations",
  "Consumer Decision Assistance: Tracking What You Spend and Save — foundations",
  "Consumer Decision Assistance: Finding Free and Low-Cost Help — foundations",
  "Consumer Decision Assistance: Documenting Everything That Matters — foundations",
  "Consumer Decision Assistance: Knowing When to Get Expert Help — foundations",
  "Consumer Decision Assistance: Teaching It to Family and Kids — foundations"
 ],
 "compounded": [
  "Consumer Decision Assistance: Comparing Two Real Options — compounded",
  "Consumer Decision Assistance: Negotiating Without Conflict — compounded",
  "Consumer Decision Assistance: Planning Around Deadlines — compounded",
  "Consumer Decision Assistance: Handling Paperwork Efficiently — compounded",
  "Consumer Decision Assistance: Measuring Whether It Worked — compounded",
  "Consumer Decision Assistance: Building the Habit Loop — compounded",
  "Consumer Decision Assistance: What the Professionals Know — compounded",
  "Consumer Decision Assistance: Seasonal and Yearly Rhythms — compounded",
  "Consumer Decision Assistance: Digital Tools That Actually Help — compounded",
  "Consumer Decision Assistance: Avoiding Scams and Bad Actors — compounded",
  "Consumer Decision Assistance: When Things Go Wrong: Recovery — compounded",
  "Consumer Decision Assistance: Explaining It to Officials — compounded"
 ],
 "advanced": [
  "Consumer Decision Assistance: Advanced: Optimizing for Long-Term Value — advanced",
  "Consumer Decision Assistance: Advanced: Handling Edge Cases — advanced",
  "Consumer Decision Assistance: Advanced: Teaching and Mentoring Others — advanced",
  "Consumer Decision Assistance: Advanced: Auditing Your Own System — advanced",
  "Consumer Decision Assistance: Advanced: Building Redundancy — advanced",
  "Consumer Decision Assistance: Advanced: Community and Collective Action — advanced",
  "Consumer Decision Assistance: Advanced: Staying Current Over Decades — advanced",
  "Consumer Decision Assistance: Advanced: Designing Your Own Method — advanced",
  "Consumer Decision Assistance: Advanced: Crisis Playbook — advanced",
  "Consumer Decision Assistance: Advanced: Passing Knowledge to the Next Generation — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Consumer Decision Assistance Database — structural study\n"
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
var gen={version:'jahdb-consumer-decision-assistance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('consumer-decision-assistance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
