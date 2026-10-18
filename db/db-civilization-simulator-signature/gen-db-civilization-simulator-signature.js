(function(){'use strict';
/* JAH The Civilization Simulator Signature Database generator — jahdb-db-civilization-simulator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CCSDS-";
var FIELDS=["Population","Resources","Institutions"];
var TOPICS={
 "Population": [
  "The Population Engine (Signature Edition) \u2014 Population",
  "The Signature Method for The Population Engine \u2014 Population",
  "The Malthusian Trap (Signature Edition) \u2014 Population",
  "The Signature Method for The Malthusian Trap \u2014 Population",
  "The Urbanization Pull (Signature Edition) \u2014 Population",
  "The Signature Method for The Urbanization Pull \u2014 Population",
  "The Disease Vector (Signature Edition) \u2014 Population",
  "The Signature Method for The Disease Vector \u2014 Population"
 ],
 "Resources": [
  "The Trade Network (Signature Edition) \u2014 Resources",
  "The Signature Method for The Trade Network \u2014 Resources",
  "The Water Table (Signature Edition) \u2014 Resources",
  "The Signature Method for The Water Table \u2014 Resources",
  "The Forest Yield (Signature Edition) \u2014 Resources",
  "The Signature Method for The Forest Yield \u2014 Resources",
  "The Climate Response (Signature Edition) \u2014 Resources",
  "The Signature Method for The Climate Response \u2014 Resources",
  "The Carrying Capacity (Signature Edition) \u2014 Resources",
  "The Signature Method for The Carrying Capacity \u2014 Resources"
 ],
 "Institutions": [
  "The Collapse Cascade (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Collapse Cascade \u2014 Institutions",
  "The Innovation Diffusion (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Innovation Diffusion \u2014 Institutions",
  "The Inequality Engine (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Inequality Engine \u2014 Institutions",
  "The Governance Cycle (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Governance Cycle \u2014 Institutions",
  "The Literacy Lift (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Literacy Lift \u2014 Institutions",
  "The Network Effect (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Network Effect \u2014 Institutions",
  "The Trust Thermocline (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Trust Thermocline \u2014 Institutions",
  "The Resilience Reserve (Signature Edition) \u2014 Institutions",
  "The Signature Method for The Resilience Reserve \u2014 Institutions"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Civilization Simulation Study — "+safe+"\n"
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
    name:topic+' — civilization simulation record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A civilization simulation record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-civilization-simulator-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-civilization-simulator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
