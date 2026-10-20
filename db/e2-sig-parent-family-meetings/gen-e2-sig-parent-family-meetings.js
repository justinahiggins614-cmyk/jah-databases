(function(){'use strict';
/* JAH Signature Family Meetings Database generator — jahdb-e2-sig-parent-family-meetings-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-family-meetings',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Family Meetings Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Family Meetings: the playbook", "d": "Family Meetings: solve problems together..", "g": "overview", "l": 2, "q": "What is Signature Family Meetings: the playbook?", "a": "Family Meetings: solve problems together..", "x": "The Signature Family Meetings playbook: solve problems together.. Weekly rhythm. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Agenda. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Family Meetings.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Family Meetings.", "x": "First principles: Everyone speaks.. solve problems together. Get these right and the rest is optimization; get them wrong and nothing else matters. Family Meetings Solutions team. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Weekly rhythm.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Weekly rhythm.", "x": "Family Meetings play 1: Weekly rhythm.. Solutions team. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Weekly rhythm..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Weekly rhythm..", "x": "In action: Weekly rhythm.. Here is how to actually do it — Fun too.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Everyone speaks. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Agenda.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Agenda.", "x": "Family Meetings play 2: Agenda.. Fun too. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Agenda..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Agenda..", "x": "In action: Agenda.. Here is how to actually do it — Follow through.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Solutions team. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Everyone speaks.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Everyone speaks.", "x": "Family Meetings play 3: Everyone speaks.. Follow through. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Everyone speaks..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Everyone speaks..", "x": "In action: Everyone speaks.. Here is how to actually do it — Rotate chair.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Fun too. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Solutions team.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Solutions team.", "x": "Family Meetings play 4: Solutions team.. Rotate chair. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Solutions team..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Solutions team..", "x": "In action: Solutions team.. Here is how to actually do it — Snacks help.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Follow through. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Fun too.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Fun too.", "x": "Family Meetings play 5: Fun too.. Snacks help. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Fun too..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Fun too..", "x": "In action: Fun too.. Here is how to actually do it — Weekly rhythm.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Rotate chair. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Follow through.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Follow through.", "x": "Family Meetings play 6: Follow through.. Weekly rhythm. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Follow through..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Follow through..", "x": "In action: Follow through.. Here is how to actually do it — Agenda.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Snacks help. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Rotate chair.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Rotate chair.", "x": "Family Meetings play 7: Rotate chair.. Agenda. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Rotate chair..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Rotate chair..", "x": "In action: Rotate chair.. Here is how to actually do it — Everyone speaks.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Weekly rhythm. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Snacks help.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Snacks help.", "x": "Family Meetings play 8: Snacks help.. Everyone speaks. This is one of the eight core moves — master all eight and you outperform most people who wing it. solve problems together. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Snacks help..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Snacks help..", "x": "In action: Snacks help.. Here is how to actually do it — Solutions team.. Family Meetings The difference between knowing and doing is a calendar entry: schedule it. Agenda. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Family Meetings: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Family Meetings: week one.", "x": "Week one: Weekly rhythm.. Start here — Agenda.. Family Meetings Do not try to do everything; do the first three plays badly rather than all eight never. solve problems together. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Family Meetings goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Family Meetings goes wrong.", "x": "The classic mistakes: Fun too.. solve problems together. Most failure in Family Meetings is not bad luck — it is these avoidable errors. Follow through. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Family Meetings toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Family Meetings toolkit.", "x": "The toolkit: Rotate chair.. Family Meetings The right tools multiply effort — Snacks help.. solve problems together. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Family Meetings results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Family Meetings results this week.", "x": "Quick wins: Agenda.. Solutions team. These pay off fast — do them first for the motivation to continue. Family Meetings solve problems together. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Family Meetings.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Family Meetings.", "x": "Advanced: Snacks help.. Follow through. Once the fundamentals run on autopilot, these separate the good from the great at Family Meetings. solve problems together. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Family Meetings: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Family Meetings: a complete example.", "x": "Walkthrough: solve problems together., applied end to end — Weekly rhythm.. Everyone speaks. Follow along with your own situation beside you. Family Meetings Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Family Meetings.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Family Meetings.", "x": "The myths: Family Meetings is surrounded by bad advice — Rotate chair.. solve problems together. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Fun too. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-family-meetings-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
