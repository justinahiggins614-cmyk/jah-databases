(function(){'use strict';
/* JAH The Occupation Requirements Database generator — jahdb-occupation-requirements-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OR-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Occupation Requirements: Mapping Your Real Skills — foundations",
  "Occupation Requirements: Reading Job Postings Critically — foundations",
  "Occupation Requirements: Resumes That Get Read — foundations",
  "Occupation Requirements: Interview Preparation System — foundations",
  "Occupation Requirements: Salary Research and Ranges — foundations",
  "Occupation Requirements: Negotiating Offers — foundations",
  "Occupation Requirements: Evaluating Benefits Deeply — foundations",
  "Occupation Requirements: Onboarding: First 90 Days — foundations",
  "Occupation Requirements: Performance Reviews That Help — foundations",
  "Occupation Requirements: Asking for Raises and Promotions — foundations",
  "Occupation Requirements: Changing Careers Safely — foundations",
  "Occupation Requirements: Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Occupation Requirements: Workplace Rights Basics — compounded",
  "Occupation Requirements: Handling Difficult Bosses — compounded",
  "Occupation Requirements: Work-Life Boundaries — compounded",
  "Occupation Requirements: Building a Professional Network — compounded",
  "Occupation Requirements: Personal Branding Honestly — compounded",
  "Occupation Requirements: Remote Work Success — compounded",
  "Occupation Requirements: Dealing With Job Loss — compounded",
  "Occupation Requirements: References and Background Checks — compounded",
  "Occupation Requirements: Contracts and Non-Competes — compounded",
  "Occupation Requirements: Planning Parental and Medical Leave — compounded",
  "Occupation Requirements: Advanced: Becoming the Expert — compounded",
  "Occupation Requirements: Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Occupation Requirements: Advanced: Negotiation Mastery — advanced",
  "Occupation Requirements: Advanced: Building a Practice or Firm — advanced",
  "Occupation Requirements: Advanced: Board and Advisory Roles — advanced",
  "Occupation Requirements: Advanced: Career Portfolio Design — advanced",
  "Occupation Requirements: Advanced: Mentoring the Next Generation — advanced",
  "Occupation Requirements: Advanced: Navigating Politics — advanced",
  "Occupation Requirements: Advanced: The Encore Career — advanced",
  "Occupation Requirements: Advanced: Legacy at Work — advanced",
  "Occupation Requirements: Advanced: When to Walk Away — advanced",
  "Occupation Requirements: Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Occupation Requirements Database — structural study\n"
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
var gen={version:'jahdb-occupation-requirements-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('occupation-requirements',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
