(function(){'use strict';
/* JAH Public Feedback Analysis Database generator — jahdb-public-feedback-analysis-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PUBLFAS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Feedback Channels (Signature Edition)", "Survey Design (Signature Edition)", "Review Analysis (Signature Edition)", "Sentiment Basics (Signature Edition)", "Thematic Coding (Signature Edition)", "Representativeness (Signature Edition)", "Acting on Feedback (Signature Edition)", "Negative Feedback (Signature Edition)", "Closing the Loop (Signature Edition)", "Feedback Tools (Signature Edition)", "Teaching Feedback Literacy (Signature Edition)"], "Compounded": ["The Feedback Audit (Signature Edition)", "Comment Moderation (Signature Edition)", "Social Listening (Signature Edition)", "Focus Groups (Signature Edition)", "Interviews (Signature Edition)", "Town Halls (Signature Edition)", "Advisory Boards (Signature Edition)", "Participatory Budgeting (Signature Edition)", "Deliberative Polling (Signature Edition)", "Feedback Biases (Signature Edition)", "Quantitative Analysis (Signature Edition)", "Qualitative Analysis (Signature Edition)"], "Advanced": ["Reporting Findings (Signature Edition)", "Crisis Feedback (Signature Edition)", "Employee Feedback (Signature Edition)", "Customer Advisory (Signature Edition)", "Government Consultation (Signature Edition)", "Nonprofit Listening (Signature Edition)", "Metrics That Matter (Signature Edition)", "Feedback Culture (Signature Edition)", "Technology Trends (Signature Edition)", "The Listening Organization (Signature Edition)", "Feedback Ethics (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — feedback guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — feedback guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A feedback guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"public-feedback-analysis-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-public-feedback-analysis-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("public-feedback-analysis-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
