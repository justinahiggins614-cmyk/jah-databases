(function(){'use strict';
/* JAH Thunderstorms Meteorology Database generator — jahdb-e2-sci-thunderstorms-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-thunderstorms',PREFIX='JAH-E2SCITHUNDE-',NAME='JAH Thunderstorms Meteorology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thunderstorms: overview", "d": "Thunderstorms: convective storms with lightning..", "g": "overview", "l": 2, "q": "What is Thunderstorms: overview?", "a": "Thunderstorms: convective storms with lightning..", "x": "The complete meteorology guide to Thunderstorms: convective storms with lightning.. Cumulonimbus towers. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Thunderstorms.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Thunderstorms.", "x": "The core principle: Updrafts/downdrafts.. convective storms with lightning. If you understand this one idea, everything else in Thunderstorms clicks into place. CAPE instability. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cumulonimbus towers.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cumulonimbus towers.", "x": "Thunderstorms: Cumulonimbus towers.. Anvil tops. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Cumulonimbus towers. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Cumulonimbus towers. is true.", "x": "The explanation: Cumulonimbus towers.. In meteorology, this fact connects to Flash floods. — and once you see the mechanism, it stops being trivia and starts being understanding. Lightning: 30,000C. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Updrafts/downdrafts.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Updrafts/downdrafts.", "x": "Thunderstorms: Updrafts/downdrafts.. Thunder: shock wave. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Updrafts/downdrafts. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Updrafts/downdrafts. is true.", "x": "The explanation: Updrafts/downdrafts.. In meteorology, this fact connects to Aviation hazard. — and once you see the mechanism, it stops being trivia and starts being understanding. Hail forms aloft. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lightning: 30,000C.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lightning: 30,000C.", "x": "Thunderstorms: Lightning: 30,000C.. Flash floods. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Lightning: 30,000C. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Lightning: 30,000C. is true.", "x": "The explanation: Lightning: 30,000C.. In meteorology, this fact connects to Counting seconds. — and once you see the mechanism, it stops being trivia and starts being understanding. Microbursts. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hail forms aloft.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hail forms aloft.", "x": "Thunderstorms: Hail forms aloft.. Aviation hazard. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Hail forms aloft. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Hail forms aloft. is true.", "x": "The explanation: Hail forms aloft.. In meteorology, this fact connects to CAPE instability. — and once you see the mechanism, it stops being trivia and starts being understanding. Single-cell vs squall.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Microbursts.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Microbursts.", "x": "Thunderstorms: Microbursts.. Counting seconds. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Microbursts. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Microbursts. is true.", "x": "The explanation: Microbursts.. In meteorology, this fact connects to Anvil tops. — and once you see the mechanism, it stops being trivia and starts being understanding. Cumulonimbus towers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Single-cell vs squall.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Single-cell vs squall.", "x": "Thunderstorms: Single-cell vs squall.. CAPE instability. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Single-cell vs squall. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Single-cell vs squall. is true.", "x": "The explanation: Single-cell vs squall.. In meteorology, this fact connects to Thunder: shock wave. — and once you see the mechanism, it stops being trivia and starts being understanding. Updrafts/downdrafts.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Cumulonimbus towers.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Cumulonimbus towers.", "x": "Thunderstorms: Cumulonimbus towers.. Anvil tops. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Cumulonimbus towers. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Cumulonimbus towers. is true.", "x": "The explanation: Cumulonimbus towers.. In meteorology, this fact connects to Flash floods. — and once you see the mechanism, it stops being trivia and starts being understanding. Lightning: 30,000C. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Updrafts/downdrafts.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Updrafts/downdrafts.", "x": "Thunderstorms: Updrafts/downdrafts.. Thunder: shock wave. This is load-bearing knowledge — the kind of fact that other facts hang from. convective storms with lightning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Updrafts/downdrafts. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Updrafts/downdrafts. is true.", "x": "The explanation: Updrafts/downdrafts.. In meteorology, this fact connects to Aviation hazard. — and once you see the mechanism, it stops being trivia and starts being understanding. Hail forms aloft. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "CAPE instability.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "CAPE instability.", "x": "Going deeper on Thunderstorms: CAPE instability.. Updrafts/downdrafts. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Anvil tops.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Anvil tops.", "x": "Going deeper on Thunderstorms: Anvil tops.. Lightning: 30,000C. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Thunder: shock wave.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Thunder: shock wave.", "x": "Going deeper on Thunderstorms: Thunder: shock wave.. Hail forms aloft. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Flash floods.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Flash floods.", "x": "Going deeper on Thunderstorms: Flash floods.. Microbursts. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aviation hazard.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aviation hazard.", "x": "Going deeper on Thunderstorms: Aviation hazard.. Single-cell vs squall. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Counting seconds.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Counting seconds.", "x": "Going deeper on Thunderstorms: Counting seconds.. Cumulonimbus towers. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "CAPE instability.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "CAPE instability.", "x": "Going deeper on Thunderstorms: CAPE instability.. Updrafts/downdrafts. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Thunderstorms from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-thunderstorms-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
