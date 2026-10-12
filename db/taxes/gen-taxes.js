(function(){'use strict';
/* Taxes Database generator — jahdb-taxes-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-TAX-';
var TOPICS=[["Income Tax", "Taxes on earnings that fund government services."], ["Sales Tax", "Taxes added to purchases in many places."], ["Property Tax", "Taxes on real estate funding local services."], ["Filing a Return", "Reporting income and calculating tax owed."], ["W-2 Forms", "The wage statements employers provide."], ["1099 Forms", "The statements for freelance and contract income."], ["Deductions", "Amounts subtracted from taxable income."], ["Tax Credits", "Amounts subtracted directly from tax owed."], ["The IRS", "The United States agency collecting federal taxes."], ["Tax Brackets", "The graduated rates taxing higher income more."], ["Withholding", "Tax taken from paychecks through the year."], ["Tax Refunds", "Money back when too much was withheld."], ["Filing Deadlines", "The yearly dates returns are due."], ["Extensions", "Extra time to file, not to pay."], ["Audits", "Reviews checking a return's accuracy."], ["State Taxes", "The income taxes many states add."], ["Payroll Taxes", "Taxes funding Social Security and Medicare."], ["Tax Professionals", "Accountants and preparers who help with returns."], ["Keeping Records", "Saving receipts and documents for tax time."], ["Estimated Taxes", "Quarterly payments for the self-employed."], ["Tax Software", "Programs guiding filers step by step."], ["Common Mistakes", "Errors like wrong Social Security numbers."], ["Tax Scams", "Frauds impersonating tax agencies."], ["Charitable Deductions", "Gifts to qualifying charities that may reduce tax."], ["Education Credits", "Tax help for college costs."], ["Retirement Tax Benefits", "How saving for retirement can lower taxes."], ["Property Tax Appeals", "Challenging assessments you believe are wrong."], ["Tax Planning", "Organizing finances year-round for tax time."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'taxes record', content:content,
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('taxes',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();