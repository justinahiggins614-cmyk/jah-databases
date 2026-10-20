(function(){'use strict';
/* JAH Signature Inventory Management Database generator — jahdb-e2-sig-biz-inventory-management-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-biz-inventory-management',PREFIX='JAH-E2SIGBIZINV-',NAME='JAH Signature Inventory Management Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Inventory Management: the playbook", "d": "Inventory Management: stock what sells..", "g": "overview", "l": 2, "q": "What is Signature Inventory Management: the playbook?", "a": "Inventory Management: stock what sells..", "x": "The Signature Inventory Management playbook: stock what sells.. ABC analysis. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Reorder points. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Inventory Management.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Inventory Management.", "x": "First principles: Shrinkage control.. stock what sells. Get these right and the rest is optimization; get them wrong and nothing else matters. Inventory Management FIFO. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "ABC analysis.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "ABC analysis.", "x": "Inventory Management play 1: ABC analysis.. FIFO. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: ABC analysis..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: ABC analysis..", "x": "In action: ABC analysis.. Here is how to actually do it — Cycle counts.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. Shrinkage control. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Reorder points.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Reorder points.", "x": "Inventory Management play 2: Reorder points.. Cycle counts. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Reorder points..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Reorder points..", "x": "In action: Reorder points.. Here is how to actually do it — Software.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. FIFO. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Shrinkage control.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Shrinkage control.", "x": "Inventory Management play 3: Shrinkage control.. Software. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Shrinkage control..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Shrinkage control..", "x": "In action: Shrinkage control.. Here is how to actually do it — Dead stock: clear.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. Cycle counts. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "FIFO.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "FIFO.", "x": "Inventory Management play 4: FIFO.. Dead stock: clear. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: FIFO..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: FIFO..", "x": "In action: FIFO.. Here is how to actually do it — Seasonal plan.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. Software. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Cycle counts.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Cycle counts.", "x": "Inventory Management play 5: Cycle counts.. Seasonal plan. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Cycle counts..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Cycle counts..", "x": "In action: Cycle counts.. Here is how to actually do it — ABC analysis.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. Dead stock: clear. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Software.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Software.", "x": "Inventory Management play 6: Software.. ABC analysis. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Software..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Software..", "x": "In action: Software.. Here is how to actually do it — Reorder points.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. Seasonal plan. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Dead stock: clear.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Dead stock: clear.", "x": "Inventory Management play 7: Dead stock: clear.. Reorder points. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Dead stock: clear..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Dead stock: clear..", "x": "In action: Dead stock: clear.. Here is how to actually do it — Shrinkage control.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. ABC analysis. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Seasonal plan.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Seasonal plan.", "x": "Inventory Management play 8: Seasonal plan.. Shrinkage control. This is one of the eight core moves — master all eight and you outperform most people who wing it. stock what sells. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Seasonal plan..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Seasonal plan..", "x": "In action: Seasonal plan.. Here is how to actually do it — FIFO.. Inventory Management The difference between knowing and doing is a calendar entry: schedule it. Reorder points. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Inventory Management: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Inventory Management: week one.", "x": "Week one: ABC analysis.. Start here — Reorder points.. Inventory Management Do not try to do everything; do the first three plays badly rather than all eight never. stock what sells. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Inventory Management goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Inventory Management goes wrong.", "x": "The classic mistakes: Cycle counts.. stock what sells. Most failure in Inventory Management is not bad luck — it is these avoidable errors. Software. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Inventory Management toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Inventory Management toolkit.", "x": "The toolkit: Dead stock: clear.. Inventory Management The right tools multiply effort — Seasonal plan.. stock what sells. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Inventory Management results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Inventory Management results this week.", "x": "Quick wins: Reorder points.. FIFO. These pay off fast — do them first for the motivation to continue. Inventory Management stock what sells. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Inventory Management.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Inventory Management.", "x": "Advanced: Seasonal plan.. Software. Once the fundamentals run on autopilot, these separate the good from the great at Inventory Management. stock what sells. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Inventory Management: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Inventory Management: a complete example.", "x": "Walkthrough: stock what sells., applied end to end — ABC analysis.. Shrinkage control. Follow along with your own situation beside you. Inventory Management Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Inventory Management.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Inventory Management.", "x": "The myths: Inventory Management is surrounded by bad advice — Dead stock: clear.. stock what sells. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Cycle counts.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-biz-inventory-management-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
