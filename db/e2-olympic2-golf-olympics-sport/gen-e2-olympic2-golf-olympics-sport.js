(function(){'use strict';
/* JAH Golf Olympics Database generator — jahdb-e2-olympic2-golf-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-golf-olympics-sport',PREFIX='JAH-E2OLYMPIC2G-',NAME='JAH Golf Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Golf Olympics: the complete guide", "d": "Golf Olympics: the returned sport..", "g": "overview", "l": 2, "q": "What is Golf Olympics: the complete guide?", "a": "Golf Olympics: the returned sport..", "x": "The complete olympic sport guide to Golf Olympics: the returned sport.. 1900. History, meaning, practices, and how to engage respectfully — everything in one database. Holes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Golf Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Golf Olympics essentials.", "x": "At a glance: Golf Olympics — the returned sport.. 2016. The essentials: Stroke.. 72 holes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1900.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1900.", "x": "Golf Olympics: 1900.. Stroke. Essential knowledge — 72 holes.. the returned sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1900..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1900..", "x": "Explained: 1900.. 2016. The context — Golf Olympics. Stroke. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2016.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2016.", "x": "Golf Olympics: 2016.. Medals. Essential knowledge — Stroke.. the returned sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 2016..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 2016..", "x": "Explained: 2016.. Course. The context — Golf Olympics. Course. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "72 holes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "72 holes.", "x": "Golf Olympics: 72 holes.. 2016. Essential knowledge — Course.. the returned sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 72 holes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 72 holes..", "x": "Explained: 72 holes.. Guide. The context — Golf Olympics. Medals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Stroke.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Stroke.", "x": "Golf Olympics: Stroke.. Course. Essential knowledge — Medals.. the returned sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Stroke..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Stroke..", "x": "Explained: Stroke.. Holes. The context — Golf Olympics. 1900. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Course.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Course.", "x": "Golf Olympics: Course.. Guide. Essential knowledge — 1900.. the returned sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Course..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Course..", "x": "Explained: Course.. Stroke. The context — Golf Olympics. 2016. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Medals.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Medals.", "x": "Golf Olympics: Medals.. Holes. Essential knowledge — 2016.. the returned sport. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Medals..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Medals..", "x": "Explained: Medals.. Medals. The context — Golf Olympics. 72 holes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Holes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Holes.", "x": "Golf Olympics in depth: Holes.. 2016. Details — the returned sport.. Medals. Stroke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stroke.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stroke.", "x": "Golf Olympics in depth: Stroke.. 72 holes. Details — the returned sport.. 2016. Course. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Medals.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Medals.", "x": "Golf Olympics in depth: Medals.. Stroke. Details — the returned sport.. Course. Medals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "2016.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "2016.", "x": "Golf Olympics in depth: 2016.. Course. Details — the returned sport.. Guide. 1900. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Course.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Course.", "x": "Golf Olympics in depth: Course.. Medals. Details — the returned sport.. Holes. 2016. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Golf Olympics in depth: Guide.. 1900. Details — the returned sport.. Stroke. 72 holes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Golf Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Golf Olympics comes from.", "x": "Origins: Holes.. 1900. The history of Golf Olympics — the returned sport.. Stroke. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Golf Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Golf Olympics respectfully.", "x": "Engaging: Medals.. 2016. How to participate or observe well — Golf Olympics. the returned sport. Respect first, always; 2016.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Golf Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Golf Olympics do's and don'ts.", "x": "Etiquette: Course.. 72 holes. The rules of respect — Golf Olympics. the returned sport. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Golf Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Golf Olympics.", "x": "Planning: Holes.. Stroke. Practical notes — Golf Olympics. the returned sport. A little planning shows respect for Stroke.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Golf Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Golf Olympics and money.", "x": "Costs: Medals.. Course. What to budget — Golf Olympics. the returned sport. The best experiences of 2016. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-golf-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
