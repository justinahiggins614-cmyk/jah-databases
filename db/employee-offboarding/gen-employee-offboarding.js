(function(){'use strict';
/* JAH The Employee Offboarding Database generator — jahdb-employee-offboarding-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EO-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Employee Offboarding: Mapping Your Real Skills — foundations",
  "Employee Offboarding: Reading Job Postings Critically — foundations",
  "Employee Offboarding: Resumes That Get Read — foundations",
  "Employee Offboarding: Interview Preparation System — foundations",
  "Employee Offboarding: Salary Research and Ranges — foundations",
  "Employee Offboarding: Negotiating Offers — foundations",
  "Employee Offboarding: Evaluating Benefits Deeply — foundations",
  "Employee Offboarding: Onboarding: First 90 Days — foundations",
  "Employee Offboarding: Performance Reviews That Help — foundations",
  "Employee Offboarding: Asking for Raises and Promotions — foundations",
  "Employee Offboarding: Changing Careers Safely — foundations",
  "Employee Offboarding: Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Employee Offboarding: Workplace Rights Basics — compounded",
  "Employee Offboarding: Handling Difficult Bosses — compounded",
  "Employee Offboarding: Work-Life Boundaries — compounded",
  "Employee Offboarding: Building a Professional Network — compounded",
  "Employee Offboarding: Personal Branding Honestly — compounded",
  "Employee Offboarding: Remote Work Success — compounded",
  "Employee Offboarding: Dealing With Job Loss — compounded",
  "Employee Offboarding: References and Background Checks — compounded",
  "Employee Offboarding: Contracts and Non-Competes — compounded",
  "Employee Offboarding: Planning Parental and Medical Leave — compounded",
  "Employee Offboarding: Advanced: Becoming the Expert — compounded",
  "Employee Offboarding: Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Employee Offboarding: Advanced: Negotiation Mastery — advanced",
  "Employee Offboarding: Advanced: Building a Practice or Firm — advanced",
  "Employee Offboarding: Advanced: Board and Advisory Roles — advanced",
  "Employee Offboarding: Advanced: Career Portfolio Design — advanced",
  "Employee Offboarding: Advanced: Mentoring the Next Generation — advanced",
  "Employee Offboarding: Advanced: Navigating Politics — advanced",
  "Employee Offboarding: Advanced: The Encore Career — advanced",
  "Employee Offboarding: Advanced: Legacy at Work — advanced",
  "Employee Offboarding: Advanced: When to Walk Away — advanced",
  "Employee Offboarding: Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Employee Offboarding Database — structural study\n"
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
var gen={version:'jahdb-employee-offboarding-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('employee-offboarding',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
