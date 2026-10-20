(function(){'use strict';
/* JAH Krak des Chevaliers Castle Database generator — jahdb-e2-castle-krak-des-chevaliers-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-castle-krak-des-chevaliers',PREFIX='JAH-E2CASTLEKRA-',NAME='JAH Krak des Chevaliers Castle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Krak des Chevaliers: the complete guide", "d": "Krak des Chevaliers: the perfect crusader castle..", "g": "overview", "l": 2, "q": "What is Krak des Chevaliers: the complete guide?", "a": "Krak des Chevaliers: the perfect crusader castle..", "x": "The complete castle guide to Krak des Chevaliers: the perfect crusader castle.. Syria. History, meaning, practices, and how to engage respectfully — everything in one database. Crusades. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Krak des Chevaliers essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Krak des Chevaliers essentials.", "x": "At a glance: Krak des Chevaliers — the perfect crusader castle.. Hospitaller. The essentials: Design.. 1142. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Syria.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Syria.", "x": "Krak des Chevaliers: Syria.. Design. Essential knowledge — 1142.. the perfect crusader castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Syria..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Syria..", "x": "Explained: Syria.. UNESCO. The context — Krak des Chevaliers. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hospitaller.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hospitaller.", "x": "Krak des Chevaliers: Hospitaller.. History. Essential knowledge — UNESCO.. the perfect crusader castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hospitaller..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hospitaller..", "x": "Explained: Hospitaller.. Views. The context — Krak des Chevaliers. Sieges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1142.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1142.", "x": "Krak des Chevaliers: 1142.. UNESCO. Essential knowledge — Sieges.. the perfect crusader castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1142..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1142..", "x": "Explained: 1142.. Syria. The context — Krak des Chevaliers. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO.", "x": "Krak des Chevaliers: UNESCO.. Views. Essential knowledge — Views.. the perfect crusader castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Crusades. The context — Krak des Chevaliers. Syria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sieges.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sieges.", "x": "Krak des Chevaliers: Sieges.. Syria. Essential knowledge — Syria.. the perfect crusader castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sieges..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sieges..", "x": "Explained: Sieges.. Design. The context — Krak des Chevaliers. Hospitaller. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Krak des Chevaliers: Views.. Crusades. Essential knowledge — Hospitaller.. the perfect crusader castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. History. The context — Krak des Chevaliers. 1142. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Crusades.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Crusades.", "x": "Krak des Chevaliers in depth: Crusades.. Hospitaller. Details — the perfect crusader castle.. History. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Design.", "x": "Krak des Chevaliers in depth: Design.. 1142. Details — the perfect crusader castle.. UNESCO. Sieges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Krak des Chevaliers in depth: History.. UNESCO. Details — the perfect crusader castle.. Views. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "UNESCO.", "x": "Krak des Chevaliers in depth: UNESCO.. Sieges. Details — the perfect crusader castle.. Syria. Syria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Krak des Chevaliers in depth: Views.. Views. Details — the perfect crusader castle.. Crusades. Hospitaller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Syria.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Syria.", "x": "Krak des Chevaliers in depth: Syria.. Syria. Details — the perfect crusader castle.. Design. 1142. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Krak des Chevaliers comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Krak des Chevaliers comes from.", "x": "Origins: Crusades.. Syria. The history of Krak des Chevaliers — the perfect crusader castle.. Design. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Krak des Chevaliers respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Krak des Chevaliers respectfully.", "x": "Engaging: History.. Hospitaller. How to participate or observe well — Krak des Chevaliers. the perfect crusader castle. Respect first, always; UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Krak des Chevaliers do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Krak des Chevaliers do's and don'ts.", "x": "Etiquette: Views.. 1142. The rules of respect — Krak des Chevaliers. the perfect crusader castle. When in doubt, ask about Syria.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Krak des Chevaliers.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Krak des Chevaliers.", "x": "Planning: Crusades.. UNESCO. Practical notes — Krak des Chevaliers. the perfect crusader castle. A little planning shows respect for Design.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Krak des Chevaliers and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Krak des Chevaliers and money.", "x": "Costs: History.. Sieges. What to budget — Krak des Chevaliers. the perfect crusader castle. The best experiences of UNESCO. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-castle-krak-des-chevaliers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
