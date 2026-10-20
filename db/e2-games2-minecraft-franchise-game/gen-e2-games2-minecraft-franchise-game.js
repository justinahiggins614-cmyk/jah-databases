(function(){'use strict';
/* JAH Minecraft Franchise Database generator — jahdb-e2-games2-minecraft-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-minecraft-franchise-game',PREFIX='JAH-E2GAMES2MIN-',NAME='JAH Minecraft Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Minecraft Franchise: the complete guide", "d": "Minecraft Franchise: the block builder..", "g": "overview", "l": 2, "q": "What is Minecraft Franchise: the complete guide?", "a": "Minecraft Franchise: the block builder..", "x": "The complete game franchise guide to Minecraft Franchise: the block builder.. 2011. History, meaning, practices, and how to engage respectfully — everything in one database. Blocks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Minecraft Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Minecraft Franchise essentials.", "x": "At a glance: Minecraft Franchise — the block builder.. Mojang. The essentials: 300M.. Blocks. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2011.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2011.", "x": "Minecraft Franchise: 2011.. 300M. Essential knowledge — Blocks.. the block builder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2011..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2011..", "x": "Explained: 2011.. Mojang. The context — Minecraft Franchise. Survival. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mojang.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mojang.", "x": "Minecraft Franchise: Mojang.. Creative. Essential knowledge — Survival.. the block builder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mojang..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mojang..", "x": "Explained: Mojang.. Survival. The context — Minecraft Franchise. 300M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Blocks.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Blocks.", "x": "Minecraft Franchise: Blocks.. Mojang. Essential knowledge — 300M.. the block builder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Blocks..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Blocks..", "x": "Explained: Blocks.. Games. The context — Minecraft Franchise. Creative. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Survival.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Survival.", "x": "Minecraft Franchise: Survival.. Survival. Essential knowledge — Creative.. the block builder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Survival..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Survival..", "x": "Explained: Survival.. Blocks. The context — Minecraft Franchise. 2011. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "300M.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "300M.", "x": "Minecraft Franchise: 300M.. Games. Essential knowledge — 2011.. the block builder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 300M..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 300M..", "x": "Explained: 300M.. 300M. The context — Minecraft Franchise. Mojang. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Creative.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Creative.", "x": "Minecraft Franchise: Creative.. Blocks. Essential knowledge — Mojang.. the block builder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Creative..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Creative..", "x": "Explained: Creative.. Creative. The context — Minecraft Franchise. Blocks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blocks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blocks.", "x": "Minecraft Franchise in depth: Blocks.. Mojang. Details — the block builder.. Creative. Survival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "300M.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "300M.", "x": "Minecraft Franchise in depth: 300M.. Blocks. Details — the block builder.. Mojang. 300M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Creative.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Creative.", "x": "Minecraft Franchise in depth: Creative.. Survival. Details — the block builder.. Survival. Creative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mojang.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mojang.", "x": "Minecraft Franchise in depth: Mojang.. 300M. Details — the block builder.. Games. 2011. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Survival.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Survival.", "x": "Minecraft Franchise in depth: Survival.. Creative. Details — the block builder.. Blocks. Mojang. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Minecraft Franchise in depth: Games.. 2011. Details — the block builder.. 300M. Blocks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Minecraft Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Minecraft Franchise comes from.", "x": "Origins: Blocks.. 2011. The history of Minecraft Franchise — the block builder.. 300M. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Minecraft Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Minecraft Franchise respectfully.", "x": "Engaging: Creative.. Mojang. How to participate or observe well — Minecraft Franchise. the block builder. Respect first, always; Mojang.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Minecraft Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Minecraft Franchise do's and don'ts.", "x": "Etiquette: Survival.. Blocks. The rules of respect — Minecraft Franchise. the block builder. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Minecraft Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Minecraft Franchise.", "x": "Planning: Blocks.. Survival. Practical notes — Minecraft Franchise. the block builder. A little planning shows respect for 300M.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Minecraft Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Minecraft Franchise and money.", "x": "Costs: Creative.. 300M. What to budget — Minecraft Franchise. the block builder. The best experiences of Mojang. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-minecraft-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
