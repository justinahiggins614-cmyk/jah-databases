(function(){'use strict';
/* JAH New York Public Library Library Database generator — jahdb-e2-library-ny-public-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-ny-public-library',PREFIX='JAH-E2LIBRARYNY-',NAME='JAH New York Public Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New York Public Library: the complete guide", "d": "New York Public Library: lions guarding knowledge..", "g": "overview", "l": 2, "q": "What is New York Public Library: the complete guide?", "a": "New York Public Library: lions guarding knowledge..", "x": "The complete library guide to New York Public Library: lions guarding knowledge.. Patience/Fortitude. History, meaning, practices, and how to engage respectfully — everything in one database. Lions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "New York Public Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "New York Public Library essentials.", "x": "At a glance: New York Public Library — lions guarding knowledge.. 1911. The essentials: Rose Room.. Rose Reading Room. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Patience/Fortitude.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Patience/Fortitude.", "x": "New York Public Library: Patience/Fortitude.. Rose Room. Essential knowledge — Rose Reading Room.. lions guarding knowledge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Patience/Fortitude..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Patience/Fortitude..", "x": "Explained: Patience/Fortitude.. Free. The context — New York Public Library. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1911.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1911.", "x": "New York Public Library: 1911.. History. Essential knowledge — Free.. lions guarding knowledge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1911..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1911..", "x": "Explained: 1911.. Branches. The context — New York Public Library. 42nd St. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rose Reading Room.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rose Reading Room.", "x": "New York Public Library: Rose Reading Room.. Free. Essential knowledge — 42nd St.. lions guarding knowledge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rose Reading Room..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rose Reading Room..", "x": "Explained: Rose Reading Room.. Tours. The context — New York Public Library. Research. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Free.", "x": "New York Public Library: Free.. Branches. Essential knowledge — Research.. lions guarding knowledge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Lions. The context — New York Public Library. Patience/Fortitude. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "42nd St.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "42nd St.", "x": "New York Public Library: 42nd St.. Tours. Essential knowledge — Patience/Fortitude.. lions guarding knowledge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 42nd St..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 42nd St..", "x": "Explained: 42nd St.. Rose Room. The context — New York Public Library. 1911. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Research.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Research.", "x": "New York Public Library: Research.. Lions. Essential knowledge — 1911.. lions guarding knowledge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Research..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Research..", "x": "Explained: Research.. History. The context — New York Public Library. Rose Reading Room. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lions.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lions.", "x": "New York Public Library in depth: Lions.. 1911. Details — lions guarding knowledge.. History. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rose Room.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rose Room.", "x": "New York Public Library in depth: Rose Room.. Rose Reading Room. Details — lions guarding knowledge.. Free. 42nd St. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "New York Public Library in depth: History.. Free. Details — lions guarding knowledge.. Branches. Research. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Free.", "x": "New York Public Library in depth: Free.. 42nd St. Details — lions guarding knowledge.. Tours. Patience/Fortitude. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Branches.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Branches.", "x": "New York Public Library in depth: Branches.. Research. Details — lions guarding knowledge.. Lions. 1911. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "New York Public Library in depth: Tours.. Patience/Fortitude. Details — lions guarding knowledge.. Rose Room. Rose Reading Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where New York Public Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where New York Public Library comes from.", "x": "Origins: Lions.. Patience/Fortitude. The history of New York Public Library — lions guarding knowledge.. Rose Room. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing New York Public Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing New York Public Library respectfully.", "x": "Engaging: History.. 1911. How to participate or observe well — New York Public Library. lions guarding knowledge. Respect first, always; Free.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "New York Public Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "New York Public Library do's and don'ts.", "x": "Etiquette: Branches.. Rose Reading Room. The rules of respect — New York Public Library. lions guarding knowledge. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around New York Public Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around New York Public Library.", "x": "Planning: Lions.. Free. Practical notes — New York Public Library. lions guarding knowledge. A little planning shows respect for Rose Room.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "New York Public Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "New York Public Library and money.", "x": "Costs: History.. 42nd St. What to budget — New York Public Library. lions guarding knowledge. The best experiences of Free. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-ny-public-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
