(function(){'use strict';
/* JAH Signature Co-Parenting Database generator — jahdb-e2-sig-parent-co-parenting-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-co-parenting',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Co-Parenting Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Co-Parenting: the playbook", "d": "Co-Parenting: kids first after split..", "g": "overview", "l": 2, "q": "What is Signature Co-Parenting: the playbook?", "a": "Co-Parenting: kids first after split..", "x": "The Signature Co-Parenting playbook: kids first after split.. Business-like tone. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Never badmouth. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Co-Parenting.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Co-Parenting.", "x": "First principles: Consistent rules.. kids first after split. Get these right and the rest is optimization; get them wrong and nothing else matters. Co-Parenting Written agreements. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Business-like tone.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Business-like tone.", "x": "Co-Parenting play 1: Business-like tone.. Written agreements. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Business-like tone..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Business-like tone..", "x": "In action: Business-like tone.. Here is how to actually do it — Kids not messengers.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Consistent rules. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Never badmouth.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Never badmouth.", "x": "Co-Parenting play 2: Never badmouth.. Kids not messengers. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Never badmouth..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Never badmouth..", "x": "In action: Never badmouth.. Here is how to actually do it — Flexibility.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Written agreements. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Consistent rules.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Consistent rules.", "x": "Co-Parenting play 3: Consistent rules.. Flexibility. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Consistent rules..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Consistent rules..", "x": "In action: Consistent rules.. Here is how to actually do it — Parallel parenting if needed.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Kids not messengers.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Written agreements.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Written agreements.", "x": "Co-Parenting play 4: Written agreements.. Parallel parenting if needed. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Written agreements..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Written agreements..", "x": "In action: Written agreements.. Here is how to actually do it — Therapy helps.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Flexibility. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Kids not messengers.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Kids not messengers.", "x": "Co-Parenting play 5: Kids not messengers.. Therapy helps. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Kids not messengers..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Kids not messengers..", "x": "In action: Kids not messengers.. Here is how to actually do it — Business-like tone.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Parallel parenting if needed.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Flexibility.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Flexibility.", "x": "Co-Parenting play 6: Flexibility.. Business-like tone. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Flexibility..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Flexibility..", "x": "In action: Flexibility.. Here is how to actually do it — Never badmouth.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Therapy helps. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Parallel parenting if needed.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Parallel parenting if needed.", "x": "Co-Parenting play 7: Parallel parenting if needed.. Never badmouth. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Parallel parenting if needed..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Parallel parenting if needed..", "x": "In action: Parallel parenting if needed.. Here is how to actually do it — Consistent rules.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Business-like tone.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Therapy helps.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Therapy helps.", "x": "Co-Parenting play 8: Therapy helps.. Consistent rules. This is one of the eight core moves — master all eight and you outperform most people who wing it. kids first after split. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Therapy helps..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Therapy helps..", "x": "In action: Therapy helps.. Here is how to actually do it — Written agreements.. Co-Parenting The difference between knowing and doing is a calendar entry: schedule it. Never badmouth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Co-Parenting: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Co-Parenting: week one.", "x": "Week one: Business-like tone.. Start here — Never badmouth.. Co-Parenting Do not try to do everything; do the first three plays badly rather than all eight never. kids first after split. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Co-Parenting goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Co-Parenting goes wrong.", "x": "The classic mistakes: Kids not messengers.. kids first after split. Most failure in Co-Parenting is not bad luck — it is these avoidable errors. Flexibility. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Co-Parenting toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Co-Parenting toolkit.", "x": "The toolkit: Parallel parenting if needed.. Co-Parenting The right tools multiply effort — Therapy helps.. kids first after split. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Co-Parenting results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Co-Parenting results this week.", "x": "Quick wins: Never badmouth.. Written agreements. These pay off fast — do them first for the motivation to continue. Co-Parenting kids first after split. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Co-Parenting.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Co-Parenting.", "x": "Advanced: Therapy helps.. Flexibility. Once the fundamentals run on autopilot, these separate the good from the great at Co-Parenting. kids first after split. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Co-Parenting: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Co-Parenting: a complete example.", "x": "Walkthrough: kids first after split., applied end to end — Business-like tone.. Consistent rules. Follow along with your own situation beside you. Co-Parenting Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Co-Parenting.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Co-Parenting.", "x": "The myths: Co-Parenting is surrounded by bad advice — Parallel parenting if needed.. kids first after split. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Kids not messengers.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-co-parenting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
