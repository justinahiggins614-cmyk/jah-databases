(function(){'use strict';
/* JAH Signature Special Needs Parenting Database generator — jahdb-e2-sig-parent-special-needs-parenting-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-special-needs-parenting',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Special Needs Parenting Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Special Needs Parenting: the playbook", "d": "Special Needs Parenting: advocate fiercely, love fully..", "g": "overview", "l": 2, "q": "What is Signature Special Needs Parenting: the playbook?", "a": "Special Needs Parenting: advocate fiercely, love fully..", "x": "The Signature Special Needs Parenting playbook: advocate fiercely, love fully.. Early intervention. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Learn IEP rights. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Special Needs Parenting.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Special Needs Parenting.", "x": "First principles: Support groups.. advocate fiercely, love fully. Get these right and the rest is optimization; get them wrong and nothing else matters. Special Needs Parenting Self-care. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Early intervention.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Early intervention.", "x": "Special Needs Parenting play 1: Early intervention.. Self-care. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Early intervention..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Early intervention..", "x": "In action: Early intervention.. Here is how to actually do it — Celebrate progress.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Support groups. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Learn IEP rights.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Learn IEP rights.", "x": "Special Needs Parenting play 2: Learn IEP rights.. Celebrate progress. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Learn IEP rights..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Learn IEP rights..", "x": "In action: Learn IEP rights.. Here is how to actually do it — Plan for future.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Self-care. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Support groups.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Support groups.", "x": "Special Needs Parenting play 3: Support groups.. Plan for future. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Support groups..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Support groups..", "x": "In action: Support groups.. Here is how to actually do it — Document everything.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Celebrate progress.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Self-care.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Self-care.", "x": "Special Needs Parenting play 4: Self-care.. Document everything. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Self-care..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Self-care..", "x": "In action: Self-care.. Here is how to actually do it — Find community.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Plan for future. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Celebrate progress.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Celebrate progress.", "x": "Special Needs Parenting play 5: Celebrate progress.. Find community. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Celebrate progress..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Celebrate progress..", "x": "In action: Celebrate progress.. Here is how to actually do it — Early intervention.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Document everything.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Plan for future.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Plan for future.", "x": "Special Needs Parenting play 6: Plan for future.. Early intervention. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Plan for future..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Plan for future..", "x": "In action: Plan for future.. Here is how to actually do it — Learn IEP rights.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Find community. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Document everything.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Document everything.", "x": "Special Needs Parenting play 7: Document everything.. Learn IEP rights. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Document everything..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Document everything..", "x": "In action: Document everything.. Here is how to actually do it — Support groups.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Early intervention.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Find community.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Find community.", "x": "Special Needs Parenting play 8: Find community.. Support groups. This is one of the eight core moves — master all eight and you outperform most people who wing it. advocate fiercely, love fully. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Find community..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Find community..", "x": "In action: Find community.. Here is how to actually do it — Self-care.. Special Needs Parenting The difference between knowing and doing is a calendar entry: schedule it. Learn IEP rights. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Special Needs Parenting: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Special Needs Parenting: week one.", "x": "Week one: Early intervention.. Start here — Learn IEP rights.. Special Needs Parenting Do not try to do everything; do the first three plays badly rather than all eight never. advocate fiercely, love fully. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Special Needs Parenting goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Special Needs Parenting goes wrong.", "x": "The classic mistakes: Celebrate progress.. advocate fiercely, love fully. Most failure in Special Needs Parenting is not bad luck — it is these avoidable errors. Plan for future. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Special Needs Parenting toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Special Needs Parenting toolkit.", "x": "The toolkit: Document everything.. Special Needs Parenting The right tools multiply effort — Find community.. advocate fiercely, love fully. Keep it simple: master a few tools rather than collecting dozens.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Special Needs Parenting results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Special Needs Parenting results this week.", "x": "Quick wins: Learn IEP rights.. Self-care. These pay off fast — do them first for the motivation to continue. Special Needs Parenting advocate fiercely, love fully. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Special Needs Parenting.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Special Needs Parenting.", "x": "Advanced: Find community.. Plan for future. Once the fundamentals run on autopilot, these separate the good from the great at Special Needs Parenting. advocate fiercely, love fully. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Special Needs Parenting: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Special Needs Parenting: a complete example.", "x": "Walkthrough: advocate fiercely, love fully., applied end to end — Early intervention.. Support groups. Follow along with your own situation beside you. Special Needs Parenting Theory becomes skill by doing.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Special Needs Parenting.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Special Needs Parenting.", "x": "The myths: Special Needs Parenting is surrounded by bad advice — Document everything.. advocate fiercely, love fully. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Celebrate progress.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-special-needs-parenting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
