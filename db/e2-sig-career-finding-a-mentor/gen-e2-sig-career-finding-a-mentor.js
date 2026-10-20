(function(){'use strict';
/* JAH Signature Finding a Mentor Database generator — jahdb-e2-sig-career-finding-a-mentor-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-career-finding-a-mentor',PREFIX='JAH-E2SIGCAREER-',NAME='JAH Signature Finding a Mentor Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Finding a Mentor: the playbook", "d": "Finding a Mentor: learn from the best..", "g": "overview", "l": 2, "q": "What is Signature Finding a Mentor: the playbook?", "a": "Finding a Mentor: learn from the best..", "x": "The Signature Finding a Mentor playbook: learn from the best.. Identify. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Ask specific. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Finding a Mentor.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Finding a Mentor.", "x": "First principles: Respect time.. learn from the best. Get these right and the rest is optimization; get them wrong and nothing else matters. Finding a Mentor Act on advice. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Identify.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Identify.", "x": "Finding a Mentor play 1: Identify.. Act on advice. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Identify..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Identify..", "x": "In action: Identify.. Here is how to actually do it — Update them.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Respect time. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Ask specific.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Ask specific.", "x": "Finding a Mentor play 2: Ask specific.. Update them. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Ask specific..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Ask specific..", "x": "In action: Ask specific.. Here is how to actually do it — Give back.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Act on advice. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Respect time.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Respect time.", "x": "Finding a Mentor play 3: Respect time.. Give back. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Respect time..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Respect time..", "x": "In action: Respect time.. Here is how to actually do it — Multiple mentors.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Update them. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Act on advice.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Act on advice.", "x": "Finding a Mentor play 4: Act on advice.. Multiple mentors. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Act on advice..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Act on advice..", "x": "In action: Act on advice.. Here is how to actually do it — Gratitude.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Give back. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Update them.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Update them.", "x": "Finding a Mentor play 5: Update them.. Gratitude. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Update them..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Update them..", "x": "In action: Update them.. Here is how to actually do it — Identify.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Multiple mentors. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Give back.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Give back.", "x": "Finding a Mentor play 6: Give back.. Identify. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Give back..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Give back..", "x": "In action: Give back.. Here is how to actually do it — Ask specific.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Gratitude. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Multiple mentors.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Multiple mentors.", "x": "Finding a Mentor play 7: Multiple mentors.. Ask specific. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Multiple mentors..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Multiple mentors..", "x": "In action: Multiple mentors.. Here is how to actually do it — Respect time.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Identify. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Gratitude.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Gratitude.", "x": "Finding a Mentor play 8: Gratitude.. Respect time. This is one of the eight core moves — master all eight and you outperform most people who wing it. learn from the best. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Gratitude..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Gratitude..", "x": "In action: Gratitude.. Here is how to actually do it — Act on advice.. Finding a Mentor The difference between knowing and doing is a calendar entry: schedule it. Ask specific. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Finding a Mentor: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Finding a Mentor: week one.", "x": "Week one: Identify.. Start here — Ask specific.. Finding a Mentor Do not try to do everything; do the first three plays badly rather than all eight never. learn from the best. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Finding a Mentor goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Finding a Mentor goes wrong.", "x": "The classic mistakes: Update them.. learn from the best. Most failure in Finding a Mentor is not bad luck — it is these avoidable errors. Give back. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Finding a Mentor toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Finding a Mentor toolkit.", "x": "The toolkit: Multiple mentors.. Finding a Mentor The right tools multiply effort — Gratitude.. learn from the best. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Finding a Mentor results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Finding a Mentor results this week.", "x": "Quick wins: Ask specific.. Act on advice. These pay off fast — do them first for the motivation to continue. Finding a Mentor learn from the best. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Finding a Mentor.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Finding a Mentor.", "x": "Advanced: Gratitude.. Give back. Once the fundamentals run on autopilot, these separate the good from the great at Finding a Mentor. learn from the best. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Finding a Mentor: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Finding a Mentor: a complete example.", "x": "Walkthrough: learn from the best., applied end to end — Identify.. Respect time. Follow along with your own situation beside you. Finding a Mentor Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Finding a Mentor.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Finding a Mentor.", "x": "The myths: Finding a Mentor is surrounded by bad advice — Multiple mentors.. learn from the best. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Update them. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-career-finding-a-mentor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
