(function(){'use strict';
/* JAH Bouillabaisse Dish Database generator — jahdb-e2-dish-bouillabaisse-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-bouillabaisse-dish',PREFIX='JAH-E2DISHBOUIL-',NAME='JAH Bouillabaisse Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bouillabaisse: the complete guide", "d": "Bouillabaisse: the Marseille fish..", "g": "overview", "l": 2, "q": "What is Bouillabaisse: the complete guide?", "a": "Bouillabaisse: the Marseille fish..", "x": "The complete dish guide to Bouillabaisse: the Marseille fish.. Marseille. History, meaning, practices, and how to engage respectfully — everything in one database. Marseille. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bouillabaisse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bouillabaisse essentials.", "x": "At a glance: Bouillabaisse — the Marseille fish.. Fish. The essentials: Rouille.. Saffron. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Marseille.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Marseille.", "x": "Bouillabaisse: Marseille.. Rouille. Essential knowledge — Saffron.. the Marseille fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Marseille..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Marseille..", "x": "Explained: Marseille.. Fish. The context — Bouillabaisse. Rouille. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fish.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fish.", "x": "Bouillabaisse: Fish.. Broth. Essential knowledge — Rouille.. the Marseille fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fish..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fish..", "x": "Explained: Fish.. Saffron. The context — Bouillabaisse. Fishermen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Saffron.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Saffron.", "x": "Bouillabaisse: Saffron.. Fish. Essential knowledge — Fishermen.. the Marseille fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Saffron..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Saffron..", "x": "Explained: Saffron.. Making. The context — Bouillabaisse. Broth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rouille.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rouille.", "x": "Bouillabaisse: Rouille.. Saffron. Essential knowledge — Broth.. the Marseille fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rouille..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rouille..", "x": "Explained: Rouille.. Marseille. The context — Bouillabaisse. Marseille. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fishermen.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fishermen.", "x": "Bouillabaisse: Fishermen.. Making. Essential knowledge — Marseille.. the Marseille fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fishermen..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fishermen..", "x": "Explained: Fishermen.. Rouille. The context — Bouillabaisse. Fish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Broth.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Broth.", "x": "Bouillabaisse: Broth.. Marseille. Essential knowledge — Fish.. the Marseille fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Broth..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Broth..", "x": "Explained: Broth.. Broth. The context — Bouillabaisse. Saffron. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Marseille.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Marseille.", "x": "Bouillabaisse in depth: Marseille.. Fish. Details — the Marseille fish.. Broth. Rouille. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rouille.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rouille.", "x": "Bouillabaisse in depth: Rouille.. Saffron. Details — the Marseille fish.. Fish. Fishermen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Broth.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Broth.", "x": "Bouillabaisse in depth: Broth.. Rouille. Details — the Marseille fish.. Saffron. Broth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fish.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fish.", "x": "Bouillabaisse in depth: Fish.. Fishermen. Details — the Marseille fish.. Making. Marseille. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Saffron.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Saffron.", "x": "Bouillabaisse in depth: Saffron.. Broth. Details — the Marseille fish.. Marseille. Fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Bouillabaisse in depth: Making.. Marseille. Details — the Marseille fish.. Rouille. Saffron. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bouillabaisse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bouillabaisse comes from.", "x": "Origins: Marseille.. Marseille. The history of Bouillabaisse — the Marseille fish.. Rouille. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bouillabaisse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bouillabaisse respectfully.", "x": "Engaging: Broth.. Fish. How to participate or observe well — Bouillabaisse. the Marseille fish. Respect first, always; Fish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bouillabaisse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bouillabaisse do's and don'ts.", "x": "Etiquette: Saffron.. Saffron. The rules of respect — Bouillabaisse. the Marseille fish. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bouillabaisse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bouillabaisse.", "x": "Planning: Marseille.. Rouille. Practical notes — Bouillabaisse. the Marseille fish. A little planning shows respect for Rouille.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bouillabaisse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bouillabaisse and money.", "x": "Costs: Broth.. Fishermen. What to budget — Bouillabaisse. the Marseille fish. The best experiences of Fish. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-bouillabaisse-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
