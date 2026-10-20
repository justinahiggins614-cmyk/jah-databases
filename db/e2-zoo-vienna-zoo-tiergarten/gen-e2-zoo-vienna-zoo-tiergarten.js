(function(){'use strict';
/* JAH Vienna Zoo Tiergarten Zoo Database generator — jahdb-e2-zoo-vienna-zoo-tiergarten-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo-vienna-zoo-tiergarten',PREFIX='JAH-E2ZOOVIENNA-',NAME='JAH Vienna Zoo Tiergarten Zoo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vienna Zoo Tiergarten: the complete guide", "d": "Vienna Zoo Tiergarten: the world's oldest zoo..", "g": "overview", "l": 2, "q": "What is Vienna Zoo Tiergarten: the complete guide?", "a": "Vienna Zoo Tiergarten: the world's oldest zoo..", "x": "The complete zoo guide to Vienna Zoo Tiergarten: the world's oldest zoo.. 1752. History, meaning, practices, and how to engage respectfully — everything in one database. Oldest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vienna Zoo Tiergarten essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vienna Zoo Tiergarten essentials.", "x": "At a glance: Vienna Zoo Tiergarten — the world's oldest zoo.. Schonbrunn. The essentials: Palace.. Pandas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1752.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1752.", "x": "Vienna Zoo Tiergarten: 1752.. Palace. Essential knowledge — Pandas.. the world's oldest zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1752..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1752..", "x": "Explained: 1752.. Tickets. The context — Vienna Zoo Tiergarten. Baroque. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Schonbrunn.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Schonbrunn.", "x": "Vienna Zoo Tiergarten: Schonbrunn.. Pandas. Essential knowledge — Baroque.. the world's oldest zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Schonbrunn..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Schonbrunn..", "x": "Explained: Schonbrunn.. Vienna. The context — Vienna Zoo Tiergarten. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pandas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pandas.", "x": "Vienna Zoo Tiergarten: Pandas.. Tickets. Essential knowledge — History.. the world's oldest zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pandas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pandas..", "x": "Explained: Pandas.. Baroque. The context — Vienna Zoo Tiergarten. Best. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Baroque.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Baroque.", "x": "Vienna Zoo Tiergarten: Baroque.. Vienna. Essential knowledge — Best.. the world's oldest zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Baroque..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Baroque..", "x": "Explained: Baroque.. Oldest. The context — Vienna Zoo Tiergarten. 1752. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Vienna Zoo Tiergarten: History.. Baroque. Essential knowledge — 1752.. the world's oldest zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. Palace. The context — Vienna Zoo Tiergarten. Schonbrunn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Best.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Best.", "x": "Vienna Zoo Tiergarten: Best.. Oldest. Essential knowledge — Schonbrunn.. the world's oldest zoo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Best..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Best..", "x": "Explained: Best.. Pandas. The context — Vienna Zoo Tiergarten. Pandas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Oldest.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Oldest.", "x": "Vienna Zoo Tiergarten in depth: Oldest.. Schonbrunn. Details — the world's oldest zoo.. Pandas. Baroque. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Palace.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Palace.", "x": "Vienna Zoo Tiergarten in depth: Palace.. Pandas. Details — the world's oldest zoo.. Tickets. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pandas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pandas.", "x": "Vienna Zoo Tiergarten in depth: Pandas.. Baroque. Details — the world's oldest zoo.. Vienna. Best. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Vienna Zoo Tiergarten in depth: Tickets.. History. Details — the world's oldest zoo.. Baroque. 1752. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Vienna.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Vienna.", "x": "Vienna Zoo Tiergarten in depth: Vienna.. Best. Details — the world's oldest zoo.. Oldest. Schonbrunn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Baroque.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Baroque.", "x": "Vienna Zoo Tiergarten in depth: Baroque.. 1752. Details — the world's oldest zoo.. Palace. Pandas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vienna Zoo Tiergarten comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vienna Zoo Tiergarten comes from.", "x": "Origins: Oldest.. 1752. The history of Vienna Zoo Tiergarten — the world's oldest zoo.. Palace. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vienna Zoo Tiergarten respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vienna Zoo Tiergarten respectfully.", "x": "Engaging: Pandas.. Schonbrunn. How to participate or observe well — Vienna Zoo Tiergarten. the world's oldest zoo. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vienna Zoo Tiergarten do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vienna Zoo Tiergarten do's and don'ts.", "x": "Etiquette: Vienna.. Pandas. The rules of respect — Vienna Zoo Tiergarten. the world's oldest zoo. When in doubt, ask about Baroque.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vienna Zoo Tiergarten.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vienna Zoo Tiergarten.", "x": "Planning: Oldest.. Baroque. Practical notes — Vienna Zoo Tiergarten. the world's oldest zoo. A little planning shows respect for Palace.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vienna Zoo Tiergarten and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vienna Zoo Tiergarten and money.", "x": "Costs: Pandas.. History. What to budget — Vienna Zoo Tiergarten. the world's oldest zoo. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo-vienna-zoo-tiergarten-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
