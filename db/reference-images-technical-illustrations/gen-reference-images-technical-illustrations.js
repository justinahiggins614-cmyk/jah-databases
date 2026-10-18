(function(){'use strict';
/* JAH The Reference Images and Technical Illustrations Database generator — jahdb-reference-images-technical-illustrations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RITI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Technical Drawing Is: A Contract in Lines \u2014 Foundations",
  "Orthographic Projection: Three Views, One Object \u2014 Foundations",
  "Line Types and Their Meanings (ISO 128) \u2014 Foundations",
  "Drawing Scales: From Paper to Reality \u2014 Foundations",
  "Paper Sizes: The A-Series and the Square Root of Two \u2014 Foundations",
  "Title Blocks: Identity of Every Drawing \u2014 Foundations",
  "Dimensioning Basics: Extension, Dimension, Arrowheads \u2014 Foundations",
  "Schematic Symbols: A Shared Visual Language \u2014 Foundations",
  "Pictorial Views: Isometric and Perspective \u2014 Foundations",
  "Reference Images: Photographs as Engineering Evidence \u2014 Foundations",
  "Sketching: The First Drawing \u2014 Foundations",
  "Drawing Standards: ISO vs ASME \u2014 Foundations"
 ],
 "Compounded": [
  "Section Views: Cutting Away to Show Inside \u2014 Compounded",
  "Detail and Auxiliary Views \u2014 Compounded",
  "Dimensioning Methods: Chain, Baseline, Direct \u2014 Compounded",
  "Tolerances: How Much Slop Is Allowed \u2014 Compounded",
  "Electrical Schematics: Reading a Circuit Drawing \u2014 Compounded",
  "P&ID: Piping and Instrumentation Diagrams \u2014 Compounded",
  "Exploded Views: Assembly Taken Apart on Paper \u2014 Compounded",
  "Parts Lists and BOMs: Every Piece Accounted For \u2014 Compounded",
  "Surface Finish Symbols \u2014 Compounded",
  "Welding Symbols \u2014 Compounded",
  "The Schematic Library: Reusable Symbols \u2014 Compounded",
  "Revision Control: ECNs and Revision Blocks \u2014 Compounded"
 ],
 "Advanced": [
  "GD&T: Geometric Dimensioning and Tolerancing (ASME Y14.5) \u2014 Advanced",
  "Tolerance Stack-Up Analysis \u2014 Advanced",
  "Drawing-Relationship Graphs: Where-Used and Dependencies \u2014 Advanced",
  "Model-Based Definition: 3D PMI \u2014 Advanced",
  "Reference Image Libraries: Building the Visual Archive \u2014 Advanced",
  "Cross-Referencing: From Schematic to Layout to Assembly \u2014 Advanced",
  "Configuration Management of Drawing Sets \u2014 Advanced",
  "Legacy Drawing Digitization: Raster to Vector \u2014 Advanced",
  "3D-Printable Reference Models \u2014 Advanced",
  "The Master Drawing Index: Finding Any Drawing \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Technical Illustration — "+safe+"\n"
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
    name:topic+' — technical illustration record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technical illustration record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"technical-illustration-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-reference-images-technical-illustrations-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('reference-images-technical-illustrations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
