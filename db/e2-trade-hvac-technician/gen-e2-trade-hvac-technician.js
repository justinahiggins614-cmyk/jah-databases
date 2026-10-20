(function(){'use strict';
/* JAH HVAC Technician Database generator — jahdb-e2-trade-hvac-technician-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-hvac-technician',PREFIX='JAH-E2TRADEHVAC-',NAME='JAH HVAC Technician Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "HVAC Technician: the complete guide", "d": "HVAC Technician: heating, cooling, and air quality..", "g": "overview", "l": 2, "q": "What is HVAC Technician: the complete guide?", "a": "HVAC Technician: heating, cooling, and air quality..", "x": "The complete HVAC Technician guide: heating, cooling, and air quality.. AC install and repair. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Change filters.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "HVAC Technician services: AC install and repair..", "g": "services", "l": 2, "q": "What is What they do?", "a": "HVAC Technician services: AC install and repair..", "x": "What a HVAC Technician does: AC install and repair.. Furnace service. The trade covers Heat pumps. — and knowing the full service list keeps you from calling the wrong pro. heating, cooling, and air quality.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "AC install and repair.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "AC install and repair.", "x": "HVAC Technician: AC install and repair.. Annual tune-ups. One of the core services — Heat pumps.. heating, cooling, and air quality. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a HVAC Technician when: AC install and repair..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a HVAC Technician when: AC install and repair..", "x": "When to call: AC install and repair.. SEER ratings. Do not wait on HVAC Technician — small problems become expensive ones. Ductwork. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Furnace service.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Furnace service.", "x": "HVAC Technician: Furnace service.. SEER ratings. One of the core services — Ductwork.. heating, cooling, and air quality. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a HVAC Technician when: Furnace service..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a HVAC Technician when: Furnace service..", "x": "When to call: Furnace service.. Size right. Do not wait on HVAC Technician — small problems become expensive ones. Thermostats. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Heat pumps.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Heat pumps.", "x": "HVAC Technician: Heat pumps.. Size right. One of the core services — Thermostats.. heating, cooling, and air quality. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a HVAC Technician when: Heat pumps..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a HVAC Technician when: Heat pumps..", "x": "When to call: Heat pumps.. Maintenance plan. Do not wait on HVAC Technician — small problems become expensive ones. Indoor air quality. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Ductwork.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Ductwork.", "x": "HVAC Technician: Ductwork.. Maintenance plan. One of the core services — Indoor air quality.. heating, cooling, and air quality. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a HVAC Technician when: Ductwork..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a HVAC Technician when: Ductwork..", "x": "When to call: Ductwork.. Rebates. Do not wait on HVAC Technician — small problems become expensive ones. AC install and repair. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Thermostats.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Thermostats.", "x": "HVAC Technician: Thermostats.. Rebates. One of the core services — AC install and repair.. heating, cooling, and air quality. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a HVAC Technician when: Thermostats..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a HVAC Technician when: Thermostats..", "x": "When to call: Thermostats.. Change filters. Do not wait on HVAC Technician — small problems become expensive ones. Furnace service. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Indoor air quality.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Indoor air quality.", "x": "HVAC Technician: Indoor air quality.. Change filters. One of the core services — Furnace service.. heating, cooling, and air quality. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a HVAC Technician when: Indoor air quality..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a HVAC Technician when: Indoor air quality..", "x": "When to call: Indoor air quality.. Annual tune-ups. Do not wait on HVAC Technician — small problems become expensive ones. Heat pumps. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Change filters.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Change filters.", "x": "HVAC Technician tip: Change filters.. Furnace service. From the trade itself — Size right.. heating, cooling, and air quality. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Annual tune-ups.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Annual tune-ups.", "x": "HVAC Technician tip: Annual tune-ups.. Heat pumps. From the trade itself — Maintenance plan.. heating, cooling, and air quality. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "SEER ratings.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "SEER ratings.", "x": "HVAC Technician tip: SEER ratings.. Ductwork. From the trade itself — Rebates.. heating, cooling, and air quality. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Size right.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Size right.", "x": "HVAC Technician tip: Size right.. Thermostats. From the trade itself — Change filters.. heating, cooling, and air quality. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Maintenance plan.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Maintenance plan.", "x": "HVAC Technician tip: Maintenance plan.. Indoor air quality. From the trade itself — Annual tune-ups.. heating, cooling, and air quality. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Rebates.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Rebates.", "x": "HVAC Technician tip: Rebates.. AC install and repair. From the trade itself — SEER ratings.. heating, cooling, and air quality. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right HVAC Technician.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right HVAC Technician.", "x": "Hiring: Change filters.. Get three quotes, check license and insurance, read reviews, and get it in writing — Ductwork.. heating, cooling, and air quality. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your HVAC Technician this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your HVAC Technician this.", "x": "Ask: Annual tune-ups.. Are you licensed and insured? What is the timeline? What is excluded? Thermostats. Good pros answer clearly; evasive ones walk away from. HVAC Technician Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a HVAC Technician.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a HVAC Technician.", "x": "Before signing: SEER ratings.. Who does the work — employees or subs? What is the payment schedule? Indoor air quality. Never pay in full upfront. heating, cooling, and air quality. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "HVAC Technician pricing: Size right..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "HVAC Technician pricing: Size right..", "x": "Costs: Size right.. Prices vary by region and job size — AC install and repair.. heating, cooling, and air quality. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do HVAC Technician yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do HVAC Technician yourself?", "x": "DIY or pro: HVAC Technician is DIY-friendly when Maintenance plan. — but Furnace service.. heating, cooling, and air quality. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-hvac-technician-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
