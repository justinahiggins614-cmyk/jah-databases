(function(){'use strict';
/* JAH The Best Tool for the Job Signature Database generator — jahdb-db-best-tool-for-the-job-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BTFTJS-";
var FIELDS=["Workshop Tools","Kitchen & Home Tools","Digital Tools"];
var TOPICS={
 "Workshop Tools": [
  "Hammer vs Nail Gun: Fastening (Signature Edition) - Workshop Tools",
  "Hand Saw vs Circular Saw: Cutting Wood (Signature Edition) - Workshop Tools",
  "Drill vs Impact Driver: Driving Screws (Signature Edition) - Workshop Tools",
  "Wrench vs Socket Set: Turning Bolts (Signature Edition) - Workshop Tools",
  "Screwdriver vs Drill: Simple Driving (Signature Edition) - Workshop Tools",
  "Level: Spirit vs Laser (Signature Edition) - Workshop Tools",
  "Tape Measure vs Laser Measure: Measuring (Signature Edition) - Workshop Tools",
  "Chisel vs Router: Wood Shaping (Signature Edition) - Workshop Tools",
  "Sander: Hand vs Power (Signature Edition) - Workshop Tools",
  "Clamp: Bar vs Spring (Signature Edition) - Workshop Tools",
  "Sawhorse vs Workbench: Work Support (Signature Edition) - Workshop Tools",
  "Multimeter vs Test Light: Electrical (Signature Edition) - Workshop Tools",
  "Jigsaw vs Coping Saw: Curves (Signature Edition) - Workshop Tools"
 ],
 "Kitchen & Home Tools": [
  "Chef's Knife vs Paring Knife: Kitchen (Signature Edition) - Kitchen & Home Tools",
  "Cast Iron vs Non-Stick: Pans (Signature Edition) - Kitchen & Home Tools",
  "Stand Mixer vs Hand Mixer: Baking (Signature Edition) - Kitchen & Home Tools",
  "French Press vs Pour-Over: Coffee (Signature Edition) - Kitchen & Home Tools",
  "Broom vs Vacuum: Floors (Signature Edition) - Kitchen & Home Tools",
  "Mop vs Steam Mop: Mopping (Signature Edition) - Kitchen & Home Tools",
  "Ladder vs Step Stool: Reaching (Signature Edition) - Kitchen & Home Tools",
  "Plunger vs Snake: Drains (Signature Edition) - Kitchen & Home Tools",
  "Iron vs Steamer: Wrinkles (Signature Edition) - Kitchen & Home Tools",
  "Sewing Machine vs Hand Stitch: Mending (Signature Edition) - Kitchen & Home Tools"
 ],
 "Digital Tools": [
  "Spreadsheet vs Database: Data (Signature Edition) - Digital Tools",
  "Pen & Paper vs Notes App: Notes (Signature Edition) - Digital Tools",
  "Calculator vs Spreadsheet: Math (Signature Edition) - Digital Tools",
  "Email vs Chat: Communication (Signature Edition) - Digital Tools",
  "Camera vs Phone: Photos (Signature Edition) - Digital Tools",
  "E-Reader vs Tablet: Best Reading Tool (Signature Edition) - Digital Tools",
  "Desktop vs Laptop: Computing (Signature Edition) - Digital Tools",
  "Wired vs Wireless: Connections (Signature Edition) - Digital Tools",
  "Notebook vs Whiteboard: Thinking (Signature Edition) - Digital Tools",
  "Alarm Clock vs Phone Alarm: Waking (Signature Edition) - Digital Tools",
  "Map App vs Paper Map: Navigation (Signature Edition) - Digital Tools"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Best Tool Study — "+safe+"\n"
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
    name:topic+' — tool selection record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tool selection record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"best-tool-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-best-tool-for-the-job-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-best-tool-for-the-job-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
