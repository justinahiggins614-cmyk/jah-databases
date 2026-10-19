(function(){'use strict';
/* JAH The Reusable Spaceplanes Future Technology Database — Signature Edition generator — jahdb-futuretech-65-reusable-spaceplanes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT65-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Reusable Spaceplanes — Silbervogel - the First Spaceplane Dream (Signature Edition)", "Reusable Spaceplanes — the X-15 - Wings to Space (Signature Edition)", "Reusable Spaceplanes — Dyna-Soar Canceled (Signature Edition)", "Reusable Spaceplanes — Wings Above 100 km (Signature Edition)", "Reusable Spaceplanes — the Shuttle Approved (Signature Edition)", "Reusable Spaceplanes — STS-1 - the Orbiter Flies (Signature Edition)", "Reusable Spaceplanes — Challenger (Signature Edition)", "Reusable Spaceplanes — Buran - the Robot Shuttle (Signature Edition)", "Reusable Spaceplanes — Columbia (Signature Edition)", "Reusable Spaceplanes — SpaceShipOne Wins the X Prize (Signature Edition)", "Reusable Spaceplanes — X-37B - the Robot Spaceplane (Signature Edition)"], "Compounded": ["Reusable Spaceplanes — the Shuttle Retires (Signature Edition)", "Reusable Spaceplanes — Dream Chaser Takes Shape (Signature Edition)", "Reusable Spaceplanes — SABRE - Breathing to Orbit (Signature Edition)", "Reusable Spaceplanes — SpaceShipTwo Tests On (Signature Edition)", "Reusable Spaceplanes — the Enduring Robot (Signature Edition)", "Reusable Spaceplanes — Branson Flies (Signature Edition)", "Reusable Spaceplanes — Tenacity Takes Form (Signature Edition)", "Reusable Spaceplanes — Sierra Space Advances (Signature Edition)", "Reusable Spaceplanes — Tenacity Ready (Signature Edition)", "Reusable Spaceplanes — Stoke - the Reusable Upper Stage (Signature Edition)", "Reusable Spaceplanes — Spaceplanes Near Flight (Signature Edition)", "Reusable Spaceplanes — Radian - the SSTO Dream (Signature Edition)"], "Advanced": ["Reusable Spaceplanes — Dream Chaser Cargo Service (Signature Edition)", "Reusable Spaceplanes — Crewed Dream Chaser (Signature Edition)", "Reusable Spaceplanes — Point-to-Point Suborbital (Signature Edition)", "Reusable Spaceplanes — Rapid-Turnaround Spaceplanes (Signature Edition)", "Reusable Spaceplanes — Single-Stage-to-Orbit (Signature Edition)", "Reusable Spaceplanes — Orbital Spaceplane Fleets (Signature Edition)", "Reusable Spaceplanes — Routine Spaceplane Tourism (Signature Edition)", "Reusable Spaceplanes — Spaceplane Satellite Servicing (Signature Edition)", "Reusable Spaceplanes — 90-Minute Intercontinental (Signature Edition)", "Reusable Spaceplanes — Spaceplanes at Scale (Signature Edition)", "Reusable Spaceplanes — The Everyday Spaceplane - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Reusable Spaceplanes study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-65-reusable-spaceplanes-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-65-reusable-spaceplanes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
