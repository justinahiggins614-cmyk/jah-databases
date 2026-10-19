(function(){'use strict';
/* JAH The Employee Offboarding Signature Database generator — jahdb-employee-offboarding-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EOS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Employee Offboarding (Signature): Mapping Your Real Skills — foundations",
  "Employee Offboarding (Signature): Reading Job Postings Critically — foundations",
  "Employee Offboarding (Signature): Resumes That Get Read — foundations",
  "Employee Offboarding (Signature): Interview Preparation System — foundations",
  "Employee Offboarding (Signature): Salary Research and Ranges — foundations",
  "Employee Offboarding (Signature): Negotiating Offers — foundations",
  "Employee Offboarding (Signature): Evaluating Benefits Deeply — foundations",
  "Employee Offboarding (Signature): Onboarding: First 90 Days — foundations",
  "Employee Offboarding (Signature): Performance Reviews That Help — foundations",
  "Employee Offboarding (Signature): Asking for Raises and Promotions — foundations",
  "Employee Offboarding (Signature): Changing Careers Safely — foundations",
  "Employee Offboarding (Signature): Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Employee Offboarding (Signature): Workplace Rights Basics — compounded",
  "Employee Offboarding (Signature): Handling Difficult Bosses — compounded",
  "Employee Offboarding (Signature): Work-Life Boundaries — compounded",
  "Employee Offboarding (Signature): Building a Professional Network — compounded",
  "Employee Offboarding (Signature): Personal Branding Honestly — compounded",
  "Employee Offboarding (Signature): Remote Work Success — compounded",
  "Employee Offboarding (Signature): Dealing With Job Loss — compounded",
  "Employee Offboarding (Signature): References and Background Checks — compounded",
  "Employee Offboarding (Signature): Contracts and Non-Competes — compounded",
  "Employee Offboarding (Signature): Planning Parental and Medical Leave — compounded",
  "Employee Offboarding (Signature): Advanced: Becoming the Expert — compounded",
  "Employee Offboarding (Signature): Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Employee Offboarding (Signature): Advanced: Negotiation Mastery — advanced",
  "Employee Offboarding (Signature): Advanced: Building a Practice or Firm — advanced",
  "Employee Offboarding (Signature): Advanced: Board and Advisory Roles — advanced",
  "Employee Offboarding (Signature): Advanced: Career Portfolio Design — advanced",
  "Employee Offboarding (Signature): Advanced: Mentoring the Next Generation — advanced",
  "Employee Offboarding (Signature): Advanced: Navigating Politics — advanced",
  "Employee Offboarding (Signature): Advanced: The Encore Career — advanced",
  "Employee Offboarding (Signature): Advanced: Legacy at Work — advanced",
  "Employee Offboarding (Signature): Advanced: When to Walk Away — advanced",
  "Employee Offboarding (Signature): Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Employee Offboarding Signature Database — structural study\n"
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
var gen={version:'jahdb-employee-offboarding-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('employee-offboarding-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
