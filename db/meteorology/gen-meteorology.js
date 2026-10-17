(function(){'use strict';
/* JAH The Meteorology Database generator — jahdb-meteorology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MET-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Meteorology Is - Foundations",
  "Observing the Sky: Weather Instruments and the Observer's Toolkit - Foundations",
  "The Observing Network: ASOS, Radiosondes, and the Global System - Foundations",
  "Reading a Weather Map: The Surface Analysis - Foundations",
  "Air Masses in Practice: Source Regions and Modification - Foundations",
  "The Diurnal Cycle and Local Winds: Sea Breezes to Mountain Breezes - Foundations",
  "Fronts in Practice: Cold, Warm, Occluded, and Stationary - Foundations",
  "The Mid-Latitude Cyclone in Practice: The Norwegian Model - Foundations",
  "Upper-Air Charts: The 500-Millibar Map and Steering - Foundations",
  "Jet Streams in Practice: Steering, Storm Tracks, and Turbulence - Foundations"
 ],
 "Compounded": [
  "The Skew-T Log-P Diagram: A Forecaster's Sounding - Compounded",
  "Thunderstorm Forecasting: Ingredients and Severe Parameters - Compounded",
  "Fog Forecasting: Radiation, Advection, and Valley Fog - Compounded",
  "Tornadoes: Formation, the Enhanced Fujita Scale, and Warning Signs - Compounded",
  "Hail, Damaging Winds, and Derechos: Supercells and Squall Lines - Compounded",
  "Lightning in Practice: Detection Networks and Safety - Compounded",
  "Winter Storm Forecasting: Snow Ratios, Blizzards, and Ice Storms - Compounded",
  "Heat and Cold Extremes: The Heat Index, Wind Chill, and Extreme Warnings - Compounded",
  "Lake-Effect Snow: The Great Lakes Snow Machine - Compounded",
  "Mountain Weather: Orographic Lift, Chinook Winds, and Mountain Waves - Compounded",
  "Marine Meteorology: The Beaufort Scale, Waves, and Marine Forecasts - Compounded",
  "Tropical Meteorology in Practice: The ITCZ, Tropical Waves, and Monsoons - Compounded",
  "Fire Weather: Red Flag Warnings and the Haines Index - Compounded",
  "Agricultural Meteorology: Growing Degree Days and Frost Forecasting - Compounded",
  "Radar Interpretation: Reflectivity, Velocity Couplets, and Hook Echoes - Compounded",
  "Hurricane Forecasting: Track Models, the Cone, and Storm Surge - Compounded",
  "Satellite Interpretation: Visible, Infrared, Water Vapor, and the Dvorak Technique - Compounded",
  "Nowcasting: Mesoscale Analysis and Storm-Scale Warning - Compounded"
 ],
 "Advanced": [
  "Numerical Weather Prediction in Practice: Models, Grids, and Spin-Up - Advanced",
  "Ensemble Forecasting: Spaghetti Plots and Probabilistic Thinking - Advanced",
  "Aviation Meteorology: METAR, TAF, and In-Flight Hazards - Advanced",
  "Statistical Post-Processing: Model Output Statistics and Downscaling - Advanced",
  "Forecast Verification: Contingency Tables, POD, FAR, and the Brier Score - Advanced",
  "Hydrologic Outlooks: SPI, Drought, and Flood Forecasting Practice - Advanced",
  "Weather Communication: Watches, Warnings, Spotters, and the Warning Process - Advanced",
  "Frontiers of Meteorology: AI Forecasting, Warn-on-Forecast, and What's Next - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Meteorology Study — "+safe+"\n"
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
    name:topic+' — meteorology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A meteorology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"meteorology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-meteorology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('meteorology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
