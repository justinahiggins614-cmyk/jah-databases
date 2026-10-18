(function(){'use strict';
/* JAH The Geometry Art Database generator — jahdb-geometry-art-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GARTS-";
var FIELDS=["Shape Foundations", "Pattern Systems", "Geometric Mastery"];
var TOPICS={
 "Shape Foundations": [
  "The Polygon Family",
  "Circles and Their Secrets",
  "The Golden Ratio",
  "Tessellations: Tiles That Think",
  "Islamic Geometric Patterns",
  "The Platonic Solids",
  "Fractals: Infinity in a Frame",
  "Classical Geometry Constructions",
  "Optical Geometry",
  "Paper Folding Geometry",
  "String Art Geometry"
 ],
 "Pattern Systems": [
  "Penrose Tilings",
  "Voronoi Visions",
  "The Truchet Tile System",
  "Spirograph Mathematics",
  "Anamorphic Geometry",
  "Impossible Constructions",
  "Geodesic Structures",
  "The Harmonic Grid",
  "Zellige and Mosaic Math",
  "The Labyrinth Line",
  "The Seven-Point Star",
  "Celtic Knot Geometry",
  "The Golden Triangle"
 ],
 "Geometric Mastery": [
  "The Hypercube Project",
  "Minimal Surface Sculpture",
  "The Infinite Staircase",
  "Parametric Design Art",
  "The Geometric Mural",
  "Monumental Architecture Models",
  "The Escher Engine",
  "Your Geometric Masterwork",
  "Tiling the Sphere",
  "Hyperbolic Geometry Art"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# geometry — "+safe+"\n"
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
    name:topic+' — geometry art concept record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A geometry art concept record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"geometry-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-geometry-art-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('geometry-art-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
