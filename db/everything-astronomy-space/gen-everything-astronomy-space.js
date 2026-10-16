(function(){'use strict';
/* JAH The Everything Astronomy and Space Database generator — jahdb-everything-astronomy-space-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVAS-";
var FIELDS=["Solar System","Stellar Astronomy","Cosmology","Spaceflight","Observation","Signature Astronomy"];
var TOPICS={
 "Solar System": [
  "The Solar System: Planets and Small Bodies \u2014 Solar System",
  "The Moon: Phases, Tides, and Exploration \u2014 Solar System"
 ],
 "Stellar Astronomy": [
  "Stars: Birth, Life, and Death \u2014 Stellar Astronomy",
  "Exoplanets: Worlds Around Other Stars \u2014 Stellar Astronomy"
 ],
 "Cosmology": [
  "Galaxies and the Expanding Universe \u2014 Cosmology"
 ],
 "Spaceflight": [
  "Orbital Mechanics: Kepler and Newton \u2014 Spaceflight",
  "Spaceflight: Rockets, Orbits, and Delta-V \u2014 Spaceflight"
 ],
 "Observation": [
  "Telescopes: How We Observe the Sky \u2014 Observation"
 ],
 "Signature Astronomy": [
  "Signature Orbital Geometry (Signature Edition) \u2014 Signature Astronomy",
  "Signature Star Catalog Engine (Signature Edition) \u2014 Signature Astronomy",
  "Signature Deep-Space Mapper (Signature Edition) \u2014 Signature Astronomy",
  "Signature Mission Planner (Signature Edition) \u2014 Signature Astronomy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Astronomy Space — "+safe+"\n"
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
    name:topic+' — astronomy and space record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A astronomy and space record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-astronomy-space-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-astronomy-space',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
