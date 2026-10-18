(function(){'use strict';
/* JAH The Space Habitat Civilization Signature Database generator — jahdb-db-space-habitat-civilization-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSHCS-";
var FIELDS=["Orbit","The Moon","Mars"];
var TOPICS={
 "Orbit": [
  "The Waystation (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Waystation \u2014 Orbit",
  "The Torus Town (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Torus Town \u2014 Orbit",
  "The Asteroid Mine (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Asteroid Mine \u2014 Orbit",
  "The Lagrange Colonies (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Lagrange Colonies \u2014 Orbit",
  "The Venus Cloud Cities (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Venus Cloud Cities \u2014 Orbit",
  "The Generation Ship (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Generation Ship \u2014 Orbit",
  "The Ceres Hub (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Ceres Hub \u2014 Orbit",
  "The Pluto Deep Station (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Pluto Deep Station \u2014 Orbit",
  "The L5 Shipyard Town (Signature Edition) \u2014 Orbit",
  "The Signature Method for The L5 Shipyard Town \u2014 Orbit",
  "The Habitat Planner's Method (Signature Edition) \u2014 Orbit",
  "The Signature Method for The Habitat Planner's Method \u2014 Orbit"
 ],
 "The Moon": [
  "The Lunar Town (Signature Edition) \u2014 The Moon",
  "The Signature Method for The Lunar Town \u2014 The Moon",
  "The Farside Observatory (Signature Edition) \u2014 The Moon",
  "The Signature Method for The Farside Observatory \u2014 The Moon",
  "The Europa Station (Signature Edition) \u2014 The Moon",
  "The Signature Method for The Europa Station \u2014 The Moon",
  "The Titan Outpost (Signature Edition) \u2014 The Moon",
  "The Signature Method for The Titan Outpost \u2014 The Moon",
  "The Mercury Polar Base (Signature Edition) \u2014 The Moon",
  "The Signature Method for The Mercury Polar Base \u2014 The Moon"
 ],
 "Mars": [
  "The Mars Town (Signature Edition) \u2014 Mars",
  "The Signature Method for The Mars Town \u2014 Mars",
  "The Phobos Port (Signature Edition) \u2014 Mars",
  "The Signature Method for The Phobos Port \u2014 Mars"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Space Habitat Study — "+safe+"\n"
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
    name:topic+' — space habitat record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A space habitat record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-space-habitat-civilization-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-space-habitat-civilization-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
