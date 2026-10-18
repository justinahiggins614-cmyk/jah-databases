(function(){'use strict';
/* JAH The Future Farm Database generator — jahdb-db-future-farm-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CFFD-";
var FIELDS=["Up Farms","Water Farms","Edge Farms"];
var TOPICS={
 "Up Farms": [
  "The Vertical Tower \u2014 Up Farms",
  "The Vertical Tower \u2014 Deep Dive \u2014 Up Farms",
  "The Orbital Greenhouse \u2014 Up Farms",
  "The Orbital Greenhouse \u2014 Deep Dive \u2014 Up Farms",
  "The Rooftop Commons \u2014 Up Farms",
  "The Rooftop Commons \u2014 Deep Dive \u2014 Up Farms",
  "The Aeroponic Spire \u2014 Up Farms",
  "The Aeroponic Spire \u2014 Deep Dive \u2014 Up Farms",
  "The Insect Ranch \u2014 Up Farms",
  "The Insect Ranch \u2014 Deep Dive \u2014 Up Farms"
 ],
 "Water Farms": [
  "The Ocean Plot \u2014 Water Farms",
  "The Ocean Plot \u2014 Deep Dive \u2014 Water Farms",
  "The Floating Rice \u2014 Water Farms",
  "The Floating Rice \u2014 Deep Dive \u2014 Water Farms",
  "The Desert Bloom Farm \u2014 Water Farms",
  "The Desert Bloom Farm \u2014 Deep Dive \u2014 Water Farms",
  "The Permaculture Commons \u2014 Water Farms",
  "The Permaculture Commons \u2014 Deep Dive \u2014 Water Farms",
  "The Algae Bioreactor \u2014 Water Farms",
  "The Algae Bioreactor \u2014 Deep Dive \u2014 Water Farms",
  "The Saltwater Greenhouse \u2014 Water Farms",
  "The Saltwater Greenhouse \u2014 Deep Dive \u2014 Water Farms"
 ],
 "Edge Farms": [
  "The Arctic Greenhouse \u2014 Edge Farms",
  "The Arctic Greenhouse \u2014 Deep Dive \u2014 Edge Farms",
  "The Lunar Farm \u2014 Edge Farms",
  "The Lunar Farm \u2014 Deep Dive \u2014 Edge Farms",
  "The Mars Farm \u2014 Edge Farms",
  "The Mars Farm \u2014 Deep Dive \u2014 Edge Farms",
  "The Underground Farm \u2014 Edge Farms",
  "The Underground Farm \u2014 Deep Dive \u2014 Edge Farms",
  "The Seed Vault Farm \u2014 Edge Farms",
  "The Seed Vault Farm \u2014 Deep Dive \u2014 Edge Farms",
  "The Farm Futurist's Method \u2014 Edge Farms",
  "The Farm Futurist's Method \u2014 Deep Dive \u2014 Edge Farms"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Farm Study — "+safe+"\n"
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
    name:topic+' — future farm record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A future farm record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-future-farm-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-future-farm',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
