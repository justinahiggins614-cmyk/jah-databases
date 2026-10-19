(function(){'use strict';
/* JAH The Volumetric Displays Future Technology Database — Signature Edition generator — jahdb-futuretech-57-volumetric-displays-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT57-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Volumetric Displays — Pepper's Ghost - the First 3D Illusion (Signature Edition)", "Volumetric Displays — Gabor Invents Holography (Signature Edition)", "Volumetric Displays — Laser Holograms - Real 3D Photographs (Signature Edition)", "Volumetric Displays — the Sword of Damocles - First 3D Headset (Signature Edition)", "Volumetric Displays — the Leia Hologram - Fiction Sets the Goal (Signature Edition)", "Volumetric Displays — Lenticular Prints - Pocket 3D (Signature Edition)", "Volumetric Displays — IMAX 3D - Depth Goes Huge (Signature Edition)", "Volumetric Displays — FogScreen - Images on Air (Signature Edition)", "Volumetric Displays — Perspecta - True 3D for Sale (Signature Edition)", "Volumetric Displays — the 3D TV Boom and Lesson (Signature Edition)", "Volumetric Displays — Looking Glass - Desktop Holograms (Signature Edition)"], "Compounded": ["Volumetric Displays — HoloLens - Holograms in the Room (Signature Edition)", "Volumetric Displays — Laser Plasma in Mid-Air (Signature Edition)", "Volumetric Displays — Hologram Fans Everywhere (Signature Edition)", "Volumetric Displays — Voxon VX1 - the Hacker Volumetric (Signature Edition)", "Volumetric Displays — Sony's 3D Desk Display (Signature Edition)", "Volumetric Displays — Volumetric Capture Stages (Signature Edition)", "Volumetric Displays — Vision Pro - Apple's 3D Bet (Signature Edition)", "Volumetric Displays — Neural Holography (Signature Edition)", "Volumetric Displays — Consumer Light-Field Monitors (Signature Edition)", "Volumetric Displays — Holographic Video Calls (Signature Edition)", "Volumetric Displays — The Volumetric TV (Signature Edition)", "Volumetric Displays — Holographic Workstations (Signature Edition)"], "Advanced": ["Volumetric Displays — Screenless 3D Projection (Signature Edition)", "Volumetric Displays — Volumetric Billboards (Signature Edition)", "Volumetric Displays — Volumetric Medical Imaging (Signature Edition)", "Volumetric Displays — Holographic Meeting Rooms (Signature Edition)", "Volumetric Displays — Volumetric Gaming (Signature Edition)", "Volumetric Displays — Volumetric Design Review (Signature Edition)", "Volumetric Displays — Holographic Navigation (Signature Edition)", "Volumetric Displays — Volumetric Classrooms (Signature Edition)", "Volumetric Displays — The Volumetric Assistant (Signature Edition)", "Volumetric Displays — Volumetric Retail (Signature Edition)", "Volumetric Displays — The Everyday Volumetric Display (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Volumetric Displays study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-57-volumetric-displays-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-57-volumetric-displays-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
