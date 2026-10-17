(function(){'use strict';
/* JAH The Transaction Records Database generator — jahdb-transaction-records-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRX-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Transaction Record - Foundations",
  "The Anatomy of a Transaction Record - Foundations",
  "Transaction Lifecycle States: Pending, Settled, Reversed - Foundations",
  "Orders, Purchases, Payments, and Transfers - Foundations",
  "Double-Entry Bookkeeping in One Lesson - Foundations",
  "Reading a Receipt Like a Record - Foundations",
  "Money in Minor Units: Cents, Rounding, and Precision - Foundations",
  "Timestamps, Time Zones, and Value Dates - Foundations",
  "The Parties to a Transaction - Foundations",
  "Transaction Identifiers and Reference Numbers - Foundations"
 ],
 "Compounded": [
  "Order Records: Carts, Line Items, and Order States - Compounded",
  "Authorization and Capture: The Two-Step Card Payment - Compounded",
  "Payment Methods Compared: Cards, ACH, Wires, Wallets - Compounded",
  "Idempotency Keys and Exactly-Once Processing - Compounded",
  "Refunds: Full, Partial, and How They Post - Compounded",
  "Returns and Reverse Logistics Records - Compounded",
  "Chargebacks and the Dispute Lifecycle - Compounded",
  "Bank Transfers: ACH Batches and Wire Records - Compounded",
  "The Card Transaction Flow: Authorization to Clearing - Compounded",
  "Reconciliation: Matching Two Ledgers - Compounded",
  "Clearing and Settlement - Compounded",
  "The Anatomy of a Fee: Interchange, Assessment, Markup - Compounded"
 ],
 "Advanced": [
  "Double-Entry Reconciliation at Scale - Advanced",
  "ISO 20022: The MX Message Grammar - Advanced",
  "SWIFT MT and MX Messages for Cross-Border Payments - Advanced",
  "NACHA and the ACH Record Layout - Advanced",
  "PCI DSS and Protecting Card Data - Advanced",
  "Fraud Signals Hidden in Transaction Records - Advanced",
  "Audit Trails: Hash Chains and Immutable History - Advanced",
  "Multi-Currency Transactions and FX - Advanced",
  "Designing an Append-Only Transaction Ledger - Advanced",
  "Reversal Records and Compensating Transactions - Advanced",
  "Real-Time Payments: RTP and FedNow Records - Advanced",
  "The Full Transaction Lifecycle, End to End - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Transaction Record Study — "+safe+"\n"
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
    name:topic+' — transaction record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A transaction record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"transaction-record-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-transaction-records-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('transaction-records',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
