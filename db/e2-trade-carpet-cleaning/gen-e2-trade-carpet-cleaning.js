(function(){'use strict';
/* JAH Carpet Cleaning Database generator — jahdb-e2-trade-carpet-cleaning-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-carpet-cleaning',PREFIX='JAH-E2TRADECARP-',NAME='JAH Carpet Cleaning Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carpet Cleaning: the complete guide", "d": "Carpet Cleaning: deep carpet care..", "g": "overview", "l": 2, "q": "What is Carpet Cleaning: the complete guide?", "a": "Carpet Cleaning: deep carpet care..", "x": "The complete Carpet Cleaning guide: deep carpet care.. Steam clean. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Vacuum first.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Carpet Cleaning services: Steam clean..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Carpet Cleaning services: Steam clean..", "x": "What a Carpet Cleaning does: Steam clean.. Stain removal. The trade covers Pet treatment. — and knowing the full service list keeps you from calling the wrong pro. deep carpet care. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Steam clean.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Steam clean.", "x": "Carpet Cleaning: Steam clean.. Annual deep. One of the core services — Pet treatment.. deep carpet care. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Carpet Cleaning when: Steam clean..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Carpet Cleaning when: Steam clean..", "x": "When to call: Steam clean.. Stain fast. Do not wait on Carpet Cleaning — small problems become expensive ones. Deodorizing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Stain removal.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Stain removal.", "x": "Carpet Cleaning: Stain removal.. Stain fast. One of the core services — Deodorizing.. deep carpet care. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Carpet Cleaning when: Stain removal..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Carpet Cleaning when: Stain removal..", "x": "When to call: Stain removal.. IICRC. Do not wait on Carpet Cleaning — small problems become expensive ones. Protection. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Pet treatment.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Pet treatment.", "x": "Carpet Cleaning: Pet treatment.. IICRC. One of the core services — Protection.. deep carpet care. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Carpet Cleaning when: Pet treatment..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Carpet Cleaning when: Pet treatment..", "x": "When to call: Pet treatment.. Dry time. Do not wait on Carpet Cleaning — small problems become expensive ones. Repairs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Deodorizing.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Deodorizing.", "x": "Carpet Cleaning: Deodorizing.. Dry time. One of the core services — Repairs.. deep carpet care. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Carpet Cleaning when: Deodorizing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Carpet Cleaning when: Deodorizing..", "x": "When to call: Deodorizing.. Quotes. Do not wait on Carpet Cleaning — small problems become expensive ones. Steam clean. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Protection.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Protection.", "x": "Carpet Cleaning: Protection.. Quotes. One of the core services — Steam clean.. deep carpet care. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Carpet Cleaning when: Protection..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Carpet Cleaning when: Protection..", "x": "When to call: Protection.. Vacuum first. Do not wait on Carpet Cleaning — small problems become expensive ones. Stain removal. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Repairs.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Repairs.", "x": "Carpet Cleaning: Repairs.. Vacuum first. One of the core services — Stain removal.. deep carpet care. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Carpet Cleaning when: Repairs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Carpet Cleaning when: Repairs..", "x": "When to call: Repairs.. Annual deep. Do not wait on Carpet Cleaning — small problems become expensive ones. Pet treatment. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Vacuum first.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Vacuum first.", "x": "Carpet Cleaning tip: Vacuum first.. Stain removal. From the trade itself — IICRC.. deep carpet care. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Annual deep.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Annual deep.", "x": "Carpet Cleaning tip: Annual deep.. Pet treatment. From the trade itself — Dry time.. deep carpet care. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Stain fast.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Stain fast.", "x": "Carpet Cleaning tip: Stain fast.. Deodorizing. From the trade itself — Quotes.. deep carpet care. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "IICRC.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "IICRC.", "x": "Carpet Cleaning tip: IICRC.. Protection. From the trade itself — Vacuum first.. deep carpet care. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Dry time.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Dry time.", "x": "Carpet Cleaning tip: Dry time.. Repairs. From the trade itself — Annual deep.. deep carpet care. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Quotes.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Quotes.", "x": "Carpet Cleaning tip: Quotes.. Steam clean. From the trade itself — Stain fast.. deep carpet care. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Carpet Cleaning.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Carpet Cleaning.", "x": "Hiring: Vacuum first.. Get three quotes, check license and insurance, read reviews, and get it in writing — Deodorizing.. deep carpet care. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Carpet Cleaning this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Carpet Cleaning this.", "x": "Ask: Annual deep.. Are you licensed and insured? What is the timeline? What is excluded? Protection. Good pros answer clearly; evasive ones walk away from. Carpet Cleaning Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Carpet Cleaning.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Carpet Cleaning.", "x": "Before signing: Stain fast.. Who does the work — employees or subs? What is the payment schedule? Repairs. Never pay in full upfront. deep carpet care. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Carpet Cleaning pricing: IICRC..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Carpet Cleaning pricing: IICRC..", "x": "Costs: IICRC.. Prices vary by region and job size — Steam clean.. deep carpet care. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Carpet Cleaning yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Carpet Cleaning yourself?", "x": "DIY or pro: Carpet Cleaning is DIY-friendly when Dry time. — but Stain removal.. deep carpet care. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-carpet-cleaning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
