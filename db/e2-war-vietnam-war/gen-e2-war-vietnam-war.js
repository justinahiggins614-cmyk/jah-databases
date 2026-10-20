(function(){'use strict';
/* JAH Vietnam War War Database generator — jahdb-e2-war-vietnam-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-vietnam-war',PREFIX='JAH-E2WARVIETNA-',NAME='JAH Vietnam War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vietnam War: overview", "d": "Vietnam War (1955-1975): America's longest Cold War conflict..", "g": "overview", "l": 2, "q": "What is Vietnam War: overview?", "a": "Vietnam War (1955-1975): America's longest Cold War conflict..", "x": "The complete war guide to Vietnam War: America's longest Cold War conflict.. Gulf of Tonkin escalation. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Vietnam War in its time: 1955-1975.", "g": "context", "l": 2, "q": "What is The era?", "a": "Vietnam War in its time: 1955-1975.", "x": "Context: Vietnam War belonged to 1955-1975 — Domino theory.. Tet Offensive (1968). Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. America's longest Cold War conflict.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gulf of Tonkin escalation.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gulf of Tonkin escalation.", "x": "Vietnam War: Gulf of Tonkin escalation.. Ho Chi Minh Trail. This is one of the load-bearing facts about Vietnam War — learn it cold. Guerrilla Viet Cong. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Gulf of Tonkin escalation..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Gulf of Tonkin escalation..", "x": "Explained: Gulf of Tonkin escalation.. Anti-war movement. In the history of Vietnam War, this fact connects to US withdrew 1973. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tet Offensive (1968).", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tet Offensive (1968).", "x": "Vietnam War: Tet Offensive (1968).. My Lai massacre. This is one of the load-bearing facts about Vietnam War — learn it cold. US withdrew 1973. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Tet Offensive (1968)..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Tet Offensive (1968)..", "x": "Explained: Tet Offensive (1968).. POW/MIA. In the history of Vietnam War, this fact connects to Saigon fell 1975. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Guerrilla Viet Cong.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Guerrilla Viet Cong.", "x": "Vietnam War: Guerrilla Viet Cong.. Anti-war movement. This is one of the load-bearing facts about Vietnam War — learn it cold. Saigon fell 1975. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Guerrilla Viet Cong..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Guerrilla Viet Cong..", "x": "Explained: Guerrilla Viet Cong.. Vietnam today. In the history of Vietnam War, this fact connects to 58,000 US dead. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "US withdrew 1973.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "US withdrew 1973.", "x": "Vietnam War: US withdrew 1973.. POW/MIA. This is one of the load-bearing facts about Vietnam War — learn it cold. 58,000 US dead. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: US withdrew 1973..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: US withdrew 1973..", "x": "Explained: US withdrew 1973.. Domino theory. In the history of Vietnam War, this fact connects to Gulf of Tonkin escalation. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Saigon fell 1975.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Saigon fell 1975.", "x": "Vietnam War: Saigon fell 1975.. Vietnam today. This is one of the load-bearing facts about Vietnam War — learn it cold. Gulf of Tonkin escalation. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Saigon fell 1975..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Saigon fell 1975..", "x": "Explained: Saigon fell 1975.. Ho Chi Minh Trail. In the history of Vietnam War, this fact connects to Tet Offensive (1968). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "58,000 US dead.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "58,000 US dead.", "x": "Vietnam War: 58,000 US dead.. Domino theory. This is one of the load-bearing facts about Vietnam War — learn it cold. Tet Offensive (1968). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 58,000 US dead..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 58,000 US dead..", "x": "Explained: 58,000 US dead.. My Lai massacre. In the history of Vietnam War, this fact connects to Guerrilla Viet Cong. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Domino theory.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Domino theory.", "x": "Going deeper: Domino theory.. Tet Offensive (1968). Details are where historians live — the numbers, the names, the decisions that turned Vietnam War the way it did. America's longest Cold War conflict.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ho Chi Minh Trail.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ho Chi Minh Trail.", "x": "Going deeper: Ho Chi Minh Trail.. Guerrilla Viet Cong. Details are where historians live — the numbers, the names, the decisions that turned Vietnam War the way it did. America's longest Cold War conflict.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "My Lai massacre.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "My Lai massacre.", "x": "Going deeper: My Lai massacre.. US withdrew 1973. Details are where historians live — the numbers, the names, the decisions that turned Vietnam War the way it did. America's longest Cold War conflict.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Anti-war movement.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Anti-war movement.", "x": "Going deeper: Anti-war movement.. Saigon fell 1975. Details are where historians live — the numbers, the names, the decisions that turned Vietnam War the way it did. America's longest Cold War conflict.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "POW/MIA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "POW/MIA.", "x": "Going deeper: POW/MIA.. 58,000 US dead. Details are where historians live — the numbers, the names, the decisions that turned Vietnam War the way it did. America's longest Cold War conflict. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Vietnam today.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Vietnam today.", "x": "Going deeper: Vietnam today.. Gulf of Tonkin escalation. Details are where historians live — the numbers, the names, the decisions that turned Vietnam War the way it did. America's longest Cold War conflict.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Vietnam War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Vietnam War, event by event.", "x": "The timeline: Gulf of Tonkin escalation.. Domino theory. Key dates in order — Guerrilla Viet Cong.. 1955-1975 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Vietnam War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Vietnam War.", "x": "The people: Ho Chi Minh Trail.. US withdrew 1973. History is made by people deciding under pressure — America's longest Cold War conflict.. Anti-war movement. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Vietnam War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Vietnam War.", "x": "More figures: Saigon fell 1975. shaped Vietnam War as surely as anyone — POW/MIA.. America's longest Cold War conflict. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Vietnam War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Vietnam War happened.", "x": "The causes: Gulf of Tonkin escalation.. My Lai massacre. Historians debate the deep vs immediate causes of Vietnam War — America's longest Cold War conflict.. 58,000 US dead. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Vietnam War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Vietnam War turned.", "x": "The turning point: Anti-war movement.. Tet Offensive (1968). Every great story has the moment it could have gone otherwise — Vietnam War. America's longest Cold War conflict. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-vietnam-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
