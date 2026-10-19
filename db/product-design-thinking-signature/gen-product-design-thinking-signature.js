(function(){'use strict';
/* JAH Product Design Thinking Database generator — jahdb-product-design-thinking-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRODDTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Empathize (Signature Edition)", "Define (Signature Edition)", "Ideate (Signature Edition)", "Prototype (Signature Edition)", "Test (Signature Edition)", "User Interviews (Signature Edition)", "Journey Mapping (Signature Edition)", "Personas (Signature Edition)", "Wireframing (Signature Edition)", "Usability Testing (Signature Edition)", "Design Systems (Signature Edition)"], "Compounded": ["Accessibility in Design (Signature Edition)", "Design Critique (Signature Edition)", "Metrics (Signature Edition)", "Teaching Design Thinking (Signature Edition)", "The Design Review (Signature Edition)", "Research Methods (Signature Edition)", "Surveys (Signature Edition)", "Analytics (Signature Edition)", "A/B Testing (Signature Edition)", "Information Architecture (Signature Edition)", "Interaction Design (Signature Edition)", "Visual Design (Signature Edition)"], "Advanced": ["Typography (Signature Edition)", "Color Theory (Signature Edition)", "Motion Design (Signature Edition)", "Design for Mobile (Signature Edition)", "Design Ethics (Signature Edition)", "Design Documentation (Signature Edition)", "Stakeholder Management (Signature Edition)", "Design Leadership (Signature Edition)", "Freelance Design (Signature Edition)", "Design Education (Signature Edition)", "The Portfolio (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — design guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — design guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"product-design-thinking-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-product-design-thinking-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("product-design-thinking-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
