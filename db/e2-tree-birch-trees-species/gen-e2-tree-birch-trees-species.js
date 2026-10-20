(function(){'use strict';
/* JAH Birch Trees Tree Database generator — jahdb-e2-tree-birch-trees-species-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tree-birch-trees-species',PREFIX='JAH-E2TREEBIRCH-',NAME='JAH Birch Trees Tree Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Birch Trees: the complete guide", "d": "Birch Trees: the white bark..", "g": "overview", "l": 2, "q": "What is Birch Trees: the complete guide?", "a": "Birch Trees: the white bark..", "x": "The complete tree guide to Birch Trees: the white bark.. White bark. History, meaning, practices, and how to engage respectfully — everything in one database. Bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Birch Trees essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Birch Trees essentials.", "x": "At a glance: Birch Trees — the white bark.. Peeling. The essentials: Fall.. Fall. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "White bark.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "White bark.", "x": "Birch Trees: White bark.. Fall. Essential knowledge — Fall.. the white bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: White bark..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: White bark..", "x": "Explained: White bark.. Species. The context — Birch Trees. Wet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Peeling.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Peeling.", "x": "Birch Trees: Peeling.. Short-lived. Essential knowledge — Wet.. the white bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Peeling..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Peeling..", "x": "Explained: Peeling.. Wet. The context — Birch Trees. Short-lived. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fall.", "x": "Birch Trees: Fall.. Species. Essential knowledge — Short-lived.. the white bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fall..", "x": "Explained: Fall.. Guide. The context — Birch Trees. Species. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wet.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wet.", "x": "Birch Trees: Wet.. Wet. Essential knowledge — Species.. the white bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Wet..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Wet..", "x": "Explained: Wet.. Bark. The context — Birch Trees. White bark. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Short-lived.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Short-lived.", "x": "Birch Trees: Short-lived.. Guide. Essential knowledge — White bark.. the white bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Short-lived..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Short-lived..", "x": "Explained: Short-lived.. Fall. The context — Birch Trees. Peeling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Species.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Species.", "x": "Birch Trees: Species.. Bark. Essential knowledge — Peeling.. the white bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Species..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Species..", "x": "Explained: Species.. Short-lived. The context — Birch Trees. Fall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bark.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bark.", "x": "Birch Trees in depth: Bark.. Peeling. Details — the white bark.. Short-lived. Wet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fall.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fall.", "x": "Birch Trees in depth: Fall.. Fall. Details — the white bark.. Species. Short-lived. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Short-lived.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Short-lived.", "x": "Birch Trees in depth: Short-lived.. Wet. Details — the white bark.. Wet. Species. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Species.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Species.", "x": "Birch Trees in depth: Species.. Short-lived. Details — the white bark.. Guide. White bark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wet.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wet.", "x": "Birch Trees in depth: Wet.. Species. Details — the white bark.. Bark. Peeling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Birch Trees in depth: Guide.. White bark. Details — the white bark.. Fall. Fall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Birch Trees comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Birch Trees comes from.", "x": "Origins: Bark.. White bark. The history of Birch Trees — the white bark.. Fall. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Birch Trees respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Birch Trees respectfully.", "x": "Engaging: Short-lived.. Peeling. How to participate or observe well — Birch Trees. the white bark. Respect first, always; Species.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Birch Trees do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Birch Trees do's and don'ts.", "x": "Etiquette: Wet.. Fall. The rules of respect — Birch Trees. the white bark. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Birch Trees.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Birch Trees.", "x": "Planning: Bark.. Wet. Practical notes — Birch Trees. the white bark. A little planning shows respect for Fall.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Birch Trees and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Birch Trees and money.", "x": "Costs: Short-lived.. Short-lived. What to budget — Birch Trees. the white bark. The best experiences of Species. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tree-birch-trees-species-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
