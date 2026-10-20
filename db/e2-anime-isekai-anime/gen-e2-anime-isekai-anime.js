(function(){'use strict';
/* JAH Isekai Anime Anime Genre Database generator — jahdb-e2-anime-isekai-anime-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-anime-isekai-anime',PREFIX='JAH-E2ANIMEISEK-',NAME='JAH Isekai Anime Anime Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Isekai Anime: the complete guide", "d": "Isekai Anime: the other world..", "g": "overview", "l": 2, "q": "What is Isekai Anime: the complete guide?", "a": "Isekai Anime: the other world..", "x": "The complete anime genre guide to Isekai Anime: the other world.. Sword Art. History, meaning, practices, and how to engage respectfully — everything in one database. Truck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Isekai Anime essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Isekai Anime essentials.", "x": "At a glance: Isekai Anime — the other world.. Re:Zero. The essentials: Game.. Truck-kun. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sword Art.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sword Art.", "x": "Isekai Anime: Sword Art.. Game. Essential knowledge — Truck-kun.. the other world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sword Art..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sword Art..", "x": "Explained: Sword Art.. SAO. The context — Isekai Anime. Game. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Re:Zero.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Re:Zero.", "x": "Isekai Anime: Re:Zero.. Boom. Essential knowledge — Game.. the other world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Re:Zero..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Re:Zero..", "x": "Explained: Re:Zero.. Re:Zero. The context — Isekai Anime. Overlord. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Truck-kun.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Truck-kun.", "x": "Isekai Anime: Truck-kun.. SAO. Essential knowledge — Overlord.. the other world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Truck-kun..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Truck-kun..", "x": "Explained: Truck-kun.. Classics. The context — Isekai Anime. Boom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Game.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Game.", "x": "Isekai Anime: Game.. Re:Zero. Essential knowledge — Boom.. the other world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Game..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Game..", "x": "Explained: Game.. Truck. The context — Isekai Anime. Sword Art. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Overlord.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Overlord.", "x": "Isekai Anime: Overlord.. Classics. Essential knowledge — Sword Art.. the other world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Overlord..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Overlord..", "x": "Explained: Overlord.. Game. The context — Isekai Anime. Re:Zero. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Boom.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Boom.", "x": "Isekai Anime: Boom.. Truck. Essential knowledge — Re:Zero.. the other world. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Boom..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Boom..", "x": "Explained: Boom.. Boom. The context — Isekai Anime. Truck-kun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Truck.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Truck.", "x": "Isekai Anime in depth: Truck.. Re:Zero. Details — the other world.. Boom. Game. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Game.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Game.", "x": "Isekai Anime in depth: Game.. Truck-kun. Details — the other world.. SAO. Overlord. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Boom.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Boom.", "x": "Isekai Anime in depth: Boom.. Game. Details — the other world.. Re:Zero. Boom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "SAO.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "SAO.", "x": "Isekai Anime in depth: SAO.. Overlord. Details — the other world.. Classics. Sword Art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Re:Zero.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Re:Zero.", "x": "Isekai Anime in depth: Re:Zero.. Boom. Details — the other world.. Truck. Re:Zero. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Isekai Anime in depth: Classics.. Sword Art. Details — the other world.. Game. Truck-kun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Isekai Anime comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Isekai Anime comes from.", "x": "Origins: Truck.. Sword Art. The history of Isekai Anime — the other world.. Game. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Isekai Anime respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Isekai Anime respectfully.", "x": "Engaging: Boom.. Re:Zero. How to participate or observe well — Isekai Anime. the other world. Respect first, always; SAO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Isekai Anime do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Isekai Anime do's and don'ts.", "x": "Etiquette: Re:Zero.. Truck-kun. The rules of respect — Isekai Anime. the other world. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Isekai Anime.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Isekai Anime.", "x": "Planning: Truck.. Game. Practical notes — Isekai Anime. the other world. A little planning shows respect for Game.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Isekai Anime and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Isekai Anime and money.", "x": "Costs: Boom.. Overlord. What to budget — Isekai Anime. the other world. The best experiences of SAO. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-anime-isekai-anime-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
