(function(){'use strict';
/* JAH The Inventory and Warehouse State Database generator — jahdb-inventory-warehouse-state-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INV-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Inventory Is and What a Warehouse Holds - Foundations",
  "The SKU: The Inventory Atom - Foundations",
  "Stock States: On Hand, Reserved, and Available to Promise - Foundations",
  "The Location Address: Aisles, Bays, and Bins - Foundations",
  "Units of Measure and the Pack Hierarchy - Foundations",
  "Inventory Valuation Basics: FIFO and LIFO - Foundations",
  "Lead Time: The Clock That Drives Everything - Foundations",
  "Goods Receipt: Receiving and Putaway Records - Foundations",
  "The Pick-Pack-Ship Flow - Foundations",
  "Lots, Batches, and Expiry: The Basics - Foundations"
 ],
 "Compounded": [
  "Cycle Counting: Counting Without Stopping - Compounded",
  "ABC Analysis: Ranking Stock by Value and Motion - Compounded",
  "Reorder Point Math - Compounded",
  "The Economic Order Quantity - Compounded",
  "Safety Stock Math - Compounded",
  "FEFO: Issuing by Expiry - Compounded",
  "Reservations and Allocation Logic - Compounded",
  "Putaway Strategies - Compounded",
  "Picking Strategies: Wave, Zone, Batch, Discrete - Compounded",
  "Packing Records and Shipment Integrity - Compounded",
  "Movement Records: Transfers, Adjustments, and Audits - Compounded",
  "Warehouse Layout and Slotting Basics - Compounded"
 ],
 "Advanced": [
  "Multi-Echelon Inventory - Advanced",
  "MRP: Materials Requirements Planning - Advanced",
  "Inventory Accuracy: Causes and Cures - Advanced",
  "Perpetual and Periodic Inventory Systems - Advanced",
  "Advanced Slotting: Cube, Velocity, and the Golden Zone - Advanced",
  "Dynamic Safety Stock and Service Levels - Advanced",
  "Replenishment Systems: Kanban, Min-Max, and DRP - Advanced",
  "Returns, RMAs, and Reverse Logistics - Advanced",
  "Serialized Inventory and Traceability - Advanced",
  "The Full Physical Inventory - Advanced",
  "Inventory Analytics: Turns, Days of Supply, and Stockouts - Advanced",
  "The Inventory Health Program - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Inventory Warehouse Study — "+safe+"\n"
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
    name:topic+' — inventory and warehouse record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A inventory and warehouse record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"inventory-warehouse-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-inventory-warehouse-state-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('inventory-warehouse-state',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
