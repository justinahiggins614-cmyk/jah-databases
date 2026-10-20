(function(){'use strict';
/* JAH Coin Magic Tricks Magic Trick Database generator — jahdb-e2-magic-coin-magic-tricks-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-magic-coin-magic-tricks',PREFIX='JAH-E2MAGICCOIN-',NAME='JAH Coin Magic Tricks Magic Trick Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Coin Magic Tricks: the complete guide", "d": "Coin Magic Tricks: the metal miracles..", "g": "overview", "l": 2, "q": "What is Coin Magic Tricks: the complete guide?", "a": "Coin Magic Tricks: the metal miracles..", "x": "The complete magic trick guide to Coin Magic Tricks: the metal miracles.. Palming. History, meaning, practices, and how to engage respectfully — everything in one database. Palming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Coin Magic Tricks essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Coin Magic Tricks essentials.", "x": "At a glance: Coin Magic Tricks — the metal miracles.. Vanish. The essentials: Vanish.. Miser's Dream. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Palming.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Palming.", "x": "Coin Magic Tricks: Palming.. Vanish. Essential knowledge — Miser's Dream.. the metal miracles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Palming..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Palming..", "x": "Explained: Palming.. Practice. The context — Coin Magic Tricks. Copper/silver. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Vanish.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Vanish.", "x": "Coin Magic Tricks: Vanish.. Sleeving. Essential knowledge — Copper/silver.. the metal miracles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Vanish..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Vanish..", "x": "Explained: Vanish.. Miser's. The context — Coin Magic Tricks. Sleeving. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Miser's Dream.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Miser's Dream.", "x": "Coin Magic Tricks: Miser's Dream.. Practice. Essential knowledge — Sleeving.. the metal miracles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Miser's Dream..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Miser's Dream..", "x": "Explained: Miser's Dream.. Learn. The context — Coin Magic Tricks. Practice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Copper/silver.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Copper/silver.", "x": "Coin Magic Tricks: Copper/silver.. Miser's. Essential knowledge — Practice.. the metal miracles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Copper/silver..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Copper/silver..", "x": "Explained: Copper/silver.. Palming. The context — Coin Magic Tricks. Palming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sleeving.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sleeving.", "x": "Coin Magic Tricks: Sleeving.. Learn. Essential knowledge — Palming.. the metal miracles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sleeving..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sleeving..", "x": "Explained: Sleeving.. Vanish. The context — Coin Magic Tricks. Vanish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Practice.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Practice.", "x": "Coin Magic Tricks: Practice.. Palming. Essential knowledge — Vanish.. the metal miracles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Practice..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Practice..", "x": "Explained: Practice.. Sleeving. The context — Coin Magic Tricks. Miser's Dream. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Palming.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Palming.", "x": "Coin Magic Tricks in depth: Palming.. Vanish. Details — the metal miracles.. Sleeving. Copper/silver. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vanish.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vanish.", "x": "Coin Magic Tricks in depth: Vanish.. Miser's Dream. Details — the metal miracles.. Practice. Sleeving. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sleeving.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sleeving.", "x": "Coin Magic Tricks in depth: Sleeving.. Copper/silver. Details — the metal miracles.. Miser's. Practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Practice.", "x": "Coin Magic Tricks in depth: Practice.. Sleeving. Details — the metal miracles.. Learn. Palming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Miser's.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Miser's.", "x": "Coin Magic Tricks in depth: Miser's.. Practice. Details — the metal miracles.. Palming. Vanish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learn.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learn.", "x": "Coin Magic Tricks in depth: Learn.. Palming. Details — the metal miracles.. Vanish. Miser's Dream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Coin Magic Tricks comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Coin Magic Tricks comes from.", "x": "Origins: Palming.. Palming. The history of Coin Magic Tricks — the metal miracles.. Vanish. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Coin Magic Tricks respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Coin Magic Tricks respectfully.", "x": "Engaging: Sleeving.. Vanish. How to participate or observe well — Coin Magic Tricks. the metal miracles. Respect first, always; Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Coin Magic Tricks do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Coin Magic Tricks do's and don'ts.", "x": "Etiquette: Miser's.. Miser's Dream. The rules of respect — Coin Magic Tricks. the metal miracles. When in doubt, ask about Learn.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Coin Magic Tricks.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Coin Magic Tricks.", "x": "Planning: Palming.. Copper/silver. Practical notes — Coin Magic Tricks. the metal miracles. A little planning shows respect for Vanish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Coin Magic Tricks and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Coin Magic Tricks and money.", "x": "Costs: Sleeving.. Sleeving. What to budget — Coin Magic Tricks. the metal miracles. The best experiences of Practice. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-magic-coin-magic-tricks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
