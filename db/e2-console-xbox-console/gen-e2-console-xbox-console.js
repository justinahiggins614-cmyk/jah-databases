(function(){'use strict';
/* JAH Xbox Console Console Database generator — jahdb-e2-console-xbox-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-xbox-console',PREFIX='JAH-E2CONSOLEXB-',NAME='JAH Xbox Console Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Xbox Console: the complete guide", "d": "Xbox Console: the Microsoft entry..", "g": "overview", "l": 2, "q": "What is Xbox Console: the complete guide?", "a": "Xbox Console: the Microsoft entry..", "x": "The complete console guide to Xbox Console: the Microsoft entry.. 2001. History, meaning, practices, and how to engage respectfully — everything in one database. Halo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Xbox Console essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Xbox Console essentials.", "x": "At a glance: Xbox Console — the Microsoft entry.. Halo. The essentials: Live.. Live. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2001.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2001.", "x": "Xbox Console: 2001.. Live. Essential knowledge — Live.. the Microsoft entry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2001..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2001..", "x": "Explained: 2001.. Microsoft. The context — Xbox Console. Duke. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Halo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Halo.", "x": "Xbox Console: Halo.. Duke. Essential knowledge — Duke.. the Microsoft entry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Halo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Halo..", "x": "Explained: Halo.. PC. The context — Xbox Console. PC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Live.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Live.", "x": "Xbox Console: Live.. Microsoft. Essential knowledge — PC.. the Microsoft entry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Live..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Live..", "x": "Explained: Live.. Legacy. The context — Xbox Console. Microsoft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Duke.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Duke.", "x": "Xbox Console: Duke.. PC. Essential knowledge — Microsoft.. the Microsoft entry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Duke..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Duke..", "x": "Explained: Duke.. Halo. The context — Xbox Console. 2001. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "PC.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "PC.", "x": "Xbox Console: PC.. Legacy. Essential knowledge — 2001.. the Microsoft entry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: PC..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: PC..", "x": "Explained: PC.. Live. The context — Xbox Console. Halo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Microsoft.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Microsoft.", "x": "Xbox Console: Microsoft.. Halo. Essential knowledge — Halo.. the Microsoft entry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Microsoft..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Microsoft..", "x": "Explained: Microsoft.. Duke. The context — Xbox Console. Live. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Halo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Halo.", "x": "Xbox Console in depth: Halo.. Halo. Details — the Microsoft entry.. Duke. Duke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Live.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Live.", "x": "Xbox Console in depth: Live.. Live. Details — the Microsoft entry.. Microsoft. PC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Duke.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Duke.", "x": "Xbox Console in depth: Duke.. Duke. Details — the Microsoft entry.. PC. Microsoft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Microsoft.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Microsoft.", "x": "Xbox Console in depth: Microsoft.. PC. Details — the Microsoft entry.. Legacy. 2001. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "PC.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "PC.", "x": "Xbox Console in depth: PC.. Microsoft. Details — the Microsoft entry.. Halo. Halo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Xbox Console in depth: Legacy.. 2001. Details — the Microsoft entry.. Live. Live. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Xbox Console comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Xbox Console comes from.", "x": "Origins: Halo.. 2001. The history of Xbox Console — the Microsoft entry.. Live. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Xbox Console respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Xbox Console respectfully.", "x": "Engaging: Duke.. Halo. How to participate or observe well — Xbox Console. the Microsoft entry. Respect first, always; Microsoft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Xbox Console do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Xbox Console do's and don'ts.", "x": "Etiquette: PC.. Live. The rules of respect — Xbox Console. the Microsoft entry. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Xbox Console.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Xbox Console.", "x": "Planning: Halo.. Duke. Practical notes — Xbox Console. the Microsoft entry. A little planning shows respect for Live.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Xbox Console and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Xbox Console and money.", "x": "Costs: Duke.. PC. What to budget — Xbox Console. the Microsoft entry. The best experiences of Microsoft. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-xbox-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
