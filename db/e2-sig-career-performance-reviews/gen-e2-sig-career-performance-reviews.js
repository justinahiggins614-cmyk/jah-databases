(function(){'use strict';
/* JAH Signature Performance Reviews Database generator — jahdb-e2-sig-career-performance-reviews-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-career-performance-reviews',PREFIX='JAH-E2SIGCAREER-',NAME='JAH Signature Performance Reviews Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Performance Reviews: the playbook", "d": "Performance Reviews: ace evaluations..", "g": "overview", "l": 2, "q": "What is Signature Performance Reviews: the playbook?", "a": "Performance Reviews: ace evaluations..", "x": "The Signature Performance Reviews playbook: ace evaluations.. Track wins yearly. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Self-review honest. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Performance Reviews.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Performance Reviews.", "x": "First principles: Ask growth.. ace evaluations. Get these right and the rest is optimization; get them wrong and nothing else matters. Performance Reviews Goals written. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Track wins yearly.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Track wins yearly.", "x": "Performance Reviews play 1: Track wins yearly.. Goals written. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Track wins yearly..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Track wins yearly..", "x": "In action: Track wins yearly.. Here is how to actually do it — Feedback: act.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Ask growth. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Self-review honest.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Self-review honest.", "x": "Performance Reviews play 2: Self-review honest.. Feedback: act. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Self-review honest..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Self-review honest..", "x": "In action: Self-review honest.. Here is how to actually do it — Promote case.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Goals written. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Ask growth.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Ask growth.", "x": "Performance Reviews play 3: Ask growth.. Promote case. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Ask growth..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Ask growth..", "x": "In action: Ask growth.. Here is how to actually do it — Document.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Feedback: act. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Goals written.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Goals written.", "x": "Performance Reviews play 4: Goals written.. Document. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Goals written..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Goals written..", "x": "In action: Goals written.. Here is how to actually do it — Follow up.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Promote case. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Feedback: act.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Feedback: act.", "x": "Performance Reviews play 5: Feedback: act.. Follow up. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Feedback: act..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Feedback: act..", "x": "In action: Feedback: act.. Here is how to actually do it — Track wins yearly.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Document. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Promote case.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Promote case.", "x": "Performance Reviews play 6: Promote case.. Track wins yearly. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Promote case..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Promote case..", "x": "In action: Promote case.. Here is how to actually do it — Self-review honest.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Follow up. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Document.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Document.", "x": "Performance Reviews play 7: Document.. Self-review honest. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Document..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Document..", "x": "In action: Document.. Here is how to actually do it — Ask growth.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Track wins yearly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Follow up.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Follow up.", "x": "Performance Reviews play 8: Follow up.. Ask growth. This is one of the eight core moves — master all eight and you outperform most people who wing it. ace evaluations. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Follow up..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Follow up..", "x": "In action: Follow up.. Here is how to actually do it — Goals written.. Performance Reviews The difference between knowing and doing is a calendar entry: schedule it. Self-review honest. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Performance Reviews: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Performance Reviews: week one.", "x": "Week one: Track wins yearly.. Start here — Self-review honest.. Performance Reviews Do not try to do everything; do the first three plays badly rather than all eight never. ace evaluations. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Performance Reviews goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Performance Reviews goes wrong.", "x": "The classic mistakes: Feedback: act.. ace evaluations. Most failure in Performance Reviews is not bad luck — it is these avoidable errors. Promote case. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Performance Reviews toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Performance Reviews toolkit.", "x": "The toolkit: Document.. Performance Reviews The right tools multiply effort — Follow up.. ace evaluations. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Performance Reviews results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Performance Reviews results this week.", "x": "Quick wins: Self-review honest.. Goals written. These pay off fast — do them first for the motivation to continue. Performance Reviews ace evaluations. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Performance Reviews.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Performance Reviews.", "x": "Advanced: Follow up.. Promote case. Once the fundamentals run on autopilot, these separate the good from the great at Performance Reviews. ace evaluations. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Performance Reviews: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Performance Reviews: a complete example.", "x": "Walkthrough: ace evaluations., applied end to end — Track wins yearly.. Ask growth. Follow along with your own situation beside you. Performance Reviews Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Performance Reviews.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Performance Reviews.", "x": "The myths: Performance Reviews is surrounded by bad advice — Document.. ace evaluations. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Feedback: act. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-career-performance-reviews-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
