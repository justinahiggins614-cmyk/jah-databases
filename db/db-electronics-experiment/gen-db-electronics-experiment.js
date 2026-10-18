(function(){'use strict';
/* JAH The Electronics Experiment Database generator — jahdb-db-electronics-experiment-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ELX-";
var FIELDS=["Circuit Basics","Components","Projects"];
var TOPICS={
 "Circuit Basics": [
  "Safety First: Respect Electricity - Circuit Basics",
  "Your First Circuit: Battery + LED - Circuit Basics",
  "Voltage, Current, Resistance - Circuit Basics",
  "Reading Resistor Codes - Circuit Basics",
  "Series vs Parallel - Circuit Basics",
  "Using a Multimeter - Circuit Basics",
  "Breadboards: Solderless Building - Circuit Basics",
  "Switches: Controlling Flow - Circuit Basics",
  "Ohm's Law in Practice - Circuit Basics",
  "Short Circuits: The Enemy - Circuit Basics",
  "Capacitors: Tiny Batteries - Circuit Basics",
  "Diodes: One-Way Streets - Circuit Basics"
 ],
 "Components": [
  "Transistors: Electronic Switches - Components",
  "555 Timer: The Classic Chip - Components",
  "Sensors: Electronics That Feel - Components",
  "Motors: Spinning With Electricity - Components",
  "Buzzers and Speakers - Components",
  "Seven-Segment Displays - Components",
  "Relays: Heavy-Duty Switches - Components",
  "Voltage Regulators - Components",
  "Project: Blinking LED - Components",
  "Project: Night Light - Components"
 ],
 "Projects": [
  "Project: Temperature Display - Projects",
  "Project: Motion Alarm - Projects",
  "Project: Plant Watering Reminder - Projects",
  "Project: Dice Roller - Projects",
  "Project: Servo Sweep - Projects",
  "Project: Light Theremin - Projects",
  "Project: Reaction Timer - Projects",
  "Project: Smart Doorbell - Projects",
  "Project: Weather Station - Projects",
  "Capstone: Your Invention - Projects",
  "Soldering: Making It Permanent - Projects",
  "Reading Schematics - Projects"
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
var gen={version:'jahdb-db-electronics-experiment-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-electronics-experiment',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
