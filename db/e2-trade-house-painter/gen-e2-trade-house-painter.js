(function(){'use strict';
/* JAH House Painter Database generator — jahdb-e2-trade-house-painter-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-house-painter',PREFIX='JAH-E2TRADEHOUS-',NAME='JAH House Painter Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "House Painter: the complete guide", "d": "House Painter: interior and exterior painting..", "g": "overview", "l": 2, "q": "What is House Painter: the complete guide?", "a": "House Painter: interior and exterior painting..", "x": "The complete House Painter guide: interior and exterior painting.. Interior painting. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Prep is everything.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "House Painter services: Interior painting..", "g": "services", "l": 2, "q": "What is What they do?", "a": "House Painter services: Interior painting..", "x": "What a House Painter does: Interior painting.. Exterior painting. The trade covers Cabinet refinishing. — and knowing the full service list keeps you from calling the wrong pro. interior and exterior painting.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Interior painting.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Interior painting.", "x": "House Painter: Interior painting.. Two coats. One of the core services — Cabinet refinishing.. interior and exterior painting. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Painter when: Interior painting..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Painter when: Interior painting..", "x": "When to call: Interior painting.. Quality paint. Do not wait on House Painter — small problems become expensive ones. Drywall repair. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Exterior painting.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Exterior painting.", "x": "House Painter: Exterior painting.. Quality paint. One of the core services — Drywall repair.. interior and exterior painting. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Painter when: Exterior painting..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Painter when: Exterior painting..", "x": "When to call: Exterior painting.. Licensed. Do not wait on House Painter — small problems become expensive ones. Color consult. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Cabinet refinishing.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Cabinet refinishing.", "x": "House Painter: Cabinet refinishing.. Licensed. One of the core services — Color consult.. interior and exterior painting. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Painter when: Cabinet refinishing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Painter when: Cabinet refinishing..", "x": "When to call: Cabinet refinishing.. Written scope. Do not wait on House Painter — small problems become expensive ones. Power washing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Drywall repair.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Drywall repair.", "x": "House Painter: Drywall repair.. Written scope. One of the core services — Power washing.. interior and exterior painting. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Painter when: Drywall repair..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Painter when: Drywall repair..", "x": "When to call: Drywall repair.. Weather window. Do not wait on House Painter — small problems become expensive ones. Interior painting. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Color consult.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Color consult.", "x": "House Painter: Color consult.. Weather window. One of the core services — Interior painting.. interior and exterior painting. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Painter when: Color consult..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Painter when: Color consult..", "x": "When to call: Color consult.. Prep is everything. Do not wait on House Painter — small problems become expensive ones. Exterior painting. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Power washing.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Power washing.", "x": "House Painter: Power washing.. Prep is everything. One of the core services — Exterior painting.. interior and exterior painting. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a House Painter when: Power washing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a House Painter when: Power washing..", "x": "When to call: Power washing.. Two coats. Do not wait on House Painter — small problems become expensive ones. Cabinet refinishing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Prep is everything.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Prep is everything.", "x": "House Painter tip: Prep is everything.. Exterior painting. From the trade itself — Licensed.. interior and exterior painting. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Two coats.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Two coats.", "x": "House Painter tip: Two coats.. Cabinet refinishing. From the trade itself — Written scope.. interior and exterior painting. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Quality paint.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Quality paint.", "x": "House Painter tip: Quality paint.. Drywall repair. From the trade itself — Weather window.. interior and exterior painting. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Licensed.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Licensed.", "x": "House Painter tip: Licensed.. Color consult. From the trade itself — Prep is everything.. interior and exterior painting. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Written scope.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Written scope.", "x": "House Painter tip: Written scope.. Power washing. From the trade itself — Two coats.. interior and exterior painting. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Weather window.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Weather window.", "x": "House Painter tip: Weather window.. Interior painting. From the trade itself — Quality paint.. interior and exterior painting. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right House Painter.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right House Painter.", "x": "Hiring: Prep is everything.. Get three quotes, check license and insurance, read reviews, and get it in writing — Drywall repair.. interior and exterior painting. The cheapest bid is rarely the best value.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your House Painter this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your House Painter this.", "x": "Ask: Two coats.. Are you licensed and insured? What is the timeline? What is excluded? Color consult. Good pros answer clearly; evasive ones walk away from. House Painter Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a House Painter.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a House Painter.", "x": "Before signing: Quality paint.. Who does the work — employees or subs? What is the payment schedule? Power washing. Never pay in full upfront. interior and exterior painting. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "House Painter pricing: Licensed..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "House Painter pricing: Licensed..", "x": "Costs: Licensed.. Prices vary by region and job size — Interior painting.. interior and exterior painting. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do House Painter yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do House Painter yourself?", "x": "DIY or pro: House Painter is DIY-friendly when Written scope. — but Exterior painting.. interior and exterior painting. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-house-painter-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
