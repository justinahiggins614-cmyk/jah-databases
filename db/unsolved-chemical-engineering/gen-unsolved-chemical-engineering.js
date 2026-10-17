(function(){'use strict';
/* JAH The Unsolved Chemical Engineering Database generator — jahdb-unsolved-chemical-engineering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USKE-";
var FIELDS=["Approachable","Deep","Frontier"];
var TOPICS={
 "Approachable": [
  "Why Is Making Fertilizer So Energy-Hungry? - Approachable",
  "Why Can't We Just Pull CO2 Out of the Air? - Approachable",
  "Why Is Iron Still Made With Coal? - Approachable",
  "Why Do We Throw Away Most Plastic Instead of Recycling It? - Approachable",
  "Why Are Medicines So Expensive to Manufacture? - Approachable",
  "Why Is Desalination So Energy-Hungry? - Approachable",
  "Why Do Catalysts Die? - Approachable",
  "Why Doesn't a Lab Recipe Work at Factory Scale? - Approachable",
  "Why Is Waste Heat So Hard to Reuse? - Approachable",
  "Why Is Hydrogen So Hard to Store and Move? - Approachable",
  "Why Can't Filters Catch Everything? - Approachable",
  "Why Do Batteries Degrade Every Cycle? - Approachable"
 ],
 "Deep": [
  "The 400-ppm Wall: The Thermodynamic Minimum of Direct Air Capture - Deep",
  "Amine Scrubbing: Capture Chemistry That Eats Itself - Deep",
  "Turning CO2 Into Fuel With Electricity - Deep",
  "Making Ammonia From Air, Water, and Electricity - Deep",
  "Unzipping Plastics Back to Monomers - Deep",
  "The Mixed-Plastic Sorting Problem - Deep",
  "Continuous Pharma: Proving Quality in Real Time - Deep",
  "Brine: The Concentrate Nobody Wants - Deep",
  "Forward Osmosis and the Search for Low-Energy Desalination - Deep",
  "Process Intensification: Doing More With Smaller Plants - Deep",
  "Replacing Distillation: Separations Without Boiling - Deep",
  "High-Temperature Electrolysis: Letting Heat Pay Part of the Bill - Deep"
 ],
 "Frontier": [
  "Artificial Photosynthesis at Industrial Scale - Frontier",
  "Direct Ocean Capture of CO2 - Frontier",
  "Lignin: The Forgotten Half of Biomass - Frontier",
  "Plasma Chemistry for Nitrogen Fixation and Methane Conversion - Frontier",
  "Very-High-Temperature Process Heat Without Fire - Frontier",
  "Numbered-Up Manufacturing: A Thousand Small Reactors - Frontier",
  "Inverse Catalyst Design: Designing the Active Site First - Frontier",
  "The Digital Twin Plant: Controlling the Uncontrollable - Frontier",
  "Biomanufacturing at Chemical-Plant Scale - Frontier",
  "The Grand Compound Challenge: A Fully Electrified, Carbon-Neutral Chemical Industry - Frontier"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Chemical Engineering Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-chemical-engineering-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-chemical-engineering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-chemical-engineering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
