(function(){'use strict';
/* JAH The Electromagnetics Signature Database generator — jahdb-electromagnetics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Electromagnetics Is: The Science of Fields That Fill Space (Signature Edition) - Foundations",
  "Coulomb's Law: The Force Between Charges, and the Birth of the Field (Signature Edition) - Foundations",
  "The Electric Field and Gauss's Law: Flux Through Closed Surfaces (Signature Edition) - Foundations",
  "Electric Potential and Voltage: The Landscape Charges Slide Down (Signature Edition) - Foundations",
  "Capacitance: Storing Electric Energy Between Plates (Signature Edition) - Foundations",
  "Electric Current and Ohm's Law: Charge in Motion (Signature Edition) - Foundations",
  "Magnetic Fields from Currents: Biot-Savart and Ampere's Law (Signature Edition) - Foundations",
  "The Lorentz Force: How Fields Push Moving Charge (Signature Edition) - Foundations",
  "Magnetic Materials: Domains, Hysteresis, and Permanent Magnets (Signature Edition) - Foundations",
  "Faraday's Law and Lenz's Law: Electricity from Changing Magnetism (Signature Edition) - Foundations",
  "Inductance: Storing Energy in Magnetic Fields (Signature Edition) - Foundations",
  "Maxwell's Equations: Four Laws, One Universe (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Displacement Current: The Term That Makes Light Possible (Signature Edition) - Compounded",
  "Boundary Conditions: What Fields Do at Material Interfaces (Signature Edition) - Compounded",
  "The Wave Equation: How Maxwell's Equations Predict Light (Signature Edition) - Compounded",
  "Plane Waves in Free Space: E, H, and the Speed of Light (Signature Edition) - Compounded",
  "Polarization: The Shape Traced by the Electric Field (Signature Edition) - Compounded",
  "The Poynting Vector: Where the Electromagnetic Energy Goes (Signature Edition) - Compounded",
  "Waves in Lossy Media: Skin Depth and the Good Conductor (Signature Edition) - Compounded",
  "Reflection and Transmission at a Boundary: The Fresnel Coefficients (Signature Edition) - Compounded",
  "Snell's Law and Total Internal Reflection: Bending Light on Purpose (Signature Edition) - Compounded",
  "Transmission Lines: When Wires Become Waveguides (Signature Edition) - Compounded",
  "The Telegrapher's Equations: The Transmission Line's Laws of Motion (Signature Edition) - Compounded",
  "Reflection, VSWR, and the Smith Chart: Reading the Circle (Signature Edition) - Compounded",
  "S-Parameters: The Language of High-Frequency Circuits (Signature Edition) - Compounded",
  "Impedance Matching: Quarter-Wave Transformers and Stubs (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Waveguides: Guiding Waves Between Metal Walls (Signature Edition) - Advanced",
  "Cavity Resonators: Trapping Waves in a Box (Signature Edition) - Advanced",
  "Antennas: Turning Guided Waves into Free Space (Signature Edition) - Advanced",
  "The Half-Wave Dipole: The Reference Antenna (Signature Edition) - Advanced",
  "Antenna Arrays: Steering Beams Without Moving (Signature Edition) - Advanced",
  "The Friis Equation: Radio Link Arithmetic (Signature Edition) - Advanced",
  "Why Accelerated Charge Radiates: The Larmor Formula (Signature Edition) - Advanced",
  "Scattering and Radar Cross Section: How Big You Look to Radar (Signature Edition) - Advanced",
  "Radar Fundamentals: Pulses, Echoes, and Doppler (Signature Edition) - Advanced",
  "EMI and EMC: When Fields Misbehave - Emissions and Immunity (Signature Edition) - Advanced",
  "Computational Electromagnetics: FDTD, FEM, and the Method of Moments (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Electromagnetics Study — "+safe+"\n"
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
    name:topic+' — electromagnetics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A electromagnetics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"electromagnetics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-electromagnetics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('electromagnetics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
