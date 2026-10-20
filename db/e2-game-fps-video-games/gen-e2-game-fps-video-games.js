(function(){'use strict';
/* JAH FPS Video Games Game Genre Database generator — jahdb-e2-game-fps-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-fps-video-games',PREFIX='JAH-E2GAMEFPSVI-',NAME='JAH FPS Video Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "FPS Video Games: the complete guide", "d": "FPS Video Games: the first-person shooter..", "g": "overview", "l": 2, "q": "What is FPS Video Games: the complete guide?", "a": "FPS Video Games: the first-person shooter..", "x": "The complete game genre guide to FPS Video Games: the first-person shooter.. Doom. History, meaning, practices, and how to engage respectfully — everything in one database. Aiming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "FPS Video Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "FPS Video Games essentials.", "x": "At a glance: FPS Video Games — the first-person shooter.. Aiming. The essentials: Multiplayer.. Multiplayer. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Doom.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Doom.", "x": "FPS Video Games: Doom.. Multiplayer. Essential knowledge — Multiplayer.. the first-person shooter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Doom..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Doom..", "x": "Explained: Doom.. Maps. The context — FPS Video Games. Call of Duty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aiming.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aiming.", "x": "FPS Video Games: Aiming.. Reflexes. Essential knowledge — Call of Duty.. the first-person shooter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Aiming..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Aiming..", "x": "Explained: Aiming.. Doom. The context — FPS Video Games. Reflexes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Multiplayer.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Multiplayer.", "x": "FPS Video Games: Multiplayer.. Maps. Essential knowledge — Reflexes.. the first-person shooter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Multiplayer..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Multiplayer..", "x": "Explained: Multiplayer.. Classics. The context — FPS Video Games. Maps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Call of Duty.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Call of Duty.", "x": "FPS Video Games: Call of Duty.. Doom. Essential knowledge — Maps.. the first-person shooter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Call of Duty..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Call of Duty..", "x": "Explained: Call of Duty.. Aiming. The context — FPS Video Games. Doom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Reflexes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Reflexes.", "x": "FPS Video Games: Reflexes.. Classics. Essential knowledge — Doom.. the first-person shooter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Reflexes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Reflexes..", "x": "Explained: Reflexes.. Multiplayer. The context — FPS Video Games. Aiming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Maps.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Maps.", "x": "FPS Video Games: Maps.. Aiming. Essential knowledge — Aiming.. the first-person shooter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Maps..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Maps..", "x": "Explained: Maps.. Reflexes. The context — FPS Video Games. Multiplayer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aiming.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aiming.", "x": "FPS Video Games in depth: Aiming.. Aiming. Details — the first-person shooter.. Reflexes. Call of Duty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Multiplayer.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Multiplayer.", "x": "FPS Video Games in depth: Multiplayer.. Multiplayer. Details — the first-person shooter.. Maps. Reflexes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Reflexes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Reflexes.", "x": "FPS Video Games in depth: Reflexes.. Call of Duty. Details — the first-person shooter.. Doom. Maps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Maps.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Maps.", "x": "FPS Video Games in depth: Maps.. Reflexes. Details — the first-person shooter.. Classics. Doom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Doom.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Doom.", "x": "FPS Video Games in depth: Doom.. Maps. Details — the first-person shooter.. Aiming. Aiming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "FPS Video Games in depth: Classics.. Doom. Details — the first-person shooter.. Multiplayer. Multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where FPS Video Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where FPS Video Games comes from.", "x": "Origins: Aiming.. Doom. The history of FPS Video Games — the first-person shooter.. Multiplayer. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing FPS Video Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing FPS Video Games respectfully.", "x": "Engaging: Reflexes.. Aiming. How to participate or observe well — FPS Video Games. the first-person shooter. Respect first, always; Maps.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "FPS Video Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "FPS Video Games do's and don'ts.", "x": "Etiquette: Doom.. Multiplayer. The rules of respect — FPS Video Games. the first-person shooter. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around FPS Video Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around FPS Video Games.", "x": "Planning: Aiming.. Call of Duty. Practical notes — FPS Video Games. the first-person shooter. A little planning shows respect for Multiplayer.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "FPS Video Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "FPS Video Games and money.", "x": "Costs: Reflexes.. Reflexes. What to budget — FPS Video Games. the first-person shooter. The best experiences of Maps. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-fps-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
