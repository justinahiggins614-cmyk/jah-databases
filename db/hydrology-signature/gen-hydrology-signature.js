(function(){'use strict';
/* JAH The Hydrology Signature Database generator — jahdb-hydrology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HYDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Hydrology Is (Signature Edition) - Foundations",
  "The Water Budget Equation (Signature Edition) - Foundations",
  "Watersheds and Drainage Basins (Signature Edition) - Foundations",
  "Measuring Precipitation (Signature Edition) - Foundations",
  "Infiltration and Soil Water (Signature Edition) - Foundations",
  "Evapotranspiration: How Water Returns to the Sky (Signature Edition) - Foundations",
  "Measuring Streamflow (Signature Edition) - Foundations",
  "The Rating Curve: Stage to Discharge (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Hydrograph: Reading a River's Pulse (Signature Edition) - Compounded",
  "Rainfall-Runoff and the Unit Hydrograph (Signature Edition) - Compounded",
  "Soil Moisture and the Vadose Zone (Signature Edition) - Compounded",
  "Darcy's Law: Groundwater in Motion (Signature Edition) - Compounded",
  "Aquifers, Wells, and the Water Table (Signature Edition) - Compounded",
  "Groundwater Recharge and Discharge (Signature Edition) - Compounded",
  "Springs and Seeps (Signature Edition) - Compounded",
  "Snow Hydrology: Reading the Snowpack (Signature Edition) - Compounded",
  "Glacier Mass Balance and Meltwater (Signature Edition) - Compounded",
  "Lakes and Reservoirs: Still-Water Hydrology (Signature Edition) - Compounded",
  "Wetlands Hydrology (Signature Edition) - Compounded",
  "Floods and Flood-Frequency Analysis (Signature Edition) - Compounded",
  "Drought Hydrology (Signature Edition) - Compounded",
  "Water Quality in Rivers (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Manning's Equation: Flow in Open Channels (Signature Edition) - Advanced",
  "Sediment Transport (Signature Edition) - Advanced",
  "Urban Hydrology (Signature Edition) - Advanced",
  "Stormwater Detention Design (Signature Edition) - Advanced",
  "Reservoir Operation and Water-Supply Yield (Signature Edition) - Advanced",
  "Hydropower Hydrology: Head and Flow (Signature Edition) - Advanced",
  "Irrigation Hydrology (Signature Edition) - Advanced",
  "Groundwater Modeling: The MODFLOW Approach (Signature Edition) - Advanced",
  "Karst Hydrology (Signature Edition) - Advanced",
  "Tracer Hydrology and Isotopes (Signature Edition) - Advanced",
  "Ecohydrology and Environmental Flows (Signature Edition) - Advanced",
  "Flood Inundation Modeling (Signature Edition) - Advanced",
  "Hydrologic Forecasting (Signature Edition) - Advanced",
  "Frontiers of Hydrology (Signature Edition) - Advanced"
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
var gen={version:'jahdb-hydrology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hydrology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
