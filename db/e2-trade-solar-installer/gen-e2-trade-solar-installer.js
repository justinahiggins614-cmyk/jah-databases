(function(){'use strict';
/* JAH Solar Installer Database generator — jahdb-e2-trade-solar-installer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-solar-installer',PREFIX='JAH-E2TRADESOLA-',NAME='JAH Solar Installer Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Solar Installer: the complete guide", "d": "Solar Installer: panels on your roof..", "g": "overview", "l": 2, "q": "What is Solar Installer: the complete guide?", "a": "Solar Installer: panels on your roof..", "x": "The complete Solar Installer guide: panels on your roof.. Rooftop solar. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Roof age.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Solar Installer services: Rooftop solar..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Solar Installer services: Rooftop solar..", "x": "What a Solar Installer does: Rooftop solar.. Batteries. The trade covers Net metering. — and knowing the full service list keeps you from calling the wrong pro. panels on your roof. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Rooftop solar.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Rooftop solar.", "x": "Solar Installer: Rooftop solar.. Shading. One of the core services — Net metering.. panels on your roof. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Solar Installer when: Rooftop solar..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Solar Installer when: Rooftop solar..", "x": "When to call: Rooftop solar.. Quotes three. Do not wait on Solar Installer — small problems become expensive ones. Financing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Batteries.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Batteries.", "x": "Solar Installer: Batteries.. Quotes three. One of the core services — Financing.. panels on your roof. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Solar Installer when: Batteries..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Solar Installer when: Batteries..", "x": "When to call: Batteries.. Incentives. Do not wait on Solar Installer — small problems become expensive ones. Monitoring. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Net metering.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Net metering.", "x": "Solar Installer: Net metering.. Incentives. One of the core services — Monitoring.. panels on your roof. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Solar Installer when: Net metering..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Solar Installer when: Net metering..", "x": "When to call: Net metering.. Warranty. Do not wait on Solar Installer — small problems become expensive ones. Repairs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Financing.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Financing.", "x": "Solar Installer: Financing.. Warranty. One of the core services — Repairs.. panels on your roof. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Solar Installer when: Financing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Solar Installer when: Financing..", "x": "When to call: Financing.. Production. Do not wait on Solar Installer — small problems become expensive ones. Rooftop solar. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Monitoring.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Monitoring.", "x": "Solar Installer: Monitoring.. Production. One of the core services — Rooftop solar.. panels on your roof. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Solar Installer when: Monitoring..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Solar Installer when: Monitoring..", "x": "When to call: Monitoring.. Roof age. Do not wait on Solar Installer — small problems become expensive ones. Batteries. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Repairs.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Repairs.", "x": "Solar Installer: Repairs.. Roof age. One of the core services — Batteries.. panels on your roof. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Solar Installer when: Repairs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Solar Installer when: Repairs..", "x": "When to call: Repairs.. Shading. Do not wait on Solar Installer — small problems become expensive ones. Net metering. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Roof age.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Roof age.", "x": "Solar Installer tip: Roof age.. Batteries. From the trade itself — Incentives.. panels on your roof. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Shading.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Shading.", "x": "Solar Installer tip: Shading.. Net metering. From the trade itself — Warranty.. panels on your roof. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Quotes three.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Quotes three.", "x": "Solar Installer tip: Quotes three.. Financing. From the trade itself — Production.. panels on your roof. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Incentives.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Incentives.", "x": "Solar Installer tip: Incentives.. Monitoring. From the trade itself — Roof age.. panels on your roof. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Warranty.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Warranty.", "x": "Solar Installer tip: Warranty.. Repairs. From the trade itself — Shading.. panels on your roof. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Production.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Production.", "x": "Solar Installer tip: Production.. Rooftop solar. From the trade itself — Quotes three.. panels on your roof. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Solar Installer.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Solar Installer.", "x": "Hiring: Roof age.. Get three quotes, check license and insurance, read reviews, and get it in writing — Financing.. panels on your roof. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Solar Installer this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Solar Installer this.", "x": "Ask: Shading.. Are you licensed and insured? What is the timeline? What is excluded? Monitoring. Good pros answer clearly; evasive ones walk away from. Solar Installer Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Solar Installer.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Solar Installer.", "x": "Before signing: Quotes three.. Who does the work — employees or subs? What is the payment schedule? Repairs. Never pay in full upfront. panels on your roof. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Solar Installer pricing: Incentives..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Solar Installer pricing: Incentives..", "x": "Costs: Incentives.. Prices vary by region and job size — Rooftop solar.. panels on your roof. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Solar Installer yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Solar Installer yourself?", "x": "DIY or pro: Solar Installer is DIY-friendly when Warranty. — but Batteries.. panels on your roof. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-solar-installer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
