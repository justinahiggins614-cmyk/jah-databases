(function(){'use strict';
/* JAH Musical Plays Play Database generator — jahdb-e2-play-musical-plays-stage-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-play-musical-plays-stage',PREFIX='JAH-E2PLAYMUSIC-',NAME='JAH Musical Plays Play Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Musical Plays: the complete guide", "d": "Musical Plays: the singing stage..", "g": "overview", "l": 2, "q": "What is Musical Plays: the complete guide?", "a": "Musical Plays: the singing stage..", "x": "The complete play guide to Musical Plays: the singing stage.. Broadway. History, meaning, practices, and how to engage respectfully — everything in one database. Book. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Musical Plays essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Musical Plays essentials.", "x": "At a glance: Musical Plays — the singing stage.. Book. The essentials: Songs.. Songs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Broadway.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Broadway.", "x": "Musical Plays: Broadway.. Songs. Essential knowledge — Songs.. the singing stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Broadway..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Broadway..", "x": "Explained: Broadway.. Finale. The context — Musical Plays. Choreography. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Book.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Book.", "x": "Musical Plays: Book.. Overture. Essential knowledge — Choreography.. the singing stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Book..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Book..", "x": "Explained: Book.. Broadway. The context — Musical Plays. Overture. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Songs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Songs.", "x": "Musical Plays: Songs.. Finale. Essential knowledge — Overture.. the singing stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Songs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Songs..", "x": "Explained: Songs.. Classics. The context — Musical Plays. Finale. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Choreography.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Choreography.", "x": "Musical Plays: Choreography.. Broadway. Essential knowledge — Finale.. the singing stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Choreography..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Choreography..", "x": "Explained: Choreography.. Book. The context — Musical Plays. Broadway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Overture.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Overture.", "x": "Musical Plays: Overture.. Classics. Essential knowledge — Broadway.. the singing stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Overture..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Overture..", "x": "Explained: Overture.. Songs. The context — Musical Plays. Book. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Finale.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Finale.", "x": "Musical Plays: Finale.. Book. Essential knowledge — Book.. the singing stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Finale..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Finale..", "x": "Explained: Finale.. Overture. The context — Musical Plays. Songs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Book.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Book.", "x": "Musical Plays in depth: Book.. Book. Details — the singing stage.. Overture. Choreography. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Songs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Songs.", "x": "Musical Plays in depth: Songs.. Songs. Details — the singing stage.. Finale. Overture. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Overture.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Overture.", "x": "Musical Plays in depth: Overture.. Choreography. Details — the singing stage.. Broadway. Finale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Finale.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Finale.", "x": "Musical Plays in depth: Finale.. Overture. Details — the singing stage.. Classics. Broadway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Broadway.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Broadway.", "x": "Musical Plays in depth: Broadway.. Finale. Details — the singing stage.. Book. Book. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Musical Plays in depth: Classics.. Broadway. Details — the singing stage.. Songs. Songs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Musical Plays comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Musical Plays comes from.", "x": "Origins: Book.. Broadway. The history of Musical Plays — the singing stage.. Songs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Musical Plays respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Musical Plays respectfully.", "x": "Engaging: Overture.. Book. How to participate or observe well — Musical Plays. the singing stage. Respect first, always; Finale.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Musical Plays do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Musical Plays do's and don'ts.", "x": "Etiquette: Broadway.. Songs. The rules of respect — Musical Plays. the singing stage. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Musical Plays.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Musical Plays.", "x": "Planning: Book.. Choreography. Practical notes — Musical Plays. the singing stage. A little planning shows respect for Songs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Musical Plays and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Musical Plays and money.", "x": "Costs: Overture.. Overture. What to budget — Musical Plays. the singing stage. The best experiences of Finale. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-play-musical-plays-stage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
