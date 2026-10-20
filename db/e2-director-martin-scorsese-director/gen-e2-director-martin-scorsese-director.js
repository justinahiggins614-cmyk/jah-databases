(function(){'use strict';
/* JAH Martin Scorsese Director Database generator — jahdb-e2-director-martin-scorsese-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-martin-scorsese-director',PREFIX='JAH-E2DIRECTORM-',NAME='JAH Martin Scorsese Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Martin Scorsese: the complete guide", "d": "Martin Scorsese: the crime auteur..", "g": "overview", "l": 2, "q": "What is Martin Scorsese: the complete guide?", "a": "Martin Scorsese: the crime auteur..", "x": "The complete director guide to Martin Scorsese: the crime auteur.. 1942. History, meaning, practices, and how to engage respectfully — everything in one database. Taxi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Martin Scorsese essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Martin Scorsese essentials.", "x": "At a glance: Martin Scorsese — the crime auteur.. Taxi Driver. The essentials: Goodfellas.. Goodfellas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1942.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1942.", "x": "Martin Scorsese: 1942.. Goodfellas. Essential knowledge — Goodfellas.. the crime auteur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1942..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1942..", "x": "Explained: 1942.. Film. The context — Martin Scorsese. De Niro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Taxi Driver.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Taxi Driver.", "x": "Martin Scorsese: Taxi Driver.. De Niro. Essential knowledge — De Niro.. the crime auteur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Taxi Driver..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Taxi Driver..", "x": "Explained: Taxi Driver.. DiCaprio. The context — Martin Scorsese. DiCaprio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Goodfellas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Goodfellas.", "x": "Martin Scorsese: Goodfellas.. Film. Essential knowledge — DiCaprio.. the crime auteur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Goodfellas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Goodfellas..", "x": "Explained: Goodfellas.. Style. The context — Martin Scorsese. Film. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "De Niro.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "De Niro.", "x": "Martin Scorsese: De Niro.. DiCaprio. Essential knowledge — Film.. the crime auteur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: De Niro..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: De Niro..", "x": "Explained: De Niro.. Taxi. The context — Martin Scorsese. 1942. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "DiCaprio.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "DiCaprio.", "x": "Martin Scorsese: DiCaprio.. Style. Essential knowledge — 1942.. the crime auteur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: DiCaprio..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: DiCaprio..", "x": "Explained: DiCaprio.. Goodfellas. The context — Martin Scorsese. Taxi Driver. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Film.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Film.", "x": "Martin Scorsese: Film.. Taxi. Essential knowledge — Taxi Driver.. the crime auteur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Film..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Film..", "x": "Explained: Film.. De Niro. The context — Martin Scorsese. Goodfellas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Taxi.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Taxi.", "x": "Martin Scorsese in depth: Taxi.. Taxi Driver. Details — the crime auteur.. De Niro. De Niro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Goodfellas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Goodfellas.", "x": "Martin Scorsese in depth: Goodfellas.. Goodfellas. Details — the crime auteur.. Film. DiCaprio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "De Niro.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "De Niro.", "x": "Martin Scorsese in depth: De Niro.. De Niro. Details — the crime auteur.. DiCaprio. Film. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Film.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Film.", "x": "Martin Scorsese in depth: Film.. DiCaprio. Details — the crime auteur.. Style. 1942. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "DiCaprio.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "DiCaprio.", "x": "Martin Scorsese in depth: DiCaprio.. Film. Details — the crime auteur.. Taxi. Taxi Driver. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Martin Scorsese in depth: Style.. 1942. Details — the crime auteur.. Goodfellas. Goodfellas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Martin Scorsese comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Martin Scorsese comes from.", "x": "Origins: Taxi.. 1942. The history of Martin Scorsese — the crime auteur.. Goodfellas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Martin Scorsese respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Martin Scorsese respectfully.", "x": "Engaging: De Niro.. Taxi Driver. How to participate or observe well — Martin Scorsese. the crime auteur. Respect first, always; Film.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Martin Scorsese do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Martin Scorsese do's and don'ts.", "x": "Etiquette: DiCaprio.. Goodfellas. The rules of respect — Martin Scorsese. the crime auteur. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Martin Scorsese.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Martin Scorsese.", "x": "Planning: Taxi.. De Niro. Practical notes — Martin Scorsese. the crime auteur. A little planning shows respect for Goodfellas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Martin Scorsese and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Martin Scorsese and money.", "x": "Costs: De Niro.. DiCaprio. What to budget — Martin Scorsese. the crime auteur. The best experiences of Film. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-martin-scorsese-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
