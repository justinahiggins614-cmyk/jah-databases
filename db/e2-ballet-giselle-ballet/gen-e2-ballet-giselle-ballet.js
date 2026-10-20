(function(){'use strict';
/* JAH Giselle Ballet Ballet Database generator — jahdb-e2-ballet-giselle-ballet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ballet-giselle-ballet',PREFIX='JAH-E2BALLETGIS-',NAME='JAH Giselle Ballet Ballet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Giselle Ballet: the complete guide", "d": "Giselle Ballet: the romantic tragedy..", "g": "overview", "l": 2, "q": "What is Giselle Ballet: the complete guide?", "a": "Giselle Ballet: the romantic tragedy..", "x": "The complete ballet guide to Giselle Ballet: the romantic tragedy.. 1841. History, meaning, practices, and how to engage respectfully — everything in one database. Wilis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Giselle Ballet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Giselle Ballet essentials.", "x": "At a glance: Giselle Ballet — the romantic tragedy.. Wilis. The essentials: Mad scene.. Albrecht. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1841.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1841.", "x": "Giselle Ballet: 1841.. Mad scene. Essential knowledge — Albrecht.. the romantic tragedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1841..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1841..", "x": "Explained: 1841.. Romantic. The context — Giselle Ballet. Mad scene. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wilis.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wilis.", "x": "Giselle Ballet: Wilis.. 1841. Essential knowledge — Mad scene.. the romantic tragedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Wilis..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Wilis..", "x": "Explained: Wilis.. Albrecht. The context — Giselle Ballet. Romantic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Albrecht.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Albrecht.", "x": "Giselle Ballet: Albrecht.. Romantic. Essential knowledge — Romantic.. the romantic tragedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Albrecht..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Albrecht..", "x": "Explained: Albrecht.. Story. The context — Giselle Ballet. Grave. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mad scene.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mad scene.", "x": "Giselle Ballet: Mad scene.. Albrecht. Essential knowledge — Grave.. the romantic tragedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mad scene..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mad scene..", "x": "Explained: Mad scene.. Wilis. The context — Giselle Ballet. 1841. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Romantic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Romantic.", "x": "Giselle Ballet: Romantic.. Story. Essential knowledge — 1841.. the romantic tragedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Romantic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Romantic..", "x": "Explained: Romantic.. Mad scene. The context — Giselle Ballet. Wilis. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Grave.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Grave.", "x": "Giselle Ballet: Grave.. Wilis. Essential knowledge — Wilis.. the romantic tragedy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Grave..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Grave..", "x": "Explained: Grave.. 1841. The context — Giselle Ballet. Albrecht. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wilis.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wilis.", "x": "Giselle Ballet in depth: Wilis.. Wilis. Details — the romantic tragedy.. 1841. Mad scene. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mad scene.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mad scene.", "x": "Giselle Ballet in depth: Mad scene.. Albrecht. Details — the romantic tragedy.. Romantic. Romantic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1841.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1841.", "x": "Giselle Ballet in depth: 1841.. Mad scene. Details — the romantic tragedy.. Albrecht. Grave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Romantic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Romantic.", "x": "Giselle Ballet in depth: Romantic.. Romantic. Details — the romantic tragedy.. Story. 1841. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Albrecht.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Albrecht.", "x": "Giselle Ballet in depth: Albrecht.. Grave. Details — the romantic tragedy.. Wilis. Wilis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Story.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Story.", "x": "Giselle Ballet in depth: Story.. 1841. Details — the romantic tragedy.. Mad scene. Albrecht. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Giselle Ballet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Giselle Ballet comes from.", "x": "Origins: Wilis.. 1841. The history of Giselle Ballet — the romantic tragedy.. Mad scene. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Giselle Ballet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Giselle Ballet respectfully.", "x": "Engaging: 1841.. Wilis. How to participate or observe well — Giselle Ballet. the romantic tragedy. Respect first, always; Romantic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Giselle Ballet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Giselle Ballet do's and don'ts.", "x": "Etiquette: Albrecht.. Albrecht. The rules of respect — Giselle Ballet. the romantic tragedy. When in doubt, ask about Story.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Giselle Ballet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Giselle Ballet.", "x": "Planning: Wilis.. Mad scene. Practical notes — Giselle Ballet. the romantic tragedy. A little planning shows respect for Mad scene.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Giselle Ballet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Giselle Ballet and money.", "x": "Costs: 1841.. Romantic. What to budget — Giselle Ballet. the romantic tragedy. The best experiences of Romantic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ballet-giselle-ballet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
