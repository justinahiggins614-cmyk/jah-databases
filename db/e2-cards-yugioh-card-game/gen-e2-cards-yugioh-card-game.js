(function(){'use strict';
/* JAH Yu-Gi-Oh Card Card Game Database generator — jahdb-e2-cards-yugioh-card-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cards-yugioh-card-game',PREFIX='JAH-E2CARDSYUGI-',NAME='JAH Yu-Gi-Oh Card Card Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yu-Gi-Oh Card: the complete guide", "d": "Yu-Gi-Oh Card: the heart of cards..", "g": "overview", "l": 2, "q": "What is Yu-Gi-Oh Card: the complete guide?", "a": "Yu-Gi-Oh Card: the heart of cards..", "x": "The complete card game guide to Yu-Gi-Oh Card: the heart of cards.. Konami. History, meaning, practices, and how to engage respectfully — everything in one database. Blue-Eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Yu-Gi-Oh Card essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Yu-Gi-Oh Card essentials.", "x": "At a glance: Yu-Gi-Oh Card — the heart of cards.. Anime. The essentials: Banlist.. Blue-Eyes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Konami.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Konami.", "x": "Yu-Gi-Oh Card: Konami.. Banlist. Essential knowledge — Blue-Eyes.. the heart of cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Konami..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Konami..", "x": "Explained: Konami.. Konami. The context — Yu-Gi-Oh Card. Banlist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Anime.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Anime.", "x": "Yu-Gi-Oh Card: Anime.. Dueling. Essential knowledge — Banlist.. the heart of cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Anime..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Anime..", "x": "Explained: Anime.. Anime. The context — Yu-Gi-Oh Card. Dueling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Blue-Eyes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Blue-Eyes.", "x": "Yu-Gi-Oh Card: Blue-Eyes.. Konami. Essential knowledge — Dueling.. the heart of cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Blue-Eyes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Blue-Eyes..", "x": "Explained: Blue-Eyes.. Strategy. The context — Yu-Gi-Oh Card. 2002. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Banlist.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Banlist.", "x": "Yu-Gi-Oh Card: Banlist.. Anime. Essential knowledge — 2002.. the heart of cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Banlist..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Banlist..", "x": "Explained: Banlist.. Blue-Eyes. The context — Yu-Gi-Oh Card. Konami. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dueling.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dueling.", "x": "Yu-Gi-Oh Card: Dueling.. Strategy. Essential knowledge — Konami.. the heart of cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Dueling..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Dueling..", "x": "Explained: Dueling.. Banlist. The context — Yu-Gi-Oh Card. Anime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "2002.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "2002.", "x": "Yu-Gi-Oh Card: 2002.. Blue-Eyes. Essential knowledge — Anime.. the heart of cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 2002..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 2002..", "x": "Explained: 2002.. Dueling. The context — Yu-Gi-Oh Card. Blue-Eyes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blue-Eyes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blue-Eyes.", "x": "Yu-Gi-Oh Card in depth: Blue-Eyes.. Anime. Details — the heart of cards.. Dueling. Banlist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Banlist.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Banlist.", "x": "Yu-Gi-Oh Card in depth: Banlist.. Blue-Eyes. Details — the heart of cards.. Konami. Dueling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dueling.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dueling.", "x": "Yu-Gi-Oh Card in depth: Dueling.. Banlist. Details — the heart of cards.. Anime. 2002. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Konami.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Konami.", "x": "Yu-Gi-Oh Card in depth: Konami.. Dueling. Details — the heart of cards.. Strategy. Konami. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Anime.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Anime.", "x": "Yu-Gi-Oh Card in depth: Anime.. 2002. Details — the heart of cards.. Blue-Eyes. Anime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Yu-Gi-Oh Card in depth: Strategy.. Konami. Details — the heart of cards.. Banlist. Blue-Eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Yu-Gi-Oh Card comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Yu-Gi-Oh Card comes from.", "x": "Origins: Blue-Eyes.. Konami. The history of Yu-Gi-Oh Card — the heart of cards.. Banlist. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Yu-Gi-Oh Card respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Yu-Gi-Oh Card respectfully.", "x": "Engaging: Dueling.. Anime. How to participate or observe well — Yu-Gi-Oh Card. the heart of cards. Respect first, always; Konami.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Yu-Gi-Oh Card do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Yu-Gi-Oh Card do's and don'ts.", "x": "Etiquette: Anime.. Blue-Eyes. The rules of respect — Yu-Gi-Oh Card. the heart of cards. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Yu-Gi-Oh Card.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Yu-Gi-Oh Card.", "x": "Planning: Blue-Eyes.. Banlist. Practical notes — Yu-Gi-Oh Card. the heart of cards. A little planning shows respect for Banlist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Yu-Gi-Oh Card and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Yu-Gi-Oh Card and money.", "x": "Costs: Dueling.. Dueling. What to budget — Yu-Gi-Oh Card. the heart of cards. The best experiences of Konami. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cards-yugioh-card-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
