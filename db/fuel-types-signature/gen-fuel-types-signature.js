(function(){'use strict';
/* JAH The Fuel Types Signature Database generator — jahdb-fuel-types-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FUELS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a fuel is: stored chemical energy (Signature Edition) - fuel-basics",
  "Wood fuel: the original fuel (Signature Edition) - solid-fuels",
  "Charcoal: wood concentrated by fire (Signature Edition) - solid-fuels",
  "Coal: ancient sunlight in rock (Signature Edition) - coal-family",
  "Coal grades: lignite, bituminous, anthracite (Signature Edition) - coal-family",
  "Coke: coal baked for the furnace (Signature Edition) - coal-family",
  "Peat: young coal from the bog (Signature Edition) - coal-family",
  "Kerosene: the lamp fuel that lit the world (Signature Edition) - petroleum-distillates",
  "Heating oil No. 2: the home heat standard (Signature Edition) - petroleum-distillates",
  "Fuel oil grades: No. 1 through No. 6 (Signature Edition) - petroleum-distillates",
  "Natural gas: methane, the pipeline fuel (Signature Edition) - gaseous-fuels",
  "Propane: bottled gas energy (Signature Edition) - gaseous-fuels"
 ],
 "Compounded": [
  "Gasoline and the octane number (Signature Edition) - liquid-transport-fuels",
  "Diesel fuel and the cetane number (Signature Edition) - liquid-transport-fuels",
  "Ethanol and E10/E15: gasoline stretched with grain (Signature Edition) - biofuels",
  "E85: the flex-fuel blend (Signature Edition) - biofuels",
  "Biodiesel B100: diesel from vegetable oil (Signature Edition) - biofuels",
  "Biodiesel blends: B5 and B20 (Signature Edition) - biofuels",
  "Methanol: the simplest alcohol fuel (Signature Edition) - alternative-fuels",
  "Aviation gasoline: 100LL for piston aircraft (Signature Edition) - aviation-fuels",
  "Jet fuel: Jet A and Jet A-1 (Signature Edition) - aviation-fuels",
  "LNG: natural gas made liquid (Signature Edition) - gaseous-fuels",
  "CNG: natural gas under pressure (Signature Edition) - gaseous-fuels",
  "Hydrogen production: steam methane reforming (Signature Edition) - hydrogen",
  "Hydrogen use: storage, handling, and fuel cells (Signature Edition) - hydrogen"
 ],
 "Advanced": [
  "Natural uranium: the nuclear fuel starting point (Signature Edition) - nuclear-fuels",
  "Enriched uranium: pellets and fuel assemblies (Signature Edition) - nuclear-fuels",
  "The nuclear fuel cycle: mine to reactor to storage (Signature Edition) - nuclear-fuels",
  "Naphtha and refinery streams (Signature Edition) - refining-systems",
  "The refinery: crude oil distilled into fuels (Signature Edition) - refining-systems",
  "Fuel blending and additives: the finished-fuel system (Signature Edition) - refining-systems",
  "Bunker fuel: residual oil for ships (Signature Edition) - fuel-systems",
  "Fuel storage, transport, and safety systems (Signature Edition) - fuel-systems",
  "Energy density: comparing every fuel on one scale (Signature Edition) - fuel-systems"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fuel Types Study — "+safe+"\n"
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
    name:topic+' — fuel type record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fuel type record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fuel-types-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-fuel-types-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fuel-types-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
