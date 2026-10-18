(function(){'use strict';
/* JAH The Efficiency Showdown Signature Database generator — jahdb-db-efficiency-showdown-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EFSS-";
var FIELDS=["Energy Efficiency","Transport Efficiency","Everyday Efficiency"];
var TOPICS={
 "Energy Efficiency": [
  "LED vs Incandescent: Lighting (Signature Edition) - Energy Efficiency",
  "EV vs Gas Car: Driving (Signature Edition) - Energy Efficiency",
  "Heat Pump vs Furnace: Heating (Signature Edition) - Energy Efficiency",
  "Induction vs Gas: Cooking (Signature Edition) - Energy Efficiency",
  "Dishwasher vs Hand Wash: Dishes (Signature Edition) - Energy Efficiency",
  "Front-Load vs Top-Load: Laundry (Signature Edition) - Energy Efficiency"
 ],
 "Transport Efficiency": [
  "Train vs Plane: Travel (Signature Edition) - Transport Efficiency",
  "Bus vs Car: Commute (Signature Edition) - Transport Efficiency",
  "Bike vs E-Bike: Cycling (Signature Edition) - Transport Efficiency",
  "Ship vs Truck: Freight (Signature Edition) - Transport Efficiency",
  "Walking vs Running: Human (Signature Edition) - Transport Efficiency",
  "Sail vs Motor: Boats (Signature Edition) - Transport Efficiency"
 ],
 "Everyday Efficiency": [
  "Insulation vs Heating: Homes (Signature Edition) - Everyday Efficiency",
  "Cold Water vs Hot: Laundry (Signature Edition) - Everyday Efficiency",
  "Air-Dry vs Dryer: Clothes (Signature Edition) - Everyday Efficiency",
  "Reusable vs Disposable: Cups (Signature Edition) - Everyday Efficiency",
  "Shower: Short vs Long (Signature Edition) - Everyday Efficiency",
  "Thermostat: 68 vs 72 (Signature Edition) - Everyday Efficiency",
  "LED TV vs Plasma: Screens (Signature Edition) - Everyday Efficiency",
  "Laptop vs Desktop: Computing (Signature Edition) - Everyday Efficiency",
  "Pressure Cooker vs Pot: Cooking (Signature Edition) - Everyday Efficiency",
  "Microwave vs Oven: Reheating (Signature Edition) - Everyday Efficiency",
  "Compost vs Trash: Food Waste (Signature Edition) - Everyday Efficiency",
  "Repair vs Replace: Stuff (Signature Edition) - Everyday Efficiency",
  "Library vs Buying: Books (Signature Edition) - Everyday Efficiency",
  "Public Transit vs Car: City (Signature Edition) - Everyday Efficiency",
  "Tap vs Bottled: Water (Signature Edition) - Everyday Efficiency",
  "Garden vs Store: Vegetables (Signature Edition) - Everyday Efficiency",
  "Bike Commute vs Drive: Work Trip (Signature Edition) - Everyday Efficiency",
  "Heat Pump Dryer vs Vented Dryer: Laundry (Signature Edition) - Everyday Efficiency",
  "Solar Water vs Gas Water: Heating Water (Signature Edition) - Everyday Efficiency",
  "Smart Thermostat vs Manual: Control (Signature Edition) - Everyday Efficiency",
  "CFL vs LED: Bulb Generations (Signature Edition) - Everyday Efficiency",
  "Double-Pane vs Single-Pane: Windows (Signature Edition) - Everyday Efficiency"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Efficiency Showdown Study — "+safe+"\n"
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
    name:topic+' — efficiency comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A efficiency comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"efficiency-showdown-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-efficiency-showdown-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-efficiency-showdown-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
