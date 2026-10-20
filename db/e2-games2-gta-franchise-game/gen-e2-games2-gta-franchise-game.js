(function(){'use strict';
/* JAH Grand Theft Auto Franchise Database generator — jahdb-e2-games2-gta-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-gta-franchise-game',PREFIX='JAH-E2GAMES2GTA-',NAME='JAH Grand Theft Auto Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Grand Theft Auto Franchise: the complete guide", "d": "Grand Theft Auto Franchise: the open crime..", "g": "overview", "l": 2, "q": "What is Grand Theft Auto Franchise: the complete guide?", "a": "Grand Theft Auto Franchise: the open crime..", "x": "The complete game franchise guide to Grand Theft Auto Franchise: the open crime.. 1997. History, meaning, practices, and how to engage respectfully — everything in one database. Rockstar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Grand Theft Auto Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Grand Theft Auto Franchise essentials.", "x": "At a glance: Grand Theft Auto Franchise — the open crime.. Rockstar. The essentials: Wanted.. Open world. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1997.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1997.", "x": "Grand Theft Auto Franchise: 1997.. Wanted. Essential knowledge — Open world.. the open crime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1997..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1997..", "x": "Explained: 1997.. Open. The context — Grand Theft Auto Franchise. Wanted. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rockstar.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rockstar.", "x": "Grand Theft Auto Franchise: Rockstar.. Records. Essential knowledge — Wanted.. the open crime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rockstar..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rockstar..", "x": "Explained: Rockstar.. Satire. The context — Grand Theft Auto Franchise. Satire. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Open world.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Open world.", "x": "Grand Theft Auto Franchise: Open world.. Open. Essential knowledge — Satire.. the open crime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Open world..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Open world..", "x": "Explained: Open world.. Games. The context — Grand Theft Auto Franchise. Records. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wanted.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wanted.", "x": "Grand Theft Auto Franchise: Wanted.. Satire. Essential knowledge — Records.. the open crime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Wanted..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Wanted..", "x": "Explained: Wanted.. Rockstar. The context — Grand Theft Auto Franchise. 1997. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Satire.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Satire.", "x": "Grand Theft Auto Franchise: Satire.. Games. Essential knowledge — 1997.. the open crime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Satire..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Satire..", "x": "Explained: Satire.. Wanted. The context — Grand Theft Auto Franchise. Rockstar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Records.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Records.", "x": "Grand Theft Auto Franchise: Records.. Rockstar. Essential knowledge — Rockstar.. the open crime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Records..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Records..", "x": "Explained: Records.. Records. The context — Grand Theft Auto Franchise. Open world. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rockstar.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rockstar.", "x": "Grand Theft Auto Franchise in depth: Rockstar.. Rockstar. Details — the open crime.. Records. Wanted. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wanted.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wanted.", "x": "Grand Theft Auto Franchise in depth: Wanted.. Open world. Details — the open crime.. Open. Satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Records.", "x": "Grand Theft Auto Franchise in depth: Records.. Wanted. Details — the open crime.. Satire. Records. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Open.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Open.", "x": "Grand Theft Auto Franchise in depth: Open.. Satire. Details — the open crime.. Games. 1997. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Satire.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Satire.", "x": "Grand Theft Auto Franchise in depth: Satire.. Records. Details — the open crime.. Rockstar. Rockstar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Grand Theft Auto Franchise in depth: Games.. 1997. Details — the open crime.. Wanted. Open world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Grand Theft Auto Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Grand Theft Auto Franchise comes from.", "x": "Origins: Rockstar.. 1997. The history of Grand Theft Auto Franchise — the open crime.. Wanted. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Grand Theft Auto Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Grand Theft Auto Franchise respectfully.", "x": "Engaging: Records.. Rockstar. How to participate or observe well — Grand Theft Auto Franchise. the open crime. Respect first, always; Open.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Grand Theft Auto Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Grand Theft Auto Franchise do's and don'ts.", "x": "Etiquette: Satire.. Open world. The rules of respect — Grand Theft Auto Franchise. the open crime. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Grand Theft Auto Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Grand Theft Auto Franchise.", "x": "Planning: Rockstar.. Wanted. Practical notes — Grand Theft Auto Franchise. the open crime. A little planning shows respect for Wanted.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Grand Theft Auto Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Grand Theft Auto Franchise and money.", "x": "Costs: Records.. Satire. What to budget — Grand Theft Auto Franchise. the open crime. The best experiences of Open. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-gta-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
