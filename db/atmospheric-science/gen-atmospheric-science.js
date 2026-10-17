(function(){'use strict';
/* JAH The Atmospheric Science Database generator — jahdb-atmospheric-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Atmospheric Science Is - Foundations",
  "The Composition of Air - Foundations",
  "The Scale of the Sky - Foundations",
  "Hydrostatic Balance and the Hypsometric Equation - Foundations",
  "The Gas Law for Air - Foundations",
  "Potential Temperature - Foundations",
  "Humidity: Vapor Pressure, Dew Point, and Relative Humidity - Foundations",
  "The Atmospheric Boundary Layer - Foundations"
 ],
 "Compounded": [
  "The Dry Adiabatic Lapse Rate - Compounded",
  "The Moist Adiabatic Lapse Rate - Compounded",
  "Static Stability of the Atmosphere - Compounded",
  "The Lifting Condensation Level and Cloud Base - Compounded",
  "Cloud Droplet Growth: Kohler Theory - Compounded",
  "Cloud Types: The Ten Genera - Compounded",
  "Warm Rain: Collision and Coalescence - Compounded",
  "Cold Rain: The Bergeron-Findeisen Process - Compounded",
  "The Thunderstorm Life Cycle - Compounded",
  "Air Masses and Fronts - Compounded",
  "Mid-Latitude Cyclones - Compounded",
  "Scattering: Why the Sky Is Blue - Compounded",
  "Atmospheric Optics: Rainbows, Halos, and Mirages - Compounded"
 ],
 "Advanced": [
  "CAPE and CIN: Reading a Sounding - Advanced",
  "Lightning and Atmospheric Electrification - Advanced",
  "Atmospheric Chemistry and Photochemistry - Advanced",
  "Smog Chemistry: Photochemical Smog - Advanced",
  "Aerosols: Particles in the Air - Advanced",
  "Air Quality and the AQI - Advanced",
  "Radiative Transfer: Beer's Law and Absorption Bands - Advanced",
  "The Polar Vortex and Sudden Stratospheric Warmings - Advanced",
  "Atmospheric Gravity Waves and Tides - Advanced",
  "Air-Sea Exchange: Fluxes Across the Interface - Advanced",
  "Doppler Radar and Remote Sensing of Storms - Advanced",
  "Weather Satellites: Eyes Above the Storms - Advanced",
  "Numerical Weather Prediction - Advanced",
  "Atmospheric Dispersion: The Gaussian Plume - Advanced",
  "Tropical Cyclones: Structure and Energetics - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Atmospheric Science Study — "+safe+"\n"
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
    name:topic+' — atmospheric science record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A atmospheric science record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"atmospheric-science-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-atmospheric-science-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('atmospheric-science',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
