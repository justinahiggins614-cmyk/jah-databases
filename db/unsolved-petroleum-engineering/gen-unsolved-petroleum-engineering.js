(function(){'use strict';
/* JAH The Unsolved Petroleum Engineering Database generator — jahdb-unsolved-petroleum-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USPE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Multiphase Flow in Porous Media Problem - Reservoir Engineering",
  "The Relative Permeability Hysteresis Problem - Reservoir Engineering",
  "The Wettability Alteration Problem - Reservoir Engineering",
  "The Wellbore Stability in Shales Problem - Drilling Engineering",
  "The Lost Circulation Control Problem - Drilling Engineering",
  "The Drilling Fluid Optimization Problem - Drilling Engineering",
  "The Rate of Penetration Limit Problem - Drilling Engineering",
  "The Asphaltene Deposition Problem - Production Engineering",
  "The Scale Formation Prediction Problem - Production Engineering",
  "The Hydrate Formation Prevention Problem - Production Engineering",
  "The Corrosion in Sour Service Problem - Production Engineering"
 ],
 "Compounded": [
  "The Enhanced Oil Recovery Efficiency Limit Problem - Reservoir Engineering",
  "The Reservoir Characterization From Sparse Data Problem - Reservoir Engineering",
  "The Hydraulic Fracturing Proppant Transport Problem - Reservoir Engineering",
  "The Fracture Network Complexity Problem - Reservoir Engineering",
  "The Induced Seismicity Prediction Problem - Reservoir Engineering",
  "The Shale Gas Desorption Kinetics Problem - Reservoir Engineering",
  "The Tight Oil Decline Curve Problem - Reservoir Engineering",
  "The Waterflooding Sweep Efficiency Problem - Reservoir Engineering",
  "The CO2 EOR Miscibility Problem - Reservoir Engineering",
  "The Steam Assisted Gravity Drainage Optimization Problem - Reservoir Engineering",
  "The Polymer Flooding Degradation Problem - Reservoir Engineering",
  "The Produced Water Treatment Problem - Production Engineering"
 ],
 "Advanced": [
  "The In Situ Combustion Control Problem - Reservoir Engineering",
  "The Surfactant EOR Cost Problem - Reservoir Engineering",
  "The Microbial EOR Mechanisms Problem - Reservoir Engineering",
  "The Integrated Flow Assurance Problem - Production Engineering",
  "The Subsea Processing Reliability Problem - Production Engineering",
  "The Offshore Decommissioning Problem - Production Engineering",
  "The Methane Leak Detection Problem - Production Engineering",
  "The Flaring Reduction Problem - Production Engineering",
  "The Carbon Capture and Storage in Depleted Reservoirs Problem - Reservoir Engineering",
  "The Geothermal Co-production Problem - Reservoir Engineering",
  "The Unified Subsurface Resource Problem - Production Engineering"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Petroleum Engineering Study — "+safe+"\n"
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
    demo:{kind:"unsolved-petroleum-engineering-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-petroleum-engineering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-petroleum-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
