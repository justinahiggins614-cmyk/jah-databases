(function(){'use strict';
/* JAH The Insurance Claims and Benefits Signature Database generator — jahdb-insurance-claims-benefits-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INCBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Shared Shield — The Signature View (Signature Edition) - Foundations",
  "The Written Promise — Signature Policy (Signature Edition) - Foundations",
  "The Honest Price — Signature Premiums (Signature Edition) - Foundations",
  "The First Call — Signature FNOL (Signature Edition) - Foundations",
  "The Fair Judge — Signature Adjuster (Signature Edition) - Foundations",
  "The Road's Reckoning — Signature Auto Claims (Signature Edition) - Foundations",
  "The Rebuilding — Signature Property Claims (Signature Edition) - Foundations",
  "The Safety Net — Signature Benefits View (Signature Edition) - Foundations",
  "The Open Door — Signature Applications (Signature Edition) - Foundations",
  "The Careful Weighing — Signature Determination (Signature Edition) - Foundations",
  "The Human Link — Signature Case Work (Signature Edition) - Foundations",
  "The First Reckoning — Signature Insurance Math (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "The Truth-Finding — Signature Investigation (Signature Edition) - Compounded",
  "The Honest Estimate — Signature Reserves (Signature Edition) - Compounded",
  "The Fair Bargain — Signature Settlement (Signature Edition) - Compounded",
  "The Recovery — Signature Subrogation (Signature Edition) - Compounded",
  "The Watchers — Signature Fraud Detection (Signature Edition) - Compounded",
  "The Neighbor's Harm — Signature Liability (Signature Edition) - Compounded",
  "The Worker's Bargain — Signature Workers' Comp (Signature Edition) - Compounded",
  "The Careful Payment — Signature Health Adjudication (Signature Edition) - Compounded",
  "The Full Table — Signature Food Assistance (Signature Edition) - Compounded",
  "The Healing Coverage — Signature Medicaid (Signature Edition) - Compounded",
  "The Bridge Between Jobs — Signature Unemployment (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Bottom Line — Signature Combined Ratio (Signature Edition) - Advanced",
  "The Insurer's Shield — Signature Reinsurance (Signature Edition) - Advanced",
  "The Surge — Signature Catastrophe Response (Signature Edition) - Advanced",
  "The Second Hearing — Signature Appeals (Signature Edition) - Advanced",
  "The Earned Rest — Signature Social Security (Signature Edition) - Advanced",
  "The Last Mile — Signature Benefit Delivery (Signature Edition) - Advanced",
  "The Guarded Purse — Signature Program Integrity (Signature Edition) - Advanced",
  "The Public's Door — Signature Service Centers (Signature Edition) - Advanced",
  "The Hardest Call — Signature Disability (Signature Edition) - Advanced",
  "The Measurers — Signature Actuarial Science (Signature Edition) - Advanced",
  "The Steward's Ledger — Signature Mastery (Signature Edition) - Advanced",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\n"
   + "# Loss-ratio structural sample calculator (insurance)\n"
   + "losses, prem = 650000.0, 1000000.0\n"
   + "lr = losses/prem\n"
   + "print('sample losses:', losses, 'earned premium:', prem)\n"
   + "print('sample loss ratio:', round(lr,3))\n"
   + "assert 0 <= lr <= 3\n"
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
    name:topic+' — insurance and benefits record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A insurance and benefits record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"insurance-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-insurance-claims-benefits-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('insurance-claims-benefits-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
