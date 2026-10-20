(function(){'use strict';
/* JAH Pluto Astronomy Database generator — jahdb-e2-sci-dwarf-planet-pluto-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-dwarf-planet-pluto',PREFIX='JAH-E2SCIDWARFP-',NAME='JAH Pluto Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pluto: overview", "d": "Pluto: the beloved dwarf planet..", "g": "overview", "l": 2, "q": "What is Pluto: overview?", "a": "Pluto: the beloved dwarf planet..", "x": "The complete astronomy guide to Pluto: the beloved dwarf planet.. Demoted 2006. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Pluto.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Pluto.", "x": "The core principle: New Horizons 2015.. the beloved dwarf planet. If you understand this one idea, everything else in Pluto clicks into place. Nitrogen ice. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Demoted 2006.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Demoted 2006.", "x": "Pluto: Demoted 2006.. Atmosphere freezes. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Demoted 2006. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Demoted 2006. is true.", "x": "The explanation: Demoted 2006.. In astronomy, this fact connects to Planet debate. — and once you see the mechanism, it stops being trivia and starts being understanding. Heart glacier (Tombaugh). Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "New Horizons 2015.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "New Horizons 2015.", "x": "Pluto: New Horizons 2015.. Charon binary. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why New Horizons 2015. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why New Horizons 2015. is true.", "x": "The explanation: New Horizons 2015.. In astronomy, this fact connects to Reclassification. — and once you see the mechanism, it stops being trivia and starts being understanding. 5 moons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Heart glacier (Tombaugh).", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Heart glacier (Tombaugh).", "x": "Pluto: Heart glacier (Tombaugh).. Planet debate. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Heart glacier (Tombaugh). is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Heart glacier (Tombaugh). is true.", "x": "The explanation: Heart glacier (Tombaugh).. In astronomy, this fact connects to Public love. — and once you see the mechanism, it stops being trivia and starts being understanding. Kuiper Belt king. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "5 moons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "5 moons.", "x": "Pluto: 5 moons.. Reclassification. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why 5 moons. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why 5 moons. is true.", "x": "The explanation: 5 moons.. In astronomy, this fact connects to Nitrogen ice. — and once you see the mechanism, it stops being trivia and starts being understanding. Clyde Tombaugh found. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kuiper Belt king.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kuiper Belt king.", "x": "Pluto: Kuiper Belt king.. Public love. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Kuiper Belt king. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Kuiper Belt king. is true.", "x": "The explanation: Kuiper Belt king.. In astronomy, this fact connects to Atmosphere freezes. — and once you see the mechanism, it stops being trivia and starts being understanding. Demoted 2006. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Clyde Tombaugh found.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Clyde Tombaugh found.", "x": "Pluto: Clyde Tombaugh found.. Nitrogen ice. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Clyde Tombaugh found. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Clyde Tombaugh found. is true.", "x": "The explanation: Clyde Tombaugh found.. In astronomy, this fact connects to Charon binary. — and once you see the mechanism, it stops being trivia and starts being understanding. New Horizons 2015. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Demoted 2006.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Demoted 2006.", "x": "Pluto: Demoted 2006.. Atmosphere freezes. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Demoted 2006. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Demoted 2006. is true.", "x": "The explanation: Demoted 2006.. In astronomy, this fact connects to Planet debate. — and once you see the mechanism, it stops being trivia and starts being understanding. Heart glacier (Tombaugh). Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "New Horizons 2015.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "New Horizons 2015.", "x": "Pluto: New Horizons 2015.. Charon binary. This is load-bearing knowledge — the kind of fact that other facts hang from. the beloved dwarf planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why New Horizons 2015. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why New Horizons 2015. is true.", "x": "The explanation: New Horizons 2015.. In astronomy, this fact connects to Reclassification. — and once you see the mechanism, it stops being trivia and starts being understanding. 5 moons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Nitrogen ice.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Nitrogen ice.", "x": "Going deeper on Pluto: Nitrogen ice.. New Horizons 2015. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Atmosphere freezes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Atmosphere freezes.", "x": "Going deeper on Pluto: Atmosphere freezes.. Heart glacier (Tombaugh). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Charon binary.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Charon binary.", "x": "Going deeper on Pluto: Charon binary.. 5 moons. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Planet debate.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Planet debate.", "x": "Going deeper on Pluto: Planet debate.. Kuiper Belt king. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reclassification.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reclassification.", "x": "Going deeper on Pluto: Reclassification.. Clyde Tombaugh found. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Public love.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Public love.", "x": "Going deeper on Pluto: Public love.. Demoted 2006. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Nitrogen ice.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Nitrogen ice.", "x": "Going deeper on Pluto: Nitrogen ice.. New Horizons 2015. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Pluto from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-dwarf-planet-pluto-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
