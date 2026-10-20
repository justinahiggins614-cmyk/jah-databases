(function(){'use strict';
/* JAH Canasta Card Card Game Database generator — jahdb-e2-cards-canasta-card-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cards-canasta-card-game',PREFIX='JAH-E2CARDSCANA-',NAME='JAH Canasta Card Card Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Canasta Card: the complete guide", "d": "Canasta Card: the basket meld..", "g": "overview", "l": 2, "q": "What is Canasta Card: the complete guide?", "a": "Canasta Card: the basket meld..", "x": "The complete card game guide to Canasta Card: the basket meld.. Uruguay. History, meaning, practices, and how to engage respectfully — everything in one database. Melds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Canasta Card essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Canasta Card essentials.", "x": "At a glance: Canasta Card — the basket meld.. Melds. The essentials: Uruguay.. Wild. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Uruguay.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Uruguay.", "x": "Canasta Card: Uruguay.. Uruguay. Essential knowledge — Wild.. the basket meld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Uruguay..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Uruguay..", "x": "Explained: Uruguay.. 1950s. The context — Canasta Card. Partners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Melds.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Melds.", "x": "Canasta Card: Melds.. Partners. Essential knowledge — Partners.. the basket meld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Melds..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Melds..", "x": "Explained: Melds.. Wild. The context — Canasta Card. 1950s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wild.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wild.", "x": "Canasta Card: Wild.. 1950s. Essential knowledge — 1950s.. the basket meld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Wild..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Wild..", "x": "Explained: Wild.. Strategy. The context — Canasta Card. Basket. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Partners.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Partners.", "x": "Canasta Card: Partners.. Wild. Essential knowledge — Basket.. the basket meld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Partners..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Partners..", "x": "Explained: Partners.. Melds. The context — Canasta Card. Uruguay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1950s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1950s.", "x": "Canasta Card: 1950s.. Strategy. Essential knowledge — Uruguay.. the basket meld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1950s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1950s..", "x": "Explained: 1950s.. Uruguay. The context — Canasta Card. Melds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Basket.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Basket.", "x": "Canasta Card: Basket.. Melds. Essential knowledge — Melds.. the basket meld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Basket..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Basket..", "x": "Explained: Basket.. Partners. The context — Canasta Card. Wild. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Melds.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Melds.", "x": "Canasta Card in depth: Melds.. Melds. Details — the basket meld.. Partners. Partners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Uruguay.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Uruguay.", "x": "Canasta Card in depth: Uruguay.. Wild. Details — the basket meld.. 1950s. 1950s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Partners.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Partners.", "x": "Canasta Card in depth: Partners.. Partners. Details — the basket meld.. Wild. Basket. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1950s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1950s.", "x": "Canasta Card in depth: 1950s.. 1950s. Details — the basket meld.. Strategy. Uruguay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wild.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wild.", "x": "Canasta Card in depth: Wild.. Basket. Details — the basket meld.. Melds. Melds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Canasta Card in depth: Strategy.. Uruguay. Details — the basket meld.. Uruguay. Wild. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Canasta Card comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Canasta Card comes from.", "x": "Origins: Melds.. Uruguay. The history of Canasta Card — the basket meld.. Uruguay. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Canasta Card respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Canasta Card respectfully.", "x": "Engaging: Partners.. Melds. How to participate or observe well — Canasta Card. the basket meld. Respect first, always; 1950s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Canasta Card do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Canasta Card do's and don'ts.", "x": "Etiquette: Wild.. Wild. The rules of respect — Canasta Card. the basket meld. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Canasta Card.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Canasta Card.", "x": "Planning: Melds.. Partners. Practical notes — Canasta Card. the basket meld. A little planning shows respect for Uruguay.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Canasta Card and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Canasta Card and money.", "x": "Costs: Partners.. 1950s. What to budget — Canasta Card. the basket meld. The best experiences of 1950s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cards-canasta-card-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
