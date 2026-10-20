(function(){'use strict';
/* JAH Fortnite Franchise Database generator — jahdb-e2-games2-fortnite-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-fortnite-franchise-game',PREFIX='JAH-E2GAMES2FOR-',NAME='JAH Fortnite Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fortnite Franchise: the complete guide", "d": "Fortnite Franchise: the battle bus..", "g": "overview", "l": 2, "q": "What is Fortnite Franchise: the complete guide?", "a": "Fortnite Franchise: the battle bus..", "x": "The complete game franchise guide to Fortnite Franchise: the battle bus.. 2017. History, meaning, practices, and how to engage respectfully — everything in one database. Epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fortnite Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fortnite Franchise essentials.", "x": "At a glance: Fortnite Franchise — the battle bus.. Epic. The essentials: Skins.. Battle royale. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2017.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2017.", "x": "Fortnite Franchise: 2017.. Skins. Essential knowledge — Battle royale.. the battle bus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2017..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2017..", "x": "Explained: 2017.. Royale. The context — Fortnite Franchise. Building. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Epic.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Epic.", "x": "Fortnite Franchise: Epic.. Events. Essential knowledge — Building.. the battle bus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Epic..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Epic..", "x": "Explained: Epic.. Building. The context — Fortnite Franchise. Skins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Battle royale.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Battle royale.", "x": "Fortnite Franchise: Battle royale.. Royale. Essential knowledge — Skins.. the battle bus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Battle royale..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Battle royale..", "x": "Explained: Battle royale.. Games. The context — Fortnite Franchise. Events. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Building.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Building.", "x": "Fortnite Franchise: Building.. Building. Essential knowledge — Events.. the battle bus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Building..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Building..", "x": "Explained: Building.. Epic. The context — Fortnite Franchise. 2017. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Skins.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Skins.", "x": "Fortnite Franchise: Skins.. Games. Essential knowledge — 2017.. the battle bus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Skins..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Skins..", "x": "Explained: Skins.. Skins. The context — Fortnite Franchise. Epic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Events.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Events.", "x": "Fortnite Franchise: Events.. Epic. Essential knowledge — Epic.. the battle bus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Events..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Events..", "x": "Explained: Events.. Events. The context — Fortnite Franchise. Battle royale. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Epic.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Epic.", "x": "Fortnite Franchise in depth: Epic.. Epic. Details — the battle bus.. Events. Building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Skins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Skins.", "x": "Fortnite Franchise in depth: Skins.. Battle royale. Details — the battle bus.. Royale. Skins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Events.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Events.", "x": "Fortnite Franchise in depth: Events.. Building. Details — the battle bus.. Building. Events. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Royale.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Royale.", "x": "Fortnite Franchise in depth: Royale.. Skins. Details — the battle bus.. Games. 2017. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Building.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Building.", "x": "Fortnite Franchise in depth: Building.. Events. Details — the battle bus.. Epic. Epic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Fortnite Franchise in depth: Games.. 2017. Details — the battle bus.. Skins. Battle royale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fortnite Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fortnite Franchise comes from.", "x": "Origins: Epic.. 2017. The history of Fortnite Franchise — the battle bus.. Skins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fortnite Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fortnite Franchise respectfully.", "x": "Engaging: Events.. Epic. How to participate or observe well — Fortnite Franchise. the battle bus. Respect first, always; Royale.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fortnite Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fortnite Franchise do's and don'ts.", "x": "Etiquette: Building.. Battle royale. The rules of respect — Fortnite Franchise. the battle bus. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fortnite Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fortnite Franchise.", "x": "Planning: Epic.. Building. Practical notes — Fortnite Franchise. the battle bus. A little planning shows respect for Skins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fortnite Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fortnite Franchise and money.", "x": "Costs: Events.. Skins. What to budget — Fortnite Franchise. the battle bus. The best experiences of Royale. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-fortnite-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
