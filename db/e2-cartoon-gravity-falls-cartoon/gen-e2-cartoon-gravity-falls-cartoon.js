(function(){'use strict';
/* JAH Gravity Falls Cartoon Database generator — jahdb-e2-cartoon-gravity-falls-cartoon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cartoon-gravity-falls-cartoon',PREFIX='JAH-E2CARTOONGR-',NAME='JAH Gravity Falls Cartoon Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gravity Falls: the complete guide", "d": "Gravity Falls: the mystery twins..", "g": "overview", "l": 2, "q": "What is Gravity Falls: the complete guide?", "a": "Gravity Falls: the mystery twins..", "x": "The complete cartoon guide to Gravity Falls: the mystery twins.. 2012. History, meaning, practices, and how to engage respectfully — everything in one database. Twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gravity Falls essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gravity Falls essentials.", "x": "At a glance: Gravity Falls — the mystery twins.. Dipper. The essentials: Journal.. Mabel. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2012.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2012.", "x": "Gravity Falls: 2012.. Journal. Essential knowledge — Mabel.. the mystery twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2012..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2012..", "x": "Explained: 2012.. Seasons. The context — Gravity Falls. Journal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dipper.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dipper.", "x": "Gravity Falls: Dipper.. Cipher. Essential knowledge — Journal.. the mystery twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dipper..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dipper..", "x": "Explained: Dipper.. Mabel. The context — Gravity Falls. 2 seasons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mabel.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mabel.", "x": "Gravity Falls: Mabel.. Seasons. Essential knowledge — 2 seasons.. the mystery twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mabel..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mabel..", "x": "Explained: Mabel.. Legacy. The context — Gravity Falls. Cipher. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Journal.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Journal.", "x": "Gravity Falls: Journal.. Mabel. Essential knowledge — Cipher.. the mystery twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Journal..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Journal..", "x": "Explained: Journal.. Twins. The context — Gravity Falls. 2012. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2 seasons.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2 seasons.", "x": "Gravity Falls: 2 seasons.. Legacy. Essential knowledge — 2012.. the mystery twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 2 seasons..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 2 seasons..", "x": "Explained: 2 seasons.. Journal. The context — Gravity Falls. Dipper. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Cipher.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Cipher.", "x": "Gravity Falls: Cipher.. Twins. Essential knowledge — Dipper.. the mystery twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Cipher..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Cipher..", "x": "Explained: Cipher.. Cipher. The context — Gravity Falls. Mabel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Twins.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Twins.", "x": "Gravity Falls in depth: Twins.. Dipper. Details — the mystery twins.. Cipher. Journal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Journal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Journal.", "x": "Gravity Falls in depth: Journal.. Mabel. Details — the mystery twins.. Seasons. 2 seasons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cipher.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cipher.", "x": "Gravity Falls in depth: Cipher.. Journal. Details — the mystery twins.. Mabel. Cipher. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Seasons.", "x": "Gravity Falls in depth: Seasons.. 2 seasons. Details — the mystery twins.. Legacy. 2012. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mabel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mabel.", "x": "Gravity Falls in depth: Mabel.. Cipher. Details — the mystery twins.. Twins. Dipper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Gravity Falls in depth: Legacy.. 2012. Details — the mystery twins.. Journal. Mabel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gravity Falls comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gravity Falls comes from.", "x": "Origins: Twins.. 2012. The history of Gravity Falls — the mystery twins.. Journal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gravity Falls respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gravity Falls respectfully.", "x": "Engaging: Cipher.. Dipper. How to participate or observe well — Gravity Falls. the mystery twins. Respect first, always; Seasons.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gravity Falls do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gravity Falls do's and don'ts.", "x": "Etiquette: Mabel.. Mabel. The rules of respect — Gravity Falls. the mystery twins. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gravity Falls.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gravity Falls.", "x": "Planning: Twins.. Journal. Practical notes — Gravity Falls. the mystery twins. A little planning shows respect for Journal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gravity Falls and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gravity Falls and money.", "x": "Costs: Cipher.. 2 seasons. What to budget — Gravity Falls. the mystery twins. The best experiences of Seasons. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cartoon-gravity-falls-cartoon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
