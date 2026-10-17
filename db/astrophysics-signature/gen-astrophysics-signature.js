(function(){'use strict';
/* JAH The Astrophysics Signature Database generator — jahdb-astrophysics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ASG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Astrophysics: The Physics of the Universe (Signature Edition) \u2014 Foundations",
  "Cosmic Units: Parsecs, Light-Years, and Solar Masses (Signature Edition) \u2014 Foundations",
  "Light and the Electromagnetic Spectrum (Signature Edition) \u2014 Foundations",
  "Blackbody Radiation: Why Stars Have Colors (Signature Edition) \u2014 Foundations",
  "The Magnitude System: Measuring Starlight (Signature Edition) \u2014 Foundations",
  "The Stefan-Boltzmann Law and Stellar Luminosity (Signature Edition) \u2014 Foundations",
  "Telescopes: How Astronomers Collect Light (Signature Edition) \u2014 Foundations",
  "The Doppler Shift: Reading Motion in Starlight (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Hydrostatic Equilibrium: What Holds a Star Up (Signature Edition) \u2014 Compounded",
  "Nuclear Fusion: The Proton-Proton Chain and the CNO Cycle (Signature Edition) \u2014 Compounded",
  "The Hertzsprung-Russell Diagram (Signature Edition) \u2014 Compounded",
  "The Mass-Luminosity Relation and Stellar Lifetimes (Signature Edition) \u2014 Compounded",
  "Radiative Transfer: How Light Escapes a Star (Signature Edition) \u2014 Compounded",
  "The Eddington Limit: How Bright a Star Can Be (Signature Edition) \u2014 Compounded",
  "The Interstellar Medium: Gas and Dust Between the Stars (Signature Edition) \u2014 Compounded",
  "Star Formation: The Jeans Criterion and Collapsing Clouds (Signature Edition) \u2014 Compounded",
  "Accretion Disks: How Matter Spirals In (Signature Edition) \u2014 Compounded",
  "Stellar Evolution: From Protostar to Remnant (Signature Edition) \u2014 Compounded",
  "Supernovae: The Deaths of Stars (Signature Edition) \u2014 Compounded",
  "Galactic Rotation Curves and Dark Matter (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "White Dwarfs and the Chandrasekhar Limit (Signature Edition) \u2014 Advanced",
  "Neutron Stars and Pulsars (Signature Edition) \u2014 Advanced",
  "Black Holes: From Stellar Mass to Supermassive (Signature Edition) \u2014 Advanced",
  "Gravitational Microlensing: Weighing Invisible Objects (Signature Edition) \u2014 Advanced",
  "Exoplanets: The Transit and Radial-Velocity Methods (Signature Edition) \u2014 Advanced",
  "The Cosmic Microwave Background (Signature Edition) \u2014 Advanced",
  "The Expanding Universe: Hubble's Law and the Friedmann Equations (Signature Edition) \u2014 Advanced",
  "Dark Energy and the Accelerating Universe (Signature Edition) \u2014 Advanced",
  "Active Galactic Nuclei and Quasars (Signature Edition) \u2014 Advanced",
  "Gamma-Ray Bursts: The Most Energetic Explosions (Signature Edition) \u2014 Advanced",
  "Nucleosynthesis: Forging the Elements in Stars (Signature Edition) \u2014 Advanced",
  "The Habitable Zone: Where Liquid Water Can Exist (Signature Edition) \u2014 Advanced",
  "Spectral Energy Distributions: Reading a Star's Light (Signature Edition) \u2014 Advanced",
  "Numerical Astrophysics: Simulating the Universe (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Astrophysics Study — "+safe+"\n"
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
    name:topic+' — astrophysics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A astrophysics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"astrophysics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-astrophysics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('astrophysics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
