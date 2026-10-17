(function(){'use strict';
/* JAH The Shapes Basics Signature Database generator — jahdb-shapes-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SHPBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Shape Is (Signature Edition) - Foundations",
  "Points, Lines, and Angles (Signature Edition) - Foundations",
  "Counting Sides, Vertices, and Corners (Signature Edition) - Foundations",
  "The Circle (Signature Edition) - Foundations",
  "The Triangle (Signature Edition) - Foundations",
  "The Square (Signature Edition) - Foundations",
  "The Rectangle (Signature Edition) - Foundations",
  "Other Quadrilaterals: Parallelogram, Rhombus, Trapezoid, Kite (Signature Edition) - Foundations",
  "Measuring Length: Units and the Ruler (Signature Edition) - Foundations",
  "Shapes in the World Around Us (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Polygons: The Pentagon and the Hexagon (Signature Edition) - Compounded",
  "Polygons: Heptagon through Decagon and the n-gon (Signature Edition) - Compounded",
  "Regular and Irregular Polygons (Signature Edition) - Compounded",
  "Perimeter: The Distance Around (Signature Edition) - Compounded",
  "Area of Rectangles and Squares (Signature Edition) - Compounded",
  "Area of Triangles (Signature Edition) - Compounded",
  "Circumference and Area of the Circle (Signature Edition) - Compounded",
  "From Flat to Solid: Faces, Edges, and Vertices (Signature Edition) - Compounded",
  "The Cube and the Rectangular Prism (Signature Edition) - Compounded",
  "The Sphere (Signature Edition) - Compounded",
  "The Cylinder (Signature Edition) - Compounded",
  "The Cone (Signature Edition) - Compounded",
  "The Pyramid (Signature Edition) - Compounded",
  "Volume of Prisms and Cylinders (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Surface Area of Solid Shapes (Signature Edition) - Advanced",
  "Volume of Pyramids, Cones, and Spheres (Signature Edition) - Advanced",
  "The Angles Inside Polygons (Signature Edition) - Advanced",
  "The Number Pi (Signature Edition) - Advanced",
  "Reflectional Symmetry: Mirror Lines (Signature Edition) - Advanced",
  "Rotational Symmetry: Turning into Place (Signature Edition) - Advanced",
  "Nets: Unfolding Solid Shapes (Signature Edition) - Advanced",
  "Euler's Formula: Faces Plus Vertices Minus Edges (Signature Edition) - Advanced",
  "Congruence and Similarity: Same Shape, Same or Scaled Size (Signature Edition) - Advanced",
  "Transformations: Slides, Flips, and Turns (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Shapes Basics Study — "+safe+"\n"
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
    name:topic+' — shapes basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A shapes basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"shapes-basics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-shapes-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shapes-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
