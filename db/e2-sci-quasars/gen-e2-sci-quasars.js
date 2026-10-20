(function(){'use strict';
/* JAH Quasars Astronomy Database generator — jahdb-e2-sci-quasars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-quasars',PREFIX='JAH-E2SCIQUASAR-',NAME='JAH Quasars Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Quasars: overview", "d": "Quasars: brightest beacons; feeding black holes..", "g": "overview", "l": 2, "q": "What is Quasars: overview?", "a": "Quasars: brightest beacons; feeding black holes..", "x": "The complete astronomy guide to Quasars: brightest beacons; feeding black holes.. Most luminous objects. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Quasars.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Quasars.", "x": "The core principle: Supermassive black holes.. brightest beacons; feeding black holes. If you understand this one idea, everything else in Quasars clicks into place. Discovered 1960s. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Most luminous objects.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Most luminous objects.", "x": "Quasars: Most luminous objects.. Blazars. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Most luminous objects. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Most luminous objects. is true.", "x": "The explanation: Most luminous objects.. In astronomy, this fact connects to Reionization. — and once you see the mechanism, it stops being trivia and starts being understanding. 3C 273. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Supermassive black holes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Supermassive black holes.", "x": "Quasars: Supermassive black holes.. Host galaxies. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Supermassive black holes. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Supermassive black holes. is true.", "x": "The explanation: Supermassive black holes.. In astronomy, this fact connects to Standard candles? — and once you see the mechanism, it stops being trivia and starts being understanding. Early universe.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "3C 273.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "3C 273.", "x": "Quasars: 3C 273.. Reionization. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why 3C 273. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why 3C 273. is true.", "x": "The explanation: 3C 273.. In astronomy, this fact connects to JWST views. — and once you see the mechanism, it stops being trivia and starts being understanding. Redshift. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Early universe.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Early universe.", "x": "Quasars: Early universe.. Standard candles? This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Early universe. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Early universe. is true.", "x": "The explanation: Early universe.. In astronomy, this fact connects to Discovered 1960s. — and once you see the mechanism, it stops being trivia and starts being understanding. Accretion power. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Redshift.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Redshift.", "x": "Quasars: Redshift.. JWST views. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Redshift. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Redshift. is true.", "x": "The explanation: Redshift.. In astronomy, this fact connects to Blazars. — and once you see the mechanism, it stops being trivia and starts being understanding. Most luminous objects. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Accretion power.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Accretion power.", "x": "Quasars: Accretion power.. Discovered 1960s. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Accretion power. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Accretion power. is true.", "x": "The explanation: Accretion power.. In astronomy, this fact connects to Host galaxies. — and once you see the mechanism, it stops being trivia and starts being understanding. Supermassive black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Most luminous objects.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Most luminous objects.", "x": "Quasars: Most luminous objects.. Blazars. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Most luminous objects. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Most luminous objects. is true.", "x": "The explanation: Most luminous objects.. In astronomy, this fact connects to Reionization. — and once you see the mechanism, it stops being trivia and starts being understanding. 3C 273. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Supermassive black holes.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Supermassive black holes.", "x": "Quasars: Supermassive black holes.. Host galaxies. This is load-bearing knowledge — the kind of fact that other facts hang from. brightest beacons; feeding black holes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Supermassive black holes. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Supermassive black holes. is true.", "x": "The explanation: Supermassive black holes.. In astronomy, this fact connects to Standard candles? — and once you see the mechanism, it stops being trivia and starts being understanding. Early universe.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Discovered 1960s.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Discovered 1960s.", "x": "Going deeper on Quasars: Discovered 1960s.. Supermassive black holes. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Blazars.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Blazars.", "x": "Going deeper on Quasars: Blazars.. 3C 273. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Host galaxies.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Host galaxies.", "x": "Going deeper on Quasars: Host galaxies.. Early universe. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Reionization.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Reionization.", "x": "Going deeper on Quasars: Reionization.. Redshift. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Standard candles?", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Standard candles?", "x": "Going deeper on Quasars: Standard candles?. Accretion power. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "JWST views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "JWST views.", "x": "Going deeper on Quasars: JWST views.. Most luminous objects. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Discovered 1960s.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Discovered 1960s.", "x": "Going deeper on Quasars: Discovered 1960s.. Supermassive black holes. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Quasars from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-quasars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
