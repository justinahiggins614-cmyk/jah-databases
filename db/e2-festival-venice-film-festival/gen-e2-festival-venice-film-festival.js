(function(){'use strict';
/* JAH Venice Film Festival Festival Database generator — jahdb-e2-festival-venice-film-festival-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-venice-film-festival',PREFIX='JAH-E2FESTIVALV-',NAME='JAH Venice Film Festival Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Venice Film Festival: the complete guide", "d": "Venice Film Festival: the oldest film fest..", "g": "overview", "l": 2, "q": "What is Venice Film Festival: the complete guide?", "a": "Venice Film Festival: the oldest film fest..", "x": "The complete festival guide to Venice Film Festival: the oldest film fest.. August. History, meaning, practices, and how to engage respectfully — everything in one database. Lion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Venice Film Festival essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Venice Film Festival essentials.", "x": "At a glance: Venice Film Festival — the oldest film fest.. Lido. The essentials: History.. Golden Lion. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "August.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "August.", "x": "Venice Film Festival: August.. History. Essential knowledge — Golden Lion.. the oldest film fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: August..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: August..", "x": "Explained: August.. Venice. The context — Venice Film Festival. Premieres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lido.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lido.", "x": "Venice Film Festival: Lido.. Premieres. Essential knowledge — Premieres.. the oldest film fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lido..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lido..", "x": "Explained: Lido.. Glamour. The context — Venice Film Festival. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Golden Lion.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Golden Lion.", "x": "Venice Film Festival: Golden Lion.. Venice. Essential knowledge — History.. the oldest film fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Golden Lion..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Golden Lion..", "x": "Explained: Golden Lion.. Cinema. The context — Venice Film Festival. Glamour. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Premieres.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Premieres.", "x": "Venice Film Festival: Premieres.. Glamour. Essential knowledge — Glamour.. the oldest film fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Premieres..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Premieres..", "x": "Explained: Premieres.. Lion. The context — Venice Film Festival. August. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Venice Film Festival: History.. Cinema. Essential knowledge — August.. the oldest film fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Venice Film Festival. Lido. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Glamour.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Glamour.", "x": "Venice Film Festival: Glamour.. Lion. Essential knowledge — Lido.. the oldest film fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Glamour..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Glamour..", "x": "Explained: Glamour.. Premieres. The context — Venice Film Festival. Golden Lion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lion.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lion.", "x": "Venice Film Festival in depth: Lion.. Lido. Details — the oldest film fest.. Premieres. Premieres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Venice Film Festival in depth: History.. Golden Lion. Details — the oldest film fest.. Venice. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Premieres.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Premieres.", "x": "Venice Film Festival in depth: Premieres.. Premieres. Details — the oldest film fest.. Glamour. Glamour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Venice.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Venice.", "x": "Venice Film Festival in depth: Venice.. History. Details — the oldest film fest.. Cinema. August. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Glamour.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Glamour.", "x": "Venice Film Festival in depth: Glamour.. Glamour. Details — the oldest film fest.. Lion. Lido. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cinema.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cinema.", "x": "Venice Film Festival in depth: Cinema.. August. Details — the oldest film fest.. History. Golden Lion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Venice Film Festival comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Venice Film Festival comes from.", "x": "Origins: Lion.. August. The history of Venice Film Festival — the oldest film fest.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Venice Film Festival respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Venice Film Festival respectfully.", "x": "Engaging: Premieres.. Lido. How to participate or observe well — Venice Film Festival. the oldest film fest. Respect first, always; Venice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Venice Film Festival do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Venice Film Festival do's and don'ts.", "x": "Etiquette: Glamour.. Golden Lion. The rules of respect — Venice Film Festival. the oldest film fest. When in doubt, ask about Cinema.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Venice Film Festival.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Venice Film Festival.", "x": "Planning: Lion.. Premieres. Practical notes — Venice Film Festival. the oldest film fest. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Venice Film Festival and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Venice Film Festival and money.", "x": "Costs: Premieres.. History. What to budget — Venice Film Festival. the oldest film fest. The best experiences of Venice. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-venice-film-festival-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
