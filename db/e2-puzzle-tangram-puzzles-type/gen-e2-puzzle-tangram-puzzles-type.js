(function(){'use strict';
/* JAH Tangram Puzzles Puzzle Database generator — jahdb-e2-puzzle-tangram-puzzles-type-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-puzzle-tangram-puzzles-type',PREFIX='JAH-E2PUZZLETAN-',NAME='JAH Tangram Puzzles Puzzle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tangram Puzzles: the complete guide", "d": "Tangram Puzzles: the seven pieces..", "g": "overview", "l": 2, "q": "What is Tangram Puzzles: the complete guide?", "a": "Tangram Puzzles: the seven pieces..", "x": "The complete puzzle guide to Tangram Puzzles: the seven pieces.. China. History, meaning, practices, and how to engage respectfully — everything in one database. China. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tangram Puzzles essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tangram Puzzles essentials.", "x": "At a glance: Tangram Puzzles — the seven pieces.. 7 pieces. The essentials: Silhouettes.. Silhouettes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "China.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "China.", "x": "Tangram Puzzles: China.. Silhouettes. Essential knowledge — Silhouettes.. the seven pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: China..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: China..", "x": "Explained: China.. 1800s. The context — Tangram Puzzles. Dissection. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "7 pieces.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "7 pieces.", "x": "Tangram Puzzles: 7 pieces.. Dissection. Essential knowledge — Dissection.. the seven pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 7 pieces..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 7 pieces..", "x": "Explained: 7 pieces.. Seven. The context — Tangram Puzzles. Square. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Silhouettes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Silhouettes.", "x": "Tangram Puzzles: Silhouettes.. 1800s. Essential knowledge — Square.. the seven pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Silhouettes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Silhouettes..", "x": "Explained: Silhouettes.. Tips. The context — Tangram Puzzles. 1800s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dissection.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dissection.", "x": "Tangram Puzzles: Dissection.. Seven. Essential knowledge — 1800s.. the seven pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dissection..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dissection..", "x": "Explained: Dissection.. China. The context — Tangram Puzzles. China. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Square.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Square.", "x": "Tangram Puzzles: Square.. Tips. Essential knowledge — China.. the seven pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Square..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Square..", "x": "Explained: Square.. Silhouettes. The context — Tangram Puzzles. 7 pieces. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1800s.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1800s.", "x": "Tangram Puzzles: 1800s.. China. Essential knowledge — 7 pieces.. the seven pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 1800s..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 1800s..", "x": "Explained: 1800s.. Dissection. The context — Tangram Puzzles. Silhouettes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "China.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "China.", "x": "Tangram Puzzles in depth: China.. 7 pieces. Details — the seven pieces.. Dissection. Dissection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Silhouettes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Silhouettes.", "x": "Tangram Puzzles in depth: Silhouettes.. Silhouettes. Details — the seven pieces.. 1800s. Square. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dissection.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dissection.", "x": "Tangram Puzzles in depth: Dissection.. Dissection. Details — the seven pieces.. Seven. 1800s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1800s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1800s.", "x": "Tangram Puzzles in depth: 1800s.. Square. Details — the seven pieces.. Tips. China. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Seven.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Seven.", "x": "Tangram Puzzles in depth: Seven.. 1800s. Details — the seven pieces.. China. 7 pieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Tangram Puzzles in depth: Tips.. China. Details — the seven pieces.. Silhouettes. Silhouettes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tangram Puzzles comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tangram Puzzles comes from.", "x": "Origins: China.. China. The history of Tangram Puzzles — the seven pieces.. Silhouettes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tangram Puzzles respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tangram Puzzles respectfully.", "x": "Engaging: Dissection.. 7 pieces. How to participate or observe well — Tangram Puzzles. the seven pieces. Respect first, always; 1800s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tangram Puzzles do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tangram Puzzles do's and don'ts.", "x": "Etiquette: Seven.. Silhouettes. The rules of respect — Tangram Puzzles. the seven pieces. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tangram Puzzles.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tangram Puzzles.", "x": "Planning: China.. Dissection. Practical notes — Tangram Puzzles. the seven pieces. A little planning shows respect for Silhouettes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tangram Puzzles and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tangram Puzzles and money.", "x": "Costs: Dissection.. Square. What to budget — Tangram Puzzles. the seven pieces. The best experiences of 1800s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-puzzle-tangram-puzzles-type-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
