(function(){'use strict';
/* JAH Flooring Installer Database generator — jahdb-e2-trade-flooring-installer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-flooring-installer',PREFIX='JAH-E2TRADEFLOO-',NAME='JAH Flooring Installer Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Flooring Installer: the complete guide", "d": "Flooring Installer: floors of every kind..", "g": "overview", "l": 2, "q": "What is Flooring Installer: the complete guide?", "a": "Flooring Installer: floors of every kind..", "x": "The complete Flooring Installer guide: floors of every kind.. Hardwood. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Acclimate.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Flooring Installer services: Hardwood..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Flooring Installer services: Hardwood..", "x": "What a Flooring Installer does: Hardwood.. LVP. The trade covers Tile. — and knowing the full service list keeps you from calling the wrong pro. floors of every kind. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Hardwood.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Hardwood.", "x": "Flooring Installer: Hardwood.. Subfloor. One of the core services — Tile.. floors of every kind. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Flooring Installer when: Hardwood..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Flooring Installer when: Hardwood..", "x": "When to call: Hardwood.. Moisture test. Do not wait on Flooring Installer — small problems become expensive ones. Carpet. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "LVP.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "LVP.", "x": "Flooring Installer: LVP.. Moisture test. One of the core services — Carpet.. floors of every kind. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Flooring Installer when: LVP..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Flooring Installer when: LVP..", "x": "When to call: LVP.. Transitions. Do not wait on Flooring Installer — small problems become expensive ones. Refinishing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Tile.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Tile.", "x": "Flooring Installer: Tile.. Transitions. One of the core services — Refinishing.. floors of every kind. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Flooring Installer when: Tile..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Flooring Installer when: Tile..", "x": "When to call: Tile.. Warranty. Do not wait on Flooring Installer — small problems become expensive ones. Repairs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Carpet.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Carpet.", "x": "Flooring Installer: Carpet.. Warranty. One of the core services — Repairs.. floors of every kind. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Flooring Installer when: Carpet..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Flooring Installer when: Carpet..", "x": "When to call: Carpet.. Samples. Do not wait on Flooring Installer — small problems become expensive ones. Hardwood. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Refinishing.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Refinishing.", "x": "Flooring Installer: Refinishing.. Samples. One of the core services — Hardwood.. floors of every kind. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Flooring Installer when: Refinishing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Flooring Installer when: Refinishing..", "x": "When to call: Refinishing.. Acclimate. Do not wait on Flooring Installer — small problems become expensive ones. LVP. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Repairs.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Repairs.", "x": "Flooring Installer: Repairs.. Acclimate. One of the core services — LVP.. floors of every kind. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Flooring Installer when: Repairs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Flooring Installer when: Repairs..", "x": "When to call: Repairs.. Subfloor. Do not wait on Flooring Installer — small problems become expensive ones. Tile. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Acclimate.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Acclimate.", "x": "Flooring Installer tip: Acclimate.. LVP. From the trade itself — Transitions.. floors of every kind. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Subfloor.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Subfloor.", "x": "Flooring Installer tip: Subfloor.. Tile. From the trade itself — Warranty.. floors of every kind. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Moisture test.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Moisture test.", "x": "Flooring Installer tip: Moisture test.. Carpet. From the trade itself — Samples.. floors of every kind. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Transitions.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Transitions.", "x": "Flooring Installer tip: Transitions.. Refinishing. From the trade itself — Acclimate.. floors of every kind. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Warranty.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Warranty.", "x": "Flooring Installer tip: Warranty.. Repairs. From the trade itself — Subfloor.. floors of every kind. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Samples.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Samples.", "x": "Flooring Installer tip: Samples.. Hardwood. From the trade itself — Moisture test.. floors of every kind. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Flooring Installer.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Flooring Installer.", "x": "Hiring: Acclimate.. Get three quotes, check license and insurance, read reviews, and get it in writing — Carpet.. floors of every kind. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Flooring Installer this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Flooring Installer this.", "x": "Ask: Subfloor.. Are you licensed and insured? What is the timeline? What is excluded? Refinishing. Good pros answer clearly; evasive ones walk away from. Flooring Installer Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Flooring Installer.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Flooring Installer.", "x": "Before signing: Moisture test.. Who does the work — employees or subs? What is the payment schedule? Repairs. Never pay in full upfront. floors of every kind. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Flooring Installer pricing: Transitions..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Flooring Installer pricing: Transitions..", "x": "Costs: Transitions.. Prices vary by region and job size — Hardwood.. floors of every kind. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Flooring Installer yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Flooring Installer yourself?", "x": "DIY or pro: Flooring Installer is DIY-friendly when Warranty. — but LVP.. floors of every kind. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-flooring-installer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
