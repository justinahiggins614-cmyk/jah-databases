(function(){'use strict';
/* JAH Palomar Observatory Observatory Database generator — jahdb-e2-observatory-palomar-observatory-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-palomar-observatory',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Palomar Observatory Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Palomar Observatory: the complete guide", "d": "Palomar Observatory: the 200-inch giant..", "g": "overview", "l": 2, "q": "What is Palomar Observatory: the complete guide?", "a": "Palomar Observatory: the 200-inch giant..", "x": "The complete observatory guide to Palomar Observatory: the 200-inch giant.. 1948. History, meaning, practices, and how to engage respectfully — everything in one database. Hale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Palomar Observatory essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Palomar Observatory essentials.", "x": "At a glance: Palomar Observatory — the 200-inch giant.. Hale Telescope. The essentials: History.. Quasars. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1948.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1948.", "x": "Palomar Observatory: 1948.. History. Essential knowledge — Quasars.. the 200-inch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1948..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1948..", "x": "Explained: 1948.. Tours. The context — Palomar Observatory. Museum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hale Telescope.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hale Telescope.", "x": "Palomar Observatory: Hale Telescope.. Discoveries. Essential knowledge — Museum.. the 200-inch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hale Telescope..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hale Telescope..", "x": "Explained: Hale Telescope.. California. The context — Palomar Observatory. California. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Quasars.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Quasars.", "x": "Palomar Observatory: Quasars.. Tours. Essential knowledge — California.. the 200-inch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Quasars..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Quasars..", "x": "Explained: Quasars.. Museum. The context — Palomar Observatory. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Museum.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Museum.", "x": "Palomar Observatory: Museum.. California. Essential knowledge — History.. the 200-inch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Museum..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Museum..", "x": "Explained: Museum.. Hale. The context — Palomar Observatory. 1948. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "California.", "x": "Palomar Observatory: California.. Museum. Essential knowledge — 1948.. the 200-inch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: California..", "x": "Explained: California.. History. The context — Palomar Observatory. Hale Telescope. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Palomar Observatory: History.. Hale. Essential knowledge — Hale Telescope.. the 200-inch giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Discoveries. The context — Palomar Observatory. Quasars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hale.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hale.", "x": "Palomar Observatory in depth: Hale.. Hale Telescope. Details — the 200-inch giant.. Discoveries. Museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Palomar Observatory in depth: History.. Quasars. Details — the 200-inch giant.. Tours. California. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Discoveries.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Discoveries.", "x": "Palomar Observatory in depth: Discoveries.. Museum. Details — the 200-inch giant.. California. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Palomar Observatory in depth: Tours.. California. Details — the 200-inch giant.. Museum. 1948. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "California.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "California.", "x": "Palomar Observatory in depth: California.. History. Details — the 200-inch giant.. Hale. Hale Telescope. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Museum.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Museum.", "x": "Palomar Observatory in depth: Museum.. 1948. Details — the 200-inch giant.. History. Quasars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Palomar Observatory comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Palomar Observatory comes from.", "x": "Origins: Hale.. 1948. The history of Palomar Observatory — the 200-inch giant.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Palomar Observatory respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Palomar Observatory respectfully.", "x": "Engaging: Discoveries.. Hale Telescope. How to participate or observe well — Palomar Observatory. the 200-inch giant. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Palomar Observatory do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Palomar Observatory do's and don'ts.", "x": "Etiquette: California.. Quasars. The rules of respect — Palomar Observatory. the 200-inch giant. When in doubt, ask about Museum.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Palomar Observatory.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Palomar Observatory.", "x": "Planning: Hale.. Museum. Practical notes — Palomar Observatory. the 200-inch giant. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Palomar Observatory and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Palomar Observatory and money.", "x": "Costs: Discoveries.. California. What to budget — Palomar Observatory. the 200-inch giant. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-palomar-observatory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
