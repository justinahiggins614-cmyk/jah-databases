(function(){'use strict';
/* JAH The Fire Science and Fire Protection Database generator — jahdb-fire-science-fire-protection-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FSP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Fire Science Is \u2014 Foundations",
  "The Fire Tetrahedron \u2014 Foundations",
  "Heat Release Rate: The Key Number \u2014 Foundations",
  "Fire Growth: The t-Squared Model \u2014 Foundations",
  "Smoke: The Real Killer \u2014 Foundations",
  "Combustion Products: CO and Friends \u2014 Foundations",
  "Ignition: How Fires Start \u2014 Foundations",
  "Fire Spread: Conduction, Convection, Radiation \u2014 Foundations",
  "Flashover: The Room Ignites \u2014 Foundations",
  "Fire Severity: Time-Temperature Curves \u2014 Foundations",
  "Human Behavior in Fire \u2014 Foundations",
  "Fire Statistics: What Burns \u2014 Foundations"
 ],
 "Compounded": [
  "Fire Detection: Smoke Detectors \u2014 Compounded",
  "Fire Detection: Heat Detectors \u2014 Compounded",
  "Fire Alarm Systems \u2014 Compounded",
  "Automatic Sprinklers: How They Work \u2014 Compounded",
  "Sprinkler Hydraulics: K-Factors \u2014 Compounded",
  "Sprinkler System Types \u2014 Compounded",
  "Standpipes and Hose Systems \u2014 Compounded",
  "Fire Extinguishers: Classes and Ratings \u2014 Compounded",
  "Compartmentation: Containing Fire \u2014 Compounded",
  "Fire-Rated Assemblies \u2014 Compounded",
  "Egress: Getting Out \u2014 Compounded",
  "Smoke Management \u2014 Compounded"
 ],
 "Advanced": [
  "Zone Models and FDS \u2014 Advanced",
  "Flashover Prediction (MQH) \u2014 Advanced",
  "Detector Spacing and Siting \u2014 Advanced",
  "Hydraulic Calculation of Sprinkler Systems \u2014 Advanced",
  "Special Suppression: Gas, Foam, Water Mist \u2014 Advanced",
  "High-Challenge Fires: Warehouses \u2014 Advanced",
  "Performance-Based Fire Design \u2014 Advanced",
  "Fire Investigation Basics \u2014 Advanced",
  "3D-Printable Fire Training Models \u2014 Advanced",
  "The Fire Protection Engineer's Role \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fire Protection — "+safe+"\n"
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
    name:topic+' — fire protection record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fire protection record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fire-protection-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fire-science-fire-protection-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fire-science-fire-protection',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
