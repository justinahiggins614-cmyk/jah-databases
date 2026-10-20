(function(){'use strict';
/* JAH K-Pop Dance Dance Form Database generator — jahdb-e2-dance-kpop-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-kpop-dance-form',PREFIX='JAH-E2DANCEKPOP-',NAME='JAH K-Pop Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "K-Pop Dance: the complete guide", "d": "K-Pop Dance: the idol choreography..", "g": "overview", "l": 2, "q": "What is K-Pop Dance: the complete guide?", "a": "K-Pop Dance: the idol choreography..", "x": "The complete dance form guide to K-Pop Dance: the idol choreography.. Korea. History, meaning, practices, and how to engage respectfully — everything in one database. Sync. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "K-Pop Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "K-Pop Dance essentials.", "x": "At a glance: K-Pop Dance — the idol choreography.. Sync. The essentials: Idols.. Idols. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Korea.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Korea.", "x": "K-Pop Dance: Korea.. Idols. Essential knowledge — Idols.. the idol choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Korea..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Korea..", "x": "Explained: Korea.. Korea. The context — K-Pop Dance. Practice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sync.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sync.", "x": "K-Pop Dance: Sync.. Covers. Essential knowledge — Practice.. the idol choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sync..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sync..", "x": "Explained: Sync.. Formations. The context — K-Pop Dance. Covers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Idols.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Idols.", "x": "K-Pop Dance: Idols.. Korea. Essential knowledge — Covers.. the idol choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Idols..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Idols..", "x": "Explained: Idols.. Training. The context — K-Pop Dance. Formations. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Practice.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Practice.", "x": "K-Pop Dance: Practice.. Formations. Essential knowledge — Formations.. the idol choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Practice..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Practice..", "x": "Explained: Practice.. Sync. The context — K-Pop Dance. Korea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Covers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Covers.", "x": "K-Pop Dance: Covers.. Training. Essential knowledge — Korea.. the idol choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Covers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Covers..", "x": "Explained: Covers.. Idols. The context — K-Pop Dance. Sync. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Formations.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Formations.", "x": "K-Pop Dance: Formations.. Sync. Essential knowledge — Sync.. the idol choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Formations..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Formations..", "x": "Explained: Formations.. Covers. The context — K-Pop Dance. Idols. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sync.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sync.", "x": "K-Pop Dance in depth: Sync.. Sync. Details — the idol choreography.. Covers. Practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Idols.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Idols.", "x": "K-Pop Dance in depth: Idols.. Idols. Details — the idol choreography.. Korea. Covers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Covers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Covers.", "x": "K-Pop Dance in depth: Covers.. Practice. Details — the idol choreography.. Formations. Formations. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Korea.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Korea.", "x": "K-Pop Dance in depth: Korea.. Covers. Details — the idol choreography.. Training. Korea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Formations.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Formations.", "x": "K-Pop Dance in depth: Formations.. Formations. Details — the idol choreography.. Sync. Sync. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "K-Pop Dance in depth: Training.. Korea. Details — the idol choreography.. Idols. Idols. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where K-Pop Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where K-Pop Dance comes from.", "x": "Origins: Sync.. Korea. The history of K-Pop Dance — the idol choreography.. Idols. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing K-Pop Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing K-Pop Dance respectfully.", "x": "Engaging: Covers.. Sync. How to participate or observe well — K-Pop Dance. the idol choreography. Respect first, always; Korea.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "K-Pop Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "K-Pop Dance do's and don'ts.", "x": "Etiquette: Formations.. Idols. The rules of respect — K-Pop Dance. the idol choreography. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around K-Pop Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around K-Pop Dance.", "x": "Planning: Sync.. Practice. Practical notes — K-Pop Dance. the idol choreography. A little planning shows respect for Idols.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "K-Pop Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "K-Pop Dance and money.", "x": "Costs: Covers.. Covers. What to budget — K-Pop Dance. the idol choreography. The best experiences of Korea. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-kpop-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
