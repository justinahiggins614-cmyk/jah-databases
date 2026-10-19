(function(){'use strict';
/* JAH Childcare Assistance Directory Database generator — jahdb-childcare-assistance-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHILADS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Childcare Subsidies (Signature Edition)", "Head Start (Signature Edition)", "Early Head Start (Signature Edition)", "State Pre-K (Signature Edition)", "Choosing Quality Care (Signature Edition)", "Licensing Basics (Signature Edition)", "Center vs Home Care (Signature Edition)", "Interviewing Providers (Signature Edition)", "Red Flags (Signature Edition)", "Costs and Budgeting (Signature Edition)", "Backup Care Plans (Signature Edition)"], "Compounded": ["Special Needs Care (Signature Edition)", "Infant Care Specifics (Signature Edition)", "After-School Programs (Signature Edition)", "Summer Care (Signature Edition)", "Nanny and Au Pair Options (Signature Edition)", "Employer Childcare Benefits (Signature Edition)", "Tax Credits (Signature Edition)", "Advocacy for Quality (Signature Edition)", "The Annual Childcare Review (Signature Edition)", "Transitioning to School (Signature Edition)", "Finding Providers (Signature Edition)", "Subsidy Copays (Signature Edition)"], "Advanced": ["Waitlist Strategies (Signature Edition)", "Quality Rating Systems (Signature Edition)", "Family, Friend, and Neighbor Care (Signature Edition)", "Sick Child Care (Signature Edition)", "Kindergarten Readiness (Signature Edition)", "Childcare Deserts (Signature Edition)", "Night and Weekend Care (Signature Edition)", "Multiple Children (Signature Edition)", "Communicating With Providers (Signature Edition)", "When to Change Providers (Signature Edition)", "The Provider's Perspective (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — assistance directory demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — assistance directory',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A assistance directory of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"childcare-assistance-directory-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-childcare-assistance-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("childcare-assistance-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
