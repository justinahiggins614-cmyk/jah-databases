(function(){'use strict';
/* JAH The Actuators and Sensors Signature Database generator — jahdb-actuators-sensors-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ACS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Are Actuators and Sensors: The Muscle and the Senses of Every Machine (Signature Edition) - Foundations",
  "The Energy Families of Motion: Electric, Hydraulic, and Pneumatic Power (Signature Edition) - Foundations",
  "DC Motors: The Spinning Workhorse of Machines (Signature Edition) - Foundations",
  "Torque, Speed, and Power: The Three Numbers Every Motor Lives By (Signature Edition) - Foundations",
  "What Sensors Do: Turning the Physical World into Numbers (Signature Edition) - Foundations",
  "Brushless DC Motors: Magnets That Switch Themselves (Signature Edition) - Foundations",
  "Stepper Motors: Motion in Counted Steps (Signature Edition) - Foundations",
  "Measurement Truth: Accuracy, Precision, Resolution, and Calibration (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Servo Motors and Drives: Closing the Loop on Motion (Signature Edition) - Compounded",
  "Gearboxes, Leadscrews, and Ballscrews: Trading Speed for Force (Signature Edition) - Compounded",
  "Solenoids and Contactors: The Electromagnetic Push and Pull (Signature Edition) - Compounded",
  "Voice Coils and Linear Motors: Force Without Gears (Signature Edition) - Compounded",
  "Hydraulic Actuators: Huge Force from Pressurized Oil (Signature Edition) - Compounded",
  "Pneumatic Actuators: Fast Muscle from Compressed Air (Signature Edition) - Compounded",
  "Piezoelectric Actuators: Crystal Precision for Tiny Moves (Signature Edition) - Compounded",
  "Shape-Memory Alloys: Metal That Remembers Its Shape (Signature Edition) - Compounded",
  "Magnetostrictive Actuators: Giant Magnetism, Tiny Stretch (Signature Edition) - Compounded",
  "Position Sensors: Encoders and Resolvers That Count Rotation (Signature Edition) - Compounded",
  "Force, Torque, and Strain: Weighing and Feeling the Load (Signature Edition) - Compounded",
  "Pressure Sensors: Feeling the Push of Fluids (Signature Edition) - Compounded",
  "Temperature Sensors: Thermocouples, RTDs, and Thermistors (Signature Edition) - Compounded",
  "Proximity and Distance: Ultrasonic, Infrared, and Capacitive Eyes (Signature Edition) - Compounded",
  "Vision Sensors: Cameras That Measure the World (Signature Edition) - Compounded",
  "IMUs: Accelerometers and Gyroscopes That Feel Motion (Signature Edition) - Compounded",
  "LIDAR and Radar: Mapping the World with Light and Radio (Signature Edition) - Compounded",
  "Tactile Sensors: Giving Machines a Sense of Touch (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Signal Conditioning: From Microvolts to Clean Data (Signature Edition) - Advanced",
  "ADCs and DACs: The Border Crossing Between Worlds (Signature Edition) - Advanced",
  "Talking to Chips: I2C, SPI, and CAN Buses (Signature Edition) - Advanced",
  "Sensor Fusion: Kalman and Complementary Filters (Signature Edition) - Advanced",
  "Sizing and Selection: Picking the Right Actuator and Sensor (Signature Edition) - Advanced",
  "Failure, Safety, and Maintenance: What Breaks and How to Know (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Actuators Sensors Study — "+safe+"\n"
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
    name:topic+' — actuators and sensors record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A actuators and sensors record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"actuators-sensors-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-actuators-sensors-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('actuators-sensors-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
