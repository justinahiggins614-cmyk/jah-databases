(function(){'use strict';
/* JAH The Photogrammetry Image-Making Database generator — jahdb-image-making-photogrammetry-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMPG-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Photogrammetry Is", "Cameras and Lenses for Photogrammetry", "Overlap: The 70 Percent Rule", "Shooting Technique: Rings and Grids", "Lighting for Clean Matching", "Difficult Surfaces: Shiny, Dark, Transparent", "Ground Control and Scale", "Processing: From Photos to Mesh", "Cleaning Meshes", "Texturing from Photos", "Drone Photogrammetry for Sites"], "Compounded": ["Accuracy: How Good Is It Really", "Underwater Photogrammetry", "Faces and People", "Aerial Mapping Outputs", "Heritage Documentation", "Forensics and Accident Reconstruction", "Real-Time Models from Scans", "Photogrammetry Software Compared", "Troubleshooting Failed Alignments", "Publishing and Sharing 3D Scans", "The Photogrammetry Business", "Teaching Photogrammetry"], "Advanced": ["Laser Scanning vs Photogrammetry", "Thermal and Multispectral Photogrammetry", "Mobile Phone Photogrammetry Pro", "Cave and Tunnel Documentation", "Crime Scene Protocols Advanced", "Deformation Monitoring Over Time", "BIM Integration for Construction", "Volumetric Video from Photogrammetry", "Open-Source Pipeline Mastery", "Teaching Photogrammetry Professionally", "The Photogrammetry Studio Business"]};
var DEMOKIND="capture planning";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+DEMOKIND+" — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — photogrammetry image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A photogrammetry image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-image-making-photogrammetry-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-photogrammetry-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
