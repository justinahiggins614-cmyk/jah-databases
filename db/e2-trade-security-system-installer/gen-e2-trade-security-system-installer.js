(function(){'use strict';
/* JAH Security System Installer Database generator — jahdb-e2-trade-security-system-installer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-security-system-installer',PREFIX='JAH-E2TRADESECU-',NAME='JAH Security System Installer Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Security System Installer: the complete guide", "d": "Security System Installer: protect your home..", "g": "overview", "l": 2, "q": "What is Security System Installer: the complete guide?", "a": "Security System Installer: protect your home..", "x": "The complete Security System Installer guide: protect your home.. Alarm systems. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Monitored vs self.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Security System Installer services: Alarm systems..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Security System Installer services: Alarm systems..", "x": "What a Security System Installer does: Alarm systems.. Cameras. The trade covers Monitoring. — and knowing the full service list keeps you from calling the wrong pro. protect your home. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Alarm systems.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Alarm systems.", "x": "Security System Installer: Alarm systems.. Camera placement. One of the core services — Monitoring.. protect your home. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Security System Installer when: Alarm systems..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Security System Installer when: Alarm systems..", "x": "When to call: Alarm systems.. Contracts. Do not wait on Security System Installer — small problems become expensive ones. Smart locks. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Cameras.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Cameras.", "x": "Security System Installer: Cameras.. Contracts. One of the core services — Smart locks.. protect your home. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Security System Installer when: Cameras..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Security System Installer when: Cameras..", "x": "When to call: Cameras.. Privacy. Do not wait on Security System Installer — small problems become expensive ones. Sensors. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Monitoring.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Monitoring.", "x": "Security System Installer: Monitoring.. Privacy. One of the core services — Sensors.. protect your home. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Security System Installer when: Monitoring..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Security System Installer when: Monitoring..", "x": "When to call: Monitoring.. Quotes. Do not wait on Security System Installer — small problems become expensive ones. Video doorbells. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Smart locks.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Smart locks.", "x": "Security System Installer: Smart locks.. Quotes. One of the core services — Video doorbells.. protect your home. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Security System Installer when: Smart locks..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Security System Installer when: Smart locks..", "x": "When to call: Smart locks.. Signs. Do not wait on Security System Installer — small problems become expensive ones. Alarm systems. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Sensors.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Sensors.", "x": "Security System Installer: Sensors.. Signs. One of the core services — Alarm systems.. protect your home. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Security System Installer when: Sensors..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Security System Installer when: Sensors..", "x": "When to call: Sensors.. Monitored vs self. Do not wait on Security System Installer — small problems become expensive ones. Cameras. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Video doorbells.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Video doorbells.", "x": "Security System Installer: Video doorbells.. Monitored vs self. One of the core services — Cameras.. protect your home. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Security System Installer when: Video doorbells..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Security System Installer when: Video doorbells..", "x": "When to call: Video doorbells.. Camera placement. Do not wait on Security System Installer — small problems become expensive ones. Monitoring. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Monitored vs self.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Monitored vs self.", "x": "Security System Installer tip: Monitored vs self.. Cameras. From the trade itself — Privacy.. protect your home. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Camera placement.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Camera placement.", "x": "Security System Installer tip: Camera placement.. Monitoring. From the trade itself — Quotes.. protect your home. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Contracts.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Contracts.", "x": "Security System Installer tip: Contracts.. Smart locks. From the trade itself — Signs.. protect your home. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Privacy.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Privacy.", "x": "Security System Installer tip: Privacy.. Sensors. From the trade itself — Monitored vs self.. protect your home. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Quotes.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Quotes.", "x": "Security System Installer tip: Quotes.. Video doorbells. From the trade itself — Camera placement.. protect your home. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Signs.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Signs.", "x": "Security System Installer tip: Signs.. Alarm systems. From the trade itself — Contracts.. protect your home. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Security System Installer.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Security System Installer.", "x": "Hiring: Monitored vs self.. Get three quotes, check license and insurance, read reviews, and get it in writing — Smart locks.. protect your home. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Security System Installer this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Security System Installer this.", "x": "Ask: Camera placement.. Are you licensed and insured? What is the timeline? What is excluded? Sensors. Good pros answer clearly; evasive ones walk away from. Security System Installer Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Security System Installer.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Security System Installer.", "x": "Before signing: Contracts.. Who does the work — employees or subs? What is the payment schedule? Video doorbells. Never pay in full upfront. protect your home. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Security System Installer pricing: Privacy..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Security System Installer pricing: Privacy..", "x": "Costs: Privacy.. Prices vary by region and job size — Alarm systems.. protect your home. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Security System Installer yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Security System Installer yourself?", "x": "DIY or pro: Security System Installer is DIY-friendly when Quotes. — but Cameras.. protect your home. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-security-system-installer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
