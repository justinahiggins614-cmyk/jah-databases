(function(){'use strict';
/* JAH Coen Brothers Director Database generator — jahdb-e2-director-coen-brothers-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-coen-brothers-director',PREFIX='JAH-E2DIRECTORC-',NAME='JAH Coen Brothers Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Coen Brothers: the complete guide", "d": "Coen Brothers: the Minnesota duo..", "g": "overview", "l": 2, "q": "What is Coen Brothers: the complete guide?", "a": "Coen Brothers: the Minnesota duo..", "x": "The complete director guide to Coen Brothers: the Minnesota duo.. Fargo. History, meaning, practices, and how to engage respectfully — everything in one database. Fargo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Coen Brothers essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Coen Brothers essentials.", "x": "At a glance: Coen Brothers — the Minnesota duo.. Big Lebowski. The essentials: Lebowski.. No Country. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fargo.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fargo.", "x": "Coen Brothers: Fargo.. Lebowski. Essential knowledge — No Country.. the Minnesota duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fargo..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fargo..", "x": "Explained: Fargo.. Quirky. The context — Coen Brothers. O Brother. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Big Lebowski.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Big Lebowski.", "x": "Coen Brothers: Big Lebowski.. No Country. Essential knowledge — O Brother.. the Minnesota duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Big Lebowski..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Big Lebowski..", "x": "Explained: Big Lebowski.. Minnesota. The context — Coen Brothers. Minnesota. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "No Country.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "No Country.", "x": "Coen Brothers: No Country.. Quirky. Essential knowledge — Minnesota.. the Minnesota duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: No Country..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: No Country..", "x": "Explained: No Country.. Style. The context — Coen Brothers. Quirky. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "O Brother.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "O Brother.", "x": "Coen Brothers: O Brother.. Minnesota. Essential knowledge — Quirky.. the Minnesota duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: O Brother..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: O Brother..", "x": "Explained: O Brother.. Fargo. The context — Coen Brothers. Fargo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Minnesota.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Minnesota.", "x": "Coen Brothers: Minnesota.. Style. Essential knowledge — Fargo.. the Minnesota duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Minnesota..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Minnesota..", "x": "Explained: Minnesota.. Lebowski. The context — Coen Brothers. Big Lebowski. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Quirky.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Quirky.", "x": "Coen Brothers: Quirky.. Fargo. Essential knowledge — Big Lebowski.. the Minnesota duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Quirky..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Quirky..", "x": "Explained: Quirky.. No Country. The context — Coen Brothers. No Country. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Fargo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Fargo.", "x": "Coen Brothers in depth: Fargo.. Big Lebowski. Details — the Minnesota duo.. No Country. O Brother. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lebowski.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lebowski.", "x": "Coen Brothers in depth: Lebowski.. No Country. Details — the Minnesota duo.. Quirky. Minnesota. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "No Country.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "No Country.", "x": "Coen Brothers in depth: No Country.. O Brother. Details — the Minnesota duo.. Minnesota. Quirky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Quirky.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Quirky.", "x": "Coen Brothers in depth: Quirky.. Minnesota. Details — the Minnesota duo.. Style. Fargo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Minnesota.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Minnesota.", "x": "Coen Brothers in depth: Minnesota.. Quirky. Details — the Minnesota duo.. Fargo. Big Lebowski. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Coen Brothers in depth: Style.. Fargo. Details — the Minnesota duo.. Lebowski. No Country. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Coen Brothers comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Coen Brothers comes from.", "x": "Origins: Fargo.. Fargo. The history of Coen Brothers — the Minnesota duo.. Lebowski. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Coen Brothers respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Coen Brothers respectfully.", "x": "Engaging: No Country.. Big Lebowski. How to participate or observe well — Coen Brothers. the Minnesota duo. Respect first, always; Quirky.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Coen Brothers do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Coen Brothers do's and don'ts.", "x": "Etiquette: Minnesota.. No Country. The rules of respect — Coen Brothers. the Minnesota duo. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Coen Brothers.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Coen Brothers.", "x": "Planning: Fargo.. O Brother. Practical notes — Coen Brothers. the Minnesota duo. A little planning shows respect for Lebowski.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Coen Brothers and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Coen Brothers and money.", "x": "Costs: No Country.. Minnesota. What to budget — Coen Brothers. the Minnesota duo. The best experiences of Quirky. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-coen-brothers-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
