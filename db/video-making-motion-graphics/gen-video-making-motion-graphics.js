(function(){'use strict';
/* JAH The Motion Graphics Database generator — 1.0.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMMG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Easing: The Soul of Motion Graphics",
  "Kinetic Typography Fundamentals",
  "Logo Animation Essentials",
  "Shape Layers and Vector Animation",
  "Lower Thirds That Work",
  "Color and Style Frames",
  "Working with Brand Guidelines",
  "Timing to Music and Voiceover",
  "The Graph Editor: Curves Are King",
  "Looping Animations",
  "File Organization for Mograph",
  "Rendering for Broadcast and Social"
 ],
 "Compounded": [
  "Expressions: Code That Animates",
  "Character Rigs for Mograph",
  "Data Visualization in Motion",
  "Title Sequences",
  "Broadcast Package Design",
  "Explainer Video Craft",
  "Transitions and Stingers",
  "Sound Design for Mograph",
  "Storyboarding Mograph",
  "Client Revisions in Mograph",
  "Working with Templates and Toolkits"
 ],
 "Advanced": [
  "Isometric and 3D in Mograph",
  "Gradient and Texture Trends",
  "Masking and Track Mattes",
  "Camera Moves in After Effects",
  "Plugins and Scripts Worth Knowing",
  "Building a Mograph Career and Reel",
  "Real-Time Broadcast Graphics",
  "Creative Direction for Motion Graphics",
  "Motion Graphics for Experiential and Projection",
  "AI Tools in the Mograph Workflow",
  "Running the Mograph Studio"
 ]
};
var DEMOKIND="motion graphics planner";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Motion Graphics Planner — "+safe+"\n"
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
    name:topic+' — motion graphics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A motion graphics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('video-making-motion-graphics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
