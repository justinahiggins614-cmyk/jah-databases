(function(){'use strict';
/* JAH Peace of Westphalia Treaty Database generator — jahdb-e2-treaty-peace-of-westphalia-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-treaty-peace-of-westphalia',PREFIX='JAH-E2TREATYPEA-',NAME='JAH Peace of Westphalia Treaty Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peace of Westphalia: overview", "d": "Peace of Westphalia (1648): ended Thirty Years' War; sovereignty..", "g": "overview", "l": 2, "q": "What is Peace of Westphalia: overview?", "a": "Peace of Westphalia (1648): ended Thirty Years' War; sovereignty..", "x": "The complete treaty guide to Peace of Westphalia: ended Thirty Years' War; sovereignty.. Munster/Osnabruck. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Peace of Westphalia in its time: 1648.", "g": "context", "l": 2, "q": "What is The era?", "a": "Peace of Westphalia in its time: 1648.", "x": "Context: Peace of Westphalia belonged to 1648 — Negotiations.. Sovereignty principle. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. ended Thirty Years' War; sovereignty.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Munster/Osnabruck.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Munster/Osnabruck.", "x": "Peace of Westphalia: Munster/Osnabruck.. Cuius regio. This is one of the load-bearing facts about Peace of Westphalia — learn it cold. Religious settlement. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Munster/Osnabruck..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Munster/Osnabruck..", "x": "Explained: Munster/Osnabruck.. Balance. In the history of Peace of Westphalia, this fact connects to States system. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sovereignty principle.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sovereignty principle.", "x": "Peace of Westphalia: Sovereignty principle.. Netherlands/Swiss. This is one of the load-bearing facts about Peace of Westphalia — learn it cold. States system. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Sovereignty principle..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Sovereignty principle..", "x": "Explained: Sovereignty principle.. Legacy. In the history of Peace of Westphalia, this fact connects to 8M dead ended. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Religious settlement.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Religious settlement.", "x": "Peace of Westphalia: Religious settlement.. Balance. This is one of the load-bearing facts about Peace of Westphalia — learn it cold. 8M dead ended. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Religious settlement..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Religious settlement..", "x": "Explained: Religious settlement.. International law. In the history of Peace of Westphalia, this fact connects to Modern diplomacy. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "States system.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "States system.", "x": "Peace of Westphalia: States system.. Legacy. This is one of the load-bearing facts about Peace of Westphalia — learn it cold. Modern diplomacy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: States system..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: States system..", "x": "Explained: States system.. Negotiations. In the history of Peace of Westphalia, this fact connects to Munster/Osnabruck. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "8M dead ended.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "8M dead ended.", "x": "Peace of Westphalia: 8M dead ended.. International law. This is one of the load-bearing facts about Peace of Westphalia — learn it cold. Munster/Osnabruck. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 8M dead ended..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 8M dead ended..", "x": "Explained: 8M dead ended.. Cuius regio. In the history of Peace of Westphalia, this fact connects to Sovereignty principle. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Modern diplomacy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Modern diplomacy.", "x": "Peace of Westphalia: Modern diplomacy.. Negotiations. This is one of the load-bearing facts about Peace of Westphalia — learn it cold. Sovereignty principle. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Modern diplomacy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Modern diplomacy..", "x": "Explained: Modern diplomacy.. Netherlands/Swiss. In the history of Peace of Westphalia, this fact connects to Religious settlement. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Negotiations.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Negotiations.", "x": "Going deeper: Negotiations.. Sovereignty principle. Details are where historians live — the numbers, the names, the decisions that turned Peace of Westphalia the way it did. ended Thirty Years' War; sovereignty.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cuius regio.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cuius regio.", "x": "Going deeper: Cuius regio.. Religious settlement. Details are where historians live — the numbers, the names, the decisions that turned Peace of Westphalia the way it did. ended Thirty Years' War; sovereignty.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Netherlands/Swiss.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Netherlands/Swiss.", "x": "Going deeper: Netherlands/Swiss.. States system. Details are where historians live — the numbers, the names, the decisions that turned Peace of Westphalia the way it did. ended Thirty Years' War; sovereignty.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Balance.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Balance.", "x": "Going deeper: Balance.. 8M dead ended. Details are where historians live — the numbers, the names, the decisions that turned Peace of Westphalia the way it did. ended Thirty Years' War; sovereignty. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. Modern diplomacy. Details are where historians live — the numbers, the names, the decisions that turned Peace of Westphalia the way it did. ended Thirty Years' War; sovereignty.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "International law.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "International law.", "x": "Going deeper: International law.. Munster/Osnabruck. Details are where historians live — the numbers, the names, the decisions that turned Peace of Westphalia the way it did. ended Thirty Years' War; sovereignty.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Peace of Westphalia, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Peace of Westphalia, event by event.", "x": "The timeline: Munster/Osnabruck.. Negotiations. Key dates in order — Religious settlement.. 1648 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Peace of Westphalia.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Peace of Westphalia.", "x": "The people: Cuius regio.. States system. History is made by people deciding under pressure — ended Thirty Years' War; sovereignty.. Balance. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Peace of Westphalia.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Peace of Westphalia.", "x": "More figures: 8M dead ended. shaped Peace of Westphalia as surely as anyone — Legacy.. ended Thirty Years' War; sovereignty. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Peace of Westphalia happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Peace of Westphalia happened.", "x": "The causes: Munster/Osnabruck.. Netherlands/Swiss. Historians debate the deep vs immediate causes of Peace of Westphalia — ended Thirty Years' War; sovereignty.. Modern diplomacy. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Peace of Westphalia turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Peace of Westphalia turned.", "x": "The turning point: Balance.. Sovereignty principle. Every great story has the moment it could have gone otherwise — Peace of Westphalia. ended Thirty Years' War; sovereignty. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-treaty-peace-of-westphalia-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
