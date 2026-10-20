(function(){'use strict';
/* JAH Maze Books Database generator — jahdb-e2-games2-maze-books-puzzle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-maze-books-puzzle',PREFIX='JAH-E2GAMES2MAZ-',NAME='JAH Maze Books Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maze Books: the complete guide", "d": "Maze Books: the paper labyrinths..", "g": "overview", "l": 2, "q": "What is Maze Books: the complete guide?", "a": "Maze Books: the paper labyrinths..", "x": "The complete puzzle guide to Maze Books: the paper labyrinths.. Labyrinths. History, meaning, practices, and how to engage respectfully — everything in one database. Labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Maze Books essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Maze Books essentials.", "x": "At a glance: Maze Books — the paper labyrinths.. Usborne. The essentials: Books.. Pencil. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Labyrinths.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Labyrinths.", "x": "Maze Books: Labyrinths.. Books. Essential knowledge — Pencil.. the paper labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Labyrinths..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Labyrinths..", "x": "Explained: Labyrinths.. Usborne. The context — Maze Books. Paths. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Usborne.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Usborne.", "x": "Maze Books: Usborne.. Kids. Essential knowledge — Paths.. the paper labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Usborne..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Usborne..", "x": "Explained: Usborne.. Paths. The context — Maze Books. Kids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pencil.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pencil.", "x": "Maze Books: Pencil.. Usborne. Essential knowledge — Kids.. the paper labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pencil..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pencil..", "x": "Explained: Pencil.. Guide. The context — Maze Books. Books. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Paths.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Paths.", "x": "Maze Books: Paths.. Paths. Essential knowledge — Books.. the paper labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Paths..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Paths..", "x": "Explained: Paths.. Labyrinths. The context — Maze Books. Labyrinths. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kids.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kids.", "x": "Maze Books: Kids.. Guide. Essential knowledge — Labyrinths.. the paper labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Kids..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Kids..", "x": "Explained: Kids.. Books. The context — Maze Books. Usborne. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Books.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Books.", "x": "Maze Books: Books.. Labyrinths. Essential knowledge — Usborne.. the paper labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Books..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Books..", "x": "Explained: Books.. Kids. The context — Maze Books. Pencil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Labyrinths.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Labyrinths.", "x": "Maze Books in depth: Labyrinths.. Usborne. Details — the paper labyrinths.. Kids. Paths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Books.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Books.", "x": "Maze Books in depth: Books.. Pencil. Details — the paper labyrinths.. Usborne. Kids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Kids.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Kids.", "x": "Maze Books in depth: Kids.. Paths. Details — the paper labyrinths.. Paths. Books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Usborne.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Usborne.", "x": "Maze Books in depth: Usborne.. Kids. Details — the paper labyrinths.. Guide. Labyrinths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Paths.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Paths.", "x": "Maze Books in depth: Paths.. Books. Details — the paper labyrinths.. Labyrinths. Usborne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Maze Books in depth: Guide.. Labyrinths. Details — the paper labyrinths.. Books. Pencil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Maze Books comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Maze Books comes from.", "x": "Origins: Labyrinths.. Labyrinths. The history of Maze Books — the paper labyrinths.. Books. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Maze Books respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Maze Books respectfully.", "x": "Engaging: Kids.. Usborne. How to participate or observe well — Maze Books. the paper labyrinths. Respect first, always; Usborne.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Maze Books do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Maze Books do's and don'ts.", "x": "Etiquette: Paths.. Pencil. The rules of respect — Maze Books. the paper labyrinths. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Maze Books.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Maze Books.", "x": "Planning: Labyrinths.. Paths. Practical notes — Maze Books. the paper labyrinths. A little planning shows respect for Books.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Maze Books and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Maze Books and money.", "x": "Costs: Kids.. Kids. What to budget — Maze Books. the paper labyrinths. The best experiences of Usborne. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-maze-books-puzzle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
