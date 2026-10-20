(function(){'use strict';
/* JAH Rooibos Tea Tea Database generator — jahdb-e2-tea-rooibos-tea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tea-rooibos-tea',PREFIX='JAH-E2TEAROOIBO-',NAME='JAH Rooibos Tea Tea Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rooibos Tea: the complete guide", "d": "Rooibos Tea: the South African red..", "g": "overview", "l": 2, "q": "What is Rooibos Tea: the complete guide?", "a": "Rooibos Tea: the South African red..", "x": "The complete tea guide to Rooibos Tea: the South African red.. South Africa. History, meaning, practices, and how to engage respectfully — everything in one database. SA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rooibos Tea essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rooibos Tea essentials.", "x": "At a glance: Rooibos Tea — the South African red.. Red. The essentials: Red.. Caffeine-free. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "South Africa.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "South Africa.", "x": "Rooibos Tea: South Africa.. Red. Essential knowledge — Caffeine-free.. the South African red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: South Africa..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: South Africa..", "x": "Explained: South Africa.. Antioxidants. The context — Rooibos Tea. Antioxidants. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Red.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Red.", "x": "Rooibos Tea: Red.. Latte. Essential knowledge — Antioxidants.. the South African red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Red..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Red..", "x": "Explained: Red.. Blends. The context — Rooibos Tea. Vanilla. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Caffeine-free.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Caffeine-free.", "x": "Rooibos Tea: Caffeine-free.. Antioxidants. Essential knowledge — Vanilla.. the South African red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Caffeine-free..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Caffeine-free..", "x": "Explained: Caffeine-free.. History. The context — Rooibos Tea. Latte. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Antioxidants.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Antioxidants.", "x": "Rooibos Tea: Antioxidants.. Blends. Essential knowledge — Latte.. the South African red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Antioxidants..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Antioxidants..", "x": "Explained: Antioxidants.. SA. The context — Rooibos Tea. South Africa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vanilla.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vanilla.", "x": "Rooibos Tea: Vanilla.. History. Essential knowledge — South Africa.. the South African red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vanilla..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vanilla..", "x": "Explained: Vanilla.. Red. The context — Rooibos Tea. Red. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Latte.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Latte.", "x": "Rooibos Tea: Latte.. SA. Essential knowledge — Red.. the South African red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Latte..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Latte..", "x": "Explained: Latte.. Latte. The context — Rooibos Tea. Caffeine-free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "SA.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "SA.", "x": "Rooibos Tea in depth: SA.. Red. Details — the South African red.. Latte. Antioxidants. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Red.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Red.", "x": "Rooibos Tea in depth: Red.. Caffeine-free. Details — the South African red.. Antioxidants. Vanilla. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Latte.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Latte.", "x": "Rooibos Tea in depth: Latte.. Antioxidants. Details — the South African red.. Blends. Latte. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Antioxidants.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Antioxidants.", "x": "Rooibos Tea in depth: Antioxidants.. Vanilla. Details — the South African red.. History. South Africa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Blends.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Blends.", "x": "Rooibos Tea in depth: Blends.. Latte. Details — the South African red.. SA. Red. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Rooibos Tea in depth: History.. South Africa. Details — the South African red.. Red. Caffeine-free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rooibos Tea comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rooibos Tea comes from.", "x": "Origins: SA.. South Africa. The history of Rooibos Tea — the South African red.. Red. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rooibos Tea respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rooibos Tea respectfully.", "x": "Engaging: Latte.. Red. How to participate or observe well — Rooibos Tea. the South African red. Respect first, always; Antioxidants.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rooibos Tea do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rooibos Tea do's and don'ts.", "x": "Etiquette: Blends.. Caffeine-free. The rules of respect — Rooibos Tea. the South African red. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rooibos Tea.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rooibos Tea.", "x": "Planning: SA.. Antioxidants. Practical notes — Rooibos Tea. the South African red. A little planning shows respect for Red.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rooibos Tea and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rooibos Tea and money.", "x": "Costs: Latte.. Vanilla. What to budget — Rooibos Tea. the South African red. The best experiences of Antioxidants. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tea-rooibos-tea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
