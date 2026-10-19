(function(){'use strict';
/* JAH Assistive Technology Directory Database generator — jahdb-assistive-technology-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ASSITDS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Screen Readers (Signature Edition)", "Screen Magnification (Signature Edition)", "Hearing Aids (Signature Edition)", "Cochlear Implants (Signature Edition)", "Alerting Devices (Signature Edition)", "AAC Devices (Signature Edition)", "Mobility Aids (Signature Edition)", "Smart Home AT (Signature Edition)", "Funding Sources (Signature Edition)", "AT Evaluations (Signature Edition)", "Training (Signature Edition)"], "Compounded": ["Maintenance (Signature Edition)", "Emerging AT (Signature Edition)", "DIY and Maker AT (Signature Edition)", "Teaching AT (Signature Edition)", "The Annual AT Review (Signature Edition)", "Low-Tech AT (Signature Edition)", "Prosthetics (Signature Edition)", "Orthotics (Signature Edition)", "Vision Apps (Signature Edition)", "Hearing Loops (Signature Edition)", "Captioning Services (Signature Edition)", "Ergonomic Workstations (Signature Edition)"], "Advanced": ["Vehicle Modifications (Signature Edition)", "Recreation AT (Signature Edition)", "Smartphone Accessibility (Signature Edition)", "Computer Access (Signature Edition)", "Home Automation AT (Signature Edition)", "AT for Seniors (Signature Edition)", "AT Reuse Programs (Signature Edition)", "Advocacy for AT (Signature Edition)", "International AT (Signature Edition)", "The Caregiver AT Guide (Signature Edition)", "Future AT (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — technology directory demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — technology directory',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology directory of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"assistive-technology-directory-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-assistive-technology-directory-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("assistive-technology-directory-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
