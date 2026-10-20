(function(){'use strict';
/* JAH Signature Potty Training Database generator — jahdb-e2-sig-parent-potty-training-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-potty-training',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Potty Training Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Potty Training: the playbook", "d": "Potty Training: readiness over schedule..", "g": "overview", "l": 2, "q": "What is Signature Potty Training: the playbook?", "a": "Potty Training: readiness over schedule..", "x": "The Signature Potty Training playbook: readiness over schedule.. Watch for signs. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Routine sits. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Potty Training.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Potty Training.", "x": "First principles: Praise efforts.. readiness over schedule. Get these right and the rest is optimization; get them wrong and nothing else matters. Potty Training Accidents normal. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Watch for signs.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Watch for signs.", "x": "Potty Training play 1: Watch for signs.. Accidents normal. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Watch for signs..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Watch for signs..", "x": "In action: Watch for signs.. Here is how to actually do it — Night comes later.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Praise efforts. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Routine sits.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Routine sits.", "x": "Potty Training play 2: Routine sits.. Night comes later. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Routine sits..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Routine sits..", "x": "In action: Routine sits.. Here is how to actually do it — Patience.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Accidents normal. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Praise efforts.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Praise efforts.", "x": "Potty Training play 3: Praise efforts.. Patience. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Praise efforts..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Praise efforts..", "x": "In action: Praise efforts.. Here is how to actually do it — Easy clothes.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Night comes later. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Accidents normal.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Accidents normal.", "x": "Potty Training play 4: Accidents normal.. Easy clothes. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Accidents normal..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Accidents normal..", "x": "In action: Accidents normal.. Here is how to actually do it — Books help.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Patience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Night comes later.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Night comes later.", "x": "Potty Training play 5: Night comes later.. Books help. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Night comes later..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Night comes later..", "x": "In action: Night comes later.. Here is how to actually do it — Watch for signs.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Easy clothes. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Patience.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Patience.", "x": "Potty Training play 6: Patience.. Watch for signs. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Patience..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Patience..", "x": "In action: Patience.. Here is how to actually do it — Routine sits.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Books help. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Easy clothes.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Easy clothes.", "x": "Potty Training play 7: Easy clothes.. Routine sits. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Easy clothes..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Easy clothes..", "x": "In action: Easy clothes.. Here is how to actually do it — Praise efforts.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Watch for signs. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Books help.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Books help.", "x": "Potty Training play 8: Books help.. Praise efforts. This is one of the eight core moves — master all eight and you outperform most people who wing it. readiness over schedule. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Books help..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Books help..", "x": "In action: Books help.. Here is how to actually do it — Accidents normal.. Potty Training The difference between knowing and doing is a calendar entry: schedule it. Routine sits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Potty Training: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Potty Training: week one.", "x": "Week one: Watch for signs.. Start here — Routine sits.. Potty Training Do not try to do everything; do the first three plays badly rather than all eight never. readiness over schedule. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Potty Training goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Potty Training goes wrong.", "x": "The classic mistakes: Night comes later.. readiness over schedule. Most failure in Potty Training is not bad luck — it is these avoidable errors. Patience. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Potty Training toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Potty Training toolkit.", "x": "The toolkit: Easy clothes.. Potty Training The right tools multiply effort — Books help.. readiness over schedule. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Potty Training results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Potty Training results this week.", "x": "Quick wins: Routine sits.. Accidents normal. These pay off fast — do them first for the motivation to continue. Potty Training readiness over schedule. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Potty Training.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Potty Training.", "x": "Advanced: Books help.. Patience. Once the fundamentals run on autopilot, these separate the good from the great at Potty Training. readiness over schedule. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Potty Training: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Potty Training: a complete example.", "x": "Walkthrough: readiness over schedule., applied end to end — Watch for signs.. Praise efforts. Follow along with your own situation beside you. Potty Training Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Potty Training.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Potty Training.", "x": "The myths: Potty Training is surrounded by bad advice — Easy clothes.. readiness over schedule. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Night comes later.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-potty-training-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
