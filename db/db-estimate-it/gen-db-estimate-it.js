(function(){'use strict';
/* JAH The Estimate It Database Database generator — jahdb-db-estimate-it-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ESTIT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Estimate: how many piano tuners in Chicago",
  "Estimate: how many breaths you take per day",
  "Estimate: how many words you speak per day",
  "Estimate: how many hairs on your head",
  "Estimate: how many seconds in a year",
  "Estimate: how many heartbeats per day",
  "Estimate: how many pages in all your school books",
  "Estimate: how many steps to walk across town",
  "Estimate: how many cups of water you drink per year",
  "Estimate: how many hours you sleep per year",
  "Estimate: how many miles you walk per year"
 ],
 "Compounded": [
  "Estimate: how many ping-pong balls fit in a school bus",
  "Estimate: how many gas stations in the US",
  "Estimate: how many tweets per day (worldwide)",
  "Estimate: how many grains of sand on a beach",
  "Estimate: how many cells in the human body",
  "Estimate: how many photos taken per day worldwide",
  "Estimate: how many hairs shed per day",
  "Estimate: how many words in all published books",
  "Estimate: how many ants on Earth",
  "Estimate: how many cups of coffee per day worldwide",
  "Estimate: how many miles of DNA in your body",
  "Estimate: how many sheets of paper used per day in a school"
 ],
 "Advanced": [
  "Estimate: how many atoms in a grape",
  "Estimate: how many piano tuners - full Fermi with overhead",
  "Estimate: how much data the internet holds",
  "Estimate: how many Earths fit in the Sun",
  "Estimate: how many heartbeats in a lifetime",
  "Estimate: how many stars in the observable universe",
  "Estimate: how many chess games possible (Shannon number)",
  "Estimate: how many books could a library of Congress hold digitally",
  "Estimate: how many years to count to a billion",
  "Estimate: how many molecules in a breath",
  "Estimate: how much the Great Pyramid weighs"
 ]
};
var DEMOKIND="fermi-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Estimate It Study — "+safe+"\n"
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
    name:topic+' — estimation puzzle record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A estimation puzzle record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-estimate-it-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-estimate-it',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
