(function(){'use strict';
/* JAH The Hydrology Database generator — jahdb-hydrology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HYD-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Hydrology Is - Foundations",
  "The Water Budget Equation - Foundations",
  "Watersheds and Drainage Basins - Foundations",
  "Measuring Precipitation - Foundations",
  "Infiltration and Soil Water - Foundations",
  "Evapotranspiration: How Water Returns to the Sky - Foundations",
  "Measuring Streamflow - Foundations",
  "The Rating Curve: Stage to Discharge - Foundations"
 ],
 "Compounded": [
  "The Hydrograph: Reading a River's Pulse - Compounded",
  "Rainfall-Runoff and the Unit Hydrograph - Compounded",
  "Soil Moisture and the Vadose Zone - Compounded",
  "Darcy's Law: Groundwater in Motion - Compounded",
  "Aquifers, Wells, and the Water Table - Compounded",
  "Groundwater Recharge and Discharge - Compounded",
  "Springs and Seeps - Compounded",
  "Snow Hydrology: Reading the Snowpack - Compounded",
  "Glacier Mass Balance and Meltwater - Compounded",
  "Lakes and Reservoirs: Still-Water Hydrology - Compounded",
  "Wetlands Hydrology - Compounded",
  "Floods and Flood-Frequency Analysis - Compounded",
  "Drought Hydrology - Compounded",
  "Water Quality in Rivers - Compounded"
 ],
 "Advanced": [
  "Manning's Equation: Flow in Open Channels - Advanced",
  "Sediment Transport - Advanced",
  "Urban Hydrology - Advanced",
  "Stormwater Detention Design - Advanced",
  "Reservoir Operation and Water-Supply Yield - Advanced",
  "Hydropower Hydrology: Head and Flow - Advanced",
  "Irrigation Hydrology - Advanced",
  "Groundwater Modeling: The MODFLOW Approach - Advanced",
  "Karst Hydrology - Advanced",
  "Tracer Hydrology and Isotopes - Advanced",
  "Ecohydrology and Environmental Flows - Advanced",
  "Flood Inundation Modeling - Advanced",
  "Hydrologic Forecasting - Advanced",
  "Frontiers of Hydrology - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hydrology Study — "+safe+"\n"
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
    name:topic+' — hydrology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hydrology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hydrology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-hydrology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hydrology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
