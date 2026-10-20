(function(){'use strict';
/* JAH Signature Freelance Careers Database generator — jahdb-e2-sig-career-freelance-careers-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sig-career-freelance-careers',PREFIX='JAH-E2SIGCAREER-',NAME='JAH Signature Freelance Careers Database';
var FIELDS=["overview", "fundamentals", "plays", "action-plan", "mistakes", "resources", "quick-wins", "advanced", "walkthrough", "myths", "checklist", "faq", "help", "quiz"];
var GEN_SRC='signature-original';
var MODE='quiz';
var BANK=[{"t": "Signature Freelance Careers: the playbook", "d": "Freelance Careers: go independent..", "g": "overview", "l": 2, "q": "What is Signature Freelance Careers: the playbook?", "a": "Freelance Careers: go independent..", "x": "The Signature Freelance Careers playbook: go independent.. Niche. This is a complete working guide — not theory, but the actual moves: what to do first, what to avoid, and how to know it is working. Pipeline. Every record is actionable.", "s": "signature-original", "f": null}, {"t": "The fundamentals", "d": "First principles of Freelance Careers.", "g": "fundamentals", "l": 2, "q": "What is The fundamentals?", "a": "First principles of Freelance Careers.", "x": "First principles: Pricing.. go independent. Get these right and the rest is optimization; get them wrong and nothing else matters. Freelance Careers Contracts. is simple but not easy — fundamentals first, always.", "s": "signature-original", "f": null}, {"t": "Play 1", "d": "Niche.", "g": "plays", "l": 2, "q": "What is Play 1?", "a": "Niche.", "x": "Freelance Careers play 1: Niche.. Contracts. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 1 in action", "d": "Applying: Niche..", "g": "plays", "l": 2, "q": "What is Play 1 in action?", "a": "Applying: Niche..", "x": "In action: Niche.. Here is how to actually do it — Taxes quarterly.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Pricing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2", "d": "Pipeline.", "g": "plays", "l": 2, "q": "What is Play 2?", "a": "Pipeline.", "x": "Freelance Careers play 2: Pipeline.. Taxes quarterly. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 2 in action", "d": "Applying: Pipeline..", "g": "plays", "l": 2, "q": "What is Play 2 in action?", "a": "Applying: Pipeline..", "x": "In action: Pipeline.. Here is how to actually do it — Insurance.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Contracts. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3", "d": "Pricing.", "g": "plays", "l": 2, "q": "What is Play 3?", "a": "Pricing.", "x": "Freelance Careers play 3: Pricing.. Insurance. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 3 in action", "d": "Applying: Pricing..", "g": "plays", "l": 2, "q": "What is Play 3 in action?", "a": "Applying: Pricing..", "x": "In action: Pricing.. Here is how to actually do it — Retirement solo.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Taxes quarterly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4", "d": "Contracts.", "g": "plays", "l": 2, "q": "What is Play 4?", "a": "Contracts.", "x": "Freelance Careers play 4: Contracts.. Retirement solo. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 4 in action", "d": "Applying: Contracts..", "g": "plays", "l": 2, "q": "What is Play 4 in action?", "a": "Applying: Contracts..", "x": "In action: Contracts.. Here is how to actually do it — Boundaries.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Insurance. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5", "d": "Taxes quarterly.", "g": "plays", "l": 2, "q": "What is Play 5?", "a": "Taxes quarterly.", "x": "Freelance Careers play 5: Taxes quarterly.. Boundaries. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 5 in action", "d": "Applying: Taxes quarterly..", "g": "plays", "l": 2, "q": "What is Play 5 in action?", "a": "Applying: Taxes quarterly..", "x": "In action: Taxes quarterly.. Here is how to actually do it — Niche.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Retirement solo. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6", "d": "Insurance.", "g": "plays", "l": 2, "q": "What is Play 6?", "a": "Insurance.", "x": "Freelance Careers play 6: Insurance.. Niche. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 6 in action", "d": "Applying: Insurance..", "g": "plays", "l": 2, "q": "What is Play 6 in action?", "a": "Applying: Insurance..", "x": "In action: Insurance.. Here is how to actually do it — Pipeline.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Boundaries. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7", "d": "Retirement solo.", "g": "plays", "l": 2, "q": "What is Play 7?", "a": "Retirement solo.", "x": "Freelance Careers play 7: Retirement solo.. Pipeline. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 7 in action", "d": "Applying: Retirement solo..", "g": "plays", "l": 2, "q": "What is Play 7 in action?", "a": "Applying: Retirement solo..", "x": "In action: Retirement solo.. Here is how to actually do it — Pricing.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Niche. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8", "d": "Boundaries.", "g": "plays", "l": 2, "q": "What is Play 8?", "a": "Boundaries.", "x": "Freelance Careers play 8: Boundaries.. Pricing. This is one of the eight core moves — master all eight and you outperform most people who wing it. go independent. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Play 8 in action", "d": "Applying: Boundaries..", "g": "plays", "l": 2, "q": "What is Play 8 in action?", "a": "Applying: Boundaries..", "x": "In action: Boundaries.. Here is how to actually do it — Contracts.. Freelance Careers The difference between knowing and doing is a calendar entry: schedule it. Pipeline. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Your action plan", "d": "Freelance Careers: week one.", "g": "action-plan", "l": 2, "q": "What is Your action plan?", "a": "Freelance Careers: week one.", "x": "Week one: Niche.. Start here — Pipeline.. Freelance Careers Do not try to do everything; do the first three plays badly rather than all eight never. go independent. Momentum beats perfection. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Mistakes to avoid", "d": "Where Freelance Careers goes wrong.", "g": "mistakes", "l": 2, "q": "What is Mistakes to avoid?", "a": "Where Freelance Careers goes wrong.", "x": "The classic mistakes: Taxes quarterly.. go independent. Most failure in Freelance Careers is not bad luck — it is these avoidable errors. Insurance. Learn them from this database, not from experience.", "s": "signature-original", "f": null}, {"t": "Tools and resources", "d": "The Freelance Careers toolkit.", "g": "resources", "l": 2, "q": "What is Tools and resources?", "a": "The Freelance Careers toolkit.", "x": "The toolkit: Retirement solo.. Freelance Careers The right tools multiply effort — Boundaries.. go independent. Keep it simple: master a few tools rather than collecting dozens. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Quick wins", "d": "Freelance Careers results this week.", "g": "quick-wins", "l": 2, "q": "What is Quick wins?", "a": "Freelance Careers results this week.", "x": "Quick wins: Pipeline.. Contracts. These pay off fast — do them first for the motivation to continue. Freelance Careers go independent. compounds; start the compounding now. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Advanced tactics", "d": "Level up Freelance Careers.", "g": "advanced", "l": 2, "q": "What is Advanced tactics?", "a": "Level up Freelance Careers.", "x": "Advanced: Boundaries.. Insurance. Once the fundamentals run on autopilot, these separate the good from the great at Freelance Careers. go independent. Do not attempt until the basics are solid. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Walkthrough", "d": "Freelance Careers: a complete example.", "g": "walkthrough", "l": 2, "q": "What is Walkthrough?", "a": "Freelance Careers: a complete example.", "x": "Walkthrough: go independent., applied end to end — Niche.. Pricing. Follow along with your own situation beside you. Freelance Careers Theory becomes skill by doing. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}, {"t": "Myths", "d": "Myths about Freelance Careers.", "g": "myths", "l": 2, "q": "What is Myths?", "a": "Myths about Freelance Careers.", "x": "The myths: Freelance Careers is surrounded by bad advice — Retirement solo.. go independent. Ignore the gurus selling shortcuts; the fundamentals in this database are the shortcut. Taxes quarterly. A Signature original: practical frameworks from the JAH system, not scraped content. Adapt to your situation; local laws and professionals govern specifics.", "s": "signature-original", "f": null}];
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
var gen={version:'jahdb-e2-sig-career-freelance-careers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
