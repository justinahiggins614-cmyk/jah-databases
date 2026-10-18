(function(){'use strict';
/* JAH The Unsolved Hydrology Database generator — jahdb-unsolved-hydrology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USHY-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Ungauged Basin Prediction Problem - Surface Water",
  "The Baseflow Separation Problem - Surface Water",
  "The Unit Hydrograph Universality Problem - Surface Water",
  "The Evapotranspiration Partitioning Problem - Water Cycle",
  "The Aquifer Recharge Estimation Problem - Groundwater",
  "The Snowmelt Runoff Timing Problem - Surface Water",
  "The Flash Flood Prediction Problem - Surface Water",
  "The Drought Propagation Problem - Water Cycle",
  "The Urban Hydrology Problem - Surface Water",
  "The Seawater Intrusion Control Problem - Groundwater",
  "The Environmental Flows Problem - Surface Water"
 ],
 "Compounded": [
  "The Groundwater Surface Water Interaction Problem - Groundwater",
  "The Karst Aquifer Modeling Problem - Groundwater",
  "The Fractured Rock Flow Problem - Groundwater",
  "The Preferential Flow Problem - Water Cycle",
  "The Glacier Melt Contribution Problem - Water Cycle",
  "The Permafrost Thaw Hydrology Problem - Water Cycle",
  "The Flood Frequency Under Nonstationarity Problem - Surface Water",
  "The Hydrological Drought Indices Problem - Water Cycle",
  "The Scaling in Hydrology Problem - Water Cycle",
  "The Equifinality Problem - Surface Water",
  "The Model Structural Uncertainty Problem - Surface Water",
  "The Data Assimilation in Hydrology Problem - Surface Water"
 ],
 "Advanced": [
  "The Remote Sensing of Soil Moisture Problem - Water Cycle",
  "The GRACE Groundwater Depletion Problem - Groundwater",
  "The Water Quality Modeling Problem - Surface Water",
  "The Sediment Transport Prediction Problem - Surface Water",
  "The River Morphodynamics Problem - Surface Water",
  "The Dam Removal Sediment Pulse Problem - Surface Water",
  "The Managed Aquifer Recharge Problem - Groundwater",
  "The Green Infrastructure Performance Problem - Surface Water",
  "The Isotope Hydrology Interpretation Problem - Water Cycle",
  "The Paleohydrology Reconstruction Problem - Water Cycle",
  "The Unified Water Cycle Problem - Water Cycle"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Hydrology Study — "+safe+"\n"
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
    demo:{kind:"unsolved-hydrology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-hydrology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-hydrology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
