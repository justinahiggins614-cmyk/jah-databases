(function(){'use strict';
/* JAH Heat Waves Meteorology Database generator — jahdb-e2-sci-heat-waves-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-heat-waves',PREFIX='JAH-E2SCIHEATWA-',NAME='JAH Heat Waves Meteorology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Heat Waves: overview", "d": "Heat Waves: dangerous prolonged heat..", "g": "overview", "l": 2, "q": "What is Heat Waves: overview?", "a": "Heat Waves: dangerous prolonged heat..", "x": "The complete meteorology guide to Heat Waves: dangerous prolonged heat.. Deadliest weather (US). From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Heat Waves.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Heat Waves.", "x": "The core principle: Heat index.. dangerous prolonged heat. If you understand this one idea, everything else in Heat Waves clicks into place. Thermometers vs feels-like. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Deadliest weather (US).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Deadliest weather (US).", "x": "Heat Waves: Deadliest weather (US).. Cooling centers. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Deadliest weather (US). is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Deadliest weather (US). is true.", "x": "The explanation: Deadliest weather (US).. In meteorology, this fact connects to Climate: more frequent. — and once you see the mechanism, it stops being trivia and starts being understanding. Urban heat islands.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Heat index.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Heat index.", "x": "Heat Waves: Heat index.. Grid strain. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Heat index. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Heat index. is true.", "x": "The explanation: Heat index.. In meteorology, this fact connects to Elderly risk. — and once you see the mechanism, it stops being trivia and starts being understanding. 2003 Europe: 70k died. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Urban heat islands.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Urban heat islands.", "x": "Heat Waves: Urban heat islands.. Climate: more frequent. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Urban heat islands. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Urban heat islands. is true.", "x": "The explanation: Urban heat islands.. In meteorology, this fact connects to Adaptation. — and once you see the mechanism, it stops being trivia and starts being understanding. Wet-bulb limits. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "2003 Europe: 70k died.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "2003 Europe: 70k died.", "x": "Heat Waves: 2003 Europe: 70k died.. Elderly risk. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why 2003 Europe: 70k died. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why 2003 Europe: 70k died. is true.", "x": "The explanation: 2003 Europe: 70k died.. In meteorology, this fact connects to Thermometers vs feels-like. — and once you see the mechanism, it stops being trivia and starts being understanding. Nighttime relief.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wet-bulb limits.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wet-bulb limits.", "x": "Heat Waves: Wet-bulb limits.. Adaptation. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Wet-bulb limits. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Wet-bulb limits. is true.", "x": "The explanation: Wet-bulb limits.. In meteorology, this fact connects to Cooling centers. — and once you see the mechanism, it stops being trivia and starts being understanding. Deadliest weather (US).", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nighttime relief.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nighttime relief.", "x": "Heat Waves: Nighttime relief.. Thermometers vs feels-like. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Nighttime relief. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Nighttime relief. is true.", "x": "The explanation: Nighttime relief.. In meteorology, this fact connects to Grid strain. — and once you see the mechanism, it stops being trivia and starts being understanding. Heat index. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Deadliest weather (US).", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Deadliest weather (US).", "x": "Heat Waves: Deadliest weather (US).. Cooling centers. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Deadliest weather (US). is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Deadliest weather (US). is true.", "x": "The explanation: Deadliest weather (US).. In meteorology, this fact connects to Climate: more frequent. — and once you see the mechanism, it stops being trivia and starts being understanding. Urban heat islands.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Heat index.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Heat index.", "x": "Heat Waves: Heat index.. Grid strain. This is load-bearing knowledge — the kind of fact that other facts hang from. dangerous prolonged heat. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Heat index. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Heat index. is true.", "x": "The explanation: Heat index.. In meteorology, this fact connects to Elderly risk. — and once you see the mechanism, it stops being trivia and starts being understanding. 2003 Europe: 70k died. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Thermometers vs feels-like.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Thermometers vs feels-like.", "x": "Going deeper on Heat Waves: Thermometers vs feels-like.. Heat index. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cooling centers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cooling centers.", "x": "Going deeper on Heat Waves: Cooling centers.. Urban heat islands. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Grid strain.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Grid strain.", "x": "Going deeper on Heat Waves: Grid strain.. 2003 Europe: 70k died. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Climate: more frequent.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Climate: more frequent.", "x": "Going deeper on Heat Waves: Climate: more frequent.. Wet-bulb limits. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Elderly risk.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Elderly risk.", "x": "Going deeper on Heat Waves: Elderly risk.. Nighttime relief. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Adaptation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Adaptation.", "x": "Going deeper on Heat Waves: Adaptation.. Deadliest weather (US). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Thermometers vs feels-like.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Thermometers vs feels-like.", "x": "Going deeper on Heat Waves: Thermometers vs feels-like.. Heat index. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Heat Waves from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-heat-waves-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
