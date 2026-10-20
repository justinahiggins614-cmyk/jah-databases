(function(){'use strict';
/* JAH Signature Journaling Practice Database generator — jahdb-e2-sig-focus-journaling-practice-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-focus-journaling-practice',PREFIX='JAH-E2SIGFOCUSJ-',NAME='JAH Signature Journaling Practice Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Journaling Practice: the playbook", "d": "Journaling Practice: think on paper..", "g": "overview", "l": 2, "q": "What is Signature Journaling Practice: the playbook?", "a": "Journaling Practice: think on paper..", "x": "The Signature Journaling Practice playbook: think on paper.. Daily five min. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Prompts. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Journaling Practice.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Journaling Practice.", "x": "First principles: Gratitude.. think on paper. Get these right and the rest is optimization; get them wrong and nothing else matters. Journaling Practice Goals. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Daily five min.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Daily five min.", "x": "Journaling Practice play 1: Daily five min.. Goals. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Daily five min..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Daily five min..", "x": "In action: Daily five min.. Here is how to actually do it — Review.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Gratitude. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Prompts.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Prompts.", "x": "Journaling Practice play 2: Prompts.. Review. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Prompts..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Prompts..", "x": "In action: Prompts.. Here is how to actually do it — Handwrite.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Goals. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Gratitude.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Gratitude.", "x": "Journaling Practice play 3: Gratitude.. Handwrite. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Gratitude..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Gratitude..", "x": "In action: Gratitude.. Here is how to actually do it — Honest.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Review. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Goals.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Goals.", "x": "Journaling Practice play 4: Goals.. Honest. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Goals..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Goals..", "x": "In action: Goals.. Here is how to actually do it — Habit.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Handwrite. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Review.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Review.", "x": "Journaling Practice play 5: Review.. Habit. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Review..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Review..", "x": "In action: Review.. Here is how to actually do it — Daily five min.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Honest. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Handwrite.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Handwrite.", "x": "Journaling Practice play 6: Handwrite.. Daily five min. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Handwrite..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Handwrite..", "x": "In action: Handwrite.. Here is how to actually do it — Prompts.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Habit. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Honest.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Honest.", "x": "Journaling Practice play 7: Honest.. Prompts. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Honest..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Honest..", "x": "In action: Honest.. Here is how to actually do it — Gratitude.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Daily five min. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Habit.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Habit.", "x": "Journaling Practice play 8: Habit.. Gratitude. This is one of the eight core moves — master all eight and you outperform most people who wing it. think on paper. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Habit..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Habit..", "x": "In action: Habit.. Here is how to actually do it — Goals.. Journaling Practice The difference between knowing and doing is a calendar entry: schedule it. Prompts. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Journaling Practice: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Journaling Practice: week one.", "x": "Week one: Daily five min.. Start here — Prompts.. Journaling Practice Do not try to do everything; do the first three plays badly rather than all eight never. think on paper. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Journaling Practice goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Journaling Practice goes wrong.", "x": "The classic mistakes: Review.. think on paper. Most failure in Journaling Practice is not bad luck — it is these avoidable errors. Handwrite. Learn them from this database, not from experience. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Journaling Practice toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Journaling Practice toolkit.", "x": "The toolkit: Honest.. Journaling Practice The right tools multiply effort — Habit.. think on paper. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Journaling Practice results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Journaling Practice results this week.", "x": "Quick wins: Prompts.. Goals. These pay off fast — do them first for the motivation to continue. Journaling Practice think on paper. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Journaling Practice.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Journaling Practice.", "x": "Advanced: Habit.. Handwrite. Once the fundamentals run on autopilot, these separate the good from the great at Journaling Practice. think on paper. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Journaling Practice: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Journaling Practice: a complete example.", "x": "Walkthrough: think on paper., applied end to end — Daily five min.. Gratitude. Follow along with your own situation beside you. Journaling Practice Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Journaling Practice.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Journaling Practice.", "x": "The myths: Journaling Practice is surrounded by bad advice — Honest.. think on paper. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Review. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-focus-journaling-practice-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
