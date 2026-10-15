(function(){'use strict';
/* JAH Hard Equations Database generator — jahdb-hard-equations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HE-";
var FIELDS=["differential-equations","transcendental-equations","diophantine-equations","functional-equations","integral-equations","optimization-equations"];
var TOPICS={
 "differential-equations": [
  "Damped oscillator: y'' + 0.40 y' + 4.00 y = 0",
  "Damped oscillator: y'' + 1.50 y' + 9.00 y = 0",
  "Damped oscillator: y'' + 0.10 y' + 1.00 y = 0",
  "Damped oscillator: y'' + 4.00 y' + 25.00 y = 0",
  "Damped oscillator: y'' + 0.15 y' + 0.25 y = 0",
  "Heat equation on (0, 1.00) with sinusoidal initial data",
  "Heat equation on (0, 2.00) with sinusoidal initial data",
  "Heat equation on (0, 1.00) with sinusoidal initial data (2)",
  "Heat equation on (0, 3.00) with sinusoidal initial data",
  "Heat equation on (0, 1.50) with sinusoidal initial data"
 ],
 "transcendental-equations": [
  "Lambert W equation: x*e^x = 2.5",
  "Lambert W equation: x*e^x = 7",
  "Lambert W equation: x*e^x = 0.5",
  "Lambert W equation: x*e^x = 10",
  "Lambert W equation: x*e^x = 3.7",
  "Kepler's equation: E - 0.30*sin(E) = 1.20",
  "Kepler's equation: E - 0.70*sin(E) = 3.00",
  "Kepler's equation: E - 0.10*sin(E) = 0.50",
  "Kepler's equation: E - 0.90*sin(E) = 5.00",
  "Kepler's equation: E - 0.50*sin(E) = 2.00",
  "Cubic x^3+0x^2-7x+6 = 0 (three real roots)",
  "Cubic x^3-3x^2-6x+8 = 0 (three real roots)",
  "Cubic x^3+0x^2-3x+1 = 0 (three real roots)",
  "Cubic x^3-6x^2+11x-6 = 0 (three real roots)",
  "Cubic x^3-4x^2+1x+6 = 0 (three real roots)"
 ],
 "diophantine-equations": [
  "Pell equation: x^2 - 2*y^2 = 1 (minimal solution)",
  "Pell equation: x^2 - 3*y^2 = 1 (minimal solution)",
  "Pell equation: x^2 - 5*y^2 = 1 (minimal solution)",
  "Pell equation: x^2 - 7*y^2 = 1 (minimal solution)",
  "Pell equation: x^2 - 11*y^2 = 1 (minimal solution)",
  "Pythagorean triple from Euclid's formula (m=2, n=1)",
  "Pythagorean triple from Euclid's formula (m=3, n=2)",
  "Pythagorean triple from Euclid's formula (m=4, n=1)",
  "Pythagorean triple from Euclid's formula (m=4, n=3)",
  "Pythagorean triple from Euclid's formula (m=5, n=2)"
 ],
 "functional-equations": [
  "Cauchy equation with f(1) = 2",
  "Cauchy equation with f(1) = -3",
  "Cauchy equation with f(1) = 0.5",
  "Cauchy equation with f(1) = 7",
  "Cauchy equation with f(1) = -1.25"
 ],
 "integral-equations": [
  "Gaussian integral from 0 to 1",
  "Gaussian integral from -1 to 2",
  "Gaussian integral from 0 to 2",
  "Integral of sin^2(x) from 0 to pi",
  "Integral of x^2*e^(-x) from 0 to 1"
 ],
 "optimization-equations": [
  "Constrained minimum of x^2+y^2 subject to 1x+1y=2",
  "Constrained minimum of x^2+y^2 subject to 2x-1y=3",
  "Constrained minimum of x^2+y^2 subject to 3x+4y=10",
  "Constrained minimum of x^2+y^2 subject to 1x-2y=1",
  "Constrained minimum of x^2+y^2 subject to 5x+12y=13",
  "Recurrence u(n+2) = 2*u(n+1) +1*u(n): closed form",
  "Recurrence u(n+2) = 3*u(n+1) -2*u(n): closed form",
  "Recurrence u(n+2) = 1*u(n+1) +1*u(n): closed form",
  "Recurrence u(n+2) = 4*u(n+1) -3*u(n): closed form",
  "Recurrence u(n+2) = 2*u(n+1) +2*u(n): closed form",
  "Eigen-decomposition of [[4, 1], [2, 3]]",
  "Eigen-decomposition of [[2, 1], [1, 2]]",
  "Eigen-decomposition of [[5, 2], [2, 2]]",
  "Eigen-decomposition of [[3, 1], [0, 2]]",
  "Eigen-decomposition of [[6, -1], [-1, 6]]"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hard Equation — "+safe+"\n"
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
    name:topic+' — hard equation record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hard equation record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"equation-verifier",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-hard-equations-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hard-equations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
