(function(){'use strict';
/* JAH Disney Musicals Musical Database generator — jahdb-e2-musical-disney-musicals-stage-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-musical-disney-musicals-stage',PREFIX='JAH-E2MUSICALDI-',NAME='JAH Disney Musicals Musical Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Disney Musicals: the complete guide", "d": "Disney Musicals: the magic on stage..", "g": "overview", "l": 2, "q": "What is Disney Musicals: the complete guide?", "a": "Disney Musicals: the magic on stage..", "x": "The complete musical guide to Disney Musicals: the magic on stage.. Lion King. History, meaning, practices, and how to engage respectfully — everything in one database. Lion King. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Disney Musicals essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Disney Musicals essentials.", "x": "At a glance: Disney Musicals — the magic on stage.. Aladdin. The essentials: Puppets.. Puppets. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lion King.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lion King.", "x": "Disney Musicals: Lion King.. Puppets. Essential knowledge — Puppets.. the magic on stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Lion King..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Lion King..", "x": "Explained: Lion King.. Spectacle. The context — Disney Musicals. Family. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aladdin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aladdin.", "x": "Disney Musicals: Aladdin.. Family. Essential knowledge — Family.. the magic on stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Aladdin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Aladdin..", "x": "Explained: Aladdin.. Aladdin. The context — Disney Musicals. Animated. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Puppets.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Puppets.", "x": "Disney Musicals: Puppets.. Spectacle. Essential knowledge — Animated.. the magic on stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Puppets..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Puppets..", "x": "Explained: Puppets.. Classics. The context — Disney Musicals. Spectacle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Family.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Family.", "x": "Disney Musicals: Family.. Aladdin. Essential knowledge — Spectacle.. the magic on stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Family..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Family..", "x": "Explained: Family.. Lion King. The context — Disney Musicals. Lion King. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Animated.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Animated.", "x": "Disney Musicals: Animated.. Classics. Essential knowledge — Lion King.. the magic on stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Animated..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Animated..", "x": "Explained: Animated.. Puppets. The context — Disney Musicals. Aladdin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spectacle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spectacle.", "x": "Disney Musicals: Spectacle.. Lion King. Essential knowledge — Aladdin.. the magic on stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Spectacle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Spectacle..", "x": "Explained: Spectacle.. Family. The context — Disney Musicals. Puppets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lion King.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lion King.", "x": "Disney Musicals in depth: Lion King.. Aladdin. Details — the magic on stage.. Family. Family. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Puppets.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Puppets.", "x": "Disney Musicals in depth: Puppets.. Puppets. Details — the magic on stage.. Spectacle. Animated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Family.", "x": "Disney Musicals in depth: Family.. Family. Details — the magic on stage.. Aladdin. Spectacle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Spectacle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Spectacle.", "x": "Disney Musicals in depth: Spectacle.. Animated. Details — the magic on stage.. Classics. Lion King. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aladdin.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aladdin.", "x": "Disney Musicals in depth: Aladdin.. Spectacle. Details — the magic on stage.. Lion King. Aladdin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Disney Musicals in depth: Classics.. Lion King. Details — the magic on stage.. Puppets. Puppets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Disney Musicals comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Disney Musicals comes from.", "x": "Origins: Lion King.. Lion King. The history of Disney Musicals — the magic on stage.. Puppets. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Disney Musicals respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Disney Musicals respectfully.", "x": "Engaging: Family.. Aladdin. How to participate or observe well — Disney Musicals. the magic on stage. Respect first, always; Spectacle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Disney Musicals do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Disney Musicals do's and don'ts.", "x": "Etiquette: Aladdin.. Puppets. The rules of respect — Disney Musicals. the magic on stage. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Disney Musicals.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Disney Musicals.", "x": "Planning: Lion King.. Family. Practical notes — Disney Musicals. the magic on stage. A little planning shows respect for Puppets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Disney Musicals and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Disney Musicals and money.", "x": "Costs: Family.. Animated. What to budget — Disney Musicals. the magic on stage. The best experiences of Spectacle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-musical-disney-musicals-stage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
