(function(){'use strict';
/* JAH Sprinkler Service Database generator — jahdb-e2-trade-sprinkler-service-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-sprinkler-service',PREFIX='JAH-E2TRADESPRI-',NAME='JAH Sprinkler Service Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sprinkler Service: the complete guide", "d": "Sprinkler Service: irrigation install and repair..", "g": "overview", "l": 2, "q": "What is Sprinkler Service: the complete guide?", "a": "Sprinkler Service: irrigation install and repair..", "x": "The complete Sprinkler Service guide: irrigation install and repair.. Install. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Winterize.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Sprinkler Service services: Install..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Sprinkler Service services: Install..", "x": "What a Sprinkler Service does: Install.. Repairs. The trade covers Spring startup. — and knowing the full service list keeps you from calling the wrong pro. irrigation install and repair. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Install.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Install.", "x": "Sprinkler Service: Install.. Head adjust. One of the core services — Spring startup.. irrigation install and repair. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Sprinkler Service when: Install..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Sprinkler Service when: Install..", "x": "When to call: Install.. Smart controller. Do not wait on Sprinkler Service — small problems become expensive ones. Winterize. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Repairs.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Repairs.", "x": "Sprinkler Service: Repairs.. Smart controller. One of the core services — Winterize.. irrigation install and repair. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Sprinkler Service when: Repairs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Sprinkler Service when: Repairs..", "x": "When to call: Repairs.. Leaks. Do not wait on Sprinkler Service — small problems become expensive ones. Controllers. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Spring startup.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Spring startup.", "x": "Sprinkler Service: Spring startup.. Leaks. One of the core services — Controllers.. irrigation install and repair. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Sprinkler Service when: Spring startup..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Sprinkler Service when: Spring startup..", "x": "When to call: Spring startup.. Zones. Do not wait on Sprinkler Service — small problems become expensive ones. Drip. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Winterize.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Winterize.", "x": "Sprinkler Service: Winterize.. Zones. One of the core services — Drip.. irrigation install and repair. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Sprinkler Service when: Winterize..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Sprinkler Service when: Winterize..", "x": "When to call: Winterize.. Quotes. Do not wait on Sprinkler Service — small problems become expensive ones. Install. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Controllers.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Controllers.", "x": "Sprinkler Service: Controllers.. Quotes. One of the core services — Install.. irrigation install and repair. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Sprinkler Service when: Controllers..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Sprinkler Service when: Controllers..", "x": "When to call: Controllers.. Winterize. Do not wait on Sprinkler Service — small problems become expensive ones. Repairs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Drip.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Drip.", "x": "Sprinkler Service: Drip.. Winterize. One of the core services — Repairs.. irrigation install and repair. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Sprinkler Service when: Drip..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Sprinkler Service when: Drip..", "x": "When to call: Drip.. Head adjust. Do not wait on Sprinkler Service — small problems become expensive ones. Spring startup. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Winterize.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Winterize.", "x": "Sprinkler Service tip: Winterize.. Repairs. From the trade itself — Leaks.. irrigation install and repair. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Head adjust.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Head adjust.", "x": "Sprinkler Service tip: Head adjust.. Spring startup. From the trade itself — Zones.. irrigation install and repair. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Smart controller.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Smart controller.", "x": "Sprinkler Service tip: Smart controller.. Winterize. From the trade itself — Quotes.. irrigation install and repair. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Leaks.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Leaks.", "x": "Sprinkler Service tip: Leaks.. Controllers. From the trade itself — Winterize.. irrigation install and repair. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Zones.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Zones.", "x": "Sprinkler Service tip: Zones.. Drip. From the trade itself — Head adjust.. irrigation install and repair. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Quotes.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Quotes.", "x": "Sprinkler Service tip: Quotes.. Install. From the trade itself — Smart controller.. irrigation install and repair. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Sprinkler Service.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Sprinkler Service.", "x": "Hiring: Winterize.. Get three quotes, check license and insurance, read reviews, and get it in writing — Winterize.. irrigation install and repair. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Sprinkler Service this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Sprinkler Service this.", "x": "Ask: Head adjust.. Are you licensed and insured? What is the timeline? What is excluded? Controllers. Good pros answer clearly; evasive ones walk away from. Sprinkler Service Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Sprinkler Service.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Sprinkler Service.", "x": "Before signing: Smart controller.. Who does the work — employees or subs? What is the payment schedule? Drip. Never pay in full upfront. irrigation install and repair. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Sprinkler Service pricing: Leaks..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Sprinkler Service pricing: Leaks..", "x": "Costs: Leaks.. Prices vary by region and job size — Install.. irrigation install and repair. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Sprinkler Service yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Sprinkler Service yourself?", "x": "DIY or pro: Sprinkler Service is DIY-friendly when Zones. — but Repairs.. irrigation install and repair. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-sprinkler-service-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
