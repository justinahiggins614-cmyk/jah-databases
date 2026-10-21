(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["thermal", "mechanical", "electrical", "environmental", "lifecycle"];
var PREFIX='JAH-SIO-S-';
var USE="Used by lab managers and field engineers to keep measurements valid and warranties intact.";
var FLD=[["limit", "Limit"], ["parameter", "Parameter"], ["range", "Range"]];
var DEMO="# {title} - in-range check (python3)\nvalue={d1}\nlo={d2}\nhi={d3}\nprint(\"value %.1f, envelope [%.1f, %.1f]\" % (value, lo, hi))\nprint(\"WITHIN ENVELOPE\" if lo <= value <= hi else \"OUT OF ENVELOPE\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["thermal", "Temperature Range", "Ambient temperatures where accuracy specs hold.", "Temperature Range", "temperature", "-10 to 40 C", "22.5", "-10.0", "40.0"], ["mechanical", "Humidity Range", "Relative humidity bounds before condensation or drift.", "Humidity Range", "humidity", "10-80% RH", "45.0", "10.0", "80.0"], ["electrical", "Vibration Limit", "Maximum vibration the instrument tolerates without measurement error.", "Vibration Limit", "vibration", "0.5 g RMS", "0.2", "0.0", "0.5"], ["environmental", "Pressure Range", "Atmospheric or process pressure bounds for valid operation.", "Pressure Range", "pressure", "80-110 kPa", "101.3", "80.0", "110.0"], ["lifecycle", "Voltage Range", "Supply voltage tolerance before regulation fails.", "Voltage Range", "supply", "+/-10%", "230.0", "207.0", "253.0"], ["thermal", "EMI Susceptibility", "Electromagnetic immunity level per IEC 61326.", "EMI Susceptibility", "EMI", "10 V/m", "6.0", "0.0", "10.0"], ["mechanical", "Altitude Limit", "Maximum altitude before cooling and insulation derate.", "Altitude Limit", "altitude", "2000 m", "350.0", "0.0", "2000.0"], ["electrical", "Warm-up Time", "Time to thermal equilibrium before specs apply.", "Warm-up Time", "warm-up", "30 min", "35.0", "30.0", "999.0"], ["environmental", "Duty Cycle", "Maximum on-time ratio before overheating.", "Duty Cycle", "duty", "50%", "40.0", "0.0", "50.0"], ["lifecycle", "Shock Limit", "Mechanical shock survival per IEC 60068.", "Shock Limit", "shock", "30 g 11 ms", "12.0", "0.0", "30.0"], ["thermal", "Ingress Protection", "Dust and water protection rating required for the deployment.", "Ingress Protection", "IP rating", "IP54", "54.0", "54.0", "68.0"], ["mechanical", "Magnetic Field Limit", "Stray field tolerance for sensitive detectors.", "Magnetic Field Limit", "B field", "1 mT", "0.4", "0.0", "1.0"], ["electrical", "Radiation Tolerance", "Total ionizing dose before electronics degrade.", "Radiation Tolerance", "TID", "10 krad", "4.0", "0.0", "10.0"], ["environmental", "Acoustic Noise Limit", "Lab noise ceiling for vibration-sensitive instruments.", "Acoustic Noise Limit", "noise", "55 dBA", "48.0", "0.0", "55.0"], ["lifecycle", "Thermal Ramp Rate", "Maximum allowed temperature change rate.", "Thermal Ramp Rate", "ramp", "2 C/min", "1.2", "0.0", "2.0"], ["thermal", "Power Quality", "THD and sag/swell limits for clean measurements.", "Power Quality", "mains", "<5% THD", "2.1", "0.0", "5.0"], ["mechanical", "Grounding Requirement", "Earth bonding resistance for safety and noise.", "Grounding Requirement", "ground", "< 1 ohm", "0.4", "0.0", "1.0"], ["electrical", "Airflow Requirement", "Cooling airflow for rack instruments.", "Airflow Requirement", "cooling", "100 CFM", "120.0", "100.0", "9999.0"], ["environmental", "Calibration Interval", "Maximum time between calibrations while specs are guaranteed.", "Calibration Interval", "interval", "12 months", "9.0", "0.0", "12.0"], ["lifecycle", "Storage Conditions", "Temperature and humidity bounds for powered-off storage.", "Storage Conditions", "storage", "-20 to 60 C", "25.0", "-20.0", "60.0"]];
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
var gen={version:'jahdb-scientific-instrument-operating-envelope-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-instrument-operating-envelope-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
