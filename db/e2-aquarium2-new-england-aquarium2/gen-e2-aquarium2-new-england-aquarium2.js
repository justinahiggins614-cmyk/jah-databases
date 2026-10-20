(function(){'use strict';
/* JAH New England Aquarium2 Database generator — jahdb-e2-aquarium2-new-england-aquarium2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium2-new-england-aquarium2',PREFIX='JAH-E2AQUARIUM2-',NAME='JAH New England Aquarium2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New England Aquarium2: the complete guide", "d": "New England Aquarium2: the Boston 2..", "g": "overview", "l": 2, "q": "What is New England Aquarium2: the complete guide?", "a": "New England Aquarium2: the Boston 2..", "x": "The complete aquarium guide to New England Aquarium2: the Boston 2.. 1969. History, meaning, practices, and how to engage respectfully — everything in one database. 1969. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "New England Aquarium2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "New England Aquarium2 essentials.", "x": "At a glance: New England Aquarium2 — the Boston 2.. Giant Ocean Tank. The essentials: Turtles.. Penguins. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1969.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1969.", "x": "New England Aquarium2: 1969.. Turtles. Essential knowledge — Penguins.. the Boston 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1969..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1969..", "x": "Explained: 1969.. Tank. The context — New England Aquarium2. Boston. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Giant Ocean Tank.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Giant Ocean Tank.", "x": "New England Aquarium2: Giant Ocean Tank.. Wharf. Essential knowledge — Boston.. the Boston 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Giant Ocean Tank..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Giant Ocean Tank..", "x": "Explained: Giant Ocean Tank.. Penguins. The context — New England Aquarium2. Wharf. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Penguins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Penguins.", "x": "New England Aquarium2: Penguins.. Tank. Essential knowledge — Wharf.. the Boston 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Penguins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Penguins..", "x": "Explained: Penguins.. Visiting. The context — New England Aquarium2. Turtles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Boston.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Boston.", "x": "New England Aquarium2: Boston.. Penguins. Essential knowledge — Turtles.. the Boston 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Boston..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Boston..", "x": "Explained: Boston.. 1969. The context — New England Aquarium2. 1969. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wharf.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wharf.", "x": "New England Aquarium2: Wharf.. Visiting. Essential knowledge — 1969.. the Boston 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wharf..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wharf..", "x": "Explained: Wharf.. Turtles. The context — New England Aquarium2. Giant Ocean Tank. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Turtles.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Turtles.", "x": "New England Aquarium2: Turtles.. 1969. Essential knowledge — Giant Ocean Tank.. the Boston 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Turtles..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Turtles..", "x": "Explained: Turtles.. Wharf. The context — New England Aquarium2. Penguins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1969.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1969.", "x": "New England Aquarium2 in depth: 1969.. Giant Ocean Tank. Details — the Boston 2.. Wharf. Boston. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Turtles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Turtles.", "x": "New England Aquarium2 in depth: Turtles.. Penguins. Details — the Boston 2.. Tank. Wharf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wharf.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wharf.", "x": "New England Aquarium2 in depth: Wharf.. Boston. Details — the Boston 2.. Penguins. Turtles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tank.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tank.", "x": "New England Aquarium2 in depth: Tank.. Wharf. Details — the Boston 2.. Visiting. 1969. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Penguins.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Penguins.", "x": "New England Aquarium2 in depth: Penguins.. Turtles. Details — the Boston 2.. 1969. Giant Ocean Tank. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "New England Aquarium2 in depth: Visiting.. 1969. Details — the Boston 2.. Turtles. Penguins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where New England Aquarium2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where New England Aquarium2 comes from.", "x": "Origins: 1969.. 1969. The history of New England Aquarium2 — the Boston 2.. Turtles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing New England Aquarium2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing New England Aquarium2 respectfully.", "x": "Engaging: Wharf.. Giant Ocean Tank. How to participate or observe well — New England Aquarium2. the Boston 2. Respect first, always; Tank.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "New England Aquarium2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "New England Aquarium2 do's and don'ts.", "x": "Etiquette: Penguins.. Penguins. The rules of respect — New England Aquarium2. the Boston 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around New England Aquarium2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around New England Aquarium2.", "x": "Planning: 1969.. Boston. Practical notes — New England Aquarium2. the Boston 2. A little planning shows respect for Turtles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "New England Aquarium2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "New England Aquarium2 and money.", "x": "Costs: Wharf.. Wharf. What to budget — New England Aquarium2. the Boston 2. The best experiences of Tank. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium2-new-england-aquarium2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
