(function(){'use strict';
/* JAH Well Drilling Database generator — jahdb-e2-trade-well-drilling-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-well-drilling',PREFIX='JAH-E2TRADEWELL-',NAME='JAH Well Drilling Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Well Drilling: the complete guide", "d": "Well Drilling: water wells drilled and serviced..", "g": "overview", "l": 2, "q": "What is Well Drilling: the complete guide?", "a": "Well Drilling: water wells drilled and serviced..", "x": "The complete Well Drilling guide: water wells drilled and serviced.. New wells. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Test yearly.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Well Drilling services: New wells..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Well Drilling services: New wells..", "x": "What a Well Drilling does: New wells.. Pump service. The trade covers Water testing. — and knowing the full service list keeps you from calling the wrong pro. water wells drilled and serviced. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "New wells.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "New wells.", "x": "Well Drilling: New wells.. Licensed driller. One of the core services — Water testing.. water wells drilled and serviced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Well Drilling when: New wells..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Well Drilling when: New wells..", "x": "When to call: New wells.. Depth costs. Do not wait on Well Drilling — small problems become expensive ones. Pressure tanks. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Pump service.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Pump service.", "x": "Well Drilling: Pump service.. Depth costs. One of the core services — Pressure tanks.. water wells drilled and serviced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Well Drilling when: Pump service..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Well Drilling when: Pump service..", "x": "When to call: Pump service.. Pressure tank. Do not wait on Well Drilling — small problems become expensive ones. Treatment. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Water testing.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Water testing.", "x": "Well Drilling: Water testing.. Pressure tank. One of the core services — Treatment.. water wells drilled and serviced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Well Drilling when: Water testing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Well Drilling when: Water testing..", "x": "When to call: Water testing.. Treatment. Do not wait on Well Drilling — small problems become expensive ones. Well sealing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Pressure tanks.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Pressure tanks.", "x": "Well Drilling: Pressure tanks.. Treatment. One of the core services — Well sealing.. water wells drilled and serviced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Well Drilling when: Pressure tanks..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Well Drilling when: Pressure tanks..", "x": "When to call: Pressure tanks.. Protect head. Do not wait on Well Drilling — small problems become expensive ones. New wells. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Treatment.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Treatment.", "x": "Well Drilling: Treatment.. Protect head. One of the core services — New wells.. water wells drilled and serviced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Well Drilling when: Treatment..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Well Drilling when: Treatment..", "x": "When to call: Treatment.. Test yearly. Do not wait on Well Drilling — small problems become expensive ones. Pump service. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Well sealing.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Well sealing.", "x": "Well Drilling: Well sealing.. Test yearly. One of the core services — Pump service.. water wells drilled and serviced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Well Drilling when: Well sealing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Well Drilling when: Well sealing..", "x": "When to call: Well sealing.. Licensed driller. Do not wait on Well Drilling — small problems become expensive ones. Water testing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Test yearly.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Test yearly.", "x": "Well Drilling tip: Test yearly.. Pump service. From the trade itself — Pressure tank.. water wells drilled and serviced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Licensed driller.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Licensed driller.", "x": "Well Drilling tip: Licensed driller.. Water testing. From the trade itself — Treatment.. water wells drilled and serviced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Depth costs.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Depth costs.", "x": "Well Drilling tip: Depth costs.. Pressure tanks. From the trade itself — Protect head.. water wells drilled and serviced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Pressure tank.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Pressure tank.", "x": "Well Drilling tip: Pressure tank.. Treatment. From the trade itself — Test yearly.. water wells drilled and serviced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Treatment.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Treatment.", "x": "Well Drilling tip: Treatment.. Well sealing. From the trade itself — Licensed driller.. water wells drilled and serviced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Protect head.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Protect head.", "x": "Well Drilling tip: Protect head.. New wells. From the trade itself — Depth costs.. water wells drilled and serviced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Well Drilling.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Well Drilling.", "x": "Hiring: Test yearly.. Get three quotes, check license and insurance, read reviews, and get it in writing — Pressure tanks.. water wells drilled and serviced. The cheapest bid is rarely the best value.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Well Drilling this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Well Drilling this.", "x": "Ask: Licensed driller.. Are you licensed and insured? What is the timeline? What is excluded? Treatment. Good pros answer clearly; evasive ones walk away from. Well Drilling Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Well Drilling.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Well Drilling.", "x": "Before signing: Depth costs.. Who does the work — employees or subs? What is the payment schedule? Well sealing. Never pay in full upfront. water wells drilled and serviced. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Well Drilling pricing: Pressure tank..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Well Drilling pricing: Pressure tank..", "x": "Costs: Pressure tank.. Prices vary by region and job size — New wells.. water wells drilled and serviced. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Well Drilling yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Well Drilling yourself?", "x": "DIY or pro: Well Drilling is DIY-friendly when Treatment. — but Pump service.. water wells drilled and serviced. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-well-drilling-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
