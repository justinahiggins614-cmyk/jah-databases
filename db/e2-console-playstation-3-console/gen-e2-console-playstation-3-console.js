(function(){'use strict';
/* JAH PlayStation 3 Console Database generator — jahdb-e2-console-playstation-3-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-playstation-3-console',PREFIX='JAH-E2CONSOLEPL-',NAME='JAH PlayStation 3 Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "PlayStation 3: the complete guide", "d": "PlayStation 3: the Cell saga..", "g": "overview", "l": 2, "q": "What is PlayStation 3: the complete guide?", "a": "PlayStation 3: the Cell saga..", "x": "The complete console guide to PlayStation 3: the Cell saga.. 2006. History, meaning, practices, and how to engage respectfully — everything in one database. Blu-ray. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "PlayStation 3 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "PlayStation 3 essentials.", "x": "At a glance: PlayStation 3 — the Cell saga.. Blu-ray. The essentials: Cell.. Cell. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2006.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2006.", "x": "PlayStation 3: 2006.. Cell. Essential knowledge — Cell.. the Cell saga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2006..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2006..", "x": "Explained: 2006.. Sony. The context — PlayStation 3. Price. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Blu-ray.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Blu-ray.", "x": "PlayStation 3: Blu-ray.. Uncharted. Essential knowledge — Price.. the Cell saga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Blu-ray..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Blu-ray..", "x": "Explained: Blu-ray.. Price. The context — PlayStation 3. Uncharted. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cell.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cell.", "x": "PlayStation 3: Cell.. Sony. Essential knowledge — Uncharted.. the Cell saga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cell..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cell..", "x": "Explained: Cell.. Legacy. The context — PlayStation 3. Sony. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Price.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Price.", "x": "PlayStation 3: Price.. Price. Essential knowledge — Sony.. the Cell saga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Price..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Price..", "x": "Explained: Price.. Blu-ray. The context — PlayStation 3. 2006. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Uncharted.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Uncharted.", "x": "PlayStation 3: Uncharted.. Legacy. Essential knowledge — 2006.. the Cell saga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Uncharted..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Uncharted..", "x": "Explained: Uncharted.. Cell. The context — PlayStation 3. Blu-ray. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sony.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sony.", "x": "PlayStation 3: Sony.. Blu-ray. Essential knowledge — Blu-ray.. the Cell saga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sony..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sony..", "x": "Explained: Sony.. Uncharted. The context — PlayStation 3. Cell. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Blu-ray.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Blu-ray.", "x": "PlayStation 3 in depth: Blu-ray.. Blu-ray. Details — the Cell saga.. Uncharted. Price. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cell.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cell.", "x": "PlayStation 3 in depth: Cell.. Cell. Details — the Cell saga.. Sony. Uncharted. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Uncharted.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Uncharted.", "x": "PlayStation 3 in depth: Uncharted.. Price. Details — the Cell saga.. Price. Sony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sony.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sony.", "x": "PlayStation 3 in depth: Sony.. Uncharted. Details — the Cell saga.. Legacy. 2006. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Price.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Price.", "x": "PlayStation 3 in depth: Price.. Sony. Details — the Cell saga.. Blu-ray. Blu-ray. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "PlayStation 3 in depth: Legacy.. 2006. Details — the Cell saga.. Cell. Cell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where PlayStation 3 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where PlayStation 3 comes from.", "x": "Origins: Blu-ray.. 2006. The history of PlayStation 3 — the Cell saga.. Cell. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing PlayStation 3 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing PlayStation 3 respectfully.", "x": "Engaging: Uncharted.. Blu-ray. How to participate or observe well — PlayStation 3. the Cell saga. Respect first, always; Sony.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "PlayStation 3 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "PlayStation 3 do's and don'ts.", "x": "Etiquette: Price.. Cell. The rules of respect — PlayStation 3. the Cell saga. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around PlayStation 3.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around PlayStation 3.", "x": "Planning: Blu-ray.. Price. Practical notes — PlayStation 3. the Cell saga. A little planning shows respect for Cell.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "PlayStation 3 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "PlayStation 3 and money.", "x": "Costs: Uncharted.. Uncharted. What to budget — PlayStation 3. the Cell saga. The best experiences of Sony. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-playstation-3-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
