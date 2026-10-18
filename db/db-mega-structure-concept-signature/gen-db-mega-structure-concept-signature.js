(function(){'use strict';
/* JAH The Mega Structure Concept Signature Database generator — jahdb-db-mega-structure-concept-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMSCS-";
var FIELDS=["Towers & Cities","Space Structures","Ocean & Earth"];
var TOPICS={
 "Towers & Cities": [
  "The Kilometer Tower (Signature Edition) \u2014 Towers & Cities",
  "The Signature Method for The Kilometer Tower \u2014 Towers & Cities",
  "The Inverted Pyramid (Signature Edition) \u2014 Towers & Cities",
  "The Signature Method for The Inverted Pyramid \u2014 Towers & Cities",
  "The Trans-Ocean Bridge (Signature Edition) \u2014 Towers & Cities",
  "The Signature Method for The Trans-Ocean Bridge \u2014 Towers & Cities",
  "The Climate Dome (Signature Edition) \u2014 Towers & Cities",
  "The Signature Method for The Climate Dome \u2014 Towers & Cities",
  "The Arcology Cluster (Signature Edition) \u2014 Towers & Cities",
  "The Signature Method for The Arcology Cluster \u2014 Towers & Cities",
  "The Mega-Structure Method (Signature Edition) \u2014 Towers & Cities",
  "The Signature Method for The Mega-Structure Method \u2014 Towers & Cities"
 ],
 "Space Structures": [
  "The Space Elevator (Signature Edition) \u2014 Space Structures",
  "The Signature Method for The Space Elevator \u2014 Space Structures",
  "The Equatorial Orbital Ring (Signature Edition) \u2014 Space Structures",
  "The Signature Method for The Equatorial Orbital Ring \u2014 Space Structures",
  "The Launch Loop (Signature Edition) \u2014 Space Structures",
  "The Signature Method for The Launch Loop \u2014 Space Structures",
  "The Orbital Shipyard (Signature Edition) \u2014 Space Structures",
  "The Signature Method for The Orbital Shipyard \u2014 Space Structures",
  "The Skyhook (Signature Edition) \u2014 Space Structures",
  "The Signature Method for The Skyhook \u2014 Space Structures"
 ],
 "Ocean & Earth": [
  "The Ocean Platform (Signature Edition) \u2014 Ocean & Earth",
  "The Signature Method for The Ocean Platform \u2014 Ocean & Earth",
  "The Continental Tunnel (Signature Edition) \u2014 Ocean & Earth",
  "The Signature Method for The Continental Tunnel \u2014 Ocean & Earth",
  "The Second Canal (Signature Edition) \u2014 Ocean & Earth",
  "The Signature Method for The Second Canal \u2014 Ocean & Earth",
  "The Geothermal Tap (Signature Edition) \u2014 Ocean & Earth",
  "The Signature Method for The Geothermal Tap \u2014 Ocean & Earth",
  "The Desert Bloom (Signature Edition) \u2014 Ocean & Earth",
  "The Signature Method for The Desert Bloom \u2014 Ocean & Earth",
  "The Iceberg Tow (Signature Edition) \u2014 Ocean & Earth",
  "The Signature Method for The Iceberg Tow \u2014 Ocean & Earth"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mega Structure Study — "+safe+"\n"
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
    name:topic+' — mega-structure concept record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mega-structure concept record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-mega-structure-concept-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mega-structure-concept-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
