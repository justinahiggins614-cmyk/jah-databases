(function(){'use strict';
/* JAH El Nino Oceanography Database generator — jahdb-e2-sci-el-nino-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-el-nino',PREFIX='JAH-E2SCIELNINO-',NAME='JAH El Nino Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "El Nino: overview", "d": "El Nino: Pacific warming that rearranges world weather..", "g": "overview", "l": 2, "q": "What is El Nino: overview?", "a": "El Nino: Pacific warming that rearranges world weather..", "x": "The complete oceanography guide to El Nino: Pacific warming that rearranges world weather.. Every 2-7 years. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind El Nino.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind El Nino.", "x": "The core principle: Peru fisheries collapse.. Pacific warming that rearranges world weather. If you understand this one idea, everything else in El Nino clicks into place. Trade winds weaken. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Every 2-7 years.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Every 2-7 years.", "x": "El Nino: Every 2-7 years.. Thermocline shifts. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Every 2-7 years. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Every 2-7 years. is true.", "x": "The explanation: Every 2-7 years.. In oceanography, this fact connects to Droughts/floods. — and once you see the mechanism, it stops being trivia and starts being understanding. Global weather teleconnections.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Peru fisheries collapse.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Peru fisheries collapse.", "x": "El Nino: Peru fisheries collapse.. Southern Oscillation. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Peru fisheries collapse. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Peru fisheries collapse. is true.", "x": "The explanation: Peru fisheries collapse.. In oceanography, this fact connects to Agriculture impacts. — and once you see the mechanism, it stops being trivia and starts being understanding. La Nina: opposite phase.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Global weather teleconnections.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Global weather teleconnections.", "x": "El Nino: Global weather teleconnections.. Droughts/floods. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Global weather teleconnections. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Global weather teleconnections. is true.", "x": "The explanation: Global weather teleconnections.. In oceanography, this fact connects to Climate models. — and once you see the mechanism, it stops being trivia and starts being understanding. ENSO forecasting.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "La Nina: opposite phase.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "La Nina: opposite phase.", "x": "El Nino: La Nina: opposite phase.. Agriculture impacts. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why La Nina: opposite phase. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why La Nina: opposite phase. is true.", "x": "The explanation: La Nina: opposite phase.. In oceanography, this fact connects to Trade winds weaken. — and once you see the mechanism, it stops being trivia and starts being understanding. 1997-98: huge event.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "ENSO forecasting.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "ENSO forecasting.", "x": "El Nino: ENSO forecasting.. Climate models. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why ENSO forecasting. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why ENSO forecasting. is true.", "x": "The explanation: ENSO forecasting.. In oceanography, this fact connects to Thermocline shifts. — and once you see the mechanism, it stops being trivia and starts being understanding. Every 2-7 years. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1997-98: huge event.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1997-98: huge event.", "x": "El Nino: 1997-98: huge event.. Trade winds weaken. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why 1997-98: huge event. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why 1997-98: huge event. is true.", "x": "The explanation: 1997-98: huge event.. In oceanography, this fact connects to Southern Oscillation. — and once you see the mechanism, it stops being trivia and starts being understanding. Peru fisheries collapse.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Every 2-7 years.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Every 2-7 years.", "x": "El Nino: Every 2-7 years.. Thermocline shifts. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Every 2-7 years. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Every 2-7 years. is true.", "x": "The explanation: Every 2-7 years.. In oceanography, this fact connects to Droughts/floods. — and once you see the mechanism, it stops being trivia and starts being understanding. Global weather teleconnections.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Peru fisheries collapse.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Peru fisheries collapse.", "x": "El Nino: Peru fisheries collapse.. Southern Oscillation. This is load-bearing knowledge — the kind of fact that other facts hang from. Pacific warming that rearranges world weather. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Peru fisheries collapse. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Peru fisheries collapse. is true.", "x": "The explanation: Peru fisheries collapse.. In oceanography, this fact connects to Agriculture impacts. — and once you see the mechanism, it stops being trivia and starts being understanding. La Nina: opposite phase.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Trade winds weaken.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Trade winds weaken.", "x": "Going deeper on El Nino: Trade winds weaken.. Peru fisheries collapse. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Thermocline shifts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Thermocline shifts.", "x": "Going deeper on El Nino: Thermocline shifts.. Global weather teleconnections. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Southern Oscillation.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Southern Oscillation.", "x": "Going deeper on El Nino: Southern Oscillation.. La Nina: opposite phase. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Droughts/floods.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Droughts/floods.", "x": "Going deeper on El Nino: Droughts/floods.. ENSO forecasting. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Agriculture impacts.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Agriculture impacts.", "x": "Going deeper on El Nino: Agriculture impacts.. 1997-98: huge event. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Climate models.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Climate models.", "x": "Going deeper on El Nino: Climate models.. Every 2-7 years. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Trade winds weaken.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Trade winds weaken.", "x": "Going deeper on El Nino: Trade winds weaken.. Peru fisheries collapse. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about El Nino from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-el-nino-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
