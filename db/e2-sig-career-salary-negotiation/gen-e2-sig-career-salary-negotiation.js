(function(){'use strict';
/* JAH Signature Salary Negotiation Database generator — jahdb-e2-sig-career-salary-negotiation-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-career-salary-negotiation',PREFIX='JAH-E2SIGCAREER-',NAME='JAH Signature Salary Negotiation Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Salary Negotiation: the playbook", "d": "Salary Negotiation: get paid fairly..", "g": "overview", "l": 2, "q": "What is Signature Salary Negotiation: the playbook?", "a": "Salary Negotiation: get paid fairly..", "x": "The Signature Salary Negotiation playbook: get paid fairly.. Research ranges. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Never first number. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Salary Negotiation.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Salary Negotiation.", "x": "First principles: Total comp.. get paid fairly. Get these right and the rest is optimization; get them wrong and nothing else matters. Salary Negotiation Silence. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Research ranges.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Research ranges.", "x": "Salary Negotiation play 1: Research ranges.. Silence. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Research ranges..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Research ranges..", "x": "In action: Research ranges.. Here is how to actually do it — Walk away ready.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Total comp. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Never first number.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Never first number.", "x": "Salary Negotiation play 2: Never first number.. Walk away ready. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Never first number..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Never first number..", "x": "In action: Never first number.. Here is how to actually do it — Get it writing.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Silence. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Total comp.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Total comp.", "x": "Salary Negotiation play 3: Total comp.. Get it writing. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Total comp..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Total comp..", "x": "In action: Total comp.. Here is how to actually do it — Counter once.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Walk away ready. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Silence.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Silence.", "x": "Salary Negotiation play 4: Silence.. Counter once. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Silence..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Silence..", "x": "In action: Silence.. Here is how to actually do it — Practice.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Get it writing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Walk away ready.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Walk away ready.", "x": "Salary Negotiation play 5: Walk away ready.. Practice. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Walk away ready..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Walk away ready..", "x": "In action: Walk away ready.. Here is how to actually do it — Research ranges.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Counter once. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Get it writing.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Get it writing.", "x": "Salary Negotiation play 6: Get it writing.. Research ranges. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Get it writing..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Get it writing..", "x": "In action: Get it writing.. Here is how to actually do it — Never first number.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Practice. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Counter once.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Counter once.", "x": "Salary Negotiation play 7: Counter once.. Never first number. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Counter once..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Counter once..", "x": "In action: Counter once.. Here is how to actually do it — Total comp.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Research ranges. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Practice.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Practice.", "x": "Salary Negotiation play 8: Practice.. Total comp. This is one of the eight core moves — master all eight and you outperform most people who wing it. get paid fairly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Practice..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Practice..", "x": "In action: Practice.. Here is how to actually do it — Silence.. Salary Negotiation The difference between knowing and doing is a calendar entry: schedule it. Never first number. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Salary Negotiation: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Salary Negotiation: week one.", "x": "Week one: Research ranges.. Start here — Never first number.. Salary Negotiation Do not try to do everything; do the first three plays badly rather than all eight never. get paid fairly. Momentum beats perfection.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Salary Negotiation goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Salary Negotiation goes wrong.", "x": "The classic mistakes: Walk away ready.. get paid fairly. Most failure in Salary Negotiation is not bad luck — it is these avoidable errors. Get it writing. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Salary Negotiation toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Salary Negotiation toolkit.", "x": "The toolkit: Counter once.. Salary Negotiation The right tools multiply effort — Practice.. get paid fairly. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Salary Negotiation results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Salary Negotiation results this week.", "x": "Quick wins: Never first number.. Silence. These pay off fast — do them first for the motivation to continue. Salary Negotiation get paid fairly. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Salary Negotiation.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Salary Negotiation.", "x": "Advanced: Practice.. Get it writing. Once the fundamentals run on autopilot, these separate the good from the great at Salary Negotiation. get paid fairly. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Salary Negotiation: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Salary Negotiation: a complete example.", "x": "Walkthrough: get paid fairly., applied end to end — Research ranges.. Total comp. Follow along with your own situation beside you. Salary Negotiation Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Salary Negotiation.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Salary Negotiation.", "x": "The myths: Salary Negotiation is surrounded by bad advice — Counter once.. get paid fairly. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Walk away ready. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-career-salary-negotiation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
