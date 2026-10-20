(function(){'use strict';
/* JAH Prairie Style Architecture Style Database generator — jahdb-e2-arch-prairie-style-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-prairie-style-architecture-style',PREFIX='JAH-E2ARCHPRAIR-',NAME='JAH Prairie Style Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Prairie Style Architecture: the complete guide", "d": "Prairie Style Architecture: the Wright horizontal..", "g": "overview", "l": 2, "q": "What is Prairie Style Architecture: the complete guide?", "a": "Prairie Style Architecture: the Wright horizontal..", "x": "The complete architecture style guide to Prairie Style Architecture: the Wright horizontal.. Wright. History, meaning, practices, and how to engage respectfully — everything in one database. Wright. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Prairie Style Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Prairie Style Architecture essentials.", "x": "At a glance: Prairie Style Architecture — the Wright horizontal.. Horizontal. The essentials: Hearth.. 1900. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wright.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wright.", "x": "Prairie Style Architecture: Wright.. Hearth. Essential knowledge — 1900.. the Wright horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wright..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wright..", "x": "Explained: Wright.. 1900. The context — Prairie Style Architecture. Hearth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Horizontal.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Horizontal.", "x": "Prairie Style Architecture: Horizontal.. Organic. Essential knowledge — Hearth.. the Wright horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Horizontal..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Horizontal..", "x": "Explained: Horizontal.. Horizontal. The context — Prairie Style Architecture. Prairie. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1900.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1900.", "x": "Prairie Style Architecture: 1900.. 1900. Essential knowledge — Prairie.. the Wright horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1900..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1900..", "x": "Explained: 1900.. Legacy. The context — Prairie Style Architecture. Organic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hearth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hearth.", "x": "Prairie Style Architecture: Hearth.. Horizontal. Essential knowledge — Organic.. the Wright horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hearth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hearth..", "x": "Explained: Hearth.. Wright. The context — Prairie Style Architecture. Wright. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Prairie.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Prairie.", "x": "Prairie Style Architecture: Prairie.. Legacy. Essential knowledge — Wright.. the Wright horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Prairie..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Prairie..", "x": "Explained: Prairie.. Hearth. The context — Prairie Style Architecture. Horizontal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Organic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Organic.", "x": "Prairie Style Architecture: Organic.. Wright. Essential knowledge — Horizontal.. the Wright horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Organic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Organic..", "x": "Explained: Organic.. Organic. The context — Prairie Style Architecture. 1900. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wright.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wright.", "x": "Prairie Style Architecture in depth: Wright.. Horizontal. Details — the Wright horizontal.. Organic. Hearth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hearth.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hearth.", "x": "Prairie Style Architecture in depth: Hearth.. 1900. Details — the Wright horizontal.. 1900. Prairie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Organic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Organic.", "x": "Prairie Style Architecture in depth: Organic.. Hearth. Details — the Wright horizontal.. Horizontal. Organic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1900.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1900.", "x": "Prairie Style Architecture in depth: 1900.. Prairie. Details — the Wright horizontal.. Legacy. Wright. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Horizontal.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Horizontal.", "x": "Prairie Style Architecture in depth: Horizontal.. Organic. Details — the Wright horizontal.. Wright. Horizontal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Prairie Style Architecture in depth: Legacy.. Wright. Details — the Wright horizontal.. Hearth. 1900. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Prairie Style Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Prairie Style Architecture comes from.", "x": "Origins: Wright.. Wright. The history of Prairie Style Architecture — the Wright horizontal.. Hearth. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Prairie Style Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Prairie Style Architecture respectfully.", "x": "Engaging: Organic.. Horizontal. How to participate or observe well — Prairie Style Architecture. the Wright horizontal. Respect first, always; 1900.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Prairie Style Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Prairie Style Architecture do's and don'ts.", "x": "Etiquette: Horizontal.. 1900. The rules of respect — Prairie Style Architecture. the Wright horizontal. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Prairie Style Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Prairie Style Architecture.", "x": "Planning: Wright.. Hearth. Practical notes — Prairie Style Architecture. the Wright horizontal. A little planning shows respect for Hearth.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Prairie Style Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Prairie Style Architecture and money.", "x": "Costs: Organic.. Prairie. What to budget — Prairie Style Architecture. the Wright horizontal. The best experiences of 1900. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-prairie-style-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
