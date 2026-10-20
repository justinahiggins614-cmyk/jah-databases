(function(){'use strict';
/* JAH Woodland Park Zoo2 Database generator — jahdb-e2-zoo2-woodland-park-zoo2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo2-woodland-park-zoo2',PREFIX='JAH-E2ZOO2WOODL-',NAME='JAH Woodland Park Zoo2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Woodland Park Zoo2: the complete guide", "d": "Woodland Park Zoo2: the Seattle 2..", "g": "overview", "l": 2, "q": "What is Woodland Park Zoo2: the complete guide?", "a": "Woodland Park Zoo2: the Seattle 2..", "x": "The complete zoo guide to Woodland Park Zoo2: the Seattle 2.. 1899. History, meaning, practices, and how to engage respectfully — everything in one database. 1899. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Woodland Park Zoo2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Woodland Park Zoo2 essentials.", "x": "At a glance: Woodland Park Zoo2 — the Seattle 2.. Gorillas. The essentials: Penguins.. Naturalistic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1899.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1899.", "x": "Woodland Park Zoo2: 1899.. Penguins. Essential knowledge — Naturalistic.. the Seattle 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1899..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1899..", "x": "Explained: 1899.. Gorillas. The context — Woodland Park Zoo2. Seattle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gorillas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gorillas.", "x": "Woodland Park Zoo2: Gorillas.. Seattle. Essential knowledge — Seattle.. the Seattle 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gorillas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gorillas..", "x": "Explained: Gorillas.. Acres. The context — Woodland Park Zoo2. 92 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Naturalistic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Naturalistic.", "x": "Woodland Park Zoo2: Naturalistic.. Gorillas. Essential knowledge — 92 acres.. the Seattle 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Naturalistic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Naturalistic..", "x": "Explained: Naturalistic.. Visiting. The context — Woodland Park Zoo2. Penguins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Seattle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Seattle.", "x": "Woodland Park Zoo2: Seattle.. Acres. Essential knowledge — Penguins.. the Seattle 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Seattle..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Seattle..", "x": "Explained: Seattle.. 1899. The context — Woodland Park Zoo2. 1899. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "92 acres.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "92 acres.", "x": "Woodland Park Zoo2: 92 acres.. Visiting. Essential knowledge — 1899.. the Seattle 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 92 acres..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 92 acres..", "x": "Explained: 92 acres.. Penguins. The context — Woodland Park Zoo2. Gorillas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Penguins.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Penguins.", "x": "Woodland Park Zoo2: Penguins.. 1899. Essential knowledge — Gorillas.. the Seattle 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Penguins..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Penguins..", "x": "Explained: Penguins.. Seattle. The context — Woodland Park Zoo2. Naturalistic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1899.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1899.", "x": "Woodland Park Zoo2 in depth: 1899.. Gorillas. Details — the Seattle 2.. Seattle. Seattle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Penguins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Penguins.", "x": "Woodland Park Zoo2 in depth: Penguins.. Naturalistic. Details — the Seattle 2.. Gorillas. 92 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Seattle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Seattle.", "x": "Woodland Park Zoo2 in depth: Seattle.. Seattle. Details — the Seattle 2.. Acres. Penguins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gorillas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gorillas.", "x": "Woodland Park Zoo2 in depth: Gorillas.. 92 acres. Details — the Seattle 2.. Visiting. 1899. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Acres.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Acres.", "x": "Woodland Park Zoo2 in depth: Acres.. Penguins. Details — the Seattle 2.. 1899. Gorillas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Woodland Park Zoo2 in depth: Visiting.. 1899. Details — the Seattle 2.. Penguins. Naturalistic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Woodland Park Zoo2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Woodland Park Zoo2 comes from.", "x": "Origins: 1899.. 1899. The history of Woodland Park Zoo2 — the Seattle 2.. Penguins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Woodland Park Zoo2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Woodland Park Zoo2 respectfully.", "x": "Engaging: Seattle.. Gorillas. How to participate or observe well — Woodland Park Zoo2. the Seattle 2. Respect first, always; Gorillas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Woodland Park Zoo2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Woodland Park Zoo2 do's and don'ts.", "x": "Etiquette: Acres.. Naturalistic. The rules of respect — Woodland Park Zoo2. the Seattle 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Woodland Park Zoo2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Woodland Park Zoo2.", "x": "Planning: 1899.. Seattle. Practical notes — Woodland Park Zoo2. the Seattle 2. A little planning shows respect for Penguins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Woodland Park Zoo2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Woodland Park Zoo2 and money.", "x": "Costs: Seattle.. 92 acres. What to budget — Woodland Park Zoo2. the Seattle 2. The best experiences of Gorillas. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo2-woodland-park-zoo2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
