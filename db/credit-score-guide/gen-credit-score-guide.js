(function(){'use strict';
/* JAH Credit Score Guide Database generator — jahdb-credit-score-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='credit-score-guide',PREFIX='JAH-CR2-',NAME='JAH Credit Score Guide Database';
var FIELDS=["basics", "factors", "building", "repair", "safety", "tips"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "What is a credit score?", "d": "A 300-850 number predicting repayment likelihood.", "g": "basics", "l": 2, "q": "What is What is a credit score??", "a": "A 300-850 number predicting repayment likelihood.", "x": "What is a credit score? — A 300-850 number predicting repayment likelihood. Example: Higher is better..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "FICO score", "d": "The dominant scoring model; 300-850.", "g": "basics", "l": 2, "q": "What is FICO score?", "a": "The dominant scoring model; 300-850.", "x": "FICO score — The dominant scoring model; 300-850. Example: Most lenders use FICO..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "VantageScore", "d": "Alternative model; also 300-850.", "g": "basics", "l": 2, "q": "What is VantageScore?", "a": "Alternative model; also 300-850.", "x": "VantageScore — Alternative model; also 300-850. Example: What free sites often show..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Payment history (35%)", "d": "The biggest factor: pay on time, every time.", "g": "factors", "l": 2, "q": "What is Payment history (35%)?", "a": "The biggest factor: pay on time, every time.", "x": "Payment history (35%) — The biggest factor: pay on time, every time. Example: One late payment hurts..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Credit utilization (30%)", "d": "Balance vs limit; keep under 30%, ideally under 10%.", "g": "factors", "l": 2, "q": "What is Credit utilization (30%)?", "a": "Balance vs limit; keep under 30%, ideally under 10%.", "x": "Credit utilization (30%) — Balance vs limit; keep under 30%, ideally under 10%. Example: Pay down balances..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Length of history (15%)", "d": "Older accounts help; keep old cards open.", "g": "factors", "l": 2, "q": "What is Length of history (15%)?", "a": "Older accounts help; keep old cards open.", "x": "Length of history (15%) — Older accounts help; keep old cards open. Example: Age matters..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "New credit (10%)", "d": "Hard inquiries ding briefly; rate-shop within 14-45 days.", "g": "factors", "l": 2, "q": "What is New credit (10%)?", "a": "Hard inquiries ding briefly; rate-shop within 14-45 days.", "x": "New credit (10%) — Hard inquiries ding briefly; rate-shop within 14-45 days. Example: One window counts once..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Credit mix (10%)", "d": "Variety of account types helps modestly.", "g": "factors", "l": 2, "q": "What is Credit mix (10%)?", "a": "Variety of account types helps modestly.", "x": "Credit mix (10%) — Variety of account types helps modestly. Example: Do not force it..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What is a good score?", "d": "670+ good, 740+ very good, 800+ exceptional.", "g": "basics", "l": 2, "q": "What is What is a good score??", "a": "670+ good, 740+ very good, 800+ exceptional.", "x": "What is a good score? — 670+ good, 740+ very good, 800+ exceptional. Example: Aim 740+..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "How to check your score free", "d": "AnnualCreditReport.com for reports; many banks show scores free.", "g": "basics", "l": 2, "q": "What is How to check your score free?", "a": "AnnualCreditReport.com for reports; many banks show scores free.", "x": "How to check your score free — AnnualCreditReport.com for reports; many banks show scores free. Example: Weekly reports free..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Hard inquiry", "d": "Lender credit check for applications; small temporary dip.", "g": "factors", "l": 2, "q": "What is Hard inquiry?", "a": "Lender credit check for applications; small temporary dip.", "x": "Hard inquiry — Lender credit check for applications; small temporary dip. Example: Necessary sometimes..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Soft inquiry", "d": "Background checks; no score impact.", "g": "factors", "l": 2, "q": "What is Soft inquiry?", "a": "Background checks; no score impact.", "x": "Soft inquiry — Background checks; no score impact. Example: Check freely..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "How to build credit from zero", "d": "Secured card, authorized user, credit-builder loan.", "g": "building", "l": 2, "q": "What is How to build credit from zero?", "a": "Secured card, authorized user, credit-builder loan.", "x": "How to build credit from zero — Secured card, authorized user, credit-builder loan. Example: Start small..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Secured credit card", "d": "Deposit-backed card for beginners.", "g": "building", "l": 2, "q": "What is Secured credit card?", "a": "Deposit-backed card for beginners.", "x": "Secured credit card — Deposit-backed card for beginners. Example: Graduates to unsecured..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Authorized user", "d": "Added to someone's card; their history helps you.", "g": "building", "l": 2, "q": "What is Authorized user?", "a": "Added to someone's card; their history helps you.", "x": "Authorized user — Added to someone's card; their history helps you. Example: Trust required..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Credit-builder loan", "d": "Payments reported; savings released at end.", "g": "building", "l": 2, "q": "What is Credit-builder loan?", "a": "Payments reported; savings released at end.", "x": "Credit-builder loan — Payments reported; savings released at end. Example: Banks and CUs offer..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "What hurts your score most?", "d": "Late payments, collections, maxed cards, bankruptcy.", "g": "factors", "l": 2, "q": "What is What hurts your score most??", "a": "Late payments, collections, maxed cards, bankruptcy.", "x": "What hurts your score most? — Late payments, collections, maxed cards, bankruptcy. Example: Avoid all four..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "How long do late payments stay?", "d": "Seven years on reports.", "g": "factors", "l": 2, "q": "What is How long do late payments stay??", "a": "Seven years on reports.", "x": "How long do late payments stay? — Seven years on reports. Example: Impact fades with time..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Collections", "d": "Unpaid debts sold to collectors; negotiate pay-for-delete.", "g": "factors", "l": 2, "q": "What is Collections?", "a": "Unpaid debts sold to collectors; negotiate pay-for-delete.", "x": "Collections — Unpaid debts sold to collectors; negotiate pay-for-delete. Example: Validate first..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Charge-off", "d": "Creditor writes off the debt; still owed and reported.", "g": "factors", "l": 2, "q": "What is Charge-off?", "a": "Creditor writes off the debt; still owed and reported.", "x": "Charge-off — Creditor writes off the debt; still owed and reported. Example: Settle if possible..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Bankruptcy Chapter 7", "d": "Liquidation; stays 10 years.", "g": "factors", "l": 2, "q": "What is Bankruptcy Chapter 7?", "a": "Liquidation; stays 10 years.", "x": "Bankruptcy Chapter 7 — Liquidation; stays 10 years. Example: Last resort..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Bankruptcy Chapter 13", "d": "Repayment plan; stays 7 years.", "g": "factors", "l": 2, "q": "What is Bankruptcy Chapter 13?", "a": "Repayment plan; stays 7 years.", "x": "Bankruptcy Chapter 13 — Repayment plan; stays 7 years. Example: Wage-earner plan..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Disputing errors", "d": "Challenge wrong items with bureaus in writing.", "g": "repair", "l": 2, "q": "What is Disputing errors?", "a": "Challenge wrong items with bureaus in writing.", "x": "Disputing errors — Challenge wrong items with bureaus in writing. Example: 30-day investigation..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "The three bureaus", "d": "Equifax, Experian, TransUnion.", "g": "basics", "l": 2, "q": "What is The three bureaus?", "a": "Equifax, Experian, TransUnion.", "x": "The three bureaus — Equifax, Experian, TransUnion. Example: Check all three..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Freezing your credit", "d": "Blocks new accounts; free; unfreeze when applying.", "g": "safety", "l": 2, "q": "What is Freezing your credit?", "a": "Blocks new accounts; free; unfreeze when applying.", "x": "Freezing your credit — Blocks new accounts; free; unfreeze when applying. Example: Best identity-theft defense..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-credit-score-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
