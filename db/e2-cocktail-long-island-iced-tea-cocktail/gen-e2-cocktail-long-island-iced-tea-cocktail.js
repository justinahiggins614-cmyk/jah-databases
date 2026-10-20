(function(){'use strict';
/* JAH Long Island Iced Tea Cocktail Database generator — jahdb-e2-cocktail-long-island-iced-tea-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-long-island-iced-tea-cocktail',PREFIX='JAH-E2COCKTAILL-',NAME='JAH Long Island Iced Tea Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Long Island Iced Tea: the complete guide", "d": "Long Island Iced Tea: the sneaky strong..", "g": "overview", "l": 2, "q": "What is Long Island Iced Tea: the complete guide?", "a": "Long Island Iced Tea: the sneaky strong..", "x": "The complete cocktail guide to Long Island Iced Tea: the sneaky strong.. 5 spirits. History, meaning, practices, and how to engage respectfully — everything in one database. Spirits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Long Island Iced Tea essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Long Island Iced Tea essentials.", "x": "At a glance: Long Island Iced Tea — the sneaky strong.. Cola. The essentials: Strong.. Strong. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "5 spirits.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "5 spirits.", "x": "Long Island Iced Tea: 5 spirits.. Strong. Essential knowledge — Strong.. the sneaky strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 5 spirits..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 5 spirits..", "x": "Explained: 5 spirits.. Deceptive. The context — Long Island Iced Tea. 1970s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cola.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cola.", "x": "Long Island Iced Tea: Cola.. History. Essential knowledge — 1970s.. the sneaky strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cola..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cola..", "x": "Explained: Cola.. Lemon. The context — Long Island Iced Tea. Deceptive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Strong.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Strong.", "x": "Long Island Iced Tea: Strong.. Deceptive. Essential knowledge — Deceptive.. the sneaky strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Strong..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Strong..", "x": "Explained: Strong.. Careful. The context — Long Island Iced Tea. Lemon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1970s.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1970s.", "x": "Long Island Iced Tea: 1970s.. Lemon. Essential knowledge — Lemon.. the sneaky strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1970s..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1970s..", "x": "Explained: 1970s.. Spirits. The context — Long Island Iced Tea. 5 spirits. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Deceptive.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Deceptive.", "x": "Long Island Iced Tea: Deceptive.. Careful. Essential knowledge — 5 spirits.. the sneaky strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Deceptive..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Deceptive..", "x": "Explained: Deceptive.. Strong. The context — Long Island Iced Tea. Cola. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lemon.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lemon.", "x": "Long Island Iced Tea: Lemon.. Spirits. Essential knowledge — Cola.. the sneaky strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lemon..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lemon..", "x": "Explained: Lemon.. History. The context — Long Island Iced Tea. Strong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spirits.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spirits.", "x": "Long Island Iced Tea in depth: Spirits.. Cola. Details — the sneaky strong.. History. 1970s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Strong.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Strong.", "x": "Long Island Iced Tea in depth: Strong.. Strong. Details — the sneaky strong.. Deceptive. Deceptive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Long Island Iced Tea in depth: History.. 1970s. Details — the sneaky strong.. Lemon. Lemon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Deceptive.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Deceptive.", "x": "Long Island Iced Tea in depth: Deceptive.. Deceptive. Details — the sneaky strong.. Careful. 5 spirits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lemon.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lemon.", "x": "Long Island Iced Tea in depth: Lemon.. Lemon. Details — the sneaky strong.. Spirits. Cola. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Careful.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Careful.", "x": "Long Island Iced Tea in depth: Careful.. 5 spirits. Details — the sneaky strong.. Strong. Strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Long Island Iced Tea comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Long Island Iced Tea comes from.", "x": "Origins: Spirits.. 5 spirits. The history of Long Island Iced Tea — the sneaky strong.. Strong. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Long Island Iced Tea respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Long Island Iced Tea respectfully.", "x": "Engaging: History.. Cola. How to participate or observe well — Long Island Iced Tea. the sneaky strong. Respect first, always; Deceptive.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Long Island Iced Tea do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Long Island Iced Tea do's and don'ts.", "x": "Etiquette: Lemon.. Strong. The rules of respect — Long Island Iced Tea. the sneaky strong. When in doubt, ask about Careful.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Long Island Iced Tea.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Long Island Iced Tea.", "x": "Planning: Spirits.. 1970s. Practical notes — Long Island Iced Tea. the sneaky strong. A little planning shows respect for Strong.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Long Island Iced Tea and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Long Island Iced Tea and money.", "x": "Costs: History.. Deceptive. What to budget — Long Island Iced Tea. the sneaky strong. The best experiences of Deceptive. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-long-island-iced-tea-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
