(function(){'use strict';
/* JAH The Specialty Labs Database generator — jahdb-specialty-labs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SLAB-";
var FIELDS=["specialty"];
var TOPICS={
 "specialty": [
  "Fabrication Laboratories \u2014 specialty",
  "Maker Spaces \u2014 specialty",
  "Hacker Spaces \u2014 specialty",
  "Wet Laboratories \u2014 specialty",
  "Dry Laboratories \u2014 specialty",
  "Computer Laboratories \u2014 specialty",
  "Artificial Intelligence Laboratories \u2014 specialty",
  "Machine Learning Laboratories \u2014 specialty",
  "Robotics Laboratories \u2014 specialty",
  "Media Laboratories \u2014 specialty",
  "Bio Laboratories \u2014 specialty",
  "Chemistry Laboratories \u2014 specialty",
  "Physics Laboratories \u2014 specialty",
  "Optics Laboratories \u2014 specialty",
  "Electronics Benches \u2014 specialty",
  "Microfabrication Facilities \u2014 specialty",
  "Environmental Chambers \u2014 specialty",
  "Thermal Chambers \u2014 specialty",
  "Vibration Tables \u2014 specialty",
  "Anechoic Chambers \u2014 specialty",
  "Reverberation Chambers \u2014 specialty",
  "EMC Laboratories \u2014 specialty",
  "Acoustic Laboratories \u2014 specialty",
  "Metrology Laboratories \u2014 specialty",
  "Calibration Laboratories \u2014 specialty",
  "Cryptography Laboratories \u2014 specialty",
  "Hardware Security Laboratories \u2014 specialty",
  "Failure Analysis Laboratories \u2014 specialty",
  "Reliability Laboratories \u2014 specialty",
  "Materials Testing Laboratories \u2014 specialty",
  "Wind Tunnels \u2014 specialty",
  "Hydrodynamics Laboratories \u2014 specialty",
  "Geotechnical Laboratories \u2014 specialty",
  "Seismic Laboratories \u2014 specialty",
  "Virtual Laboratories \u2014 specialty",
  "Remote Laboratories \u2014 specialty",
  "Field Test Sites \u2014 specialty",
  "Proving Grounds \u2014 specialty",
  "Test Tracks \u2014 specialty",
  "Flight Test Ranges \u2014 specialty",
  "Marine Test Ranges \u2014 specialty",
  "Desert Test Sites \u2014 specialty",
  "Arctic Test Sites \u2014 specialty",
  "High-Altitude Laboratories \u2014 specialty",
  "Underground Laboratories \u2014 specialty",
  "Space Simulation Chambers \u2014 specialty",
  "Clean Assembly Areas \u2014 specialty",
  "Biosafety Laboratories \u2014 specialty",
  "Pharmaceutical Laboratories \u2014 specialty",
  "Food Testing Laboratories \u2014 specialty",
  "Forensic Laboratories \u2014 specialty",
  "Dental Laboratories \u2014 specialty",
  "Jewelry Laboratories \u2014 specialty",
  "Art Conservation Laboratories \u2014 specialty",
  "Archaeology Laboratories \u2014 specialty"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Specialty Labs — "+safe+"\n"
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
    name:topic+' — specialty lab record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A specialty lab record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
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
var gen={version:'jahdb-specialty-labs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('specialty-labs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
