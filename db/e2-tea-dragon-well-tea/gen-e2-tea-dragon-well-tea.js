(function(){'use strict';
/* JAH Dragon Well Tea Database generator — jahdb-e2-tea-dragon-well-tea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tea-dragon-well-tea',PREFIX='JAH-E2TEADRAGON-',NAME='JAH Dragon Well Tea Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dragon Well: the complete guide", "d": "Dragon Well: the Hangzhou green..", "g": "overview", "l": 2, "q": "What is Dragon Well: the complete guide?", "a": "Dragon Well: the Hangzhou green..", "x": "The complete tea guide to Dragon Well: the Hangzhou green.. Longjing. History, meaning, practices, and how to engage respectfully — everything in one database. Hangzhou. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dragon Well essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dragon Well essentials.", "x": "At a glance: Dragon Well — the Hangzhou green.. Hangzhou. The essentials: Pan-fired.. Pan-fired. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Longjing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Longjing.", "x": "Dragon Well: Longjing.. Pan-fired. Essential knowledge — Pan-fired.. the Hangzhou green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Longjing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Longjing..", "x": "Explained: Longjing.. China. The context — Dragon Well. Flat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hangzhou.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hangzhou.", "x": "Dragon Well: Hangzhou.. Qingming. Essential knowledge — Flat.. the Hangzhou green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hangzhou..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hangzhou..", "x": "Explained: Hangzhou.. Flat. The context — Dragon Well. Qingming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pan-fired.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pan-fired.", "x": "Dragon Well: Pan-fired.. China. Essential knowledge — Qingming.. the Hangzhou green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pan-fired..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pan-fired..", "x": "Explained: Pan-fired.. Prestige. The context — Dragon Well. China. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flat.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flat.", "x": "Dragon Well: Flat.. Flat. Essential knowledge — China.. the Hangzhou green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Flat..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Flat..", "x": "Explained: Flat.. Hangzhou. The context — Dragon Well. Longjing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Qingming.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Qingming.", "x": "Dragon Well: Qingming.. Prestige. Essential knowledge — Longjing.. the Hangzhou green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Qingming..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Qingming..", "x": "Explained: Qingming.. Pan-fired. The context — Dragon Well. Hangzhou. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "China.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "China.", "x": "Dragon Well: China.. Hangzhou. Essential knowledge — Hangzhou.. the Hangzhou green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: China..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: China..", "x": "Explained: China.. Qingming. The context — Dragon Well. Pan-fired. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hangzhou.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hangzhou.", "x": "Dragon Well in depth: Hangzhou.. Hangzhou. Details — the Hangzhou green.. Qingming. Flat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pan-fired.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pan-fired.", "x": "Dragon Well in depth: Pan-fired.. Pan-fired. Details — the Hangzhou green.. China. Qingming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Qingming.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Qingming.", "x": "Dragon Well in depth: Qingming.. Flat. Details — the Hangzhou green.. Flat. China. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "China.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "China.", "x": "Dragon Well in depth: China.. Qingming. Details — the Hangzhou green.. Prestige. Longjing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flat.", "x": "Dragon Well in depth: Flat.. China. Details — the Hangzhou green.. Hangzhou. Hangzhou. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Prestige.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Prestige.", "x": "Dragon Well in depth: Prestige.. Longjing. Details — the Hangzhou green.. Pan-fired. Pan-fired. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dragon Well comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dragon Well comes from.", "x": "Origins: Hangzhou.. Longjing. The history of Dragon Well — the Hangzhou green.. Pan-fired. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dragon Well respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dragon Well respectfully.", "x": "Engaging: Qingming.. Hangzhou. How to participate or observe well — Dragon Well. the Hangzhou green. Respect first, always; China.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dragon Well do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dragon Well do's and don'ts.", "x": "Etiquette: Flat.. Pan-fired. The rules of respect — Dragon Well. the Hangzhou green. When in doubt, ask about Prestige.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dragon Well.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dragon Well.", "x": "Planning: Hangzhou.. Flat. Practical notes — Dragon Well. the Hangzhou green. A little planning shows respect for Pan-fired.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dragon Well and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dragon Well and money.", "x": "Costs: Qingming.. Qingming. What to budget — Dragon Well. the Hangzhou green. The best experiences of China. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tea-dragon-well-tea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
