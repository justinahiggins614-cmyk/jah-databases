(function(){'use strict';
/* JAH The Field Modification and Retrofit Records Database generator — jahdb-field-modification-retrofit-records-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FMRR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Documenting a Field Modification - Safety & Compliance",
  "Guard Addition to Exposed Belt Drive - Mechanical Modifications",
  "Emergency Stop Addition - Electrical Modifications",
  "Lighting Upgrade in a Work Area - Electrical Modifications",
  "Labeling and Placard Retrofit - Safety & Compliance",
  "Vibration Isolation Pad Retrofit - Mechanical Modifications",
  "Drip Tray Addition Under Hydraulics - Mechanical Modifications",
  "Cord and Plug Strain Relief - Electrical Modifications",
  "Setpoint Limit Adjustment - Control & Software Modifications",
  "Alarm Addition to Existing Panel - Control & Software Modifications"
 ],
 "Compounded": [
  "Variable Speed Drive Retrofit - Electrical Modifications",
  "Pneumatic to Electric Actuator Swap - Mechanical Modifications",
  "Bearing Upgrade to Sealed Type - Mechanical Modifications",
  "PLC I/O Expansion in the Field - Control & Software Modifications",
  "HMI Replacement Retrofit - Control & Software Modifications",
  "Motor Efficiency Upgrade - Electrical Modifications",
  "Dust Collection Retrofit - Mechanical Modifications",
  "Noise Reduction Enclosure Retrofit - Mechanical Modifications",
  "Safety Relay Retrofit - Safety & Compliance",
  "Lockout/Tagout Station Addition - Safety & Compliance",
  "Firmware Update in the Field - Control & Software Modifications",
  "Sensor Upgrade Retrofit - Control & Software Modifications"
 ],
 "Advanced": [
  "Structural Reinforcement for Added Load - Mechanical Modifications",
  "Hazardous-Area Reclassification Retrofit - Safety & Compliance",
  "Functional Safety Upgrade to PLd - Safety & Compliance",
  "Legacy Control System Migration - Control & Software Modifications",
  "Pressure Vessel Alteration Record - Mechanical Modifications",
  "Electrical Service Capacity Increase - Electrical Modifications",
  "Seismic Restraint Retrofit - Mechanical Modifications",
  "Fire Suppression System Retrofit - Safety & Compliance",
  "Energy Metering Retrofit - Electrical Modifications",
  "Cybersecurity Hardening Retrofit - Control & Software Modifications",
  "Modification Reversal Procedure - Safety & Compliance",
  "Fleet-Wide Modification Rollout - Safety & Compliance"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Field Modification Retrofit Records — "+safe+"\n"
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
    name:topic+' — field modification record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A field modification record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-field-modification-retrofit-records-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('field-modification-retrofit-records',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
