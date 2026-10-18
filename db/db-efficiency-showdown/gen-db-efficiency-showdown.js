(function(){'use strict';
/* JAH The Efficiency Showdown Database generator — jahdb-db-efficiency-showdown-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EFS-";
var FIELDS=["Energy Efficiency","Transport Efficiency","Everyday Efficiency"];
var TOPICS={
 "Energy Efficiency": [
  "LED vs Incandescent: Lighting - Energy Efficiency",
  "EV vs Gas Car: Driving - Energy Efficiency",
  "Heat Pump vs Furnace: Heating - Energy Efficiency",
  "Induction vs Gas: Cooking - Energy Efficiency",
  "Dishwasher vs Hand Wash: Dishes - Energy Efficiency",
  "Front-Load vs Top-Load: Laundry - Energy Efficiency"
 ],
 "Transport Efficiency": [
  "Train vs Plane: Travel - Transport Efficiency",
  "Bus vs Car: Commute - Transport Efficiency",
  "Bike vs E-Bike: Cycling - Transport Efficiency",
  "Ship vs Truck: Freight - Transport Efficiency",
  "Walking vs Running: Human - Transport Efficiency",
  "Sail vs Motor: Boats - Transport Efficiency"
 ],
 "Everyday Efficiency": [
  "Insulation vs Heating: Homes - Everyday Efficiency",
  "Cold Water vs Hot: Laundry - Everyday Efficiency",
  "Air-Dry vs Dryer: Clothes - Everyday Efficiency",
  "Reusable vs Disposable: Cups - Everyday Efficiency",
  "Shower: Short vs Long - Everyday Efficiency",
  "Thermostat: 68 vs 72 - Everyday Efficiency",
  "LED TV vs Plasma: Screens - Everyday Efficiency",
  "Laptop vs Desktop: Computing - Everyday Efficiency",
  "Pressure Cooker vs Pot: Cooking - Everyday Efficiency",
  "Microwave vs Oven: Reheating - Everyday Efficiency",
  "Compost vs Trash: Food Waste - Everyday Efficiency",
  "Repair vs Replace: Stuff - Everyday Efficiency",
  "Library vs Buying: Books - Everyday Efficiency",
  "Public Transit vs Car: City - Everyday Efficiency",
  "Tap vs Bottled: Water - Everyday Efficiency",
  "Garden vs Store: Vegetables - Everyday Efficiency",
  "Bike Commute vs Drive: Work Trip - Everyday Efficiency",
  "Heat Pump Dryer vs Vented Dryer: Laundry - Everyday Efficiency",
  "Solar Water vs Gas Water: Heating Water - Everyday Efficiency",
  "Smart Thermostat vs Manual: Control - Everyday Efficiency",
  "CFL vs LED: Bulb Generations - Everyday Efficiency",
  "Double-Pane vs Single-Pane: Windows - Everyday Efficiency"
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
var gen={version:'jahdb-db-efficiency-showdown-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-efficiency-showdown',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
