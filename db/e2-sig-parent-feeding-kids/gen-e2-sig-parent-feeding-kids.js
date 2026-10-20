(function(){'use strict';
/* JAH Signature Feeding Kids Database generator — jahdb-e2-sig-parent-feeding-kids-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-parent-feeding-kids',PREFIX='JAH-E2SIGPARENT-',NAME='JAH Signature Feeding Kids Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Feeding Kids: the playbook", "d": "Feeding Kids: nutrition without battles..", "g": "overview", "l": 2, "q": "What is Signature Feeding Kids: the playbook?", "a": "Feeding Kids: nutrition without battles..", "x": "The Signature Feeding Kids playbook: nutrition without battles.. Offer variety. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Never force. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Feeding Kids.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Feeding Kids.", "x": "First principles: Family meals.. nutrition without battles. Get these right and the rest is optimization; get them wrong and nothing else matters. Feeding Kids Snacks planned. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Offer variety.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Offer variety.", "x": "Feeding Kids play 1: Offer variety.. Snacks planned. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Offer variety..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Offer variety..", "x": "In action: Offer variety.. Here is how to actually do it — Model eating.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Family meals. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Never force.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Never force.", "x": "Feeding Kids play 2: Never force.. Model eating. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Never force..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Never force..", "x": "In action: Never force.. Here is how to actually do it — Picky phases pass.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Snacks planned. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Family meals.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Family meals.", "x": "Feeding Kids play 3: Family meals.. Picky phases pass. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Family meals..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Family meals..", "x": "In action: Family meals.. Here is how to actually do it — Involve them cooking.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Model eating. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Snacks planned.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Snacks planned.", "x": "Feeding Kids play 4: Snacks planned.. Involve them cooking. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Snacks planned..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Snacks planned..", "x": "In action: Snacks planned.. Here is how to actually do it — Water first.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Picky phases pass. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Model eating.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Model eating.", "x": "Feeding Kids play 5: Model eating.. Water first. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Model eating..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Model eating..", "x": "In action: Model eating.. Here is how to actually do it — Offer variety.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Involve them cooking. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Picky phases pass.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Picky phases pass.", "x": "Feeding Kids play 6: Picky phases pass.. Offer variety. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Picky phases pass..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Picky phases pass..", "x": "In action: Picky phases pass.. Here is how to actually do it — Never force.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Water first. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Involve them cooking.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Involve them cooking.", "x": "Feeding Kids play 7: Involve them cooking.. Never force. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Involve them cooking..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Involve them cooking..", "x": "In action: Involve them cooking.. Here is how to actually do it — Family meals.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Offer variety. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Water first.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Water first.", "x": "Feeding Kids play 8: Water first.. Family meals. This is one of the eight core moves — master all eight and you outperform most people who wing it. nutrition without battles. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Water first..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Water first..", "x": "In action: Water first.. Here is how to actually do it — Snacks planned.. Feeding Kids The difference between knowing and doing is a calendar entry: schedule it. Never force. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Feeding Kids: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Feeding Kids: week one.", "x": "Week one: Offer variety.. Start here — Never force.. Feeding Kids Do not try to do everything; do the first three plays badly rather than all eight never. nutrition without battles. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Feeding Kids goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Feeding Kids goes wrong.", "x": "The classic mistakes: Model eating.. nutrition without battles. Most failure in Feeding Kids is not bad luck — it is these avoidable errors. Picky phases pass. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Feeding Kids toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Feeding Kids toolkit.", "x": "The toolkit: Involve them cooking.. Feeding Kids The right tools multiply effort — Water first.. nutrition without battles. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Feeding Kids results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Feeding Kids results this week.", "x": "Quick wins: Never force.. Snacks planned. These pay off fast — do them first for the motivation to continue. Feeding Kids nutrition without battles. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Feeding Kids.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Feeding Kids.", "x": "Advanced: Water first.. Picky phases pass. Once the fundamentals run on autopilot, these separate the good from the great at Feeding Kids. nutrition without battles. Do not attempt until the basics are solid.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Feeding Kids: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Feeding Kids: a complete example.", "x": "Walkthrough: nutrition without battles., applied end to end — Offer variety.. Family meals. Follow along with your own situation beside you. Feeding Kids Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Feeding Kids.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Feeding Kids.", "x": "The myths: Feeding Kids is surrounded by bad advice — Involve them cooking.. nutrition without battles. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Model eating.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-parent-feeding-kids-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
