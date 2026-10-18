(function(){'use strict';
/* JAH The Railway Systems Signature Database generator — jahdb-railway-systems-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RLSYS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Sworn Road — The Signature View (Signature Edition) - Foundations",
  "The True Path — Signature Track (Signature Edition) - Foundations",
  "The Measure Between — Signature Gauge (Signature Edition) - Foundations",
  "The Coin of Contact — Signature Wheel-Rail (Signature Edition) - Foundations",
  "The Binding Oath — Signature Couplers (Signature Edition) - Foundations",
  "The Failing-Safe — Signature Braking (Signature Edition) - Foundations",
  "The Iron Horse — Signature Diesel (Signature Edition) - Foundations",
  "The Wire's Gift — Signature Electric Traction (Signature Edition) - Foundations",
  "The Rolling Inn — Signature Passenger Cars (Signature Edition) - Foundations",
  "The Beasts of Burden — Signature Freight Wagons (Signature Edition) - Foundations",
  "The Meeting House — Signature Stations (Signature Edition) - Foundations",
  "The Square Law — Signature Braking Math (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "The Blocked Road — Signature Block Signaling (Signature Edition) - Compounded",
  "The Referee — Signature Interlocking (Signature Edition) - Compounded",
  "The Master Plan — Signature Timetables (Signature Edition) - Compounded",
  "The Living Command — Signature Dispatching (Signature Edition) - Compounded",
  "The Sorting Ground — Signature Freight Yards (Signature Edition) - Compounded",
  "The Self-Movers — Signature Multiple Units (Signature Edition) - Compounded",
  "The Perilous Meeting — Signature Level Crossings (Signature Edition) - Compounded",
  "The Path's Renewal — Signature Track Maintenance (Signature Edition) - Compounded",
  "The High Grid — Signature Electrification (Signature Edition) - Compounded",
  "The Paid Promise — Signature Ticketing (Signature Edition) - Compounded",
  "The Rested Crew — Signature Crew Scheduling (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Unsleeping Guardian — Signature Train Control (Signature Edition) - Advanced",
  "The Moving Rooms — Signature CBTC (Signature Edition) - Advanced",
  "The Swift Road — Signature High-Speed (Signature Edition) - Advanced",
  "The Loom of Time — Signature Network Optimization (Signature Edition) - Advanced",
  "The Banking of Curves — Signature Geometry (Signature Edition) - Advanced",
  "The Layered Shield — Signature Railway Safety (Signature Edition) - Advanced",
  "The Two-Mode Road — Signature Intermodal (Signature Edition) - Advanced",
  "The Ledger of the Road — Signature Railway Economics (Signature Edition) - Advanced",
  "The Open Door — Signature Accessibility (Signature Edition) - Advanced",
  "The Floating Future — Signature Maglev and Beyond (Signature Edition) - Advanced",
  "The Keeper of the Road — Signature Mastery (Signature Edition) - Advanced",
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('railway-systems-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
