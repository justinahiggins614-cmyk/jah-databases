(function(){'use strict';
/* JAH Geometry Tutoring Database generator — jahdb-geometry-tutoring-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GEOMTS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Points, Lines, and Planes (Signature Edition)", "Angles and Measurement (Signature Edition)", "Parallel and Perpendicular Lines (Signature Edition)", "Triangle Basics (Signature Edition)", "Congruent Triangles (Signature Edition)", "Similar Triangles (Signature Edition)", "The Pythagorean Theorem (Signature Edition)", "Special Right Triangles (Signature Edition)", "Quadrilaterals (Signature Edition)", "Polygons and Angles (Signature Edition)", "Circles: Parts (Signature Edition)"], "Compounded": ["Circle Theorems (Signature Edition)", "Area Formulas (Signature Edition)", "Perimeter and Circumference (Signature Edition)", "Volume and Surface Area (Signature Edition)", "Transformations (Signature Edition)", "Coordinate Geometry (Signature Edition)", "Proofs: Direct (Signature Edition)", "Proofs: Indirect (Signature Edition)", "Construction Basics (Signature Edition)", "Problem-Solving Strategies (Signature Edition)", "Common Misconceptions (Signature Edition)", "Test Strategies (Signature Edition)"], "Advanced": ["Real-World Geometry (Signature Edition)", "Teaching Geometry (Signature Edition)", "The Annual Geometry Review (Signature Edition)", "Trigonometry Bridges (Signature Edition)", "Geometric Probability (Signature Edition)", "Locus and Construction (Signature Edition)", "3D Visualization (Signature Edition)", "Geometric Transformations Proof (Signature Edition)", "Competition Geometry (Signature Edition)", "Geometry in Art (Signature Edition)", "Geometric Reasoning in Life (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — tutoring guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — tutoring guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tutoring guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"geometry-tutoring-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-geometry-tutoring-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("geometry-tutoring-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
