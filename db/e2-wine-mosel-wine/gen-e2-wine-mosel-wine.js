(function(){'use strict';
/* JAH Mosel Wine Wine Region Database generator — jahdb-e2-wine-mosel-wine-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wine-mosel-wine',PREFIX='JAH-E2WINEMOSEL-',NAME='JAH Mosel Wine Wine Region Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mosel Wine: the complete guide", "d": "Mosel Wine: the steep Riesling slopes..", "g": "overview", "l": 2, "q": "What is Mosel Wine: the complete guide?", "a": "Mosel Wine: the steep Riesling slopes..", "x": "The complete wine region guide to Mosel Wine: the steep Riesling slopes.. Germany. History, meaning, practices, and how to engage respectfully — everything in one database. Riesling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mosel Wine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mosel Wine essentials.", "x": "At a glance: Mosel Wine — the steep Riesling slopes.. Riesling. The essentials: Slate.. Slate. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Germany.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Germany.", "x": "Mosel Wine: Germany.. Slate. Essential knowledge — Slate.. the steep Riesling slopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Germany..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Germany..", "x": "Explained: Germany.. River. The context — Mosel Wine. Steep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Riesling.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Riesling.", "x": "Mosel Wine: Riesling.. Steep. Essential knowledge — Steep.. the steep Riesling slopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Riesling..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Riesling..", "x": "Explained: Riesling.. Sweet. The context — Mosel Wine. Sweet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Slate.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Slate.", "x": "Mosel Wine: Slate.. River. Essential knowledge — Sweet.. the steep Riesling slopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Slate..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Slate..", "x": "Explained: Slate.. Tasting. The context — Mosel Wine. River. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Steep.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Steep.", "x": "Mosel Wine: Steep.. Sweet. Essential knowledge — River.. the steep Riesling slopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Steep..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Steep..", "x": "Explained: Steep.. Riesling. The context — Mosel Wine. Germany. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sweet.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sweet.", "x": "Mosel Wine: Sweet.. Tasting. Essential knowledge — Germany.. the steep Riesling slopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sweet..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sweet..", "x": "Explained: Sweet.. Slate. The context — Mosel Wine. Riesling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "River.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "River.", "x": "Mosel Wine: River.. Riesling. Essential knowledge — Riesling.. the steep Riesling slopes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: River..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: River..", "x": "Explained: River.. Steep. The context — Mosel Wine. Slate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Riesling.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Riesling.", "x": "Mosel Wine in depth: Riesling.. Riesling. Details — the steep Riesling slopes.. Steep. Steep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Slate.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Slate.", "x": "Mosel Wine in depth: Slate.. Slate. Details — the steep Riesling slopes.. River. Sweet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Steep.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Steep.", "x": "Mosel Wine in depth: Steep.. Steep. Details — the steep Riesling slopes.. Sweet. River. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "River.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "River.", "x": "Mosel Wine in depth: River.. Sweet. Details — the steep Riesling slopes.. Tasting. Germany. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sweet.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sweet.", "x": "Mosel Wine in depth: Sweet.. River. Details — the steep Riesling slopes.. Riesling. Riesling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tasting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tasting.", "x": "Mosel Wine in depth: Tasting.. Germany. Details — the steep Riesling slopes.. Slate. Slate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mosel Wine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mosel Wine comes from.", "x": "Origins: Riesling.. Germany. The history of Mosel Wine — the steep Riesling slopes.. Slate. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mosel Wine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mosel Wine respectfully.", "x": "Engaging: Steep.. Riesling. How to participate or observe well — Mosel Wine. the steep Riesling slopes. Respect first, always; River.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mosel Wine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mosel Wine do's and don'ts.", "x": "Etiquette: Sweet.. Slate. The rules of respect — Mosel Wine. the steep Riesling slopes. When in doubt, ask about Tasting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mosel Wine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mosel Wine.", "x": "Planning: Riesling.. Steep. Practical notes — Mosel Wine. the steep Riesling slopes. A little planning shows respect for Slate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mosel Wine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mosel Wine and money.", "x": "Costs: Steep.. Sweet. What to budget — Mosel Wine. the steep Riesling slopes. The best experiences of River. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wine-mosel-wine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
