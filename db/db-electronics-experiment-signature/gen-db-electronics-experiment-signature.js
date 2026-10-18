(function(){'use strict';
/* JAH The Electronics Experiment Signature Database generator — jahdb-db-electronics-experiment-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ELXS-";
var FIELDS=["Circuit Basics","Components","Projects"];
var TOPICS={
 "Circuit Basics": [
  "Safety First: Respect Electricity (Signature Edition) - Circuit Basics",
  "Your First Circuit: Battery + LED (Signature Edition) - Circuit Basics",
  "Voltage, Current, Resistance (Signature Edition) - Circuit Basics",
  "Reading Resistor Codes (Signature Edition) - Circuit Basics",
  "Series vs Parallel (Signature Edition) - Circuit Basics",
  "Using a Multimeter (Signature Edition) - Circuit Basics",
  "Breadboards: Solderless Building (Signature Edition) - Circuit Basics",
  "Switches: Controlling Flow (Signature Edition) - Circuit Basics",
  "Ohm's Law in Practice (Signature Edition) - Circuit Basics",
  "Short Circuits: The Enemy (Signature Edition) - Circuit Basics",
  "Capacitors: Tiny Batteries (Signature Edition) - Circuit Basics",
  "Diodes: One-Way Streets (Signature Edition) - Circuit Basics"
 ],
 "Components": [
  "Transistors: Electronic Switches (Signature Edition) - Components",
  "555 Timer: The Classic Chip (Signature Edition) - Components",
  "Sensors: Electronics That Feel (Signature Edition) - Components",
  "Motors: Spinning With Electricity (Signature Edition) - Components",
  "Buzzers and Speakers (Signature Edition) - Components",
  "Seven-Segment Displays (Signature Edition) - Components",
  "Relays: Heavy-Duty Switches (Signature Edition) - Components",
  "Voltage Regulators (Signature Edition) - Components",
  "Project: Blinking LED (Signature Edition) - Components",
  "Project: Night Light (Signature Edition) - Components"
 ],
 "Projects": [
  "Project: Temperature Display (Signature Edition) - Projects",
  "Project: Motion Alarm (Signature Edition) - Projects",
  "Project: Plant Watering Reminder (Signature Edition) - Projects",
  "Project: Dice Roller (Signature Edition) - Projects",
  "Project: Servo Sweep (Signature Edition) - Projects",
  "Project: Light Theremin (Signature Edition) - Projects",
  "Project: Reaction Timer (Signature Edition) - Projects",
  "Project: Smart Doorbell (Signature Edition) - Projects",
  "Project: Weather Station (Signature Edition) - Projects",
  "Capstone: Your Invention (Signature Edition) - Projects",
  "Soldering: Making It Permanent (Signature Edition) - Projects",
  "Reading Schematics (Signature Edition) - Projects"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Electronics Experiment Study — "+safe+"\n"
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
    name:topic+' — electronics lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A electronics lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"electronics-experiment-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-electronics-experiment-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-electronics-experiment-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
