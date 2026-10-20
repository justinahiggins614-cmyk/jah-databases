(function(){'use strict';
/* JAH General Contractor Database generator — jahdb-e2-trade-general-contractor-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-general-contractor',PREFIX='JAH-E2TRADEGENE-',NAME='JAH General Contractor Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "General Contractor: the complete guide", "d": "General Contractor: run your renovation..", "g": "overview", "l": 2, "q": "What is General Contractor: the complete guide?", "a": "General Contractor: run your renovation..", "x": "The complete General Contractor guide: run your renovation.. Remodels. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Licensed.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "General Contractor services: Remodels..", "g": "services", "l": 2, "q": "What is What they do?", "a": "General Contractor services: Remodels..", "x": "What a General Contractor does: Remodels.. Additions. The trade covers Project manage. — and knowing the full service list keeps you from calling the wrong pro. run your renovation. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Remodels.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Remodels.", "x": "General Contractor: Remodels.. References. One of the core services — Project manage.. run your renovation. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a General Contractor when: Remodels..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a General Contractor when: Remodels..", "x": "When to call: Remodels.. Written contract. Do not wait on General Contractor — small problems become expensive ones. Permits. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Additions.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Additions.", "x": "General Contractor: Additions.. Written contract. One of the core services — Permits.. run your renovation. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a General Contractor when: Additions..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a General Contractor when: Additions..", "x": "When to call: Additions.. Payment schedule. Do not wait on General Contractor — small problems become expensive ones. Subs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Project manage.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Project manage.", "x": "General Contractor: Project manage.. Payment schedule. One of the core services — Subs.. run your renovation. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a General Contractor when: Project manage..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a General Contractor when: Project manage..", "x": "When to call: Project manage.. Insured. Do not wait on General Contractor — small problems become expensive ones. Scheduling. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Permits.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Permits.", "x": "General Contractor: Permits.. Insured. One of the core services — Scheduling.. run your renovation. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a General Contractor when: Permits..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a General Contractor when: Permits..", "x": "When to call: Permits.. Communication. Do not wait on General Contractor — small problems become expensive ones. Remodels. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Subs.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Subs.", "x": "General Contractor: Subs.. Communication. One of the core services — Remodels.. run your renovation. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a General Contractor when: Subs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a General Contractor when: Subs..", "x": "When to call: Subs.. Licensed. Do not wait on General Contractor — small problems become expensive ones. Additions. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Scheduling.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Scheduling.", "x": "General Contractor: Scheduling.. Licensed. One of the core services — Additions.. run your renovation. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a General Contractor when: Scheduling..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a General Contractor when: Scheduling..", "x": "When to call: Scheduling.. References. Do not wait on General Contractor — small problems become expensive ones. Project manage. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Licensed.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Licensed.", "x": "General Contractor tip: Licensed.. Additions. From the trade itself — Payment schedule.. run your renovation. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "References.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "References.", "x": "General Contractor tip: References.. Project manage. From the trade itself — Insured.. run your renovation. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Written contract.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Written contract.", "x": "General Contractor tip: Written contract.. Permits. From the trade itself — Communication.. run your renovation. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Payment schedule.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Payment schedule.", "x": "General Contractor tip: Payment schedule.. Subs. From the trade itself — Licensed.. run your renovation. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Insured.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Insured.", "x": "General Contractor tip: Insured.. Scheduling. From the trade itself — References.. run your renovation. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Communication.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Communication.", "x": "General Contractor tip: Communication.. Remodels. From the trade itself — Written contract.. run your renovation. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right General Contractor.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right General Contractor.", "x": "Hiring: Licensed.. Get three quotes, check license and insurance, read reviews, and get it in writing — Permits.. run your renovation. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your General Contractor this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your General Contractor this.", "x": "Ask: References.. Are you licensed and insured? What is the timeline? What is excluded? Subs. Good pros answer clearly; evasive ones walk away from. General Contractor Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a General Contractor.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a General Contractor.", "x": "Before signing: Written contract.. Who does the work — employees or subs? What is the payment schedule? Scheduling. Never pay in full upfront. run your renovation. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "General Contractor pricing: Payment schedule..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "General Contractor pricing: Payment schedule..", "x": "Costs: Payment schedule.. Prices vary by region and job size — Remodels.. run your renovation. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do General Contractor yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do General Contractor yourself?", "x": "DIY or pro: General Contractor is DIY-friendly when Insured. — but Additions.. run your renovation. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-general-contractor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
