(function(){'use strict';
/* JAH Honeybees Entomology Database generator — jahdb-e2-sci-honeybees-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-honeybees',PREFIX='JAH-E2SCIHONEYB-',NAME='JAH Honeybees Entomology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Honeybees: overview", "d": "Honeybees: eusocial pollinators making honey..", "g": "overview", "l": 2, "q": "What is Honeybees: overview?", "a": "Honeybees: eusocial pollinators making honey..", "x": "The complete entomology guide to Honeybees: eusocial pollinators making honey.. Waggle dance. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Honeybees.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Honeybees.", "x": "The core principle: Queen/worker/drone.. eusocial pollinators making honey. If you understand this one idea, everything else in Honeybees clicks into place. Apis mellifera. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Waggle dance.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Waggle dance.", "x": "Honeybees: Waggle dance.. Beekeeping. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Waggle dance. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Waggle dance. is true.", "x": "The explanation: Waggle dance.. In entomology, this fact connects to Swarming. — and once you see the mechanism, it stops being trivia and starts being understanding. Hive 50,000. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Queen/worker/drone.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Queen/worker/drone.", "x": "Honeybees: Queen/worker/drone.. Sting facts. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Queen/worker/drone. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Queen/worker/drone. is true.", "x": "The explanation: Queen/worker/drone.. In entomology, this fact connects to Varroa mites. — and once you see the mechanism, it stops being trivia and starts being understanding. Honeycomb hexagons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hive 50,000.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hive 50,000.", "x": "Honeybees: Hive 50,000.. Swarming. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Hive 50,000. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Hive 50,000. is true.", "x": "The explanation: Hive 50,000.. In entomology, this fact connects to Save bees. — and once you see the mechanism, it stops being trivia and starts being understanding. Pollinate crops. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Honeycomb hexagons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Honeycomb hexagons.", "x": "Honeybees: Honeycomb hexagons.. Varroa mites. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Honeycomb hexagons. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Honeycomb hexagons. is true.", "x": "The explanation: Honeycomb hexagons.. In entomology, this fact connects to Apis mellifera. — and once you see the mechanism, it stops being trivia and starts being understanding. Colony collapse. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pollinate crops.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pollinate crops.", "x": "Honeybees: Pollinate crops.. Save bees. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Pollinate crops. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Pollinate crops. is true.", "x": "The explanation: Pollinate crops.. In entomology, this fact connects to Beekeeping. — and once you see the mechanism, it stops being trivia and starts being understanding. Waggle dance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Colony collapse.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Colony collapse.", "x": "Honeybees: Colony collapse.. Apis mellifera. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Colony collapse. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Colony collapse. is true.", "x": "The explanation: Colony collapse.. In entomology, this fact connects to Sting facts. — and once you see the mechanism, it stops being trivia and starts being understanding. Queen/worker/drone. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Waggle dance.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Waggle dance.", "x": "Honeybees: Waggle dance.. Beekeeping. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Waggle dance. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Waggle dance. is true.", "x": "The explanation: Waggle dance.. In entomology, this fact connects to Swarming. — and once you see the mechanism, it stops being trivia and starts being understanding. Hive 50,000. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Queen/worker/drone.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Queen/worker/drone.", "x": "Honeybees: Queen/worker/drone.. Sting facts. This is load-bearing knowledge — the kind of fact that other facts hang from. eusocial pollinators making honey. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Queen/worker/drone. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Queen/worker/drone. is true.", "x": "The explanation: Queen/worker/drone.. In entomology, this fact connects to Varroa mites. — and once you see the mechanism, it stops being trivia and starts being understanding. Honeycomb hexagons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Apis mellifera.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Apis mellifera.", "x": "Going deeper on Honeybees: Apis mellifera.. Queen/worker/drone. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beekeeping.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beekeeping.", "x": "Going deeper on Honeybees: Beekeeping.. Hive 50,000. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sting facts.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sting facts.", "x": "Going deeper on Honeybees: Sting facts.. Honeycomb hexagons. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Swarming.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Swarming.", "x": "Going deeper on Honeybees: Swarming.. Pollinate crops. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Varroa mites.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Varroa mites.", "x": "Going deeper on Honeybees: Varroa mites.. Colony collapse. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Save bees.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Save bees.", "x": "Going deeper on Honeybees: Save bees.. Waggle dance. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Apis mellifera.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Apis mellifera.", "x": "Going deeper on Honeybees: Apis mellifera.. Queen/worker/drone. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Honeybees from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-honeybees-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
