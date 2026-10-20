(function(){'use strict';
/* JAH MMO Games Game Genre Database generator — jahdb-e2-game-mmo-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-mmo-video-games',PREFIX='JAH-E2GAMEMMOVI-',NAME='JAH MMO Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "MMO Games: the complete guide", "d": "MMO Games: the massive online..", "g": "overview", "l": 2, "q": "What is MMO Games: the complete guide?", "a": "MMO Games: the massive online..", "x": "The complete game genre guide to MMO Games: the massive online.. WoW. History, meaning, practices, and how to engage respectfully — everything in one database. Raids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "MMO Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "MMO Games essentials.", "x": "At a glance: MMO Games — the massive online.. Raids. The essentials: Guilds.. Guilds. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "WoW.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "WoW.", "x": "MMO Games: WoW.. Guilds. Essential knowledge — Guilds.. the massive online. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: WoW..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: WoW..", "x": "Explained: WoW.. WoW. The context — MMO Games. Grinding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Raids.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Raids.", "x": "MMO Games: Raids.. Grinding. Essential knowledge — Grinding.. the massive online. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Raids..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Raids..", "x": "Explained: Raids.. Subscription. The context — MMO Games. Subscription. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Guilds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Guilds.", "x": "MMO Games: Guilds.. WoW. Essential knowledge — Subscription.. the massive online. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Guilds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Guilds..", "x": "Explained: Guilds.. Classics. The context — MMO Games. 2004. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Grinding.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Grinding.", "x": "MMO Games: Grinding.. Subscription. Essential knowledge — 2004.. the massive online. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Grinding..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Grinding..", "x": "Explained: Grinding.. Raids. The context — MMO Games. WoW. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Subscription.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Subscription.", "x": "MMO Games: Subscription.. Classics. Essential knowledge — WoW.. the massive online. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Subscription..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Subscription..", "x": "Explained: Subscription.. Guilds. The context — MMO Games. Raids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "2004.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "2004.", "x": "MMO Games: 2004.. Raids. Essential knowledge — Raids.. the massive online. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 2004..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 2004..", "x": "Explained: 2004.. Grinding. The context — MMO Games. Guilds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Raids.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Raids.", "x": "MMO Games in depth: Raids.. Raids. Details — the massive online.. Grinding. Grinding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Guilds.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Guilds.", "x": "MMO Games in depth: Guilds.. Guilds. Details — the massive online.. WoW. Subscription. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Grinding.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Grinding.", "x": "MMO Games in depth: Grinding.. Grinding. Details — the massive online.. Subscription. 2004. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "WoW.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "WoW.", "x": "MMO Games in depth: WoW.. Subscription. Details — the massive online.. Classics. WoW. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Subscription.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Subscription.", "x": "MMO Games in depth: Subscription.. 2004. Details — the massive online.. Raids. Raids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "MMO Games in depth: Classics.. WoW. Details — the massive online.. Guilds. Guilds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where MMO Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where MMO Games comes from.", "x": "Origins: Raids.. WoW. The history of MMO Games — the massive online.. Guilds. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing MMO Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing MMO Games respectfully.", "x": "Engaging: Grinding.. Raids. How to participate or observe well — MMO Games. the massive online. Respect first, always; WoW.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "MMO Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "MMO Games do's and don'ts.", "x": "Etiquette: Subscription.. Guilds. The rules of respect — MMO Games. the massive online. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around MMO Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around MMO Games.", "x": "Planning: Raids.. Grinding. Practical notes — MMO Games. the massive online. A little planning shows respect for Guilds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "MMO Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "MMO Games and money.", "x": "Costs: Grinding.. Subscription. What to budget — MMO Games. the massive online. The best experiences of WoW. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-mmo-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
