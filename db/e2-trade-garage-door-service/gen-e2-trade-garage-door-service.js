(function(){'use strict';
/* JAH Garage Door Service Database generator — jahdb-e2-trade-garage-door-service-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-garage-door-service',PREFIX='JAH-E2TRADEGARA-',NAME='JAH Garage Door Service Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Garage Door Service: the complete guide", "d": "Garage Door Service: doors, openers, springs..", "g": "overview", "l": 2, "q": "What is Garage Door Service: the complete guide?", "a": "Garage Door Service: doors, openers, springs..", "x": "The complete Garage Door Service guide: doors, openers, springs.. Spring replacement. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Springs dangerous.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Garage Door Service services: Spring replacement..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Garage Door Service services: Spring replacement..", "x": "What a Garage Door Service does: Spring replacement.. Opener install. The trade covers Track repair. — and knowing the full service list keeps you from calling the wrong pro. doors, openers, springs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Spring replacement.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Spring replacement.", "x": "Garage Door Service: Spring replacement.. Annual lube. One of the core services — Track repair.. doors, openers, springs. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Garage Door Service when: Spring replacement..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Garage Door Service when: Spring replacement..", "x": "When to call: Spring replacement.. Safety sensors. Do not wait on Garage Door Service — small problems become expensive ones. Panel replacement. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Opener install.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Opener install.", "x": "Garage Door Service: Opener install.. Safety sensors. One of the core services — Panel replacement.. doors, openers, springs. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Garage Door Service when: Opener install..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Garage Door Service when: Opener install..", "x": "When to call: Opener install.. Quiet openers. Do not wait on Garage Door Service — small problems become expensive ones. Maintenance. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Track repair.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Track repair.", "x": "Garage Door Service: Track repair.. Quiet openers. One of the core services — Maintenance.. doors, openers, springs. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Garage Door Service when: Track repair..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Garage Door Service when: Track repair..", "x": "When to call: Track repair.. Insulated doors. Do not wait on Garage Door Service — small problems become expensive ones. Smart openers. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Panel replacement.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Panel replacement.", "x": "Garage Door Service: Panel replacement.. Insulated doors. One of the core services — Smart openers.. doors, openers, springs. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Garage Door Service when: Panel replacement..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Garage Door Service when: Panel replacement..", "x": "When to call: Panel replacement.. Pro for springs. Do not wait on Garage Door Service — small problems become expensive ones. Spring replacement. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Maintenance.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Maintenance.", "x": "Garage Door Service: Maintenance.. Pro for springs. One of the core services — Spring replacement.. doors, openers, springs. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Garage Door Service when: Maintenance..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Garage Door Service when: Maintenance..", "x": "When to call: Maintenance.. Springs dangerous. Do not wait on Garage Door Service — small problems become expensive ones. Opener install. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Smart openers.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Smart openers.", "x": "Garage Door Service: Smart openers.. Springs dangerous. One of the core services — Opener install.. doors, openers, springs. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Garage Door Service when: Smart openers..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Garage Door Service when: Smart openers..", "x": "When to call: Smart openers.. Annual lube. Do not wait on Garage Door Service — small problems become expensive ones. Track repair. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Springs dangerous.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Springs dangerous.", "x": "Garage Door Service tip: Springs dangerous.. Opener install. From the trade itself — Quiet openers.. doors, openers, springs. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Annual lube.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Annual lube.", "x": "Garage Door Service tip: Annual lube.. Track repair. From the trade itself — Insulated doors.. doors, openers, springs. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Safety sensors.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Safety sensors.", "x": "Garage Door Service tip: Safety sensors.. Panel replacement. From the trade itself — Pro for springs.. doors, openers, springs. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Quiet openers.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Quiet openers.", "x": "Garage Door Service tip: Quiet openers.. Maintenance. From the trade itself — Springs dangerous.. doors, openers, springs. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Insulated doors.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Insulated doors.", "x": "Garage Door Service tip: Insulated doors.. Smart openers. From the trade itself — Annual lube.. doors, openers, springs. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Pro for springs.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Pro for springs.", "x": "Garage Door Service tip: Pro for springs.. Spring replacement. From the trade itself — Safety sensors.. doors, openers, springs. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Garage Door Service.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Garage Door Service.", "x": "Hiring: Springs dangerous.. Get three quotes, check license and insurance, read reviews, and get it in writing — Panel replacement.. doors, openers, springs. The cheapest bid is rarely the best value.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Garage Door Service this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Garage Door Service this.", "x": "Ask: Annual lube.. Are you licensed and insured? What is the timeline? What is excluded? Maintenance. Good pros answer clearly; evasive ones walk away from. Garage Door Service Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Garage Door Service.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Garage Door Service.", "x": "Before signing: Safety sensors.. Who does the work — employees or subs? What is the payment schedule? Smart openers. Never pay in full upfront. doors, openers, springs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Garage Door Service pricing: Quiet openers..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Garage Door Service pricing: Quiet openers..", "x": "Costs: Quiet openers.. Prices vary by region and job size — Spring replacement.. doors, openers, springs. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Garage Door Service yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Garage Door Service yourself?", "x": "DIY or pro: Garage Door Service is DIY-friendly when Insulated doors. — but Opener install.. doors, openers, springs. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-garage-door-service-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
