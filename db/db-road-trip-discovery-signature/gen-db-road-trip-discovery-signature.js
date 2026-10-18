(function(){'use strict';
/* JAH The Road Trip Discovery Database Signature Database generator — jahdb-db-road-trip-discovery-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TDRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Road Trip?",
  "Route 66, USA",
  "Planning the Route",
  "The Great Ocean Road, Australia",
  "The Road Trip Car",
  "The Pacific Coast Highway",
  "The Road Trip Food",
  "The Garden Route, South Africa",
  "The Road Trip Safety",
  "The Ring Road, Iceland",
  "The Road Trip Year"
 ],
 "Compounded": [
  "The Amalfi Coast Road",
  "The Road Trip Story",
  "The Blue Ridge Parkway",
  "The Road Trip with Kids",
  "The North Coast 500, Scotland",
  "The Road Trip Solo",
  "The Romantic Road, Germany",
  "The Road Trip Decade",
  "The Wild Atlantic Way",
  "The Road Trip Cruise",
  "The Sani Pass",
  "The Road Trip Festival"
 ],
 "Advanced": [
  "Advanced: The Road Index",
  "Advanced: Your Road Ranking",
  "Advanced: The Road Passport",
  "Advanced: The Road Storyteller",
  "Advanced: The Road Bucket List",
  "Advanced: The Road Finale",
  "Advanced: The Road Legacy",
  "Advanced: The Road Memoir",
  "Advanced: The Road Master Decade",
  "Advanced: The Road Year",
  "The Road Trip Discovery Encyclopedia"
 ]
};
var DEMOKIND="travel-lab-demo";
var SAMPLEDESC="Sample records are complete real road entries with real measurement math.";
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
    name:topic+' — road trip record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A road trip record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-road-trip-discovery-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-road-trip-discovery-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
