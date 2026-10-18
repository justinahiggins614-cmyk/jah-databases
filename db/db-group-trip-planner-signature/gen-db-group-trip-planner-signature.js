(function(){'use strict';
/* JAH The Group Trip Planner Database Signature Database generator — jahdb-db-group-trip-planner-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GROTRIPLAS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Trip: Park picnic day",
  "Trip: Beach afternoon",
  "Trip: Zoo visit",
  "Trip: Movie night out",
  "Trip: Hiking morning",
  "Trip: Museum day",
  "Trip: Bowling night",
  "Trip: Farmers market",
  "Trip: Mini golf",
  "Trip: Lake swim",
  "Trip: City walking tour"
 ],
 "Compounded": [
  "Trip: Cabin weekend",
  "Trip: City break",
  "Trip: Camping trip",
  "Trip: Road trip",
  "Trip: Ski weekend",
  "Trip: Festival weekend",
  "Trip: Wine country",
  "Trip: Theme park day",
  "Trip: Kayak day",
  "Trip: Historic town",
  "Trip: Sports game",
  "Trip: Beach weekend"
 ],
 "Advanced": [
  "Trip: International week",
  "Trip: Safari adventure",
  "Trip: Sailing week",
  "Trip: National parks tour",
  "Trip: Food tour abroad",
  "Trip: Northern lights",
  "Trip: Island hopping",
  "Trip: Mountain trek",
  "Trip: River cruise",
  "Trip: Desert expedition",
  "Trip: Reunion cruise"
 ]
};
var DEMOKIND="journey-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Group Trip Study — "+safe+"\n"
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
    name:topic+' — trip plan record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A trip plan record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-group-trip-planner-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-group-trip-planner-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
