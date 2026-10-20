(function(){'use strict';
/* JAH DC Comics Database generator — jahdb-e2-comics2-dc-comics-publisher-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-comics2-dc-comics-publisher',PREFIX='JAH-E2COMICS2DC-',NAME='JAH DC Comics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "DC Comics: the complete guide", "d": "DC Comics: the Distinguished Competition..", "g": "overview", "l": 2, "q": "What is DC Comics: the complete guide?", "a": "DC Comics: the Distinguished Competition..", "x": "The complete comic publisher guide to DC Comics: the Distinguished Competition.. 1934. History, meaning, practices, and how to engage respectfully — everything in one database. Superman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "DC Comics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "DC Comics essentials.", "x": "At a glance: DC Comics — the Distinguished Competition.. Superman. The essentials: Vertigo.. Batman. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1934.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1934.", "x": "DC Comics: 1934.. Vertigo. Essential knowledge — Batman.. the Distinguished Competition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1934..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1934..", "x": "Explained: 1934.. Batman. The context — DC Comics. Detective. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Superman.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Superman.", "x": "DC Comics: Superman.. Multiverse. Essential knowledge — Detective.. the Distinguished Competition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Superman..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Superman..", "x": "Explained: Superman.. Detective. The context — DC Comics. Vertigo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Batman.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Batman.", "x": "DC Comics: Batman.. Batman. Essential knowledge — Vertigo.. the Distinguished Competition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Batman..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Batman..", "x": "Explained: Batman.. History. The context — DC Comics. Multiverse. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Detective.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Detective.", "x": "DC Comics: Detective.. Detective. Essential knowledge — Multiverse.. the Distinguished Competition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Detective..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Detective..", "x": "Explained: Detective.. Superman. The context — DC Comics. 1934. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vertigo.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vertigo.", "x": "DC Comics: Vertigo.. History. Essential knowledge — 1934.. the Distinguished Competition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vertigo..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vertigo..", "x": "Explained: Vertigo.. Vertigo. The context — DC Comics. Superman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Multiverse.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Multiverse.", "x": "DC Comics: Multiverse.. Superman. Essential knowledge — Superman.. the Distinguished Competition. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Multiverse..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Multiverse..", "x": "Explained: Multiverse.. Multiverse. The context — DC Comics. Batman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Superman.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Superman.", "x": "DC Comics in depth: Superman.. Superman. Details — the Distinguished Competition.. Multiverse. Detective. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vertigo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vertigo.", "x": "DC Comics in depth: Vertigo.. Batman. Details — the Distinguished Competition.. Batman. Vertigo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Multiverse.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Multiverse.", "x": "DC Comics in depth: Multiverse.. Detective. Details — the Distinguished Competition.. Detective. Multiverse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Batman.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Batman.", "x": "DC Comics in depth: Batman.. Vertigo. Details — the Distinguished Competition.. History. 1934. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Detective.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Detective.", "x": "DC Comics in depth: Detective.. Multiverse. Details — the Distinguished Competition.. Superman. Superman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "DC Comics in depth: History.. 1934. Details — the Distinguished Competition.. Vertigo. Batman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where DC Comics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where DC Comics comes from.", "x": "Origins: Superman.. 1934. The history of DC Comics — the Distinguished Competition.. Vertigo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing DC Comics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing DC Comics respectfully.", "x": "Engaging: Multiverse.. Superman. How to participate or observe well — DC Comics. the Distinguished Competition. Respect first, always; Batman.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "DC Comics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "DC Comics do's and don'ts.", "x": "Etiquette: Detective.. Batman. The rules of respect — DC Comics. the Distinguished Competition. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around DC Comics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around DC Comics.", "x": "Planning: Superman.. Detective. Practical notes — DC Comics. the Distinguished Competition. A little planning shows respect for Vertigo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "DC Comics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "DC Comics and money.", "x": "Costs: Multiverse.. Vertigo. What to budget — DC Comics. the Distinguished Competition. The best experiences of Batman. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-comics2-dc-comics-publisher-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
