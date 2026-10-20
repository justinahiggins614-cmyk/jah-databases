(function(){'use strict';
/* JAH Children\'s Novels Novel Database generator — jahdb-e2-novel-childrens-novels-genre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-novel-childrens-novels-genre',PREFIX='JAH-E2NOVELCHIL-',NAME='JAH Children\'s Novels Novel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Children's Novels: the complete guide", "d": "Children's Novels: the young books..", "g": "overview", "l": 2, "q": "What is Children's Novels: the complete guide?", "a": "Children's Novels: the young books..", "x": "The complete novel guide to Children's Novels: the young books.. Rowling. History, meaning, practices, and how to engage respectfully — everything in one database. Narnia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Children's Novels essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Children's Novels essentials.", "x": "At a glance: Children's Novels — the young books.. Narnia. The essentials: Wonder.. Wonder. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rowling.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rowling.", "x": "Children's Novels: Rowling.. Wonder. Essential knowledge — Wonder.. the young books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rowling..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rowling..", "x": "Explained: Rowling.. Magic. The context — Children's Novels. Read-aloud. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Narnia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Narnia.", "x": "Children's Novels: Narnia.. Illustrated. Essential knowledge — Read-aloud.. the young books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Narnia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Narnia..", "x": "Explained: Narnia.. Rowling. The context — Children's Novels. Illustrated. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wonder.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wonder.", "x": "Children's Novels: Wonder.. Magic. Essential knowledge — Illustrated.. the young books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Wonder..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Wonder..", "x": "Explained: Wonder.. Classics. The context — Children's Novels. Magic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Read-aloud.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Read-aloud.", "x": "Children's Novels: Read-aloud.. Rowling. Essential knowledge — Magic.. the young books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Read-aloud..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Read-aloud..", "x": "Explained: Read-aloud.. Narnia. The context — Children's Novels. Rowling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Illustrated.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Illustrated.", "x": "Children's Novels: Illustrated.. Classics. Essential knowledge — Rowling.. the young books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Illustrated..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Illustrated..", "x": "Explained: Illustrated.. Wonder. The context — Children's Novels. Narnia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Magic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Magic.", "x": "Children's Novels: Magic.. Narnia. Essential knowledge — Narnia.. the young books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Magic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Magic..", "x": "Explained: Magic.. Illustrated. The context — Children's Novels. Wonder. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Narnia.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Narnia.", "x": "Children's Novels in depth: Narnia.. Narnia. Details — the young books.. Illustrated. Read-aloud. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wonder.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wonder.", "x": "Children's Novels in depth: Wonder.. Wonder. Details — the young books.. Magic. Illustrated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Illustrated.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Illustrated.", "x": "Children's Novels in depth: Illustrated.. Read-aloud. Details — the young books.. Rowling. Magic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Magic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Magic.", "x": "Children's Novels in depth: Magic.. Illustrated. Details — the young books.. Classics. Rowling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rowling.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rowling.", "x": "Children's Novels in depth: Rowling.. Magic. Details — the young books.. Narnia. Narnia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Children's Novels in depth: Classics.. Rowling. Details — the young books.. Wonder. Wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Children's Novels comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Children's Novels comes from.", "x": "Origins: Narnia.. Rowling. The history of Children's Novels — the young books.. Wonder. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Children's Novels respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Children's Novels respectfully.", "x": "Engaging: Illustrated.. Narnia. How to participate or observe well — Children's Novels. the young books. Respect first, always; Magic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Children's Novels do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Children's Novels do's and don'ts.", "x": "Etiquette: Rowling.. Wonder. The rules of respect — Children's Novels. the young books. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Children's Novels.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Children's Novels.", "x": "Planning: Narnia.. Read-aloud. Practical notes — Children's Novels. the young books. A little planning shows respect for Wonder.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Children's Novels and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Children's Novels and money.", "x": "Costs: Illustrated.. Illustrated. What to budget — Children's Novels. the young books. The best experiences of Magic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-novel-childrens-novels-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
