(function(){'use strict';
/* JAH The Speculated Fuel Types Database generator — jahdb-fuel-types-speculated-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FUSPEC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Speculation Spectrum: What Makes a Fuel Speculative - Foundations",
  "Energy Density and the Rocket Equation - Foundations",
  "Deuterium-Tritium (D-T) Fusion Fuel - Foundations",
  "Deuterium-Deuterium (D-D) Fusion Fuel - Foundations",
  "Deuterium-Helium-3 (D-He3) Fusion Fuel - Foundations",
  "Helium-3 on Helium-3 (He3-He3) Fusion Fuel - Foundations",
  "Proton-Boron-11 (p-B11) Aneutronic Fusion Fuel - Foundations",
  "Muon-Catalyzed Fusion Fuel - Foundations",
  "Metallic Hydrogen Fuel - Foundations",
  "Antimatter-Catalyzed Fusion Fuel - Foundations",
  "Pure Antimatter Annihilation Fuel - Foundations",
  "Positronium Fuel Concepts - Foundations"
 ],
 "Compounded": [
  "Bussard Ramjet Fuel: Interstellar Hydrogen Scooping - Compounded",
  "Ram-Augmented Interstellar Ramjet Variants - Compounded",
  "Fusion Ramjet Concepts - Compounded",
  "Inertial-Confinement Micro-Fusion Pellet Fuel - Compounded",
  "Magnetized Target Fusion Fuel - Compounded",
  "Z-Pinch and Dense Plasma Focus Fuel Concepts - Compounded",
  "Quark Matter Fuel Concepts - Compounded",
  "Strangelet Concepts - Compounded",
  "Strange-Matter Conversion Concepts - Compounded",
  "Negative-Mass Propellant Concepts - Compounded",
  "Zero-Point Energy Schemes - Compounded",
  "Casimir Cavity Energy Concepts - Compounded"
 ],
 "Advanced": [
  "Hawking-Radiation Black-Hole Power - Advanced",
  "Kugelblitz Black Holes: Light-Formed Micro Black Holes - Advanced",
  "Dark Matter Annihilation Concepts - Advanced",
  "False-Vacuum Energy Scenarios - Advanced",
  "Warp-Drive Fuel Requirements - Advanced",
  "Wormhole Exotic-Matter Requirements - Advanced",
  "Exotic Matter Sourcing Concepts - Advanced",
  "White Hole Concepts - Advanced",
  "Cosmic String Energy Concepts - Advanced",
  "The Kardashev Fuel Ladder - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Speculated Fuel Study — "+safe+"\n"
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
    name:topic+' — speculated fuel record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A speculated fuel record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"speculated-fuel-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fuel-types-speculated-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fuel-types-speculated',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
