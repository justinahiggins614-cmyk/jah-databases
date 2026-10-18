(function(){'use strict';
/* JAH The Battery Endurance Signature Database generator — jahdb-db-battery-endurance-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BES-";
var FIELDS=["Device Endurance","EV & Transport","Power & Tools"];
var TOPICS={
 "Device Endurance": [
  "Phone A vs Phone B: Flagship Battery (Signature Edition) - Device Endurance",
  "Laptop: Ultrabook vs Workstation (Signature Edition) - Device Endurance",
  "Earbuds vs Headphones: Audio Battery (Signature Edition) - Device Endurance",
  "Tablet vs Laptop: Screen Time (Signature Edition) - Device Endurance",
  "Smartwatch vs Fitness Band: Wrist (Signature Edition) - Device Endurance",
  "E-Reader vs Tablet: Battery Endurance (Signature Edition) - Device Endurance",
  "Camera: Mirrorless vs DSLR (Signature Edition) - Device Endurance",
  "Drone: Consumer vs Pro (Signature Edition) - Device Endurance",
  "Handheld Console vs Phone: Gaming (Signature Edition) - Device Endurance",
  "Flashlight: LED vs Old Bulb (Signature Edition) - Device Endurance",
  "Power Bank: Big vs Small (Signature Edition) - Device Endurance"
 ],
 "EV & Transport": [
  "EV: Long Range vs Standard (Signature Edition) - EV & Transport",
  "E-Bike vs E-Scooter: Range (Signature Edition) - EV & Transport",
  "Electric Mower vs Gas: Yard (Signature Edition) - EV & Transport",
  "EV vs Hybrid: Road Trip (Signature Edition) - EV & Transport",
  "Electric Boat vs Diesel: Water (Signature Edition) - EV & Transport",
  "E-Skateboard vs E-Bike: Fun Range (Signature Edition) - EV & Transport",
  "Golf Cart vs UTV: Work Play (Signature Edition) - EV & Transport"
 ],
 "Power & Tools": [
  "Drill: 12V vs 18V (Signature Edition) - Power & Tools",
  "Chainsaw: Battery vs Gas (Signature Edition) - Power & Tools",
  "Leaf Blower: Battery vs Gas (Signature Edition) - Power & Tools",
  "Mower: Robot vs Push Battery (Signature Edition) - Power & Tools",
  "Impact Wrench: Compact vs High-Torque (Signature Edition) - Power & Tools",
  "Grinder: 4.5in Battery vs Corded (Signature Edition) - Power & Tools",
  "Nailer: Battery vs Pneumatic (Signature Edition) - Power & Tools",
  "Saw: Track vs Circular Battery (Signature Edition) - Power & Tools",
  "Multitool: Oscillating Battery vs Corded (Signature Edition) - Power & Tools",
  "Inflator: Battery vs 12V Plug (Signature Edition) - Power & Tools",
  "Work Light: Battery vs Corded (Signature Edition) - Power & Tools",
  "Hedge Trimmer: Battery vs Gas (Signature Edition) - Power & Tools",
  "Pressure Washer: Battery vs Electric (Signature Edition) - Power & Tools",
  "Soldering: Battery vs Corded Iron (Signature Edition) - Power & Tools",
  "Fan: Battery vs Mains (Signature Edition) - Power & Tools",
  "Jump Starter: Lithium vs Lead (Signature Edition) - Power & Tools"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Battery Endurance Study — "+safe+"\n"
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
    name:topic+' — battery comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A battery comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"battery-endurance-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-battery-endurance-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-battery-endurance-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
