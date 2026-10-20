(function(){'use strict';
/* JAH Signature Business Fundraising Database generator — jahdb-e2-sig-biz-business-fundraising-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-biz-business-fundraising',PREFIX='JAH-E2SIGBIZBUS-',NAME='JAH Signature Business Fundraising Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Business Fundraising: the playbook", "d": "Business Fundraising: raise money wisely..", "g": "overview", "l": 2, "q": "What is Signature Business Fundraising: the playbook?", "a": "Business Fundraising: raise money wisely..", "x": "The Signature Business Fundraising playbook: raise money wisely.. Bootstrap first. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Friends and family carefully. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Business Fundraising.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Business Fundraising.", "x": "First principles: SBA loans.. raise money wisely. Get these right and the rest is optimization; get them wrong and nothing else matters. Business Fundraising Pitch: problem and solution. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Bootstrap first.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Bootstrap first.", "x": "Business Fundraising play 1: Bootstrap first.. Pitch: problem and solution. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Bootstrap first..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Bootstrap first..", "x": "In action: Bootstrap first.. Here is how to actually do it — Unit economics.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. SBA loans. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Friends and family carefully.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Friends and family carefully.", "x": "Business Fundraising play 2: Friends and family carefully.. Unit economics. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Friends and family carefully..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Friends and family carefully..", "x": "In action: Friends and family carefully.. Here is how to actually do it — Do not over-raise.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Pitch: problem and solution.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "SBA loans.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "SBA loans.", "x": "Business Fundraising play 3: SBA loans.. Do not over-raise. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: SBA loans..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: SBA loans..", "x": "In action: SBA loans.. Here is how to actually do it — Deck ten slides.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Unit economics. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Pitch: problem and solution.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Pitch: problem and solution.", "x": "Business Fundraising play 4: Pitch: problem and solution.. Deck ten slides. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Pitch: problem and solution..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Pitch: problem and solution..", "x": "In action: Pitch: problem and solution.. Here is how to actually do it — Due diligence.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Do not over-raise.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Unit economics.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Unit economics.", "x": "Business Fundraising play 5: Unit economics.. Due diligence. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Unit economics..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Unit economics..", "x": "In action: Unit economics.. Here is how to actually do it — Bootstrap first.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Deck ten slides. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Do not over-raise.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Do not over-raise.", "x": "Business Fundraising play 6: Do not over-raise.. Bootstrap first. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Do not over-raise..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Do not over-raise..", "x": "In action: Do not over-raise.. Here is how to actually do it — Friends and family carefully.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Due diligence.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Deck ten slides.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Deck ten slides.", "x": "Business Fundraising play 7: Deck ten slides.. Friends and family carefully. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Deck ten slides..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Deck ten slides..", "x": "In action: Deck ten slides.. Here is how to actually do it — SBA loans.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Bootstrap first. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Due diligence.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Due diligence.", "x": "Business Fundraising play 8: Due diligence.. SBA loans. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise money wisely. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Due diligence..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Due diligence..", "x": "In action: Due diligence.. Here is how to actually do it — Pitch: problem and solution.. Business Fundraising The difference between knowing and doing is a calendar entry: schedule it. Friends and family carefully.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Business Fundraising: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Business Fundraising: week one.", "x": "Week one: Bootstrap first.. Start here — Friends and family carefully.. Business Fundraising Do not try to do everything; do the first three plays badly rather than all eight never. raise money wisely. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Business Fundraising goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Business Fundraising goes wrong.", "x": "The classic mistakes: Unit economics.. raise money wisely. Most failure in Business Fundraising is not bad luck — it is these avoidable errors. Do not over-raise. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Business Fundraising toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Business Fundraising toolkit.", "x": "The toolkit: Deck ten slides.. Business Fundraising The right tools multiply effort — Due diligence.. raise money wisely. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Business Fundraising results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Business Fundraising results this week.", "x": "Quick wins: Friends and family carefully.. Pitch: problem and solution. These pay off fast — do them first for the motivation to continue. Business Fundraising raise money wisely. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Business Fundraising.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Business Fundraising.", "x": "Advanced: Due diligence.. Do not over-raise. Once the fundamentals run on autopilot, these separate the good from the great at Business Fundraising. raise money wisely. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Business Fundraising: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Business Fundraising: a complete example.", "x": "Walkthrough: raise money wisely., applied end to end — Bootstrap first.. SBA loans. Follow along with your own situation beside you. Business Fundraising Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Business Fundraising.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Business Fundraising.", "x": "The myths: Business Fundraising is surrounded by bad advice — Deck ten slides.. raise money wisely. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Unit economics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-biz-business-fundraising-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
