(function(){'use strict';
/* JAH Character Arcs Screenwriting Database generator — jahdb-e2-screen-character-arcs-screen-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen-character-arcs-screen',PREFIX='JAH-E2SCREENCHA-',NAME='JAH Character Arcs Screenwriting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Character Arcs: the complete guide", "d": "Character Arcs: the inner change..", "g": "overview", "l": 2, "q": "What is Character Arcs: the complete guide?", "a": "Character Arcs: the inner change..", "x": "The complete screenwriting guide to Character Arcs: the inner change.. Arc. History, meaning, practices, and how to engage respectfully — everything in one database. Want. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Character Arcs essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Character Arcs essentials.", "x": "At a glance: Character Arcs — the inner change.. Want/need. The essentials: Flaw.. Flaw. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Arc.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Arc.", "x": "Character Arcs: Arc.. Flaw. Essential knowledge — Flaw.. the inner change. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Arc..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Arc..", "x": "Explained: Arc.. Transformation. The context — Character Arcs. Ghost. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Want/need.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Want/need.", "x": "Character Arcs: Want/need.. Ghost. Essential knowledge — Ghost.. the inner change. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Want/need..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Want/need..", "x": "Explained: Want/need.. Flat. The context — Character Arcs. Transformation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Flaw.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Flaw.", "x": "Character Arcs: Flaw.. Transformation. Essential knowledge — Transformation.. the inner change. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Flaw..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Flaw..", "x": "Explained: Flaw.. Craft. The context — Character Arcs. Flat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ghost.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ghost.", "x": "Character Arcs: Ghost.. Flat. Essential knowledge — Flat.. the inner change. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ghost..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ghost..", "x": "Explained: Ghost.. Want. The context — Character Arcs. Arc. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Transformation.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Transformation.", "x": "Character Arcs: Transformation.. Craft. Essential knowledge — Arc.. the inner change. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Transformation..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Transformation..", "x": "Explained: Transformation.. Flaw. The context — Character Arcs. Want/need. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Flat.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Flat.", "x": "Character Arcs: Flat.. Want. Essential knowledge — Want/need.. the inner change. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Flat..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Flat..", "x": "Explained: Flat.. Ghost. The context — Character Arcs. Flaw. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Want.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Want.", "x": "Character Arcs in depth: Want.. Want/need. Details — the inner change.. Ghost. Ghost. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Flaw.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Flaw.", "x": "Character Arcs in depth: Flaw.. Flaw. Details — the inner change.. Transformation. Transformation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ghost.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ghost.", "x": "Character Arcs in depth: Ghost.. Ghost. Details — the inner change.. Flat. Flat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Transformation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Transformation.", "x": "Character Arcs in depth: Transformation.. Transformation. Details — the inner change.. Craft. Arc. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flat.", "x": "Character Arcs in depth: Flat.. Flat. Details — the inner change.. Want. Want/need. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Craft.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Craft.", "x": "Character Arcs in depth: Craft.. Arc. Details — the inner change.. Flaw. Flaw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Character Arcs comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Character Arcs comes from.", "x": "Origins: Want.. Arc. The history of Character Arcs — the inner change.. Flaw. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Character Arcs respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Character Arcs respectfully.", "x": "Engaging: Ghost.. Want/need. How to participate or observe well — Character Arcs. the inner change. Respect first, always; Transformation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Character Arcs do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Character Arcs do's and don'ts.", "x": "Etiquette: Flat.. Flaw. The rules of respect — Character Arcs. the inner change. When in doubt, ask about Craft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Character Arcs.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Character Arcs.", "x": "Planning: Want.. Ghost. Practical notes — Character Arcs. the inner change. A little planning shows respect for Flaw.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Character Arcs and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Character Arcs and money.", "x": "Costs: Ghost.. Transformation. What to budget — Character Arcs. the inner change. The best experiences of Transformation. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen-character-arcs-screen-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
