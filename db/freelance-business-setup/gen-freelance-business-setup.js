(function(){'use strict';
/* JAH The Freelance Business Setup Database generator — jahdb-freelance-business-setup-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FBS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Freelance Business Setup: Mapping Your Real Skills — foundations",
  "Freelance Business Setup: Reading Job Postings Critically — foundations",
  "Freelance Business Setup: Resumes That Get Read — foundations",
  "Freelance Business Setup: Interview Preparation System — foundations",
  "Freelance Business Setup: Salary Research and Ranges — foundations",
  "Freelance Business Setup: Negotiating Offers — foundations",
  "Freelance Business Setup: Evaluating Benefits Deeply — foundations",
  "Freelance Business Setup: Onboarding: First 90 Days — foundations",
  "Freelance Business Setup: Performance Reviews That Help — foundations",
  "Freelance Business Setup: Asking for Raises and Promotions — foundations",
  "Freelance Business Setup: Changing Careers Safely — foundations",
  "Freelance Business Setup: Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Freelance Business Setup: Workplace Rights Basics — compounded",
  "Freelance Business Setup: Handling Difficult Bosses — compounded",
  "Freelance Business Setup: Work-Life Boundaries — compounded",
  "Freelance Business Setup: Building a Professional Network — compounded",
  "Freelance Business Setup: Personal Branding Honestly — compounded",
  "Freelance Business Setup: Remote Work Success — compounded",
  "Freelance Business Setup: Dealing With Job Loss — compounded",
  "Freelance Business Setup: References and Background Checks — compounded",
  "Freelance Business Setup: Contracts and Non-Competes — compounded",
  "Freelance Business Setup: Planning Parental and Medical Leave — compounded",
  "Freelance Business Setup: Advanced: Becoming the Expert — compounded",
  "Freelance Business Setup: Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Freelance Business Setup: Advanced: Negotiation Mastery — advanced",
  "Freelance Business Setup: Advanced: Building a Practice or Firm — advanced",
  "Freelance Business Setup: Advanced: Board and Advisory Roles — advanced",
  "Freelance Business Setup: Advanced: Career Portfolio Design — advanced",
  "Freelance Business Setup: Advanced: Mentoring the Next Generation — advanced",
  "Freelance Business Setup: Advanced: Navigating Politics — advanced",
  "Freelance Business Setup: Advanced: The Encore Career — advanced",
  "Freelance Business Setup: Advanced: Legacy at Work — advanced",
  "Freelance Business Setup: Advanced: When to Walk Away — advanced",
  "Freelance Business Setup: Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Freelance Business Setup Database — structural study\n"
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
var gen={version:'jahdb-freelance-business-setup-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('freelance-business-setup',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
