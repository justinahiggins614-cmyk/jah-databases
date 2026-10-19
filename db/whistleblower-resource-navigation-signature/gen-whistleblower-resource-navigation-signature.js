(function(){'use strict';
/* JAH The Whistleblower Resource Navigation Signature Database generator — jahdb-whistleblower-resource-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WRNS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Whistleblower Resource Navigation (Signature): Mapping Your Real Skills — foundations",
  "Whistleblower Resource Navigation (Signature): Reading Job Postings Critically — foundations",
  "Whistleblower Resource Navigation (Signature): Resumes That Get Read — foundations",
  "Whistleblower Resource Navigation (Signature): Interview Preparation System — foundations",
  "Whistleblower Resource Navigation (Signature): Salary Research and Ranges — foundations",
  "Whistleblower Resource Navigation (Signature): Negotiating Offers — foundations",
  "Whistleblower Resource Navigation (Signature): Evaluating Benefits Deeply — foundations",
  "Whistleblower Resource Navigation (Signature): Onboarding: First 90 Days — foundations",
  "Whistleblower Resource Navigation (Signature): Performance Reviews That Help — foundations",
  "Whistleblower Resource Navigation (Signature): Asking for Raises and Promotions — foundations",
  "Whistleblower Resource Navigation (Signature): Changing Careers Safely — foundations",
  "Whistleblower Resource Navigation (Signature): Freelance and Contract Realities — foundations"
 ],
 "compounded": [
  "Whistleblower Resource Navigation (Signature): Workplace Rights Basics — compounded",
  "Whistleblower Resource Navigation (Signature): Handling Difficult Bosses — compounded",
  "Whistleblower Resource Navigation (Signature): Work-Life Boundaries — compounded",
  "Whistleblower Resource Navigation (Signature): Building a Professional Network — compounded",
  "Whistleblower Resource Navigation (Signature): Personal Branding Honestly — compounded",
  "Whistleblower Resource Navigation (Signature): Remote Work Success — compounded",
  "Whistleblower Resource Navigation (Signature): Dealing With Job Loss — compounded",
  "Whistleblower Resource Navigation (Signature): References and Background Checks — compounded",
  "Whistleblower Resource Navigation (Signature): Contracts and Non-Competes — compounded",
  "Whistleblower Resource Navigation (Signature): Planning Parental and Medical Leave — compounded",
  "Whistleblower Resource Navigation (Signature): Advanced: Becoming the Expert — compounded",
  "Whistleblower Resource Navigation (Signature): Advanced: Leadership Transition — compounded"
 ],
 "advanced": [
  "Whistleblower Resource Navigation (Signature): Advanced: Negotiation Mastery — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Building a Practice or Firm — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Board and Advisory Roles — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Career Portfolio Design — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Mentoring the Next Generation — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Navigating Politics — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: The Encore Career — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Legacy at Work — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: When to Walk Away — advanced",
  "Whistleblower Resource Navigation (Signature): Advanced: Reinvention After Setbacks — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Whistleblower Resource Navigation Signature Database — structural study\n"
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
var gen={version:'jahdb-whistleblower-resource-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('whistleblower-resource-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
