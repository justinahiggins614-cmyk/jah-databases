(function(){'use strict';
/* JAH The Surgeons Database generator — jahdb-surgeons-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SRGN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Surgeons Do",
  "The Road to Surgeon: Residency",
  "Sterile Technique and the Surgical Field",
  "Surgical Instruments: The Basic Set",
  "Suturing and Knot Tying",
  "Hemostasis: Controlling Bleeding",
  "The Surgical Timeout",
  "Postoperative Care Basics",
  "Informed Consent for Surgery",
  "Surgical History: From Barbers to Robots",
  "Surgical Team Roles",
 ],
 "Compounded": [
  "General Surgery",
  "Cardiothoracic Surgery",
  "Neurosurgery",
  "Orthopedic Surgery",
  "Plastic and Reconstructive Surgery",
  "Vascular Surgery",
  "Pediatric Surgery",
  "Surgical Oncology",
  "Trauma Surgery",
  "Minimally Invasive and Robotic Surgery",
  "The WHO Surgical Safety Checklist",
  "Surgical Complications and Disclosure",
 ],
 "Advanced": [
  "Cardiopulmonary Bypass Management",
  "Aneurysm Clipping and Coiling",
  "Joint Replacement Mastery",
  "Microsurgery: Vessels Under the Microscope",
  "Endovascular Aneurysm Repair (EVAR)",
  "Neonatal Surgical Emergencies",
  "HIPEC: Heated Chemotherapy Surgery",
  "Damage Control Resuscitation",
  "Natural Orifice and Single-Site Surgery",
  "The Surgeon Career Ladder",
  "Surgical Critical Care",
 ],
};
var DEMOKIND="surgical calculation";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Surgical calculator — "+safe+"\n"
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
    name:topic+' — surgeon profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miners profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-surgeons-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('surgeons',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
