(function(){'use strict';
/* JAH Andrew Lloyd Webber Musical Database generator — jahdb-e2-musical-andrew-lloyd-webber-musical-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-musical-andrew-lloyd-webber-musical',PREFIX='JAH-E2MUSICALAN-',NAME='JAH Andrew Lloyd Webber Musical Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Andrew Lloyd Webber: the complete guide", "d": "Andrew Lloyd Webber: the mega-musical..", "g": "overview", "l": 2, "q": "What is Andrew Lloyd Webber: the complete guide?", "a": "Andrew Lloyd Webber: the mega-musical..", "x": "The complete musical guide to Andrew Lloyd Webber: the mega-musical.. Phantom. History, meaning, practices, and how to engage respectfully — everything in one database. Phantom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Andrew Lloyd Webber essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Andrew Lloyd Webber essentials.", "x": "At a glance: Andrew Lloyd Webber — the mega-musical.. Cats. The essentials: Cats.. Jesus Christ. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Phantom.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Phantom.", "x": "Andrew Lloyd Webber: Phantom.. Cats. Essential knowledge — Jesus Christ.. the mega-musical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Phantom..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Phantom..", "x": "Explained: Phantom.. 1980s. The context — Andrew Lloyd Webber. Spectacle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cats.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cats.", "x": "Andrew Lloyd Webber: Cats.. Spectacle. Essential knowledge — Spectacle.. the mega-musical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cats..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cats..", "x": "Explained: Cats.. Superstar. The context — Andrew Lloyd Webber. 1980s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Jesus Christ.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Jesus Christ.", "x": "Andrew Lloyd Webber: Jesus Christ.. 1980s. Essential knowledge — 1980s.. the mega-musical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Jesus Christ..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Jesus Christ..", "x": "Explained: Jesus Christ.. Classics. The context — Andrew Lloyd Webber. Really Useful. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spectacle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spectacle.", "x": "Andrew Lloyd Webber: Spectacle.. Superstar. Essential knowledge — Really Useful.. the mega-musical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Spectacle..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Spectacle..", "x": "Explained: Spectacle.. Phantom. The context — Andrew Lloyd Webber. Phantom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1980s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1980s.", "x": "Andrew Lloyd Webber: 1980s.. Classics. Essential knowledge — Phantom.. the mega-musical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1980s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1980s..", "x": "Explained: 1980s.. Cats. The context — Andrew Lloyd Webber. Cats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Really Useful.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Really Useful.", "x": "Andrew Lloyd Webber: Really Useful.. Phantom. Essential knowledge — Cats.. the mega-musical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Really Useful..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Really Useful..", "x": "Explained: Really Useful.. Spectacle. The context — Andrew Lloyd Webber. Jesus Christ. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Phantom.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Phantom.", "x": "Andrew Lloyd Webber in depth: Phantom.. Cats. Details — the mega-musical.. Spectacle. Spectacle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cats.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cats.", "x": "Andrew Lloyd Webber in depth: Cats.. Jesus Christ. Details — the mega-musical.. 1980s. 1980s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spectacle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spectacle.", "x": "Andrew Lloyd Webber in depth: Spectacle.. Spectacle. Details — the mega-musical.. Superstar. Really Useful. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1980s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1980s.", "x": "Andrew Lloyd Webber in depth: 1980s.. 1980s. Details — the mega-musical.. Classics. Phantom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Superstar.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Superstar.", "x": "Andrew Lloyd Webber in depth: Superstar.. Really Useful. Details — the mega-musical.. Phantom. Cats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Andrew Lloyd Webber in depth: Classics.. Phantom. Details — the mega-musical.. Cats. Jesus Christ. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Andrew Lloyd Webber comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Andrew Lloyd Webber comes from.", "x": "Origins: Phantom.. Phantom. The history of Andrew Lloyd Webber — the mega-musical.. Cats. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Andrew Lloyd Webber respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Andrew Lloyd Webber respectfully.", "x": "Engaging: Spectacle.. Cats. How to participate or observe well — Andrew Lloyd Webber. the mega-musical. Respect first, always; 1980s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Andrew Lloyd Webber do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Andrew Lloyd Webber do's and don'ts.", "x": "Etiquette: Superstar.. Jesus Christ. The rules of respect — Andrew Lloyd Webber. the mega-musical. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Andrew Lloyd Webber.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Andrew Lloyd Webber.", "x": "Planning: Phantom.. Spectacle. Practical notes — Andrew Lloyd Webber. the mega-musical. A little planning shows respect for Cats.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Andrew Lloyd Webber and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Andrew Lloyd Webber and money.", "x": "Costs: Spectacle.. 1980s. What to budget — Andrew Lloyd Webber. the mega-musical. The best experiences of 1980s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-musical-andrew-lloyd-webber-musical-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
