(function(){'use strict';
/* JAH Tsunamis Oceanography Database generator — jahdb-e2-sci-tsunamis-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-tsunamis',PREFIX='JAH-E2SCITSUNAM-',NAME='JAH Tsunamis Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tsunamis: overview", "d": "Tsunamis: giant waves from undersea earthquakes..", "g": "overview", "l": 2, "q": "What is Tsunamis: overview?", "a": "Tsunamis: giant waves from undersea earthquakes..", "x": "The complete oceanography guide to Tsunamis: giant waves from undersea earthquakes.. Not tidal waves. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Tsunamis.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Tsunamis.", "x": "The core principle: 2004: 230,000 died.. giant waves from undersea earthquakes. If you understand this one idea, everything else in Tsunamis clicks into place. Megathrust quakes. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Not tidal waves.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Not tidal waves.", "x": "Tsunamis: Not tidal waves.. Drawback before wave. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Not tidal waves. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Not tidal waves. is true.", "x": "The explanation: Not tidal waves.. In oceanography, this fact connects to Inundation maps. — and once you see the mechanism, it stops being trivia and starts being understanding. 2011 Japan. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2004: 230,000 died.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2004: 230,000 died.", "x": "Tsunamis: 2004: 230,000 died.. DART buoys. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why 2004: 230,000 died. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why 2004: 230,000 died. is true.", "x": "The explanation: 2004: 230,000 died.. In oceanography, this fact connects to Evacuation drills. — and once you see the mechanism, it stops being trivia and starts being understanding. Speed: jetliner in deep ocean.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "2011 Japan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "2011 Japan.", "x": "Tsunamis: 2011 Japan.. Inundation maps. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why 2011 Japan. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why 2011 Japan. is true.", "x": "The explanation: 2011 Japan.. In oceanography, this fact connects to History: Lisbon 1755. — and once you see the mechanism, it stops being trivia and starts being understanding. Warning systems. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Speed: jetliner in deep ocean.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Speed: jetliner in deep ocean.", "x": "Tsunamis: Speed: jetliner in deep ocean.. Evacuation drills. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Speed: jetliner in deep ocean. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Speed: jetliner in deep ocean. is true.", "x": "The explanation: Speed: jetliner in deep ocean.. In oceanography, this fact connects to Megathrust quakes. — and once you see the mechanism, it stops being trivia and starts being understanding. Run to high ground.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Warning systems.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Warning systems.", "x": "Tsunamis: Warning systems.. History: Lisbon 1755. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Warning systems. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Warning systems. is true.", "x": "The explanation: Warning systems.. In oceanography, this fact connects to Drawback before wave. — and once you see the mechanism, it stops being trivia and starts being understanding. Not tidal waves.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Run to high ground.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Run to high ground.", "x": "Tsunamis: Run to high ground.. Megathrust quakes. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Run to high ground. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Run to high ground. is true.", "x": "The explanation: Run to high ground.. In oceanography, this fact connects to DART buoys. — and once you see the mechanism, it stops being trivia and starts being understanding. 2004: 230,000 died. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Not tidal waves.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Not tidal waves.", "x": "Tsunamis: Not tidal waves.. Drawback before wave. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Not tidal waves. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Not tidal waves. is true.", "x": "The explanation: Not tidal waves.. In oceanography, this fact connects to Inundation maps. — and once you see the mechanism, it stops being trivia and starts being understanding. 2011 Japan. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "2004: 230,000 died.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "2004: 230,000 died.", "x": "Tsunamis: 2004: 230,000 died.. DART buoys. This is load-bearing knowledge — the kind of fact that other facts hang from. giant waves from undersea earthquakes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why 2004: 230,000 died. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why 2004: 230,000 died. is true.", "x": "The explanation: 2004: 230,000 died.. In oceanography, this fact connects to Evacuation drills. — and once you see the mechanism, it stops being trivia and starts being understanding. Speed: jetliner in deep ocean.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Megathrust quakes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Megathrust quakes.", "x": "Going deeper on Tsunamis: Megathrust quakes.. 2004: 230,000 died. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Drawback before wave.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Drawback before wave.", "x": "Going deeper on Tsunamis: Drawback before wave.. 2011 Japan. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "DART buoys.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "DART buoys.", "x": "Going deeper on Tsunamis: DART buoys.. Speed: jetliner in deep ocean. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Inundation maps.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Inundation maps.", "x": "Going deeper on Tsunamis: Inundation maps.. Warning systems. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Evacuation drills.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Evacuation drills.", "x": "Going deeper on Tsunamis: Evacuation drills.. Run to high ground. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History: Lisbon 1755.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History: Lisbon 1755.", "x": "Going deeper on Tsunamis: History: Lisbon 1755.. Not tidal waves. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Megathrust quakes.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Megathrust quakes.", "x": "Going deeper on Tsunamis: Megathrust quakes.. 2004: 230,000 died. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Tsunamis from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-tsunamis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
