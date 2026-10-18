(function(){'use strict';
/* JAH The Geologic Marvels Database Signature Database generator — jahdb-db-geologic-marvels-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GLMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Geologic Marvel?",
  "The Grand Canyon (Geologic)",
  "Reading Rocks",
  "The Giant's Causeway, N. Ireland",
  "The Geologic Time",
  "The Zhangjiajie Pillars (Geologic)",
  "The Marvel Photography",
  "The Salar de Uyuni (Geologic)",
  "The Marvels with Kids",
  "The Wave, Arizona",
  "The Geologic Year"
 ],
 "Compounded": [
  "The Antelope Canyon (Geologic)",
  "The Marvel Story",
  "The Fly Geyser, Nevada",
  "The Marvel Tour",
  "The Chocolate Hills, Philippines",
  "The Marvel Solo",
  "The Richat Structure, Mauritania",
  "The Marvel Decade",
  "The Bryce Amphitheater",
  "The Geologic Road Trip",
  "The Danakil Depression",
  "The Geologic Festival"
 ],
 "Advanced": [
  "Advanced: The Geologic Index",
  "Advanced: Your Geologic Ranking",
  "Advanced: The Geologic Passport",
  "Advanced: The Geologic Storyteller",
  "Advanced: The Geologic Bucket List",
  "Advanced: The Geologic Finale",
  "Advanced: The Geologic Legacy",
  "Advanced: The Geologic Memoir",
  "Advanced: The Ancient Master Decade",
  "Advanced: The Geologic Year",
  "The Geologic Marvels Encyclopedia"
 ]
};
var DEMOKIND="travel-lab-demo";
var SAMPLEDESC="Sample records are complete real geologic entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Travel Lab Demo — "+safe+"\n"
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
    name:topic+' — geologic marvel record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A geologic marvel record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-geologic-marvels-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-geologic-marvels-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
