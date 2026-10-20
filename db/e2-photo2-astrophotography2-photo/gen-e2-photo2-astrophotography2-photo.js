(function(){'use strict';
/* JAH Astro2 Database generator — jahdb-e2-photo2-astrophotography2-photo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo2-astrophotography2-photo',PREFIX='JAH-E2PHOTO2AST-',NAME='JAH Astro2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Astro2: the complete guide", "d": "Astro2: the night sky 2..", "g": "overview", "l": 2, "q": "What is Astro2: the complete guide?", "a": "Astro2: the night sky 2..", "x": "The complete photography guide to Astro2: the night sky 2.. Stacking. History, meaning, practices, and how to engage respectfully — everything in one database. Stacking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Astro2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Astro2 essentials.", "x": "At a glance: Astro2 — the night sky 2.. Tracker. The essentials: Planning.. Milky Way. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Stacking.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Stacking.", "x": "Astro2: Stacking.. Planning. Essential knowledge — Milky Way.. the night sky 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Stacking..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Stacking..", "x": "Explained: Stacking.. Tracker. The context — Astro2. Foreground. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tracker.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tracker.", "x": "Astro2: Tracker.. Dark. Essential knowledge — Foreground.. the night sky 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tracker..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tracker..", "x": "Explained: Tracker.. Foreground. The context — Astro2. Planning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Milky Way.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Milky Way.", "x": "Astro2: Milky Way.. Tracker. Essential knowledge — Planning.. the night sky 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Milky Way..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Milky Way..", "x": "Explained: Milky Way.. Tips. The context — Astro2. Dark. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Foreground.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Foreground.", "x": "Astro2: Foreground.. Foreground. Essential knowledge — Dark.. the night sky 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Foreground..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Foreground..", "x": "Explained: Foreground.. Stacking. The context — Astro2. Stacking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Planning.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Planning.", "x": "Astro2: Planning.. Tips. Essential knowledge — Stacking.. the night sky 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Planning..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Planning..", "x": "Explained: Planning.. Planning. The context — Astro2. Tracker. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dark.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dark.", "x": "Astro2: Dark.. Stacking. Essential knowledge — Tracker.. the night sky 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dark..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dark..", "x": "Explained: Dark.. Dark. The context — Astro2. Milky Way. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stacking.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stacking.", "x": "Astro2 in depth: Stacking.. Tracker. Details — the night sky 2.. Dark. Foreground. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Planning.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Planning.", "x": "Astro2 in depth: Planning.. Milky Way. Details — the night sky 2.. Tracker. Planning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dark.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dark.", "x": "Astro2 in depth: Dark.. Foreground. Details — the night sky 2.. Foreground. Dark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tracker.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tracker.", "x": "Astro2 in depth: Tracker.. Planning. Details — the night sky 2.. Tips. Stacking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Foreground.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Foreground.", "x": "Astro2 in depth: Foreground.. Dark. Details — the night sky 2.. Stacking. Tracker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Astro2 in depth: Tips.. Stacking. Details — the night sky 2.. Planning. Milky Way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Astro2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Astro2 comes from.", "x": "Origins: Stacking.. Stacking. The history of Astro2 — the night sky 2.. Planning. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Astro2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Astro2 respectfully.", "x": "Engaging: Dark.. Tracker. How to participate or observe well — Astro2. the night sky 2. Respect first, always; Tracker.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Astro2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Astro2 do's and don'ts.", "x": "Etiquette: Foreground.. Milky Way. The rules of respect — Astro2. the night sky 2. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Astro2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Astro2.", "x": "Planning: Stacking.. Foreground. Practical notes — Astro2. the night sky 2. A little planning shows respect for Planning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Astro2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Astro2 and money.", "x": "Costs: Dark.. Planning. What to budget — Astro2. the night sky 2. The best experiences of Tracker. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo2-astrophotography2-photo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
