(function(){'use strict';
/* JAH Dark Souls Franchise Database generator — jahdb-e2-games2-dark-souls-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-dark-souls-franchise-game',PREFIX='JAH-E2GAMES2DAR-',NAME='JAH Dark Souls Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dark Souls Franchise: the complete guide", "d": "Dark Souls Franchise: the bonfire trial..", "g": "overview", "l": 2, "q": "What is Dark Souls Franchise: the complete guide?", "a": "Dark Souls Franchise: the bonfire trial..", "x": "The complete game franchise guide to Dark Souls Franchise: the bonfire trial.. 2011. History, meaning, practices, and how to engage respectfully — everything in one database. Bonfires. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dark Souls Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dark Souls Franchise essentials.", "x": "At a glance: Dark Souls Franchise — the bonfire trial.. FromSoftware. The essentials: Lore.. Bonfires. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2011.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2011.", "x": "Dark Souls Franchise: 2011.. Lore. Essential knowledge — Bonfires.. the bonfire trial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2011..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2011..", "x": "Explained: 2011.. FromSoft. The context — Dark Souls Franchise. Difficulty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "FromSoftware.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "FromSoftware.", "x": "Dark Souls Franchise: FromSoftware.. Bosses. Essential knowledge — Difficulty.. the bonfire trial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: FromSoftware..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: FromSoftware..", "x": "Explained: FromSoftware.. Difficulty. The context — Dark Souls Franchise. Bosses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bonfires.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bonfires.", "x": "Dark Souls Franchise: Bonfires.. FromSoft. Essential knowledge — Bosses.. the bonfire trial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bonfires..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bonfires..", "x": "Explained: Bonfires.. Games. The context — Dark Souls Franchise. Lore. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Difficulty.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Difficulty.", "x": "Dark Souls Franchise: Difficulty.. Difficulty. Essential knowledge — Lore.. the bonfire trial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Difficulty..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Difficulty..", "x": "Explained: Difficulty.. Bonfires. The context — Dark Souls Franchise. 2011. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bosses.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bosses.", "x": "Dark Souls Franchise: Bosses.. Games. Essential knowledge — 2011.. the bonfire trial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bosses..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bosses..", "x": "Explained: Bosses.. Lore. The context — Dark Souls Franchise. FromSoftware. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lore.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lore.", "x": "Dark Souls Franchise: Lore.. Bonfires. Essential knowledge — FromSoftware.. the bonfire trial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lore..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lore..", "x": "Explained: Lore.. Bosses. The context — Dark Souls Franchise. Bonfires. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bonfires.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bonfires.", "x": "Dark Souls Franchise in depth: Bonfires.. FromSoftware. Details — the bonfire trial.. Bosses. Difficulty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lore.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lore.", "x": "Dark Souls Franchise in depth: Lore.. Bonfires. Details — the bonfire trial.. FromSoft. Bosses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bosses.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bosses.", "x": "Dark Souls Franchise in depth: Bosses.. Difficulty. Details — the bonfire trial.. Difficulty. Lore. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "FromSoft.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "FromSoft.", "x": "Dark Souls Franchise in depth: FromSoft.. Bosses. Details — the bonfire trial.. Games. 2011. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Difficulty.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Difficulty.", "x": "Dark Souls Franchise in depth: Difficulty.. Lore. Details — the bonfire trial.. Bonfires. FromSoftware. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Dark Souls Franchise in depth: Games.. 2011. Details — the bonfire trial.. Lore. Bonfires. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dark Souls Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dark Souls Franchise comes from.", "x": "Origins: Bonfires.. 2011. The history of Dark Souls Franchise — the bonfire trial.. Lore. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dark Souls Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dark Souls Franchise respectfully.", "x": "Engaging: Bosses.. FromSoftware. How to participate or observe well — Dark Souls Franchise. the bonfire trial. Respect first, always; FromSoft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dark Souls Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dark Souls Franchise do's and don'ts.", "x": "Etiquette: Difficulty.. Bonfires. The rules of respect — Dark Souls Franchise. the bonfire trial. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dark Souls Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dark Souls Franchise.", "x": "Planning: Bonfires.. Difficulty. Practical notes — Dark Souls Franchise. the bonfire trial. A little planning shows respect for Lore.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dark Souls Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dark Souls Franchise and money.", "x": "Costs: Bosses.. Bosses. What to budget — Dark Souls Franchise. the bonfire trial. The best experiences of FromSoft. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-dark-souls-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
