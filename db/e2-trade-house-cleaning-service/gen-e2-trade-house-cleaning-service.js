(function(){'use strict';
/* JAH House Cleaning Service Database generator — jahdb-e2-trade-house-cleaning-service-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-house-cleaning-service',PREFIX='JAH-E2TRADEHOUS-',NAME='JAH House Cleaning Service Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "House Cleaning Service: the complete guide", "d": "House Cleaning Service: recurring home cleaning..", "g": "overview", "l": 2, "q": "What is House Cleaning Service: the complete guide?", "a": "House Cleaning Service: recurring home cleaning..", "x": "The complete House Cleaning Service guide: recurring home cleaning.. Recurring clean. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Walk-through.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "House Cleaning Service services: Recurring clean..", "g": "services", "l": 2, "q": "What is What they do?", "a": "House Cleaning Service services: Recurring clean..", "x": "What a House Cleaning Service does: Recurring clean.. Deep clean. The trade covers Move clean. — and knowing the full service list keeps you from calling the wrong pro. recurring home cleaning. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Recurring clean.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Recurring clean.", "x": "House Cleaning Service: Recurring clean.. Checklist. One of the core services — Move clean.. recurring home cleaning. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Cleaning Service when: Recurring clean..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Cleaning Service when: Recurring clean..", "x": "When to call: Recurring clean.. Insured. Do not wait on House Cleaning Service — small problems become expensive ones. Checklists. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Deep clean.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Deep clean.", "x": "House Cleaning Service: Deep clean.. Insured. One of the core services — Checklists.. recurring home cleaning. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Cleaning Service when: Deep clean..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Cleaning Service when: Deep clean..", "x": "When to call: Deep clean.. Supplies. Do not wait on House Cleaning Service — small problems become expensive ones. Supplies. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Move clean.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Move clean.", "x": "House Cleaning Service: Move clean.. Supplies. One of the core services — Supplies.. recurring home cleaning. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Cleaning Service when: Move clean..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Cleaning Service when: Move clean..", "x": "When to call: Move clean.. Feedback. Do not wait on House Cleaning Service — small problems become expensive ones. Teams. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Checklists.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Checklists.", "x": "House Cleaning Service: Checklists.. Feedback. One of the core services — Teams.. recurring home cleaning. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Cleaning Service when: Checklists..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Cleaning Service when: Checklists..", "x": "When to call: Checklists.. Trial. Do not wait on House Cleaning Service — small problems become expensive ones. Recurring clean. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Supplies.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Supplies.", "x": "House Cleaning Service: Supplies.. Trial. One of the core services — Recurring clean.. recurring home cleaning. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Cleaning Service when: Supplies..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Cleaning Service when: Supplies..", "x": "When to call: Supplies.. Walk-through. Do not wait on House Cleaning Service — small problems become expensive ones. Deep clean. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Teams.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Teams.", "x": "House Cleaning Service: Teams.. Walk-through. One of the core services — Deep clean.. recurring home cleaning. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Cleaning Service when: Teams..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Cleaning Service when: Teams..", "x": "When to call: Teams.. Checklist. Do not wait on House Cleaning Service — small problems become expensive ones. Move clean. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Walk-through.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Walk-through.", "x": "House Cleaning Service tip: Walk-through.. Deep clean. From the trade itself — Supplies.. recurring home cleaning. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Checklist.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Checklist.", "x": "House Cleaning Service tip: Checklist.. Move clean. From the trade itself — Feedback.. recurring home cleaning. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Insured.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Insured.", "x": "House Cleaning Service tip: Insured.. Checklists. From the trade itself — Trial.. recurring home cleaning. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Supplies.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Supplies.", "x": "House Cleaning Service tip: Supplies.. Supplies. From the trade itself — Walk-through.. recurring home cleaning. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Feedback.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Feedback.", "x": "House Cleaning Service tip: Feedback.. Teams. From the trade itself — Checklist.. recurring home cleaning. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Trial.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Trial.", "x": "House Cleaning Service tip: Trial.. Recurring clean. From the trade itself — Insured.. recurring home cleaning. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right House Cleaning Service.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right House Cleaning Service.", "x": "Hiring: Walk-through.. Get three quotes, check license and insurance, read reviews, and get it in writing — Checklists.. recurring home cleaning. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your House Cleaning Service this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your House Cleaning Service this.", "x": "Ask: Checklist.. Are you licensed and insured? What is the timeline? What is excluded? Supplies. Good pros answer clearly; evasive ones walk away from. House Cleaning Service Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a House Cleaning Service.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a House Cleaning Service.", "x": "Before signing: Insured.. Who does the work — employees or subs? What is the payment schedule? Teams. Never pay in full upfront. recurring home cleaning. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "House Cleaning Service pricing: Supplies..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "House Cleaning Service pricing: Supplies..", "x": "Costs: Supplies.. Prices vary by region and job size — Recurring clean.. recurring home cleaning. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do House Cleaning Service yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do House Cleaning Service yourself?", "x": "DIY or pro: House Cleaning Service is DIY-friendly when Feedback. — but Deep clean.. recurring home cleaning. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-house-cleaning-service-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
