(function(){'use strict';
/* JAH The Agriculture Ecology Data Types Database generator - agriculture-ecology-data-types-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AEGR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS=["Foundations: Agriculture Ecology Data Types", "CropRecord - Type Definition", "CropRecord - Schema and Validator", "SoilSample - Type Definition", "SoilSample - Schema and Validator", "LivestockRecord - Type Definition", "LivestockRecord - Schema and Validator", "WeatherObservation - Type Definition", "WeatherObservation - Schema and Validator", "IrrigationEvent - Type Definition", "IrrigationEvent - Schema and Validator", "PestObservation - Type Definition", "PestObservation - Schema and Validator", "BiodiversitySurvey - Type Definition", "BiodiversitySurvey - Schema and Validator", "HarvestLot - Type Definition", "HarvestLot - Schema and Validator", "FertilizerApplication - Type Definition", "FertilizerApplication - Schema and Validator", "FieldBoundary - Type Definition", "FieldBoundary - Schema and Validator"];
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+"\n# Field: "+field+"\nrecord={'title': \""+safe+"\", 'field': \""+field+"\"}\nprint('Record: '+record['title']+' ['+record['field']+']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var topic=pick(TOPICS,rnd);
  return {id:PREFIX+String(seed).padStart(6,'0'),title:topic,field:field,src:'public-harvest',
    summary:'Generated record for '+topic+'.',demo:{language:'python',program:demoProgram(topic,field)},_seed:seed};
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
var gen={version:'agriculture-ecology-data-types-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('agriculture-ecology-data-types',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
