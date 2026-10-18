(function(){'use strict';
/* JAH Signature Digital Painting Database generator — jahdb-digital-painting-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DIGPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Digital Painting Is",
  "Tablets and Pens",
  "Painting Software Compared",
  "Setting Up Your Workspace",
  "Brushes: Digital Basics",
  "Layers Explained",
  "Color Picking Digitally",
  "Undo: Painting Fearlessly",
  "Canvas Size and Resolution",
  "File Formats",
  "Ergonomics for Digital Artists"
 ],
 "Compounded": [
  "Digital Brushwork",
  "Blending Digitally",
  "Digital Color Theory",
  "Painting Skin Tones",
  "Digital Landscapes",
  "Digital Portraits",
  "Painting Metal, Glass, Fabric",
  "Photo-Bashing Basics",
  "Matte Painting Basics",
  "Concept Art Workflow",
  "Speedpainting",
  "Custom Brushes"
 ],
 "Advanced": [
  "Finished Digital Exhibition Pieces",
  "Digital Illustration for Clients",
  "Concept Art for Games and Film",
  "The Digital Artist's Business",
  "Teaching Digital Painting",
  "Famous Digital Painters",
  "Printing Digital Work",
  "Animation-Ready Painting",
  "3D and Digital Painting",
  "Building a Portfolio",
  "Protecting Digital Work"
 ]
};
var DEMOKIND="digital canvas planning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Digital Canvas Planner — "+safe+"\n"
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
    name:topic+' — digital painting record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A digital painting record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-digital-painting-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('digital-painting-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
