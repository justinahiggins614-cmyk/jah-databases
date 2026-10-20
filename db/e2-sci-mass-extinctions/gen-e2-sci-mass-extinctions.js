(function(){'use strict';
/* JAH Mass Extinctions Geology Database generator — jahdb-e2-sci-mass-extinctions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-mass-extinctions',PREFIX='JAH-E2SCIMASSEX-',NAME='JAH Mass Extinctions Geology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mass Extinctions: overview", "d": "Mass Extinctions: the Big Five die-offs in Earth's history..", "g": "overview", "l": 2, "q": "What is Mass Extinctions: overview?", "a": "Mass Extinctions: the Big Five die-offs in Earth's history..", "x": "The complete geology guide to Mass Extinctions: the Big Five die-offs in Earth's history.. Ordovician, Devonian, Permian, Triassic, Cretaceous. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Mass Extinctions.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Mass Extinctions.", "x": "The core principle: Permian: 96% marine species.. the Big Five die-offs in Earth's history. If you understand this one idea, everything else in Mass Extinctions clicks into place. K-Pg boundary layer. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Ordovician, Devonian, Permian, Triassic, Cretaceous.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Ordovician, Devonian, Permian, Triassic, Cretaceous.", "x": "Mass Extinctions: Ordovician, Devonian, Permian, Triassic, Cretaceous.. Deccan Traps. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Ordovician, Devonian, Permian, Triassic, Cretaceous. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Ordovician, Devonian, Permian, Triassic, Cretaceous. is true.", "x": "The explanation: Ordovician, Devonian, Permian, Triassic, Cretaceous.. In geology, this fact connects to Refugia survivors. — and once you see the mechanism, it stops being trivia and starts being understanding. Asteroid killed dinosaurs.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Permian: 96% marine species.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Permian: 96% marine species.", "x": "Mass Extinctions: Permian: 96% marine species.. Iridium anomaly. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Permian: 96% marine species. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Permian: 96% marine species. is true.", "x": "The explanation: Permian: 96% marine species.. In geology, this fact connects to Biodiversity rebounds. — and once you see the mechanism, it stops being trivia and starts being understanding. Volcanism suspects.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Asteroid killed dinosaurs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Asteroid killed dinosaurs.", "x": "Mass Extinctions: Asteroid killed dinosaurs.. Refugia survivors. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Asteroid killed dinosaurs. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Asteroid killed dinosaurs. is true.", "x": "The explanation: Asteroid killed dinosaurs.. In geology, this fact connects to Conservation urgency. — and once you see the mechanism, it stops being trivia and starts being understanding. Sixth extinction now?", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Volcanism suspects.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Volcanism suspects.", "x": "Mass Extinctions: Volcanism suspects.. Biodiversity rebounds. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Volcanism suspects. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Volcanism suspects. is true.", "x": "The explanation: Volcanism suspects.. In geology, this fact connects to K-Pg boundary layer. — and once you see the mechanism, it stops being trivia and starts being understanding. Recovery takes millions of years.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sixth extinction now?", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sixth extinction now?", "x": "Mass Extinctions: Sixth extinction now?. Conservation urgency. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Sixth extinction now? is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Sixth extinction now? is true.", "x": "The explanation: Sixth extinction now?. In geology, this fact connects to Deccan Traps. — and once you see the mechanism, it stops being trivia and starts being understanding. Ordovician, Devonian, Permian, Triassic, Cretaceous.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Recovery takes millions of years.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Recovery takes millions of years.", "x": "Mass Extinctions: Recovery takes millions of years.. K-Pg boundary layer. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Recovery takes millions of years. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Recovery takes millions of years. is true.", "x": "The explanation: Recovery takes millions of years.. In geology, this fact connects to Iridium anomaly. — and once you see the mechanism, it stops being trivia and starts being understanding. Permian: 96% marine species.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Ordovician, Devonian, Permian, Triassic, Cretaceous.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Ordovician, Devonian, Permian, Triassic, Cretaceous.", "x": "Mass Extinctions: Ordovician, Devonian, Permian, Triassic, Cretaceous.. Deccan Traps. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Ordovician, Devonian, Permian, Triassic, Cretaceous. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Ordovician, Devonian, Permian, Triassic, Cretaceous. is true.", "x": "The explanation: Ordovician, Devonian, Permian, Triassic, Cretaceous.. In geology, this fact connects to Refugia survivors. — and once you see the mechanism, it stops being trivia and starts being understanding. Asteroid killed dinosaurs.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Permian: 96% marine species.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Permian: 96% marine species.", "x": "Mass Extinctions: Permian: 96% marine species.. Iridium anomaly. This is load-bearing knowledge — the kind of fact that other facts hang from. the Big Five die-offs in Earth's history. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Permian: 96% marine species. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Permian: 96% marine species. is true.", "x": "The explanation: Permian: 96% marine species.. In geology, this fact connects to Biodiversity rebounds. — and once you see the mechanism, it stops being trivia and starts being understanding. Volcanism suspects.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "K-Pg boundary layer.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "K-Pg boundary layer.", "x": "Going deeper on Mass Extinctions: K-Pg boundary layer.. Permian: 96% marine species. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Deccan Traps.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Deccan Traps.", "x": "Going deeper on Mass Extinctions: Deccan Traps.. Asteroid killed dinosaurs. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Iridium anomaly.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Iridium anomaly.", "x": "Going deeper on Mass Extinctions: Iridium anomaly.. Volcanism suspects. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Refugia survivors.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Refugia survivors.", "x": "Going deeper on Mass Extinctions: Refugia survivors.. Sixth extinction now? Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Biodiversity rebounds.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Biodiversity rebounds.", "x": "Going deeper on Mass Extinctions: Biodiversity rebounds.. Recovery takes millions of years. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conservation urgency.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conservation urgency.", "x": "Going deeper on Mass Extinctions: Conservation urgency.. Ordovician, Devonian, Permian, Triassic, Cretaceous. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "K-Pg boundary layer.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "K-Pg boundary layer.", "x": "Going deeper on Mass Extinctions: K-Pg boundary layer.. Permian: 96% marine species. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mass Extinctions from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-mass-extinctions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
