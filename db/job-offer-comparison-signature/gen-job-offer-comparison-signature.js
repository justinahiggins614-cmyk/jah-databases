(function(){'use strict';
/* JAH The Job Offer Comparison Signature Database generator — jahdb-job-offer-comparison-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JOCS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Job Offer Comparison (Signature): Mapping Your Real Skills — foundations",
  "Job Offer Comparison (Signature): Reading Job Postings Critically — foundations",
  "Job Offer Comparison (Signature): Resumes That Get Read — foundations",
  "Job Offer Comparison (Signature): Interview Preparation System — foundations",
  "Job Offer Comparison (Signature): Salary Research and Ranges — foundations",
  "Job Offer Comparison (Signature): Negotiating Offers — foundations",
  "Job Offer Comparison (Signature): Evaluating Benefits Deeply — foundations",
  "Job Offer Comparison (Signature): Onboarding: First 90 Days — foundations",
  "Job Offer Comparison (Signature): Performance Reviews That Help — foundations",
  "Job Offer Comparison (Signature): Asking for Raises and Promotions — foundations",
  "Job Offer Comparison (Signature): Changing Careers Safely — foundations",
  "Job Offer Comparison (Signature): Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Job Offer Comparison (Signature): Workplace Rights Basics — compounded",
  "Job Offer Comparison (Signature): Handling Difficult Bosses — compounded",
  "Job Offer Comparison (Signature): Work-Life Boundaries — compounded",
  "Job Offer Comparison (Signature): Building a Professional Network — compounded",
  "Job Offer Comparison (Signature): Personal Branding Honestly — compounded",
  "Job Offer Comparison (Signature): Remote Work Success — compounded",
  "Job Offer Comparison (Signature): Dealing With Job Loss — compounded",
  "Job Offer Comparison (Signature): References and Background Checks — compounded",
  "Job Offer Comparison (Signature): Contracts and Non-Competes — compounded",
  "Job Offer Comparison (Signature): Planning Parental and Medical Leave — compounded",
  "Job Offer Comparison (Signature): Advanced: Becoming the Expert — compounded",
  "Job Offer Comparison (Signature): Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Job Offer Comparison (Signature): Advanced: Negotiation Mastery — advanced",
  "Job Offer Comparison (Signature): Advanced: Building a Practice or Firm — advanced",
  "Job Offer Comparison (Signature): Advanced: Board and Advisory Roles — advanced",
  "Job Offer Comparison (Signature): Advanced: Career Portfolio Design — advanced",
  "Job Offer Comparison (Signature): Advanced: Mentoring the Next Generation — advanced",
  "Job Offer Comparison (Signature): Advanced: Navigating Politics — advanced",
  "Job Offer Comparison (Signature): Advanced: The Encore Career — advanced",
  "Job Offer Comparison (Signature): Advanced: Legacy at Work — advanced",
  "Job Offer Comparison (Signature): Advanced: When to Walk Away — advanced",
  "Job Offer Comparison (Signature): Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Job Offer Comparison Signature Database — structural study\n"
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
var gen={version:'jahdb-job-offer-comparison-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('job-offer-comparison-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
