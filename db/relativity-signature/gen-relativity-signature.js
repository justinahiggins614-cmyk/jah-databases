(function(){'use strict';
/* JAH The Relativity Signature Database generator — jahdb-relativity-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-REG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Relativity: Motion Is Always Relative (Signature Edition) \u2014 Foundations",
  "The Principle of Relativity (Signature Edition) \u2014 Foundations",
  "The Two Postulates of Special Relativity (Signature Edition) \u2014 Foundations",
  "Inertial Reference Frames (Signature Edition) \u2014 Foundations",
  "The Light Clock Thought Experiment (Signature Edition) \u2014 Foundations",
  "Time Dilation (Signature Edition) \u2014 Foundations",
  "The Lorentz Factor (Signature Edition) \u2014 Foundations",
  "Length Contraction (Signature Edition) \u2014 Foundations",
  "Simultaneity Is Relative (Signature Edition) \u2014 Foundations",
  "Spacetime: The Four-Dimensional Continuum (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "The Lorentz Transformations (Signature Edition) \u2014 Compounded",
  "Relativistic Velocity Addition (Signature Edition) \u2014 Compounded",
  "Mass-Energy Equivalence (E = mc^2) (Signature Edition) \u2014 Compounded",
  "Relativistic Momentum and Energy (Signature Edition) \u2014 Compounded",
  "The Spacetime Interval and Causality (Signature Edition) \u2014 Compounded",
  "The Twin Paradox (Signature Edition) \u2014 Compounded",
  "The Relativistic Doppler Effect (Signature Edition) \u2014 Compounded",
  "Proper Time and Proper Length (Signature Edition) \u2014 Compounded",
  "The Michelson-Morley Experiment (Signature Edition) \u2014 Compounded",
  "The Equivalence Principle (Signature Edition) \u2014 Compounded",
  "Spacetime Curvature (Signature Edition) \u2014 Compounded",
  "The Einstein Field Equations (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Gravitational Time Dilation (Signature Edition) \u2014 Advanced",
  "Geodesics: The Straightest Paths in Curved Spacetime (Signature Edition) \u2014 Advanced",
  "Black Holes (Signature Edition) \u2014 Advanced",
  "Gravitational Waves in General Relativity (Signature Edition) \u2014 Advanced",
  "The Expanding Universe (Signature Edition) \u2014 Advanced",
  "Frame Dragging (Lense-Thirring Effect) (Signature Edition) \u2014 Advanced",
  "Gravitational Lensing (Signature Edition) \u2014 Advanced",
  "The Cosmological Constant and Dark Energy (Signature Edition) \u2014 Advanced",
  "Tests of General Relativity (Signature Edition) \u2014 Advanced",
  "Relativity and GPS: Everyday Proof (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Relativity Study — "+safe+"\n"
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
    name:topic+' — relativity record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A relativity record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"relativity-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-relativity-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('relativity-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
