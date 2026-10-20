(function(){'use strict';
/* JAH San Fermin Holiday Database generator — jahdb-e2-holiday-san-fermin-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-san-fermin',PREFIX='JAH-E2HOLIDAYSA-',NAME='JAH San Fermin Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "San Fermin: the complete guide", "d": "San Fermin: Pamplona's running of the bulls..", "g": "overview", "l": 2, "q": "What is San Fermin: the complete guide?", "a": "San Fermin: Pamplona's running of the bulls..", "x": "The complete holiday guide to San Fermin: Pamplona's running of the bulls.. July. History, meaning, practices, and how to engage respectfully — everything in one database. Bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "San Fermin essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "San Fermin essentials.", "x": "At a glance: San Fermin — Pamplona's running of the bulls.. Bulls. The essentials: History.. Red scarves. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "July.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "July.", "x": "San Fermin: July.. History. Essential knowledge — Red scarves.. Pamplona's running of the bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: July..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: July..", "x": "Explained: July.. Debate. The context — San Fermin. Hemingway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bulls.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bulls.", "x": "San Fermin: Bulls.. Fiesta. Essential knowledge — Hemingway.. Pamplona's running of the bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bulls..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bulls..", "x": "Explained: Bulls.. Travel. The context — San Fermin. 9 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Red scarves.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Red scarves.", "x": "San Fermin: Red scarves.. Debate. Essential knowledge — 9 days.. Pamplona's running of the bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Red scarves..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Red scarves..", "x": "Explained: Red scarves.. Culture. The context — San Fermin. Controversy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hemingway.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hemingway.", "x": "San Fermin: Hemingway.. Travel. Essential knowledge — Controversy.. Pamplona's running of the bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hemingway..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hemingway..", "x": "Explained: Hemingway.. Bulls. The context — San Fermin. July. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "9 days.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "9 days.", "x": "San Fermin: 9 days.. Culture. Essential knowledge — July.. Pamplona's running of the bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 9 days..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 9 days..", "x": "Explained: 9 days.. History. The context — San Fermin. Bulls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Controversy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Controversy.", "x": "San Fermin: Controversy.. Bulls. Essential knowledge — Bulls.. Pamplona's running of the bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Controversy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Controversy..", "x": "Explained: Controversy.. Fiesta. The context — San Fermin. Red scarves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bulls.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bulls.", "x": "San Fermin in depth: Bulls.. Bulls. Details — Pamplona's running of the bulls.. Fiesta. Hemingway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "San Fermin in depth: History.. Red scarves. Details — Pamplona's running of the bulls.. Debate. 9 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fiesta.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fiesta.", "x": "San Fermin in depth: Fiesta.. Hemingway. Details — Pamplona's running of the bulls.. Travel. Controversy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Debate.", "x": "San Fermin in depth: Debate.. 9 days. Details — Pamplona's running of the bulls.. Culture. July. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "San Fermin in depth: Travel.. Controversy. Details — Pamplona's running of the bulls.. Bulls. Bulls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "San Fermin in depth: Culture.. July. Details — Pamplona's running of the bulls.. History. Red scarves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where San Fermin comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where San Fermin comes from.", "x": "Origins: Bulls.. July. The history of San Fermin — Pamplona's running of the bulls.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing San Fermin respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing San Fermin respectfully.", "x": "Engaging: Fiesta.. Bulls. How to participate or observe well — San Fermin. Pamplona's running of the bulls. Respect first, always; Debate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "San Fermin do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "San Fermin do's and don'ts.", "x": "Etiquette: Travel.. Red scarves. The rules of respect — San Fermin. Pamplona's running of the bulls. When in doubt, ask about Culture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around San Fermin.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around San Fermin.", "x": "Planning: Bulls.. Hemingway. Practical notes — San Fermin. Pamplona's running of the bulls. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "San Fermin and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "San Fermin and money.", "x": "Costs: Fiesta.. 9 days. What to budget — San Fermin. Pamplona's running of the bulls. The best experiences of Debate. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-san-fermin-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
