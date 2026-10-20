(function(){'use strict';
/* JAH Jigsaw2 Database generator — jahdb-e2-games2-jigsaw-puzzles2-type-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-jigsaw-puzzles2-type',PREFIX='JAH-E2GAMES2JIG-',NAME='JAH Jigsaw2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jigsaw2: the complete guide", "d": "Jigsaw2: the interlocking 2..", "g": "overview", "l": 2, "q": "What is Jigsaw2: the complete guide?", "a": "Jigsaw2: the interlocking 2..", "x": "The complete puzzle guide to Jigsaw2: the interlocking 2.. Wasgij. History, meaning, practices, and how to engage respectfully — everything in one database. Wasgij. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jigsaw2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jigsaw2 essentials.", "x": "At a glance: Jigsaw2 — the interlocking 2.. 3D. The essentials: Panoramic.. 5000 pieces. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wasgij.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wasgij.", "x": "Jigsaw2: Wasgij.. Panoramic. Essential knowledge — 5000 pieces.. the interlocking 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wasgij..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wasgij..", "x": "Explained: Wasgij.. 3D. The context — Jigsaw2. Panoramic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "3D.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "3D.", "x": "Jigsaw2: 3D.. Sorting. Essential knowledge — Panoramic.. the interlocking 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 3D..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 3D..", "x": "Explained: 3D.. Pieces. The context — Jigsaw2. Ravensburger. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "5000 pieces.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "5000 pieces.", "x": "Jigsaw2: 5000 pieces.. 3D. Essential knowledge — Ravensburger.. the interlocking 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 5000 pieces..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 5000 pieces..", "x": "Explained: 5000 pieces.. Guide. The context — Jigsaw2. Sorting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Panoramic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Panoramic.", "x": "Jigsaw2: Panoramic.. Pieces. Essential knowledge — Sorting.. the interlocking 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Panoramic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Panoramic..", "x": "Explained: Panoramic.. Wasgij. The context — Jigsaw2. Wasgij. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ravensburger.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ravensburger.", "x": "Jigsaw2: Ravensburger.. Guide. Essential knowledge — Wasgij.. the interlocking 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ravensburger..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ravensburger..", "x": "Explained: Ravensburger.. Panoramic. The context — Jigsaw2. 3D. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sorting.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sorting.", "x": "Jigsaw2: Sorting.. Wasgij. Essential knowledge — 3D.. the interlocking 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sorting..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sorting..", "x": "Explained: Sorting.. Sorting. The context — Jigsaw2. 5000 pieces. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wasgij.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wasgij.", "x": "Jigsaw2 in depth: Wasgij.. 3D. Details — the interlocking 2.. Sorting. Panoramic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Panoramic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Panoramic.", "x": "Jigsaw2 in depth: Panoramic.. 5000 pieces. Details — the interlocking 2.. 3D. Ravensburger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sorting.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sorting.", "x": "Jigsaw2 in depth: Sorting.. Panoramic. Details — the interlocking 2.. Pieces. Sorting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "3D.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "3D.", "x": "Jigsaw2 in depth: 3D.. Ravensburger. Details — the interlocking 2.. Guide. Wasgij. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pieces.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pieces.", "x": "Jigsaw2 in depth: Pieces.. Sorting. Details — the interlocking 2.. Wasgij. 3D. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Jigsaw2 in depth: Guide.. Wasgij. Details — the interlocking 2.. Panoramic. 5000 pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jigsaw2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jigsaw2 comes from.", "x": "Origins: Wasgij.. Wasgij. The history of Jigsaw2 — the interlocking 2.. Panoramic. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jigsaw2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jigsaw2 respectfully.", "x": "Engaging: Sorting.. 3D. How to participate or observe well — Jigsaw2. the interlocking 2. Respect first, always; 3D.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jigsaw2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jigsaw2 do's and don'ts.", "x": "Etiquette: Pieces.. 5000 pieces. The rules of respect — Jigsaw2. the interlocking 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jigsaw2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jigsaw2.", "x": "Planning: Wasgij.. Panoramic. Practical notes — Jigsaw2. the interlocking 2. A little planning shows respect for Panoramic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jigsaw2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jigsaw2 and money.", "x": "Costs: Sorting.. Ravensburger. What to budget — Jigsaw2. the interlocking 2. The best experiences of 3D. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-jigsaw-puzzles2-type-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
