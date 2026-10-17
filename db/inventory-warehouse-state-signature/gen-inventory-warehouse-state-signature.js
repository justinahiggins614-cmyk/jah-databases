(function(){'use strict';
/* JAH The Inventory and Warehouse State Signature Database generator — jahdb-inventory-warehouse-state-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INVS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Inventory Is and What a Warehouse Holds (Signature Edition) - Foundations",
  "The SKU: The Inventory Atom (Signature Edition) - Foundations",
  "Stock States: On Hand, Reserved, and Available to Promise (Signature Edition) - Foundations",
  "The Location Address: Aisles, Bays, and Bins (Signature Edition) - Foundations",
  "Units of Measure and the Pack Hierarchy (Signature Edition) - Foundations",
  "Inventory Valuation Basics: FIFO and LIFO (Signature Edition) - Foundations",
  "Lead Time: The Clock That Drives Everything (Signature Edition) - Foundations",
  "Goods Receipt: Receiving and Putaway Records (Signature Edition) - Foundations",
  "The Pick-Pack-Ship Flow (Signature Edition) - Foundations",
  "Lots, Batches, and Expiry: The Basics (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Cycle Counting: Counting Without Stopping (Signature Edition) - Compounded",
  "ABC Analysis: Ranking Stock by Value and Motion (Signature Edition) - Compounded",
  "Reorder Point Math (Signature Edition) - Compounded",
  "The Economic Order Quantity (Signature Edition) - Compounded",
  "Safety Stock Math (Signature Edition) - Compounded",
  "FEFO: Issuing by Expiry (Signature Edition) - Compounded",
  "Reservations and Allocation Logic (Signature Edition) - Compounded",
  "Putaway Strategies (Signature Edition) - Compounded",
  "Picking Strategies: Wave, Zone, Batch, Discrete (Signature Edition) - Compounded",
  "Packing Records and Shipment Integrity (Signature Edition) - Compounded",
  "Movement Records: Transfers, Adjustments, and Audits (Signature Edition) - Compounded",
  "Warehouse Layout and Slotting Basics (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Multi-Echelon Inventory (Signature Edition) - Advanced",
  "MRP: Materials Requirements Planning (Signature Edition) - Advanced",
  "Inventory Accuracy: Causes and Cures (Signature Edition) - Advanced",
  "Perpetual and Periodic Inventory Systems (Signature Edition) - Advanced",
  "Advanced Slotting: Cube, Velocity, and the Golden Zone (Signature Edition) - Advanced",
  "Dynamic Safety Stock and Service Levels (Signature Edition) - Advanced",
  "Replenishment Systems: Kanban, Min-Max, and DRP (Signature Edition) - Advanced",
  "Returns, RMAs, and Reverse Logistics (Signature Edition) - Advanced",
  "Serialized Inventory and Traceability (Signature Edition) - Advanced",
  "The Full Physical Inventory (Signature Edition) - Advanced",
  "Inventory Analytics: Turns, Days of Supply, and Stockouts (Signature Edition) - Advanced",
  "The Inventory Health Program (Signature Edition) - Advanced"
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
var gen={version:'jahdb-inventory-warehouse-state-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('inventory-warehouse-state-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
