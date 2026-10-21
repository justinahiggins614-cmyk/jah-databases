(function(){'use strict';
/* JAH The Delta-V Spaceflight Signature Database generator — jahdb-delta-v-spaceflight-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Delta-V Ladder \u2014 Foundations",
  "The Perfect Burn Principle \u2014 Foundations",
  "Signature Mass-Fraction Thinking \u2014 Foundations",
  "The Three-Tank Rule \u2014 Foundations",
  "Reading Velocity Like a Map \u2014 Foundations",
  "The Patience Burn \u2014 Foundations",
  "Signature Gravity-Turn Doctrine \u2014 Foundations",
  "The Capture-First Rule \u2014 Foundations",
  "Signature Propellant Ledger Method \u2014 Foundations",
  "The Margin Doctrine \u2014 Foundations"
 ],
 "Compounded": [
  "Signature Hohmann-Plus Framework \u2014 Compounded",
  "The Signature Plane-Change Playbook \u2014 Compounded",
  "Signature Gravity-Assist Choreography \u2014 Compounded",
  "The Oberth Harvest \u2014 Compounded",
  "Signature Aerocapture Study \u2014 Compounded",
  "The Spiral Doctrine \u2014 Compounded",
  "Signature Isp-vs-Thrust Tradeoff Compass \u2014 Compounded",
  "The Signature Mars Architecture \u2014 Compounded",
  "The Signature Lunar Cycle \u2014 Compounded",
  "Signature Propellant-Depot Doctrine \u2014 Compounded",
  "The Signature Oberth-Elliptic \u2014 Compounded",
  "Signature Stationkeeping Doctrine \u2014 Compounded"
 ],
 "Advanced": [
  "The Signature Patched-Conic Workbook \u2014 Advanced",
  "Signature Porkchop Reading Method \u2014 Advanced",
  "The Signature Grand Tour Study \u2014 Advanced",
  "Signature Mass-Fraction Ceiling Analysis \u2014 Advanced",
  "The Signature Interstellar Ladder \u2014 Advanced",
  "Signature Combined-Maneuver Optimizer \u2014 Advanced",
  "The Signature Mission Ledger \u2014 Advanced",
  "The Signature Axiom Set \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Delta-V Signature Study \u2014 "+safe+"\n"
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
    name:topic+' \u2014 delta-v signature record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A delta-v signature record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"delta-v-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-delta-v-spaceflight-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('delta-v-spaceflight-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
