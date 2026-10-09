(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function p2(n){return String(n).padStart(2,'0');}
var CATS=['contract','tort','criminal','property','constitutional','family'];
var SUR=['Holloway','Vance','Marlowe','Quill','Ashford','Bennett','Calloway','Drexler','Ellery','Fairbanks','Granger','Harlow','Inskip','Judd','Kestrel','Larkin','Merritt','Norwood','Osgood','Pemberton','Radcliffe','Sutton','Thackeray','Upton','Vale','Whitmore','Yardley','Zimmerman','Blackwood','Corvane','Dunmore','Easton','Fenwick','Godfrey','Hale','Irving'];
var STATES=['California','Texas','New York','Florida','Illinois','Ohio','Georgia','Virginia','Washington','Colorado','Arizona','Massachusetts'];
var COURTS=['U.S. Supreme Court','U.S. Court of Appeals','State Supreme Court','Superior Court','District Court'];
var REP=['N.E.3d','S.E.2d','P.3d','A.3d','N.W.2d','So. 3d'];
var HOLD={
 contract:['{A} breached the supply agreement by halting delivery without notice, and the court awarded {B} expectation damages measured by the contract price.','Because the merger clause controlled, the court enforced the written terms and rejected {A}\u2019s claim of an oral side promise.','The court found the liquidated-damages clause enforceable as a reasonable forecast of loss, and entered judgment for {B}.'],
 tort:['The court held {A} liable in negligence after finding a duty of care, a breach of that duty, and harm that was reasonably foreseeable to {B}.','Applying comparative fault, the jury\u2019s award to {B} was reduced in proportion to {B}\u2019s own negligence.','The court dismissed the strict-liability claim because {A}\u2019s activity was not abnormally dangerous as a matter of law.'],
 criminal:['The court affirmed the conviction, holding that the evidence viewed in the light most favorable to the state proved every element beyond a reasonable doubt.','The sentence imposed on {A} was vacated and remanded after the court found the sentencing range had been miscalculated.','The court suppressed the seized evidence, ruling that the search exceeded the scope of the warrant and tainted the prosecution of {A}.'],
 property:['The court quieted title in favor of {B}, finding the chain of deeds unbroken and {A}\u2019s adverse-possession claim unsupported by continuous use.','The easement claimed by {A} was denied because the use was permissive rather than hostile throughout the statutory period.','The court partitioned the parcel between {A} and {B}, ordering sale and an equal division of proceeds.'],
 constitutional:['The court held the ordinance unconstitutional as applied, finding it burdened protected expression without a compelling government interest.','The statute survived rational-basis review because the legislature\u2019s classification was reasonably related to a legitimate public purpose.','The court struck down the restriction, ruling that it singled out disfavored speakers in violation of equal protection.'],
 family:['The court awarded primary custody to {B}, finding that placement served the child\u2019s best interests after weighing stability, schooling, and each parent\u2019s caregiving history.','The support order against {A} was modified upward to reflect a material change in income since the prior decree.','The court approved the mediated parenting plan submitted by {A} and {B}, incorporating it into the final judgment.']};
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var ctype=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(CATS,rnd);
  var A=pick(SUR,rnd), B=pick(SUR,rnd);
  while(B===A)B=pick(SUR,rnd);
  var cname=A+' v. '+B;
  var court=pick(COURTS,rnd), juris=pick(STATES,rnd);
  var yr=ri(rnd,2015,2026);
  var dec=yr+'-'+p2(ri(rnd,1,12))+'-'+p2(ri(rnd,1,28));
  var holding=pick(HOLD[ctype],rnd).replace(/\{A\}/g,A).replace(/\{B\}/g,B);
  var nc=ri(rnd,1,2), cites=[];
  for(var i=0;i<nc;i++){
    var f=rnd();
    if(f<0.4)cites.push(ri(rnd,100,999)+' U.S. '+ri(rnd,1,999)+' ('+yr+')');
    else if(f<0.7)cites.push(ri(rnd,10,99)+' F.4th '+ri(rnd,100,999)+' ('+yr+')');
    else cites.push(ri(rnd,100,999)+' '+pick(REP,rnd)+' '+ri(rnd,100,999)+' ('+yr+')');
  }
  var nj=ri(rnd,1,2), judges=[], jp=SUR.slice();
  for(var j=0;j<nj&&jp.length;j++){judges.push(pick(['Justice','Judge'],rnd)+' '+jp.splice((rnd()*jp.length)|0,1)[0]);}
  var id='JAH-CASE-'+String(seed).padStart(6,'0');
  return {id:id,case_id:id,case_name:cname,title:cname,description:holding.slice(0,600),
    court:court,jurisdiction:juris,decision_date:dec,case_type:ctype,
    holding_summary:holding,citations:cites,judges:judges};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['record']};
  if(typeof r.id!=='string'||!/^JAH-CASE-\d{6}$/.test(r.id))e.push('id');
  if(r.case_id!==r.id)e.push('case_id');
  if(typeof r.case_name!=='string'||r.case_name.indexOf(' v. ')<0)e.push('case_name');
  if(r.title!==r.case_name)e.push('title');
  if(typeof r.description!=='string'||!r.description||r.description.length>600)e.push('description');
  if(typeof r.court!=='string'||!r.court)e.push('court');
  if(typeof r.jurisdiction!=='string'||!r.jurisdiction)e.push('jurisdiction');
  if(typeof r.decision_date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.decision_date))e.push('decision_date');
  if(CATS.indexOf(r.case_type)<0)e.push('case_type');
  if(typeof r.holding_summary!=='string'||!r.holding_summary||r.holding_summary.length>600)e.push('holding_summary');
  if(!Array.isArray(r.citations)||r.citations.length<1||r.citations.length>3)e.push('citations');
  if(!Array.isArray(r.judges)||r.judges.length<1||r.judges.length>3)e.push('judges');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-legal-cases-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('legal-cases',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;})();
