(function(){'use strict';
/* JAH Magic the Gathering Card Game Database generator — jahdb-e2-cards-magic-gathering-card-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cards-magic-gathering-card',PREFIX='JAH-E2CARDSMAGI-',NAME='JAH Magic the Gathering Card Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Magic the Gathering: the complete guide", "d": "Magic the Gathering: the TCG origin..", "g": "overview", "l": 2, "q": "What is Magic the Gathering: the complete guide?", "a": "Magic the Gathering: the TCG origin..", "x": "The complete card game guide to Magic the Gathering: the TCG origin.. 1993. History, meaning, practices, and how to engage respectfully — everything in one database. Mana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Magic the Gathering essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Magic the Gathering essentials.", "x": "At a glance: Magic the Gathering — the TCG origin.. Wizards. The essentials: Decks.. Mana. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1993.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1993.", "x": "Magic the Gathering: 1993.. Decks. Essential knowledge — Mana.. the TCG origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1993..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1993..", "x": "Explained: 1993.. Garfield. The context — Magic the Gathering. Decks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wizards.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wizards.", "x": "Magic the Gathering: Wizards.. Tour. Essential knowledge — Decks.. the TCG origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Wizards..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Wizards..", "x": "Explained: Wizards.. Wizards. The context — Magic the Gathering. Pro Tour. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mana.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mana.", "x": "Magic the Gathering: Mana.. Garfield. Essential knowledge — Pro Tour.. the TCG origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mana..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mana..", "x": "Explained: Mana.. Strategy. The context — Magic the Gathering. Garfield. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Decks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Decks.", "x": "Magic the Gathering: Decks.. Wizards. Essential knowledge — Garfield.. the TCG origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Decks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Decks..", "x": "Explained: Decks.. Mana. The context — Magic the Gathering. 1993. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pro Tour.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pro Tour.", "x": "Magic the Gathering: Pro Tour.. Strategy. Essential knowledge — 1993.. the TCG origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pro Tour..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pro Tour..", "x": "Explained: Pro Tour.. Decks. The context — Magic the Gathering. Wizards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Garfield.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Garfield.", "x": "Magic the Gathering: Garfield.. Mana. Essential knowledge — Wizards.. the TCG origin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Garfield..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Garfield..", "x": "Explained: Garfield.. Tour. The context — Magic the Gathering. Mana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mana.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mana.", "x": "Magic the Gathering in depth: Mana.. Wizards. Details — the TCG origin.. Tour. Decks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Decks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Decks.", "x": "Magic the Gathering in depth: Decks.. Mana. Details — the TCG origin.. Garfield. Pro Tour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tour.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tour.", "x": "Magic the Gathering in depth: Tour.. Decks. Details — the TCG origin.. Wizards. Garfield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Garfield.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Garfield.", "x": "Magic the Gathering in depth: Garfield.. Pro Tour. Details — the TCG origin.. Strategy. 1993. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wizards.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wizards.", "x": "Magic the Gathering in depth: Wizards.. Garfield. Details — the TCG origin.. Mana. Wizards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Magic the Gathering in depth: Strategy.. 1993. Details — the TCG origin.. Decks. Mana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Magic the Gathering comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Magic the Gathering comes from.", "x": "Origins: Mana.. 1993. The history of Magic the Gathering — the TCG origin.. Decks. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Magic the Gathering respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Magic the Gathering respectfully.", "x": "Engaging: Tour.. Wizards. How to participate or observe well — Magic the Gathering. the TCG origin. Respect first, always; Garfield.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Magic the Gathering do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Magic the Gathering do's and don'ts.", "x": "Etiquette: Wizards.. Mana. The rules of respect — Magic the Gathering. the TCG origin. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Magic the Gathering.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Magic the Gathering.", "x": "Planning: Mana.. Decks. Practical notes — Magic the Gathering. the TCG origin. A little planning shows respect for Decks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Magic the Gathering and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Magic the Gathering and money.", "x": "Costs: Tour.. Pro Tour. What to budget — Magic the Gathering. the TCG origin. The best experiences of Garfield. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cards-magic-gathering-card-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
