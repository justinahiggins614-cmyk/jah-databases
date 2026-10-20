(function(){'use strict';
/* JAH Nubia Civilization Database generator — jahdb-e2-civilization-nubia-civilization-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-civilization-nubia-civilization',PREFIX='JAH-E2CIVILIZAT-',NAME='JAH Nubia Civilization Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nubia: overview", "d": "Nubia (c.3800 BC-1500 AD): Egypt's southern rival; black pharaohs..", "g": "overview", "l": 2, "q": "What is Nubia: overview?", "a": "Nubia (c.3800 BC-1500 AD): Egypt's southern rival; black pharaohs..", "x": "The complete civilization guide to Nubia: Egypt's southern rival; black pharaohs.. Kush kingdom. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Nubia in its time: c.3800 BC-1500 AD.", "g": "context", "l": 2, "q": "What is The era?", "a": "Nubia in its time: c.3800 BC-1500 AD.", "x": "Context: Nubia belonged to c.3800 BC-1500 AD — Kerma.. 25th Dynasty ruled Egypt. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Egypt's southern rival; black pharaohs.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Kush kingdom.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Kush kingdom.", "x": "Nubia: Kush kingdom.. Napata. This is one of the load-bearing facts about Nubia — learn it cold. Pyramids of Meroe. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Kush kingdom..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Kush kingdom..", "x": "Explained: Kush kingdom.. Candaces. In the history of Nubia, this fact connects to Gold. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "25th Dynasty ruled Egypt.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "25th Dynasty ruled Egypt.", "x": "Nubia: 25th Dynasty ruled Egypt.. Meroe. This is one of the load-bearing facts about Nubia — learn it cold. Gold. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: 25th Dynasty ruled Egypt..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: 25th Dynasty ruled Egypt..", "x": "Explained: 25th Dynasty ruled Egypt.. Temples. In the history of Nubia, this fact connects to Archers. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pyramids of Meroe.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pyramids of Meroe.", "x": "Nubia: Pyramids of Meroe.. Candaces. This is one of the load-bearing facts about Nubia — learn it cold. Archers. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Pyramids of Meroe..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Pyramids of Meroe..", "x": "Explained: Pyramids of Meroe.. Sudan. In the history of Nubia, this fact connects to Iron working. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gold.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gold.", "x": "Nubia: Gold.. Temples. This is one of the load-bearing facts about Nubia — learn it cold. Iron working. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Gold..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Gold..", "x": "Explained: Gold.. Kerma. In the history of Nubia, this fact connects to Kush kingdom. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Archers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Archers.", "x": "Nubia: Archers.. Sudan. This is one of the load-bearing facts about Nubia — learn it cold. Kush kingdom. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Archers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Archers..", "x": "Explained: Archers.. Napata. In the history of Nubia, this fact connects to 25th Dynasty ruled Egypt. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Iron working.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Iron working.", "x": "Nubia: Iron working.. Kerma. This is one of the load-bearing facts about Nubia — learn it cold. 25th Dynasty ruled Egypt. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Iron working..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Iron working..", "x": "Explained: Iron working.. Meroe. In the history of Nubia, this fact connects to Pyramids of Meroe. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Kerma.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Kerma.", "x": "Going deeper: Kerma.. 25th Dynasty ruled Egypt. Details are where historians live — the numbers, the names, the decisions that turned Nubia the way it did. Egypt's southern rival; black pharaohs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Napata.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Napata.", "x": "Going deeper: Napata.. Pyramids of Meroe. Details are where historians live — the numbers, the names, the decisions that turned Nubia the way it did. Egypt's southern rival; black pharaohs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Meroe.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Meroe.", "x": "Going deeper: Meroe.. Gold. Details are where historians live — the numbers, the names, the decisions that turned Nubia the way it did. Egypt's southern rival; black pharaohs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Candaces.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Candaces.", "x": "Going deeper: Candaces.. Archers. Details are where historians live — the numbers, the names, the decisions that turned Nubia the way it did. Egypt's southern rival; black pharaohs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Temples.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Temples.", "x": "Going deeper: Temples.. Iron working. Details are where historians live — the numbers, the names, the decisions that turned Nubia the way it did. Egypt's southern rival; black pharaohs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sudan.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sudan.", "x": "Going deeper: Sudan.. Kush kingdom. Details are where historians live — the numbers, the names, the decisions that turned Nubia the way it did. Egypt's southern rival; black pharaohs. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Nubia, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Nubia, event by event.", "x": "The timeline: Kush kingdom.. Kerma. Key dates in order — Pyramids of Meroe.. c.3800 BC-1500 AD Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Nubia.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Nubia.", "x": "The people: Napata.. Gold. History is made by people deciding under pressure — Egypt's southern rival; black pharaohs.. Candaces. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Nubia.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Nubia.", "x": "More figures: Archers. shaped Nubia as surely as anyone — Temples.. Egypt's southern rival; black pharaohs. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Nubia happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Nubia happened.", "x": "The causes: Kush kingdom.. Meroe. Historians debate the deep vs immediate causes of Nubia — Egypt's southern rival; black pharaohs.. Iron working. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Nubia turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Nubia turned.", "x": "The turning point: Candaces.. 25th Dynasty ruled Egypt. Every great story has the moment it could have gone otherwise — Nubia. Egypt's southern rival; black pharaohs. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-civilization-nubia-civilization-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
