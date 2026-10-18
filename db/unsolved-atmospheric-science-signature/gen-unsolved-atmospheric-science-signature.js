(function(){'use strict';
/* JAH The Unsolved Atmospheric Science Signature Database generator — jahdb-unsolved-atmospheric-science-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USATS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Convection Parameterization Problem (Signature Edition) - Atmospheric Dynamics",
  "The Cloud Feedback Problem (Signature Edition) - Climate",
  "The Aerosol Indirect Effect Problem (Signature Edition) - Climate",
  "The Stratospheric Ozone Recovery Problem (Signature Edition) - Atmospheric Chemistry",
  "The Lightning Initiation Problem (Signature Edition) - Atmospheric Electricity",
  "The Tornadogenesis Problem (Signature Edition) - Severe Weather",
  "The Hurricane Intensification Problem (Signature Edition) - Severe Weather",
  "The Monsoon Prediction Problem (Signature Edition) - Climate",
  "The El Nino Diversity Problem (Signature Edition) - Climate",
  "The Stratosphere Troposphere Coupling Problem (Signature Edition) - Atmospheric Dynamics",
  "The Atmospheric Rivers Problem (Signature Edition) - Climate"
 ],
 "Compounded": [
  "The Boundary Layer Turbulence Problem (Signature Edition) - Atmospheric Dynamics",
  "The Cloud Microphysics Problem (Signature Edition) - Atmospheric Dynamics",
  "The Ice Nucleation Problem (Signature Edition) - Atmospheric Dynamics",
  "The Atmospheric Chemistry Coupling Problem (Signature Edition) - Atmospheric Chemistry",
  "The Methane Budget Problem (Signature Edition) - Atmospheric Chemistry",
  "The Ozone Hole Chemistry Problem (Signature Edition) - Atmospheric Chemistry",
  "The Polar Vortex Disruption Problem (Signature Edition) - Atmospheric Dynamics",
  "The Sudden Stratospheric Warming Problem (Signature Edition) - Atmospheric Dynamics",
  "The Quasi Biennial Oscillation Problem (Signature Edition) - Atmospheric Dynamics",
  "The Madden Julian Oscillation Problem (Signature Edition) - Atmospheric Dynamics",
  "The Blocking Highs Problem (Signature Edition) - Atmospheric Dynamics",
  "The Jet Stream Meandering Problem (Signature Edition) - Atmospheric Dynamics"
 ],
 "Advanced": [
  "The Climate Sensitivity Problem (Signature Edition) - Climate",
  "The Hydrological Cycle Amplification Problem (Signature Edition) - Climate",
  "The Tropical Cyclone Frequency Problem (Signature Edition) - Climate",
  "The Climate Tipping Points Problem (Signature Edition) - Climate",
  "The Paleoclimate Data Model Mismatch Problem (Signature Edition) - Climate",
  "The Urban Air Chemistry Problem (Signature Edition) - Atmospheric Chemistry",
  "The Geoengineering Governance Problem (Signature Edition) - Climate",
  "The Atmospheric Electricity Problem (Signature Edition) - Atmospheric Electricity",
  "The Noctilucent Clouds Problem (Signature Edition) - Atmospheric Dynamics",
  "The Atmospheric Tides Problem (Signature Edition) - Atmospheric Dynamics",
  "The Unified Atmosphere Problem (Signature Edition) - Climate"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Atmospheric Science Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-atmospheric-science-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-atmospheric-science-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-atmospheric-science-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
