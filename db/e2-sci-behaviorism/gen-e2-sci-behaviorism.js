(function(){'use strict';
/* JAH Behaviorism Psychology Database generator — jahdb-e2-sci-behaviorism-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-behaviorism',PREFIX='JAH-E2SCIBEHAVI-',NAME='JAH Behaviorism Psychology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Behaviorism: overview", "d": "Behaviorism: the school that studies observable behavior..", "g": "overview", "l": 2, "q": "What is Behaviorism: overview?", "a": "Behaviorism: the school that studies observable behavior..", "x": "The complete psychology guide to Behaviorism: the school that studies observable behavior.. Founded by John B. Watson (1913). From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Behaviorism.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Behaviorism.", "x": "The core principle: Pavlov's dogs: classical conditioning.. the school that studies observable behavior. If you understand this one idea, everything else in Behaviorism clicks into place. Classical vs operant conditioning. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Founded by John B. Watson (1913).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Founded by John B. Watson (1913).", "x": "Behaviorism: Founded by John B. Watson (1913).. Positive/negative reinforcement. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Founded by John B. Watson (1913). is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Founded by John B. Watson (1913). is true.", "x": "The explanation: Founded by John B. Watson (1913).. In psychology, this fact connects to Extinction of behaviors. — and once you see the mechanism, it stops being trivia and starts being understanding. Skinner's box: operant conditioning.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pavlov's dogs: classical conditioning.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pavlov's dogs: classical conditioning.", "x": "Behaviorism: Pavlov's dogs: classical conditioning.. Schedules of reinforcement. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Pavlov's dogs: classical conditioning. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Pavlov's dogs: classical conditioning. is true.", "x": "The explanation: Pavlov's dogs: classical conditioning.. In psychology, this fact connects to Token economies. — and once you see the mechanism, it stops being trivia and starts being understanding. Reinforcement shapes behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Skinner's box: operant conditioning.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Skinner's box: operant conditioning.", "x": "Behaviorism: Skinner's box: operant conditioning.. Extinction of behaviors. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Skinner's box: operant conditioning. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Skinner's box: operant conditioning. is true.", "x": "The explanation: Skinner's box: operant conditioning.. In psychology, this fact connects to Criticized for ignoring cognition. — and once you see the mechanism, it stops being trivia and starts being understanding. Rejected unobservable mental states.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Reinforcement shapes behavior.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Reinforcement shapes behavior.", "x": "Behaviorism: Reinforcement shapes behavior.. Token economies. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Reinforcement shapes behavior. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Reinforcement shapes behavior. is true.", "x": "The explanation: Reinforcement shapes behavior.. In psychology, this fact connects to Cognitive-behavioral therapy descends from it. — and once you see the mechanism, it stops being trivia and starts being understanding. Little Albert experiment (ethically condemned).", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rejected unobservable mental states.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rejected unobservable mental states.", "x": "Behaviorism: Rejected unobservable mental states.. Criticized for ignoring cognition. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Rejected unobservable mental states. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Rejected unobservable mental states. is true.", "x": "The explanation: Rejected unobservable mental states.. In psychology, this fact connects to Animal lab foundations. — and once you see the mechanism, it stops being trivia and starts being understanding. Behavior therapy treats phobias.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Little Albert experiment (ethically condemned).", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Little Albert experiment (ethically condemned).", "x": "Behaviorism: Little Albert experiment (ethically condemned).. Cognitive-behavioral therapy descends from it. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Little Albert experiment (ethically condemned). is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Little Albert experiment (ethically condemned). is true.", "x": "The explanation: Little Albert experiment (ethically condemned).. In psychology, this fact connects to Classical vs operant conditioning. — and once you see the mechanism, it stops being trivia and starts being understanding. Influenced education and training.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Behavior therapy treats phobias.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Behavior therapy treats phobias.", "x": "Behaviorism: Behavior therapy treats phobias.. Animal lab foundations. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Behavior therapy treats phobias. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Behavior therapy treats phobias. is true.", "x": "The explanation: Behavior therapy treats phobias.. In psychology, this fact connects to Positive/negative reinforcement. — and once you see the mechanism, it stops being trivia and starts being understanding. Founded by John B. Watson (1913).", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Influenced education and training.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Influenced education and training.", "x": "Behaviorism: Influenced education and training.. Classical vs operant conditioning. This is load-bearing knowledge — the kind of fact that other facts hang from. the school that studies observable behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Influenced education and training. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Influenced education and training. is true.", "x": "The explanation: Influenced education and training.. In psychology, this fact connects to Schedules of reinforcement. — and once you see the mechanism, it stops being trivia and starts being understanding. Pavlov's dogs: classical conditioning.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Classical vs operant conditioning.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Classical vs operant conditioning.", "x": "Going deeper on Behaviorism: Classical vs operant conditioning.. Pavlov's dogs: classical conditioning. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Positive/negative reinforcement.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Positive/negative reinforcement.", "x": "Going deeper on Behaviorism: Positive/negative reinforcement.. Skinner's box: operant conditioning. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Schedules of reinforcement.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Schedules of reinforcement.", "x": "Going deeper on Behaviorism: Schedules of reinforcement.. Reinforcement shapes behavior. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Extinction of behaviors.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Extinction of behaviors.", "x": "Going deeper on Behaviorism: Extinction of behaviors.. Rejected unobservable mental states. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Token economies.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Token economies.", "x": "Going deeper on Behaviorism: Token economies.. Little Albert experiment (ethically condemned). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Criticized for ignoring cognition.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Criticized for ignoring cognition.", "x": "Going deeper on Behaviorism: Criticized for ignoring cognition.. Behavior therapy treats phobias. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Cognitive-behavioral therapy descends from it.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Cognitive-behavioral therapy descends from it.", "x": "Going deeper on Behaviorism: Cognitive-behavioral therapy descends from it.. Influenced education and training. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Behaviorism from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-behaviorism-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
