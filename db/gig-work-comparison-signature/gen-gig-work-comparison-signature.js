(function(){'use strict';
/* JAH Gig Work Comparison Database generator — jahdb-gig-work-comparison-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GIGWCS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["True Hourly Rate Math (Signature Edition)", "Rideshare Realities (Signature Edition)", "Delivery Platforms (Signature Edition)", "Freelance Platforms (Signature Edition)", "Task and Handyman Gigs (Signature Edition)", "Vehicle Cost Accounting (Signature Edition)", "Gig Taxes (Signature Edition)", "Multi-App Strategy (Signature Edition)", "Peak Hour Optimization (Signature Edition)", "Safety Practices (Signature Edition)", "Insurance Gaps (Signature Edition)"], "Compounded": ["Choosing Your Vehicle (Signature Edition)", "Gig Goals and Fit (Signature Edition)", "Burnout Prevention (Signature Edition)", "Customer Ratings Game (Signature Edition)", "Expense Tracking Systems (Signature Edition)", "Health Insurance Options (Signature Edition)", "Retirement for Gig Workers (Signature Edition)", "Scaling Beyond Solo (Signature Edition)", "Platform Dependence Risk (Signature Edition)", "Seasonal Gig Patterns (Signature Edition)", "Dispute Resolution (Signature Edition)", "Gig Work and Benefits (Signature Edition)"], "Advanced": ["Teaching Gig Literacy (Signature Edition)", "The Annual Gig Review (Signature Edition)", "Niche Gig Opportunities (Signature Edition)", "Gig Work Abroad (Signature Edition)", "Exit Planning (Signature Edition)", "Community and Advocacy (Signature Edition)", "Record-Keeping for Audits (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — gig guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — gig guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A gig guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"gig-work-comparison-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-gig-work-comparison-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gig-work-comparison-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
