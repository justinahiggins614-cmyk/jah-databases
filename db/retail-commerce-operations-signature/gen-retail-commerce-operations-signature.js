(function(){'use strict';
/* JAH The Retail Commerce Operations Signature Database generator — jahdb-retail-commerce-operations-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RTCOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Retail Commerce Is — The Signature View (Signature Edition) - Foundations",
  "The Sworn SKU Registry (Signature Edition) - Foundations",
  "Seals of Identity — Barcodes in the Signature Method (Signature Edition) - Foundations",
  "The Pricing Covenant (Signature Edition) - Foundations",
  "The Point of Sale as Witness (Signature Edition) - Foundations",
  "The Honest Till — Cash in the Signature Method (Signature Edition) - Foundations",
  "The Pilgrim's Path — Store Layout in the Signature Method (Signature Edition) - Foundations",
  "The True Count — Inventory in the Signature Method (Signature Edition) - Foundations",
  "The Receiving Oath (Signature Edition) - Foundations",
  "The Guest Law — Service in the Signature Method (Signature Edition) - Foundations",
  "The Art of the Display — Signature Merchandising (Signature Edition) - Foundations",
  "Signature Retail Math — Markup and Margin (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "Foreseeing Demand — The Signature View (Signature Edition) - Compounded",
  "The Ordering Discipline (Signature Edition) - Compounded",
  "The Balanced Order — Signature EOQ (Signature Edition) - Compounded",
  "The Honorable Reduction — Markdowns in the Signature Method (Signature Edition) - Compounded",
  "The Measured Shelf — Signature Planograms (Signature Edition) - Compounded",
  "The Never-Closing Store — Signature E-commerce (Signature Edition) - Compounded",
  "One Inventory, Many Doors — Signature Omnichannel (Signature Edition) - Compounded",
  "The Great Storehouse — Signature Warehousing (Signature Edition) - Compounded",
  "The Backward Road — Signature Returns (Signature Edition) - Compounded",
  "The Circle of Return — Signature Loyalty (Signature Edition) - Compounded",
  "Guarding the Goods — Signature Loss Prevention (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Two Lenses — Signature Retail Analytics (Signature Edition) - Advanced",
  "Kindred Goods — Signature Basket Wisdom (Signature Edition) - Advanced",
  "The Stewardship of Kinds — Signature Category Management (Signature Edition) - Advanced",
  "The House Brand — Signature Private Label (Signature Edition) - Advanced",
  "The Long Road — Signature Supply Chain (Signature Edition) - Advanced",
  "The Right Hands at the Right Hour — Signature Labor (Signature Edition) - Advanced",
  "Choosing Ground — Signature Site Selection (Signature Edition) - Advanced",
  "The Unseen Counters — Signature RFID and Automation (Signature Edition) - Advanced",
  "The Turning Year — Signature Seasonal Planning (Signature Edition) - Advanced",
  "The Shared Banner — Signature Franchising (Signature Edition) - Advanced",
  "The Keeper's Review — Signature Mastery (Signature Edition) - Advanced",
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('retail-commerce-operations-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
