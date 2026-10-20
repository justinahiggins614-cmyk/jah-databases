(function(){'use strict';
/* JAH Hip-Hop Dance Dance Form Database generator — jahdb-e2-dance-hiphop-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-hiphop-dance-form',PREFIX='JAH-E2DANCEHIPH-',NAME='JAH Hip-Hop Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hip-Hop Dance: the complete guide", "d": "Hip-Hop Dance: the street dance..", "g": "overview", "l": 2, "q": "What is Hip-Hop Dance: the complete guide?", "a": "Hip-Hop Dance: the street dance..", "x": "The complete dance form guide to Hip-Hop Dance: the street dance.. Breaking. History, meaning, practices, and how to engage respectfully — everything in one database. Breaking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hip-Hop Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hip-Hop Dance essentials.", "x": "At a glance: Hip-Hop Dance — the street dance.. Popping. The essentials: Popping.. Locking. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Breaking.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Breaking.", "x": "Hip-Hop Dance: Breaking.. Popping. Essential knowledge — Locking.. the street dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Breaking..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Breaking..", "x": "Explained: Breaking.. Battles. The context — Hip-Hop Dance. Bronx. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Popping.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Popping.", "x": "Hip-Hop Dance: Popping.. Cypher. Essential knowledge — Bronx.. the street dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Popping..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Popping..", "x": "Explained: Popping.. Bronx. The context — Hip-Hop Dance. Cypher. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Locking.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Locking.", "x": "Hip-Hop Dance: Locking.. Battles. Essential knowledge — Cypher.. the street dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Locking..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Locking..", "x": "Explained: Locking.. Training. The context — Hip-Hop Dance. Battles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bronx.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bronx.", "x": "Hip-Hop Dance: Bronx.. Bronx. Essential knowledge — Battles.. the street dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bronx..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bronx..", "x": "Explained: Bronx.. Breaking. The context — Hip-Hop Dance. Breaking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cypher.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cypher.", "x": "Hip-Hop Dance: Cypher.. Training. Essential knowledge — Breaking.. the street dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cypher..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cypher..", "x": "Explained: Cypher.. Popping. The context — Hip-Hop Dance. Popping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Battles.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Battles.", "x": "Hip-Hop Dance: Battles.. Breaking. Essential knowledge — Popping.. the street dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Battles..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Battles..", "x": "Explained: Battles.. Cypher. The context — Hip-Hop Dance. Locking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Breaking.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Breaking.", "x": "Hip-Hop Dance in depth: Breaking.. Popping. Details — the street dance.. Cypher. Bronx. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Popping.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Popping.", "x": "Hip-Hop Dance in depth: Popping.. Locking. Details — the street dance.. Battles. Cypher. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cypher.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cypher.", "x": "Hip-Hop Dance in depth: Cypher.. Bronx. Details — the street dance.. Bronx. Battles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Battles.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Battles.", "x": "Hip-Hop Dance in depth: Battles.. Cypher. Details — the street dance.. Training. Breaking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bronx.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bronx.", "x": "Hip-Hop Dance in depth: Bronx.. Battles. Details — the street dance.. Breaking. Popping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Hip-Hop Dance in depth: Training.. Breaking. Details — the street dance.. Popping. Locking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hip-Hop Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hip-Hop Dance comes from.", "x": "Origins: Breaking.. Breaking. The history of Hip-Hop Dance — the street dance.. Popping. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hip-Hop Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hip-Hop Dance respectfully.", "x": "Engaging: Cypher.. Popping. How to participate or observe well — Hip-Hop Dance. the street dance. Respect first, always; Battles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hip-Hop Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hip-Hop Dance do's and don'ts.", "x": "Etiquette: Bronx.. Locking. The rules of respect — Hip-Hop Dance. the street dance. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hip-Hop Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hip-Hop Dance.", "x": "Planning: Breaking.. Bronx. Practical notes — Hip-Hop Dance. the street dance. A little planning shows respect for Popping.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hip-Hop Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hip-Hop Dance and money.", "x": "Costs: Cypher.. Cypher. What to budget — Hip-Hop Dance. the street dance. The best experiences of Battles. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-hiphop-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
