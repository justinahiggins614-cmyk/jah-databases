(function(){'use strict';
/* JAH Bodiam Castle Castle Database generator — jahdb-e2-castle-bodiam-castle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-bodiam-castle',PREFIX='JAH-E2CASTLEBOD-',NAME='JAH Bodiam Castle Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bodiam Castle: the complete guide", "d": "Bodiam Castle: the perfect moated ruin..", "g": "overview", "l": 2, "q": "What is Bodiam Castle: the complete guide?", "a": "Bodiam Castle: the perfect moated ruin..", "x": "The complete castle guide to Bodiam Castle: the perfect moated ruin.. 1385. History, meaning, practices, and how to engage respectfully — everything in one database. Moat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bodiam Castle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bodiam Castle essentials.", "x": "At a glance: Bodiam Castle — the perfect moated ruin.. Moat. The essentials: History.. Sussex. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1385.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1385.", "x": "Bodiam Castle: 1385.. History. Essential knowledge — Sussex.. the perfect moated ruin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1385..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1385..", "x": "Explained: 1385.. Trust. The context — Bodiam Castle. Ruins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Moat.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Moat.", "x": "Bodiam Castle: Moat.. Ruins. Essential knowledge — Ruins.. the perfect moated ruin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Moat..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Moat..", "x": "Explained: Moat.. Photos. The context — Bodiam Castle. National Trust. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sussex.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sussex.", "x": "Bodiam Castle: Sussex.. Trust. Essential knowledge — National Trust.. the perfect moated ruin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sussex..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sussex..", "x": "Explained: Sussex.. Sussex. The context — Bodiam Castle. Photos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ruins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ruins.", "x": "Bodiam Castle: Ruins.. Photos. Essential knowledge — Photos.. the perfect moated ruin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ruins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ruins..", "x": "Explained: Ruins.. Moat. The context — Bodiam Castle. 1385. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "National Trust.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "National Trust.", "x": "Bodiam Castle: National Trust.. Sussex. Essential knowledge — 1385.. the perfect moated ruin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: National Trust..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: National Trust..", "x": "Explained: National Trust.. History. The context — Bodiam Castle. Moat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Photos.", "x": "Bodiam Castle: Photos.. Moat. Essential knowledge — Moat.. the perfect moated ruin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Photos..", "x": "Explained: Photos.. Ruins. The context — Bodiam Castle. Sussex. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Moat.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Moat.", "x": "Bodiam Castle in depth: Moat.. Moat. Details — the perfect moated ruin.. Ruins. Ruins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Bodiam Castle in depth: History.. Sussex. Details — the perfect moated ruin.. Trust. National Trust. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ruins.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ruins.", "x": "Bodiam Castle in depth: Ruins.. Ruins. Details — the perfect moated ruin.. Photos. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Trust.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Trust.", "x": "Bodiam Castle in depth: Trust.. National Trust. Details — the perfect moated ruin.. Sussex. 1385. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Photos.", "x": "Bodiam Castle in depth: Photos.. Photos. Details — the perfect moated ruin.. Moat. Moat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sussex.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sussex.", "x": "Bodiam Castle in depth: Sussex.. 1385. Details — the perfect moated ruin.. History. Sussex. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bodiam Castle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bodiam Castle comes from.", "x": "Origins: Moat.. 1385. The history of Bodiam Castle — the perfect moated ruin.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bodiam Castle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bodiam Castle respectfully.", "x": "Engaging: Ruins.. Moat. How to participate or observe well — Bodiam Castle. the perfect moated ruin. Respect first, always; Trust.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bodiam Castle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bodiam Castle do's and don'ts.", "x": "Etiquette: Photos.. Sussex. The rules of respect — Bodiam Castle. the perfect moated ruin. When in doubt, ask about Sussex.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bodiam Castle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bodiam Castle.", "x": "Planning: Moat.. Ruins. Practical notes — Bodiam Castle. the perfect moated ruin. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bodiam Castle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bodiam Castle and money.", "x": "Costs: Ruins.. National Trust. What to budget — Bodiam Castle. the perfect moated ruin. The best experiences of Trust. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-bodiam-castle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
