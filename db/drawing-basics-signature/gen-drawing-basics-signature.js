(function(){'use strict';
/* JAH Signature Drawing Basics Database generator — jahdb-drawing-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DRAWBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Drawing Is",
  "Drawing Tools: Pencils, Erasers, Paper",
  "Lines: The Drawing Vocabulary",
  "Basic Shapes: Building Blocks",
  "Shading: Value and Tone",
  "Contour Drawing",
  "Gesture Drawing",
  "Proportion and Sighting",
  "Perspective Primer",
  "Composition Basics for Drawing",
  "The Drawing Sketchbook Habit"
 ],
 "Compounded": [
  "Cross-Hatching and Texture",
  "Still Life Drawing",
  "Drawing Hands",
  "Drawing Faces: Features",
  "Figure Drawing Basics",
  "Drapery and Fabric",
  "Drawing Animals",
  "Botanical Drawing",
  "Light and Shadow: Rendering Form",
  "Negative Space",
  "Grid Method",
  "Drawing from Photographs vs Life"
 ],
 "Advanced": [
  "Portrait Drawing",
  "Anatomy for Artists: Skeleton",
  "Anatomy: Muscles in Motion",
  "Master Studies: Copying the Masters",
  "Expressive Mark-Making",
  "Large-Scale Drawing",
  "Drawing with Mixed Dry Media",
  "The Artist's Portfolio",
  "Teaching Drawing",
  "Selling Drawings",
  "Exhibiting and Framing Drawings"
 ]
};
var DEMOKIND="drawing proportion planning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Drawing Proportion Planner — "+safe+"\n"
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
    name:topic+' — drawing basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A drawing basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-drawing-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('drawing-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
