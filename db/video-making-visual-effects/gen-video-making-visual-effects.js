(function(){'use strict';
/* JAH The Visual Effects Database generator — 1.0.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMVFX-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Compositing Really Is",
  "Green Screen Keying That Works",
  "2D Tracking: Points That Stick",
  "Rotoscoping Fundamentals",
  "Plate Preparation",
  "On-Set VFX Supervision",
  "Previs: Planning in 3D",
  "Practical vs Digital: Choosing",
  "Matchmoving: Cameras That Solve",
  "Cleanup and Paint-Out",
  "Set Extension and Matte Painting",
  "Color Space in the VFX Pipeline"
 ],
 "Compounded": [
  "Rendering: Engines and Optimization",
  "Particles and Simulations",
  "Virtual Production and LED Walls",
  "Deep Compositing and EXR Workflow",
  "Motion Capture for VFX",
  "Crowd Duplication",
  "Screen Comps and Replacements",
  "Camera Projection and Photogrammetry",
  "Lens Distortion and Undistortion",
  "Chroma Subsampling and Edge Quality",
  "VFX Editorial: Conforms and Turnovers"
 ],
 "Advanced": [
  "De-aging and Digital Humans",
  "Previs to Postvis to Final",
  "VFX Bidding and Scheduling",
  "VFX Review and Approval",
  "Building a VFX Career and Reel",
  "AI-Assisted VFX: Inpainting and Generation",
  "Real-Time VFX with Game Engines",
  "Digital Makeup and Beauty Work",
  "Episodic and Streaming VFX Pipelines",
  "Creature Work and Muscle Systems",
  "Full-CG Shots and Digital Environments"
 ]
};
var DEMOKIND="visual effects planner";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Visual Effects Planner — "+safe+"\n"
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
    name:topic+' — visual effects record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A visual effects record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'1.0.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-making-visual-effects',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
