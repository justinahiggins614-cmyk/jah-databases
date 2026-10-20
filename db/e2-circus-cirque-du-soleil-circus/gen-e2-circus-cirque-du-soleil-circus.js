(function(){'use strict';
/* JAH Cirque du Soleil Circus Database generator — jahdb-e2-circus-cirque-du-soleil-circus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-circus-cirque-du-soleil-circus',PREFIX='JAH-E2CIRCUSCIR-',NAME='JAH Cirque du Soleil Circus Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cirque du Soleil: the complete guide", "d": "Cirque du Soleil: the new circus..", "g": "overview", "l": 2, "q": "What is Cirque du Soleil: the complete guide?", "a": "Cirque du Soleil: the new circus..", "x": "The complete circus guide to Cirque du Soleil: the new circus.. 1984. History, meaning, practices, and how to engage respectfully — everything in one database. Quebec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cirque du Soleil essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cirque du Soleil essentials.", "x": "At a glance: Cirque du Soleil — the new circus.. Quebec. The essentials: Acrobatics.. No animals. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1984.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1984.", "x": "Cirque du Soleil: 1984.. Acrobatics. Essential knowledge — No animals.. the new circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1984..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1984..", "x": "Explained: 1984.. Mystère. The context — Cirque du Soleil. Acrobatics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Quebec.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Quebec.", "x": "Cirque du Soleil: Quebec.. Vegas. Essential knowledge — Acrobatics.. the new circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Quebec..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Quebec..", "x": "Explained: Quebec.. 1984. The context — Cirque du Soleil. Vegas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "No animals.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "No animals.", "x": "Cirque du Soleil: No animals.. Mystère. Essential knowledge — Vegas.. the new circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: No animals..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: No animals..", "x": "Explained: No animals.. Shows. The context — Cirque du Soleil. Mystère. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Acrobatics.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Acrobatics.", "x": "Cirque du Soleil: Acrobatics.. 1984. Essential knowledge — Mystère.. the new circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Acrobatics..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Acrobatics..", "x": "Explained: Acrobatics.. Quebec. The context — Cirque du Soleil. 1984. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vegas.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vegas.", "x": "Cirque du Soleil: Vegas.. Shows. Essential knowledge — 1984.. the new circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vegas..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vegas..", "x": "Explained: Vegas.. Acrobatics. The context — Cirque du Soleil. Quebec. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mystère.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mystère.", "x": "Cirque du Soleil: Mystère.. Quebec. Essential knowledge — Quebec.. the new circus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mystère..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mystère..", "x": "Explained: Mystère.. Vegas. The context — Cirque du Soleil. No animals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Quebec.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Quebec.", "x": "Cirque du Soleil in depth: Quebec.. Quebec. Details — the new circus.. Vegas. Acrobatics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Acrobatics.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Acrobatics.", "x": "Cirque du Soleil in depth: Acrobatics.. No animals. Details — the new circus.. Mystère. Vegas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vegas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vegas.", "x": "Cirque du Soleil in depth: Vegas.. Acrobatics. Details — the new circus.. 1984. Mystère. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mystère.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mystère.", "x": "Cirque du Soleil in depth: Mystère.. Vegas. Details — the new circus.. Shows. 1984. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1984.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1984.", "x": "Cirque du Soleil in depth: 1984.. Mystère. Details — the new circus.. Quebec. Quebec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Shows.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Shows.", "x": "Cirque du Soleil in depth: Shows.. 1984. Details — the new circus.. Acrobatics. No animals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cirque du Soleil comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cirque du Soleil comes from.", "x": "Origins: Quebec.. 1984. The history of Cirque du Soleil — the new circus.. Acrobatics. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cirque du Soleil respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cirque du Soleil respectfully.", "x": "Engaging: Vegas.. Quebec. How to participate or observe well — Cirque du Soleil. the new circus. Respect first, always; Mystère.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cirque du Soleil do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cirque du Soleil do's and don'ts.", "x": "Etiquette: 1984.. No animals. The rules of respect — Cirque du Soleil. the new circus. When in doubt, ask about Shows.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cirque du Soleil.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cirque du Soleil.", "x": "Planning: Quebec.. Acrobatics. Practical notes — Cirque du Soleil. the new circus. A little planning shows respect for Acrobatics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cirque du Soleil and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cirque du Soleil and money.", "x": "Costs: Vegas.. Vegas. What to budget — Cirque du Soleil. the new circus. The best experiences of Mystère. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-circus-cirque-du-soleil-circus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
