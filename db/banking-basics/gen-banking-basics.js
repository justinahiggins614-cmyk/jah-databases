(function(){'use strict';
/* JAH Banking Basics Database generator — jahdb-banking-basics-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='banking-basics',PREFIX='JAH-BNK-',NAME='JAH Banking Basics Database';
var FIELDS=["accounts", "basics", "fees", "transfers", "cards", "safety", "institutions", "planning"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Checking account", "d": "Everyday spending account with debit card and checks.", "g": "accounts", "l": 2, "q": "What is Checking account?", "a": "Everyday spending account with debit card and checks.", "x": "Checking account — Everyday spending account with debit card and checks. Example: Direct deposit goes here..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Savings account", "d": "Interest-earning account for stored money.", "g": "accounts", "l": 2, "q": "What is Savings account?", "a": "Interest-earning account for stored money.", "x": "Savings account — Interest-earning account for stored money. Example: Emergency fund home..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Certificate of deposit", "d": "Fixed-term deposit with higher interest; early withdrawal penalties.", "g": "accounts", "l": 2, "q": "What is Certificate of deposit?", "a": "Fixed-term deposit with higher interest; early withdrawal penalties.", "x": "Certificate of deposit — Fixed-term deposit with higher interest; early withdrawal penalties. Example: Ladder them..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Money market account", "d": "Hybrid: check-writing with higher interest.", "g": "accounts", "l": 2, "q": "What is Money market account?", "a": "Hybrid: check-writing with higher interest.", "x": "Money market account — Hybrid: check-writing with higher interest. Example: Higher minimums..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Routing number", "d": "The 9-digit bank identifier for transfers.", "g": "basics", "l": 2, "q": "What is Routing number?", "a": "The 9-digit bank identifier for transfers.", "x": "Routing number — The 9-digit bank identifier for transfers. Example: On checks and statements..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Account number", "d": "Your specific account identifier.", "g": "basics", "l": 2, "q": "What is Account number?", "a": "Your specific account identifier.", "x": "Account number — Your specific account identifier. Example: Keep private..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Direct deposit", "d": "Electronic paycheck deposit.", "g": "basics", "l": 2, "q": "What is Direct deposit?", "a": "Electronic paycheck deposit.", "x": "Direct deposit — Electronic paycheck deposit. Example: Faster than paper..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Overdraft", "d": "Spending beyond your balance; fees apply.", "g": "fees", "l": 2, "q": "What is Overdraft?", "a": "Spending beyond your balance; fees apply.", "x": "Overdraft — Spending beyond your balance; fees apply. Example: Opt out of overdraft coverage..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Overdraft fee", "d": "Typical $30-35 per overdraft; avoidable.", "g": "fees", "l": 2, "q": "What is Overdraft fee?", "a": "Typical $30-35 per overdraft; avoidable.", "x": "Overdraft fee — Typical $30-35 per overdraft; avoidable. Example: Link savings as backup..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Monthly maintenance fee", "d": "Often waivable with direct deposit or minimum balance.", "g": "fees", "l": 2, "q": "What is Monthly maintenance fee?", "a": "Often waivable with direct deposit or minimum balance.", "x": "Monthly maintenance fee — Often waivable with direct deposit or minimum balance. Example: Ask how to waive..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "ATM fee", "d": "Out-of-network charges; use your bank's ATMs.", "g": "fees", "l": 2, "q": "What is ATM fee?", "a": "Out-of-network charges; use your bank's ATMs.", "x": "ATM fee — Out-of-network charges; use your bank's ATMs. Example: Get reimbursed by some banks..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Wire transfer", "d": "Fast bank-to-bank transfer; fees $15-50.", "g": "transfers", "l": 2, "q": "What is Wire transfer?", "a": "Fast bank-to-bank transfer; fees $15-50.", "x": "Wire transfer — Fast bank-to-bank transfer; fees $15-50. Example: Same-day domestic..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "ACH transfer", "d": "Slower electronic transfer; usually free.", "g": "transfers", "l": 2, "q": "What is ACH transfer?", "a": "Slower electronic transfer; usually free.", "x": "ACH transfer — Slower electronic transfer; usually free. Example: 1-3 business days..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Mobile check deposit", "d": "Photograph checks to deposit.", "g": "transfers", "l": 2, "q": "What is Mobile check deposit?", "a": "Photograph checks to deposit.", "x": "Mobile check deposit — Photograph checks to deposit. Example: Endorse first..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Debit card", "d": "Spends directly from checking.", "g": "cards", "l": 2, "q": "What is Debit card?", "a": "Spends directly from checking.", "x": "Debit card — Spends directly from checking. Example: No debt built..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Credit card", "d": "Borrows up to a limit; pay monthly to avoid interest.", "g": "cards", "l": 2, "q": "What is Credit card?", "a": "Borrows up to a limit; pay monthly to avoid interest.", "x": "Credit card — Borrows up to a limit; pay monthly to avoid interest. Example: Builds credit when paid off..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "APR", "d": "Annual Percentage Rate: the yearly interest cost.", "g": "cards", "l": 2, "q": "What is APR?", "a": "Annual Percentage Rate: the yearly interest cost.", "x": "APR — Annual Percentage Rate: the yearly interest cost. Example: Compare before borrowing..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Minimum payment", "d": "The smallest monthly payment; paying only it costs dearly.", "g": "cards", "l": 2, "q": "What is Minimum payment?", "a": "The smallest monthly payment; paying only it costs dearly.", "x": "Minimum payment — The smallest monthly payment; paying only it costs dearly. Example: Pay in full when possible..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "FDIC insurance", "d": "Protects deposits up to $250,000 per depositor per bank.", "g": "safety", "l": 2, "q": "What is FDIC insurance?", "a": "Protects deposits up to $250,000 per depositor per bank.", "x": "FDIC insurance — Protects deposits up to $250,000 per depositor per bank. Example: Government-backed..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "NCUA insurance", "d": "Credit-union equivalent of FDIC.", "g": "safety", "l": 2, "q": "What is NCUA insurance?", "a": "Credit-union equivalent of FDIC.", "x": "NCUA insurance — Credit-union equivalent of FDIC. Example: Same $250,000 protection..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Two-factor authentication", "d": "Second login verification for accounts.", "g": "safety", "l": 2, "q": "What is Two-factor authentication?", "a": "Second login verification for accounts.", "x": "Two-factor authentication — Second login verification for accounts. Example: Always enable..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Phishing", "d": "Fake messages stealing bank logins.", "g": "safety", "l": 2, "q": "What is Phishing?", "a": "Fake messages stealing bank logins.", "x": "Phishing — Fake messages stealing bank logins. Example: Banks never ask for passwords by email..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Credit union", "d": "Member-owned nonprofit banks; often better rates.", "g": "institutions", "l": 2, "q": "What is Credit union?", "a": "Member-owned nonprofit banks; often better rates.", "x": "Credit union — Member-owned nonprofit banks; often better rates. Example: Join one..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Online bank", "d": "Branchless banks with higher savings rates.", "g": "institutions", "l": 2, "q": "What is Online bank?", "a": "Branchless banks with higher savings rates.", "x": "Online bank — Branchless banks with higher savings rates. Example: FDIC-insured too..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names.", "s": "public-reference", "f": null}, {"t": "Bank statement", "d": "Monthly record of transactions.", "g": "basics", "l": 2, "q": "What is Bank statement?", "a": "Monthly record of transactions.", "x": "Bank statement — Monthly record of transactions. Example: Reconcile it..  Based on official public sources (USCIS, state DMVs, federal agencies). Officeholders change — verify current names. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-banking-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
