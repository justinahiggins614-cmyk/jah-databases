(function(){'use strict';
/* JAH The Insurance Claims and Benefits Database generator — jahdb-insurance-claims-benefits-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INCB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Insurance Is — Industry Overview - Foundations",
  "The Insurance Policy — Parts and Terms - Foundations",
  "Premiums — How Prices Are Set - Foundations",
  "First Notice of Loss (FNOL) - Foundations",
  "The Claims Adjuster - Foundations",
  "Auto Insurance Claims - Foundations",
  "Property Insurance Claims - Foundations",
  "What Public Benefits Are — Overview - Foundations",
  "Benefit Applications - Foundations",
  "Eligibility Determination - Foundations",
  "Case Workers and Service Delivery - Foundations",
  "Insurance Math I — Loss Ratios and Premiums - Foundations",
 ],
 "Compounded": [
  "Claims Investigation - Compounded",
  "Setting Claim Reserves - Compounded",
  "Settlement Negotiation - Compounded",
  "Subrogation and Recovery Operations - Compounded",
  "Fraud Detection — SIU - Compounded",
  "Liability Claims - Compounded",
  "Workers' Compensation Claims - Compounded",
  "Health Claims Adjudication - Compounded",
  "SNAP — Food Assistance Operations - Compounded",
  "Medicaid Operations - Compounded",
  "Unemployment Insurance - Compounded",
 ],
 "Advanced": [
  "Combined Ratio and Underwriting Profit - Advanced",
  "Reinsurance Treaties and Programs - Advanced",
  "Catastrophe Claims Operations - Advanced",
  "The Appeals Process - Advanced",
  "Social Security Administration - Advanced",
  "Benefit Delivery — EBT and Payments - Advanced",
  "Program Integrity - Advanced",
  "Call Centers and Field Offices - Advanced",
  "Disability Determinations - Advanced",
  "The Actuarial Function in Insurance - Advanced",
  "Insurance and Benefits Mastery Review — Running the Whole System - Advanced",
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('insurance-claims-benefits',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
