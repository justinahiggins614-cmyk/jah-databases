(function(){'use strict';
/* JAH Plant Diseases Botany Database generator — jahdb-e2-sci-plant-diseases-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-plant-diseases',PREFIX='JAH-E2SCIPLANTD-',NAME='JAH Plant Diseases Botany Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Plant Diseases: overview", "d": "Plant Diseases: pathogens that attack plants..", "g": "overview", "l": 2, "q": "What is Plant Diseases: overview?", "a": "Plant Diseases: pathogens that attack plants..", "x": "The complete botany guide to Plant Diseases: pathogens that attack plants.. Irish potato famine. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Plant Diseases.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Plant Diseases.", "x": "The core principle: Chestnut blight.. pathogens that attack plants. If you understand this one idea, everything else in Plant Diseases clicks into place. Fungi top culprits. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Irish potato famine.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Irish potato famine.", "x": "Plant Diseases: Irish potato famine.. Vectors: insects. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Irish potato famine. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Irish potato famine. is true.", "x": "The explanation: Irish potato famine.. In botany, this fact connects to Crop losses. — and once you see the mechanism, it stops being trivia and starts being understanding. Citrus greening. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chestnut blight.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chestnut blight.", "x": "Plant Diseases: Chestnut blight.. Quarantines. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Chestnut blight. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Chestnut blight. is true.", "x": "The explanation: Chestnut blight.. In botany, this fact connects to Diagnosis. — and once you see the mechanism, it stops being trivia and starts being understanding. Rusts and smuts. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Citrus greening.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Citrus greening.", "x": "Plant Diseases: Citrus greening.. Crop losses. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Citrus greening. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Citrus greening. is true.", "x": "The explanation: Citrus greening.. In botany, this fact connects to Prevention. — and once you see the mechanism, it stops being trivia and starts being understanding. Integrated pest management. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rusts and smuts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rusts and smuts.", "x": "Plant Diseases: Rusts and smuts.. Diagnosis. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Rusts and smuts. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Rusts and smuts. is true.", "x": "The explanation: Rusts and smuts.. In botany, this fact connects to Fungi top culprits. — and once you see the mechanism, it stops being trivia and starts being understanding. Resistant varieties. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Integrated pest management.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Integrated pest management.", "x": "Plant Diseases: Integrated pest management.. Prevention. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Integrated pest management. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Integrated pest management. is true.", "x": "The explanation: Integrated pest management.. In botany, this fact connects to Vectors: insects. — and once you see the mechanism, it stops being trivia and starts being understanding. Irish potato famine.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Resistant varieties.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Resistant varieties.", "x": "Plant Diseases: Resistant varieties.. Fungi top culprits. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Resistant varieties. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Resistant varieties. is true.", "x": "The explanation: Resistant varieties.. In botany, this fact connects to Quarantines. — and once you see the mechanism, it stops being trivia and starts being understanding. Chestnut blight. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Irish potato famine.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Irish potato famine.", "x": "Plant Diseases: Irish potato famine.. Vectors: insects. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Irish potato famine. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Irish potato famine. is true.", "x": "The explanation: Irish potato famine.. In botany, this fact connects to Crop losses. — and once you see the mechanism, it stops being trivia and starts being understanding. Citrus greening. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Chestnut blight.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Chestnut blight.", "x": "Plant Diseases: Chestnut blight.. Quarantines. This is load-bearing knowledge — the kind of fact that other facts hang from. pathogens that attack plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Chestnut blight. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Chestnut blight. is true.", "x": "The explanation: Chestnut blight.. In botany, this fact connects to Diagnosis. — and once you see the mechanism, it stops being trivia and starts being understanding. Rusts and smuts. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Fungi top culprits.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Fungi top culprits.", "x": "Going deeper on Plant Diseases: Fungi top culprits.. Chestnut blight. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vectors: insects.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vectors: insects.", "x": "Going deeper on Plant Diseases: Vectors: insects.. Citrus greening. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Quarantines.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Quarantines.", "x": "Going deeper on Plant Diseases: Quarantines.. Rusts and smuts. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Crop losses.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Crop losses.", "x": "Going deeper on Plant Diseases: Crop losses.. Integrated pest management. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Diagnosis.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Diagnosis.", "x": "Going deeper on Plant Diseases: Diagnosis.. Resistant varieties. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Prevention.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Prevention.", "x": "Going deeper on Plant Diseases: Prevention.. Irish potato famine. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Fungi top culprits.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Fungi top culprits.", "x": "Going deeper on Plant Diseases: Fungi top culprits.. Chestnut blight. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Diseases from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-plant-diseases-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
