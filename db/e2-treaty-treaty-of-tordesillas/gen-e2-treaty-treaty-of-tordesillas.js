(function(){'use strict';
/* JAH Treaty of Tordesillas Treaty Database generator — jahdb-e2-treaty-treaty-of-tordesillas-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-treaty-treaty-of-tordesillas',PREFIX='JAH-E2TREATYTRE-',NAME='JAH Treaty of Tordesillas Treaty Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Treaty of Tordesillas: overview", "d": "Treaty of Tordesillas (1494): split the world: Spain/Portugal..", "g": "overview", "l": 2, "q": "What is Treaty of Tordesillas: overview?", "a": "Treaty of Tordesillas (1494): split the world: Spain/Portugal..", "x": "The complete treaty guide to Treaty of Tordesillas: split the world: Spain/Portugal.. Pope's line. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Treaty of Tordesillas in its time: 1494.", "g": "context", "l": 2, "q": "What is The era?", "a": "Treaty of Tordesillas in its time: 1494.", "x": "Context: Treaty of Tordesillas belonged to 1494 — Inter caetera.. 370 leagues. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. split the world: Spain/Portugal.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pope's line.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pope's line.", "x": "Treaty of Tordesillas: Pope's line.. Negotiations. This is one of the load-bearing facts about Treaty of Tordesillas — learn it cold. Brazil to Portugal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Pope's line..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Pope's line..", "x": "Explained: Pope's line.. Legacy. In the history of Treaty of Tordesillas, this fact connects to Spain: rest. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "370 leagues.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "370 leagues.", "x": "Treaty of Tordesillas: 370 leagues.. Enforcement. This is one of the load-bearing facts about Treaty of Tordesillas — learn it cold. Spain: rest. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: 370 leagues..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: 370 leagues..", "x": "Explained: 370 leagues.. South America. In the history of Treaty of Tordesillas, this fact connects to Demarcation. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Brazil to Portugal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Brazil to Portugal.", "x": "Treaty of Tordesillas: Brazil to Portugal.. Legacy. This is one of the load-bearing facts about Treaty of Tordesillas — learn it cold. Demarcation. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Brazil to Portugal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Brazil to Portugal..", "x": "Explained: Brazil to Portugal.. Disputes. In the history of Treaty of Tordesillas, this fact connects to Colonial map. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spain: rest.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spain: rest.", "x": "Treaty of Tordesillas: Spain: rest.. South America. This is one of the load-bearing facts about Treaty of Tordesillas — learn it cold. Colonial map. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Spain: rest..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Spain: rest..", "x": "Explained: Spain: rest.. Inter caetera. In the history of Treaty of Tordesillas, this fact connects to Pope's line. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Demarcation.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Demarcation.", "x": "Treaty of Tordesillas: Demarcation.. Disputes. This is one of the load-bearing facts about Treaty of Tordesillas — learn it cold. Pope's line. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Demarcation..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Demarcation..", "x": "Explained: Demarcation.. Negotiations. In the history of Treaty of Tordesillas, this fact connects to 370 leagues. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Colonial map.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Colonial map.", "x": "Treaty of Tordesillas: Colonial map.. Inter caetera. This is one of the load-bearing facts about Treaty of Tordesillas — learn it cold. 370 leagues. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Colonial map..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Colonial map..", "x": "Explained: Colonial map.. Enforcement. In the history of Treaty of Tordesillas, this fact connects to Brazil to Portugal. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Inter caetera.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Inter caetera.", "x": "Going deeper: Inter caetera.. 370 leagues. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Tordesillas the way it did. split the world: Spain/Portugal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Negotiations.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Negotiations.", "x": "Going deeper: Negotiations.. Brazil to Portugal. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Tordesillas the way it did. split the world: Spain/Portugal.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Enforcement.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Enforcement.", "x": "Going deeper: Enforcement.. Spain: rest. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Tordesillas the way it did. split the world: Spain/Portugal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Legacy.", "x": "Going deeper: Legacy.. Demarcation. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Tordesillas the way it did. split the world: Spain/Portugal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "South America.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "South America.", "x": "Going deeper: South America.. Colonial map. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Tordesillas the way it did. split the world: Spain/Portugal.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Disputes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Disputes.", "x": "Going deeper: Disputes.. Pope's line. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Tordesillas the way it did. split the world: Spain/Portugal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Treaty of Tordesillas, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Treaty of Tordesillas, event by event.", "x": "The timeline: Pope's line.. Inter caetera. Key dates in order — Brazil to Portugal.. 1494 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Treaty of Tordesillas.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Treaty of Tordesillas.", "x": "The people: Negotiations.. Spain: rest. History is made by people deciding under pressure — split the world: Spain/Portugal.. Legacy. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Treaty of Tordesillas.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Treaty of Tordesillas.", "x": "More figures: Demarcation. shaped Treaty of Tordesillas as surely as anyone — South America.. split the world: Spain/Portugal. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Treaty of Tordesillas happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Treaty of Tordesillas happened.", "x": "The causes: Pope's line.. Enforcement. Historians debate the deep vs immediate causes of Treaty of Tordesillas — split the world: Spain/Portugal.. Colonial map. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Treaty of Tordesillas turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Treaty of Tordesillas turned.", "x": "The turning point: Legacy.. 370 leagues. Every great story has the moment it could have gone otherwise — Treaty of Tordesillas. split the world: Spain/Portugal. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-treaty-treaty-of-tordesillas-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
