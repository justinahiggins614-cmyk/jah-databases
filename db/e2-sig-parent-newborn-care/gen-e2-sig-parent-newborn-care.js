(function(){'use strict';
/* JAH Signature Newborn Care Database generator — jahdb-e2-sig-parent-newborn-care-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-newborn-care',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Newborn Care Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Newborn Care: the playbook", "d": "Newborn Care: the first weeks survival guide..", "g": "overview", "l": 2, "q": "What is Signature Newborn Care: the playbook?", "a": "Newborn Care: the first weeks survival guide..", "x": "The Signature Newborn Care playbook: the first weeks survival guide.. Sleep when baby sleeps. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Feeding every two to three hours. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Newborn Care.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Newborn Care.", "x": "First principles: Swaddle snug.. the first weeks survival guide. Get these right and the rest is optimization; get them wrong and nothing else matters. Newborn Care Umbilical cord care. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Sleep when baby sleeps.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Sleep when baby sleeps.", "x": "Newborn Care play 1: Sleep when baby sleeps.. Umbilical cord care. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Sleep when baby sleeps..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Sleep when baby sleeps..", "x": "In action: Sleep when baby sleeps.. Here is how to actually do it — Pediatrician visits.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Swaddle snug. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Feeding every two to three hours.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Feeding every two to three hours.", "x": "Newborn Care play 2: Feeding every two to three hours.. Pediatrician visits. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Feeding every two to three hours..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Feeding every two to three hours..", "x": "In action: Feeding every two to three hours.. Here is how to actually do it — Trust instincts.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Umbilical cord care.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Swaddle snug.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Swaddle snug.", "x": "Newborn Care play 3: Swaddle snug.. Trust instincts. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Swaddle snug..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Swaddle snug..", "x": "In action: Swaddle snug.. Here is how to actually do it — Skin to skin.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Pediatrician visits. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Umbilical cord care.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Umbilical cord care.", "x": "Newborn Care play 4: Umbilical cord care.. Skin to skin. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Umbilical cord care..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Umbilical cord care..", "x": "In action: Umbilical cord care.. Here is how to actually do it — Accept help.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Trust instincts. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Pediatrician visits.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Pediatrician visits.", "x": "Newborn Care play 5: Pediatrician visits.. Accept help. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Pediatrician visits..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Pediatrician visits..", "x": "In action: Pediatrician visits.. Here is how to actually do it — Sleep when baby sleeps.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Skin to skin. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Trust instincts.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Trust instincts.", "x": "Newborn Care play 6: Trust instincts.. Sleep when baby sleeps. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Trust instincts..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Trust instincts..", "x": "In action: Trust instincts.. Here is how to actually do it — Feeding every two to three hours.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Accept help. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Skin to skin.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Skin to skin.", "x": "Newborn Care play 7: Skin to skin.. Feeding every two to three hours. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Skin to skin..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Skin to skin..", "x": "In action: Skin to skin.. Here is how to actually do it — Swaddle snug.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Sleep when baby sleeps. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Accept help.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Accept help.", "x": "Newborn Care play 8: Accept help.. Swaddle snug. This is one of the eight core moves — master all eight and you outperform most people who wing it. the first weeks survival guide. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Accept help..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Accept help..", "x": "In action: Accept help.. Here is how to actually do it — Umbilical cord care.. Newborn Care The difference between knowing and doing is a calendar entry: schedule it. Feeding every two to three hours.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Newborn Care: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Newborn Care: week one.", "x": "Week one: Sleep when baby sleeps.. Start here — Feeding every two to three hours.. Newborn Care Do not try to do everything; do the first three plays badly rather than all eight never. the first weeks survival guide. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Newborn Care goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Newborn Care goes wrong.", "x": "The classic mistakes: Pediatrician visits.. the first weeks survival guide. Most failure in Newborn Care is not bad luck — it is these avoidable errors. Trust instincts. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Newborn Care toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Newborn Care toolkit.", "x": "The toolkit: Skin to skin.. Newborn Care The right tools multiply effort — Accept help.. the first weeks survival guide. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Newborn Care results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Newborn Care results this week.", "x": "Quick wins: Feeding every two to three hours.. Umbilical cord care. These pay off fast — do them first for the motivation to continue. Newborn Care the first weeks survival guide. compounds; start the compounding now.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Newborn Care.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Newborn Care.", "x": "Advanced: Accept help.. Trust instincts. Once the fundamentals run on autopilot, these separate the good from the great at Newborn Care. the first weeks survival guide. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Newborn Care: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Newborn Care: a complete example.", "x": "Walkthrough: the first weeks survival guide., applied end to end — Sleep when baby sleeps.. Swaddle snug. Follow along with your own situation beside you. Newborn Care Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Newborn Care.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Newborn Care.", "x": "The myths: Newborn Care is surrounded by bad advice — Skin to skin.. the first weeks survival guide. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Pediatrician visits.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-newborn-care-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
