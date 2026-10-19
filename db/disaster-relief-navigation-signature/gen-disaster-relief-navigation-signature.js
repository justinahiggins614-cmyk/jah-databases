(function(){'use strict';
/* JAH Disaster Relief Navigation Database generator — jahdb-disaster-relief-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DISARNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Immediate Safety (Signature Edition)", "Documenting Damage (Signature Edition)", "FEMA Assistance (Signature Edition)", "FEMA Inspection (Signature Edition)", "Appealing FEMA Decisions (Signature Edition)", "Insurance Claims (Signature Edition)", "Flood Insurance Specifics (Signature Edition)", "SBA Disaster Loans (Signature Edition)", "Temporary Housing (Signature Edition)", "Cleanup Safety (Signature Edition)", "Mold Remediation (Signature Edition)"], "Compounded": ["Contractor Selection (Signature Edition)", "Disaster Scams (Signature Edition)", "Replacing Documents (Signature Edition)", "Emotional Recovery (Signature Edition)", "Helping Neighbors (Signature Edition)", "Business Recovery (Signature Edition)", "Farm Recovery (Signature Edition)", "Long-Term Rebuilding (Signature Edition)", "Mitigation for Next Time (Signature Edition)", "Teaching Preparedness (Signature Edition)", "The Annual Readiness Review (Signature Edition)", "Replacing Vehicles (Signature Edition)"], "Advanced": ["Temporary Schools (Signature Edition)", "Pet Recovery (Signature Edition)", "Historic Property Recovery (Signature Edition)", "Disability in Disasters (Signature Edition)", "Language Access (Signature Edition)", "Renters and Disasters (Signature Edition)", "Manufactured Homes (Signature Edition)", "The Recovery Timeline (Signature Edition)", "Community Resilience (Signature Edition)", "After-Action Review (Signature Edition)", "Helping Future Survivors (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — relief guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — relief guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A relief guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"disaster-relief-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-disaster-relief-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("disaster-relief-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
