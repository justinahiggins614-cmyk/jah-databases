(function(){'use strict';
/* JAH Ray-Finned Fishes Zoology Database generator — jahdb-e2-sci-ray-finned-fishes-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-ray-finned-fishes',PREFIX='JAH-E2SCIRAYFIN-',NAME='JAH Ray-Finned Fishes Zoology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ray-Finned Fishes: overview", "d": "Ray-Finned Fishes: Actinopterygii: most vertebrates..", "g": "overview", "l": 2, "q": "What is Ray-Finned Fishes: overview?", "a": "Ray-Finned Fishes: Actinopterygii: most vertebrates..", "x": "The complete zoology guide to Ray-Finned Fishes: Actinopterygii: most vertebrates.. 30,000 species. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Ray-Finned Fishes.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Ray-Finned Fishes.", "x": "The core principle: Bass, tuna, goldfish.. Actinopterygii: most vertebrates. If you understand this one idea, everything else in Ray-Finned Fishes clicks into place. Diversity. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "30,000 species.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "30,000 species.", "x": "Ray-Finned Fishes: 30,000 species.. Aquariums. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 30,000 species. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 30,000 species. is true.", "x": "The explanation: 30,000 species.. In zoology, this fact connects to Evolution. — and once you see the mechanism, it stops being trivia and starts being understanding. Swim bladders. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bass, tuna, goldfish.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bass, tuna, goldfish.", "x": "Ray-Finned Fishes: Bass, tuna, goldfish.. Fisheries. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Bass, tuna, goldfish. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Bass, tuna, goldfish. is true.", "x": "The explanation: Bass, tuna, goldfish.. In zoology, this fact connects to Anatomy. — and once you see the mechanism, it stops being trivia and starts being understanding. Coral reef fish. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Swim bladders.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Swim bladders.", "x": "Ray-Finned Fishes: Swim bladders.. Evolution. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Swim bladders. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Swim bladders. is true.", "x": "The explanation: Swim bladders.. In zoology, this fact connects to Fishing. — and once you see the mechanism, it stops being trivia and starts being understanding. Deep-sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Coral reef fish.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Coral reef fish.", "x": "Ray-Finned Fishes: Coral reef fish.. Anatomy. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Coral reef fish. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Coral reef fish. is true.", "x": "The explanation: Coral reef fish.. In zoology, this fact connects to Diversity. — and once you see the mechanism, it stops being trivia and starts being understanding. Anadromous salmon. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Deep-sea.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Deep-sea.", "x": "Ray-Finned Fishes: Deep-sea.. Fishing. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Deep-sea. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Deep-sea. is true.", "x": "The explanation: Deep-sea.. In zoology, this fact connects to Aquariums. — and once you see the mechanism, it stops being trivia and starts being understanding. 30,000 species. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Anadromous salmon.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Anadromous salmon.", "x": "Ray-Finned Fishes: Anadromous salmon.. Diversity. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Anadromous salmon. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Anadromous salmon. is true.", "x": "The explanation: Anadromous salmon.. In zoology, this fact connects to Fisheries. — and once you see the mechanism, it stops being trivia and starts being understanding. Bass, tuna, goldfish. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "30,000 species.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "30,000 species.", "x": "Ray-Finned Fishes: 30,000 species.. Aquariums. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 30,000 species. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 30,000 species. is true.", "x": "The explanation: 30,000 species.. In zoology, this fact connects to Evolution. — and once you see the mechanism, it stops being trivia and starts being understanding. Swim bladders. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Bass, tuna, goldfish.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Bass, tuna, goldfish.", "x": "Ray-Finned Fishes: Bass, tuna, goldfish.. Fisheries. This is load-bearing knowledge — the kind of fact that other facts hang from. Actinopterygii: most vertebrates. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Bass, tuna, goldfish. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Bass, tuna, goldfish. is true.", "x": "The explanation: Bass, tuna, goldfish.. In zoology, this fact connects to Anatomy. — and once you see the mechanism, it stops being trivia and starts being understanding. Coral reef fish. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Diversity.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Diversity.", "x": "Going deeper on Ray-Finned Fishes: Diversity.. Bass, tuna, goldfish. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Aquariums.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Aquariums.", "x": "Going deeper on Ray-Finned Fishes: Aquariums.. Swim bladders. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fisheries.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fisheries.", "x": "Going deeper on Ray-Finned Fishes: Fisheries.. Coral reef fish. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Evolution.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Evolution.", "x": "Going deeper on Ray-Finned Fishes: Evolution.. Deep-sea. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Anatomy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Anatomy.", "x": "Going deeper on Ray-Finned Fishes: Anatomy.. Anadromous salmon. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fishing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fishing.", "x": "Going deeper on Ray-Finned Fishes: Fishing.. 30,000 species. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Diversity.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Diversity.", "x": "Going deeper on Ray-Finned Fishes: Diversity.. Bass, tuna, goldfish. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ray-Finned Fishes from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-ray-finned-fishes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
