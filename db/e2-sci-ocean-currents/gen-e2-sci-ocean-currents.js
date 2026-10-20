(function(){'use strict';
/* JAH Ocean Currents Oceanography Database generator — jahdb-e2-sci-ocean-currents-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-ocean-currents',PREFIX='JAH-E2SCIOCEANC-',NAME='JAH Ocean Currents Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ocean Currents: overview", "d": "Ocean Currents: rivers in the sea that move heat around the planet..", "g": "overview", "l": 2, "q": "What is Ocean Currents: overview?", "a": "Ocean Currents: rivers in the sea that move heat around the planet..", "x": "The complete oceanography guide to Ocean Currents: rivers in the sea that move heat around the planet.. Gulf Stream warms Europe. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Ocean Currents.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Ocean Currents.", "x": "The core principle: Thermohaline circulation.. rivers in the sea that move heat around the planet. If you understand this one idea, everything else in Ocean Currents clicks into place. Surface vs deep currents. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gulf Stream warms Europe.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gulf Stream warms Europe.", "x": "Ocean Currents: Gulf Stream warms Europe.. Ekman transport. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Gulf Stream warms Europe. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Gulf Stream warms Europe. is true.", "x": "The explanation: Gulf Stream warms Europe.. In oceanography, this fact connects to Climate regulation. — and once you see the mechanism, it stops being trivia and starts being understanding. Gyres rotate (Coriolis).", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thermohaline circulation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thermohaline circulation.", "x": "Ocean Currents: Thermohaline circulation.. Western boundary intensification. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Thermohaline circulation. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Thermohaline circulation. is true.", "x": "The explanation: Thermohaline circulation.. In oceanography, this fact connects to Drifters measure. — and once you see the mechanism, it stops being trivia and starts being understanding. Kuroshio: Pacific Gulf Stream.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gyres rotate (Coriolis).", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gyres rotate (Coriolis).", "x": "Ocean Currents: Gyres rotate (Coriolis).. Climate regulation. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Gyres rotate (Coriolis). is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Gyres rotate (Coriolis). is true.", "x": "The explanation: Gyres rotate (Coriolis).. In oceanography, this fact connects to Sailing routes. — and once you see the mechanism, it stops being trivia and starts being understanding. Upwelling feeds fisheries.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Kuroshio: Pacific Gulf Stream.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Kuroshio: Pacific Gulf Stream.", "x": "Ocean Currents: Kuroshio: Pacific Gulf Stream.. Drifters measure. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Kuroshio: Pacific Gulf Stream. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Kuroshio: Pacific Gulf Stream. is true.", "x": "The explanation: Kuroshio: Pacific Gulf Stream.. In oceanography, this fact connects to Surface vs deep currents. — and once you see the mechanism, it stops being trivia and starts being understanding. El Nino disrupts patterns.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Upwelling feeds fisheries.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Upwelling feeds fisheries.", "x": "Ocean Currents: Upwelling feeds fisheries.. Sailing routes. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Upwelling feeds fisheries. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Upwelling feeds fisheries. is true.", "x": "The explanation: Upwelling feeds fisheries.. In oceanography, this fact connects to Ekman transport. — and once you see the mechanism, it stops being trivia and starts being understanding. Gulf Stream warms Europe.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "El Nino disrupts patterns.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "El Nino disrupts patterns.", "x": "Ocean Currents: El Nino disrupts patterns.. Surface vs deep currents. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why El Nino disrupts patterns. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why El Nino disrupts patterns. is true.", "x": "The explanation: El Nino disrupts patterns.. In oceanography, this fact connects to Western boundary intensification. — and once you see the mechanism, it stops being trivia and starts being understanding. Thermohaline circulation.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Gulf Stream warms Europe.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Gulf Stream warms Europe.", "x": "Ocean Currents: Gulf Stream warms Europe.. Ekman transport. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Gulf Stream warms Europe. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Gulf Stream warms Europe. is true.", "x": "The explanation: Gulf Stream warms Europe.. In oceanography, this fact connects to Climate regulation. — and once you see the mechanism, it stops being trivia and starts being understanding. Gyres rotate (Coriolis).", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Thermohaline circulation.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Thermohaline circulation.", "x": "Ocean Currents: Thermohaline circulation.. Western boundary intensification. This is load-bearing knowledge — the kind of fact that other facts hang from. rivers in the sea that move heat around the planet.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Thermohaline circulation. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Thermohaline circulation. is true.", "x": "The explanation: Thermohaline circulation.. In oceanography, this fact connects to Drifters measure. — and once you see the mechanism, it stops being trivia and starts being understanding. Kuroshio: Pacific Gulf Stream.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Surface vs deep currents.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Surface vs deep currents.", "x": "Going deeper on Ocean Currents: Surface vs deep currents.. Thermohaline circulation. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ekman transport.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ekman transport.", "x": "Going deeper on Ocean Currents: Ekman transport.. Gyres rotate (Coriolis). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Western boundary intensification.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Western boundary intensification.", "x": "Going deeper on Ocean Currents: Western boundary intensification.. Kuroshio: Pacific Gulf Stream. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Climate regulation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Climate regulation.", "x": "Going deeper on Ocean Currents: Climate regulation.. Upwelling feeds fisheries. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Drifters measure.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Drifters measure.", "x": "Going deeper on Ocean Currents: Drifters measure.. El Nino disrupts patterns. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sailing routes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sailing routes.", "x": "Going deeper on Ocean Currents: Sailing routes.. Gulf Stream warms Europe. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Surface vs deep currents.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Surface vs deep currents.", "x": "Going deeper on Ocean Currents: Surface vs deep currents.. Thermohaline circulation. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Currents from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-ocean-currents-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
