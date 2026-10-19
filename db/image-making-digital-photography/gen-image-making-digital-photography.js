(function(){'use strict';
/* JAH The Digital Photography Image-Making Database generator — jahdb-image-making-digital-photography-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMDP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["How a Digital Camera Sees Light", "Exposure Triangle: Aperture, Shutter, ISO", "Focus That Never Misses", "White Balance and True Color", "Composition: Rule of Thirds and Beyond", "Holding Steady: Sharp Shots Handheld", "Reading the Histogram", "Shooting Modes: When to Use Each", "Lenses: Focal Length and What It Does", "Memory Cards and File Formats (RAW vs JPEG)", "Your First Photo Walk"], "Compounded": ["Golden Hour and Blue Hour", "Portraits with Natural Light", "Landscapes with Depth", "Freezing Motion: Sports and Action", "Long Exposures: Water and Night", "Flash Basics: Fill and Bounce", "Street Photography Ethics and Craft", "Macro: The Tiny World", "Night Sky: Stars and Milky Way", "Backlight and Silhouettes", "Color Theory in the Field", "Culling and Organizing Thousands of Shots"], "Advanced": ["Off-Camera Flash Mastery", "Panoramas and HDR Done Right", "Focus Stacking for Infinite Depth", "Time-Lapse from Stills", "Client Portraits: Posing and Directing", "Wedding-Day Workflow", "Real Estate and Architecture", "Building a Cohesive Portfolio", "Printing and Displaying Photographs", "The Photography Business: Pricing", "Teaching Photography"]};
var DEMOKIND="exposure planning";
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
    name:topic+' — digital photography image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A digital photography image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-image-making-digital-photography-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-digital-photography',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
