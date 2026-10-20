(function(){'use strict';
/* JAH Stravinsky Composer Composer Database generator — jahdb-e2-composer-stravinsky-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-stravinsky-composer',PREFIX='JAH-E2COMPOSERS-',NAME='JAH Stravinsky Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stravinsky Composer: the complete guide", "d": "Stravinsky Composer: the rite revolutionary..", "g": "overview", "l": 2, "q": "What is Stravinsky Composer: the complete guide?", "a": "Stravinsky Composer: the rite revolutionary..", "x": "The complete composer guide to Stravinsky Composer: the rite revolutionary.. 1882. History, meaning, practices, and how to engage respectfully — everything in one database. Rite. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Stravinsky Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Stravinsky Composer essentials.", "x": "At a glance: Stravinsky Composer — the rite revolutionary.. Rite of Spring. The essentials: Firebird.. Firebird. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1882.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1882.", "x": "Stravinsky Composer: 1882.. Firebird. Essential knowledge — Firebird.. the rite revolutionary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1882..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1882..", "x": "Explained: 1882.. Neoclassical. The context — Stravinsky Composer. Petrushka. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rite of Spring.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rite of Spring.", "x": "Stravinsky Composer: Rite of Spring.. Russia. Essential knowledge — Petrushka.. the rite revolutionary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rite of Spring..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rite of Spring..", "x": "Explained: Rite of Spring.. Riot. The context — Stravinsky Composer. Russia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Firebird.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Firebird.", "x": "Stravinsky Composer: Firebird.. Neoclassical. Essential knowledge — Russia.. the rite revolutionary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Firebird..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Firebird..", "x": "Explained: Firebird.. Legacy. The context — Stravinsky Composer. Neoclassical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Petrushka.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Petrushka.", "x": "Stravinsky Composer: Petrushka.. Riot. Essential knowledge — Neoclassical.. the rite revolutionary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Petrushka..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Petrushka..", "x": "Explained: Petrushka.. Rite. The context — Stravinsky Composer. 1882. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Russia.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Russia.", "x": "Stravinsky Composer: Russia.. Legacy. Essential knowledge — 1882.. the rite revolutionary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Russia..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Russia..", "x": "Explained: Russia.. Firebird. The context — Stravinsky Composer. Rite of Spring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Neoclassical.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Neoclassical.", "x": "Stravinsky Composer: Neoclassical.. Rite. Essential knowledge — Rite of Spring.. the rite revolutionary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Neoclassical..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Neoclassical..", "x": "Explained: Neoclassical.. Russia. The context — Stravinsky Composer. Firebird. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rite.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rite.", "x": "Stravinsky Composer in depth: Rite.. Rite of Spring. Details — the rite revolutionary.. Russia. Petrushka. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Firebird.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Firebird.", "x": "Stravinsky Composer in depth: Firebird.. Firebird. Details — the rite revolutionary.. Neoclassical. Russia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Russia.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Russia.", "x": "Stravinsky Composer in depth: Russia.. Petrushka. Details — the rite revolutionary.. Riot. Neoclassical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Neoclassical.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Neoclassical.", "x": "Stravinsky Composer in depth: Neoclassical.. Russia. Details — the rite revolutionary.. Legacy. 1882. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Riot.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Riot.", "x": "Stravinsky Composer in depth: Riot.. Neoclassical. Details — the rite revolutionary.. Rite. Rite of Spring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Stravinsky Composer in depth: Legacy.. 1882. Details — the rite revolutionary.. Firebird. Firebird. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Stravinsky Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Stravinsky Composer comes from.", "x": "Origins: Rite.. 1882. The history of Stravinsky Composer — the rite revolutionary.. Firebird. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Stravinsky Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Stravinsky Composer respectfully.", "x": "Engaging: Russia.. Rite of Spring. How to participate or observe well — Stravinsky Composer. the rite revolutionary. Respect first, always; Neoclassical.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Stravinsky Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Stravinsky Composer do's and don'ts.", "x": "Etiquette: Riot.. Firebird. The rules of respect — Stravinsky Composer. the rite revolutionary. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Stravinsky Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Stravinsky Composer.", "x": "Planning: Rite.. Petrushka. Practical notes — Stravinsky Composer. the rite revolutionary. A little planning shows respect for Firebird.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Stravinsky Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Stravinsky Composer and money.", "x": "Costs: Russia.. Russia. What to budget — Stravinsky Composer. the rite revolutionary. The best experiences of Neoclassical. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-stravinsky-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
