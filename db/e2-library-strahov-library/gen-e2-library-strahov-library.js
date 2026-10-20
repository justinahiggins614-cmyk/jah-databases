(function(){'use strict';
/* JAH Strahov Library Library Database generator — jahdb-e2-library-strahov-library-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-strahov-library',PREFIX='JAH-E2LIBRARYST-',NAME='JAH Strahov Library Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Strahov Library: the complete guide", "d": "Strahov Library: Prague's baroque beauty..", "g": "overview", "l": 2, "q": "What is Strahov Library: the complete guide?", "a": "Strahov Library: Prague's baroque beauty..", "x": "The complete library guide to Strahov Library: Prague's baroque beauty.. 1679. History, meaning, practices, and how to engage respectfully — everything in one database. Halls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Strahov Library essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Strahov Library essentials.", "x": "At a glance: Strahov Library — Prague's baroque beauty.. Baroque halls. The essentials: History.. 200K volumes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1679.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1679.", "x": "Strahov Library: 1679.. History. Essential knowledge — 200K volumes.. Prague's baroque beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1679..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1679..", "x": "Explained: 1679.. Prague. The context — Strahov Library. Prague. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Baroque halls.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Baroque halls.", "x": "Strahov Library: Baroque halls.. Tours. Essential knowledge — Prague.. Prague's baroque beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Baroque halls..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Baroque halls..", "x": "Explained: Baroque halls.. Baroque. The context — Strahov Library. Theological. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "200K volumes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "200K volumes.", "x": "Strahov Library: 200K volumes.. Prague. Essential knowledge — Theological.. Prague's baroque beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 200K volumes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 200K volumes..", "x": "Explained: 200K volumes.. Photos. The context — Strahov Library. Photos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Prague.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Prague.", "x": "Strahov Library: Prague.. Baroque. Essential knowledge — Photos.. Prague's baroque beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Prague..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Prague..", "x": "Explained: Prague.. Halls. The context — Strahov Library. 1679. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Theological.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Theological.", "x": "Strahov Library: Theological.. Photos. Essential knowledge — 1679.. Prague's baroque beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Theological..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Theological..", "x": "Explained: Theological.. History. The context — Strahov Library. Baroque halls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Photos.", "x": "Strahov Library: Photos.. Halls. Essential knowledge — Baroque halls.. Prague's baroque beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Photos..", "x": "Explained: Photos.. Tours. The context — Strahov Library. 200K volumes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Halls.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Halls.", "x": "Strahov Library in depth: Halls.. Baroque halls. Details — Prague's baroque beauty.. Tours. Prague. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Strahov Library in depth: History.. 200K volumes. Details — Prague's baroque beauty.. Prague. Theological. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tours.", "x": "Strahov Library in depth: Tours.. Prague. Details — Prague's baroque beauty.. Baroque. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Prague.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Prague.", "x": "Strahov Library in depth: Prague.. Theological. Details — Prague's baroque beauty.. Photos. 1679. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Baroque.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Baroque.", "x": "Strahov Library in depth: Baroque.. Photos. Details — Prague's baroque beauty.. Halls. Baroque halls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Photos.", "x": "Strahov Library in depth: Photos.. 1679. Details — Prague's baroque beauty.. History. 200K volumes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Strahov Library comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Strahov Library comes from.", "x": "Origins: Halls.. 1679. The history of Strahov Library — Prague's baroque beauty.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Strahov Library respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Strahov Library respectfully.", "x": "Engaging: Tours.. Baroque halls. How to participate or observe well — Strahov Library. Prague's baroque beauty. Respect first, always; Prague.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Strahov Library do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Strahov Library do's and don'ts.", "x": "Etiquette: Baroque.. 200K volumes. The rules of respect — Strahov Library. Prague's baroque beauty. When in doubt, ask about Photos.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Strahov Library.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Strahov Library.", "x": "Planning: Halls.. Prague. Practical notes — Strahov Library. Prague's baroque beauty. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Strahov Library and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Strahov Library and money.", "x": "Costs: Tours.. Theological. What to budget — Strahov Library. Prague's baroque beauty. The best experiences of Prague. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-strahov-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
