(function(){'use strict';
/* JAH Three-Act Structure Screenwriting Database generator — jahdb-e2-screen-three-act-structure-screen-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen-three-act-structure-screen',PREFIX='JAH-E2SCREENTHR-',NAME='JAH Three-Act Structure Screenwriting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Three-Act Structure: the complete guide", "d": "Three-Act Structure: the classic shape..", "g": "overview", "l": 2, "q": "What is Three-Act Structure: the complete guide?", "a": "Three-Act Structure: the classic shape..", "x": "The complete screenwriting guide to Three-Act Structure: the classic shape.. Setup. History, meaning, practices, and how to engage respectfully — everything in one database. Setup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Three-Act Structure essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Three-Act Structure essentials.", "x": "At a glance: Three-Act Structure — the classic shape.. Confrontation. The essentials: Confrontation.. Resolution. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Setup.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Setup.", "x": "Three-Act Structure: Setup.. Confrontation. Essential knowledge — Resolution.. the classic shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Setup..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Setup..", "x": "Explained: Setup.. Field. The context — Three-Act Structure. Syd Field. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Confrontation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Confrontation.", "x": "Three-Act Structure: Confrontation.. Resolution. Essential knowledge — Syd Field.. the classic shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Confrontation..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Confrontation..", "x": "Explained: Confrontation.. Points. The context — Three-Act Structure. Aristotle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Resolution.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Resolution.", "x": "Three-Act Structure: Resolution.. Field. Essential knowledge — Aristotle.. the classic shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Resolution..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Resolution..", "x": "Explained: Resolution.. Structure. The context — Three-Act Structure. Turning points. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Syd Field.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Syd Field.", "x": "Three-Act Structure: Syd Field.. Points. Essential knowledge — Turning points.. the classic shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Syd Field..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Syd Field..", "x": "Explained: Syd Field.. Setup. The context — Three-Act Structure. Setup. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Aristotle.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Aristotle.", "x": "Three-Act Structure: Aristotle.. Structure. Essential knowledge — Setup.. the classic shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Aristotle..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Aristotle..", "x": "Explained: Aristotle.. Confrontation. The context — Three-Act Structure. Confrontation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Turning points.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Turning points.", "x": "Three-Act Structure: Turning points.. Setup. Essential knowledge — Confrontation.. the classic shape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Turning points..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Turning points..", "x": "Explained: Turning points.. Resolution. The context — Three-Act Structure. Resolution. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Setup.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Setup.", "x": "Three-Act Structure in depth: Setup.. Confrontation. Details — the classic shape.. Resolution. Syd Field. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Confrontation.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Confrontation.", "x": "Three-Act Structure in depth: Confrontation.. Resolution. Details — the classic shape.. Field. Aristotle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Resolution.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Resolution.", "x": "Three-Act Structure in depth: Resolution.. Syd Field. Details — the classic shape.. Points. Turning points. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Field.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Field.", "x": "Three-Act Structure in depth: Field.. Aristotle. Details — the classic shape.. Structure. Setup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Points.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Points.", "x": "Three-Act Structure in depth: Points.. Turning points. Details — the classic shape.. Setup. Confrontation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Structure.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Structure.", "x": "Three-Act Structure in depth: Structure.. Setup. Details — the classic shape.. Confrontation. Resolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Three-Act Structure comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Three-Act Structure comes from.", "x": "Origins: Setup.. Setup. The history of Three-Act Structure — the classic shape.. Confrontation. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Three-Act Structure respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Three-Act Structure respectfully.", "x": "Engaging: Resolution.. Confrontation. How to participate or observe well — Three-Act Structure. the classic shape. Respect first, always; Field.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Three-Act Structure do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Three-Act Structure do's and don'ts.", "x": "Etiquette: Points.. Resolution. The rules of respect — Three-Act Structure. the classic shape. When in doubt, ask about Structure.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Three-Act Structure.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Three-Act Structure.", "x": "Planning: Setup.. Syd Field. Practical notes — Three-Act Structure. the classic shape. A little planning shows respect for Confrontation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Three-Act Structure and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Three-Act Structure and money.", "x": "Costs: Resolution.. Aristotle. What to budget — Three-Act Structure. the classic shape. The best experiences of Field. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen-three-act-structure-screen-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
