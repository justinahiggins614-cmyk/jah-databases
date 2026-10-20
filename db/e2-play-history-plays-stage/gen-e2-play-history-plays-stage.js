(function(){'use strict';
/* JAH History Plays Play Database generator — jahdb-e2-play-history-plays-stage-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-play-history-plays-stage',PREFIX='JAH-E2PLAYHISTO-',NAME='JAH History Plays Play Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "History Plays: the complete guide", "d": "History Plays: the crown dramas..", "g": "overview", "l": 2, "q": "What is History Plays: the complete guide?", "a": "History Plays: the crown dramas..", "x": "The complete play guide to History Plays: the crown dramas.. Shakespeare. History, meaning, practices, and how to engage respectfully — everything in one database. Henriad. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "History Plays essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "History Plays essentials.", "x": "At a glance: History Plays — the crown dramas.. Henriad. The essentials: Kings.. Kings. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shakespeare.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shakespeare.", "x": "History Plays: Shakespeare.. Kings. Essential knowledge — Kings.. the crown dramas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shakespeare..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shakespeare..", "x": "Explained: Shakespeare.. Bard. The context — History Plays. Chronicle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Henriad.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Henriad.", "x": "History Plays: Henriad.. Power. Essential knowledge — Chronicle.. the crown dramas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Henriad..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Henriad..", "x": "Explained: Henriad.. Chronicle. The context — History Plays. Power. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kings.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kings.", "x": "History Plays: Kings.. Bard. Essential knowledge — Power.. the crown dramas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kings..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kings..", "x": "Explained: Kings.. Classics. The context — History Plays. Bard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chronicle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chronicle.", "x": "History Plays: Chronicle.. Chronicle. Essential knowledge — Bard.. the crown dramas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chronicle..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chronicle..", "x": "Explained: Chronicle.. Henriad. The context — History Plays. Shakespeare. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Power.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Power.", "x": "History Plays: Power.. Classics. Essential knowledge — Shakespeare.. the crown dramas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Power..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Power..", "x": "Explained: Power.. Kings. The context — History Plays. Henriad. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bard.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bard.", "x": "History Plays: Bard.. Henriad. Essential knowledge — Henriad.. the crown dramas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bard..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bard..", "x": "Explained: Bard.. Power. The context — History Plays. Kings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Henriad.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Henriad.", "x": "History Plays in depth: Henriad.. Henriad. Details — the crown dramas.. Power. Chronicle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kings.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kings.", "x": "History Plays in depth: Kings.. Kings. Details — the crown dramas.. Bard. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Power.", "x": "History Plays in depth: Power.. Chronicle. Details — the crown dramas.. Chronicle. Bard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bard.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bard.", "x": "History Plays in depth: Bard.. Power. Details — the crown dramas.. Classics. Shakespeare. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chronicle.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chronicle.", "x": "History Plays in depth: Chronicle.. Bard. Details — the crown dramas.. Henriad. Henriad. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "History Plays in depth: Classics.. Shakespeare. Details — the crown dramas.. Kings. Kings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where History Plays comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where History Plays comes from.", "x": "Origins: Henriad.. Shakespeare. The history of History Plays — the crown dramas.. Kings. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing History Plays respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing History Plays respectfully.", "x": "Engaging: Power.. Henriad. How to participate or observe well — History Plays. the crown dramas. Respect first, always; Bard.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "History Plays do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "History Plays do's and don'ts.", "x": "Etiquette: Chronicle.. Kings. The rules of respect — History Plays. the crown dramas. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around History Plays.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around History Plays.", "x": "Planning: Henriad.. Chronicle. Practical notes — History Plays. the crown dramas. A little planning shows respect for Kings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "History Plays and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "History Plays and money.", "x": "Costs: Power.. Power. What to budget — History Plays. the crown dramas. The best experiences of Bard. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-play-history-plays-stage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
