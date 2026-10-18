(function(){'use strict';
/* JAH The Retail Commerce Operations Database generator — jahdb-retail-commerce-operations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RTCO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Retail Commerce Is — Industry Overview - Foundations",
  "Product Catalogs and SKU Systems - Foundations",
  "Barcodes, GTINs, and Product Identification - Foundations",
  "Retail Pricing Strategy Fundamentals - Foundations",
  "The Point of Sale (POS) System - Foundations",
  "Cash Handling and Payment Processing - Foundations",
  "Store Layout and Customer Flow - Foundations",
  "Inventory Basics — Stock Counts - Foundations",
  "Receiving and Stocking Goods - Foundations",
  "Customer Service Fundamentals - Foundations",
  "Merchandising Basics - Foundations",
  "Retail Math I — Markup and Margin - Foundations",
 ],
 "Compounded": [
  "Demand Forecasting - Compounded",
  "Purchase Orders and Replenishment - Compounded",
  "Economic Order Quantity (EOQ) - Compounded",
  "Markdowns, Promotions, and Clearance - Compounded",
  "Planograms and Shelf Space - Compounded",
  "E-commerce Operations - Compounded",
  "Omnichannel Fulfillment - Compounded",
  "Warehousing and Distribution Centers - Compounded",
  "Returns and Reverse Logistics - Compounded",
  "Loyalty Programs - Compounded",
  "Loss Prevention and Shrink - Compounded",
 ],
 "Advanced": [
  "Retail Analytics — Sell-Through and GMROI - Advanced",
  "Market Basket Analysis - Advanced",
  "Category Management - Advanced",
  "Private Label Development - Advanced",
  "Supply Chain Management - Advanced",
  "Labor Scheduling and Workforce Management - Advanced",
  "Site Selection and Store Real Estate - Advanced",
  "RFID and Store Automation - Advanced",
  "Seasonal Planning and Open-to-Buy - Advanced",
  "Franchise Operations - Advanced",
  "Retail Mastery Review — Running the Whole Operation - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + '# '+safe+' -- structural sample demo. Property of Justin Addam Higgins (JAH).\n'
   + "# EOQ structural sample calculator (retail operations)\n"
   + "import math\n"
   + "D, S, H = 1200.0, 50.0, 2.5\n"
   + "eoq = math.sqrt(2*D*S/H)\n"
   + "orders = D/eoq\n"
   + "print('sample annual demand:', D)\n"
   + "print('sample EOQ:', round(eoq,2))\n"
   + "print('sample orders per year:', round(orders,2))\n"
   + "assert eoq > 0 and orders > 0\n"
   + "print('OK: structural sample demo ran')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — retail operations record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A retail operations record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"retail-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-retail-commerce-operations-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('retail-commerce-operations',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
