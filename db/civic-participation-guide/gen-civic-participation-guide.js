(function(){'use strict';
/* JAH The Civic Participation Guide Database generator — jahdb-civic-participation-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPG-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Civic Participation Guide: The Law in Plain Words — foundations",
  "Civic Participation Guide: Your Rights, Stated Simply — foundations",
  "Civic Participation Guide: Forms: Which Ones and How — foundations",
  "Civic Participation Guide: Deadlines That Decide Cases — foundations",
  "Civic Participation Guide: Evidence and Documentation — foundations",
  "Civic Participation Guide: Filing and Fees — foundations",
  "Civic Participation Guide: What Happens at Each Stage — foundations",
  "Civic Participation Guide: Representing Yourself: Basics — foundations",
  "Civic Participation Guide: When You Must Hire a Lawyer — foundations",
  "Civic Participation Guide: Free and Low-Cost Legal Help — foundations",
  "Civic Participation Guide: Common Mistakes That Lose Cases — foundations",
  "Civic Participation Guide: Negotiation and Settlement — foundations"
 ],
 "compounded": [
  "Civic Participation Guide: Appeals and Second Chances — compounded",
  "Civic Participation Guide: Records, Background, and Privacy — compounded",
  "Civic Participation Guide: Dealing With Agencies — compounded",
  "Civic Participation Guide: Mediation and Alternatives — compounded",
  "Civic Participation Guide: Costs: Real Numbers — compounded",
  "Civic Participation Guide: Timelines: How Long It Takes — compounded",
  "Civic Participation Guide: Protecting Yourself Going Forward — compounded",
  "Civic Participation Guide: Helping Others Navigate This — compounded",
  "Civic Participation Guide: Language Access Rights — compounded",
  "Civic Participation Guide: Digital Filing and Remote Hearings — compounded",
  "Civic Participation Guide: Advanced: Reading Statutes — compounded",
  "Civic Participation Guide: Advanced: Case Law Basics — compounded"
 ],
 "advanced": [
  "Civic Participation Guide: Advanced: Building a Case File — advanced",
  "Civic Participation Guide: Advanced: Expert Witnesses — advanced",
  "Civic Participation Guide: Advanced: Class and Collective Action — advanced",
  "Civic Participation Guide: Advanced: Cross-Jurisdiction Issues — advanced",
  "Civic Participation Guide: Advanced: Legislative Change Tracking — advanced",
  "Civic Participation Guide: Advanced: Teaching Legal Literacy — advanced",
  "Civic Participation Guide: Advanced: Systemic Advocacy — advanced",
  "Civic Participation Guide: Advanced: Ethics for Non-Lawyers Helping — advanced",
  "Civic Participation Guide: Advanced: Building Precedent — advanced",
  "Civic Participation Guide: Advanced: Restorative Approaches — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Civic Participation Guide Database — structural study\n"
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
var gen={version:'jahdb-civic-participation-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('civic-participation-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
