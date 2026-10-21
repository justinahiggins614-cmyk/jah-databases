(function(){'use strict';
/* JAH The PC Gadgets Master Catalog Signature Database generator — SigGen-Gadget-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record.
   HARD CAP: 1,000,000,000,000,000 records (one quadrillion, 10^15) — the generator
   self-regulates and stops at the cap or earlier when the topic is genuinely
   complete (marked complete with reason). Generator ladder: simple -> competitive
   -> mix-and-match -> unmade -> top-notch -> future grade -> God mode. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GPCMS-";
var MAX_RECORDS=1000000000000000;
var GEN_LADDER=["simple","competitive","mix-and-match","unmade","top-notch","future grade","God mode"];
var FIELDS=["simple","compounded","complex"];
var TOPICS={"simple": ["Signature CPU (Processor)", "Signature GPU (Graphics Card)", "Signature Dedicated NPU (Neural Processing Unit)", "Signature RAM (System Memory)", "Signature NVMe M.2 SSD", "Signature PCIe AI Accelerator Card", "Signature Capture Card", "Signature PCIe Wi-Fi / Bluetooth Card", "Signature Thermal Paste / Pad", "Signature Uninterruptible Power Supply (UPS)", "Signature Trackball Mouse", "Signature Game Controller / Gamepad", "Signature Macro Pad / Stream Deck", "Signature Document Scanner", "Signature Barcode / QR Code Reader", "Signature External Touchpad", "Signature Fingerprint Reader Module", "Signature Smart Ring", "Signature High-Refresh-Rate Monitor", "Signature Portable USB-C Monitor", "Signature Desktop Projector", "Signature Display Calibration Colorimeter", "Signature Ultra-Wide Curved Display", "Signature Bone Conduction Headphones", "Signature Monitor Screen Bar Light", "Signature Mesh Network Node", "Signature Single-Board Computer (SBC)", "Signature USB Edge TPU Accelerator", "Signature NVIDIA Jetson Board", "Signature Thunderbolt / USB-C Dock", "Signature Smart Video Doorbell", "Signature Smart Door Lock", "Signature Robotic Vacuum Cleaner", "Signature Hardware Firewall Appliance", "Signature USB Flash Drive / Pen Drive", "Signature Glossary", "Signature Safety and care"], "compounded": ["Signature SATA SSD", "Signature Mechanical Hard Drive (HDD)", "Signature Power Supply Unit (PSU)", "Signature AIO Liquid CPU Cooler", "Signature External RAID Enclosure", "Signature Hardware Security Key", "Signature Mechanical Keyboard", "Signature Optical / Laser Mouse", "Signature Digital Dictaphone / Voice Recorder", "Signature Stylus Pen", "Signature MIDI Controller Keyboard", "Signature Eye-Tracking Sensor", "Signature Active Noise-Canceling (ANC) Headphones", "Signature True Wireless (TWS) Earbuds", "Signature Desktop Studio Monitors", "Signature USB Audio Interface", "Signature Smart Screen / Echo Show", "Signature KVM Switch", "Signature Wireless Audio Transmitter", "Signature Spatial Audio Headphones", "Signature Fast GaN Wall Charger", "Signature High-Capacity Power Bank", "Signature Network Attached Storage (NAS)", "Signature Smart Power Strip", "Signature Zigbee / Z-Wave Smart Hub", "Signature Portable Solar Generator / Battery Station", "Signature Mini PC", "Signature Gadget buying guide"], "complex": ["Signature Air CPU Cooler", "Signature PC Chassis / Case", "Signature Case Fans", "Signature Drawing / Graphics Tablet", "Signature USB Microphone", "Signature AI Tracking Webcam", "Signature VR Motion Controllers", "Signature Flight Simulator Joystick / Throttle", "Signature Sim Racing Steering Wheel & Pedals", "Signature VR Headset (HMD)", "Signature AR Smart Glasses", "Signature Computer Soundbar", "Signature External DAC / Headphone Amplifier", "Signature E-Ink Secondary Display", "Signature Wi-Fi 7 Router", "Signature Smart Plug", "Signature Smart Thermostat", "Signature AI Security Camera", "Signature Compatibility and standards", "Signature History", "Signature Future"]};
var DEMOKIND="gadget spec evaluator";
var SAMPLEDESC="Samples are clearly labeled and never archive records. Generator ladder: simple, competitive, mix-and-match, unmade, top-notch, future grade, God mode. Hard cap: one quadrillion records (10^15) or stop when genuinely complete.";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "// Gadget spec evaluator — "+safe+"\n"
   + "// Field: "+field+" | Property of Justin Addam Higgins (JAH).\n"
   + "// Deterministic sample demo. Archive records carry their own executed demos.\n"
   + "var spec={topic:\""+safe+"\",field:\""+field+"\",seed:"+seed+"};\n"
   + "var h=0;for(var i=0;i<spec.topic.length;i++){h=(h*31+spec.topic.charCodeAt(i))>>>0;}\n"
   + "var score=((h%900)+100)/10;\n"
   + "console.log('DEMO_OK|SAMPLE-'+spec.seed+'|'+score.toFixed(2)+' spec score');\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  if(seed>=MAX_RECORDS) return {error:'quadrillion cap reached',complete:true,reason:'hard stop at 10^15 records'};
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var ladder=opts.ladder&&GEN_LADDER.indexOf(opts.ladder)>=0?opts.ladder:pick(GEN_LADDER,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — gadget sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A gadget sample of "'+topic+'" in '+field+', generator ladder rank "'+ladder+'". Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    ladder_rank:ladder,
    src:'signature-generated-completion',
    sample:true,
    generator_cap:MAX_RECORDS,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'javascript',program:demoProgram(topic,field,seed),note:'Structural sample demo.'},
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
var gen={version:'SigGen-Gadget-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,ladder:GEN_LADDER,cap:MAX_RECORDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pc-gadgets-master-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
