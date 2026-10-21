(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG="form-database";
var CATS=["business","government","legal","medical","web"];
var PREFIX="JAH-FORMS-";
var KIND="form";
/* rows: [category, title, description-head] — seeded from the archive */
var B=[
 ["web","Contact Form","FORM: Contact Form. A standard website contact form. Collects name, email, subject, and message; the workhorse"],
 ["business","Job Application Form","FORM: Job Application Form. A hiring intake form used by employers to collect applicant basics before intervie"],
 ["medical","Medical Intake Form","FORM: Medical Intake Form. The clipboard form every clinic hands out: identity, emergency contact, allergies, "],
 ["medical","Patient Consent Form","FORM: Patient Consent Form. Informed-consent capture: names the procedure and records the patient's explicit a"],
 ["government","Tax Worksheet","FORM: Tax Worksheet. A simplified income-tax worksheet in the style of government tax forms: income minus dedu"],
 ["business","Business Invoice Form","FORM: Business Invoice Form. The form behind every invoice: who pays, what for, how much, by when. Invoice num"],
 ["business","Employee Onboarding Form","FORM: Employee Onboarding Form. HR's day-one form: who is joining, where they sit in the org, and when they st"],
 ["legal","Rental Application Form","FORM: Rental Application Form. What landlords ask before handing over keys: identity, address history, income,"],
 ["web","Event Registration Form","FORM: Event Registration Form. Sign-up form for conferences, workshops, and community events. Guest count and "],
 ["business","Customer Feedback Survey","FORM: Customer Feedback Survey. Post-purchase survey: a numeric rating plus open-ended pros and cons. Keep sur"],
 ["business","Purchase Order Form","FORM: Purchase Order Form. A buyer's formal offer to a vendor: PO number, line items, quantities, prices. A pu"],
 ["business","Travel Expense Report","FORM: Travel Expense Report. Reimbursement form: who spent what, on which trip, with receipt confirmation. Fin"]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:b[1],description:b[2],category:cat,
    ladder_rank:1+((rnd()*3)|0),
    demo:'#!/usr/bin/env python3\nprint('+JSON.stringify('demo for '+b[1])+')\n',
    provenance:'Boundless generator jahdb-'+SLUG+'-1.0; seed '+seed+'.',
    last_verified:'2026-10-21',
    src:"public-harvest",
    _seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var rx=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!rx.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||!r.description.length)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].id!==rec.id){e.push('near-duplicate title');break;}
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-'+SLUG+'-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
