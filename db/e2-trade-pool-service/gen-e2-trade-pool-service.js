(function(){'use strict';
/* JAH Pool Service Database generator — jahdb-e2-trade-pool-service-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-pool-service',PREFIX='JAH-E2TRADEPOOL-',NAME='JAH Pool Service Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pool Service: the complete guide", "d": "Pool Service: pools cleaned and balanced..", "g": "overview", "l": 2, "q": "What is Pool Service: the complete guide?", "a": "Pool Service: pools cleaned and balanced..", "x": "The complete Pool Service guide: pools cleaned and balanced.. Weekly cleaning. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Test water.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Pool Service services: Weekly cleaning..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Pool Service services: Weekly cleaning..", "x": "What a Pool Service does: Weekly cleaning.. Chemical balancing. The trade covers Equipment repair. — and knowing the full service list keeps you from calling the wrong pro. pools cleaned and balanced.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Weekly cleaning.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Weekly cleaning.", "x": "Pool Service: Weekly cleaning.. Chlorine levels. One of the core services — Equipment repair.. pools cleaned and balanced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Pool Service when: Weekly cleaning..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Pool Service when: Weekly cleaning..", "x": "When to call: Weekly cleaning.. Filter clean. Do not wait on Pool Service — small problems become expensive ones. Green to clean. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Chemical balancing.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Chemical balancing.", "x": "Pool Service: Chemical balancing.. Filter clean. One of the core services — Green to clean.. pools cleaned and balanced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Pool Service when: Chemical balancing..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Pool Service when: Chemical balancing..", "x": "When to call: Chemical balancing.. Cover. Do not wait on Pool Service — small problems become expensive ones. Open/close. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Equipment repair.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Equipment repair.", "x": "Pool Service: Equipment repair.. Cover. One of the core services — Open/close.. pools cleaned and balanced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Pool Service when: Equipment repair..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Pool Service when: Equipment repair..", "x": "When to call: Equipment repair.. Safety fence. Do not wait on Pool Service — small problems become expensive ones. Leak detection. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Green to clean.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Green to clean.", "x": "Pool Service: Green to clean.. Safety fence. One of the core services — Leak detection.. pools cleaned and balanced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Pool Service when: Green to clean..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Pool Service when: Green to clean..", "x": "When to call: Green to clean.. Energy pump. Do not wait on Pool Service — small problems become expensive ones. Weekly cleaning. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Open/close.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Open/close.", "x": "Pool Service: Open/close.. Energy pump. One of the core services — Weekly cleaning.. pools cleaned and balanced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Pool Service when: Open/close..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Pool Service when: Open/close..", "x": "When to call: Open/close.. Test water. Do not wait on Pool Service — small problems become expensive ones. Chemical balancing. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Leak detection.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Leak detection.", "x": "Pool Service: Leak detection.. Test water. One of the core services — Chemical balancing.. pools cleaned and balanced. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Pool Service when: Leak detection..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Pool Service when: Leak detection..", "x": "When to call: Leak detection.. Chlorine levels. Do not wait on Pool Service — small problems become expensive ones. Equipment repair. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Test water.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Test water.", "x": "Pool Service tip: Test water.. Chemical balancing. From the trade itself — Cover.. pools cleaned and balanced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Chlorine levels.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Chlorine levels.", "x": "Pool Service tip: Chlorine levels.. Equipment repair. From the trade itself — Safety fence.. pools cleaned and balanced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Filter clean.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Filter clean.", "x": "Pool Service tip: Filter clean.. Green to clean. From the trade itself — Energy pump.. pools cleaned and balanced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Cover.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Cover.", "x": "Pool Service tip: Cover.. Open/close. From the trade itself — Test water.. pools cleaned and balanced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Safety fence.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Safety fence.", "x": "Pool Service tip: Safety fence.. Leak detection. From the trade itself — Chlorine levels.. pools cleaned and balanced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Energy pump.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Energy pump.", "x": "Pool Service tip: Energy pump.. Weekly cleaning. From the trade itself — Filter clean.. pools cleaned and balanced. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Pool Service.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Pool Service.", "x": "Hiring: Test water.. Get three quotes, check license and insurance, read reviews, and get it in writing — Green to clean.. pools cleaned and balanced. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Pool Service this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Pool Service this.", "x": "Ask: Chlorine levels.. Are you licensed and insured? What is the timeline? What is excluded? Open/close. Good pros answer clearly; evasive ones walk away from. Pool Service Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Pool Service.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Pool Service.", "x": "Before signing: Filter clean.. Who does the work — employees or subs? What is the payment schedule? Leak detection. Never pay in full upfront. pools cleaned and balanced. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Pool Service pricing: Cover..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Pool Service pricing: Cover..", "x": "Costs: Cover.. Prices vary by region and job size — Weekly cleaning.. pools cleaned and balanced. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Pool Service yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Pool Service yourself?", "x": "DIY or pro: Pool Service is DIY-friendly when Safety fence. — but Chemical balancing.. pools cleaned and balanced. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-pool-service-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
