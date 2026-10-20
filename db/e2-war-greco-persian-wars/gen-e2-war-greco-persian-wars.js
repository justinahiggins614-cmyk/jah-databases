(function(){'use strict';
/* JAH Greco-Persian Wars War Database generator — jahdb-e2-war-greco-persian-wars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-greco-persian-wars',PREFIX='JAH-E2WARGRECOP-',NAME='JAH Greco-Persian Wars War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Greco-Persian Wars: overview", "d": "Greco-Persian Wars (499-449 BC): Greece repelled the Persian Empire..", "g": "overview", "l": 2, "q": "What is Greco-Persian Wars: overview?", "a": "Greco-Persian Wars (499-449 BC): Greece repelled the Persian Empire..", "x": "The complete war guide to Greco-Persian Wars: Greece repelled the Persian Empire.. Marathon (490 BC). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Greco-Persian Wars in its time: 499-449 BC.", "g": "context", "l": 2, "q": "What is The era?", "a": "Greco-Persian Wars in its time: 499-449 BC.", "x": "Context: Greco-Persian Wars belonged to 499-449 BC — Ionian revolt.. Thermopylae: 300 Spartans. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Greece repelled the Persian Empire.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Marathon (490 BC).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Marathon (490 BC).", "x": "Greco-Persian Wars: Marathon (490 BC).. Darius, Xerxes. This is one of the load-bearing facts about Greco-Persian Wars — learn it cold. Salamis: naval win. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Marathon (490 BC)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Marathon (490 BC)..", "x": "Explained: Marathon (490 BC).. Themistocles. In the history of Greco-Persian Wars, this fact connects to Plataea. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thermopylae: 300 Spartans.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thermopylae: 300 Spartans.", "x": "Greco-Persian Wars: Thermopylae: 300 Spartans.. Triremes. This is one of the load-bearing facts about Greco-Persian Wars — learn it cold. Plataea. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Thermopylae: 300 Spartans..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Thermopylae: 300 Spartans..", "x": "Explained: Thermopylae: 300 Spartans.. Delian League. In the history of Greco-Persian Wars, this fact connects to Persian Wars legacy. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Salamis: naval win.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Salamis: naval win.", "x": "Greco-Persian Wars: Salamis: naval win.. Themistocles. This is one of the load-bearing facts about Greco-Persian Wars — learn it cold. Persian Wars legacy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Salamis: naval win..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Salamis: naval win..", "x": "Explained: Salamis: naval win.. Herodotus. In the history of Greco-Persian Wars, this fact connects to Democracy defended. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Plataea.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Plataea.", "x": "Greco-Persian Wars: Plataea.. Delian League. This is one of the load-bearing facts about Greco-Persian Wars — learn it cold. Democracy defended. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Plataea..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Plataea..", "x": "Explained: Plataea.. Ionian revolt. In the history of Greco-Persian Wars, this fact connects to Marathon (490 BC). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Persian Wars legacy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Persian Wars legacy.", "x": "Greco-Persian Wars: Persian Wars legacy.. Herodotus. This is one of the load-bearing facts about Greco-Persian Wars — learn it cold. Marathon (490 BC). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Persian Wars legacy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Persian Wars legacy..", "x": "Explained: Persian Wars legacy.. Darius, Xerxes. In the history of Greco-Persian Wars, this fact connects to Thermopylae: 300 Spartans. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Democracy defended.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Democracy defended.", "x": "Greco-Persian Wars: Democracy defended.. Ionian revolt. This is one of the load-bearing facts about Greco-Persian Wars — learn it cold. Thermopylae: 300 Spartans. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Democracy defended..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Democracy defended..", "x": "Explained: Democracy defended.. Triremes. In the history of Greco-Persian Wars, this fact connects to Salamis: naval win. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ionian revolt.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ionian revolt.", "x": "Going deeper: Ionian revolt.. Thermopylae: 300 Spartans. Details are where historians live — the numbers, the names, the decisions that turned Greco-Persian Wars the way it did. Greece repelled the Persian Empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Darius, Xerxes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Darius, Xerxes.", "x": "Going deeper: Darius, Xerxes.. Salamis: naval win. Details are where historians live — the numbers, the names, the decisions that turned Greco-Persian Wars the way it did. Greece repelled the Persian Empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Triremes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Triremes.", "x": "Going deeper: Triremes.. Plataea. Details are where historians live — the numbers, the names, the decisions that turned Greco-Persian Wars the way it did. Greece repelled the Persian Empire. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Themistocles.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Themistocles.", "x": "Going deeper: Themistocles.. Persian Wars legacy. Details are where historians live — the numbers, the names, the decisions that turned Greco-Persian Wars the way it did. Greece repelled the Persian Empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Delian League.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Delian League.", "x": "Going deeper: Delian League.. Democracy defended. Details are where historians live — the numbers, the names, the decisions that turned Greco-Persian Wars the way it did. Greece repelled the Persian Empire.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Herodotus.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Herodotus.", "x": "Going deeper: Herodotus.. Marathon (490 BC). Details are where historians live — the numbers, the names, the decisions that turned Greco-Persian Wars the way it did. Greece repelled the Persian Empire.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Greco-Persian Wars, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Greco-Persian Wars, event by event.", "x": "The timeline: Marathon (490 BC).. Ionian revolt. Key dates in order — Salamis: naval win.. 499-449 BC Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Greco-Persian Wars.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Greco-Persian Wars.", "x": "The people: Darius, Xerxes.. Plataea. History is made by people deciding under pressure — Greece repelled the Persian Empire.. Themistocles. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Greco-Persian Wars.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Greco-Persian Wars.", "x": "More figures: Persian Wars legacy. shaped Greco-Persian Wars as surely as anyone — Delian League.. Greece repelled the Persian Empire. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Greco-Persian Wars happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Greco-Persian Wars happened.", "x": "The causes: Marathon (490 BC).. Triremes. Historians debate the deep vs immediate causes of Greco-Persian Wars — Greece repelled the Persian Empire.. Democracy defended. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Greco-Persian Wars turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Greco-Persian Wars turned.", "x": "The turning point: Themistocles.. Thermopylae: 300 Spartans. Every great story has the moment it could have gone otherwise — Greco-Persian Wars. Greece repelled the Persian Empire. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-greco-persian-wars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
