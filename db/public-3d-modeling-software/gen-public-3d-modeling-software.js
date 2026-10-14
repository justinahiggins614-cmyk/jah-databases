(function(){'use strict';
/* Public 3D Modeling Software Database generator — jahdb-public-3d-modeling-software-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-3DMS-';
var SRC='public-harvest';
var RECORD_KIND='3D modeling software';
var GENRES=["3D animation", "3D design", "3D modeling", "3D modeling/render", "3D motion design", "3D suite", "CAD", "CAD/CAM", "NURBS modeling", "UV mapping", "VR 3D", "VR illustration", "VR painting", "VR sculpting", "animation", "beginner 3D", "character", "cloth", "cloud 3D", "cloud CAD", "digital sculpting", "environments", "facial capture", "material authoring", "material capture", "mesh tools", "mobile 3D", "mobile CAD", "mobile sculpting", "mocap", "procedural 3D/VFX", "real-time render", "real-time viz", "rendering", "retopology", "rigging/animation", "scene staging", "sculpt/texture", "sculpting", "stop motion", "terrain", "terrain render", "texturing", "vegetation"];
var TOPICS=["Blender", "Autodesk Maya", "Autodesk 3ds Max", "Cinema 4D", "ZBrush", "SketchUp", "Houdini", "Modo", "Rhinoceros 3D", "Autodesk Fusion 360", "SolidWorks", "Onshape", "Tinkercad", "Sculptris", "Meshmixer", "Microsoft 3D Builder", "Paint 3D", "Clara.io", "Vectary", "Spline", "Nomad Sculpt", "Forger", "Shapr3D", "uMake", "Gravity Sketch", "Tilt Brush", "Quill", "Medium", "Substance 3D Painter", "Substance 3D Designer", "Substance 3D Sampler", "Substance 3D Stager", "Mari", "3DCoat", "Mudbox", "TopoGun", "RizomUV", "UVLayout", "World Machine", "Gaea", "Terragen", "Vue", "SpeedTree", "Marvelous Designer", "DAZ 3D", "Character Creator", "MetaHuman", "Mixamo", "Cascadeur", "Akeytsu", "Dragonframe", "Stop Motion Studio", "Plask", "Rokoko Studio", "Faceware", "Dynamixyz", "KeyShot", "Twinmotion", "Enscape", "D5 Render"];
function mulberry(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
function buildContent(title,genre){
  var summary='A 3D modeling software record for '+title+' ('+genre+'). Full profile in the archive.';
  var sections=[
    {heading:'Overview',body:'See the archived record '+title+' for the complete profile.'},
    {heading:'Key features',body:'Full feature list in the archived record.'},
    {heading:'Details',body:'Full details in the archived record.'}
  ];
  return{summary:summary,sections:sections,key_facts:['Deterministic generator record.','src: '+SRC+'.']};
}
function defaultDemo(){
  return{kind:'record-program',
    program:"// record viewer \u2014 run with: node demo.js\nconst r = JSON.parse(require('fs').readFileSync('record.json','utf8'));\nconsole.log(r.id+' \u2014 '+r.title);\nconsole.log(r.description);\nconsole.log('['+r.src+']');",
    note:'Prints the record. Run: node demo.js'};
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0)||1;
  var title=TOPICS[(s-1)%TOPICS.length];
  var genre=GENRES[(s-1)%GENRES.length];
  if(opts.genre&&GENRES.indexOf(opts.genre)>=0)genre=opts.genre;
  var ctopic=opts.topic?String(opts.topic).trim().slice(0,120):'';
  if(ctopic){title=ctopic;}
  var id=PREFIX+pad(s);
  var c=buildContent(title,genre);
  return{id:id,title:title,description:c.summary,genre:genre,type:RECORD_KIND,
    content:{summary:c.summary,sections:c.sections,key_facts:c.key_facts},
    demo:defaultDemo(),src:SRC,_seed:s};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0||!/\d{6}$/.test(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!r.content||typeof r.content!=='object'||typeof r.content.summary!=='string'||r.content.summary.length<10)e.push('content');
  if(!r.demo||typeof r.demo!=='object')e.push('demo');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].t===rec.title)return{ok:false,errors:['duplicate title in archive sample']};}
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-public-3d-modeling-software-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-3d-modeling-software',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();