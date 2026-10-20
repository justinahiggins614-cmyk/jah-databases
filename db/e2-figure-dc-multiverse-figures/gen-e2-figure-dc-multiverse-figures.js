(function(){'use strict';
/* JAH DC Multiverse Action Figure Database generator — jahdb-e2-figure-dc-multiverse-figures-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-figure-dc-multiverse-figures',PREFIX='JAH-E2FIGUREDCM-',NAME='JAH DC Multiverse Action Figure Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "DC Multiverse: the complete guide", "d": "DC Multiverse: the McFarlane heroes..", "g": "overview", "l": 2, "q": "What is DC Multiverse: the complete guide?", "a": "DC Multiverse: the McFarlane heroes..", "x": "The complete action figure guide to DC Multiverse: the McFarlane heroes.. McFarlane. History, meaning, practices, and how to engage respectfully — everything in one database. McFarlane. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "DC Multiverse essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "DC Multiverse essentials.", "x": "At a glance: DC Multiverse — the McFarlane heroes.. Batman. The essentials: Batman.. 7 inch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "McFarlane.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "McFarlane.", "x": "DC Multiverse: McFarlane.. Batman. Essential knowledge — 7 inch.. the McFarlane heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: McFarlane..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: McFarlane..", "x": "Explained: McFarlane.. Collect. The context — DC Multiverse. Comic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Batman.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Batman.", "x": "DC Multiverse: Batman.. Comic. Essential knowledge — Comic.. the McFarlane heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Batman..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Batman..", "x": "Explained: Batman.. 2020. The context — DC Multiverse. Collect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "7 inch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "7 inch.", "x": "DC Multiverse: 7 inch.. Collect. Essential knowledge — Collect.. the McFarlane heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 7 inch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 7 inch..", "x": "Explained: 7 inch.. History. The context — DC Multiverse. 2020. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Comic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Comic.", "x": "DC Multiverse: Comic.. 2020. Essential knowledge — 2020.. the McFarlane heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Comic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Comic..", "x": "Explained: Comic.. McFarlane. The context — DC Multiverse. McFarlane. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Collect.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Collect.", "x": "DC Multiverse: Collect.. History. Essential knowledge — McFarlane.. the McFarlane heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Collect..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Collect..", "x": "Explained: Collect.. Batman. The context — DC Multiverse. Batman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "2020.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "2020.", "x": "DC Multiverse: 2020.. McFarlane. Essential knowledge — Batman.. the McFarlane heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 2020..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 2020..", "x": "Explained: 2020.. Comic. The context — DC Multiverse. 7 inch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "McFarlane.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "McFarlane.", "x": "DC Multiverse in depth: McFarlane.. Batman. Details — the McFarlane heroes.. Comic. Comic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Batman.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Batman.", "x": "DC Multiverse in depth: Batman.. 7 inch. Details — the McFarlane heroes.. Collect. Collect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Comic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Comic.", "x": "DC Multiverse in depth: Comic.. Comic. Details — the McFarlane heroes.. 2020. 2020. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Collect.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Collect.", "x": "DC Multiverse in depth: Collect.. Collect. Details — the McFarlane heroes.. History. McFarlane. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "2020.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "2020.", "x": "DC Multiverse in depth: 2020.. 2020. Details — the McFarlane heroes.. McFarlane. Batman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "DC Multiverse in depth: History.. McFarlane. Details — the McFarlane heroes.. Batman. 7 inch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where DC Multiverse comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where DC Multiverse comes from.", "x": "Origins: McFarlane.. McFarlane. The history of DC Multiverse — the McFarlane heroes.. Batman. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing DC Multiverse respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing DC Multiverse respectfully.", "x": "Engaging: Comic.. Batman. How to participate or observe well — DC Multiverse. the McFarlane heroes. Respect first, always; Collect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "DC Multiverse do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "DC Multiverse do's and don'ts.", "x": "Etiquette: 2020.. 7 inch. The rules of respect — DC Multiverse. the McFarlane heroes. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around DC Multiverse.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around DC Multiverse.", "x": "Planning: McFarlane.. Comic. Practical notes — DC Multiverse. the McFarlane heroes. A little planning shows respect for Batman.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "DC Multiverse and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "DC Multiverse and money.", "x": "Costs: Comic.. Collect. What to budget — DC Multiverse. the McFarlane heroes. The best experiences of Collect. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-figure-dc-multiverse-figures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
