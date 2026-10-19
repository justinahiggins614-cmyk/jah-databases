(function(){'use strict';
/* JAH The Live Action Filming Database — Signature Edition generator — 1.0.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMLFS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Camera Bodies for Live Action",
  "Sensor Sizes and Crop Factors",
  "Lenses and Focal Lengths",
  "Aperture and Depth of Field",
  "Shutter Speed and the 180-Degree Rule",
  "ISO and Clean Exposure",
  "White Balance and Color Temperature",
  "The Exposure Triangle in Practice",
  "Three-Point Lighting",
  "Shooting with Natural Light",
  "Tripods, Monopods, and Stable Shots",
  "Framing and the Rule of Thirds"
 ],
 "Compounded": [
  "Shot Sizes and What They Mean",
  "Camera Movement: Pan, Tilt, and Dolly",
  "Gimbals and Stabilized Shooting",
  "Sliders, Dollies, and Jibs",
  "Recording Clean Dialogue on Set",
  "Microphone Types for Film Sets",
  "Boom Operating Technique",
  "Directing Actors on Set",
  "Blocking a Scene",
  "Shot Lists That Work",
  "Call Sheets and the Shooting Day",
  "Continuity and Script Supervision"
 ],
 "Advanced": [
  "Slow Motion and High Frame Rates",
  "Time-Lapse Cinematography",
  "Drone Filming, Legally and Well",
  "Multicamera Live Action",
  "Shooting at Night",
  "Taming Harsh Daylight",
  "B-Roll That Cuts",
  "Coverage Strategy",
  "On-Set Safety",
  "Wrapping and Backing Up Camera Originals"
 ]
};
var DEMOKIND="signature live action planner";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature Live Action Planner — "+safe+"\n"
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
    name:topic+' — live action filming record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A live action filming record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'1.0.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-making-live-action-filming-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
