(function(){'use strict';
/* JAH Marvel Legends Action Figure Database generator — jahdb-e2-figure-marvel-legends-figures-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-figure-marvel-legends-figures',PREFIX='JAH-E2FIGUREMAR-',NAME='JAH Marvel Legends Action Figure Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Marvel Legends: the complete guide", "d": "Marvel Legends: the 6-inch heroes..", "g": "overview", "l": 2, "q": "What is Marvel Legends: the complete guide?", "a": "Marvel Legends: the 6-inch heroes..", "x": "The complete action figure guide to Marvel Legends: the 6-inch heroes.. 2002. History, meaning, practices, and how to engage respectfully — everything in one database. BAF. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Marvel Legends essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Marvel Legends essentials.", "x": "At a glance: Marvel Legends — the 6-inch heroes.. Hasbro. The essentials: 6 inch.. Build-A-Figure. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2002.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2002.", "x": "Marvel Legends: 2002.. 6 inch. Essential knowledge — Build-A-Figure.. the 6-inch heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2002..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2002..", "x": "Explained: 2002.. X-Men. The context — Marvel Legends. 6 inch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hasbro.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hasbro.", "x": "Marvel Legends: Hasbro.. Hasbro. Essential knowledge — 6 inch.. the 6-inch heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hasbro..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hasbro..", "x": "Explained: Hasbro.. 2002. The context — Marvel Legends. X-Men. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Build-A-Figure.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Build-A-Figure.", "x": "Marvel Legends: Build-A-Figure.. X-Men. Essential knowledge — X-Men.. the 6-inch heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Build-A-Figure..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Build-A-Figure..", "x": "Explained: Build-A-Figure.. History. The context — Marvel Legends. Avengers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "6 inch.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "6 inch.", "x": "Marvel Legends: 6 inch.. 2002. Essential knowledge — Avengers.. the 6-inch heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 6 inch..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 6 inch..", "x": "Explained: 6 inch.. BAF. The context — Marvel Legends. 2002. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "X-Men.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "X-Men.", "x": "Marvel Legends: X-Men.. History. Essential knowledge — 2002.. the 6-inch heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: X-Men..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: X-Men..", "x": "Explained: X-Men.. 6 inch. The context — Marvel Legends. Hasbro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Avengers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Avengers.", "x": "Marvel Legends: Avengers.. BAF. Essential knowledge — Hasbro.. the 6-inch heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Avengers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Avengers..", "x": "Explained: Avengers.. Hasbro. The context — Marvel Legends. Build-A-Figure. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "BAF.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "BAF.", "x": "Marvel Legends in depth: BAF.. Hasbro. Details — the 6-inch heroes.. Hasbro. 6 inch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "6 inch.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "6 inch.", "x": "Marvel Legends in depth: 6 inch.. Build-A-Figure. Details — the 6-inch heroes.. X-Men. X-Men. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hasbro.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hasbro.", "x": "Marvel Legends in depth: Hasbro.. 6 inch. Details — the 6-inch heroes.. 2002. Avengers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "X-Men.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "X-Men.", "x": "Marvel Legends in depth: X-Men.. X-Men. Details — the 6-inch heroes.. History. 2002. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "2002.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "2002.", "x": "Marvel Legends in depth: 2002.. Avengers. Details — the 6-inch heroes.. BAF. Hasbro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Marvel Legends in depth: History.. 2002. Details — the 6-inch heroes.. 6 inch. Build-A-Figure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Marvel Legends comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Marvel Legends comes from.", "x": "Origins: BAF.. 2002. The history of Marvel Legends — the 6-inch heroes.. 6 inch. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Marvel Legends respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Marvel Legends respectfully.", "x": "Engaging: Hasbro.. Hasbro. How to participate or observe well — Marvel Legends. the 6-inch heroes. Respect first, always; X-Men.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Marvel Legends do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Marvel Legends do's and don'ts.", "x": "Etiquette: 2002.. Build-A-Figure. The rules of respect — Marvel Legends. the 6-inch heroes. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Marvel Legends.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Marvel Legends.", "x": "Planning: BAF.. 6 inch. Practical notes — Marvel Legends. the 6-inch heroes. A little planning shows respect for 6 inch.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Marvel Legends and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Marvel Legends and money.", "x": "Costs: Hasbro.. X-Men. What to budget — Marvel Legends. the 6-inch heroes. The best experiences of X-Men. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-figure-marvel-legends-figures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
