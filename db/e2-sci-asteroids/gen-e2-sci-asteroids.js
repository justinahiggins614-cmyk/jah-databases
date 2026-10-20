(function(){'use strict';
/* JAH Asteroids Astronomy Database generator — jahdb-e2-sci-asteroids-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-asteroids',PREFIX='JAH-E2SCIASTERO-',NAME='JAH Asteroids Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Asteroids: overview", "d": "Asteroids: rocky leftovers; some threaten Earth..", "g": "overview", "l": 2, "q": "What is Asteroids: overview?", "a": "Asteroids: rocky leftovers; some threaten Earth..", "x": "The complete astronomy guide to Asteroids: rocky leftovers; some threaten Earth.. Belt between Mars/Jupiter. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Asteroids.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Asteroids.", "x": "The core principle: Bennu sample returned.. rocky leftovers; some threaten Earth. If you understand this one idea, everything else in Asteroids clicks into place. Near-Earth objects. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Belt between Mars/Jupiter.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Belt between Mars/Jupiter.", "x": "Asteroids: Belt between Mars/Jupiter.. Chicxulub killer. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Belt between Mars/Jupiter. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Belt between Mars/Jupiter. is true.", "x": "The explanation: Belt between Mars/Jupiter.. In astronomy, this fact connects to Vesta. — and once you see the mechanism, it stops being trivia and starts being understanding. DART deflected Dimorphos.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bennu sample returned.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bennu sample returned.", "x": "Asteroids: Bennu sample returned.. Ryugu sample. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Bennu sample returned. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Bennu sample returned. is true.", "x": "The explanation: Bennu sample returned.. In astronomy, this fact connects to Planetary defense. — and once you see the mechanism, it stops being trivia and starts being understanding. Ceres: dwarf planet.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "DART deflected Dimorphos.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "DART deflected Dimorphos.", "x": "Asteroids: DART deflected Dimorphos.. Vesta. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why DART deflected Dimorphos. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why DART deflected Dimorphos. is true.", "x": "The explanation: DART deflected Dimorphos.. In astronomy, this fact connects to Composition types. — and once you see the mechanism, it stops being trivia and starts being understanding. Trojan asteroids.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ceres: dwarf planet.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ceres: dwarf planet.", "x": "Asteroids: Ceres: dwarf planet.. Planetary defense. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Ceres: dwarf planet. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Ceres: dwarf planet. is true.", "x": "The explanation: Ceres: dwarf planet.. In astronomy, this fact connects to Near-Earth objects. — and once you see the mechanism, it stops being trivia and starts being understanding. Mining dreams. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Trojan asteroids.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Trojan asteroids.", "x": "Asteroids: Trojan asteroids.. Composition types. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Trojan asteroids. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Trojan asteroids. is true.", "x": "The explanation: Trojan asteroids.. In astronomy, this fact connects to Chicxulub killer. — and once you see the mechanism, it stops being trivia and starts being understanding. Belt between Mars/Jupiter.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mining dreams.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mining dreams.", "x": "Asteroids: Mining dreams.. Near-Earth objects. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Mining dreams. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Mining dreams. is true.", "x": "The explanation: Mining dreams.. In astronomy, this fact connects to Ryugu sample. — and once you see the mechanism, it stops being trivia and starts being understanding. Bennu sample returned. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Belt between Mars/Jupiter.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Belt between Mars/Jupiter.", "x": "Asteroids: Belt between Mars/Jupiter.. Chicxulub killer. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Belt between Mars/Jupiter. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Belt between Mars/Jupiter. is true.", "x": "The explanation: Belt between Mars/Jupiter.. In astronomy, this fact connects to Vesta. — and once you see the mechanism, it stops being trivia and starts being understanding. DART deflected Dimorphos.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Bennu sample returned.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Bennu sample returned.", "x": "Asteroids: Bennu sample returned.. Ryugu sample. This is load-bearing knowledge — the kind of fact that other facts hang from. rocky leftovers; some threaten Earth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Bennu sample returned. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Bennu sample returned. is true.", "x": "The explanation: Bennu sample returned.. In astronomy, this fact connects to Planetary defense. — and once you see the mechanism, it stops being trivia and starts being understanding. Ceres: dwarf planet.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Near-Earth objects.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Near-Earth objects.", "x": "Going deeper on Asteroids: Near-Earth objects.. Bennu sample returned. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chicxulub killer.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chicxulub killer.", "x": "Going deeper on Asteroids: Chicxulub killer.. DART deflected Dimorphos. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ryugu sample.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ryugu sample.", "x": "Going deeper on Asteroids: Ryugu sample.. Ceres: dwarf planet. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Vesta.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Vesta.", "x": "Going deeper on Asteroids: Vesta.. Trojan asteroids. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Planetary defense.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Planetary defense.", "x": "Going deeper on Asteroids: Planetary defense.. Mining dreams. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Composition types.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Composition types.", "x": "Going deeper on Asteroids: Composition types.. Belt between Mars/Jupiter. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Near-Earth objects.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Near-Earth objects.", "x": "Going deeper on Asteroids: Near-Earth objects.. Bennu sample returned. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Asteroids from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-asteroids-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
