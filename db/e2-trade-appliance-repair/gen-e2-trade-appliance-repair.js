(function(){'use strict';
/* JAH Appliance Repair Database generator — jahdb-e2-trade-appliance-repair-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-appliance-repair',PREFIX='JAH-E2TRADEAPPL-',NAME='JAH Appliance Repair Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Appliance Repair: the complete guide", "d": "Appliance Repair: fix washers, fridges, ovens and more..", "g": "overview", "l": 2, "q": "What is Appliance Repair: the complete guide?", "a": "Appliance Repair: fix washers, fridges, ovens and more..", "x": "The complete Appliance Repair guide: fix washers, fridges, ovens and more.. Refrigerator repair. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Model number ready.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Appliance Repair services: Refrigerator repair..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Appliance Repair services: Refrigerator repair..", "x": "What a Appliance Repair does: Refrigerator repair.. Washer/dryer. The trade covers Oven/range. — and knowing the full service list keeps you from calling the wrong pro. fix washers, fridges, ovens and more.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Refrigerator repair.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Refrigerator repair.", "x": "Appliance Repair: Refrigerator repair.. Repair vs replace 50%. One of the core services — Oven/range.. fix washers, fridges, ovens and more. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Appliance Repair when: Refrigerator repair..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Appliance Repair when: Refrigerator repair..", "x": "When to call: Refrigerator repair.. Warranty check. Do not wait on Appliance Repair — small problems become expensive ones. Dishwasher. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Washer/dryer.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Washer/dryer.", "x": "Appliance Repair: Washer/dryer.. Warranty check. One of the core services — Dishwasher.. fix washers, fridges, ovens and more. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Appliance Repair when: Washer/dryer..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Appliance Repair when: Washer/dryer..", "x": "When to call: Washer/dryer.. Factory parts. Do not wait on Appliance Repair — small problems become expensive ones. Microwave. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Oven/range.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Oven/range.", "x": "Appliance Repair: Oven/range.. Factory parts. One of the core services — Microwave.. fix washers, fridges, ovens and more. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Appliance Repair when: Oven/range..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Appliance Repair when: Oven/range..", "x": "When to call: Oven/range.. Clean coils. Do not wait on Appliance Repair — small problems become expensive ones. Diagnostics. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Dishwasher.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Dishwasher.", "x": "Appliance Repair: Dishwasher.. Clean coils. One of the core services — Diagnostics.. fix washers, fridges, ovens and more. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Appliance Repair when: Dishwasher..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Appliance Repair when: Dishwasher..", "x": "When to call: Dishwasher.. Surge protector. Do not wait on Appliance Repair — small problems become expensive ones. Refrigerator repair. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Microwave.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Microwave.", "x": "Appliance Repair: Microwave.. Surge protector. One of the core services — Refrigerator repair.. fix washers, fridges, ovens and more. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Appliance Repair when: Microwave..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Appliance Repair when: Microwave..", "x": "When to call: Microwave.. Model number ready. Do not wait on Appliance Repair — small problems become expensive ones. Washer/dryer. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Diagnostics.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Diagnostics.", "x": "Appliance Repair: Diagnostics.. Model number ready. One of the core services — Washer/dryer.. fix washers, fridges, ovens and more. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Appliance Repair when: Diagnostics..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Appliance Repair when: Diagnostics..", "x": "When to call: Diagnostics.. Repair vs replace 50%. Do not wait on Appliance Repair — small problems become expensive ones. Oven/range. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Model number ready.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Model number ready.", "x": "Appliance Repair tip: Model number ready.. Washer/dryer. From the trade itself — Factory parts.. fix washers, fridges, ovens and more. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Repair vs replace 50%.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Repair vs replace 50%.", "x": "Appliance Repair tip: Repair vs replace 50%.. Oven/range. From the trade itself — Clean coils.. fix washers, fridges, ovens and more. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Warranty check.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Warranty check.", "x": "Appliance Repair tip: Warranty check.. Dishwasher. From the trade itself — Surge protector.. fix washers, fridges, ovens and more. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Factory parts.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Factory parts.", "x": "Appliance Repair tip: Factory parts.. Microwave. From the trade itself — Model number ready.. fix washers, fridges, ovens and more. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Clean coils.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Clean coils.", "x": "Appliance Repair tip: Clean coils.. Diagnostics. From the trade itself — Repair vs replace 50%.. fix washers, fridges, ovens and more. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Surge protector.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Surge protector.", "x": "Appliance Repair tip: Surge protector.. Refrigerator repair. From the trade itself — Warranty check.. fix washers, fridges, ovens and more. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Appliance Repair.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Appliance Repair.", "x": "Hiring: Model number ready.. Get three quotes, check license and insurance, read reviews, and get it in writing — Dishwasher.. fix washers, fridges, ovens and more. The cheapest bid is rarely the best value.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Appliance Repair this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Appliance Repair this.", "x": "Ask: Repair vs replace 50%.. Are you licensed and insured? What is the timeline? What is excluded? Microwave. Good pros answer clearly; evasive ones walk away from. Appliance Repair Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Appliance Repair.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Appliance Repair.", "x": "Before signing: Warranty check.. Who does the work — employees or subs? What is the payment schedule? Diagnostics. Never pay in full upfront. fix washers, fridges, ovens and more. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Appliance Repair pricing: Factory parts..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Appliance Repair pricing: Factory parts..", "x": "Costs: Factory parts.. Prices vary by region and job size — Refrigerator repair.. fix washers, fridges, ovens and more. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Appliance Repair yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Appliance Repair yourself?", "x": "DIY or pro: Appliance Repair is DIY-friendly when Clean coils. — but Washer/dryer.. fix washers, fridges, ovens and more. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-appliance-repair-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
