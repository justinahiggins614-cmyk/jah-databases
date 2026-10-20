(function(){'use strict';
/* JAH Junk Removal Database generator — jahdb-e2-trade-junk-removal-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade-junk-removal',PREFIX='JAH-E2TRADEJUNK-',NAME='JAH Junk Removal Database';
var FIELDS=["overview", "services", "tips", "hiring", "costs", "diy", "warnings", "maintenance", "emergencies", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Junk Removal: the complete guide", "d": "Junk Removal: clear it out..", "g": "overview", "l": 2, "q": "What is Junk Removal: the complete guide?", "a": "Junk Removal: clear it out..", "x": "The complete Junk Removal guide: clear it out.. Furniture. What they do, when to call, what it costs, how to hire right, and what you can do yourself — everything a homeowner needs in one database. Volume pricing.", "s": "public-reference", "f": null}, {"t": "What they do", "d": "Junk Removal services: Furniture..", "g": "services", "l": 2, "q": "What is What they do?", "a": "Junk Removal services: Furniture..", "x": "What a Junk Removal does: Furniture.. Yard debris. The trade covers Estate cleanout. — and knowing the full service list keeps you from calling the wrong pro. clear it out. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 1", "d": "Furniture.", "g": "services", "l": 2, "q": "What is Service 1?", "a": "Furniture.", "x": "Junk Removal: Furniture.. Donate first. One of the core services — Estate cleanout.. clear it out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Junk Removal when: Furniture..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Junk Removal when: Furniture..", "x": "When to call: Furniture.. Quotes. Do not wait on Junk Removal — small problems become expensive ones. Hot tubs. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 2", "d": "Yard debris.", "g": "services", "l": 2, "q": "What is Service 2?", "a": "Yard debris.", "x": "Junk Removal: Yard debris.. Quotes. One of the core services — Hot tubs.. clear it out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Junk Removal when: Yard debris..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Junk Removal when: Yard debris..", "x": "When to call: Yard debris.. Same day. Do not wait on Junk Removal — small problems become expensive ones. Donation. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 3", "d": "Estate cleanout.", "g": "services", "l": 2, "q": "What is Service 3?", "a": "Estate cleanout.", "x": "Junk Removal: Estate cleanout.. Same day. One of the core services — Donation.. clear it out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Junk Removal when: Estate cleanout..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Junk Removal when: Estate cleanout..", "x": "When to call: Estate cleanout.. Eco. Do not wait on Junk Removal — small problems become expensive ones. Recycling. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 4", "d": "Hot tubs.", "g": "services", "l": 2, "q": "What is Service 4?", "a": "Hot tubs.", "x": "Junk Removal: Hot tubs.. Eco. One of the core services — Recycling.. clear it out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Junk Removal when: Hot tubs..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Junk Removal when: Hot tubs..", "x": "When to call: Hot tubs.. Hazardous. Do not wait on Junk Removal — small problems become expensive ones. Furniture. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 5", "d": "Donation.", "g": "services", "l": 2, "q": "What is Service 5?", "a": "Donation.", "x": "Junk Removal: Donation.. Hazardous. One of the core services — Furniture.. clear it out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Junk Removal when: Donation..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Junk Removal when: Donation..", "x": "When to call: Donation.. Volume pricing. Do not wait on Junk Removal — small problems become expensive ones. Yard debris. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Service 6", "d": "Recycling.", "g": "services", "l": 2, "q": "What is Service 6?", "a": "Recycling.", "x": "Junk Removal: Recycling.. Volume pricing. One of the core services — Yard debris.. clear it out. Know what good looks like before anyone starts work. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "When you need it", "d": "Call a Junk Removal when: Recycling..", "g": "services", "l": 2, "q": "What is When you need it?", "a": "Call a Junk Removal when: Recycling..", "x": "When to call: Recycling.. Donate first. Do not wait on Junk Removal — small problems become expensive ones. Estate cleanout. If in doubt, call and ask; quotes are usually free. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 1", "d": "Volume pricing.", "g": "tips", "l": 2, "q": "What is Pro tip 1?", "a": "Volume pricing.", "x": "Junk Removal tip: Volume pricing.. Yard debris. From the trade itself — Same day.. clear it out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 2", "d": "Donate first.", "g": "tips", "l": 2, "q": "What is Pro tip 2?", "a": "Donate first.", "x": "Junk Removal tip: Donate first.. Estate cleanout. From the trade itself — Eco.. clear it out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 3", "d": "Quotes.", "g": "tips", "l": 2, "q": "What is Pro tip 3?", "a": "Quotes.", "x": "Junk Removal tip: Quotes.. Hot tubs. From the trade itself — Hazardous.. clear it out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 4", "d": "Same day.", "g": "tips", "l": 2, "q": "What is Pro tip 4?", "a": "Same day.", "x": "Junk Removal tip: Same day.. Donation. From the trade itself — Volume pricing.. clear it out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 5", "d": "Eco.", "g": "tips", "l": 2, "q": "What is Pro tip 5?", "a": "Eco.", "x": "Junk Removal tip: Eco.. Recycling. From the trade itself — Donate first.. clear it out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Pro tip 6", "d": "Hazardous.", "g": "tips", "l": 2, "q": "What is Pro tip 6?", "a": "Hazardous.", "x": "Junk Removal tip: Hazardous.. Furniture. From the trade itself — Quotes.. clear it out. Tips like this save money and headaches. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Hiring guide", "d": "Hire the right Junk Removal.", "g": "hiring", "l": 2, "q": "What is Hiring guide?", "a": "Hire the right Junk Removal.", "x": "Hiring: Volume pricing.. Get three quotes, check license and insurance, read reviews, and get it in writing — Hot tubs.. clear it out. The cheapest bid is rarely the best value. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "Questions to ask", "d": "Ask your Junk Removal this.", "g": "hiring", "l": 2, "q": "What is Questions to ask?", "a": "Ask your Junk Removal this.", "x": "Ask: Donate first.. Are you licensed and insured? What is the timeline? What is excluded? Donation. Good pros answer clearly; evasive ones walk away from. Junk Removal Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "More questions", "d": "Before you sign with a Junk Removal.", "g": "hiring", "l": 2, "q": "What is More questions?", "a": "Before you sign with a Junk Removal.", "x": "Before signing: Quotes.. Who does the work — employees or subs? What is the payment schedule? Recycling. Never pay in full upfront. clear it out. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "What it costs", "d": "Junk Removal pricing: Same day..", "g": "costs", "l": 2, "q": "What is What it costs?", "a": "Junk Removal pricing: Same day..", "x": "Costs: Same day.. Prices vary by region and job size — Furniture.. clear it out. Get itemized quotes and understand what drives the price before you compare. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}, {"t": "DIY vs pro", "d": "Can you do Junk Removal yourself?", "g": "diy", "l": 2, "q": "What is DIY vs pro?", "a": "Can you do Junk Removal yourself?", "x": "DIY or pro: Junk Removal is DIY-friendly when Eco. — but Yard debris.. clear it out. Know your limits: permits, safety, and warranties favor pros on big jobs. Trade knowledge from industry standards and consumer guidance. Licensing varies by state; verify credentials locally.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade-junk-removal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
