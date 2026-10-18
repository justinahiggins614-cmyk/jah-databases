(function(){'use strict';
/* JAH The Mathematics in Real Life Signature Database generator — jahdb-db-mathematics-in-real-life-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MIRLS-";
var FIELDS=["Numbers & Patterns","Shapes & Space","Chance & Change"];
var TOPICS={
 "Numbers & Patterns": [
  "Percentages: The Language of Deals (Signature Edition) - Numbers & Patterns",
  "Ratios: Recipes and Maps (Signature Edition) - Numbers & Patterns",
  "Negative Numbers: Below Zero (Signature Edition) - Numbers & Patterns",
  "Order of Operations: The Grammar of Math (Signature Edition) - Numbers & Patterns",
  "Fractions: Fair Shares (Signature Edition) - Numbers & Patterns",
  "Decimals: Money Math (Signature Edition) - Numbers & Patterns",
  "Exponents: Repeated Multiplication (Signature Edition) - Numbers & Patterns",
  "Square Roots: Undoing Squares (Signature Edition) - Numbers & Patterns",
  "Prime Numbers: The Atoms of Math (Signature Edition) - Numbers & Patterns",
  "Fibonacci: Nature's Numbers (Signature Edition) - Numbers & Patterns",
  "Zero: The Powerful Nothing (Signature Edition) - Numbers & Patterns",
  "Infinity: Bigger Than Big (Signature Edition) - Numbers & Patterns"
 ],
 "Shapes & Space": [
  "Angles: The Geometry of Turning (Signature Edition) - Shapes & Space",
  "Triangles: Nature's Strongest Shape (Signature Edition) - Shapes & Space",
  "Circles: Pi Everywhere (Signature Edition) - Shapes & Space",
  "Area: Measuring Surfaces (Signature Edition) - Shapes & Space",
  "Volume: Filling Space (Signature Edition) - Shapes & Space",
  "Symmetry: Nature's Shortcut (Signature Edition) - Shapes & Space",
  "The Pythagorean Theorem in Action (Signature Edition) - Shapes & Space",
  "Coordinate Geometry: Maps of Math (Signature Edition) - Shapes & Space",
  "Tessellations: Tiling the Plane (Signature Edition) - Shapes & Space"
 ],
 "Chance & Change": [
  "Probability: The Math of Maybe (Signature Edition) - Chance & Change",
  "Expected Value: Fair Prices (Signature Edition) - Chance & Change",
  "Statistics: Lies, Damn Lies (Signature Edition) - Chance & Change",
  "Compound Interest: The Eighth Wonder (Signature Edition) - Chance & Change",
  "Graphs: Change Made Visible (Signature Edition) - Chance & Change",
  "Logic: The Rules of Reason (Signature Edition) - Chance & Change",
  "Estimation: Fermi Problems (Signature Edition) - Chance & Change",
  "Game Theory: Thinking Strategically (Signature Edition) - Chance & Change",
  "Cryptography: Math That Keeps Secrets (Signature Edition) - Chance & Change",
  "Fractals: Infinity in a Picture (Signature Edition) - Chance & Change",
  "Topology: Donuts and Coffee Cups (Signature Edition) - Chance & Change",
  "The Monty Hall Problem (Signature Edition) - Chance & Change",
  "Benford's Law: The First-Digit Trick (Signature Edition) - Chance & Change"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Math Real Life Study — "+safe+"\n"
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
    name:topic+' — mathematics lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mathematics lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"math-real-life-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-mathematics-in-real-life-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mathematics-in-real-life-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
