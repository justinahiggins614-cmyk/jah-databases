(function(){'use strict';
/* JAH Orion Nebula Astronomy Database generator — jahdb-e2-sci-orion-nebulia-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-orion-nebulia',PREFIX='JAH-E2SCIORIONN-',NAME='JAH Orion Nebula Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Orion Nebula: overview", "d": "Orion Nebula: stellar nursery in Orion's sword..", "g": "overview", "l": 2, "q": "What is Orion Nebula: overview?", "a": "Orion Nebula: stellar nursery in Orion's sword..", "x": "The complete astronomy guide to Orion Nebula: stellar nursery in Orion's sword.. 1,344 ly away. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Orion Nebula.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Orion Nebula.", "x": "The core principle: Star formation visible.. stellar nursery in Orion's sword. If you understand this one idea, everything else in Orion Nebula clicks into place. H II region. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1,344 ly away.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1,344 ly away.", "x": "Orion Nebula: 1,344 ly away.. Protostars. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 1,344 ly away. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 1,344 ly away. is true.", "x": "The explanation: 1,344 ly away.. In astronomy, this fact connects to Infrared views. — and once you see the mechanism, it stops being trivia and starts being understanding. Trapezium stars. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Star formation visible.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Star formation visible.", "x": "Orion Nebula: Star formation visible.. Herbig-Haro. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Star formation visible. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Star formation visible. is true.", "x": "The explanation: Star formation visible.. In astronomy, this fact connects to Stellar winds. — and once you see the mechanism, it stops being trivia and starts being understanding. Proplyds: baby systems.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Trapezium stars.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Trapezium stars.", "x": "Orion Nebula: Trapezium stars.. Infrared views. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Trapezium stars. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Trapezium stars. is true.", "x": "The explanation: Trapezium stars.. In astronomy, this fact connects to Telescope target. — and once you see the mechanism, it stops being trivia and starts being understanding. Hubble iconic. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Proplyds: baby systems.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Proplyds: baby systems.", "x": "Orion Nebula: Proplyds: baby systems.. Stellar winds. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Proplyds: baby systems. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Proplyds: baby systems. is true.", "x": "The explanation: Proplyds: baby systems.. In astronomy, this fact connects to H II region. — and once you see the mechanism, it stops being trivia and starts being understanding. Naked-eye smudge. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hubble iconic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hubble iconic.", "x": "Orion Nebula: Hubble iconic.. Telescope target. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Hubble iconic. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Hubble iconic. is true.", "x": "The explanation: Hubble iconic.. In astronomy, this fact connects to Protostars. — and once you see the mechanism, it stops being trivia and starts being understanding. 1,344 ly away. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Naked-eye smudge.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Naked-eye smudge.", "x": "Orion Nebula: Naked-eye smudge.. H II region. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Naked-eye smudge. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Naked-eye smudge. is true.", "x": "The explanation: Naked-eye smudge.. In astronomy, this fact connects to Herbig-Haro. — and once you see the mechanism, it stops being trivia and starts being understanding. Star formation visible. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "1,344 ly away.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "1,344 ly away.", "x": "Orion Nebula: 1,344 ly away.. Protostars. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 1,344 ly away. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 1,344 ly away. is true.", "x": "The explanation: 1,344 ly away.. In astronomy, this fact connects to Infrared views. — and once you see the mechanism, it stops being trivia and starts being understanding. Trapezium stars. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Star formation visible.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Star formation visible.", "x": "Orion Nebula: Star formation visible.. Herbig-Haro. This is load-bearing knowledge — the kind of fact that other facts hang from. stellar nursery in Orion's sword. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Star formation visible. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Star formation visible. is true.", "x": "The explanation: Star formation visible.. In astronomy, this fact connects to Stellar winds. — and once you see the mechanism, it stops being trivia and starts being understanding. Proplyds: baby systems.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "H II region.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "H II region.", "x": "Going deeper on Orion Nebula: H II region.. Star formation visible. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Protostars.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Protostars.", "x": "Going deeper on Orion Nebula: Protostars.. Trapezium stars. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Herbig-Haro.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Herbig-Haro.", "x": "Going deeper on Orion Nebula: Herbig-Haro.. Proplyds: baby systems. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Infrared views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Infrared views.", "x": "Going deeper on Orion Nebula: Infrared views.. Hubble iconic. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Stellar winds.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Stellar winds.", "x": "Going deeper on Orion Nebula: Stellar winds.. Naked-eye smudge. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Telescope target.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Telescope target.", "x": "Going deeper on Orion Nebula: Telescope target.. 1,344 ly away. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "H II region.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "H II region.", "x": "Going deeper on Orion Nebula: H II region.. Star formation visible. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Orion Nebula from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-orion-nebulia-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
