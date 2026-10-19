(function(){'use strict';
/* JAH Court Form Navigation Database generator — jahdb-court-form-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COURFNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Finding the Right Forms (Signature Edition)", "Small Claims Basics (Signature Edition)", "Filling Forms Accurately (Signature Edition)", "Filing With the Clerk (Signature Edition)", "Fee Waivers (Signature Edition)", "Serving the Other Side (Signature Edition)", "Deadlines That Matter (Signature Edition)", "Responding to Lawsuits (Signature Edition)", "Preparing for Hearings (Signature Edition)", "Evidence Basics (Signature Edition)", "Family Court Forms (Signature Edition)"], "Compounded": ["Housing Court Forms (Signature Edition)", "Name Change Petitions (Signature Edition)", "Restraining Orders (Signature Edition)", "Probate Forms (Signature Edition)", "Traffic Court (Signature Edition)", "Appealing Decisions (Signature Edition)", "Mediation Alternatives (Signature Edition)", "Working With Clerks (Signature Edition)", "Legal Aid Options (Signature Edition)", "Representing Yourself (Signature Edition)", "Courtroom Behavior (Signature Edition)", "Judgments and Collection (Signature Edition)"], "Advanced": ["Expungement Forms (Signature Edition)", "Guardianship Forms (Signature Edition)", "Small Business Court Needs (Signature Edition)", "Document Organization (Signature Edition)", "After the Case (Signature Edition)", "Teaching Court Literacy (Signature Edition)", "The Annual Legal Checkup (Signature Edition)", "E-Filing Systems (Signature Edition)", "Subpoenas (Signature Edition)", "Settlements (Signature Edition)", "Legal Research Basics (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — court guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — court guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A court guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"court-form-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-court-form-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("court-form-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
