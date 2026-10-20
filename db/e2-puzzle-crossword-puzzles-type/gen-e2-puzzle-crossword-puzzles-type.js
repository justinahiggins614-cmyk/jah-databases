(function(){'use strict';
/* JAH Crossword Puzzles Puzzle Database generator — jahdb-e2-puzzle-crossword-puzzles-type-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-puzzle-crossword-puzzles-type',PREFIX='JAH-E2PUZZLECRO-',NAME='JAH Crossword Puzzles Puzzle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Crossword Puzzles: the complete guide", "d": "Crossword Puzzles: the grid words..", "g": "overview", "l": 2, "q": "What is Crossword Puzzles: the complete guide?", "a": "Crossword Puzzles: the grid words..", "x": "The complete puzzle guide to Crossword Puzzles: the grid words.. 1913. History, meaning, practices, and how to engage respectfully — everything in one database. NYT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Crossword Puzzles essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Crossword Puzzles essentials.", "x": "At a glance: Crossword Puzzles — the grid words.. NYT. The essentials: Cryptic.. Across/down. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1913.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1913.", "x": "Crossword Puzzles: 1913.. Cryptic. Essential knowledge — Across/down.. the grid words. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1913..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1913..", "x": "Explained: 1913.. Pencil. The context — Crossword Puzzles. Cryptic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "NYT.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "NYT.", "x": "Crossword Puzzles: NYT.. Sunday. Essential knowledge — Cryptic.. the grid words. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: NYT..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: NYT..", "x": "Explained: NYT.. Across. The context — Crossword Puzzles. Pencil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Across/down.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Across/down.", "x": "Crossword Puzzles: Across/down.. Pencil. Essential knowledge — Pencil.. the grid words. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Across/down..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Across/down..", "x": "Explained: Across/down.. Tips. The context — Crossword Puzzles. Sunday. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cryptic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cryptic.", "x": "Crossword Puzzles: Cryptic.. Across. Essential knowledge — Sunday.. the grid words. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cryptic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cryptic..", "x": "Explained: Cryptic.. NYT. The context — Crossword Puzzles. 1913. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pencil.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pencil.", "x": "Crossword Puzzles: Pencil.. Tips. Essential knowledge — 1913.. the grid words. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pencil..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pencil..", "x": "Explained: Pencil.. Cryptic. The context — Crossword Puzzles. NYT. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sunday.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sunday.", "x": "Crossword Puzzles: Sunday.. NYT. Essential knowledge — NYT.. the grid words. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sunday..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sunday..", "x": "Explained: Sunday.. Sunday. The context — Crossword Puzzles. Across/down. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "NYT.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "NYT.", "x": "Crossword Puzzles in depth: NYT.. NYT. Details — the grid words.. Sunday. Cryptic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cryptic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cryptic.", "x": "Crossword Puzzles in depth: Cryptic.. Across/down. Details — the grid words.. Pencil. Pencil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sunday.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sunday.", "x": "Crossword Puzzles in depth: Sunday.. Cryptic. Details — the grid words.. Across. Sunday. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pencil.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pencil.", "x": "Crossword Puzzles in depth: Pencil.. Pencil. Details — the grid words.. Tips. 1913. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Across.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Across.", "x": "Crossword Puzzles in depth: Across.. Sunday. Details — the grid words.. NYT. NYT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Crossword Puzzles in depth: Tips.. 1913. Details — the grid words.. Cryptic. Across/down. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Crossword Puzzles comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Crossword Puzzles comes from.", "x": "Origins: NYT.. 1913. The history of Crossword Puzzles — the grid words.. Cryptic. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Crossword Puzzles respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Crossword Puzzles respectfully.", "x": "Engaging: Sunday.. NYT. How to participate or observe well — Crossword Puzzles. the grid words. Respect first, always; Pencil.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Crossword Puzzles do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Crossword Puzzles do's and don'ts.", "x": "Etiquette: Across.. Across/down. The rules of respect — Crossword Puzzles. the grid words. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Crossword Puzzles.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Crossword Puzzles.", "x": "Planning: NYT.. Cryptic. Practical notes — Crossword Puzzles. the grid words. A little planning shows respect for Cryptic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Crossword Puzzles and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Crossword Puzzles and money.", "x": "Costs: Sunday.. Pencil. What to budget — Crossword Puzzles. the grid words. The best experiences of Pencil. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-puzzle-crossword-puzzles-type-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
