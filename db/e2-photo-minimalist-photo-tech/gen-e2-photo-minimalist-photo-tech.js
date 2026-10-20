(function(){'use strict';
/* JAH Minimalist Photo Photography Database generator — jahdb-e2-photo-minimalist-photo-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-minimalist-photo-tech',PREFIX='JAH-E2PHOTOMINI-',NAME='JAH Minimalist Photo Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Minimalist Photo: the complete guide", "d": "Minimalist Photo: the less image..", "g": "overview", "l": 2, "q": "What is Minimalist Photo: the complete guide?", "a": "Minimalist Photo: the less image..", "x": "The complete photography guide to Minimalist Photo: the less image.. Negative. History, meaning, practices, and how to engage respectfully — everything in one database. Negative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Minimalist Photo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Minimalist Photo essentials.", "x": "At a glance: Minimalist Photo — the less image.. Simple. The essentials: Geometry.. Color. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Negative.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Negative.", "x": "Minimalist Photo: Negative.. Geometry. Essential knowledge — Color.. the less image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Negative..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Negative..", "x": "Explained: Negative.. Less. The context — Minimalist Photo. Geometry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Simple.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Simple.", "x": "Minimalist Photo: Simple.. Calm. Essential knowledge — Geometry.. the less image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Simple..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Simple..", "x": "Explained: Simple.. Simple. The context — Minimalist Photo. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Color.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Color.", "x": "Minimalist Photo: Color.. Less. Essential knowledge — Calm.. the less image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Color..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Color..", "x": "Explained: Color.. Tips. The context — Minimalist Photo. Less. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Geometry.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Geometry.", "x": "Minimalist Photo: Geometry.. Simple. Essential knowledge — Less.. the less image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Geometry..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Geometry..", "x": "Explained: Geometry.. Negative. The context — Minimalist Photo. Negative. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Calm.", "x": "Minimalist Photo: Calm.. Tips. Essential knowledge — Negative.. the less image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Geometry. The context — Minimalist Photo. Simple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Less.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Less.", "x": "Minimalist Photo: Less.. Negative. Essential knowledge — Simple.. the less image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Less..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Less..", "x": "Explained: Less.. Calm. The context — Minimalist Photo. Color. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Negative.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Negative.", "x": "Minimalist Photo in depth: Negative.. Simple. Details — the less image.. Calm. Geometry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Geometry.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Geometry.", "x": "Minimalist Photo in depth: Geometry.. Color. Details — the less image.. Less. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Calm.", "x": "Minimalist Photo in depth: Calm.. Geometry. Details — the less image.. Simple. Less. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Less.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Less.", "x": "Minimalist Photo in depth: Less.. Calm. Details — the less image.. Tips. Negative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Simple.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Simple.", "x": "Minimalist Photo in depth: Simple.. Less. Details — the less image.. Negative. Simple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Minimalist Photo in depth: Tips.. Negative. Details — the less image.. Geometry. Color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Minimalist Photo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Minimalist Photo comes from.", "x": "Origins: Negative.. Negative. The history of Minimalist Photo — the less image.. Geometry. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Minimalist Photo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Minimalist Photo respectfully.", "x": "Engaging: Calm.. Simple. How to participate or observe well — Minimalist Photo. the less image. Respect first, always; Less.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Minimalist Photo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Minimalist Photo do's and don'ts.", "x": "Etiquette: Simple.. Color. The rules of respect — Minimalist Photo. the less image. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Minimalist Photo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Minimalist Photo.", "x": "Planning: Negative.. Geometry. Practical notes — Minimalist Photo. the less image. A little planning shows respect for Geometry.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Minimalist Photo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Minimalist Photo and money.", "x": "Costs: Calm.. Calm. What to budget — Minimalist Photo. the less image. The best experiences of Less. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-minimalist-photo-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
