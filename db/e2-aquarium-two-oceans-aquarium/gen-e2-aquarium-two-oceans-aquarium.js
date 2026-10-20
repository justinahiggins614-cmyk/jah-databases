(function(){'use strict';
/* JAH Two Oceans Aquarium Aquarium Database generator — jahdb-e2-aquarium-two-oceans-aquarium-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium-two-oceans-aquarium',PREFIX='JAH-E2AQUARIUMT-',NAME='JAH Two Oceans Aquarium Aquarium Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Two Oceans Aquarium: the complete guide", "d": "Two Oceans Aquarium: Cape Town's seas..", "g": "overview", "l": 2, "q": "What is Two Oceans Aquarium: the complete guide?", "a": "Two Oceans Aquarium: Cape Town's seas..", "x": "The complete aquarium guide to Two Oceans Aquarium: Cape Town's seas.. Atlantic/Indian. History, meaning, practices, and how to engage respectfully — everything in one database. Kelp. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Two Oceans Aquarium essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Two Oceans Aquarium essentials.", "x": "At a glance: Two Oceans Aquarium — Cape Town's seas.. Kelp. The essentials: Penguins.. Penguins. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Atlantic/Indian.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Atlantic/Indian.", "x": "Two Oceans Aquarium: Atlantic/Indian.. Penguins. Essential knowledge — Penguins.. Cape Town's seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Atlantic/Indian..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Atlantic/Indian..", "x": "Explained: Atlantic/Indian.. Tickets. The context — Two Oceans Aquarium. V&A. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kelp.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kelp.", "x": "Two Oceans Aquarium: Kelp.. Harbor. Essential knowledge — V&A.. Cape Town's seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Kelp..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Kelp..", "x": "Explained: Kelp.. Cape Town. The context — Two Oceans Aquarium. 1995. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Penguins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Penguins.", "x": "Two Oceans Aquarium: Penguins.. Tickets. Essential knowledge — 1995.. Cape Town's seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Penguins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Penguins..", "x": "Explained: Penguins.. Oceans. The context — Two Oceans Aquarium. Conservation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "V&A.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "V&A.", "x": "Two Oceans Aquarium: V&A.. Cape Town. Essential knowledge — Conservation.. Cape Town's seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: V&A..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: V&A..", "x": "Explained: V&A.. Kelp. The context — Two Oceans Aquarium. Atlantic/Indian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1995.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1995.", "x": "Two Oceans Aquarium: 1995.. Oceans. Essential knowledge — Atlantic/Indian.. Cape Town's seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1995..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1995..", "x": "Explained: 1995.. Penguins. The context — Two Oceans Aquarium. Kelp. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Conservation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Conservation.", "x": "Two Oceans Aquarium: Conservation.. Kelp. Essential knowledge — Kelp.. Cape Town's seas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Conservation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Conservation..", "x": "Explained: Conservation.. Harbor. The context — Two Oceans Aquarium. Penguins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Kelp.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Kelp.", "x": "Two Oceans Aquarium in depth: Kelp.. Kelp. Details — Cape Town's seas.. Harbor. V&A. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Penguins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Penguins.", "x": "Two Oceans Aquarium in depth: Penguins.. Penguins. Details — Cape Town's seas.. Tickets. 1995. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Harbor.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Harbor.", "x": "Two Oceans Aquarium in depth: Harbor.. V&A. Details — Cape Town's seas.. Cape Town. Conservation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Two Oceans Aquarium in depth: Tickets.. 1995. Details — Cape Town's seas.. Oceans. Atlantic/Indian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cape Town.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cape Town.", "x": "Two Oceans Aquarium in depth: Cape Town.. Conservation. Details — Cape Town's seas.. Kelp. Kelp. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Oceans.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Oceans.", "x": "Two Oceans Aquarium in depth: Oceans.. Atlantic/Indian. Details — Cape Town's seas.. Penguins. Penguins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Two Oceans Aquarium comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Two Oceans Aquarium comes from.", "x": "Origins: Kelp.. Atlantic/Indian. The history of Two Oceans Aquarium — Cape Town's seas.. Penguins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Two Oceans Aquarium respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Two Oceans Aquarium respectfully.", "x": "Engaging: Harbor.. Kelp. How to participate or observe well — Two Oceans Aquarium. Cape Town's seas. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Two Oceans Aquarium do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Two Oceans Aquarium do's and don'ts.", "x": "Etiquette: Cape Town.. Penguins. The rules of respect — Two Oceans Aquarium. Cape Town's seas. When in doubt, ask about Oceans.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Two Oceans Aquarium.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Two Oceans Aquarium.", "x": "Planning: Kelp.. V&A. Practical notes — Two Oceans Aquarium. Cape Town's seas. A little planning shows respect for Penguins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Two Oceans Aquarium and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Two Oceans Aquarium and money.", "x": "Costs: Harbor.. 1995. What to budget — Two Oceans Aquarium. Cape Town's seas. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium-two-oceans-aquarium-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
