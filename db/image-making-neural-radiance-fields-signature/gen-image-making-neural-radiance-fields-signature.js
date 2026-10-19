(function(){'use strict';
/* JAH The Neural Radiance Fields Image-Making Database generator — jahdb-image-making-neural-radiance-fields-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMNF-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Neural Radiance Fields Are", "Capturing for NeRF", "Training: What Happens", "Instant-NGP: NeRFs in Minutes", "NeRF vs Photogrammetry", "Rendering Novel Views", "Dynamic NeRFs: Moving Scenes", "NeRFs for VFX Production", "3D Gaussian Splatting: The Challenger", "Editing NeRF Scenes", "NeRFs on Mobile"], "Compounded": ["The Business of Volumetric Capture", "Ethics of Navigable Captures", "COLMAP Deep Dive", "Camera Pose Troubleshooting", "Lighting for NeRF Capture", "Reflective Surfaces in NeRF", "Outdoor Scene Capture", "Indoor Room Capture", "Object Turntable Capture", "Drone Capture for NeRF", "Mesh Extraction from NeRF", "Depth Map Export"], "Advanced": ["Dynamic Scene Frontiers", "Relighting NeRFs", "Semantic Segmentation in NeRF", "Large-Scale Scene Tiling", "Real-Time Viewers Compared", "Web Delivery of Volumetric", "NeRFs in Unreal/Unity", "Commercial Licensing of Captures", "Privacy Law for Volumetric Capture", "Teaching Volumetric Capture", "The Volumetric Studio Business"]};
var DEMOKIND="nerf capture planning";
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
    name:topic+' — neural radiance fields image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A neural radiance fields image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-image-making-neural-radiance-fields-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-neural-radiance-fields-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
