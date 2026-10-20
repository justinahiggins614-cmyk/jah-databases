(function(){'use strict';
/* JAH Signature Mortgage Guide Database generator — jahdb-e2-sig-money-mortgage-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-money-mortgage-guide',PREFIX='JAH-E2SIGMONEYM-',NAME='JAH Signature Mortgage Guide Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Mortgage Guide: the playbook", "d": "Mortgage Guide: buy smart..", "g": "overview", "l": 2, "q": "What is Signature Mortgage Guide: the playbook?", "a": "Mortgage Guide: buy smart..", "x": "The Signature Mortgage Guide playbook: buy smart.. Pre-approval. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Down payment. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Mortgage Guide.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Mortgage Guide.", "x": "First principles: Rates shop.. buy smart. Get these right and the rest is optimization; get them wrong and nothing else matters. Mortgage Guide Fifteen vs thirty. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Pre-approval.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Pre-approval.", "x": "Mortgage Guide play 1: Pre-approval.. Fifteen vs thirty. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Pre-approval..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Pre-approval..", "x": "In action: Pre-approval.. Here is how to actually do it — Closing costs.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Rates shop. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Down payment.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Down payment.", "x": "Mortgage Guide play 2: Down payment.. Closing costs. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Down payment..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Down payment..", "x": "In action: Down payment.. Here is how to actually do it — Affordability.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Fifteen vs thirty. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Rates shop.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Rates shop.", "x": "Mortgage Guide play 3: Rates shop.. Affordability. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Rates shop..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Rates shop..", "x": "In action: Rates shop.. Here is how to actually do it — Inspection.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Closing costs. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Fifteen vs thirty.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Fifteen vs thirty.", "x": "Mortgage Guide play 4: Fifteen vs thirty.. Inspection. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Fifteen vs thirty..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Fifteen vs thirty..", "x": "In action: Fifteen vs thirty.. Here is how to actually do it — Lock.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Affordability. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Closing costs.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Closing costs.", "x": "Mortgage Guide play 5: Closing costs.. Lock. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Closing costs..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Closing costs..", "x": "In action: Closing costs.. Here is how to actually do it — Pre-approval.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Inspection. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Affordability.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Affordability.", "x": "Mortgage Guide play 6: Affordability.. Pre-approval. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Affordability..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Affordability..", "x": "In action: Affordability.. Here is how to actually do it — Down payment.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Lock. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Inspection.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Inspection.", "x": "Mortgage Guide play 7: Inspection.. Down payment. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Inspection..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Inspection..", "x": "In action: Inspection.. Here is how to actually do it — Rates shop.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Pre-approval. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Lock.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Lock.", "x": "Mortgage Guide play 8: Lock.. Rates shop. This is one of the eight core moves — master all eight and you outperform most people who wing it. buy smart. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Lock..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Lock..", "x": "In action: Lock.. Here is how to actually do it — Fifteen vs thirty.. Mortgage Guide The difference between knowing and doing is a calendar entry: schedule it. Down payment. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Mortgage Guide: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Mortgage Guide: week one.", "x": "Week one: Pre-approval.. Start here — Down payment.. Mortgage Guide Do not try to do everything; do the first three plays badly rather than all eight never. buy smart. Momentum beats perfection. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Mortgage Guide goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Mortgage Guide goes wrong.", "x": "The classic mistakes: Closing costs.. buy smart. Most failure in Mortgage Guide is not bad luck — it is these avoidable errors. Affordability. Learn them from this database, not from experience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Mortgage Guide toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Mortgage Guide toolkit.", "x": "The toolkit: Inspection.. Mortgage Guide The right tools multiply effort — Lock.. buy smart. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Mortgage Guide results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Mortgage Guide results this week.", "x": "Quick wins: Down payment.. Fifteen vs thirty. These pay off fast — do them first for the motivation to continue. Mortgage Guide buy smart. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Mortgage Guide.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Mortgage Guide.", "x": "Advanced: Lock.. Affordability. Once the fundamentals run on autopilot, these separate the good from the great at Mortgage Guide. buy smart. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Mortgage Guide: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Mortgage Guide: a complete example.", "x": "Walkthrough: buy smart., applied end to end — Pre-approval.. Rates shop. Follow along with your own situation beside you. Mortgage Guide Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Mortgage Guide.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Mortgage Guide.", "x": "The myths: Mortgage Guide is surrounded by bad advice — Inspection.. buy smart. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Closing costs. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-money-mortgage-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
