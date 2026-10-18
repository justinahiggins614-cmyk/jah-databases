(function(){'use strict';
/* JAH The Railway Systems Database generator — jahdb-railway-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RLSY-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Railway Systems Are — Industry Overview - Foundations",
  "Track — Rails, Sleepers, and Ballast - Foundations",
  "Track Gauge - Foundations",
  "Wheels and the Wheel-Rail Interface - Foundations",
  "Couplers — Joining Cars - Foundations",
  "Braking Systems - Foundations",
  "Diesel Locomotives - Foundations",
  "Electric Locomotives and Catenary - Foundations",
  "Passenger Cars - Foundations",
  "Freight Wagons - Foundations",
  "Railway Stations - Foundations",
  "Railway Math I — Braking Distance and Speed - Foundations",
 ],
 "Compounded": [
  "Block Signaling - Compounded",
  "Interlocking - Compounded",
  "Timetables and Scheduling - Compounded",
  "Dispatching and Train Control - Compounded",
  "Freight Operations and Yards - Compounded",
  "Multiple Units — EMU and DMU - Compounded",
  "Level Crossings - Compounded",
  "Track Maintenance — Tamping and Grinding - Compounded",
  "Electrification Systems - Compounded",
  "Ticketing and Fare Systems - Compounded",
  "Crew Scheduling - Compounded",
 ],
 "Advanced": [
  "ETCS and Positive Train Control - Advanced",
  "CBTC — Communications-Based Train Control - Advanced",
  "High-Speed Rail - Advanced",
  "Network Optimization - Advanced",
  "Track Geometry and Cant - Advanced",
  "Railway Safety Systems - Advanced",
  "Freight Logistics and Intermodal - Advanced",
  "Railway Economics - Advanced",
  "Accessibility in Rail - Advanced",
  "Maglev and Future Systems - Advanced",
  "Railway Mastery Review — Running the Whole Network - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\n"
   + "# Braking-distance structural sample calculator (railway systems)\n"
   + "v, a = 27.8, 0.9\n"
   + "d = v*v/(2*a)\n"
   + "print('sample speed m/s:', v)\n"
   + "print('sample braking distance m:', round(d,1))\n"
   + "assert d > 0\n"
   + "print('OK: structural sample demo ran')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — railway systems record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A railway systems record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"railway-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-railway-systems-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('railway-systems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
