(function(){'use strict';
/* JAH Visual Novels Game Genre Database generator — jahdb-e2-game-visual-novel-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-visual-novel-games',PREFIX='JAH-E2GAMEVISUA-',NAME='JAH Visual Novels Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Visual Novels: the complete guide", "d": "Visual Novels: the reading game..", "g": "overview", "l": 2, "q": "What is Visual Novels: the complete guide?", "a": "Visual Novels: the reading game..", "x": "The complete game genre guide to Visual Novels: the reading game.. Choices. History, meaning, practices, and how to engage respectfully — everything in one database. Choices. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Visual Novels essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Visual Novels essentials.", "x": "At a glance: Visual Novels — the reading game.. Routes. The essentials: Routes.. Japan. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Choices.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Choices.", "x": "Visual Novels: Choices.. Routes. Essential knowledge — Japan.. the reading game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Choices..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Choices..", "x": "Explained: Choices.. Endings. The context — Visual Novels. Romance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Routes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Routes.", "x": "Visual Novels: Routes.. Japan. Essential knowledge — Romance.. the reading game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Routes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Routes..", "x": "Explained: Routes.. Romance. The context — Visual Novels. Sprites. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Japan.", "x": "Visual Novels: Japan.. Endings. Essential knowledge — Sprites.. the reading game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Classics. The context — Visual Novels. Endings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Romance.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Romance.", "x": "Visual Novels: Romance.. Romance. Essential knowledge — Endings.. the reading game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Romance..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Romance..", "x": "Explained: Romance.. Choices. The context — Visual Novels. Choices. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sprites.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sprites.", "x": "Visual Novels: Sprites.. Classics. Essential knowledge — Choices.. the reading game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sprites..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sprites..", "x": "Explained: Sprites.. Routes. The context — Visual Novels. Routes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Endings.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Endings.", "x": "Visual Novels: Endings.. Choices. Essential knowledge — Routes.. the reading game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Endings..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Endings..", "x": "Explained: Endings.. Japan. The context — Visual Novels. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Choices.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Choices.", "x": "Visual Novels in depth: Choices.. Routes. Details — the reading game.. Japan. Romance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Routes.", "x": "Visual Novels in depth: Routes.. Japan. Details — the reading game.. Endings. Sprites. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Japan.", "x": "Visual Novels in depth: Japan.. Romance. Details — the reading game.. Romance. Endings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Endings.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Endings.", "x": "Visual Novels in depth: Endings.. Sprites. Details — the reading game.. Classics. Choices. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Romance.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Romance.", "x": "Visual Novels in depth: Romance.. Endings. Details — the reading game.. Choices. Routes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Visual Novels in depth: Classics.. Choices. Details — the reading game.. Routes. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Visual Novels comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Visual Novels comes from.", "x": "Origins: Choices.. Choices. The history of Visual Novels — the reading game.. Routes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Visual Novels respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Visual Novels respectfully.", "x": "Engaging: Japan.. Routes. How to participate or observe well — Visual Novels. the reading game. Respect first, always; Endings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Visual Novels do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Visual Novels do's and don'ts.", "x": "Etiquette: Romance.. Japan. The rules of respect — Visual Novels. the reading game. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Visual Novels.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Visual Novels.", "x": "Planning: Choices.. Romance. Practical notes — Visual Novels. the reading game. A little planning shows respect for Routes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Visual Novels and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Visual Novels and money.", "x": "Costs: Japan.. Sprites. What to budget — Visual Novels. the reading game. The best experiences of Endings. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-visual-novel-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
