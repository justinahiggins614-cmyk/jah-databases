(function(){'use strict';
/* JAH Fundamentals of Electromagnetism Database generator — jahdb-fundamental-electromagnetism-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic fundamental record generation: pick a field, set a seed, get a complete record.
   Same seed + same field = same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ELE-";
var FIELDS=["electrostatics", "magnetostatics", "induction", "Maxwell's equations", "waves", "circuits"];
var TOPICS=[
    {t: "Electric Charge", b: "Charge is conserved and quantized; conductors share it freely, insulators trap it \u2014 the two material classes of electrostatics."},
    {t: "Coulomb's Law and the E Field", b: "Inverse-square forces become the electric field: force per unit charge, mapped by field lines from + to \u2212."},
    {t: "Electric Potential", b: "Voltage is potential energy per charge: circuits are just charges rolling downhill from high to low potential."},
    {t: "Capacitors", b: "Storing charge across a dielectric: C = \u03b5A/d, energy \u00bdCV\u00b2 \u2014 the physics inside every power supply and touch screen."},
    {t: "Currents and Resistance", b: "Drifting electrons scatter off atoms (Ohm's law V = IR); superconductors scatter none at all below their critical temperature."},
    {t: "Magnetism from Motion", b: "Moving charges make magnetic fields (Biot-Savart); magnets are just aligned atomic currents."},
    {t: "The Lorentz Force", b: "F = q(E + v\u00d7B): the single force law behind motors, cyclotrons, and the aurora."},
    {t: "Faraday's Induction", b: "Changing magnetic flux induces EMF: every generator, transformer, and induction stove is Faraday's law at work."},
    {t: "Maxwell's Equations", b: "Four equations unify electricity and magnetism \u2014 and predict electromagnetic waves traveling at c, identifying light itself."},
    {t: "Electromagnetic Waves", b: "Self-propagating E and B oscillations: the spectrum from radio to gamma is one phenomenon at different frequencies."},
    {t: "AC Circuits", b: "Inductors and capacitors trade energy back and forth; impedance generalizes resistance and resonance picks stations."},
    {t: "Electromagnetic Energy Flow", b: "The Poynting vector S = E\u00d7H tracks energy: fields themselves carry power from transmitter to receiver."}
];
var PRINCIPLES=[
    {n: "Coulomb's law", e: "F = k\u00b7q\u2081q\u2082/r\u00b2", s: "Like charges repel with inverse-square force \u2014 electrostatics' foundation."},
    {n: "Faraday's law", e: "\u2207\u00d7E = \u2212\u2202B/\u2202t", s: "Changing magnetic fields create electric fields \u2014 generators and transformers obey this."},
    {n: "Maxwell's equations", e: "4 equations, all of EM", s: "Gauss, no magnetic monopoles, Faraday, Amp\u00e8re-Maxwell: the complete classical theory."}
];
var USES=["Designing motors and transformers", "Engineering antennas", "Building power supplies", "Shielding sensitive electronics"];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ti=(rnd()*TOPICS.length)|0, pi=(rnd()*PRINCIPLES.length)|0, ui=(rnd()*USES.length)|0;
  var tp=TOPICS[ti], pr=PRINCIPLES[pi], use=USES[ui];
  var rank=((ti/2)|0)+1;
  var id=PREFIX+String(seed).padStart(6,'0');
  var eq=pr.e?(' Governing relation: '+pr.e+'.'):'';
  var desc=tp.b+' First principle: '+pr.n+' — '+pr.s+'.'+eq+' In practice: '+use+' Rank '+rank+' of 6 on the teaching ladder.';
  return {
    id:id, t:tp.t, g:field, name:"Electromagnetism"+': '+tp.t, title:tp.t,
    description:desc, edition: seed%2 ? 'signature' : 'public',
    ladder_rank:rank, field:field,
    principle:{name:pr.n, equation:pr.e, statement:pr.s},
    key_points:[tp.b, pr.n+': '+pr.s, 'Application: '+use, 'Ladder rank '+rank+'/6'],
    src:'generator-sample', sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:'# JAH Fundamentals of Electromagnetism demo\n# Record '+id+' — '+tp.t.replace(/\n/g,' ')+'\nprint("record jahdb-fundamental-electromagnetism-1.0")\nprint("OK: '+id+' generated fundamental record")\n',note:'Generator sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0&&FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&(r.g===record.g||r.field===record.field);});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-fundamental-electromagnetism-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("fundamental-electromagnetism",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
