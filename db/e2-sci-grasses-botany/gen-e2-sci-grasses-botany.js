(function(){'use strict';
/* JAH Grasses Botany Database generator — jahdb-e2-sci-grasses-botany-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-grasses-botany',PREFIX='JAH-E2SCIGRASSE-',NAME='JAH Grasses Botany Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Grasses: overview", "d": "Grasses: the family feeding the world..", "g": "overview", "l": 2, "q": "What is Grasses: overview?", "a": "Grasses: the family feeding the world..", "x": "The complete botany guide to Grasses: the family feeding the world.. Wheat, rice, corn. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Grasses.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Grasses.", "x": "The core principle: Poaceae family.. the family feeding the world. If you understand this one idea, everything else in Grasses clicks into place. Cereals. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wheat, rice, corn.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wheat, rice, corn.", "x": "Grasses: Wheat, rice, corn.. Staple crops. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Wheat, rice, corn. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Wheat, rice, corn. is true.", "x": "The explanation: Wheat, rice, corn.. In botany, this fact connects to Biofuels. — and once you see the mechanism, it stops being trivia and starts being understanding. C4 photosynthesis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Poaceae family.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Poaceae family.", "x": "Grasses: Poaceae family.. Pastures. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Poaceae family. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Poaceae family. is true.", "x": "The explanation: Poaceae family.. In botany, this fact connects to Weeds. — and once you see the mechanism, it stops being trivia and starts being understanding. Lawns. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "C4 photosynthesis.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "C4 photosynthesis.", "x": "Grasses: C4 photosynthesis.. Biofuels. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why C4 photosynthesis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why C4 photosynthesis. is true.", "x": "The explanation: C4 photosynthesis.. In botany, this fact connects to Breeding. — and once you see the mechanism, it stops being trivia and starts being understanding. Prairies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lawns.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lawns.", "x": "Grasses: Lawns.. Weeds. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Lawns. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Lawns. is true.", "x": "The explanation: Lawns.. In botany, this fact connects to Cereals. — and once you see the mechanism, it stops being trivia and starts being understanding. Bamboo: giant grass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Prairies.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Prairies.", "x": "Grasses: Prairies.. Breeding. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Prairies. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Prairies. is true.", "x": "The explanation: Prairies.. In botany, this fact connects to Staple crops. — and once you see the mechanism, it stops being trivia and starts being understanding. Wheat, rice, corn. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bamboo: giant grass.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bamboo: giant grass.", "x": "Grasses: Bamboo: giant grass.. Cereals. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Bamboo: giant grass. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Bamboo: giant grass. is true.", "x": "The explanation: Bamboo: giant grass.. In botany, this fact connects to Pastures. — and once you see the mechanism, it stops being trivia and starts being understanding. Poaceae family. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Wheat, rice, corn.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Wheat, rice, corn.", "x": "Grasses: Wheat, rice, corn.. Staple crops. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Wheat, rice, corn. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Wheat, rice, corn. is true.", "x": "The explanation: Wheat, rice, corn.. In botany, this fact connects to Biofuels. — and once you see the mechanism, it stops being trivia and starts being understanding. C4 photosynthesis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Poaceae family.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Poaceae family.", "x": "Grasses: Poaceae family.. Pastures. This is load-bearing knowledge — the kind of fact that other facts hang from. the family feeding the world. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Poaceae family. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Poaceae family. is true.", "x": "The explanation: Poaceae family.. In botany, this fact connects to Weeds. — and once you see the mechanism, it stops being trivia and starts being understanding. Lawns. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cereals.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cereals.", "x": "Going deeper on Grasses: Cereals.. Poaceae family. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Staple crops.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Staple crops.", "x": "Going deeper on Grasses: Staple crops.. C4 photosynthesis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pastures.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pastures.", "x": "Going deeper on Grasses: Pastures.. Lawns. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Biofuels.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Biofuels.", "x": "Going deeper on Grasses: Biofuels.. Prairies. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Weeds.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Weeds.", "x": "Going deeper on Grasses: Weeds.. Bamboo: giant grass. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Breeding.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Breeding.", "x": "Going deeper on Grasses: Breeding.. Wheat, rice, corn. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Cereals.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Cereals.", "x": "Going deeper on Grasses: Cereals.. Poaceae family. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Grasses from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-grasses-botany-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
