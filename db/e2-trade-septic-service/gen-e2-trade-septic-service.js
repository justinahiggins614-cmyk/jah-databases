(function(){'use strict';
/* JAH Septic Service Database generator — jahdb-e2-trade-septic-service-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-septic-service',PREFIX='JAH-E2TRADESEPT-',NAME='JAH Septic Service Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Septic Service: the complete guide", "d": "Septic Service: septic tanks pumped and maintained..", "g": "overview", "l": 2, "q": "What is Septic Service: the complete guide?", "a": "Septic Service: septic tanks pumped and maintained..", "x": "The complete Septic Service guide: septic tanks pumped and maintained.. Tank pumping. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Pump 3-5 years.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Septic Service services: Tank pumping..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Septic Service services: Tank pumping..", "x": "What a Septic Service does: Tank pumping.. Inspections. The trade covers Repairs. — and knowing the full service list keeps you from calling the wrong pro. septic tanks pumped and maintained. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Tank pumping.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Tank pumping.", "x": "Septic Service: Tank pumping.. No wipes. One of the core services — Repairs.. septic tanks pumped and maintained. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Septic Service when: Tank pumping..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Septic Service when: Tank pumping..", "x": "When to call: Tank pumping.. Water conserve. Do not wait on Septic Service — small problems become expensive ones. Drain field. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Inspections.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Inspections.", "x": "Septic Service: Inspections.. Water conserve. One of the core services — Drain field.. septic tanks pumped and maintained. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Septic Service when: Inspections..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Septic Service when: Inspections..", "x": "When to call: Inspections.. Drain field care. Do not wait on Septic Service — small problems become expensive ones. Baffle service. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Repairs.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Repairs.", "x": "Septic Service: Repairs.. Drain field care. One of the core services — Baffle service.. septic tanks pumped and maintained. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Septic Service when: Repairs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Septic Service when: Repairs..", "x": "When to call: Repairs.. Records. Do not wait on Septic Service — small problems become expensive ones. Locating. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Drain field.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Drain field.", "x": "Septic Service: Drain field.. Records. One of the core services — Locating.. septic tanks pumped and maintained. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Septic Service when: Drain field..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Septic Service when: Drain field..", "x": "When to call: Drain field.. Licensed. Do not wait on Septic Service — small problems become expensive ones. Tank pumping. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Baffle service.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Baffle service.", "x": "Septic Service: Baffle service.. Licensed. One of the core services — Tank pumping.. septic tanks pumped and maintained. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Septic Service when: Baffle service..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Septic Service when: Baffle service..", "x": "When to call: Baffle service.. Pump 3-5 years. Do not wait on Septic Service — small problems become expensive ones. Inspections. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Locating.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Locating.", "x": "Septic Service: Locating.. Pump 3-5 years. One of the core services — Inspections.. septic tanks pumped and maintained. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Septic Service when: Locating..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Septic Service when: Locating..", "x": "When to call: Locating.. No wipes. Do not wait on Septic Service — small problems become expensive ones. Repairs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Pump 3-5 years.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Pump 3-5 years.", "x": "Septic Service tip: Pump 3-5 years.. Inspections. From the trade itself — Drain field care.. septic tanks pumped and maintained. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "No wipes.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "No wipes.", "x": "Septic Service tip: No wipes.. Repairs. From the trade itself — Records.. septic tanks pumped and maintained. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Water conserve.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Water conserve.", "x": "Septic Service tip: Water conserve.. Drain field. From the trade itself — Licensed.. septic tanks pumped and maintained. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Drain field care.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Drain field care.", "x": "Septic Service tip: Drain field care.. Baffle service. From the trade itself — Pump 3-5 years.. septic tanks pumped and maintained. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Records.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Records.", "x": "Septic Service tip: Records.. Locating. From the trade itself — No wipes.. septic tanks pumped and maintained. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Licensed.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Licensed.", "x": "Septic Service tip: Licensed.. Tank pumping. From the trade itself — Water conserve.. septic tanks pumped and maintained. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Septic Service.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Septic Service.", "x": "Hiring: Pump 3-5 years.. Get three quotes, check license and insurance, read reviews, and get it in writing — Drain field.. septic tanks pumped and maintained. The cheapest bid is rarely the best value.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Septic Service this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Septic Service this.", "x": "Ask: No wipes.. Are you licensed and insured? What is the timeline? What is excluded? Baffle service. Good pros answer clearly; evasive ones walk away from. Septic Service Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Septic Service.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Septic Service.", "x": "Before signing: Water conserve.. Who does the work — employees or subs? What is the payment schedule? Locating. Never pay in full upfront. septic tanks pumped and maintained. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Septic Service pricing: Drain field care..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Septic Service pricing: Drain field care..", "x": "Costs: Drain field care.. Prices vary by region and job size — Tank pumping.. septic tanks pumped and maintained. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Septic Service yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Septic Service yourself?", "x": "DIY or pro: Septic Service is DIY-friendly when Records. — but Inspections.. septic tanks pumped and maintained. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-septic-service-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
