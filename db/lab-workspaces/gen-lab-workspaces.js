(function(){'use strict';
/* JAH The Lab Workspaces Database generator — jahdb-lab-workspaces-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LAB-";
var FIELDS=["workspace"];
var TOPICS={
 "workspace": [
  "Research Laboratories \u2014 workspace",
  "Development Workspaces \u2014 workspace",
  "Testbeds \u2014 workspace",
  "Sandboxes \u2014 workspace",
  "Workshops \u2014 workspace",
  "Studios \u2014 workspace",
  "Workbenches \u2014 workspace",
  "Workstations \u2014 workspace",
  "Terminals \u2014 workspace",
  "Dashboards \u2014 workspace",
  "Control Rooms \u2014 workspace",
  "Network Operations Centers \u2014 workspace",
  "Security Operations Centers \u2014 workspace",
  "War Rooms \u2014 workspace",
  "Command Centers \u2014 workspace",
  "Stations \u2014 workspace",
  "Bays \u2014 workspace",
  "Pods \u2014 workspace",
  "Hubs \u2014 workspace",
  "Clean Benches \u2014 workspace",
  "Darkrooms \u2014 workspace",
  "Anechoic Workstations \u2014 workspace",
  "Server Rooms \u2014 workspace",
  "Wiring Closets \u2014 workspace",
  "Demo Rooms \u2014 workspace",
  "Training Labs \u2014 workspace",
  "Usability Labs \u2014 workspace",
  "Conference Bridges \u2014 workspace",
  "Hot Desks \u2014 workspace",
  "Maker Benches \u2014 workspace",
  "Repair Cafes \u2014 workspace",
  "Calibration Stations \u2014 workspace",
  "Metrology Benches \u2014 workspace",
  "Soldering Stations \u2014 workspace",
  "Rework Stations \u2014 workspace",
  "Test Jigs \u2014 workspace",
  "Burn-In Racks \u2014 workspace",
  "Prototype Bays \u2014 workspace",
  "Integration Labs \u2014 workspace",
  "Compatibility Labs \u2014 workspace",
  "Performance Labs \u2014 workspace",
  "Security Labs \u2014 workspace",
  "Forensics Workstations \u2014 workspace",
  "Recovery Benches \u2014 workspace",
  "Archive Rooms \u2014 workspace",
  "Media Labs \u2014 workspace",
  "Broadcast Studios \u2014 workspace",
  "Podcast Booths \u2014 workspace",
  "Streaming Rigs \u2014 workspace",
  "VR Labs \u2014 workspace",
  "Robotics Bays \u2014 workspace",
  "Drone Cages \u2014 workspace",
  "Field Kits \u2014 workspace",
  "Mobile Labs \u2014 workspace",
  "Pop-Up Labs \u2014 workspace",
  "Classroom Labs \u2014 workspace",
  "Library Labs \u2014 workspace",
  "Community Labs \u2014 workspace",
  "Corporate Labs \u2014 workspace",
  "University Labs \u2014 workspace",
  "Government Labs \u2014 workspace"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Lab Workspaces — "+safe+"\n"
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
    name:topic+' — lab workspace record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A lab workspace record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-lab-workspaces-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('lab-workspaces',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
