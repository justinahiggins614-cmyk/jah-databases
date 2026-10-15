(function(){'use strict';
/* JAH The Graphics Pipeline Database generator — jahdb-graphics-pipeline-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GFX-";
var FIELDS=["graphics"];
var TOPICS={
 "graphics": [
  "Vertex Shaders \u2014 graphics",
  "Fragment Shaders \u2014 graphics",
  "Pixel Shaders \u2014 graphics",
  "Compute Shaders \u2014 graphics",
  "Geometry Shaders \u2014 graphics",
  "Tessellation Shaders \u2014 graphics",
  "Mesh Shaders \u2014 graphics",
  "Ray Generation Shaders \u2014 graphics",
  "Intersection Shaders \u2014 graphics",
  "Any-Hit Shaders \u2014 graphics",
  "Closest-Hit Shaders \u2014 graphics",
  "Miss Shaders \u2014 graphics",
  "Bounding Volume Hierarchies \u2014 graphics",
  "KD-Trees \u2014 graphics",
  "Octrees \u2014 graphics",
  "Framebuffers \u2014 graphics",
  "Render Targets \u2014 graphics",
  "Depth Buffers \u2014 graphics",
  "Stencil Buffers \u2014 graphics",
  "G-Buffers \u2014 graphics",
  "Texture Maps \u2014 graphics",
  "Normal Maps \u2014 graphics",
  "Roughness Maps \u2014 graphics",
  "Metalness Maps \u2014 graphics",
  "Albedo Maps \u2014 graphics",
  "Ambient Occlusion Maps \u2014 graphics",
  "Height Maps \u2014 graphics",
  "Sprite Sheets \u2014 graphics",
  "Texture Atlases \u2014 graphics",
  "Texture Arrays \u2014 graphics",
  "Cubemaps \u2014 graphics",
  "Voxel Engines \u2014 graphics",
  "Rasterizers \u2014 graphics",
  "Ray Tracers \u2014 graphics",
  "Path Tracers \u2014 graphics",
  "Photon Mappers \u2014 graphics",
  "Radiosity Engines \u2014 graphics",
  "Lightmap Bakers \u2014 graphics",
  "Reflection Probes \u2014 graphics",
  "Irradiance Volumes \u2014 graphics",
  "Shadow Mappers \u2014 graphics",
  "Cascaded Shadows \u2014 graphics",
  "Post-Processors \u2014 graphics",
  "Tonemappers \u2014 graphics",
  "Bloom Filters \u2014 graphics",
  "Motion Blurrers \u2014 graphics",
  "Depth-of-Field \u2014 graphics",
  "Anti-Aliasing \u2014 graphics",
  "Temporal Upscalers \u2014 graphics",
  "Variable Rate Shaders \u2014 graphics",
  "Foveated Renderers \u2014 graphics",
  "Occlusion Cullers \u2014 graphics",
  "Frustum Cullers \u2014 graphics",
  "LOD Systems \u2014 graphics",
  "Impostor Systems \u2014 graphics",
  "Particle Systems \u2014 graphics",
  "Decal Systems \u2014 graphics",
  "Terrain Engines \u2014 graphics",
  "Water Renderers \u2014 graphics",
  "Sky Renderers \u2014 graphics",
  "Cloud Renderers \u2014 graphics",
  "Vegetation Systems \u2014 graphics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Graphics Pipeline — "+safe+"\n"
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
    name:topic+' — graphics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A graphics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-graphics-pipeline-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('graphics-pipeline',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
