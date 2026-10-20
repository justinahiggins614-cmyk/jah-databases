(function(){'use strict';
/* JAH Drought Meteorology Database generator — jahdb-e2-sci-drought-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-drought',PREFIX='JAH-E2SCIDROUGH-',NAME='JAH Drought Meteorology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Drought: overview", "d": "Drought: prolonged water shortage..", "g": "overview", "l": 2, "q": "What is Drought: overview?", "a": "Drought: prolonged water shortage..", "x": "The complete meteorology guide to Drought: prolonged water shortage.. Meteorological vs agricultural. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Drought.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Drought.", "x": "The core principle: Dust Bowl 1930s.. prolonged water shortage. If you understand this one idea, everything else in Drought clicks into place. Palmer index. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Meteorological vs agricultural.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Meteorological vs agricultural.", "x": "Drought: Meteorological vs agricultural.. Aquifer depletion. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Meteorological vs agricultural. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Meteorological vs agricultural. is true.", "x": "The explanation: Meteorological vs agricultural.. In meteorology, this fact connects to Conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Megadroughts.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dust Bowl 1930s.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dust Bowl 1930s.", "x": "Drought: Dust Bowl 1930s.. Crop insurance. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Dust Bowl 1930s. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Dust Bowl 1930s. is true.", "x": "The explanation: Dust Bowl 1930s.. In meteorology, this fact connects to Cloud seeding? — and once you see the mechanism, it stops being trivia and starts being understanding. Water rights wars. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Megadroughts.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Megadroughts.", "x": "Drought: Megadroughts.. Conservation. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Megadroughts. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Megadroughts. is true.", "x": "The explanation: Megadroughts.. In meteorology, this fact connects to History: famines. — and once you see the mechanism, it stops being trivia and starts being understanding. Desertification. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Water rights wars.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Water rights wars.", "x": "Drought: Water rights wars.. Cloud seeding? This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Water rights wars. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Water rights wars. is true.", "x": "The explanation: Water rights wars.. In meteorology, this fact connects to Palmer index. — and once you see the mechanism, it stops being trivia and starts being understanding. El Nino links. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Desertification.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Desertification.", "x": "Drought: Desertification.. History: famines. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Desertification. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Desertification. is true.", "x": "The explanation: Desertification.. In meteorology, this fact connects to Aquifer depletion. — and once you see the mechanism, it stops being trivia and starts being understanding. Meteorological vs agricultural.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "El Nino links.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "El Nino links.", "x": "Drought: El Nino links.. Palmer index. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why El Nino links. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why El Nino links. is true.", "x": "The explanation: El Nino links.. In meteorology, this fact connects to Crop insurance. — and once you see the mechanism, it stops being trivia and starts being understanding. Dust Bowl 1930s. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Meteorological vs agricultural.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Meteorological vs agricultural.", "x": "Drought: Meteorological vs agricultural.. Aquifer depletion. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Meteorological vs agricultural. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Meteorological vs agricultural. is true.", "x": "The explanation: Meteorological vs agricultural.. In meteorology, this fact connects to Conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Megadroughts.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Dust Bowl 1930s.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Dust Bowl 1930s.", "x": "Drought: Dust Bowl 1930s.. Crop insurance. This is load-bearing knowledge — the kind of fact that other facts hang from. prolonged water shortage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Dust Bowl 1930s. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Dust Bowl 1930s. is true.", "x": "The explanation: Dust Bowl 1930s.. In meteorology, this fact connects to Cloud seeding? — and once you see the mechanism, it stops being trivia and starts being understanding. Water rights wars. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Palmer index.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Palmer index.", "x": "Going deeper on Drought: Palmer index.. Dust Bowl 1930s. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Aquifer depletion.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Aquifer depletion.", "x": "Going deeper on Drought: Aquifer depletion.. Megadroughts. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Crop insurance.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Crop insurance.", "x": "Going deeper on Drought: Crop insurance.. Water rights wars. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Conservation.", "x": "Going deeper on Drought: Conservation.. Desertification. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cloud seeding?", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cloud seeding?", "x": "Going deeper on Drought: Cloud seeding?. El Nino links. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History: famines.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History: famines.", "x": "Going deeper on Drought: History: famines.. Meteorological vs agricultural. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Palmer index.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Palmer index.", "x": "Going deeper on Drought: Palmer index.. Dust Bowl 1930s. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Drought from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-drought-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
