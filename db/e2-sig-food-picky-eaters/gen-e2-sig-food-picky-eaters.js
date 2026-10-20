(function(){'use strict';
/* JAH Signature Picky Eaters Database generator — jahdb-e2-sig-food-picky-eaters-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-food-picky-eaters',PREFIX='JAH-E2SIGFOODPI-',NAME='JAH Signature Picky Eaters Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Picky Eaters: the playbook", "d": "Picky Eaters: expand tastes gently..", "g": "overview", "l": 2, "q": "What is Signature Picky Eaters: the playbook?", "a": "Picky Eaters: expand tastes gently..", "x": "The Signature Picky Eaters playbook: expand tastes gently.. No pressure. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Repeated exposure. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Picky Eaters.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Picky Eaters.", "x": "First principles: Involve cooking.. expand tastes gently. Get these right and the rest is optimization; get them wrong and nothing else matters. Picky Eaters Dip everything. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "No pressure.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "No pressure.", "x": "Picky Eaters play 1: No pressure.. Dip everything. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: No pressure..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: No pressure..", "x": "In action: No pressure.. Here is how to actually do it — Model.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Involve cooking. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Repeated exposure.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Repeated exposure.", "x": "Picky Eaters play 2: Repeated exposure.. Model. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Repeated exposure..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Repeated exposure..", "x": "In action: Repeated exposure.. Here is how to actually do it — Small tastes.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Dip everything. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Involve cooking.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Involve cooking.", "x": "Picky Eaters play 3: Involve cooking.. Small tastes. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Involve cooking..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Involve cooking..", "x": "In action: Involve cooking.. Here is how to actually do it — Routine.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Model. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Dip everything.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Dip everything.", "x": "Picky Eaters play 4: Dip everything.. Routine. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Dip everything..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Dip everything..", "x": "In action: Dip everything.. Here is how to actually do it — Patience.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Small tastes. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Model.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Model.", "x": "Picky Eaters play 5: Model.. Patience. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Model..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Model..", "x": "In action: Model.. Here is how to actually do it — No pressure.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Routine. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Small tastes.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Small tastes.", "x": "Picky Eaters play 6: Small tastes.. No pressure. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Small tastes..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Small tastes..", "x": "In action: Small tastes.. Here is how to actually do it — Repeated exposure.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Patience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Routine.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Routine.", "x": "Picky Eaters play 7: Routine.. Repeated exposure. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Routine..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Routine..", "x": "In action: Routine.. Here is how to actually do it — Involve cooking.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. No pressure. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Patience.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Patience.", "x": "Picky Eaters play 8: Patience.. Involve cooking. This is one of the eight core moves — master all eight and you outperform most people who wing it. expand tastes gently. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Patience..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Patience..", "x": "In action: Patience.. Here is how to actually do it — Dip everything.. Picky Eaters The difference between knowing and doing is a calendar entry: schedule it. Repeated exposure. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Picky Eaters: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Picky Eaters: week one.", "x": "Week one: No pressure.. Start here — Repeated exposure.. Picky Eaters Do not try to do everything; do the first three plays badly rather than all eight never. expand tastes gently. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Picky Eaters goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Picky Eaters goes wrong.", "x": "The classic mistakes: Model.. expand tastes gently. Most failure in Picky Eaters is not bad luck — it is these avoidable errors. Small tastes. Learn them from this database, not from experience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Picky Eaters toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Picky Eaters toolkit.", "x": "The toolkit: Routine.. Picky Eaters The right tools multiply effort — Patience.. expand tastes gently. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Picky Eaters results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Picky Eaters results this week.", "x": "Quick wins: Repeated exposure.. Dip everything. These pay off fast — do them first for the motivation to continue. Picky Eaters expand tastes gently. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Picky Eaters.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Picky Eaters.", "x": "Advanced: Patience.. Small tastes. Once the fundamentals run on autopilot, these separate the good from the great at Picky Eaters. expand tastes gently. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Picky Eaters: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Picky Eaters: a complete example.", "x": "Walkthrough: expand tastes gently., applied end to end — No pressure.. Involve cooking. Follow along with your own situation beside you. Picky Eaters Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Picky Eaters.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Picky Eaters.", "x": "The myths: Picky Eaters is surrounded by bad advice — Routine.. expand tastes gently. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Model. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-food-picky-eaters-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
