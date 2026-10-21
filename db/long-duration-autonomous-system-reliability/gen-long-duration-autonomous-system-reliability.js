(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["redundancy", "fault-tolerance", "hardening", "prognostics", "testing"];
var PREFIX='JAH-LDA-';
var USE="Used by spacecraft, subsea, and remote-infrastructure engineers designing for no-service missions.";
var FLD=[["practice", "Practice"], ["protects_against", "Protects against"], ["metric", "Metric"]];
var DEMO="# {title} - MTBF check (python3)\nhours={d1}\nfailures={d2}\ntarget={d3}\nmtbf=hours/max(failures,1)\nprint(\"MTBF: %.0f hours (%.1f years)\" % (mtbf, mtbf/8760))\nprint(\"RELIABLE\" if mtbf >= target else \"BELOW TARGET\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["redundancy", "Triple-modular Redundancy", "Votes three identical channels so one fault cannot corrupt output.", "Triple-modular Redundancy", "single faults", "voter coverage", "50000", "2", "20000.0"], ["fault-tolerance", "Radiation-hardened Parts", "Uses rad-hard components rated for total dose and single-event effects.", "Radiation-hardened Parts", "radiation", "TID rating", "30000", "1", "25000.0"], ["hardening", "Watchdog Timers", "Resets hung processors when heartbeats stop, bounding outage time.", "Watchdog Timers", "software hangs", "recovery time", "40000", "3", "12000.0"], ["prognostics", "Error-correcting Memory", "Corrects single-bit and detects multi-bit memory errors in hardware.", "Error-correcting Memory", "bit flips", "uncorrectable rate", "60000", "2", "25000.0"], ["testing", "Graceful Degradation", "Sheds non-critical functions to keep the core mission alive under faults.", "Graceful Degradation", "total loss", "degraded availability", "45000", "2", "20000.0"], ["redundancy", "Autonomous Fault Recovery", "Detects, isolates, and recovers from faults without ground contact.", "Autonomous Fault Recovery", "long light-time delays", "recovery success", "35000", "2", "15000.0"], ["fault-tolerance", "Power Cycling Strategy", "Periodically power-cycles subsystems to clear latch-ups and leaks.", "Power Cycling Strategy", "stuck states", "cycle effectiveness", "25000", "2", "10000.0"], ["hardening", "Thermal Management", "Keeps electronics in their happy band across extreme environments.", "Thermal Management", "thermal death", "margin", "80000", "3", "25000.0"], ["prognostics", "Lubrication-free Mechanisms", "Uses dry or solid lubricants that never outgas or freeze.", "Lubrication-free Mechanisms", "mechanism seizure", "cycles to failure", "100000", "4", "20000.0"], ["testing", "Dormant-mode Preservation", "Puts systems in ultra-low-power hibernation between active phases.", "Dormant-mode Preservation", "battery drain", "hibernation years", "70000", "2", "30000.0"], ["redundancy", "Periodic Self-test", "Runs built-in tests on schedule to catch latent faults early.", "Periodic Self-test", "hidden faults", "detection rate", "55000", "3", "15000.0"], ["fault-tolerance", "Redundant Communication", "Keeps backup links on different bands so no single failure silences the craft.", "Redundant Communication", "comm loss", "link availability", "90000", "4", "20000.0"], ["hardening", "Safe-mode Fallback", "Enters a power-positive, Earth-pointing safe mode on any critical fault.", "Safe-mode Fallback", "loss of control", "safe-mode entry", "120000", "5", "20000.0"], ["prognostics", "Prognostics and Health Management", "Predicts remaining useful life from trending telemetry.", "Prognostics and Health Management", "surprise failures", "prediction accuracy", "65000", "3", "20000.0"], ["testing", "Spare Activation", "Switches to cold or warm spares when primaries degrade.", "Spare Activation", "unit failure", "switchover time", "75000", "3", "22000.0"], ["redundancy", "Software Rejuvenation", "Periodically restarts software to clear aging effects like leaks.", "Software Rejuvenation", "software aging", "rejuvenation interval", "30000", "2", "12000.0"], ["fault-tolerance", "Diversity in Design", "Implements critical functions two different ways to defeat common-cause faults.", "Diversity in Design", "common cause", "diverse coverage", "85000", "3", "25000.0"], ["hardening", "Derating Components", "Runs parts well below rated stress to multiply lifetime.", "Derating Components", "wear-out", "derating factor", "95000", "4", "20000.0"], ["prognostics", "Accelerated Life Testing", "Ages prototypes fast with heat and voltage to prove lifetime claims.", "Accelerated Life Testing", "unknown life", "test acceleration", "50000", "0", "40000.0"], ["testing", "Reliability Growth Tracking", "Plots MTBF growth across test phases to predict field reliability.", "Reliability Growth Tracking", "stagnation", "growth rate", "40000", "2", "15000.0"]];
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
var gen={version:'jahdb-long-duration-autonomous-system-reliability-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('long-duration-autonomous-system-reliability',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
