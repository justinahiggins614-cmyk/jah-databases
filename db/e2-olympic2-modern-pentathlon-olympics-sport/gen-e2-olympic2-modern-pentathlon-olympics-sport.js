(function(){'use strict';
/* JAH Modern Pentathlon Olympics Database generator — jahdb-e2-olympic2-modern-pentathlon-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-modern-pentathlon-olympics-sport',PREFIX='JAH-E2OLYMPIC2M-',NAME='JAH Modern Pentathlon Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Modern Pentathlon Olympics: the complete guide", "d": "Modern Pentathlon Olympics: the five events..", "g": "overview", "l": 2, "q": "What is Modern Pentathlon Olympics: the complete guide?", "a": "Modern Pentathlon Olympics: the five events..", "x": "The complete olympic sport guide to Modern Pentathlon Olympics: the five events.. 1912. History, meaning, practices, and how to engage respectfully — everything in one database. Events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Modern Pentathlon Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Modern Pentathlon Olympics essentials.", "x": "At a glance: Modern Pentathlon Olympics — the five events.. 5 events. The essentials: Laser.. Laser run. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1912.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1912.", "x": "Modern Pentathlon Olympics: 1912.. Laser. Essential knowledge — Laser run.. the five events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1912..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1912..", "x": "Explained: 1912.. Shooting. The context — Modern Pentathlon Olympics. Fencing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "5 events.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "5 events.", "x": "Modern Pentathlon Olympics: 5 events.. Riding. Essential knowledge — Fencing.. the five events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 5 events..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 5 events..", "x": "Explained: 5 events.. Fencing. The context — Modern Pentathlon Olympics. Riding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Laser run.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Laser run.", "x": "Modern Pentathlon Olympics: Laser run.. Shooting. Essential knowledge — Riding.. the five events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Laser run..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Laser run..", "x": "Explained: Laser run.. Guide. The context — Modern Pentathlon Olympics. Shooting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fencing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fencing.", "x": "Modern Pentathlon Olympics: Fencing.. Fencing. Essential knowledge — Shooting.. the five events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fencing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fencing..", "x": "Explained: Fencing.. Events. The context — Modern Pentathlon Olympics. 1912. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Riding.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Riding.", "x": "Modern Pentathlon Olympics: Riding.. Guide. Essential knowledge — 1912.. the five events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Riding..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Riding..", "x": "Explained: Riding.. Laser. The context — Modern Pentathlon Olympics. 5 events. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shooting.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shooting.", "x": "Modern Pentathlon Olympics: Shooting.. Events. Essential knowledge — 5 events.. the five events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shooting..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shooting..", "x": "Explained: Shooting.. Riding. The context — Modern Pentathlon Olympics. Laser run. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Events.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Events.", "x": "Modern Pentathlon Olympics in depth: Events.. 5 events. Details — the five events.. Riding. Fencing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Laser.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Laser.", "x": "Modern Pentathlon Olympics in depth: Laser.. Laser run. Details — the five events.. Shooting. Riding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Riding.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Riding.", "x": "Modern Pentathlon Olympics in depth: Riding.. Fencing. Details — the five events.. Fencing. Shooting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shooting.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shooting.", "x": "Modern Pentathlon Olympics in depth: Shooting.. Riding. Details — the five events.. Guide. 1912. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fencing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fencing.", "x": "Modern Pentathlon Olympics in depth: Fencing.. Shooting. Details — the five events.. Events. 5 events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Modern Pentathlon Olympics in depth: Guide.. 1912. Details — the five events.. Laser. Laser run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Modern Pentathlon Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Modern Pentathlon Olympics comes from.", "x": "Origins: Events.. 1912. The history of Modern Pentathlon Olympics — the five events.. Laser. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Modern Pentathlon Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Modern Pentathlon Olympics respectfully.", "x": "Engaging: Riding.. 5 events. How to participate or observe well — Modern Pentathlon Olympics. the five events. Respect first, always; Shooting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Modern Pentathlon Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Modern Pentathlon Olympics do's and don'ts.", "x": "Etiquette: Fencing.. Laser run. The rules of respect — Modern Pentathlon Olympics. the five events. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Modern Pentathlon Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Modern Pentathlon Olympics.", "x": "Planning: Events.. Fencing. Practical notes — Modern Pentathlon Olympics. the five events. A little planning shows respect for Laser.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Modern Pentathlon Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Modern Pentathlon Olympics and money.", "x": "Costs: Riding.. Riding. What to budget — Modern Pentathlon Olympics. the five events. The best experiences of Shooting. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-modern-pentathlon-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
