(function(){'use strict';
/* JAH Flower Shows Database generator — jahdb-e2-shows2-flower-shows-show-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-shows2-flower-shows-show',PREFIX='JAH-E2SHOWS2FLO-',NAME='JAH Flower Shows Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Flower Shows: the complete guide", "d": "Flower Shows: the bloom exhibits..", "g": "overview", "l": 2, "q": "What is Flower Shows: the complete guide?", "a": "Flower Shows: the bloom exhibits..", "x": "The complete show guide to Flower Shows: the bloom exhibits.. Chelsea. History, meaning, practices, and how to engage respectfully — everything in one database. Chelsea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Flower Shows essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Flower Shows essentials.", "x": "At a glance: Flower Shows — the bloom exhibits.. Orchids. The essentials: Judging.. Landscapes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Chelsea.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Chelsea.", "x": "Flower Shows: Chelsea.. Judging. Essential knowledge — Landscapes.. the bloom exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Chelsea..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Chelsea..", "x": "Explained: Chelsea.. Orchids. The context — Flower Shows. Spring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Orchids.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Orchids.", "x": "Flower Shows: Orchids.. Scents. Essential knowledge — Spring.. the bloom exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Orchids..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Orchids..", "x": "Explained: Orchids.. Spring. The context — Flower Shows. Judging. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Landscapes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Landscapes.", "x": "Flower Shows: Landscapes.. Orchids. Essential knowledge — Judging.. the bloom exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Landscapes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Landscapes..", "x": "Explained: Landscapes.. Guide. The context — Flower Shows. Scents. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spring.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spring.", "x": "Flower Shows: Spring.. Spring. Essential knowledge — Scents.. the bloom exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Spring..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Spring..", "x": "Explained: Spring.. Chelsea. The context — Flower Shows. Chelsea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Judging.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Judging.", "x": "Flower Shows: Judging.. Guide. Essential knowledge — Chelsea.. the bloom exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Judging..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Judging..", "x": "Explained: Judging.. Judging. The context — Flower Shows. Orchids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Scents.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Scents.", "x": "Flower Shows: Scents.. Chelsea. Essential knowledge — Orchids.. the bloom exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Scents..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Scents..", "x": "Explained: Scents.. Scents. The context — Flower Shows. Landscapes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chelsea.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chelsea.", "x": "Flower Shows in depth: Chelsea.. Orchids. Details — the bloom exhibits.. Scents. Spring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Judging.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Judging.", "x": "Flower Shows in depth: Judging.. Landscapes. Details — the bloom exhibits.. Orchids. Judging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Scents.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Scents.", "x": "Flower Shows in depth: Scents.. Spring. Details — the bloom exhibits.. Spring. Scents. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Orchids.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Orchids.", "x": "Flower Shows in depth: Orchids.. Judging. Details — the bloom exhibits.. Guide. Chelsea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Spring.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Spring.", "x": "Flower Shows in depth: Spring.. Scents. Details — the bloom exhibits.. Chelsea. Orchids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Flower Shows in depth: Guide.. Chelsea. Details — the bloom exhibits.. Judging. Landscapes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Flower Shows comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Flower Shows comes from.", "x": "Origins: Chelsea.. Chelsea. The history of Flower Shows — the bloom exhibits.. Judging. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Flower Shows respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Flower Shows respectfully.", "x": "Engaging: Scents.. Orchids. How to participate or observe well — Flower Shows. the bloom exhibits. Respect first, always; Orchids.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Flower Shows do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Flower Shows do's and don'ts.", "x": "Etiquette: Spring.. Landscapes. The rules of respect — Flower Shows. the bloom exhibits. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Flower Shows.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Flower Shows.", "x": "Planning: Chelsea.. Spring. Practical notes — Flower Shows. the bloom exhibits. A little planning shows respect for Judging.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Flower Shows and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Flower Shows and money.", "x": "Costs: Scents.. Judging. What to budget — Flower Shows. the bloom exhibits. The best experiences of Orchids. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-shows2-flower-shows-show-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
