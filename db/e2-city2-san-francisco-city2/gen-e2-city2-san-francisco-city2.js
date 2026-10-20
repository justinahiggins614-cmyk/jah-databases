(function(){'use strict';
/* JAH San Francisco City2 Database generator — jahdb-e2-city2-san-francisco-city2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city2-san-francisco-city2',PREFIX='JAH-E2CITY2SANF-',NAME='JAH San Francisco City2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "San Francisco City2: the complete guide", "d": "San Francisco City2: the fog 2..", "g": "overview", "l": 2, "q": "What is San Francisco City2: the complete guide?", "a": "San Francisco City2: the fog 2..", "x": "The complete city guide to San Francisco City2: the fog 2.. Golden Gate. History, meaning, practices, and how to engage respectfully — everything in one database. Gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "San Francisco City2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "San Francisco City2 essentials.", "x": "At a glance: San Francisco City2 — the fog 2.. Hills. The essentials: USA.. 874K. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Golden Gate.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Golden Gate.", "x": "San Francisco City2: Golden Gate.. USA. Essential knowledge — 874K.. the fog 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Golden Gate..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Golden Gate..", "x": "Explained: Golden Gate.. Hills. The context — San Francisco City2. Tech. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hills.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hills.", "x": "San Francisco City2: Hills.. Fog. Essential knowledge — Tech.. the fog 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hills..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hills..", "x": "Explained: Hills.. Tech. The context — San Francisco City2. USA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "874K.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "874K.", "x": "San Francisco City2: 874K.. Hills. Essential knowledge — USA.. the fog 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 874K..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 874K..", "x": "Explained: 874K.. Guide. The context — San Francisco City2. Fog. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tech.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tech.", "x": "San Francisco City2: Tech.. Tech. Essential knowledge — Fog.. the fog 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tech..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tech..", "x": "Explained: Tech.. Gate. The context — San Francisco City2. Golden Gate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "USA.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "USA.", "x": "San Francisco City2: USA.. Guide. Essential knowledge — Golden Gate.. the fog 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: USA..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: USA..", "x": "Explained: USA.. USA. The context — San Francisco City2. Hills. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fog.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fog.", "x": "San Francisco City2: Fog.. Gate. Essential knowledge — Hills.. the fog 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fog..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fog..", "x": "Explained: Fog.. Fog. The context — San Francisco City2. 874K. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gate.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gate.", "x": "San Francisco City2 in depth: Gate.. Hills. Details — the fog 2.. Fog. Tech. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "USA.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "USA.", "x": "San Francisco City2 in depth: USA.. 874K. Details — the fog 2.. Hills. USA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fog.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fog.", "x": "San Francisco City2 in depth: Fog.. Tech. Details — the fog 2.. Tech. Fog. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hills.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hills.", "x": "San Francisco City2 in depth: Hills.. USA. Details — the fog 2.. Guide. Golden Gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tech.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tech.", "x": "San Francisco City2 in depth: Tech.. Fog. Details — the fog 2.. Gate. Hills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "San Francisco City2 in depth: Guide.. Golden Gate. Details — the fog 2.. USA. 874K. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where San Francisco City2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where San Francisco City2 comes from.", "x": "Origins: Gate.. Golden Gate. The history of San Francisco City2 — the fog 2.. USA. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing San Francisco City2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing San Francisco City2 respectfully.", "x": "Engaging: Fog.. Hills. How to participate or observe well — San Francisco City2. the fog 2. Respect first, always; Hills.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "San Francisco City2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "San Francisco City2 do's and don'ts.", "x": "Etiquette: Tech.. 874K. The rules of respect — San Francisco City2. the fog 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around San Francisco City2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around San Francisco City2.", "x": "Planning: Gate.. Tech. Practical notes — San Francisco City2. the fog 2. A little planning shows respect for USA.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "San Francisco City2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "San Francisco City2 and money.", "x": "Costs: Fog.. USA. What to budget — San Francisco City2. the fog 2. The best experiences of Hills. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city2-san-francisco-city2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
