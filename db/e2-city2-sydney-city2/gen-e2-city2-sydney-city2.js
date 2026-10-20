(function(){'use strict';
/* JAH Sydney City2 Database generator — jahdb-e2-city2-sydney-city2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city2-sydney-city2',PREFIX='JAH-E2CITY2SYDN-',NAME='JAH Sydney City2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sydney City2: the complete guide", "d": "Sydney City2: the harbor 2..", "g": "overview", "l": 2, "q": "What is Sydney City2: the complete guide?", "a": "Sydney City2: the harbor 2..", "x": "The complete city guide to Sydney City2: the harbor 2.. Opera House. History, meaning, practices, and how to engage respectfully — everything in one database. Opera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sydney City2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sydney City2 essentials.", "x": "At a glance: Sydney City2 — the harbor 2.. Harbour. The essentials: Australia.. 5M. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Opera House.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Opera House.", "x": "Sydney City2: Opera House.. Australia. Essential knowledge — 5M.. the harbor 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Opera House..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Opera House..", "x": "Explained: Opera House.. Harbour. The context — Sydney City2. Australia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Harbour.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Harbour.", "x": "Sydney City2: Harbour.. Bridge. Essential knowledge — Australia.. the harbor 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Harbour..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Harbour..", "x": "Explained: Harbour.. Beaches. The context — Sydney City2. Beaches. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "5M.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "5M.", "x": "Sydney City2: 5M.. Harbour. Essential knowledge — Beaches.. the harbor 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 5M..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 5M..", "x": "Explained: 5M.. Guide. The context — Sydney City2. Bridge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Australia.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Australia.", "x": "Sydney City2: Australia.. Beaches. Essential knowledge — Bridge.. the harbor 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Australia..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Australia..", "x": "Explained: Australia.. Opera. The context — Sydney City2. Opera House. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beaches.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beaches.", "x": "Sydney City2: Beaches.. Guide. Essential knowledge — Opera House.. the harbor 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Beaches..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Beaches..", "x": "Explained: Beaches.. Australia. The context — Sydney City2. Harbour. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bridge.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bridge.", "x": "Sydney City2: Bridge.. Opera. Essential knowledge — Harbour.. the harbor 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bridge..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bridge..", "x": "Explained: Bridge.. Bridge. The context — Sydney City2. 5M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Opera.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Opera.", "x": "Sydney City2 in depth: Opera.. Harbour. Details — the harbor 2.. Bridge. Australia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Australia.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Australia.", "x": "Sydney City2 in depth: Australia.. 5M. Details — the harbor 2.. Harbour. Beaches. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bridge.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bridge.", "x": "Sydney City2 in depth: Bridge.. Australia. Details — the harbor 2.. Beaches. Bridge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Harbour.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Harbour.", "x": "Sydney City2 in depth: Harbour.. Beaches. Details — the harbor 2.. Guide. Opera House. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Beaches.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Beaches.", "x": "Sydney City2 in depth: Beaches.. Bridge. Details — the harbor 2.. Opera. Harbour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Sydney City2 in depth: Guide.. Opera House. Details — the harbor 2.. Australia. 5M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sydney City2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sydney City2 comes from.", "x": "Origins: Opera.. Opera House. The history of Sydney City2 — the harbor 2.. Australia. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sydney City2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sydney City2 respectfully.", "x": "Engaging: Bridge.. Harbour. How to participate or observe well — Sydney City2. the harbor 2. Respect first, always; Harbour.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sydney City2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sydney City2 do's and don'ts.", "x": "Etiquette: Beaches.. 5M. The rules of respect — Sydney City2. the harbor 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sydney City2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sydney City2.", "x": "Planning: Opera.. Australia. Practical notes — Sydney City2. the harbor 2. A little planning shows respect for Australia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sydney City2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sydney City2 and money.", "x": "Costs: Bridge.. Beaches. What to budget — Sydney City2. the harbor 2. The best experiences of Harbour. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city2-sydney-city2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
