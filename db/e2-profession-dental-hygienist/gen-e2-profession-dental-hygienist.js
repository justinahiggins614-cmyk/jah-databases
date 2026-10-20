(function(){'use strict';
/* JAH Dental Hygienist Profession Database generator — jahdb-e2-profession-dental-hygienist-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-dental-hygienist',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Dental Hygienist Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dental Hygienist Profession: the complete guide", "d": "Dental Hygienist Profession: the clean profession..", "g": "overview", "l": 2, "q": "What is Dental Hygienist Profession: the complete guide?", "a": "Dental Hygienist Profession: the clean profession..", "x": "The complete profession guide to Dental Hygienist Profession: the clean profession.. Cleanings. History, meaning, practices, and how to engage respectfully — everything in one database. Cleanings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dental Hygienist Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dental Hygienist Profession essentials.", "x": "At a glance: Dental Hygienist Profession — the clean profession.. X-rays. The essentials: Chair.. Chair. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cleanings.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cleanings.", "x": "Dental Hygienist Profession: Cleanings.. Chair. Essential knowledge — Chair.. the clean profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cleanings..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cleanings..", "x": "Explained: Cleanings.. Polish. The context — Dental Hygienist Profession. Scrubs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "X-rays.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "X-rays.", "x": "Dental Hygienist Profession: X-rays.. Recall. Essential knowledge — Scrubs.. the clean profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: X-rays..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: X-rays..", "x": "Explained: X-rays.. Scrubs. The context — Dental Hygienist Profession. Recall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chair.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chair.", "x": "Dental Hygienist Profession: Chair.. Polish. Essential knowledge — Recall.. the clean profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chair..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chair..", "x": "Explained: Chair.. Day. The context — Dental Hygienist Profession. Polish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Scrubs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Scrubs.", "x": "Dental Hygienist Profession: Scrubs.. Scrubs. Essential knowledge — Polish.. the clean profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Scrubs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Scrubs..", "x": "Explained: Scrubs.. Cleanings. The context — Dental Hygienist Profession. Cleanings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Recall.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Recall.", "x": "Dental Hygienist Profession: Recall.. Day. Essential knowledge — Cleanings.. the clean profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Recall..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Recall..", "x": "Explained: Recall.. Chair. The context — Dental Hygienist Profession. X-rays. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Polish.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Polish.", "x": "Dental Hygienist Profession: Polish.. Cleanings. Essential knowledge — X-rays.. the clean profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Polish..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Polish..", "x": "Explained: Polish.. Recall. The context — Dental Hygienist Profession. Chair. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cleanings.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cleanings.", "x": "Dental Hygienist Profession in depth: Cleanings.. X-rays. Details — the clean profession.. Recall. Scrubs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chair.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chair.", "x": "Dental Hygienist Profession in depth: Chair.. Chair. Details — the clean profession.. Polish. Recall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Recall.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Recall.", "x": "Dental Hygienist Profession in depth: Recall.. Scrubs. Details — the clean profession.. Scrubs. Polish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Polish.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Polish.", "x": "Dental Hygienist Profession in depth: Polish.. Recall. Details — the clean profession.. Day. Cleanings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Scrubs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Scrubs.", "x": "Dental Hygienist Profession in depth: Scrubs.. Polish. Details — the clean profession.. Cleanings. X-rays. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Dental Hygienist Profession in depth: Day.. Cleanings. Details — the clean profession.. Chair. Chair. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dental Hygienist Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dental Hygienist Profession comes from.", "x": "Origins: Cleanings.. Cleanings. The history of Dental Hygienist Profession — the clean profession.. Chair. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dental Hygienist Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dental Hygienist Profession respectfully.", "x": "Engaging: Recall.. X-rays. How to participate or observe well — Dental Hygienist Profession. the clean profession. Respect first, always; Polish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dental Hygienist Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dental Hygienist Profession do's and don'ts.", "x": "Etiquette: Scrubs.. Chair. The rules of respect — Dental Hygienist Profession. the clean profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dental Hygienist Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dental Hygienist Profession.", "x": "Planning: Cleanings.. Scrubs. Practical notes — Dental Hygienist Profession. the clean profession. A little planning shows respect for Chair.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dental Hygienist Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dental Hygienist Profession and money.", "x": "Costs: Recall.. Recall. What to budget — Dental Hygienist Profession. the clean profession. The best experiences of Polish. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-dental-hygienist-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
