(function(){'use strict';
/* JAH Public Photoshop Database generator — jahdb-public-photoshop-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PHT-';
var FIELDS=["layers-panels", "selection-tools", "basic-tools", "painting-tools", "retouching-tools", "filters-effects", "color-correction", "techniques", "automation-workflow", "history"];
var TOPICS={
 "automation-workflow":["Actions","Batch processing","Export As and Save for Web","History panel and snapshots"],
 "basic-tools":["Crop tool","Type tool","Eyedropper and color samplers","Zoom and Hand tools"],
 "color-correction":["Curves","Levels","Hue/Saturation","Color Balance","Selective Color","Black and white conversion","White balance in Camera Raw"],
 "filters-effects":["Liquify filter","Camera Raw filter","Neural Filters","Sky Replacement","Puppet Warp","Vanishing Point","Blur Gallery"],
 "history":["Photoshop version history","Thomas and John Knoll: the origins","Generative Fill and Firefly"],
 "layers-panels":["Layers panel","Layer masks","Clipping masks","Adjustment layers","Blend modes","Smart Objects","Smart Filters","Layer styles"],
 "painting-tools":["Brush tool","Eraser tools","Gradient tool","Paint Bucket tool"],
 "retouching-tools":["Clone Stamp tool","Healing Brush tool","Spot Healing Brush tool","Content-Aware Fill","Patch tool","Remove tool","Dodge, Burn, and Sponge tools"],
 "selection-tools":["Marquee tools","Lasso tools","Object Selection tool","Quick Selection tool","Magic Wand tool","Select Subject","Select and Mask workspace","Pen tool","Channels for selections"],
 "techniques":["Frequency separation","Portrait dodge and burn","Compositing workflow","Non-destructive editing","Sharpening for output","HDR merge","Photomerge panorama"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Study Lab — "+safe+"\n"
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
    name:topic+' — photoshop study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A photoshop study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'photo-edit-lab',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-photoshop-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-photoshop',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
