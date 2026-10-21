(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["life-support", "power", "thermal", "safety", "logistics"];
var PREFIX='JAH-SHSD-S-';
var USE="Used by habitat designers and mission planners to find single points of failure.";
var FLD=[["system", "System"], ["depends_on", "Depends on"], ["criticality", "Criticality"]];
var DEMO="# {title} - dependency depth (python3)\ndeps={d1}\nmax_depth={d2}\nprint(\"dependency chain:\", \" -> \".join(deps))\nprint(\"depth %d\" % len(deps))\nprint(\"ACCEPTABLE\" if len(deps) <= max_depth else \"TOO DEEP - add redundancy\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["life-support", "ECLSS Air Revitalization", "Removes CO2 and supplies oxygen; the most critical life-support function.", "ECLSS Air Revitalization", "power, thermal", "critical", "['power', 'thermal', 'air revitalization']", "4", "'ECLSS'"], ["power", "Water Recovery", "Reclaims water from humidity and urine; loss means rationing within days.", "Water Recovery", "power", "critical", "['power', 'water recovery']", "4", "'Water'"], ["thermal", "Power Distribution", "Routes power from arrays or reactors to every subsystem.", "Power Distribution", "generation", "critical", "['generation', 'distribution']", "4", "'Power'"], ["safety", "Thermal Control", "Rejects waste heat via radiators; overheating kills electronics fast.", "Thermal Control", "power, radiators", "critical", "['power', 'radiators', 'thermal control']", "4", "'Thermal'"], ["logistics", "Pressure Shell", "Holds breathable atmosphere against vacuum.", "Pressure Shell", "structure", "critical", "['structure', 'pressure shell']", "4", "'Shell'"], ["life-support", "Radiation Shielding", "Water walls or regolith protect crew from solar and cosmic radiation.", "Radiation Shielding", "structure, water", "high", "['structure', 'shielding']", "4", "'Shielding'"], ["power", "Food Production", "Greenhouses supplement stored food for long missions.", "Food Production", "water, power, light", "medium", "['water', 'power', 'greenhouse']", "4", "'Food'"], ["thermal", "Waste Management", "Processes solid waste and trash without contaminating the habitat.", "Waste Management", "power", "medium", "['power', 'waste processing']", "4", "'Waste'"], ["safety", "Fire Detection", "Detects smoke and heat early; fire in a sealed habitat is catastrophic.", "Fire Detection", "power, comms", "critical", "['power', 'detection', 'suppression']", "4", "'Fire'"], ["logistics", "Medical Bay", "Treats injuries and illness with telemedicine backup.", "Medical Bay", "power, comms", "high", "['power', 'comms', 'medical']", "4", "'Medical'"], ["life-support", "Communications", "Links to Earth and surface assets for ops and crew welfare.", "Communications", "power", "high", "['power', 'comms']", "4", "'Comms'"], ["power", "Navigation", "Knows position and attitude for maneuvers and pointing.", "Navigation", "power, sensors", "high", "['power', 'sensors', 'nav']", "4", "'Nav'"], ["thermal", "Docking Interface", "Standard interface for visiting vehicles and resupply.", "Docking Interface", "structure, power", "high", "['structure', 'docking']", "4", "'Docking'"], ["safety", "EVA Airlock", "Cycles crew and equipment between habitat and vacuum safely.", "EVA Airlock", "pressure shell, power", "high", "['shell', 'power', 'airlock']", "4", "'Airlock'"], ["logistics", "Lighting", "Full-spectrum lighting for crew health and plant growth.", "Lighting", "power", "medium", "['power', 'lighting']", "4", "'Lighting'"], ["life-support", "Humidity Control", "Keeps humidity in the comfort band, preventing mold and static.", "Humidity Control", "thermal, power", "medium", "['thermal', 'power', 'humidity']", "4", "'Humidity'"], ["power", "CO2 Scrubbing", "Removes carbon dioxide continuously; part of air revitalization.", "CO2 Scrubbing", "power", "critical", "['power', 'scrubbers']", "4", "'CO2'"], ["thermal", "O2 Generation", "Electrolyzes water to oxygen, closing the air loop.", "O2 Generation", "power, water", "critical", "['power', 'water', 'O2 gen']", "4", "'O2'"], ["safety", "Trace Contaminant Control", "Filters volatile organics and particulates from cabin air.", "Trace Contaminant Control", "power", "high", "['power', 'filters']", "4", "'TCC'"], ["logistics", "Emergency Egress", "Provides a survivable path to a return vehicle under any single failure.", "Emergency Egress", "structure", "critical", "['structure', 'egress']", "4", "'Egress'"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-space-habitat-systems-dependency-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('space-habitat-systems-dependency-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
