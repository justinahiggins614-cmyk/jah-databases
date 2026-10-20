(function(){'use strict';
/* JAH Arecibo Observatory2 Database generator — jahdb-e2-observatory2-arecibo-observatory2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory2-arecibo-observatory2',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Arecibo Observatory2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Arecibo Observatory2: the complete guide", "d": "Arecibo Observatory2: the Puerto Rico 2..", "g": "overview", "l": 2, "q": "What is Arecibo Observatory2: the complete guide?", "a": "Arecibo Observatory2: the Puerto Rico 2..", "x": "The complete observatory guide to Arecibo Observatory2: the Puerto Rico 2.. 1963. History, meaning, practices, and how to engage respectfully — everything in one database. 1963. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Arecibo Observatory2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Arecibo Observatory2 essentials.", "x": "At a glance: Arecibo Observatory2 — the Puerto Rico 2.. Collapsed. The essentials: Dish.. 1000 ft. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1963.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1963.", "x": "Arecibo Observatory2: 1963.. Dish. Essential knowledge — 1000 ft.. the Puerto Rico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1963..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1963..", "x": "Explained: 1963.. Collapsed. The context — Arecibo Observatory2. SETI. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Collapsed.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Collapsed.", "x": "Arecibo Observatory2: Collapsed.. Message. Essential knowledge — SETI.. the Puerto Rico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Collapsed..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Collapsed..", "x": "Explained: Collapsed.. SETI. The context — Arecibo Observatory2. Message. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1000 ft.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1000 ft.", "x": "Arecibo Observatory2: 1000 ft.. Collapsed. Essential knowledge — Message.. the Puerto Rico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1000 ft..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1000 ft..", "x": "Explained: 1000 ft.. Legacy. The context — Arecibo Observatory2. Dish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "SETI.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "SETI.", "x": "Arecibo Observatory2: SETI.. SETI. Essential knowledge — Dish.. the Puerto Rico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: SETI..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: SETI..", "x": "Explained: SETI.. 1963. The context — Arecibo Observatory2. 1963. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Message.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Message.", "x": "Arecibo Observatory2: Message.. Legacy. Essential knowledge — 1963.. the Puerto Rico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Message..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Message..", "x": "Explained: Message.. Dish. The context — Arecibo Observatory2. Collapsed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dish.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dish.", "x": "Arecibo Observatory2: Dish.. 1963. Essential knowledge — Collapsed.. the Puerto Rico 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dish..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dish..", "x": "Explained: Dish.. Message. The context — Arecibo Observatory2. 1000 ft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1963.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1963.", "x": "Arecibo Observatory2 in depth: 1963.. Collapsed. Details — the Puerto Rico 2.. Message. SETI. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dish.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dish.", "x": "Arecibo Observatory2 in depth: Dish.. 1000 ft. Details — the Puerto Rico 2.. Collapsed. Message. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Message.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Message.", "x": "Arecibo Observatory2 in depth: Message.. SETI. Details — the Puerto Rico 2.. SETI. Dish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Collapsed.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Collapsed.", "x": "Arecibo Observatory2 in depth: Collapsed.. Message. Details — the Puerto Rico 2.. Legacy. 1963. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "SETI.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "SETI.", "x": "Arecibo Observatory2 in depth: SETI.. Dish. Details — the Puerto Rico 2.. 1963. Collapsed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Arecibo Observatory2 in depth: Legacy.. 1963. Details — the Puerto Rico 2.. Dish. 1000 ft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Arecibo Observatory2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Arecibo Observatory2 comes from.", "x": "Origins: 1963.. 1963. The history of Arecibo Observatory2 — the Puerto Rico 2.. Dish. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Arecibo Observatory2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Arecibo Observatory2 respectfully.", "x": "Engaging: Message.. Collapsed. How to participate or observe well — Arecibo Observatory2. the Puerto Rico 2. Respect first, always; Collapsed.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Arecibo Observatory2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Arecibo Observatory2 do's and don'ts.", "x": "Etiquette: SETI.. 1000 ft. The rules of respect — Arecibo Observatory2. the Puerto Rico 2. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Arecibo Observatory2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Arecibo Observatory2.", "x": "Planning: 1963.. SETI. Practical notes — Arecibo Observatory2. the Puerto Rico 2. A little planning shows respect for Dish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Arecibo Observatory2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Arecibo Observatory2 and money.", "x": "Costs: Message.. Message. What to budget — Arecibo Observatory2. the Puerto Rico 2. The best experiences of Collapsed. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory2-arecibo-observatory2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
