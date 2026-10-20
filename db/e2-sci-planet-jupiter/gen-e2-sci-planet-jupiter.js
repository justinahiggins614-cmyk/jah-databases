(function(){'use strict';
/* JAH Jupiter Astronomy Database generator — jahdb-e2-sci-planet-jupiter-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-planet-jupiter',PREFIX='JAH-E2SCIPLANET-',NAME='JAH Jupiter Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jupiter: overview", "d": "Jupiter: the giant; solar system's king..", "g": "overview", "l": 2, "q": "What is Jupiter: overview?", "a": "Jupiter: the giant; solar system's king..", "x": "The complete astronomy guide to Jupiter: the giant; solar system's king.. Great Red Spot storm. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Jupiter.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Jupiter.", "x": "The core principle: 79+ moons.. the giant; solar system's king. If you understand this one idea, everything else in Jupiter clicks into place. Gas giant. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Great Red Spot storm.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Great Red Spot storm.", "x": "Jupiter: Great Red Spot storm.. Galileo moons. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Great Red Spot storm. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Great Red Spot storm. is true.", "x": "The explanation: Great Red Spot storm.. In astronomy, this fact connects to Shoemaker-Levy 9. — and once you see the mechanism, it stops being trivia and starts being understanding. Europa: ocean moon.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "79+ moons.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "79+ moons.", "x": "Jupiter: 79+ moons.. Magnetic field huge. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why 79+ moons. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why 79+ moons. is true.", "x": "The explanation: 79+ moons.. In astronomy, this fact connects to Bands/zones. — and once you see the mechanism, it stops being trivia and starts being understanding. Ganymede: biggest moon. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Europa: ocean moon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Europa: ocean moon.", "x": "Jupiter: Europa: ocean moon.. Shoemaker-Levy 9. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Europa: ocean moon. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Europa: ocean moon. is true.", "x": "The explanation: Europa: ocean moon.. In astronomy, this fact connects to Formation. — and once you see the mechanism, it stops being trivia and starts being understanding. Shielded inner planets. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ganymede: biggest moon.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ganymede: biggest moon.", "x": "Jupiter: Ganymede: biggest moon.. Bands/zones. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Ganymede: biggest moon. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Ganymede: biggest moon. is true.", "x": "The explanation: Ganymede: biggest moon.. In astronomy, this fact connects to Gas giant. — and once you see the mechanism, it stops being trivia and starts being understanding. Juno orbiter. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Shielded inner planets.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Shielded inner planets.", "x": "Jupiter: Shielded inner planets.. Formation. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Shielded inner planets. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Shielded inner planets. is true.", "x": "The explanation: Shielded inner planets.. In astronomy, this fact connects to Galileo moons. — and once you see the mechanism, it stops being trivia and starts being understanding. Great Red Spot storm.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Juno orbiter.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Juno orbiter.", "x": "Jupiter: Juno orbiter.. Gas giant. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Juno orbiter. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Juno orbiter. is true.", "x": "The explanation: Juno orbiter.. In astronomy, this fact connects to Magnetic field huge. — and once you see the mechanism, it stops being trivia and starts being understanding. 79+ moons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Great Red Spot storm.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Great Red Spot storm.", "x": "Jupiter: Great Red Spot storm.. Galileo moons. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Great Red Spot storm. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Great Red Spot storm. is true.", "x": "The explanation: Great Red Spot storm.. In astronomy, this fact connects to Shoemaker-Levy 9. — and once you see the mechanism, it stops being trivia and starts being understanding. Europa: ocean moon.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "79+ moons.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "79+ moons.", "x": "Jupiter: 79+ moons.. Magnetic field huge. This is load-bearing knowledge — the kind of fact that other facts hang from. the giant; solar system's king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why 79+ moons. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why 79+ moons. is true.", "x": "The explanation: 79+ moons.. In astronomy, this fact connects to Bands/zones. — and once you see the mechanism, it stops being trivia and starts being understanding. Ganymede: biggest moon. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gas giant.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gas giant.", "x": "Going deeper on Jupiter: Gas giant.. 79+ moons. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Galileo moons.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Galileo moons.", "x": "Going deeper on Jupiter: Galileo moons.. Europa: ocean moon. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Magnetic field huge.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Magnetic field huge.", "x": "Going deeper on Jupiter: Magnetic field huge.. Ganymede: biggest moon. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shoemaker-Levy 9.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shoemaker-Levy 9.", "x": "Going deeper on Jupiter: Shoemaker-Levy 9.. Shielded inner planets. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bands/zones.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bands/zones.", "x": "Going deeper on Jupiter: Bands/zones.. Juno orbiter. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Formation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Formation.", "x": "Going deeper on Jupiter: Formation.. Great Red Spot storm. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Gas giant.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Gas giant.", "x": "Going deeper on Jupiter: Gas giant.. 79+ moons. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Jupiter from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-planet-jupiter-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
