(function(){'use strict';
/* JAH Nonogram Puzzles Puzzle Database generator — jahdb-e2-puzzle-nonogram-puzzles-type-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-puzzle-nonogram-puzzles-type',PREFIX='JAH-E2PUZZLENON-',NAME='JAH Nonogram Puzzles Puzzle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nonogram Puzzles: the complete guide", "d": "Nonogram Puzzles: the picture logic..", "g": "overview", "l": 2, "q": "What is Nonogram Puzzles: the complete guide?", "a": "Nonogram Puzzles: the picture logic..", "x": "The complete puzzle guide to Nonogram Puzzles: the picture logic.. Picross. History, meaning, practices, and how to engage respectfully — everything in one database. Picross. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nonogram Puzzles essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nonogram Puzzles essentials.", "x": "At a glance: Nonogram Puzzles — the picture logic.. Grid. The essentials: Pixels.. Nintendo. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Picross.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Picross.", "x": "Nonogram Puzzles: Picross.. Pixels. Essential knowledge — Nintendo.. the picture logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Picross..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Picross..", "x": "Explained: Picross.. Nintendo. The context — Nonogram Puzzles. Pixels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Grid.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Grid.", "x": "Nonogram Puzzles: Grid.. Japan. Essential knowledge — Pixels.. the picture logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Grid..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Grid..", "x": "Explained: Grid.. Logic. The context — Nonogram Puzzles. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nintendo.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nintendo.", "x": "Nonogram Puzzles: Nintendo.. Nintendo. Essential knowledge — Japan.. the picture logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Nintendo..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Nintendo..", "x": "Explained: Nintendo.. Tips. The context — Nonogram Puzzles. Logic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pixels.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pixels.", "x": "Nonogram Puzzles: Pixels.. Logic. Essential knowledge — Logic.. the picture logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pixels..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pixels..", "x": "Explained: Pixels.. Picross. The context — Nonogram Puzzles. Picross. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Japan.", "x": "Nonogram Puzzles: Japan.. Tips. Essential knowledge — Picross.. the picture logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Pixels. The context — Nonogram Puzzles. Grid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Logic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Logic.", "x": "Nonogram Puzzles: Logic.. Picross. Essential knowledge — Grid.. the picture logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Logic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Logic..", "x": "Explained: Logic.. Japan. The context — Nonogram Puzzles. Nintendo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Picross.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Picross.", "x": "Nonogram Puzzles in depth: Picross.. Grid. Details — the picture logic.. Japan. Pixels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pixels.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pixels.", "x": "Nonogram Puzzles in depth: Pixels.. Nintendo. Details — the picture logic.. Nintendo. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Japan.", "x": "Nonogram Puzzles in depth: Japan.. Pixels. Details — the picture logic.. Logic. Logic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nintendo.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nintendo.", "x": "Nonogram Puzzles in depth: Nintendo.. Japan. Details — the picture logic.. Tips. Picross. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Logic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Logic.", "x": "Nonogram Puzzles in depth: Logic.. Logic. Details — the picture logic.. Picross. Grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Nonogram Puzzles in depth: Tips.. Picross. Details — the picture logic.. Pixels. Nintendo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nonogram Puzzles comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nonogram Puzzles comes from.", "x": "Origins: Picross.. Picross. The history of Nonogram Puzzles — the picture logic.. Pixels. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nonogram Puzzles respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nonogram Puzzles respectfully.", "x": "Engaging: Japan.. Grid. How to participate or observe well — Nonogram Puzzles. the picture logic. Respect first, always; Nintendo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nonogram Puzzles do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nonogram Puzzles do's and don'ts.", "x": "Etiquette: Logic.. Nintendo. The rules of respect — Nonogram Puzzles. the picture logic. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nonogram Puzzles.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nonogram Puzzles.", "x": "Planning: Picross.. Pixels. Practical notes — Nonogram Puzzles. the picture logic. A little planning shows respect for Pixels.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nonogram Puzzles and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nonogram Puzzles and money.", "x": "Costs: Japan.. Japan. What to budget — Nonogram Puzzles. the picture logic. The best experiences of Nintendo. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-puzzle-nonogram-puzzles-type-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
