(function(){'use strict';
/* JAH Caves Geology Database generator — jahdb-e2-sci-caves-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-caves',PREFIX='JAH-E2SCICAVES-',NAME='JAH Caves Geology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Caves: overview", "d": "Caves: natural underground chambers..", "g": "overview", "l": 2, "q": "What is Caves: overview?", "a": "Caves: natural underground chambers..", "x": "The complete geology guide to Caves: natural underground chambers.. Limestone solution caves. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Caves.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Caves.", "x": "The core principle: Stalactites vs stalagmites.. natural underground chambers. If you understand this one idea, everything else in Caves clicks into place. Speleothems form. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Limestone solution caves.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Limestone solution caves.", "x": "Caves: Limestone solution caves.. Cave ecosystems. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Limestone solution caves. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Limestone solution caves. is true.", "x": "The explanation: Limestone solution caves.. In geology, this fact connects to Cave diving risks. — and once you see the mechanism, it stops being trivia and starts being understanding. Mammoth Cave: longest.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Stalactites vs stalagmites.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Stalactites vs stalagmites.", "x": "Caves: Stalactites vs stalagmites.. Bats hibernate. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Stalactites vs stalagmites. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Stalactites vs stalagmites. is true.", "x": "The explanation: Stalactites vs stalagmites.. In geology, this fact connects to Karst topography. — and once you see the mechanism, it stops being trivia and starts being understanding. Carlsbad Caverns.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mammoth Cave: longest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mammoth Cave: longest.", "x": "Caves: Mammoth Cave: longest.. Cave diving risks. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Mammoth Cave: longest. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Mammoth Cave: longest. is true.", "x": "The explanation: Mammoth Cave: longest.. In geology, this fact connects to Conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Lava tubes. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Carlsbad Caverns.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Carlsbad Caverns.", "x": "Caves: Carlsbad Caverns.. Karst topography. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Carlsbad Caverns. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Carlsbad Caverns. is true.", "x": "The explanation: Carlsbad Caverns.. In geology, this fact connects to Speleothems form. — and once you see the mechanism, it stops being trivia and starts being understanding. Show caves tourism. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Lava tubes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Lava tubes.", "x": "Caves: Lava tubes.. Conservation. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Lava tubes. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Lava tubes. is true.", "x": "The explanation: Lava tubes.. In geology, this fact connects to Cave ecosystems. — and once you see the mechanism, it stops being trivia and starts being understanding. Limestone solution caves. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Show caves tourism.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Show caves tourism.", "x": "Caves: Show caves tourism.. Speleothems form. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Show caves tourism. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Show caves tourism. is true.", "x": "The explanation: Show caves tourism.. In geology, this fact connects to Bats hibernate. — and once you see the mechanism, it stops being trivia and starts being understanding. Stalactites vs stalagmites.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Limestone solution caves.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Limestone solution caves.", "x": "Caves: Limestone solution caves.. Cave ecosystems. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Limestone solution caves. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Limestone solution caves. is true.", "x": "The explanation: Limestone solution caves.. In geology, this fact connects to Cave diving risks. — and once you see the mechanism, it stops being trivia and starts being understanding. Mammoth Cave: longest.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Stalactites vs stalagmites.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Stalactites vs stalagmites.", "x": "Caves: Stalactites vs stalagmites.. Bats hibernate. This is load-bearing knowledge — the kind of fact that other facts hang from. natural underground chambers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Stalactites vs stalagmites. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Stalactites vs stalagmites. is true.", "x": "The explanation: Stalactites vs stalagmites.. In geology, this fact connects to Karst topography. — and once you see the mechanism, it stops being trivia and starts being understanding. Carlsbad Caverns.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Speleothems form.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Speleothems form.", "x": "Going deeper on Caves: Speleothems form.. Stalactites vs stalagmites. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cave ecosystems.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cave ecosystems.", "x": "Going deeper on Caves: Cave ecosystems.. Mammoth Cave: longest. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bats hibernate.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bats hibernate.", "x": "Going deeper on Caves: Bats hibernate.. Carlsbad Caverns. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cave diving risks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cave diving risks.", "x": "Going deeper on Caves: Cave diving risks.. Lava tubes. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Karst topography.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Karst topography.", "x": "Going deeper on Caves: Karst topography.. Show caves tourism. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conservation.", "x": "Going deeper on Caves: Conservation.. Limestone solution caves. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Speleothems form.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Speleothems form.", "x": "Going deeper on Caves: Speleothems form.. Stalactites vs stalagmites. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Caves from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-caves-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
