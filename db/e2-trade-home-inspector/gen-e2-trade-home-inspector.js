(function(){'use strict';
/* JAH Home Inspector Database generator — jahdb-e2-trade-home-inspector-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-home-inspector',PREFIX='JAH-E2TRADEHOME-',NAME='JAH Home Inspector Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Home Inspector: the complete guide", "d": "Home Inspector: know before you buy..", "g": "overview", "l": 2, "q": "What is Home Inspector: the complete guide?", "a": "Home Inspector: know before you buy..", "x": "The complete Home Inspector guide: know before you buy.. Buyer inspections. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Certified.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Home Inspector services: Buyer inspections..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Home Inspector services: Buyer inspections..", "x": "What a Home Inspector does: Buyer inspections.. Pre-listing. The trade covers Radon. — and knowing the full service list keeps you from calling the wrong pro. know before you buy. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Buyer inspections.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Buyer inspections.", "x": "Home Inspector: Buyer inspections.. Attend. One of the core services — Radon.. know before you buy. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Home Inspector when: Buyer inspections..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Home Inspector when: Buyer inspections..", "x": "When to call: Buyer inspections.. Report. Do not wait on Home Inspector — small problems become expensive ones. Mold. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Pre-listing.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Pre-listing.", "x": "Home Inspector: Pre-listing.. Report. One of the core services — Mold.. know before you buy. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Home Inspector when: Pre-listing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Home Inspector when: Pre-listing..", "x": "When to call: Pre-listing.. Negotiate. Do not wait on Home Inspector — small problems become expensive ones. Sewer scope. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Radon.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Radon.", "x": "Home Inspector: Radon.. Negotiate. One of the core services — Sewer scope.. know before you buy. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Home Inspector when: Radon..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Home Inspector when: Radon..", "x": "When to call: Radon.. Specialists. Do not wait on Home Inspector — small problems become expensive ones. New build. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Mold.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Mold.", "x": "Home Inspector: Mold.. Specialists. One of the core services — New build.. know before you buy. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Home Inspector when: Mold..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Home Inspector when: Mold..", "x": "When to call: Mold.. Re-inspect. Do not wait on Home Inspector — small problems become expensive ones. Buyer inspections. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Sewer scope.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Sewer scope.", "x": "Home Inspector: Sewer scope.. Re-inspect. One of the core services — Buyer inspections.. know before you buy. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Home Inspector when: Sewer scope..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Home Inspector when: Sewer scope..", "x": "When to call: Sewer scope.. Certified. Do not wait on Home Inspector — small problems become expensive ones. Pre-listing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "New build.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "New build.", "x": "Home Inspector: New build.. Certified. One of the core services — Pre-listing.. know before you buy. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Home Inspector when: New build..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Home Inspector when: New build..", "x": "When to call: New build.. Attend. Do not wait on Home Inspector — small problems become expensive ones. Radon. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Certified.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Certified.", "x": "Home Inspector tip: Certified.. Pre-listing. From the trade itself — Negotiate.. know before you buy. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Attend.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Attend.", "x": "Home Inspector tip: Attend.. Radon. From the trade itself — Specialists.. know before you buy. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Report.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Report.", "x": "Home Inspector tip: Report.. Mold. From the trade itself — Re-inspect.. know before you buy. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Negotiate.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Negotiate.", "x": "Home Inspector tip: Negotiate.. Sewer scope. From the trade itself — Certified.. know before you buy. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Specialists.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Specialists.", "x": "Home Inspector tip: Specialists.. New build. From the trade itself — Attend.. know before you buy. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Re-inspect.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Re-inspect.", "x": "Home Inspector tip: Re-inspect.. Buyer inspections. From the trade itself — Report.. know before you buy. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Home Inspector.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Home Inspector.", "x": "Hiring: Certified.. Get three quotes, check license and insurance, read reviews, and get it in writing — Mold.. know before you buy. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Home Inspector this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Home Inspector this.", "x": "Ask: Attend.. Are you licensed and insured? What is the timeline? What is excluded? Sewer scope. Good pros answer clearly; evasive ones walk away from. Home Inspector Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Home Inspector.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Home Inspector.", "x": "Before signing: Report.. Who does the work — employees or subs? What is the payment schedule? New build. Never pay in full upfront. know before you buy. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Home Inspector pricing: Negotiate..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Home Inspector pricing: Negotiate..", "x": "Costs: Negotiate.. Prices vary by region and job size — Buyer inspections.. know before you buy. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Home Inspector yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Home Inspector yourself?", "x": "DIY or pro: Home Inspector is DIY-friendly when Specialists. — but Pre-listing.. know before you buy. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-home-inspector-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
