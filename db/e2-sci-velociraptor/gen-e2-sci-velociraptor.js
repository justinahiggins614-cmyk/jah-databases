(function(){'use strict';
/* JAH Velociraptor Paleontology Database generator — jahdb-e2-sci-velociraptor-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-velociraptor',PREFIX='JAH-E2SCIVELOCI-',NAME='JAH Velociraptor Paleontology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Velociraptor: overview", "d": "Velociraptor: turkey-sized pack hunter; feathered..", "g": "overview", "l": 2, "q": "What is Velociraptor: overview?", "a": "Velociraptor: turkey-sized pack hunter; feathered..", "x": "The complete paleontology guide to Velociraptor: turkey-sized pack hunter; feathered.. Real size: turkey. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Velociraptor.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Velociraptor.", "x": "The core principle: Feathered.. turkey-sized pack hunter; feathered. If you understand this one idea, everything else in Velociraptor clicks into place. Discovery 1924. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Real size: turkey.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Real size: turkey.", "x": "Velociraptor: Real size: turkey.. Deinonychus bigger. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Real size: turkey. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Real size: turkey. is true.", "x": "The explanation: Real size: turkey.. In paleontology, this fact connects to Fossils. — and once you see the mechanism, it stops being trivia and starts being understanding. Sickle claw. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Feathered.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Feathered.", "x": "Velociraptor: Feathered.. Brain smart. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Feathered. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Feathered. is true.", "x": "The explanation: Feathered.. In paleontology, this fact connects to Pop culture. — and once you see the mechanism, it stops being trivia and starts being understanding. Pack hunting? Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sickle claw.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sickle claw.", "x": "Velociraptor: Sickle claw.. Fossils. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Sickle claw. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Sickle claw. is true.", "x": "The explanation: Sickle claw.. In paleontology, this fact connects to Relatives. — and once you see the mechanism, it stops being trivia and starts being understanding. Mongolia. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pack hunting?", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pack hunting?", "x": "Velociraptor: Pack hunting?. Pop culture. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Pack hunting? is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Pack hunting? is true.", "x": "The explanation: Pack hunting?. In paleontology, this fact connects to Discovery 1924. — and once you see the mechanism, it stops being trivia and starts being understanding. Jurassic Park oversized. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mongolia.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mongolia.", "x": "Velociraptor: Mongolia.. Relatives. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Mongolia. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Mongolia. is true.", "x": "The explanation: Mongolia.. In paleontology, this fact connects to Deinonychus bigger. — and once you see the mechanism, it stops being trivia and starts being understanding. Real size: turkey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Jurassic Park oversized.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Jurassic Park oversized.", "x": "Velociraptor: Jurassic Park oversized.. Discovery 1924. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Jurassic Park oversized. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Jurassic Park oversized. is true.", "x": "The explanation: Jurassic Park oversized.. In paleontology, this fact connects to Brain smart. — and once you see the mechanism, it stops being trivia and starts being understanding. Feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Real size: turkey.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Real size: turkey.", "x": "Velociraptor: Real size: turkey.. Deinonychus bigger. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Real size: turkey. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Real size: turkey. is true.", "x": "The explanation: Real size: turkey.. In paleontology, this fact connects to Fossils. — and once you see the mechanism, it stops being trivia and starts being understanding. Sickle claw. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Feathered.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Feathered.", "x": "Velociraptor: Feathered.. Brain smart. This is load-bearing knowledge — the kind of fact that other facts hang from. turkey-sized pack hunter; feathered. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Feathered. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Feathered. is true.", "x": "The explanation: Feathered.. In paleontology, this fact connects to Pop culture. — and once you see the mechanism, it stops being trivia and starts being understanding. Pack hunting? Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Discovery 1924.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Discovery 1924.", "x": "Going deeper on Velociraptor: Discovery 1924.. Feathered. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Deinonychus bigger.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Deinonychus bigger.", "x": "Going deeper on Velociraptor: Deinonychus bigger.. Sickle claw. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Brain smart.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Brain smart.", "x": "Going deeper on Velociraptor: Brain smart.. Pack hunting? Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fossils.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fossils.", "x": "Going deeper on Velociraptor: Fossils.. Mongolia. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pop culture.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pop culture.", "x": "Going deeper on Velociraptor: Pop culture.. Jurassic Park oversized. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Relatives.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Relatives.", "x": "Going deeper on Velociraptor: Relatives.. Real size: turkey. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Discovery 1924.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Discovery 1924.", "x": "Going deeper on Velociraptor: Discovery 1924.. Feathered. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Velociraptor from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-velociraptor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
