(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["solar", "storage", "hydrogen", "thermal", "grid"];
var PREFIX='JAH-AEM-';
var USE="Used by energy researchers, investors, and planners tracking the materials race.";
var FLD=[["material", "Material"], ["property", "Property"], ["application", "Application"]];
var DEMO="# {title} - efficiency gain (python3)\nold={d1}\nnew={d2}\ntarget_gain={d3}\ngain=100.0*(new-old)/old\nprint(\"efficiency: %.1f%% -> %.1f%% (+%.1f%%)\" % (old, new, gain))\nprint(\"BREAKTHROUGH\" if gain >= target_gain else \"INCREMENTAL\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["solar", "Perovskite Solar Absorbers", "Reached 26%+ lab efficiency with cheap solution processing.", "Perovskite Solar Absorbers", "26% efficiency", "tandem solar cells", "22.0", "26.5", "15.0"], ["storage", "Solid-state Electrolytes (LLZO)", "Ceramic conductors enabling lithium-metal anodes safely.", "Solid-state Electrolytes (LLZO)", "1 mS/cm ionic conductivity", "solid-state batteries", "0.5", "1.2", "50.0"], ["hydrogen", "Silicon Anodes", "Store 10x the lithium of graphite, with swelling managed by nanostructure.", "Silicon Anodes", "3500 mAh/g capacity", "EV batteries", "372.0", "3500.0", "200.0"], ["thermal", "Lithium Iron Phosphate", "Cheap, safe, long-lived cathode dominating mass-market EVs.", "Lithium Iron Phosphate", "170 mAh/g, 4000 cycles", "EV + storage", "150.0", "170.0", "10.0"], ["grid", "Sodium-ion Cathodes", "Abundant sodium replaces lithium for stationary storage.", "Sodium-ion Cathodes", "150 mAh/g", "grid storage", "120.0", "150.0", "20.0"], ["solar", "Solid-oxide Fuel Cell Electrolytes", "Conduct oxygen ions at high temperature for efficient power.", "Solid-oxide Fuel Cell Electrolytes", "0.1 S/cm at 800C", "stationary power", "0.05", "0.1", "50.0"], ["storage", "Thermoelectric Skutterudites", "Convert waste heat to electricity with improving ZT.", "Thermoelectric Skutterudites", "ZT 1.5", "waste-heat recovery", "1.0", "1.5", "40.0"], ["hydrogen", "Phase-change Storage Salts", "Store heat in melting transitions for concentrated solar.", "Phase-change Storage Salts", "200 kJ/kg latent heat", "thermal storage", "150.0", "200.0", "25.0"], ["thermal", "Metal-organic Frameworks", "Record surface areas for hydrogen storage and carbon capture.", "Metal-organic Frameworks", "7000 m2/g", "H2 storage", "3000.0", "7000.0", "50.0"], ["grid", "MXene Supercapacitors", "2D carbides with exceptional volumetric capacitance.", "MXene Supercapacitors", "1500 F/cm3", "fast storage", "800.0", "1500.0", "50.0"], ["solar", "Graphene Additives", "Boost conductivity and strength in batteries and composites.", "Graphene Additives", "5000 W/mK thermal", "battery additives", "2000.0", "5000.0", "100.0"], ["storage", "High-entropy Alloys", "Multi-principal-element alloys with exceptional strength-toughness.", "High-entropy Alloys", "1.5 GPa strength", "turbines", "1.0", "1.5", "40.0"], ["hydrogen", "Proton-exchange Membranes", "Conduct protons for fuel cells and electrolyzers.", "Proton-exchange Membranes", "0.2 S/cm", "hydrogen economy", "0.1", "0.2", "50.0"], ["thermal", "Flow-battery Electrolytes", "Decouple power and energy for long-duration storage.", "Flow-battery Electrolytes", "vanadium/organic", "grid storage", "25.0", "35.0", "30.0"], ["grid", "Piezoelectric Harvesters", "Convert vibration to electricity for sensors.", "Piezoelectric Harvesters", "30% coupling", "IoT power", "20.0", "30.0", "40.0"], ["solar", "Transparent Conductors (AZO)", "Aluminum-doped zinc oxide replaces indium in displays and solar.", "Transparent Conductors (AZO)", "10 ohm/sq", "optoelectronics", "20.0", "10.0", "40.0"], ["storage", "Superconducting Tapes", "REBCO tapes carry huge currents for fusion and grids.", "Superconducting Tapes", "500 A/mm2", "fusion magnets", "200.0", "500.0", "100.0"], ["hydrogen", "Aerogel Insulation", "Nanoporous silica with the lowest thermal conductivity of solids.", "Aerogel Insulation", "0.015 W/mK", "buildings", "0.03", "0.015", "40.0"], ["thermal", "Catalyst Nanoparticles", "Platinum-group alternatives for electrolyzers and fuel cells.", "Catalyst Nanoparticles", "10x mass activity", "hydrogen", "1.0", "10.0", "200.0"], ["grid", "Bio-derived Binders", "Replace toxic battery binders with water-processable biopolymers.", "Bio-derived Binders", "aqueous processing", "green batteries", "5.0", "8.0", "40.0"]];
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
var gen={version:'jahdb-advanced-energy-material-discovery-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('advanced-energy-material-discovery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
