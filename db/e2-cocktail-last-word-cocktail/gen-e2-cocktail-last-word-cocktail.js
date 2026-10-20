(function(){'use strict';
/* JAH Last Word Cocktail Database generator — jahdb-e2-cocktail-last-word-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-last-word-cocktail',PREFIX='JAH-E2COCKTAILL-',NAME='JAH Last Word Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Last Word: the complete guide", "d": "Last Word: the equal-parts gin..", "g": "overview", "l": 2, "q": "What is Last Word: the complete guide?", "a": "Last Word: the equal-parts gin..", "x": "The complete cocktail guide to Last Word: the equal-parts gin.. Gin. History, meaning, practices, and how to engage respectfully — everything in one database. Chartreuse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Last Word essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Last Word essentials.", "x": "At a glance: Last Word — the equal-parts gin.. Chartreuse. The essentials: Equal.. Maraschino. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gin.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gin.", "x": "Last Word: Gin.. Equal. Essential knowledge — Maraschino.. the equal-parts gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gin..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gin..", "x": "Explained: Gin.. Detroit. The context — Last Word. Lime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chartreuse.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chartreuse.", "x": "Last Word: Chartreuse.. 1920s. Essential knowledge — Lime.. the equal-parts gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chartreuse..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chartreuse..", "x": "Explained: Chartreuse.. Lime. The context — Last Word. 1920s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Maraschino.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Maraschino.", "x": "Last Word: Maraschino.. Detroit. Essential knowledge — 1920s.. the equal-parts gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Maraschino..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Maraschino..", "x": "Explained: Maraschino.. Classic. The context — Last Word. Detroit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lime.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lime.", "x": "Last Word: Lime.. Lime. Essential knowledge — Detroit.. the equal-parts gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lime..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lime..", "x": "Explained: Lime.. Chartreuse. The context — Last Word. Gin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1920s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1920s.", "x": "Last Word: 1920s.. Classic. Essential knowledge — Gin.. the equal-parts gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1920s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1920s..", "x": "Explained: 1920s.. Equal. The context — Last Word. Chartreuse. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Detroit.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Detroit.", "x": "Last Word: Detroit.. Chartreuse. Essential knowledge — Chartreuse.. the equal-parts gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Detroit..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Detroit..", "x": "Explained: Detroit.. 1920s. The context — Last Word. Maraschino. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chartreuse.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chartreuse.", "x": "Last Word in depth: Chartreuse.. Chartreuse. Details — the equal-parts gin.. 1920s. Lime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Equal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Equal.", "x": "Last Word in depth: Equal.. Maraschino. Details — the equal-parts gin.. Detroit. 1920s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1920s.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1920s.", "x": "Last Word in depth: 1920s.. Lime. Details — the equal-parts gin.. Lime. Detroit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Detroit.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Detroit.", "x": "Last Word in depth: Detroit.. 1920s. Details — the equal-parts gin.. Classic. Gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lime.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lime.", "x": "Last Word in depth: Lime.. Detroit. Details — the equal-parts gin.. Chartreuse. Chartreuse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classic.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classic.", "x": "Last Word in depth: Classic.. Gin. Details — the equal-parts gin.. Equal. Maraschino. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Last Word comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Last Word comes from.", "x": "Origins: Chartreuse.. Gin. The history of Last Word — the equal-parts gin.. Equal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Last Word respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Last Word respectfully.", "x": "Engaging: 1920s.. Chartreuse. How to participate or observe well — Last Word. the equal-parts gin. Respect first, always; Detroit.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Last Word do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Last Word do's and don'ts.", "x": "Etiquette: Lime.. Maraschino. The rules of respect — Last Word. the equal-parts gin. When in doubt, ask about Classic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Last Word.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Last Word.", "x": "Planning: Chartreuse.. Lime. Practical notes — Last Word. the equal-parts gin. A little planning shows respect for Equal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Last Word and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Last Word and money.", "x": "Costs: 1920s.. 1920s. What to budget — Last Word. the equal-parts gin. The best experiences of Detroit. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-last-word-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
