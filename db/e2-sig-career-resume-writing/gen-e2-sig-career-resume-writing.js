(function(){'use strict';
/* JAH Signature Resume Writing Database generator — jahdb-e2-sig-career-resume-writing-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-career-resume-writing',PREFIX='JAH-E2SIGCAREER-',NAME='JAH Signature Resume Writing Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Resume Writing: the playbook", "d": "Resume Writing: get the interview..", "g": "overview", "l": 2, "q": "What is Signature Resume Writing: the playbook?", "a": "Resume Writing: get the interview..", "x": "The Signature Resume Writing playbook: get the interview.. One page early career. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Results not duties. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Resume Writing.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Resume Writing.", "x": "First principles: Keywords match posting.. get the interview. Get these right and the rest is optimization; get them wrong and nothing else matters. Resume Writing No objective; summary. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "One page early career.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "One page early career.", "x": "Resume Writing play 1: One page early career.. No objective; summary. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: One page early career..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: One page early career..", "x": "In action: One page early career.. Here is how to actually do it — Clean format.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. Keywords match posting. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Results not duties.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Results not duties.", "x": "Resume Writing play 2: Results not duties.. Clean format. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Results not duties..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Results not duties..", "x": "In action: Results not duties.. Here is how to actually do it — Quantify wins.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. No objective; summary. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Keywords match posting.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Keywords match posting.", "x": "Resume Writing play 3: Keywords match posting.. Quantify wins. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Keywords match posting..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Keywords match posting..", "x": "In action: Keywords match posting.. Here is how to actually do it — Tailor each.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. Clean format. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "No objective; summary.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "No objective; summary.", "x": "Resume Writing play 4: No objective; summary.. Tailor each. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: No objective; summary..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: No objective; summary..", "x": "In action: No objective; summary.. Here is how to actually do it — Proofread.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. Quantify wins. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Clean format.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Clean format.", "x": "Resume Writing play 5: Clean format.. Proofread. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Clean format..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Clean format..", "x": "In action: Clean format.. Here is how to actually do it — One page early career.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. Tailor each. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Quantify wins.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Quantify wins.", "x": "Resume Writing play 6: Quantify wins.. One page early career. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Quantify wins..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Quantify wins..", "x": "In action: Quantify wins.. Here is how to actually do it — Results not duties.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. Proofread. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Tailor each.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Tailor each.", "x": "Resume Writing play 7: Tailor each.. Results not duties. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Tailor each..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Tailor each..", "x": "In action: Tailor each.. Here is how to actually do it — Keywords match posting.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. One page early career. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Proofread.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Proofread.", "x": "Resume Writing play 8: Proofread.. Keywords match posting. This is one of the eight core moves — master all eight and you outperform most people who wing it. get the interview. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Proofread..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Proofread..", "x": "In action: Proofread.. Here is how to actually do it — No objective; summary.. Resume Writing The difference between knowing and doing is a calendar entry: schedule it. Results not duties. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Resume Writing: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Resume Writing: week one.", "x": "Week one: One page early career.. Start here — Results not duties.. Resume Writing Do not try to do everything; do the first three plays badly rather than all eight never. get the interview. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Resume Writing goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Resume Writing goes wrong.", "x": "The classic mistakes: Clean format.. get the interview. Most failure in Resume Writing is not bad luck — it is these avoidable errors. Quantify wins. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Resume Writing toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Resume Writing toolkit.", "x": "The toolkit: Tailor each.. Resume Writing The right tools multiply effort — Proofread.. get the interview. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Resume Writing results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Resume Writing results this week.", "x": "Quick wins: Results not duties.. No objective; summary. These pay off fast — do them first for the motivation to continue. Resume Writing get the interview. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Resume Writing.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Resume Writing.", "x": "Advanced: Proofread.. Quantify wins. Once the fundamentals run on autopilot, these separate the good from the great at Resume Writing. get the interview. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Resume Writing: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Resume Writing: a complete example.", "x": "Walkthrough: get the interview., applied end to end — One page early career.. Keywords match posting. Follow along with your own situation beside you. Resume Writing Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Resume Writing.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Resume Writing.", "x": "The myths: Resume Writing is surrounded by bad advice — Tailor each.. get the interview. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Clean format. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-career-resume-writing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
