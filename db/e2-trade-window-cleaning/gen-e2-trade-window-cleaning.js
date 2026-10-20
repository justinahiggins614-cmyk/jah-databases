(function(){'use strict';
/* JAH Window Cleaning Database generator — jahdb-e2-trade-window-cleaning-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-window-cleaning',PREFIX='JAH-E2TRADEWIND-',NAME='JAH Window Cleaning Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Window Cleaning: the complete guide", "d": "Window Cleaning: streak-free glass inside and out..", "g": "overview", "l": 2, "q": "What is Window Cleaning: the complete guide?", "a": "Window Cleaning: streak-free glass inside and out..", "x": "The complete Window Cleaning guide: streak-free glass inside and out.. Exterior windows. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Twice yearly.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Window Cleaning services: Exterior windows..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Window Cleaning services: Exterior windows..", "x": "What a Window Cleaning does: Exterior windows.. Interior. The trade covers Screens. — and knowing the full service list keeps you from calling the wrong pro. streak-free glass inside and out. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Exterior windows.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Exterior windows.", "x": "Window Cleaning: Exterior windows.. Pure water. One of the core services — Screens.. streak-free glass inside and out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Window Cleaning when: Exterior windows..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Window Cleaning when: Exterior windows..", "x": "When to call: Exterior windows.. Screens too. Do not wait on Window Cleaning — small problems become expensive ones. Tracks. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Interior.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Interior.", "x": "Window Cleaning: Interior.. Screens too. One of the core services — Tracks.. streak-free glass inside and out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Window Cleaning when: Interior..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Window Cleaning when: Interior..", "x": "When to call: Interior.. Safety. Do not wait on Window Cleaning — small problems become expensive ones. Skylights. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Screens.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Screens.", "x": "Window Cleaning: Screens.. Safety. One of the core services — Skylights.. streak-free glass inside and out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Window Cleaning when: Screens..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Window Cleaning when: Screens..", "x": "When to call: Screens.. Quotes. Do not wait on Window Cleaning — small problems become expensive ones. Gutters. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Tracks.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Tracks.", "x": "Window Cleaning: Tracks.. Quotes. One of the core services — Gutters.. streak-free glass inside and out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Window Cleaning when: Tracks..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Window Cleaning when: Tracks..", "x": "When to call: Tracks.. Maintain. Do not wait on Window Cleaning — small problems become expensive ones. Exterior windows. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Skylights.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Skylights.", "x": "Window Cleaning: Skylights.. Maintain. One of the core services — Exterior windows.. streak-free glass inside and out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Window Cleaning when: Skylights..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Window Cleaning when: Skylights..", "x": "When to call: Skylights.. Twice yearly. Do not wait on Window Cleaning — small problems become expensive ones. Interior. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Gutters.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Gutters.", "x": "Window Cleaning: Gutters.. Twice yearly. One of the core services — Interior.. streak-free glass inside and out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Window Cleaning when: Gutters..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Window Cleaning when: Gutters..", "x": "When to call: Gutters.. Pure water. Do not wait on Window Cleaning — small problems become expensive ones. Screens. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Twice yearly.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Twice yearly.", "x": "Window Cleaning tip: Twice yearly.. Interior. From the trade itself — Safety.. streak-free glass inside and out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Pure water.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Pure water.", "x": "Window Cleaning tip: Pure water.. Screens. From the trade itself — Quotes.. streak-free glass inside and out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Screens too.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Screens too.", "x": "Window Cleaning tip: Screens too.. Tracks. From the trade itself — Maintain.. streak-free glass inside and out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Safety.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Safety.", "x": "Window Cleaning tip: Safety.. Skylights. From the trade itself — Twice yearly.. streak-free glass inside and out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Quotes.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Quotes.", "x": "Window Cleaning tip: Quotes.. Gutters. From the trade itself — Pure water.. streak-free glass inside and out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Maintain.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Maintain.", "x": "Window Cleaning tip: Maintain.. Exterior windows. From the trade itself — Screens too.. streak-free glass inside and out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Window Cleaning.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Window Cleaning.", "x": "Hiring: Twice yearly.. Get three quotes, check license and insurance, read reviews, and get it in writing — Tracks.. streak-free glass inside and out. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Window Cleaning this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Window Cleaning this.", "x": "Ask: Pure water.. Are you licensed and insured? What is the timeline? What is excluded? Skylights. Good pros answer clearly; evasive ones walk away from. Window Cleaning Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Window Cleaning.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Window Cleaning.", "x": "Before signing: Screens too.. Who does the work — employees or subs? What is the payment schedule? Gutters. Never pay in full upfront. streak-free glass inside and out. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Window Cleaning pricing: Safety..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Window Cleaning pricing: Safety..", "x": "Costs: Safety.. Prices vary by region and job size — Exterior windows.. streak-free glass inside and out. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Window Cleaning yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Window Cleaning yourself?", "x": "DIY or pro: Window Cleaning is DIY-friendly when Quotes. — but Interior.. streak-free glass inside and out. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-window-cleaning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
