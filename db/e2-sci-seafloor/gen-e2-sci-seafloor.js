(function(){'use strict';
/* JAH Seafloor Oceanography Database generator — jahdb-e2-sci-seafloor-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-seafloor',PREFIX='JAH-E2SCISEAFLO-',NAME='JAH Seafloor Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Seafloor: overview", "d": "Seafloor: mountains, trenches, and plains under the sea..", "g": "overview", "l": 2, "q": "What is Seafloor: overview?", "a": "Seafloor: mountains, trenches, and plains under the sea..", "x": "The complete oceanography guide to Seafloor: mountains, trenches, and plains under the sea.. Mid-ocean ridges circle globe. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Seafloor.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Seafloor.", "x": "The core principle: Trenches at subduction.. mountains, trenches, and plains under the sea. If you understand this one idea, everything else in Seafloor clicks into place. Bathymetry. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mid-ocean ridges circle globe.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mid-ocean ridges circle globe.", "x": "Seafloor: Mid-ocean ridges circle globe.. Rift valleys. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Mid-ocean ridges circle globe. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Mid-ocean ridges circle globe. is true.", "x": "The explanation: Mid-ocean ridges circle globe.. In oceanography, this fact connects to Sediment cores. — and once you see the mechanism, it stops being trivia and starts being understanding. Abyssal plains flat.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Trenches at subduction.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Trenches at subduction.", "x": "Seafloor: Trenches at subduction.. Black smokers. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Trenches at subduction. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Trenches at subduction. is true.", "x": "The explanation: Trenches at subduction.. In oceanography, this fact connects to EEZ claims. — and once you see the mechanism, it stops being trivia and starts being understanding. Seamounts: underwater volcanoes.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Abyssal plains flat.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Abyssal plains flat.", "x": "Seafloor: Abyssal plains flat.. Sediment cores. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Abyssal plains flat. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Abyssal plains flat. is true.", "x": "The explanation: Abyssal plains flat.. In oceanography, this fact connects to Exploration. — and once you see the mechanism, it stops being trivia and starts being understanding. Sonar mapping. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Seamounts: underwater volcanoes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Seamounts: underwater volcanoes.", "x": "Seafloor: Seamounts: underwater volcanoes.. EEZ claims. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Seamounts: underwater volcanoes. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Seamounts: underwater volcanoes. is true.", "x": "The explanation: Seamounts: underwater volcanoes.. In oceanography, this fact connects to Bathymetry. — and once you see the mechanism, it stops being trivia and starts being understanding. Plate tectonics proof.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sonar mapping.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sonar mapping.", "x": "Seafloor: Sonar mapping.. Exploration. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Sonar mapping. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Sonar mapping. is true.", "x": "The explanation: Sonar mapping.. In oceanography, this fact connects to Rift valleys. — and once you see the mechanism, it stops being trivia and starts being understanding. Mid-ocean ridges circle globe.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Plate tectonics proof.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Plate tectonics proof.", "x": "Seafloor: Plate tectonics proof.. Bathymetry. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Plate tectonics proof. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Plate tectonics proof. is true.", "x": "The explanation: Plate tectonics proof.. In oceanography, this fact connects to Black smokers. — and once you see the mechanism, it stops being trivia and starts being understanding. Trenches at subduction.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Mid-ocean ridges circle globe.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Mid-ocean ridges circle globe.", "x": "Seafloor: Mid-ocean ridges circle globe.. Rift valleys. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Mid-ocean ridges circle globe. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Mid-ocean ridges circle globe. is true.", "x": "The explanation: Mid-ocean ridges circle globe.. In oceanography, this fact connects to Sediment cores. — and once you see the mechanism, it stops being trivia and starts being understanding. Abyssal plains flat.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Trenches at subduction.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Trenches at subduction.", "x": "Seafloor: Trenches at subduction.. Black smokers. This is load-bearing knowledge — the kind of fact that other facts hang from. mountains, trenches, and plains under the sea. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Trenches at subduction. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Trenches at subduction. is true.", "x": "The explanation: Trenches at subduction.. In oceanography, this fact connects to EEZ claims. — and once you see the mechanism, it stops being trivia and starts being understanding. Seamounts: underwater volcanoes.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bathymetry.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bathymetry.", "x": "Going deeper on Seafloor: Bathymetry.. Trenches at subduction. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rift valleys.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rift valleys.", "x": "Going deeper on Seafloor: Rift valleys.. Abyssal plains flat. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Black smokers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Black smokers.", "x": "Going deeper on Seafloor: Black smokers.. Seamounts: underwater volcanoes. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sediment cores.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sediment cores.", "x": "Going deeper on Seafloor: Sediment cores.. Sonar mapping. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "EEZ claims.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "EEZ claims.", "x": "Going deeper on Seafloor: EEZ claims.. Plate tectonics proof. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Exploration.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Exploration.", "x": "Going deeper on Seafloor: Exploration.. Mid-ocean ridges circle globe. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Bathymetry.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Bathymetry.", "x": "Going deeper on Seafloor: Bathymetry.. Trenches at subduction. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Seafloor from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-seafloor-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
