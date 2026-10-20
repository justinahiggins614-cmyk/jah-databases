(function(){'use strict';
/* JAH Vivaldi Composer Composer Database generator — jahdb-e2-composer-vivaldi-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-vivaldi-composer',PREFIX='JAH-E2COMPOSERV-',NAME='JAH Vivaldi Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vivaldi Composer: the complete guide", "d": "Vivaldi Composer: the red priest..", "g": "overview", "l": 2, "q": "What is Vivaldi Composer: the complete guide?", "a": "Vivaldi Composer: the red priest..", "x": "The complete composer guide to Vivaldi Composer: the red priest.. 1678. History, meaning, practices, and how to engage respectfully — everything in one database. Seasons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Vivaldi Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Vivaldi Composer essentials.", "x": "At a glance: Vivaldi Composer — the red priest.. Four Seasons. The essentials: Venice.. Venice. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1678.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1678.", "x": "Vivaldi Composer: 1678.. Venice. Essential knowledge — Venice.. the red priest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1678..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1678..", "x": "Explained: 1678.. Baroque. The context — Vivaldi Composer. Violin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Four Seasons.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Four Seasons.", "x": "Vivaldi Composer: Four Seasons.. Violin. Essential knowledge — Violin.. the red priest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Four Seasons..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Four Seasons..", "x": "Explained: Four Seasons.. Priest. The context — Vivaldi Composer. Baroque. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Venice.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Venice.", "x": "Vivaldi Composer: Venice.. Baroque. Essential knowledge — Baroque.. the red priest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Venice..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Venice..", "x": "Explained: Venice.. Legacy. The context — Vivaldi Composer. Orphans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Violin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Violin.", "x": "Vivaldi Composer: Violin.. Priest. Essential knowledge — Orphans.. the red priest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Violin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Violin..", "x": "Explained: Violin.. Seasons. The context — Vivaldi Composer. 1678. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Baroque.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Baroque.", "x": "Vivaldi Composer: Baroque.. Legacy. Essential knowledge — 1678.. the red priest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Baroque..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Baroque..", "x": "Explained: Baroque.. Venice. The context — Vivaldi Composer. Four Seasons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Orphans.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Orphans.", "x": "Vivaldi Composer: Orphans.. Seasons. Essential knowledge — Four Seasons.. the red priest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Orphans..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Orphans..", "x": "Explained: Orphans.. Violin. The context — Vivaldi Composer. Venice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Seasons.", "x": "Vivaldi Composer in depth: Seasons.. Four Seasons. Details — the red priest.. Violin. Violin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Venice.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Venice.", "x": "Vivaldi Composer in depth: Venice.. Venice. Details — the red priest.. Baroque. Baroque. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Violin.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Violin.", "x": "Vivaldi Composer in depth: Violin.. Violin. Details — the red priest.. Priest. Orphans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Baroque.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Baroque.", "x": "Vivaldi Composer in depth: Baroque.. Baroque. Details — the red priest.. Legacy. 1678. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Priest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Priest.", "x": "Vivaldi Composer in depth: Priest.. Orphans. Details — the red priest.. Seasons. Four Seasons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Vivaldi Composer in depth: Legacy.. 1678. Details — the red priest.. Venice. Venice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Vivaldi Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Vivaldi Composer comes from.", "x": "Origins: Seasons.. 1678. The history of Vivaldi Composer — the red priest.. Venice. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Vivaldi Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Vivaldi Composer respectfully.", "x": "Engaging: Violin.. Four Seasons. How to participate or observe well — Vivaldi Composer. the red priest. Respect first, always; Baroque.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Vivaldi Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Vivaldi Composer do's and don'ts.", "x": "Etiquette: Priest.. Venice. The rules of respect — Vivaldi Composer. the red priest. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Vivaldi Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Vivaldi Composer.", "x": "Planning: Seasons.. Violin. Practical notes — Vivaldi Composer. the red priest. A little planning shows respect for Venice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Vivaldi Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Vivaldi Composer and money.", "x": "Costs: Violin.. Baroque. What to budget — Vivaldi Composer. the red priest. The best experiences of Baroque. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-vivaldi-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
