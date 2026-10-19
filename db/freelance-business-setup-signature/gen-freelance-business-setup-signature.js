(function(){'use strict';
/* JAH The Freelance Business Setup Signature Database generator — jahdb-freelance-business-setup-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FBSS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Freelance Business Setup (Signature): Mapping Your Real Skills — foundations",
  "Freelance Business Setup (Signature): Reading Job Postings Critically — foundations",
  "Freelance Business Setup (Signature): Resumes That Get Read — foundations",
  "Freelance Business Setup (Signature): Interview Preparation System — foundations",
  "Freelance Business Setup (Signature): Salary Research and Ranges — foundations",
  "Freelance Business Setup (Signature): Negotiating Offers — foundations",
  "Freelance Business Setup (Signature): Evaluating Benefits Deeply — foundations",
  "Freelance Business Setup (Signature): Onboarding: First 90 Days — foundations",
  "Freelance Business Setup (Signature): Performance Reviews That Help — foundations",
  "Freelance Business Setup (Signature): Asking for Raises and Promotions — foundations",
  "Freelance Business Setup (Signature): Changing Careers Safely — foundations",
  "Freelance Business Setup (Signature): Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Freelance Business Setup (Signature): Workplace Rights Basics — compounded",
  "Freelance Business Setup (Signature): Handling Difficult Bosses — compounded",
  "Freelance Business Setup (Signature): Work-Life Boundaries — compounded",
  "Freelance Business Setup (Signature): Building a Professional Network — compounded",
  "Freelance Business Setup (Signature): Personal Branding Honestly — compounded",
  "Freelance Business Setup (Signature): Remote Work Success — compounded",
  "Freelance Business Setup (Signature): Dealing With Job Loss — compounded",
  "Freelance Business Setup (Signature): References and Background Checks — compounded",
  "Freelance Business Setup (Signature): Contracts and Non-Competes — compounded",
  "Freelance Business Setup (Signature): Planning Parental and Medical Leave — compounded",
  "Freelance Business Setup (Signature): Advanced: Becoming the Expert — compounded",
  "Freelance Business Setup (Signature): Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Freelance Business Setup (Signature): Advanced: Negotiation Mastery — advanced",
  "Freelance Business Setup (Signature): Advanced: Building a Practice or Firm — advanced",
  "Freelance Business Setup (Signature): Advanced: Board and Advisory Roles — advanced",
  "Freelance Business Setup (Signature): Advanced: Career Portfolio Design — advanced",
  "Freelance Business Setup (Signature): Advanced: Mentoring the Next Generation — advanced",
  "Freelance Business Setup (Signature): Advanced: Navigating Politics — advanced",
  "Freelance Business Setup (Signature): Advanced: The Encore Career — advanced",
  "Freelance Business Setup (Signature): Advanced: Legacy at Work — advanced",
  "Freelance Business Setup (Signature): Advanced: When to Walk Away — advanced",
  "Freelance Business Setup (Signature): Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Freelance Business Setup Signature Database — structural study\n"
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
var gen={version:'jahdb-freelance-business-setup-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('freelance-business-setup-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
