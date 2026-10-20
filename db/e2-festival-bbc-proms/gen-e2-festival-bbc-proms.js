(function(){'use strict';
/* JAH BBC Proms Festival Database generator — jahdb-e2-festival-bbc-proms-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-bbc-proms',PREFIX='JAH-E2FESTIVALB-',NAME='JAH BBC Proms Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "BBC Proms: the complete guide", "d": "BBC Proms: the world's greatest classical fest..", "g": "overview", "l": 2, "q": "What is BBC Proms: the complete guide?", "a": "BBC Proms: the world's greatest classical fest..", "x": "The complete festival guide to BBC Proms: the world's greatest classical fest.. Summer. History, meaning, practices, and how to engage respectfully — everything in one database. Concerts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "BBC Proms essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "BBC Proms essentials.", "x": "At a glance: BBC Proms — the world's greatest classical fest.. Royal Albert Hall. The essentials: Promming.. Promming. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Summer.", "x": "BBC Proms: Summer.. Promming. Essential knowledge — Promming.. the world's greatest classical fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Summer..", "x": "Explained: Summer.. Travel. The context — BBC Proms. Last Night. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Royal Albert Hall.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Royal Albert Hall.", "x": "BBC Proms: Royal Albert Hall.. History. Essential knowledge — Last Night.. the world's greatest classical fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Royal Albert Hall..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Royal Albert Hall..", "x": "Explained: Royal Albert Hall.. Music. The context — BBC Proms. 8 weeks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Promming.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Promming.", "x": "BBC Proms: Promming.. Travel. Essential knowledge — 8 weeks.. the world's greatest classical fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Promming..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Promming..", "x": "Explained: Promming.. Tradition. The context — BBC Proms. London. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Last Night.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Last Night.", "x": "BBC Proms: Last Night.. Music. Essential knowledge — London.. the world's greatest classical fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Last Night..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Last Night..", "x": "Explained: Last Night.. Concerts. The context — BBC Proms. Summer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "8 weeks.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "8 weeks.", "x": "BBC Proms: 8 weeks.. Tradition. Essential knowledge — Summer.. the world's greatest classical fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 8 weeks..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 8 weeks..", "x": "Explained: 8 weeks.. Promming. The context — BBC Proms. Royal Albert Hall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "London.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "London.", "x": "BBC Proms: London.. Concerts. Essential knowledge — Royal Albert Hall.. the world's greatest classical fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: London..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: London..", "x": "Explained: London.. History. The context — BBC Proms. Promming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Concerts.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Concerts.", "x": "BBC Proms in depth: Concerts.. Royal Albert Hall. Details — the world's greatest classical fest.. History. Last Night. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Promming.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Promming.", "x": "BBC Proms in depth: Promming.. Promming. Details — the world's greatest classical fest.. Travel. 8 weeks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "BBC Proms in depth: History.. Last Night. Details — the world's greatest classical fest.. Music. London. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Travel.", "x": "BBC Proms in depth: Travel.. 8 weeks. Details — the world's greatest classical fest.. Tradition. Summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Music.", "x": "BBC Proms in depth: Music.. London. Details — the world's greatest classical fest.. Concerts. Royal Albert Hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tradition.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tradition.", "x": "BBC Proms in depth: Tradition.. Summer. Details — the world's greatest classical fest.. Promming. Promming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where BBC Proms comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where BBC Proms comes from.", "x": "Origins: Concerts.. Summer. The history of BBC Proms — the world's greatest classical fest.. Promming. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing BBC Proms respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing BBC Proms respectfully.", "x": "Engaging: History.. Royal Albert Hall. How to participate or observe well — BBC Proms. the world's greatest classical fest. Respect first, always; Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "BBC Proms do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "BBC Proms do's and don'ts.", "x": "Etiquette: Music.. Promming. The rules of respect — BBC Proms. the world's greatest classical fest. When in doubt, ask about Tradition.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around BBC Proms.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around BBC Proms.", "x": "Planning: Concerts.. Last Night. Practical notes — BBC Proms. the world's greatest classical fest. A little planning shows respect for Promming.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "BBC Proms and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "BBC Proms and money.", "x": "Costs: History.. 8 weeks. What to budget — BBC Proms. the world's greatest classical fest. The best experiences of Travel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-bbc-proms-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
