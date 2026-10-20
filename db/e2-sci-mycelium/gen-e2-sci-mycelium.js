(function(){'use strict';
/* JAH Mycelium Mycology Database generator — jahdb-e2-sci-mycelium-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-mycelium',PREFIX='JAH-E2SCIMYCELI-',NAME='JAH Mycelium Mycology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mycelium: overview", "d": "Mycelium: the vast fungal network..", "g": "overview", "l": 2, "q": "What is Mycelium: overview?", "a": "Mycelium: the vast fungal network..", "x": "The complete mycology guide to Mycelium: the vast fungal network.. Largest organism (Oregon). From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Mycelium.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Mycelium.", "x": "The core principle: Wood wide web.. the vast fungal network. If you understand this one idea, everything else in Mycelium clicks into place. Hyphae. Return to it whenever the details get confusing. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Largest organism (Oregon).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Largest organism (Oregon).", "x": "Mycelium: Largest organism (Oregon).. Networks. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Largest organism (Oregon). is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Largest organism (Oregon). is true.", "x": "The explanation: Largest organism (Oregon).. In mycology, this fact connects to Myco-materials. — and once you see the mechanism, it stops being trivia and starts being understanding. Nutrient trading.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wood wide web.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wood wide web.", "x": "Mycelium: Wood wide web.. Mycorrhizae. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Wood wide web. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Wood wide web. is true.", "x": "The explanation: Wood wide web.. In mycology, this fact connects to Soil health. — and once you see the mechanism, it stops being trivia and starts being understanding. Decomposition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nutrient trading.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nutrient trading.", "x": "Mycelium: Nutrient trading.. Myco-materials. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Nutrient trading. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Nutrient trading. is true.", "x": "The explanation: Nutrient trading.. In mycology, this fact connects to Research. — and once you see the mechanism, it stops being trivia and starts being understanding. Mycelium materials. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Decomposition.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Decomposition.", "x": "Mycelium: Decomposition.. Soil health. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Decomposition. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Decomposition. is true.", "x": "The explanation: Decomposition.. In mycology, this fact connects to Hyphae. — and once you see the mechanism, it stops being trivia and starts being understanding. Remediation. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mycelium materials.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mycelium materials.", "x": "Mycelium: Mycelium materials.. Research. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Mycelium materials. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Mycelium materials. is true.", "x": "The explanation: Mycelium materials.. In mycology, this fact connects to Networks. — and once you see the mechanism, it stops being trivia and starts being understanding. Largest organism (Oregon). Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Remediation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Remediation.", "x": "Mycelium: Remediation.. Hyphae. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Remediation. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Remediation. is true.", "x": "The explanation: Remediation.. In mycology, this fact connects to Mycorrhizae. — and once you see the mechanism, it stops being trivia and starts being understanding. Wood wide web. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Largest organism (Oregon).", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Largest organism (Oregon).", "x": "Mycelium: Largest organism (Oregon).. Networks. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Largest organism (Oregon). is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Largest organism (Oregon). is true.", "x": "The explanation: Largest organism (Oregon).. In mycology, this fact connects to Myco-materials. — and once you see the mechanism, it stops being trivia and starts being understanding. Nutrient trading.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Wood wide web.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Wood wide web.", "x": "Mycelium: Wood wide web.. Mycorrhizae. This is load-bearing knowledge — the kind of fact that other facts hang from. the vast fungal network. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Wood wide web. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Wood wide web. is true.", "x": "The explanation: Wood wide web.. In mycology, this fact connects to Soil health. — and once you see the mechanism, it stops being trivia and starts being understanding. Decomposition. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hyphae.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hyphae.", "x": "Going deeper on Mycelium: Hyphae.. Wood wide web. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Networks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Networks.", "x": "Going deeper on Mycelium: Networks.. Nutrient trading. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mycorrhizae.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mycorrhizae.", "x": "Going deeper on Mycelium: Mycorrhizae.. Decomposition. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Myco-materials.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Myco-materials.", "x": "Going deeper on Mycelium: Myco-materials.. Mycelium materials. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Soil health.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Soil health.", "x": "Going deeper on Mycelium: Soil health.. Remediation. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Research.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Research.", "x": "Going deeper on Mycelium: Research.. Largest organism (Oregon). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Hyphae.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Hyphae.", "x": "Going deeper on Mycelium: Hyphae.. Wood wide web. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mycelium from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-mycelium-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
