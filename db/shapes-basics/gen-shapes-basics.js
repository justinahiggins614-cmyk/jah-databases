(function(){'use strict';
/* JAH The Shapes Basics Database generator — jahdb-shapes-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SHPB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Shape Is - Foundations",
  "Points, Lines, and Angles - Foundations",
  "Counting Sides, Vertices, and Corners - Foundations",
  "The Circle - Foundations",
  "The Triangle - Foundations",
  "The Square - Foundations",
  "The Rectangle - Foundations",
  "Other Quadrilaterals: Parallelogram, Rhombus, Trapezoid, Kite - Foundations",
  "Measuring Length: Units and the Ruler - Foundations",
  "Shapes in the World Around Us - Foundations"
 ],
 "Compounded": [
  "Polygons: The Pentagon and the Hexagon - Compounded",
  "Polygons: Heptagon through Decagon and the n-gon - Compounded",
  "Regular and Irregular Polygons - Compounded",
  "Perimeter: The Distance Around - Compounded",
  "Area of Rectangles and Squares - Compounded",
  "Area of Triangles - Compounded",
  "Circumference and Area of the Circle - Compounded",
  "From Flat to Solid: Faces, Edges, and Vertices - Compounded",
  "The Cube and the Rectangular Prism - Compounded",
  "The Sphere - Compounded",
  "The Cylinder - Compounded",
  "The Cone - Compounded",
  "The Pyramid - Compounded",
  "Volume of Prisms and Cylinders - Compounded"
 ],
 "Advanced": [
  "Surface Area of Solid Shapes - Advanced",
  "Volume of Pyramids, Cones, and Spheres - Advanced",
  "The Angles Inside Polygons - Advanced",
  "The Number Pi - Advanced",
  "Reflectional Symmetry: Mirror Lines - Advanced",
  "Rotational Symmetry: Turning into Place - Advanced",
  "Nets: Unfolding Solid Shapes - Advanced",
  "Euler's Formula: Faces Plus Vertices Minus Edges - Advanced",
  "Congruence and Similarity: Same Shape, Same or Scaled Size - Advanced",
  "Transformations: Slides, Flips, and Turns - Advanced"
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
var gen={version:'jahdb-shapes-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shapes-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
