(function(){'use strict';
/* JAH The Simulation Tools Database generator — jahdb-simulation-tools-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SIM-";
var FIELDS=["simulation"];
var TOPICS={
 "simulation": [
  "Hardware Emulators \u2014 simulation",
  "CPU Emulators \u2014 simulation",
  "Terminal Emulators \u2014 simulation",
  "Flight Simulators \u2014 simulation",
  "Circuit Simulators \u2014 simulation",
  "Physics Simulators \u2014 simulation",
  "Network Simulators \u2014 simulation",
  "Isolation Sandboxes \u2014 simulation",
  "Type-1 Hypervisors \u2014 simulation",
  "Type-2 Hypervisors \u2014 simulation",
  "Virtual Machines \u2014 simulation",
  "Container Runtimes \u2014 simulation",
  "Testbeds \u2014 simulation",
  "Prototyping Engines \u2014 simulation",
  "Physics Engines \u2014 simulation",
  "Rendering Engines \u2014 simulation",
  "2D Engines \u2014 simulation",
  "3D Engines \u2014 simulation",
  "Audio Engines \u2014 simulation",
  "Inference Engines \u2014 simulation",
  "Neural Network Engines \u2014 simulation",
  "Execution Engines \u2014 simulation",
  "Rule Engines \u2014 simulation",
  "Workflow Engines \u2014 simulation",
  "Policy Engines \u2014 simulation",
  "Mock Service Frameworks \u2014 simulation",
  "Device Farms \u2014 simulation",
  "Render Farms \u2014 simulation",
  "Build Farms \u2014 simulation",
  "Haptic Simulators \u2014 simulation",
  "VR Toolkits \u2014 simulation",
  "Digital Twins \u2014 simulation",
  "Chaos Engines \u2014 simulation",
  "Load Balancer Sims \u2014 simulation",
  "Cache Simulators \u2014 simulation",
  "CPU Simulators \u2014 simulation",
  "Network Emulators \u2014 simulation",
  "API Simulators \u2014 simulation",
  "Data Simulators \u2014 simulation",
  "Environment Simulators \u2014 simulation",
  "Economic Simulators \u2014 simulation",
  "Climate Simulators \u2014 simulation",
  "Traffic Simulators \u2014 simulation",
  "Crowd Simulators \u2014 simulation",
  "Epidemic Simulators \u2014 simulation",
  "Quantum Simulators \u2014 simulation",
  "Molecular Simulators \u2014 simulation",
  "Structural Simulators \u2014 simulation",
  "Fluid Simulators \u2014 simulation",
  "Electromagnetic Simulators \u2014 simulation",
  "Hardware-in-Loop Rigs \u2014 simulation",
  "Software-in-Loop Rigs \u2014 simulation",
  "Robot Simulators \u2014 simulation",
  "Autonomous Driving Sims \u2014 simulation",
  "Drone Simulators \u2014 simulation",
  "Factory Simulators \u2014 simulation",
  "Power Grid Simulators \u2014 simulation",
  "Chemical Process Sims \u2014 simulation",
  "Building Simulators \u2014 simulation",
  "Acoustic Simulators \u2014 simulation"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Simulation Tools — "+safe+"\n"
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
    name:topic+' — simulation tool record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A simulation tool record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-simulation-tools-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('simulation-tools',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
