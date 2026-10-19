(function(){'use strict';
/* JAH Freelancer Business Setup Database generator — jahdb-freelancer-business-setup-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FREEBSS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Choosing Your Niche (Signature Edition)", "Defining Your Offer (Signature Edition)", "Freelance Pricing (Signature Edition)", "Hourly vs Project Pricing (Signature Edition)", "Raising Rates (Signature Edition)", "Contracts That Protect (Signature Edition)", "Deposits and Payment Terms (Signature Edition)", "Invoicing Systems (Signature Edition)", "Finding First Clients (Signature Edition)", "Ongoing Client Acquisition (Signature Edition)", "Freelance Platforms (Signature Edition)"], "Compounded": ["Proposals That Win (Signature Edition)", "Discovery Calls (Signature Edition)", "Onboarding Clients (Signature Edition)", "Managing Projects (Signature Edition)", "Handling Revisions (Signature Edition)", "Difficult Clients (Signature Edition)", "Freelancer Taxes (Signature Edition)", "Retirement for Freelancers (Signature Edition)", "Health Insurance (Signature Edition)", "Time Management (Signature Edition)", "Home Office Setup (Signature Edition)", "Building a Portfolio (Signature Edition)"], "Advanced": ["Testimonials and Reviews (Signature Edition)", "Networking for Freelancers (Signature Edition)", "Scaling Beyond Solo (Signature Edition)", "Legal Structure for Freelancers (Signature Edition)", "Insurance for Freelancers (Signature Edition)", "Work-Life Boundaries (Signature Edition)", "Dry Spells (Signature Edition)", "Teaching Freelancing (Signature Edition)", "The Annual Freelance Review (Signature Edition)", "Personal Branding (Signature Edition)", "Freelance Communities (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — freelancer guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — freelancer guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A freelancer guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"freelancer-business-setup-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-freelancer-business-setup-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("freelancer-business-setup-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
