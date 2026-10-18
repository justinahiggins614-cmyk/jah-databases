(function(){'use strict';
/* JAH The Emergency Medicine Database generator — jahdb-emergency-medicine-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMED-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Emergency Medicine Is",
  "When to Call Emergency Services",
  "The Emergency Call and Dispatch",
  "Emergency Medical Services Levels",
  "The Emergency Department Team",
  "Triage Basics",
  "Patient Assessment in the Field",
  "Ambulance Equipment",
  "Communication During Emergencies",
  "Patient Rights in Emergencies (EMTALA)",
  "After the Emergency: Follow-up Care"
 ],
 "Compounded": [
  "Dispatch Operations and Protocols",
  "Triage Systems: ESI and START",
  "Ambulance Operations and Fleet",
  "Air Medical Transport",
  "Cardiac Emergency Protocols",
  "Stroke Recognition and Response",
  "Trauma Care Systems",
  "Pediatric Emergency Protocols",
  "Behavioral Health Emergencies",
  "Mass Casualty Incident Response",
  "Hazardous Materials Response",
  "Continuity of Care and Handoffs"
 ],
 "Advanced": [
  "Emergency Department Operations",
  "Crowding and Patient Flow",
  "Telemedicine in Emergency Care",
  "Community Paramedicine",
  "Disaster Medical Response Teams",
  "Emergency Preparedness Planning",
  "Quality Metrics in Emergency Care",
  "Resuscitation Science Updates",
  "Rural Emergency Service Models",
  "Interfacility Transport",
  "The Future of Emergency Care"
 ]
};
var DEMOKIND="emergency-demo";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Emergency Medicine Demo — "+safe+"\n"
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
    name:topic+' — emergency medicine record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A emergency medicine record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-emergency-medicine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('emergency-medicine',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
