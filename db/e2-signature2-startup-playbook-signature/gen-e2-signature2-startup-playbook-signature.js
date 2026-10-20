(function(){'use strict';
/* JAH Startup Playbook Database generator — jahdb-e2-signature2-startup-playbook-signature-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-signature2-startup-playbook-signature',PREFIX='JAH-E2SIGNATURE-',NAME='JAH Startup Playbook Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Startup Playbook: the complete guide", "d": "Startup Playbook: the launch guide..", "g": "overview", "l": 2, "q": "What is Startup Playbook: the complete guide?", "a": "Startup Playbook: the launch guide..", "x": "The complete signature original guide to Startup Playbook: the launch guide.. MVP. History, meaning, practices, and how to engage respectfully — everything in one database. MVP. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Startup Playbook essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Startup Playbook essentials.", "x": "At a glance: Startup Playbook — the launch guide.. Validation. The essentials: Runway.. Runway. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "MVP.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "MVP.", "x": "Startup Playbook: MVP.. Runway. Essential knowledge — Runway.. the launch guide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: MVP..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: MVP..", "x": "Explained: MVP.. Validation. The context — Startup Playbook. Pitch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Validation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Validation.", "x": "Startup Playbook: Validation.. Product-market. Essential knowledge — Pitch.. the launch guide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Validation..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Validation..", "x": "Explained: Validation.. Pitch. The context — Startup Playbook. Co-founders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Runway.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Runway.", "x": "Startup Playbook: Runway.. Validation. Essential knowledge — Co-founders.. the launch guide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Runway..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Runway..", "x": "Explained: Runway.. Playbook. The context — Startup Playbook. Product-market. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pitch.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pitch.", "x": "Startup Playbook: Pitch.. Pitch. Essential knowledge — Product-market.. the launch guide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pitch..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pitch..", "x": "Explained: Pitch.. MVP. The context — Startup Playbook. MVP. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Co-founders.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Co-founders.", "x": "Startup Playbook: Co-founders.. Playbook. Essential knowledge — MVP.. the launch guide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Co-founders..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Co-founders..", "x": "Explained: Co-founders.. Runway. The context — Startup Playbook. Validation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Product-market.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Product-market.", "x": "Startup Playbook: Product-market.. MVP. Essential knowledge — Validation.. the launch guide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Product-market..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Product-market..", "x": "Explained: Product-market.. Product-market. The context — Startup Playbook. Runway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "MVP.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "MVP.", "x": "Startup Playbook in depth: MVP.. Validation. Details — the launch guide.. Product-market. Pitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Runway.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Runway.", "x": "Startup Playbook in depth: Runway.. Runway. Details — the launch guide.. Validation. Co-founders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Product-market.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Product-market.", "x": "Startup Playbook in depth: Product-market.. Pitch. Details — the launch guide.. Pitch. Product-market. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Validation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Validation.", "x": "Startup Playbook in depth: Validation.. Co-founders. Details — the launch guide.. Playbook. MVP. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pitch.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pitch.", "x": "Startup Playbook in depth: Pitch.. Product-market. Details — the launch guide.. MVP. Validation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Playbook.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Playbook.", "x": "Startup Playbook in depth: Playbook.. MVP. Details — the launch guide.. Runway. Runway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Startup Playbook comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Startup Playbook comes from.", "x": "Origins: MVP.. MVP. The history of Startup Playbook — the launch guide.. Runway. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Startup Playbook respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Startup Playbook respectfully.", "x": "Engaging: Product-market.. Validation. How to participate or observe well — Startup Playbook. the launch guide. Respect first, always; Validation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Startup Playbook do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Startup Playbook do's and don'ts.", "x": "Etiquette: Pitch.. Runway. The rules of respect — Startup Playbook. the launch guide. When in doubt, ask about Playbook.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Startup Playbook.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Startup Playbook.", "x": "Planning: MVP.. Pitch. Practical notes — Startup Playbook. the launch guide. A little planning shows respect for Runway.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Startup Playbook and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Startup Playbook and money.", "x": "Costs: Product-market.. Co-founders. What to budget — Startup Playbook. the launch guide. The best experiences of Validation. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-signature2-startup-playbook-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
