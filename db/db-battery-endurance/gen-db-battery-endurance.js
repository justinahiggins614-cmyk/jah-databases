(function(){'use strict';
/* JAH The Battery Endurance Database generator — jahdb-db-battery-endurance-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BE-";
var FIELDS=["Device Endurance","EV & Transport","Power & Tools"];
var TOPICS={
 "Device Endurance": [
  "Phone A vs Phone B: Flagship Battery - Device Endurance",
  "Laptop: Ultrabook vs Workstation - Device Endurance",
  "Earbuds vs Headphones: Audio Battery - Device Endurance",
  "Tablet vs Laptop: Screen Time - Device Endurance",
  "Smartwatch vs Fitness Band: Wrist - Device Endurance",
  "E-Reader vs Tablet: Battery Endurance - Device Endurance",
  "Camera: Mirrorless vs DSLR - Device Endurance",
  "Drone: Consumer vs Pro - Device Endurance",
  "Handheld Console vs Phone: Gaming - Device Endurance",
  "Flashlight: LED vs Old Bulb - Device Endurance",
  "Power Bank: Big vs Small - Device Endurance"
 ],
 "EV & Transport": [
  "EV: Long Range vs Standard - EV & Transport",
  "E-Bike vs E-Scooter: Range - EV & Transport",
  "Electric Mower vs Gas: Yard - EV & Transport",
  "EV vs Hybrid: Road Trip - EV & Transport",
  "Electric Boat vs Diesel: Water - EV & Transport",
  "E-Skateboard vs E-Bike: Fun Range - EV & Transport",
  "Golf Cart vs UTV: Work Play - EV & Transport"
 ],
 "Power & Tools": [
  "Drill: 12V vs 18V - Power & Tools",
  "Chainsaw: Battery vs Gas - Power & Tools",
  "Leaf Blower: Battery vs Gas - Power & Tools",
  "Mower: Robot vs Push Battery - Power & Tools",
  "Impact Wrench: Compact vs High-Torque - Power & Tools",
  "Grinder: 4.5in Battery vs Corded - Power & Tools",
  "Nailer: Battery vs Pneumatic - Power & Tools",
  "Saw: Track vs Circular Battery - Power & Tools",
  "Multitool: Oscillating Battery vs Corded - Power & Tools",
  "Inflator: Battery vs 12V Plug - Power & Tools",
  "Work Light: Battery vs Corded - Power & Tools",
  "Hedge Trimmer: Battery vs Gas - Power & Tools",
  "Pressure Washer: Battery vs Electric - Power & Tools",
  "Soldering: Battery vs Corded Iron - Power & Tools",
  "Fan: Battery vs Mains - Power & Tools",
  "Jump Starter: Lithium vs Lead - Power & Tools"
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
var gen={version:'jahdb-db-battery-endurance-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-battery-endurance',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
