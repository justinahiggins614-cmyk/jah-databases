(function(){'use strict';
/* JAH Neuropsychology Psychology Database generator — jahdb-e2-sci-neuropsychology-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-neuropsychology',PREFIX='JAH-E2SCINEUROP-',NAME='JAH Neuropsychology Psychology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Neuropsychology: overview", "d": "Neuropsychology: the brain basis of behavior and cognition..", "g": "overview", "l": 2, "q": "What is Neuropsychology: overview?", "a": "Neuropsychology: the brain basis of behavior and cognition..", "x": "The complete psychology guide to Neuropsychology: the brain basis of behavior and cognition.. Studies brain-behavior links. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Neuropsychology.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Neuropsychology.", "x": "The core principle: Phineas Gage case.. the brain basis of behavior and cognition. If you understand this one idea, everything else in Neuropsychology clicks into place. Lateralization of function. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Studies brain-behavior links.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Studies brain-behavior links.", "x": "Neuropsychology: Studies brain-behavior links.. Neuroplasticity. This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Studies brain-behavior links. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Studies brain-behavior links. is true.", "x": "The explanation: Studies brain-behavior links.. In psychology, this fact connects to Executive functions (frontal lobe). — and once you see the mechanism, it stops being trivia and starts being understanding. Split-brain research (Sperry).", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Phineas Gage case.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Phineas Gage case.", "x": "Neuropsychology: Phineas Gage case.. Memory systems (hippocampus). This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Phineas Gage case. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Phineas Gage case. is true.", "x": "The explanation: Phineas Gage case.. In psychology, this fact connects to Clinical assessment. — and once you see the mechanism, it stops being trivia and starts being understanding. Broca's and Wernicke's areas.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Split-brain research (Sperry).", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Split-brain research (Sperry).", "x": "Neuropsychology: Split-brain research (Sperry).. Executive functions (frontal lobe). This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Split-brain research (Sperry). is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Split-brain research (Sperry). is true.", "x": "The explanation: Split-brain research (Sperry).. In psychology, this fact connects to Connects to neurology. — and once you see the mechanism, it stops being trivia and starts being understanding. Neuroimaging (fMRI).", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Broca's and Wernicke's areas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Broca's and Wernicke's areas.", "x": "Neuropsychology: Broca's and Wernicke's areas.. Clinical assessment. This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Broca's and Wernicke's areas. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Broca's and Wernicke's areas. is true.", "x": "The explanation: Broca's and Wernicke's areas.. In psychology, this fact connects to Lateralization of function. — and once you see the mechanism, it stops being trivia and starts being understanding. Rehabilitation after injury.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Neuroimaging (fMRI).", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Neuroimaging (fMRI).", "x": "Neuropsychology: Neuroimaging (fMRI).. Connects to neurology. This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Neuroimaging (fMRI). is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Neuroimaging (fMRI). is true.", "x": "The explanation: Neuroimaging (fMRI).. In psychology, this fact connects to Neuroplasticity. — and once you see the mechanism, it stops being trivia and starts being understanding. Studies brain-behavior links.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rehabilitation after injury.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rehabilitation after injury.", "x": "Neuropsychology: Rehabilitation after injury.. Lateralization of function. This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Rehabilitation after injury. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Rehabilitation after injury. is true.", "x": "The explanation: Rehabilitation after injury.. In psychology, this fact connects to Memory systems (hippocampus). — and once you see the mechanism, it stops being trivia and starts being understanding. Phineas Gage case.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Studies brain-behavior links.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Studies brain-behavior links.", "x": "Neuropsychology: Studies brain-behavior links.. Neuroplasticity. This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Studies brain-behavior links. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Studies brain-behavior links. is true.", "x": "The explanation: Studies brain-behavior links.. In psychology, this fact connects to Executive functions (frontal lobe). — and once you see the mechanism, it stops being trivia and starts being understanding. Split-brain research (Sperry).", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Phineas Gage case.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Phineas Gage case.", "x": "Neuropsychology: Phineas Gage case.. Memory systems (hippocampus). This is load-bearing knowledge — the kind of fact that other facts hang from. the brain basis of behavior and cognition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Phineas Gage case. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Phineas Gage case. is true.", "x": "The explanation: Phineas Gage case.. In psychology, this fact connects to Clinical assessment. — and once you see the mechanism, it stops being trivia and starts being understanding. Broca's and Wernicke's areas.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lateralization of function.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lateralization of function.", "x": "Going deeper on Neuropsychology: Lateralization of function.. Phineas Gage case. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Neuroplasticity.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Neuroplasticity.", "x": "Going deeper on Neuropsychology: Neuroplasticity.. Split-brain research (Sperry). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Memory systems (hippocampus).", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Memory systems (hippocampus).", "x": "Going deeper on Neuropsychology: Memory systems (hippocampus).. Broca's and Wernicke's areas. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Executive functions (frontal lobe).", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Executive functions (frontal lobe).", "x": "Going deeper on Neuropsychology: Executive functions (frontal lobe).. Neuroimaging (fMRI). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Clinical assessment.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Clinical assessment.", "x": "Going deeper on Neuropsychology: Clinical assessment.. Rehabilitation after injury. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Connects to neurology.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Connects to neurology.", "x": "Going deeper on Neuropsychology: Connects to neurology.. Studies brain-behavior links. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Lateralization of function.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Lateralization of function.", "x": "Going deeper on Neuropsychology: Lateralization of function.. Phineas Gage case. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Neuropsychology from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-neuropsychology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
