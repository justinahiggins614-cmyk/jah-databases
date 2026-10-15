(function(){'use strict';
/* JAH The Signature Equation Workability Database generator — jahdb-signature-equation-workability-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EQW-";
var FIELDS=["equations"];
var TOPICS={
 "equations": [
  "Vector cross product (flagship)",
  "Vector dot product",
  "Pythagorean theorem",
  "Quadratic formula",
  "Euler's identity",
  "Law of cosines",
  "Law of sines",
  "Area of a circle",
  "Circumference",
  "Line: slope-intercept",
  "Distance formula",
  "Midpoint formula",
  "Newton's second law",
  "Kinetic energy",
  "Gravitational potential energy",
  "Newton's law of gravitation",
  "Mass-energy equivalence",
  "Ohm's law",
  "Electrical power",
  "Wave speed",
  "Snell's law",
  "Ideal gas law",
  "Binomial theorem",
  "Arithmetic series sum",
  "Geometric series sum",
  "Compound interest",
  "Bayes' theorem",
  "Normal distribution PDF",
  "Population standard deviation",
  "Power rule (derivative)",
  "Power rule (integral)",
  "Chain rule",
  "Product rule",
  "Fundamental theorem of calculus",
  "Taylor series",
  "Euler's formula",
  "De Moivre's theorem",
  "Matrix multiplication",
  "2x2 determinant",
  "Eigenvalue equation",
  "Fibonacci recurrence",
  "Factorial",
  "Permutations",
  "Combinations",
  "Shannon entropy",
  "De Morgan's laws",
  "Haversine formula",
  "Projectile range",
  "Doppler effect",
  "Lorentz factor",
  "Time-independent Schrodinger equation",
  "Heisenberg uncertainty",
  "Planck relation",
  "Coulomb's law",
  "RC time constant",
  "Discrete Fourier transform",
  "Sum of squares",
  "Logarithm product law",
  "Circle equation",
  "Volume of a sphere",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var tpl="# Vector cross product — flagship demo (Signature Equation Workability)\n" +
   "import math\n" +
   "A=(2.0,3.0,1.0); B=(1.0,-1.0,4.0)\n" +
   "def cross(a,b):\n" +
   "    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])\n" +
   "def dot(a,b): return sum(x*y for x,y in zip(a,b))\n" +
   "def mag(a): return math.sqrt(dot(a,a))\n" +
   "C=cross(A,B)\n" +
   "theta=math.asin(max(-1,min(1,mag(C)/(mag(A)*mag(B)))))\n" +
   "print(\"A =\",A); print(\"B =\",B)\n" +
   "print(\"A x B =\",tuple(round(x,6) for x in C))\n" +
   "print(\"|A x B| =\",round(mag(C),6),\" (parallelogram area)\")\n" +
   "print(\"theta =\",round(math.degrees(theta),4),\"degrees; |A||B|sin(theta) =\",round(mag(A)*mag(B)*math.sin(theta),6))\n" +
   "# Signature reading\n" +
   "print(\"Signature-One origin: both lines start counted at 1, the shared point.\")\n" +
   "print(\"Square tool: area\",round(mag(C),6),\"is the measured parallelogram.\")\n" +
   "print(\"Right-hand rule: A x B is perpendicular to both:\",round(dot(C,A),9),round(dot(C,B),9))\n" +
   "print(\"Torque example: r=(0.5,0,0) F=(0,10,0) -> tau =\",cross((0.5,0,0),(0,10,0)))\n" +
   "\n";
  return tpl.split('__TOPIC__').join(safe);
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — electronics diagnostic record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A electronics diagnostic record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-signature-equation-workability-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('signature-equation-workability',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
