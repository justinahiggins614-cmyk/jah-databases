(function(){'use strict';
/* JAH The Shape Database generator — jahdb-shapes-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SHAPE-";
var FIELDS=["Fractals & Curves", "Higher-Dimensional", "Three-Dimensional", "Two-Dimensional"];
var TOPICS={"Two-Dimensional": ["Equilateral Triangle", "Isosceles Triangle", "Scalene Triangle", "Right Triangle", "Acute Triangle", "Obtuse Triangle", "Square", "Rectangle", "Parallelogram", "Rhombus", "Trapezoid", "Kite", "Regular Pentagon", "Regular Hexagon", "Regular Heptagon", "Regular Octagon", "Regular Nonagon", "Regular Decagon", "Regular Dodecagon", "Circle", "Ellipse", "Semicircle", "Annulus", "Circular Sector", "Circular Segment", "Vesica Piscis", "Lune of Hippocrates", "Reuleaux Triangle", "Pentagram", "Hexagram", "Astroid", "Cardioid", "Lemniscate of Bernoulli", "Cycloid", "Parabola", "Hyperbola", "Catenary", "Deltoid", "Concave Quadrilateral (Dart)", "Golden Rectangle", "Crescent", "Tangential Polygon"], "Three-Dimensional": ["Cube", "Cuboid (Rectangular Prism)", "Triangular Prism", "Hexagonal Prism", "Cylinder", "Cone", "Sphere", "Hemisphere", "Ellipsoid", "Torus", "Regular Tetrahedron", "Square Pyramid", "Regular Octahedron", "Regular Dodecahedron", "Regular Icosahedron", "Truncated Tetrahedron", "Cuboctahedron", "Truncated Octahedron", "Rhombic Dodecahedron", "Stella Octangula", "Conical Frustum", "Paraboloid", "Hyperboloid of One Sheet", "Mobius Strip", "Klein Bottle", "Parallelepiped", "Rhombohedron", "Square Antiprism", "Pentagonal Bipyramid", "Spherical Cap", "Steinmetz Solid (Bicylinder)", "Triangular Bipyramid", "Square Cupola (J4)", "Spherical Wedge", "Torus Knot (Trefoil Surface)"], "Higher-Dimensional": ["Tesseract (8-Cell)", "5-Cell (4-Simplex)", "16-Cell (4-Orthoplex)", "24-Cell", "120-Cell", "600-Cell", "n-Cube (Hypercube)", "3-Sphere (Hypersphere)", "n-Simplex", "n-Orthoplex", "Duoprism", "Hypercone", "4D Pyramid (Pyramid over Cube)", "Clifford Torus", "Demihypercube"], "Fractals & Curves": ["Sierpinski Triangle", "Sierpinski Carpet", "Koch Snowflake", "Menger Sponge", "Mandelbrot Set", "Cantor Set", "Golden Spiral", "Archimedean Spiral", "Logarithmic Spiral", "Tractrix"]};
var DEMOKIND="formula calculator";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — "+field+" sample\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('SAMPLE TOPIC: ' + record['topic'])\n"
   + "print('FIELD: ' + record['field'])\n"
   + "print('This is a labeled structural sample, not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — shape record',
    title:topic+' — The Shape Database',
    description:'SAMPLE RECORD (generated — structural sample). A shape record sample of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-shapes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shapes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
