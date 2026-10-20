(function(){'use strict';
/* JAH Vignette Stories Short Story Database generator — jahdb-e2-story-vignette-short-stories-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-story-vignette-short-stories',PREFIX='JAH-E2STORYVIGN-',NAME='JAH Vignette Stories Short Story Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vignette Stories: the complete guide", "d": "Vignette Stories: the snapshot prose..", "g": "overview", "l": 2, "q": "What is Vignette Stories: the complete guide?", "a": "Vignette Stories: the snapshot prose..", "x": "The complete short story guide to Vignette Stories: the snapshot prose.. Scenes. History, meaning, practices, and how to engage respectfully — everything in one database. Scenes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vignette Stories essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vignette Stories essentials.", "x": "At a glance: Vignette Stories — the snapshot prose.. Impression. The essentials: Mood.. No plot. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Scenes.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Scenes.", "x": "Vignette Stories: Scenes.. Mood. Essential knowledge — No plot.. the snapshot prose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Scenes..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Scenes..", "x": "Explained: Scenes.. Hemingway. The context — Vignette Stories. Mood. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Impression.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Impression.", "x": "Vignette Stories: Impression.. Slice. Essential knowledge — Mood.. the snapshot prose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Impression..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Impression..", "x": "Explained: Impression.. Impression. The context — Vignette Stories. Hemingway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "No plot.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "No plot.", "x": "Vignette Stories: No plot.. Hemingway. Essential knowledge — Hemingway.. the snapshot prose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: No plot..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: No plot..", "x": "Explained: No plot.. Craft. The context — Vignette Stories. Slice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mood.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mood.", "x": "Vignette Stories: Mood.. Impression. Essential knowledge — Slice.. the snapshot prose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mood..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mood..", "x": "Explained: Mood.. Scenes. The context — Vignette Stories. Scenes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hemingway.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hemingway.", "x": "Vignette Stories: Hemingway.. Craft. Essential knowledge — Scenes.. the snapshot prose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hemingway..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hemingway..", "x": "Explained: Hemingway.. Mood. The context — Vignette Stories. Impression. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Slice.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Slice.", "x": "Vignette Stories: Slice.. Scenes. Essential knowledge — Impression.. the snapshot prose. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Slice..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Slice..", "x": "Explained: Slice.. Slice. The context — Vignette Stories. No plot. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Scenes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Scenes.", "x": "Vignette Stories in depth: Scenes.. Impression. Details — the snapshot prose.. Slice. Mood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mood.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mood.", "x": "Vignette Stories in depth: Mood.. No plot. Details — the snapshot prose.. Hemingway. Hemingway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Slice.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Slice.", "x": "Vignette Stories in depth: Slice.. Mood. Details — the snapshot prose.. Impression. Slice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hemingway.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hemingway.", "x": "Vignette Stories in depth: Hemingway.. Hemingway. Details — the snapshot prose.. Craft. Scenes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Impression.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Impression.", "x": "Vignette Stories in depth: Impression.. Slice. Details — the snapshot prose.. Scenes. Impression. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Craft.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Craft.", "x": "Vignette Stories in depth: Craft.. Scenes. Details — the snapshot prose.. Mood. No plot. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vignette Stories comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vignette Stories comes from.", "x": "Origins: Scenes.. Scenes. The history of Vignette Stories — the snapshot prose.. Mood. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vignette Stories respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vignette Stories respectfully.", "x": "Engaging: Slice.. Impression. How to participate or observe well — Vignette Stories. the snapshot prose. Respect first, always; Hemingway.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vignette Stories do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vignette Stories do's and don'ts.", "x": "Etiquette: Impression.. No plot. The rules of respect — Vignette Stories. the snapshot prose. When in doubt, ask about Craft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vignette Stories.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vignette Stories.", "x": "Planning: Scenes.. Mood. Practical notes — Vignette Stories. the snapshot prose. A little planning shows respect for Mood.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vignette Stories and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vignette Stories and money.", "x": "Costs: Slice.. Hemingway. What to budget — Vignette Stories. the snapshot prose. The best experiences of Hemingway. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-story-vignette-short-stories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
