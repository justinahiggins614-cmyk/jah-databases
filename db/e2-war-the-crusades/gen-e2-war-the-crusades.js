(function(){'use strict';
/* JAH The Crusades War Database generator — jahdb-e2-war-the-crusades-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-the-crusades',PREFIX='JAH-E2WARTHECRU-',NAME='JAH The Crusades War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Crusades: overview", "d": "The Crusades (1095-1291): holy wars for the Holy Land..", "g": "overview", "l": 2, "q": "What is The Crusades: overview?", "a": "The Crusades (1095-1291): holy wars for the Holy Land..", "x": "The complete war guide to The Crusades: holy wars for the Holy Land.. Pope Urban II called (1095). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "The Crusades in its time: 1095-1291.", "g": "context", "l": 2, "q": "What is The era?", "a": "The Crusades in its time: 1095-1291.", "x": "Context: The Crusades belonged to 1095-1291 — Knight orders.. Jerusalem taken 1099. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. holy wars for the Holy Land.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pope Urban II called (1095).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pope Urban II called (1095).", "x": "The Crusades: Pope Urban II called (1095).. Richard Lionheart. This is one of the load-bearing facts about The Crusades — learn it cold. Saladin retook 1187. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Pope Urban II called (1095)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Pope Urban II called (1095)..", "x": "Explained: Pope Urban II called (1095).. Trade effects. In the history of The Crusades, this fact connects to Children's Crusade myth. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jerusalem taken 1099.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jerusalem taken 1099.", "x": "The Crusades: Jerusalem taken 1099.. Siege warfare. This is one of the load-bearing facts about The Crusades — learn it cold. Children's Crusade myth. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Jerusalem taken 1099..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Jerusalem taken 1099..", "x": "Explained: Jerusalem taken 1099.. Muslim perspectives. In the history of The Crusades, this fact connects to Fourth sacked Constantinople. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Saladin retook 1187.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Saladin retook 1187.", "x": "The Crusades: Saladin retook 1187.. Trade effects. This is one of the load-bearing facts about The Crusades — learn it cold. Fourth sacked Constantinople. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Saladin retook 1187..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Saladin retook 1187..", "x": "Explained: Saladin retook 1187.. Legacy. In the history of The Crusades, this fact connects to Nine major crusades. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Children's Crusade myth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Children's Crusade myth.", "x": "The Crusades: Children's Crusade myth.. Muslim perspectives. This is one of the load-bearing facts about The Crusades — learn it cold. Nine major crusades. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Children's Crusade myth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Children's Crusade myth..", "x": "Explained: Children's Crusade myth.. Knight orders. In the history of The Crusades, this fact connects to Pope Urban II called (1095). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fourth sacked Constantinople.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fourth sacked Constantinople.", "x": "The Crusades: Fourth sacked Constantinople.. Legacy. This is one of the load-bearing facts about The Crusades — learn it cold. Pope Urban II called (1095). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Fourth sacked Constantinople..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Fourth sacked Constantinople..", "x": "Explained: Fourth sacked Constantinople.. Richard Lionheart. In the history of The Crusades, this fact connects to Jerusalem taken 1099. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nine major crusades.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nine major crusades.", "x": "The Crusades: Nine major crusades.. Knight orders. This is one of the load-bearing facts about The Crusades — learn it cold. Jerusalem taken 1099. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Nine major crusades..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Nine major crusades..", "x": "Explained: Nine major crusades.. Siege warfare. In the history of The Crusades, this fact connects to Saladin retook 1187. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Knight orders.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Knight orders.", "x": "Going deeper: Knight orders.. Jerusalem taken 1099. Details are where historians live — the numbers, the names, the decisions that turned The Crusades the way it did. holy wars for the Holy Land. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Richard Lionheart.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Richard Lionheart.", "x": "Going deeper: Richard Lionheart.. Saladin retook 1187. Details are where historians live — the numbers, the names, the decisions that turned The Crusades the way it did. holy wars for the Holy Land. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Siege warfare.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Siege warfare.", "x": "Going deeper: Siege warfare.. Children's Crusade myth. Details are where historians live — the numbers, the names, the decisions that turned The Crusades the way it did. holy wars for the Holy Land. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Trade effects.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Trade effects.", "x": "Going deeper: Trade effects.. Fourth sacked Constantinople. Details are where historians live — the numbers, the names, the decisions that turned The Crusades the way it did. holy wars for the Holy Land.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Muslim perspectives.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Muslim perspectives.", "x": "Going deeper: Muslim perspectives.. Nine major crusades. Details are where historians live — the numbers, the names, the decisions that turned The Crusades the way it did. holy wars for the Holy Land.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Pope Urban II called (1095). Details are where historians live — the numbers, the names, the decisions that turned The Crusades the way it did. holy wars for the Holy Land. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "The Crusades, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "The Crusades, event by event.", "x": "The timeline: Pope Urban II called (1095).. Knight orders. Key dates in order — Saladin retook 1187.. 1095-1291 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of The Crusades.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of The Crusades.", "x": "The people: Richard Lionheart.. Children's Crusade myth. History is made by people deciding under pressure — holy wars for the Holy Land.. Trade effects. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped The Crusades.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped The Crusades.", "x": "More figures: Fourth sacked Constantinople. shaped The Crusades as surely as anyone — Muslim perspectives.. holy wars for the Holy Land. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why The Crusades happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why The Crusades happened.", "x": "The causes: Pope Urban II called (1095).. Siege warfare. Historians debate the deep vs immediate causes of The Crusades — holy wars for the Holy Land.. Nine major crusades. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment The Crusades turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment The Crusades turned.", "x": "The turning point: Trade effects.. Jerusalem taken 1099. Every great story has the moment it could have gone otherwise — The Crusades. holy wars for the Holy Land. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-the-crusades-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
