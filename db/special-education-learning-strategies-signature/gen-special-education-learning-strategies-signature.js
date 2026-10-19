(function(){'use strict';
/* JAH Special Education Learning Strategies Database generator — jahdb-special-education-learning-strategies-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPECELSS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Understanding the IEP (Signature Edition)", "504 Plans Explained (Signature Edition)", "Evaluation Rights (Signature Edition)", "Multisensory Learning (Signature Edition)", "Breaking Down Tasks (Signature Edition)", "Assistive Technology (Signature Edition)", "Reading Interventions (Signature Edition)", "Math Strategies (Signature Edition)", "Behavior Supports (Signature Edition)", "Executive Function Help (Signature Edition)", "Social Skills Teaching (Signature Edition)"], "Compounded": ["Communication Supports (Signature Edition)", "Sensory Needs (Signature Edition)", "Partnering With Teachers (Signature Edition)", "Homework Strategies (Signature Edition)", "Testing Accommodations (Signature Edition)", "Transition Planning (Signature Edition)", "Self-Advocacy Skills (Signature Edition)", "Inclusion That Works (Signature Edition)", "Data and Progress Monitoring (Signature Edition)", "Dispute Resolution (Signature Edition)", "The Annual Review Meeting (Signature Edition)", "Summer and Breaks (Signature Edition)"], "Advanced": ["Sibling Considerations (Signature Edition)", "Cultural Responsiveness (Signature Edition)", "Teacher Self-Care (Signature Edition)", "Technology Trends (Signature Edition)", "Post-School Outcomes (Signature Edition)", "Building the Support Team (Signature Edition)", "Celebrating Growth (Signature Edition)", "Home-School Communication (Signature Edition)", "Assistive Tech Funding (Signature Edition)", "College Preparation (Signature Edition)", "Employment Preparation (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — learning guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — learning guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A learning guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"special-education-learning-strategies-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-special-education-learning-strategies-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("special-education-learning-strategies-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
