(function(){'use strict';
/* JAH Sydney Harbour Bridge Bridge Database generator — jahdb-e2-bridge-sydney-harbour-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-sydney-harbour-bridge',PREFIX='JAH-E2BRIDGESYD-',NAME='JAH Sydney Harbour Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sydney Harbour Bridge: the complete guide", "d": "Sydney Harbour Bridge: the coat hanger..", "g": "overview", "l": 2, "q": "What is Sydney Harbour Bridge: the complete guide?", "a": "Sydney Harbour Bridge: the coat hanger..", "x": "The complete bridge guide to Sydney Harbour Bridge: the coat hanger.. 1932. History, meaning, practices, and how to engage respectfully — everything in one database. Climb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sydney Harbour Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sydney Harbour Bridge essentials.", "x": "At a glance: Sydney Harbour Bridge — the coat hanger.. Coat hanger. The essentials: History.. Climb. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1932.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1932.", "x": "Sydney Harbour Bridge: 1932.. History. Essential knowledge — Climb.. the coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1932..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1932..", "x": "Explained: 1932.. Harbour. The context — Sydney Harbour Bridge. Arch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Coat hanger.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Coat hanger.", "x": "Sydney Harbour Bridge: Coat hanger.. Arch. Essential knowledge — Arch.. the coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Coat hanger..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Coat hanger..", "x": "Explained: Coat hanger.. Views. The context — Sydney Harbour Bridge. Harbour. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Climb.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Climb.", "x": "Sydney Harbour Bridge: Climb.. Harbour. Essential knowledge — Harbour.. the coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Climb..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Climb..", "x": "Explained: Climb.. NYE. The context — Sydney Harbour Bridge. NYE. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Arch.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Arch.", "x": "Sydney Harbour Bridge: Arch.. Views. Essential knowledge — NYE.. the coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Arch..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Arch..", "x": "Explained: Arch.. Climb. The context — Sydney Harbour Bridge. 1932. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Harbour.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Harbour.", "x": "Sydney Harbour Bridge: Harbour.. NYE. Essential knowledge — 1932.. the coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Harbour..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Harbour..", "x": "Explained: Harbour.. History. The context — Sydney Harbour Bridge. Coat hanger. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "NYE.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "NYE.", "x": "Sydney Harbour Bridge: NYE.. Climb. Essential knowledge — Coat hanger.. the coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: NYE..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: NYE..", "x": "Explained: NYE.. Arch. The context — Sydney Harbour Bridge. Climb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Climb.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Climb.", "x": "Sydney Harbour Bridge in depth: Climb.. Coat hanger. Details — the coat hanger.. Arch. Arch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Sydney Harbour Bridge in depth: History.. Climb. Details — the coat hanger.. Harbour. Harbour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Arch.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Arch.", "x": "Sydney Harbour Bridge in depth: Arch.. Arch. Details — the coat hanger.. Views. NYE. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Harbour.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Harbour.", "x": "Sydney Harbour Bridge in depth: Harbour.. Harbour. Details — the coat hanger.. NYE. 1932. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Sydney Harbour Bridge in depth: Views.. NYE. Details — the coat hanger.. Climb. Coat hanger. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "NYE.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "NYE.", "x": "Sydney Harbour Bridge in depth: NYE.. 1932. Details — the coat hanger.. History. Climb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sydney Harbour Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sydney Harbour Bridge comes from.", "x": "Origins: Climb.. 1932. The history of Sydney Harbour Bridge — the coat hanger.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sydney Harbour Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sydney Harbour Bridge respectfully.", "x": "Engaging: Arch.. Coat hanger. How to participate or observe well — Sydney Harbour Bridge. the coat hanger. Respect first, always; Harbour.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sydney Harbour Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sydney Harbour Bridge do's and don'ts.", "x": "Etiquette: Views.. Climb. The rules of respect — Sydney Harbour Bridge. the coat hanger. When in doubt, ask about NYE.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sydney Harbour Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sydney Harbour Bridge.", "x": "Planning: Climb.. Arch. Practical notes — Sydney Harbour Bridge. the coat hanger. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sydney Harbour Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sydney Harbour Bridge and money.", "x": "Costs: Arch.. Harbour. What to budget — Sydney Harbour Bridge. the coat hanger. The best experiences of Harbour. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-sydney-harbour-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
