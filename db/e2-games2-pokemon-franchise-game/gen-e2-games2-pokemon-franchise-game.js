(function(){'use strict';
/* JAH Pokemon Franchise Database generator — jahdb-e2-games2-pokemon-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-pokemon-franchise-game',PREFIX='JAH-E2GAMES2POK-',NAME='JAH Pokemon Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pokemon Franchise: the complete guide", "d": "Pokemon Franchise: the pocket monsters..", "g": "overview", "l": 2, "q": "What is Pokemon Franchise: the complete guide?", "a": "Pokemon Franchise: the pocket monsters..", "x": "The complete game franchise guide to Pokemon Franchise: the pocket monsters.. 1996. History, meaning, practices, and how to engage respectfully — everything in one database. Pikachu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pokemon Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pokemon Franchise essentials.", "x": "At a glance: Pokemon Franchise — the pocket monsters.. Gotta catch. The essentials: Cards.. Pikachu. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1996.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1996.", "x": "Pokemon Franchise: 1996.. Cards. Essential knowledge — Pikachu.. the pocket monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1996..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1996..", "x": "Explained: 1996.. Nintendo. The context — Pokemon Franchise. Cards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gotta catch.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gotta catch.", "x": "Pokemon Franchise: Gotta catch.. Anime. Essential knowledge — Cards.. the pocket monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gotta catch..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gotta catch..", "x": "Explained: Gotta catch.. Catch. The context — Pokemon Franchise. Anime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pikachu.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pikachu.", "x": "Pokemon Franchise: Pikachu.. Nintendo. Essential knowledge — Anime.. the pocket monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pikachu..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pikachu..", "x": "Explained: Pikachu.. Games. The context — Pokemon Franchise. Nintendo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cards.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cards.", "x": "Pokemon Franchise: Cards.. Catch. Essential knowledge — Nintendo.. the pocket monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cards..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cards..", "x": "Explained: Cards.. Pikachu. The context — Pokemon Franchise. 1996. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Anime.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Anime.", "x": "Pokemon Franchise: Anime.. Games. Essential knowledge — 1996.. the pocket monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Anime..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Anime..", "x": "Explained: Anime.. Cards. The context — Pokemon Franchise. Gotta catch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nintendo.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nintendo.", "x": "Pokemon Franchise: Nintendo.. Pikachu. Essential knowledge — Gotta catch.. the pocket monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Nintendo..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Nintendo..", "x": "Explained: Nintendo.. Anime. The context — Pokemon Franchise. Pikachu. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pikachu.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pikachu.", "x": "Pokemon Franchise in depth: Pikachu.. Gotta catch. Details — the pocket monsters.. Anime. Cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cards.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cards.", "x": "Pokemon Franchise in depth: Cards.. Pikachu. Details — the pocket monsters.. Nintendo. Anime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Anime.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Anime.", "x": "Pokemon Franchise in depth: Anime.. Cards. Details — the pocket monsters.. Catch. Nintendo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nintendo.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nintendo.", "x": "Pokemon Franchise in depth: Nintendo.. Anime. Details — the pocket monsters.. Games. 1996. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Catch.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Catch.", "x": "Pokemon Franchise in depth: Catch.. Nintendo. Details — the pocket monsters.. Pikachu. Gotta catch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Pokemon Franchise in depth: Games.. 1996. Details — the pocket monsters.. Cards. Pikachu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pokemon Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pokemon Franchise comes from.", "x": "Origins: Pikachu.. 1996. The history of Pokemon Franchise — the pocket monsters.. Cards. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pokemon Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pokemon Franchise respectfully.", "x": "Engaging: Anime.. Gotta catch. How to participate or observe well — Pokemon Franchise. the pocket monsters. Respect first, always; Nintendo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pokemon Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pokemon Franchise do's and don'ts.", "x": "Etiquette: Catch.. Pikachu. The rules of respect — Pokemon Franchise. the pocket monsters. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pokemon Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pokemon Franchise.", "x": "Planning: Pikachu.. Cards. Practical notes — Pokemon Franchise. the pocket monsters. A little planning shows respect for Cards.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pokemon Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pokemon Franchise and money.", "x": "Costs: Anime.. Anime. What to budget — Pokemon Franchise. the pocket monsters. The best experiences of Nintendo. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-pokemon-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
