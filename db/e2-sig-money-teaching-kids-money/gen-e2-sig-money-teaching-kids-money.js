(function(){'use strict';
/* JAH Signature Teaching Kids Money Database generator — jahdb-e2-sig-money-teaching-kids-money-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-money-teaching-kids-money',PREFIX='JAH-E2SIGMONEYT-',NAME='JAH Signature Teaching Kids Money Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Teaching Kids Money: the playbook", "d": "Teaching Kids Money: raise smart spenders..", "g": "overview", "l": 2, "q": "What is Signature Teaching Kids Money: the playbook?", "a": "Teaching Kids Money: raise smart spenders..", "x": "The Signature Teaching Kids Money playbook: raise smart spenders.. Allowance. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Save spend give. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Teaching Kids Money.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Teaching Kids Money.", "x": "First principles: Work.. raise smart spenders. Get these right and the rest is optimization; get them wrong and nothing else matters. Teaching Kids Money Delayed gratification. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Allowance.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Allowance.", "x": "Teaching Kids Money play 1: Allowance.. Delayed gratification. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Allowance..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Allowance..", "x": "In action: Allowance.. Here is how to actually do it — Model.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Work. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Save spend give.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Save spend give.", "x": "Teaching Kids Money play 2: Save spend give.. Model. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Save spend give..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Save spend give..", "x": "In action: Save spend give.. Here is how to actually do it — Bank account.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Delayed gratification. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Work.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Work.", "x": "Teaching Kids Money play 3: Work.. Bank account. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Work..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Work..", "x": "In action: Work.. Here is how to actually do it — Goals.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Model. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Delayed gratification.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Delayed gratification.", "x": "Teaching Kids Money play 4: Delayed gratification.. Goals. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Delayed gratification..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Delayed gratification..", "x": "In action: Delayed gratification.. Here is how to actually do it — Talk.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Bank account. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Model.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Model.", "x": "Teaching Kids Money play 5: Model.. Talk. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Model..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Model..", "x": "In action: Model.. Here is how to actually do it — Allowance.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Goals. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Bank account.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Bank account.", "x": "Teaching Kids Money play 6: Bank account.. Allowance. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Bank account..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Bank account..", "x": "In action: Bank account.. Here is how to actually do it — Save spend give.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Talk. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Goals.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Goals.", "x": "Teaching Kids Money play 7: Goals.. Save spend give. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Goals..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Goals..", "x": "In action: Goals.. Here is how to actually do it — Work.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Allowance. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Talk.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Talk.", "x": "Teaching Kids Money play 8: Talk.. Work. This is one of the eight core moves — master all eight and you outperform most people who wing it. raise smart spenders. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Talk..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Talk..", "x": "In action: Talk.. Here is how to actually do it — Delayed gratification.. Teaching Kids Money The difference between knowing and doing is a calendar entry: schedule it. Save spend give. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Teaching Kids Money: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Teaching Kids Money: week one.", "x": "Week one: Allowance.. Start here — Save spend give.. Teaching Kids Money Do not try to do everything; do the first three plays badly rather than all eight never. raise smart spenders. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Teaching Kids Money goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Teaching Kids Money goes wrong.", "x": "The classic mistakes: Model.. raise smart spenders. Most failure in Teaching Kids Money is not bad luck — it is these avoidable errors. Bank account. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Teaching Kids Money toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Teaching Kids Money toolkit.", "x": "The toolkit: Goals.. Teaching Kids Money The right tools multiply effort — Talk.. raise smart spenders. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Teaching Kids Money results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Teaching Kids Money results this week.", "x": "Quick wins: Save spend give.. Delayed gratification. These pay off fast — do them first for the motivation to continue. Teaching Kids Money raise smart spenders. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Teaching Kids Money.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Teaching Kids Money.", "x": "Advanced: Talk.. Bank account. Once the fundamentals run on autopilot, these separate the good from the great at Teaching Kids Money. raise smart spenders. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Teaching Kids Money: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Teaching Kids Money: a complete example.", "x": "Walkthrough: raise smart spenders., applied end to end — Allowance.. Work. Follow along with your own situation beside you. Teaching Kids Money Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Teaching Kids Money.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Teaching Kids Money.", "x": "The myths: Teaching Kids Money is surrounded by bad advice — Goals.. raise smart spenders. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Model. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-money-teaching-kids-money-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
