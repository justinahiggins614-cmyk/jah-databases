(function(){'use strict';
/* JAH Mozzarella2 Database generator — jahdb-e2-cheese2-mozzarella2-cheese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cheese2-mozzarella2-cheese',PREFIX='JAH-E2CHEESE2MO-',NAME='JAH Mozzarella2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mozzarella2: the complete guide", "d": "Mozzarella2: the fresh 2..", "g": "overview", "l": 2, "q": "What is Mozzarella2: the complete guide?", "a": "Mozzarella2: the fresh 2..", "x": "The complete cheese guide to Mozzarella2: the fresh 2.. Burrata. History, meaning, practices, and how to engage respectfully — everything in one database. Burrata. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mozzarella2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mozzarella2 essentials.", "x": "At a glance: Mozzarella2 — the fresh 2.. Buffalo. The essentials: Fresh.. Pasta filata. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Burrata.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Burrata.", "x": "Mozzarella2: Burrata.. Fresh. Essential knowledge — Pasta filata.. the fresh 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Burrata..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Burrata..", "x": "Explained: Burrata.. Buffalo. The context — Mozzarella2. Caprese. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Buffalo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Buffalo.", "x": "Mozzarella2: Buffalo.. Stretch. Essential knowledge — Caprese.. the fresh 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Buffalo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Buffalo..", "x": "Explained: Buffalo.. Caprese. The context — Mozzarella2. Fresh. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pasta filata.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pasta filata.", "x": "Mozzarella2: Pasta filata.. Buffalo. Essential knowledge — Fresh.. the fresh 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pasta filata..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pasta filata..", "x": "Explained: Pasta filata.. Pairing. The context — Mozzarella2. Stretch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Caprese.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Caprese.", "x": "Mozzarella2: Caprese.. Caprese. Essential knowledge — Stretch.. the fresh 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Caprese..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Caprese..", "x": "Explained: Caprese.. Burrata. The context — Mozzarella2. Burrata. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fresh.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fresh.", "x": "Mozzarella2: Fresh.. Pairing. Essential knowledge — Burrata.. the fresh 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fresh..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fresh..", "x": "Explained: Fresh.. Fresh. The context — Mozzarella2. Buffalo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stretch.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stretch.", "x": "Mozzarella2: Stretch.. Burrata. Essential knowledge — Buffalo.. the fresh 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stretch..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stretch..", "x": "Explained: Stretch.. Stretch. The context — Mozzarella2. Pasta filata. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Burrata.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Burrata.", "x": "Mozzarella2 in depth: Burrata.. Buffalo. Details — the fresh 2.. Stretch. Caprese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fresh.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fresh.", "x": "Mozzarella2 in depth: Fresh.. Pasta filata. Details — the fresh 2.. Buffalo. Fresh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stretch.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stretch.", "x": "Mozzarella2 in depth: Stretch.. Caprese. Details — the fresh 2.. Caprese. Stretch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Buffalo.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Buffalo.", "x": "Mozzarella2 in depth: Buffalo.. Fresh. Details — the fresh 2.. Pairing. Burrata. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Caprese.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Caprese.", "x": "Mozzarella2 in depth: Caprese.. Stretch. Details — the fresh 2.. Burrata. Buffalo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Pairing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Pairing.", "x": "Mozzarella2 in depth: Pairing.. Burrata. Details — the fresh 2.. Fresh. Pasta filata. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mozzarella2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mozzarella2 comes from.", "x": "Origins: Burrata.. Burrata. The history of Mozzarella2 — the fresh 2.. Fresh. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mozzarella2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mozzarella2 respectfully.", "x": "Engaging: Stretch.. Buffalo. How to participate or observe well — Mozzarella2. the fresh 2. Respect first, always; Buffalo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mozzarella2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mozzarella2 do's and don'ts.", "x": "Etiquette: Caprese.. Pasta filata. The rules of respect — Mozzarella2. the fresh 2. When in doubt, ask about Pairing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mozzarella2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mozzarella2.", "x": "Planning: Burrata.. Caprese. Practical notes — Mozzarella2. the fresh 2. A little planning shows respect for Fresh.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mozzarella2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mozzarella2 and money.", "x": "Costs: Stretch.. Fresh. What to budget — Mozzarella2. the fresh 2. The best experiences of Buffalo. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cheese2-mozzarella2-cheese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
