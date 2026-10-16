(function(){'use strict';
/* JAH The Everything Agriculture and Food Database generator — jahdb-everything-agriculture-food-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVAF-";
var FIELDS=["Agronomy","Livestock","Crop Protection","Food Science","Farm Business","Signature Agriculture"];
var TOPICS={
 "Agronomy": [
  "Soil Science for Farming \u2014 Agronomy",
  "Crop Production: Planting to Harvest \u2014 Agronomy",
  "Irrigation and Water Management \u2014 Agronomy"
 ],
 "Livestock": [
  "Animal Husbandry: Care and Breeding \u2014 Livestock"
 ],
 "Crop Protection": [
  "Pest and Disease Management \u2014 Crop Protection"
 ],
 "Food Science": [
  "Food Safety: From Farm to Table \u2014 Food Science",
  "Food Preservation: Canning to Freezing \u2014 Food Science"
 ],
 "Farm Business": [
  "Agricultural Economics: The Farm Business \u2014 Farm Business"
 ],
 "Signature Agriculture": [
  "Signature Yield Geometry (Signature Edition) \u2014 Signature Agriculture",
  "Signature Crop Planner (Signature Edition) \u2014 Signature Agriculture",
  "Signature Irrigation Optimizer (Signature Edition) \u2014 Signature Agriculture",
  "Signature Food System Mapper (Signature Edition) \u2014 Signature Agriculture"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Agriculture Food — "+safe+"\n"
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
    name:topic+' — agriculture and food record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A agriculture and food record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-agriculture-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-agriculture-food',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
