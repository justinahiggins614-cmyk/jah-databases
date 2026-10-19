(function(){'use strict';
/* Signature Schleicher ASK 21 generator — jahdb-glider-ask-21-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GLASK-S-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Signature Schleicher ASK 21: Development Origins \u2014 foundations",
  "Signature Schleicher ASK 21: The Design Team \u2014 foundations",
  "Signature Schleicher ASK 21: First Flight \u2014 foundations",
  "Signature Schleicher ASK 21: Certification \u2014 foundations",
  "Signature Schleicher ASK 21: Entry Into Service \u2014 foundations",
  "Signature Schleicher ASK 21: Production History \u2014 foundations",
  "Signature Schleicher ASK 21: Notable Operators \u2014 foundations",
  "Signature Schleicher ASK 21: Famous Flights and Records \u2014 foundations",
  "Signature Schleicher ASK 21: Safety Record \u2014 foundations",
  "Signature Schleicher ASK 21: Legacy and Preservation \u2014 foundations",
 ],
 "compounded": [
  "Signature Schleicher ASK 21: Dimensions Overview \u2014 compounded",
  "Signature Schleicher ASK 21: Airframe and Materials \u2014 compounded",
  "Signature Schleicher ASK 21: Engines and Propulsion \u2014 compounded",
  "Signature Schleicher ASK 21: Fuel and Energy System \u2014 compounded",
  "Signature Schleicher ASK 21: Performance Envelope \u2014 compounded",
  "Signature Schleicher ASK 21: Range and Endurance \u2014 compounded",
  "Signature Schleicher ASK 21: Wing and Aerodynamics \u2014 compounded",
  "Signature Schleicher ASK 21: Landing Gear \u2014 compounded",
  "Signature Schleicher ASK 21: Cockpit and Avionics \u2014 compounded",
  "Signature Schleicher ASK 21: Cabin and Payload \u2014 compounded",
  "Signature Schleicher ASK 21: Flight Controls \u2014 compounded",
  "Signature Schleicher ASK 21: Electrical and Hydraulic Systems \u2014 compounded",
  "Signature Schleicher ASK 21: Noise and Emissions \u2014 compounded",
  "Signature Schleicher ASK 21: Maintenance \u2014 compounded",
 ],
 "advanced": [
  "Signature Schleicher ASK 21: Three-View Schematic \u2014 advanced",
  "Signature Schleicher ASK 21: Fuselage Cross-Section \u2014 advanced",
  "Signature Schleicher ASK 21: Wing Planform Drawing \u2014 advanced",
  "Signature Schleicher ASK 21: Engine Installation Drawing \u2014 advanced",
  "Signature Schleicher ASK 21: Landing-Gear Geometry \u2014 advanced",
  "Signature Schleicher ASK 21: Empennage Drawing \u2014 advanced",
  "Signature Schleicher ASK 21: Fuel System Schematic \u2014 advanced",
  "Signature Schleicher ASK 21: Avionics Architecture \u2014 advanced",
  "Signature Schleicher ASK 21: Cockpit Layout \u2014 advanced",
  "Signature Schleicher ASK 21: Assembly Breakdown \u2014 advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature Schleicher ASK 21 — structural study\n"
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
    name:topic+' — study record',
    title:topic,
    description:'SIGNATURE SAMPLE (generated — structural sample). A study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-glider-ask-21-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('glider-ask-21-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
