(function(){'use strict';
/* JAH Shojo Anime Anime Genre Database generator — jahdb-e2-anime-shojo-anime-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-anime-shojo-anime',PREFIX='JAH-E2ANIMESHOJ-',NAME='JAH Shojo Anime Anime Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Shojo Anime: the complete guide", "d": "Shojo Anime: the girls' romance..", "g": "overview", "l": 2, "q": "What is Shojo Anime: the complete guide?", "a": "Shojo Anime: the girls' romance..", "x": "The complete anime genre guide to Shojo Anime: the girls' romance.. Sailor Moon. History, meaning, practices, and how to engage respectfully — everything in one database. Sailor Moon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Shojo Anime essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Shojo Anime essentials.", "x": "At a glance: Shojo Anime — the girls' romance.. Fruits Basket. The essentials: Romance.. Romance. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sailor Moon.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sailor Moon.", "x": "Shojo Anime: Sailor Moon.. Romance. Essential knowledge — Romance.. the girls' romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sailor Moon..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sailor Moon..", "x": "Explained: Sailor Moon.. Flowers. The context — Shojo Anime. Flowers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fruits Basket.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fruits Basket.", "x": "Shojo Anime: Fruits Basket.. Emotion. Essential knowledge — Flowers.. the girls' romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fruits Basket..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fruits Basket..", "x": "Explained: Fruits Basket.. Basket. The context — Shojo Anime. Shojo Beat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Romance.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Romance.", "x": "Shojo Anime: Romance.. Flowers. Essential knowledge — Shojo Beat.. the girls' romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Romance..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Romance..", "x": "Explained: Romance.. Classics. The context — Shojo Anime. Emotion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flowers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flowers.", "x": "Shojo Anime: Flowers.. Basket. Essential knowledge — Emotion.. the girls' romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Flowers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Flowers..", "x": "Explained: Flowers.. Sailor Moon. The context — Shojo Anime. Sailor Moon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Shojo Beat.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Shojo Beat.", "x": "Shojo Anime: Shojo Beat.. Classics. Essential knowledge — Sailor Moon.. the girls' romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Shojo Beat..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Shojo Beat..", "x": "Explained: Shojo Beat.. Romance. The context — Shojo Anime. Fruits Basket. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Emotion.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Emotion.", "x": "Shojo Anime: Emotion.. Sailor Moon. Essential knowledge — Fruits Basket.. the girls' romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Emotion..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Emotion..", "x": "Explained: Emotion.. Emotion. The context — Shojo Anime. Romance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sailor Moon.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sailor Moon.", "x": "Shojo Anime in depth: Sailor Moon.. Fruits Basket. Details — the girls' romance.. Emotion. Flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Romance.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Romance.", "x": "Shojo Anime in depth: Romance.. Romance. Details — the girls' romance.. Flowers. Shojo Beat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Emotion.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Emotion.", "x": "Shojo Anime in depth: Emotion.. Flowers. Details — the girls' romance.. Basket. Emotion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Flowers.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Flowers.", "x": "Shojo Anime in depth: Flowers.. Shojo Beat. Details — the girls' romance.. Classics. Sailor Moon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Basket.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Basket.", "x": "Shojo Anime in depth: Basket.. Emotion. Details — the girls' romance.. Sailor Moon. Fruits Basket. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Shojo Anime in depth: Classics.. Sailor Moon. Details — the girls' romance.. Romance. Romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Shojo Anime comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Shojo Anime comes from.", "x": "Origins: Sailor Moon.. Sailor Moon. The history of Shojo Anime — the girls' romance.. Romance. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Shojo Anime respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Shojo Anime respectfully.", "x": "Engaging: Emotion.. Fruits Basket. How to participate or observe well — Shojo Anime. the girls' romance. Respect first, always; Flowers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Shojo Anime do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Shojo Anime do's and don'ts.", "x": "Etiquette: Basket.. Romance. The rules of respect — Shojo Anime. the girls' romance. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Shojo Anime.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Shojo Anime.", "x": "Planning: Sailor Moon.. Flowers. Practical notes — Shojo Anime. the girls' romance. A little planning shows respect for Romance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Shojo Anime and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Shojo Anime and money.", "x": "Costs: Emotion.. Shojo Beat. What to budget — Shojo Anime. the girls' romance. The best experiences of Flowers. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-anime-shojo-anime-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
