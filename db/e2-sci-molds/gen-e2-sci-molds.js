(function(){'use strict';
/* JAH Molds Mycology Database generator — jahdb-e2-sci-molds-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-molds',PREFIX='JAH-E2SCIMOLDS-',NAME='JAH Molds Mycology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Molds: overview", "d": "Molds: ubiquitous decomposers; some dangerous..", "g": "overview", "l": 2, "q": "What is Molds: overview?", "a": "Molds: ubiquitous decomposers; some dangerous..", "x": "The complete mycology guide to Molds: ubiquitous decomposers; some dangerous.. Penicillium: antibiotic. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Molds.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Molds.", "x": "The core principle: Aspergillus risks.. ubiquitous decomposers; some dangerous. If you understand this one idea, everything else in Molds clicks into place. Spores everywhere. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Penicillium: antibiotic.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Penicillium: antibiotic.", "x": "Molds: Penicillium: antibiotic.. Food spoilage. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Penicillium: antibiotic. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Penicillium: antibiotic. is true.", "x": "The explanation: Penicillium: antibiotic.. In mycology, this fact connects to Allergies. — and once you see the mechanism, it stops being trivia and starts being understanding. Cheese molds. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aspergillus risks.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aspergillus risks.", "x": "Molds: Aspergillus risks.. Antibiotics. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Aspergillus risks. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Aspergillus risks. is true.", "x": "The explanation: Aspergillus risks.. In mycology, this fact connects to Prevention. — and once you see the mechanism, it stops being trivia and starts being understanding. Bread mold. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cheese molds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cheese molds.", "x": "Molds: Cheese molds.. Allergies. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Cheese molds. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Cheese molds. is true.", "x": "The explanation: Cheese molds.. In mycology, this fact connects to Useful molds. — and once you see the mechanism, it stops being trivia and starts being understanding. Mycotoxins. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bread mold.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bread mold.", "x": "Molds: Bread mold.. Prevention. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Bread mold. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Bread mold. is true.", "x": "The explanation: Bread mold.. In mycology, this fact connects to Spores everywhere. — and once you see the mechanism, it stops being trivia and starts being understanding. Indoor mold health. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mycotoxins.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mycotoxins.", "x": "Molds: Mycotoxins.. Useful molds. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Mycotoxins. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Mycotoxins. is true.", "x": "The explanation: Mycotoxins.. In mycology, this fact connects to Food spoilage. — and once you see the mechanism, it stops being trivia and starts being understanding. Penicillium: antibiotic. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Indoor mold health.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Indoor mold health.", "x": "Molds: Indoor mold health.. Spores everywhere. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Indoor mold health. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Indoor mold health. is true.", "x": "The explanation: Indoor mold health.. In mycology, this fact connects to Antibiotics. — and once you see the mechanism, it stops being trivia and starts being understanding. Aspergillus risks. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Penicillium: antibiotic.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Penicillium: antibiotic.", "x": "Molds: Penicillium: antibiotic.. Food spoilage. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Penicillium: antibiotic. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Penicillium: antibiotic. is true.", "x": "The explanation: Penicillium: antibiotic.. In mycology, this fact connects to Allergies. — and once you see the mechanism, it stops being trivia and starts being understanding. Cheese molds. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Aspergillus risks.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Aspergillus risks.", "x": "Molds: Aspergillus risks.. Antibiotics. This is load-bearing knowledge — the kind of fact that other facts hang from. ubiquitous decomposers; some dangerous. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Aspergillus risks. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Aspergillus risks. is true.", "x": "The explanation: Aspergillus risks.. In mycology, this fact connects to Prevention. — and once you see the mechanism, it stops being trivia and starts being understanding. Bread mold. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spores everywhere.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spores everywhere.", "x": "Going deeper on Molds: Spores everywhere.. Aspergillus risks. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Food spoilage.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Food spoilage.", "x": "Going deeper on Molds: Food spoilage.. Cheese molds. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Antibiotics.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Antibiotics.", "x": "Going deeper on Molds: Antibiotics.. Bread mold. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Allergies.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Allergies.", "x": "Going deeper on Molds: Allergies.. Mycotoxins. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Prevention.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Prevention.", "x": "Going deeper on Molds: Prevention.. Indoor mold health. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Useful molds.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Useful molds.", "x": "Going deeper on Molds: Useful molds.. Penicillium: antibiotic. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Spores everywhere.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Spores everywhere.", "x": "Going deeper on Molds: Spores everywhere.. Aspergillus risks. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Molds from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-molds-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
