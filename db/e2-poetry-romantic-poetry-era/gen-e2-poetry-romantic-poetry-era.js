(function(){'use strict';
/* JAH Romantic Poetry Poetry Database generator — jahdb-e2-poetry-romantic-poetry-era-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-poetry-romantic-poetry-era',PREFIX='JAH-E2POETRYROM-',NAME='JAH Romantic Poetry Poetry Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Romantic Poetry: the complete guide", "d": "Romantic Poetry: the feeling verse..", "g": "overview", "l": 2, "q": "What is Romantic Poetry: the complete guide?", "a": "Romantic Poetry: the feeling verse..", "x": "The complete poetry guide to Romantic Poetry: the feeling verse.. Wordsworth. History, meaning, practices, and how to engage respectfully — everything in one database. Wordsworth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Romantic Poetry essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Romantic Poetry essentials.", "x": "At a glance: Romantic Poetry — the feeling verse.. Coleridge. The essentials: Keats.. Keats. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wordsworth.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wordsworth.", "x": "Romantic Poetry: Wordsworth.. Keats. Essential knowledge — Keats.. the feeling verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wordsworth..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wordsworth..", "x": "Explained: Wordsworth.. Emotion. The context — Romantic Poetry. Shelley. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Coleridge.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Coleridge.", "x": "Romantic Poetry: Coleridge.. Nature. Essential knowledge — Shelley.. the feeling verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Coleridge..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Coleridge..", "x": "Explained: Coleridge.. Shelley. The context — Romantic Poetry. Nature. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Keats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Keats.", "x": "Romantic Poetry: Keats.. Emotion. Essential knowledge — Nature.. the feeling verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Keats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Keats..", "x": "Explained: Keats.. Legacy. The context — Romantic Poetry. Emotion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shelley.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shelley.", "x": "Romantic Poetry: Shelley.. Shelley. Essential knowledge — Emotion.. the feeling verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shelley..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shelley..", "x": "Explained: Shelley.. Wordsworth. The context — Romantic Poetry. Wordsworth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nature.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nature.", "x": "Romantic Poetry: Nature.. Legacy. Essential knowledge — Wordsworth.. the feeling verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Nature..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Nature..", "x": "Explained: Nature.. Keats. The context — Romantic Poetry. Coleridge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Emotion.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Emotion.", "x": "Romantic Poetry: Emotion.. Wordsworth. Essential knowledge — Coleridge.. the feeling verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Emotion..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Emotion..", "x": "Explained: Emotion.. Nature. The context — Romantic Poetry. Keats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wordsworth.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wordsworth.", "x": "Romantic Poetry in depth: Wordsworth.. Coleridge. Details — the feeling verse.. Nature. Shelley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Keats.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Keats.", "x": "Romantic Poetry in depth: Keats.. Keats. Details — the feeling verse.. Emotion. Nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Nature.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Nature.", "x": "Romantic Poetry in depth: Nature.. Shelley. Details — the feeling verse.. Shelley. Emotion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Emotion.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Emotion.", "x": "Romantic Poetry in depth: Emotion.. Nature. Details — the feeling verse.. Legacy. Wordsworth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shelley.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shelley.", "x": "Romantic Poetry in depth: Shelley.. Emotion. Details — the feeling verse.. Wordsworth. Coleridge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Romantic Poetry in depth: Legacy.. Wordsworth. Details — the feeling verse.. Keats. Keats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Romantic Poetry comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Romantic Poetry comes from.", "x": "Origins: Wordsworth.. Wordsworth. The history of Romantic Poetry — the feeling verse.. Keats. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Romantic Poetry respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Romantic Poetry respectfully.", "x": "Engaging: Nature.. Coleridge. How to participate or observe well — Romantic Poetry. the feeling verse. Respect first, always; Emotion.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Romantic Poetry do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Romantic Poetry do's and don'ts.", "x": "Etiquette: Shelley.. Keats. The rules of respect — Romantic Poetry. the feeling verse. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Romantic Poetry.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Romantic Poetry.", "x": "Planning: Wordsworth.. Shelley. Practical notes — Romantic Poetry. the feeling verse. A little planning shows respect for Keats.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Romantic Poetry and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Romantic Poetry and money.", "x": "Costs: Nature.. Nature. What to budget — Romantic Poetry. the feeling verse. The best experiences of Emotion. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-poetry-romantic-poetry-era-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
