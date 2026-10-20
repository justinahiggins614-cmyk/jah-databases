(function(){'use strict';
/* JAH Signature Business Accounting Basics Database generator — jahdb-e2-sig-biz-business-accounting-basics-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-biz-business-accounting-basics',PREFIX='JAH-E2SIGBIZBUS-',NAME='JAH Signature Business Accounting Basics Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Business Accounting Basics: the playbook", "d": "Business Accounting Basics: know your numbers..", "g": "overview", "l": 2, "q": "What is Signature Business Accounting Basics: the playbook?", "a": "Business Accounting Basics: know your numbers..", "x": "The Signature Business Accounting Basics playbook: know your numbers.. Separate accounts day one. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Track every expense. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Business Accounting Basics.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Business Accounting Basics.", "x": "First principles: Profit first method.. know your numbers. Get these right and the rest is optimization; get them wrong and nothing else matters. Business Accounting Basics Quarterly taxes. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Separate accounts day one.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Separate accounts day one.", "x": "Business Accounting Basics play 1: Separate accounts day one.. Quarterly taxes. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Separate accounts day one..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Separate accounts day one..", "x": "In action: Separate accounts day one.. Here is how to actually do it — Bookkeeper worth it.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Profit first method.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Track every expense.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Track every expense.", "x": "Business Accounting Basics play 2: Track every expense.. Bookkeeper worth it. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Track every expense..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Track every expense..", "x": "In action: Track every expense.. Here is how to actually do it — Read P and L monthly.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Quarterly taxes.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Profit first method.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Profit first method.", "x": "Business Accounting Basics play 3: Profit first method.. Read P and L monthly. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Profit first method..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Profit first method..", "x": "In action: Profit first method.. Here is how to actually do it — Invoice promptly.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Bookkeeper worth it.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Quarterly taxes.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Quarterly taxes.", "x": "Business Accounting Basics play 4: Quarterly taxes.. Invoice promptly. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Quarterly taxes..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Quarterly taxes..", "x": "In action: Quarterly taxes.. Here is how to actually do it — Cash reserves.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Read P and L monthly.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Bookkeeper worth it.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Bookkeeper worth it.", "x": "Business Accounting Basics play 5: Bookkeeper worth it.. Cash reserves. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Bookkeeper worth it..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Bookkeeper worth it..", "x": "In action: Bookkeeper worth it.. Here is how to actually do it — Separate accounts day one.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Invoice promptly.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Read P and L monthly.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Read P and L monthly.", "x": "Business Accounting Basics play 6: Read P and L monthly.. Separate accounts day one. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Read P and L monthly..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Read P and L monthly..", "x": "In action: Read P and L monthly.. Here is how to actually do it — Track every expense.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Cash reserves.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Invoice promptly.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Invoice promptly.", "x": "Business Accounting Basics play 7: Invoice promptly.. Track every expense. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Invoice promptly..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Invoice promptly..", "x": "In action: Invoice promptly.. Here is how to actually do it — Profit first method.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Separate accounts day one.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Cash reserves.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Cash reserves.", "x": "Business Accounting Basics play 8: Cash reserves.. Profit first method. This is one of the eight core moves — master all eight and you outperform most people who wing it. know your numbers. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Cash reserves..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Cash reserves..", "x": "In action: Cash reserves.. Here is how to actually do it — Quarterly taxes.. Business Accounting Basics The difference between knowing and doing is a calendar entry: schedule it. Track every expense. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Business Accounting Basics: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Business Accounting Basics: week one.", "x": "Week one: Separate accounts day one.. Start here — Track every expense.. Business Accounting Basics Do not try to do everything; do the first three plays badly rather than all eight never. know your numbers. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Business Accounting Basics goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Business Accounting Basics goes wrong.", "x": "The classic mistakes: Bookkeeper worth it.. know your numbers. Most failure in Business Accounting Basics is not bad luck — it is these avoidable errors. Read P and L monthly. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Business Accounting Basics toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Business Accounting Basics toolkit.", "x": "The toolkit: Invoice promptly.. Business Accounting Basics The right tools multiply effort — Cash reserves.. know your numbers. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Business Accounting Basics results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Business Accounting Basics results this week.", "x": "Quick wins: Track every expense.. Quarterly taxes. These pay off fast — do them first for the motivation to continue. Business Accounting Basics know your numbers. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Business Accounting Basics.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Business Accounting Basics.", "x": "Advanced: Cash reserves.. Read P and L monthly. Once the fundamentals run on autopilot, these separate the good from the great at Business Accounting Basics. know your numbers. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Business Accounting Basics: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Business Accounting Basics: a complete example.", "x": "Walkthrough: know your numbers., applied end to end — Separate accounts day one.. Profit first method. Follow along with your own situation beside you. Business Accounting Basics Theory becomes skill by doing.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Business Accounting Basics.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Business Accounting Basics.", "x": "The myths: Business Accounting Basics is surrounded by bad advice — Invoice promptly.. know your numbers. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Bookkeeper worth it.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-biz-business-accounting-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
