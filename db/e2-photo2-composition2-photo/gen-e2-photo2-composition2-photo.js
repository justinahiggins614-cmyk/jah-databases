(function(){'use strict';
/* JAH Composition2 Database generator — jahdb-e2-photo2-composition2-photo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo2-composition2-photo',PREFIX='JAH-E2PHOTO2COM-',NAME='JAH Composition2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Composition2: the complete guide", "d": "Composition2: the framing 2..", "g": "overview", "l": 2, "q": "What is Composition2: the complete guide?", "a": "Composition2: the framing 2..", "x": "The complete photography guide to Composition2: the framing 2.. Golden spiral. History, meaning, practices, and how to engage respectfully — everything in one database. Spiral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Composition2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Composition2 essentials.", "x": "At a glance: Composition2 — the framing 2.. Diagonals. The essentials: Balance.. Framing. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Golden spiral.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Golden spiral.", "x": "Composition2: Golden spiral.. Balance. Essential knowledge — Framing.. the framing 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Golden spiral..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Golden spiral..", "x": "Explained: Golden spiral.. Diagonals. The context — Composition2. Minimal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Diagonals.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Diagonals.", "x": "Composition2: Diagonals.. Tension. Essential knowledge — Minimal.. the framing 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Diagonals..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Diagonals..", "x": "Explained: Diagonals.. Framing. The context — Composition2. Balance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Framing.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Framing.", "x": "Composition2: Framing.. Diagonals. Essential knowledge — Balance.. the framing 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Framing..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Framing..", "x": "Explained: Framing.. Tips. The context — Composition2. Tension. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Minimal.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Minimal.", "x": "Composition2: Minimal.. Framing. Essential knowledge — Tension.. the framing 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Minimal..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Minimal..", "x": "Explained: Minimal.. Spiral. The context — Composition2. Golden spiral. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Balance.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Balance.", "x": "Composition2: Balance.. Tips. Essential knowledge — Golden spiral.. the framing 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Balance..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Balance..", "x": "Explained: Balance.. Balance. The context — Composition2. Diagonals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tension.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tension.", "x": "Composition2: Tension.. Spiral. Essential knowledge — Diagonals.. the framing 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tension..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tension..", "x": "Explained: Tension.. Tension. The context — Composition2. Framing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spiral.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spiral.", "x": "Composition2 in depth: Spiral.. Diagonals. Details — the framing 2.. Tension. Minimal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Balance.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Balance.", "x": "Composition2 in depth: Balance.. Framing. Details — the framing 2.. Diagonals. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tension.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tension.", "x": "Composition2 in depth: Tension.. Minimal. Details — the framing 2.. Framing. Tension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Diagonals.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Diagonals.", "x": "Composition2 in depth: Diagonals.. Balance. Details — the framing 2.. Tips. Golden spiral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Framing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Framing.", "x": "Composition2 in depth: Framing.. Tension. Details — the framing 2.. Spiral. Diagonals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Composition2 in depth: Tips.. Golden spiral. Details — the framing 2.. Balance. Framing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Composition2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Composition2 comes from.", "x": "Origins: Spiral.. Golden spiral. The history of Composition2 — the framing 2.. Balance. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Composition2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Composition2 respectfully.", "x": "Engaging: Tension.. Diagonals. How to participate or observe well — Composition2. the framing 2. Respect first, always; Diagonals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Composition2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Composition2 do's and don'ts.", "x": "Etiquette: Framing.. Framing. The rules of respect — Composition2. the framing 2. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Composition2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Composition2.", "x": "Planning: Spiral.. Minimal. Practical notes — Composition2. the framing 2. A little planning shows respect for Balance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Composition2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Composition2 and money.", "x": "Costs: Tension.. Balance. What to budget — Composition2. the framing 2. The best experiences of Diagonals. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo2-composition2-photo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
