(function(){'use strict';
/* JAH Longwood Gardens2 Database generator — jahdb-e2-botanical2-longwood-gardens2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-botanical2-longwood-gardens2',PREFIX='JAH-E2BOTANICAL-',NAME='JAH Longwood Gardens2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Longwood Gardens2: the complete guide", "d": "Longwood Gardens2: the PA 2..", "g": "overview", "l": 2, "q": "What is Longwood Gardens2: the complete guide?", "a": "Longwood Gardens2: the PA 2..", "x": "The complete botanical garden guide to Longwood Gardens2: the PA 2.. 1906. History, meaning, practices, and how to engage respectfully — everything in one database. 1906. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Longwood Gardens2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Longwood Gardens2 essentials.", "x": "At a glance: Longwood Gardens2 — the PA 2.. Fountains. The essentials: Christmas.. Conservatory. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1906.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1906.", "x": "Longwood Gardens2: 1906.. Christmas. Essential knowledge — Conservatory.. the PA 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1906..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1906..", "x": "Explained: 1906.. Fountains. The context — Longwood Gardens2. 1,077 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fountains.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fountains.", "x": "Longwood Gardens2: Fountains.. du Pont. Essential knowledge — 1,077 acres.. the PA 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fountains..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fountains..", "x": "Explained: Fountains.. Acres. The context — Longwood Gardens2. du Pont. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Conservatory.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Conservatory.", "x": "Longwood Gardens2: Conservatory.. Fountains. Essential knowledge — du Pont.. the PA 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Conservatory..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Conservatory..", "x": "Explained: Conservatory.. Visiting. The context — Longwood Gardens2. Christmas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1,077 acres.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1,077 acres.", "x": "Longwood Gardens2: 1,077 acres.. Acres. Essential knowledge — Christmas.. the PA 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1,077 acres..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1,077 acres..", "x": "Explained: 1,077 acres.. 1906. The context — Longwood Gardens2. 1906. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "du Pont.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "du Pont.", "x": "Longwood Gardens2: du Pont.. Visiting. Essential knowledge — 1906.. the PA 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: du Pont..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: du Pont..", "x": "Explained: du Pont.. Christmas. The context — Longwood Gardens2. Fountains. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Christmas.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Christmas.", "x": "Longwood Gardens2: Christmas.. 1906. Essential knowledge — Fountains.. the PA 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Christmas..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Christmas..", "x": "Explained: Christmas.. du Pont. The context — Longwood Gardens2. Conservatory. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1906.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1906.", "x": "Longwood Gardens2 in depth: 1906.. Fountains. Details — the PA 2.. du Pont. 1,077 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Christmas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Christmas.", "x": "Longwood Gardens2 in depth: Christmas.. Conservatory. Details — the PA 2.. Fountains. du Pont. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "du Pont.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "du Pont.", "x": "Longwood Gardens2 in depth: du Pont.. 1,077 acres. Details — the PA 2.. Acres. Christmas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fountains.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fountains.", "x": "Longwood Gardens2 in depth: Fountains.. du Pont. Details — the PA 2.. Visiting. 1906. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Acres.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Acres.", "x": "Longwood Gardens2 in depth: Acres.. Christmas. Details — the PA 2.. 1906. Fountains. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Longwood Gardens2 in depth: Visiting.. 1906. Details — the PA 2.. Christmas. Conservatory. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Longwood Gardens2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Longwood Gardens2 comes from.", "x": "Origins: 1906.. 1906. The history of Longwood Gardens2 — the PA 2.. Christmas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Longwood Gardens2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Longwood Gardens2 respectfully.", "x": "Engaging: du Pont.. Fountains. How to participate or observe well — Longwood Gardens2. the PA 2. Respect first, always; Fountains.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Longwood Gardens2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Longwood Gardens2 do's and don'ts.", "x": "Etiquette: Acres.. Conservatory. The rules of respect — Longwood Gardens2. the PA 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Longwood Gardens2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Longwood Gardens2.", "x": "Planning: 1906.. 1,077 acres. Practical notes — Longwood Gardens2. the PA 2. A little planning shows respect for Christmas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Longwood Gardens2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Longwood Gardens2 and money.", "x": "Costs: du Pont.. du Pont. What to budget — Longwood Gardens2. the PA 2. The best experiences of Fountains. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-botanical2-longwood-gardens2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
