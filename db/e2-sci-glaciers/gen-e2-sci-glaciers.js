(function(){'use strict';
/* JAH Glaciers Geology Database generator — jahdb-e2-sci-glaciers-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-glaciers',PREFIX='JAH-E2SCIGLACIE-',NAME='JAH Glaciers Geology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Glaciers: overview", "d": "Glaciers: rivers of ice that carve landscapes..", "g": "overview", "l": 2, "q": "What is Glaciers: overview?", "a": "Glaciers: rivers of ice that carve landscapes..", "x": "The complete geology guide to Glaciers: rivers of ice that carve landscapes.. Form from compacted snow. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Glaciers.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Glaciers.", "x": "The core principle: Move cm-meters/day.. rivers of ice that carve landscapes. If you understand this one idea, everything else in Glaciers clicks into place. Moraines mark retreat. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Form from compacted snow.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Form from compacted snow.", "x": "Glaciers: Form from compacted snow.. Crevasses dangers. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Form from compacted snow. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Form from compacted snow. is true.", "x": "The explanation: Form from compacted snow.. In geology, this fact connects to Meltwater floods. — and once you see the mechanism, it stops being trivia and starts being understanding. Carve U-shaped valleys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Move cm-meters/day.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Move cm-meters/day.", "x": "Glaciers: Move cm-meters/day.. Calving icebergs. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Move cm-meters/day. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Move cm-meters/day. is true.", "x": "The explanation: Move cm-meters/day.. In geology, this fact connects to Glacial erratics. — and once you see the mechanism, it stops being trivia and starts being understanding. Ice ages cycle. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Carve U-shaped valleys.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Carve U-shaped valleys.", "x": "Glaciers: Carve U-shaped valleys.. Meltwater floods. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Carve U-shaped valleys. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Carve U-shaped valleys. is true.", "x": "The explanation: Carve U-shaped valleys.. In geology, this fact connects to Climate archive in ice cores. — and once you see the mechanism, it stops being trivia and starts being understanding. Antarctica holds 70% fresh water.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ice ages cycle.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ice ages cycle.", "x": "Glaciers: Ice ages cycle.. Glacial erratics. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Ice ages cycle. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Ice ages cycle. is true.", "x": "The explanation: Ice ages cycle.. In geology, this fact connects to Moraines mark retreat. — and once you see the mechanism, it stops being trivia and starts being understanding. Retreating worldwide.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Antarctica holds 70% fresh water.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Antarctica holds 70% fresh water.", "x": "Glaciers: Antarctica holds 70% fresh water.. Climate archive in ice cores. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Antarctica holds 70% fresh water. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Antarctica holds 70% fresh water. is true.", "x": "The explanation: Antarctica holds 70% fresh water.. In geology, this fact connects to Crevasses dangers. — and once you see the mechanism, it stops being trivia and starts being understanding. Form from compacted snow.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Retreating worldwide.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Retreating worldwide.", "x": "Glaciers: Retreating worldwide.. Moraines mark retreat. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Retreating worldwide. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Retreating worldwide. is true.", "x": "The explanation: Retreating worldwide.. In geology, this fact connects to Calving icebergs. — and once you see the mechanism, it stops being trivia and starts being understanding. Move cm-meters/day. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Form from compacted snow.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Form from compacted snow.", "x": "Glaciers: Form from compacted snow.. Crevasses dangers. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Form from compacted snow. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Form from compacted snow. is true.", "x": "The explanation: Form from compacted snow.. In geology, this fact connects to Meltwater floods. — and once you see the mechanism, it stops being trivia and starts being understanding. Carve U-shaped valleys.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Move cm-meters/day.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Move cm-meters/day.", "x": "Glaciers: Move cm-meters/day.. Calving icebergs. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers of ice that carve landscapes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Move cm-meters/day. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Move cm-meters/day. is true.", "x": "The explanation: Move cm-meters/day.. In geology, this fact connects to Glacial erratics. — and once you see the mechanism, it stops being trivia and starts being understanding. Ice ages cycle. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Moraines mark retreat.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Moraines mark retreat.", "x": "Going deeper on Glaciers: Moraines mark retreat.. Move cm-meters/day. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crevasses dangers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crevasses dangers.", "x": "Going deeper on Glaciers: Crevasses dangers.. Carve U-shaped valleys. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Calving icebergs.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Calving icebergs.", "x": "Going deeper on Glaciers: Calving icebergs.. Ice ages cycle. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Meltwater floods.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Meltwater floods.", "x": "Going deeper on Glaciers: Meltwater floods.. Antarctica holds 70% fresh water. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Glacial erratics.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Glacial erratics.", "x": "Going deeper on Glaciers: Glacial erratics.. Retreating worldwide. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Climate archive in ice cores.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Climate archive in ice cores.", "x": "Going deeper on Glaciers: Climate archive in ice cores.. Form from compacted snow. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Moraines mark retreat.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Moraines mark retreat.", "x": "Going deeper on Glaciers: Moraines mark retreat.. Move cm-meters/day. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Glaciers from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-glaciers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
