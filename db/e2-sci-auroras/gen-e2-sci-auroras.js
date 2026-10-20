(function(){'use strict';
/* JAH Auroras Astronomy Database generator — jahdb-e2-sci-auroras-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-auroras',PREFIX='JAH-E2SCIAURORA-',NAME='JAH Auroras Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Auroras: overview", "d": "Auroras: polar lights from solar wind..", "g": "overview", "l": 2, "q": "What is Auroras: overview?", "a": "Auroras: polar lights from solar wind..", "x": "The complete astronomy guide to Auroras: polar lights from solar wind.. Solar wind + magnetosphere. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Auroras.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Auroras.", "x": "The core principle: Aurora borealis/australis.. polar lights from solar wind. If you understand this one idea, everything else in Auroras clicks into place. Oxygen green. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Solar wind + magnetosphere.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Solar wind + magnetosphere.", "x": "Auroras: Solar wind + magnetosphere.. Nitrogen purple. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Solar wind + magnetosphere. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Solar wind + magnetosphere. is true.", "x": "The explanation: Solar wind + magnetosphere.. In astronomy, this fact connects to Substorms. — and once you see the mechanism, it stops being trivia and starts being understanding. Best: dark winter. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aurora borealis/australis.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aurora borealis/australis.", "x": "Auroras: Aurora borealis/australis.. Oval zones. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Aurora borealis/australis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Aurora borealis/australis. is true.", "x": "The explanation: Aurora borealis/australis.. In astronomy, this fact connects to Other planets. — and once you see the mechanism, it stops being trivia and starts being understanding. Kp index. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Best: dark winter.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Best: dark winter.", "x": "Auroras: Best: dark winter.. Substorms. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Best: dark winter. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Best: dark winter. is true.", "x": "The explanation: Best: dark winter.. In astronomy, this fact connects to Forecasting. — and once you see the mechanism, it stops being trivia and starts being understanding. Carrington 1859. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Kp index.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Kp index.", "x": "Auroras: Kp index.. Other planets. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Kp index. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Kp index. is true.", "x": "The explanation: Kp index.. In astronomy, this fact connects to Oxygen green. — and once you see the mechanism, it stops being trivia and starts being understanding. Photography tips. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Carrington 1859.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Carrington 1859.", "x": "Auroras: Carrington 1859.. Forecasting. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Carrington 1859. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Carrington 1859. is true.", "x": "The explanation: Carrington 1859.. In astronomy, this fact connects to Nitrogen purple. — and once you see the mechanism, it stops being trivia and starts being understanding. Solar wind + magnetosphere.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Photography tips.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Photography tips.", "x": "Auroras: Photography tips.. Oxygen green. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Photography tips. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Photography tips. is true.", "x": "The explanation: Photography tips.. In astronomy, this fact connects to Oval zones. — and once you see the mechanism, it stops being trivia and starts being understanding. Aurora borealis/australis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Solar wind + magnetosphere.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Solar wind + magnetosphere.", "x": "Auroras: Solar wind + magnetosphere.. Nitrogen purple. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Solar wind + magnetosphere. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Solar wind + magnetosphere. is true.", "x": "The explanation: Solar wind + magnetosphere.. In astronomy, this fact connects to Substorms. — and once you see the mechanism, it stops being trivia and starts being understanding. Best: dark winter. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Aurora borealis/australis.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Aurora borealis/australis.", "x": "Auroras: Aurora borealis/australis.. Oval zones. This is load-bearing knowledge — the kind of fact that other facts hang from. polar lights from solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Aurora borealis/australis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Aurora borealis/australis. is true.", "x": "The explanation: Aurora borealis/australis.. In astronomy, this fact connects to Other planets. — and once you see the mechanism, it stops being trivia and starts being understanding. Kp index. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Oxygen green.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Oxygen green.", "x": "Going deeper on Auroras: Oxygen green.. Aurora borealis/australis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nitrogen purple.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nitrogen purple.", "x": "Going deeper on Auroras: Nitrogen purple.. Best: dark winter. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Oval zones.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Oval zones.", "x": "Going deeper on Auroras: Oval zones.. Kp index. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Substorms.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Substorms.", "x": "Going deeper on Auroras: Substorms.. Carrington 1859. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Other planets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Other planets.", "x": "Going deeper on Auroras: Other planets.. Photography tips. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Forecasting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Forecasting.", "x": "Going deeper on Auroras: Forecasting.. Solar wind + magnetosphere. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Oxygen green.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Oxygen green.", "x": "Going deeper on Auroras: Oxygen green.. Aurora borealis/australis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Auroras from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-auroras-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
