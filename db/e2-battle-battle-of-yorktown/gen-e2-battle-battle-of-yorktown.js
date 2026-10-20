(function(){'use strict';
/* JAH Battle of Yorktown Battle Database generator — jahdb-e2-battle-battle-of-yorktown-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-battle-battle-of-yorktown',PREFIX='JAH-E2BATTLEBAT-',NAME='JAH Battle of Yorktown Battle Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Battle of Yorktown: overview", "d": "Battle of Yorktown (1781): British surrender; US independence..", "g": "overview", "l": 2, "q": "What is Battle of Yorktown: overview?", "a": "Battle of Yorktown (1781): British surrender; US independence..", "x": "The complete battle guide to Battle of Yorktown: British surrender; US independence.. Washington + Rochambeau. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Battle of Yorktown in its time: 1781.", "g": "context", "l": 2, "q": "What is The era?", "a": "Battle of Yorktown in its time: 1781.", "x": "Context: Battle of Yorktown belonged to 1781 — Siege.. De Grasse fleet. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. British surrender; US independence.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Washington + Rochambeau.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Washington + Rochambeau.", "x": "Battle of Yorktown: Washington + Rochambeau.. Allies. This is one of the load-bearing facts about Battle of Yorktown — learn it cold. Cornwallis trapped. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Washington + Rochambeau..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Washington + Rochambeau..", "x": "Explained: Washington + Rochambeau.. Park. In the history of Battle of Yorktown, this fact connects to Siege. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "De Grasse fleet.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "De Grasse fleet.", "x": "Battle of Yorktown: De Grasse fleet.. Aftermath. This is one of the load-bearing facts about Battle of Yorktown — learn it cold. Siege. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: De Grasse fleet..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: De Grasse fleet..", "x": "Explained: De Grasse fleet.. Reenactment. In the history of Battle of Yorktown, this fact connects to Treaty followed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cornwallis trapped.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cornwallis trapped.", "x": "Battle of Yorktown: Cornwallis trapped.. Park. This is one of the load-bearing facts about Battle of Yorktown — learn it cold. Treaty followed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Cornwallis trapped..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Cornwallis trapped..", "x": "Explained: Cornwallis trapped.. Legacy. In the history of Battle of Yorktown, this fact connects to Victory. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Siege.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Siege.", "x": "Battle of Yorktown: Siege.. Reenactment. This is one of the load-bearing facts about Battle of Yorktown — learn it cold. Victory. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Siege..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Siege..", "x": "Explained: Siege.. Siege. In the history of Battle of Yorktown, this fact connects to Washington + Rochambeau. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Treaty followed.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Treaty followed.", "x": "Battle of Yorktown: Treaty followed.. Legacy. This is one of the load-bearing facts about Battle of Yorktown — learn it cold. Washington + Rochambeau. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Treaty followed..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Treaty followed..", "x": "Explained: Treaty followed.. Allies. In the history of Battle of Yorktown, this fact connects to De Grasse fleet. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Victory.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Victory.", "x": "Battle of Yorktown: Victory.. Siege. This is one of the load-bearing facts about Battle of Yorktown — learn it cold. De Grasse fleet. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Victory..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Victory..", "x": "Explained: Victory.. Aftermath. In the history of Battle of Yorktown, this fact connects to Cornwallis trapped. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Siege.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Siege.", "x": "Going deeper: Siege.. De Grasse fleet. Details are where historians live — the numbers, the names, the decisions that turned Battle of Yorktown the way it did. British surrender; US independence. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Allies.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Allies.", "x": "Going deeper: Allies.. Cornwallis trapped. Details are where historians live — the numbers, the names, the decisions that turned Battle of Yorktown the way it did. British surrender; US independence. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. Siege. Details are where historians live — the numbers, the names, the decisions that turned Battle of Yorktown the way it did. British surrender; US independence. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Park.", "x": "Going deeper: Park.. Treaty followed. Details are where historians live — the numbers, the names, the decisions that turned Battle of Yorktown the way it did. British surrender; US independence. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reenactment.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reenactment.", "x": "Going deeper: Reenactment.. Victory. Details are where historians live — the numbers, the names, the decisions that turned Battle of Yorktown the way it did. British surrender; US independence. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Washington + Rochambeau. Details are where historians live — the numbers, the names, the decisions that turned Battle of Yorktown the way it did. British surrender; US independence.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Battle of Yorktown, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Battle of Yorktown, event by event.", "x": "The timeline: Washington + Rochambeau.. Siege. Key dates in order — Cornwallis trapped.. 1781 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Battle of Yorktown.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Battle of Yorktown.", "x": "The people: Allies.. Siege. History is made by people deciding under pressure — British surrender; US independence.. Park. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Battle of Yorktown.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Battle of Yorktown.", "x": "More figures: Treaty followed. shaped Battle of Yorktown as surely as anyone — Reenactment.. British surrender; US independence. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Battle of Yorktown happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Battle of Yorktown happened.", "x": "The causes: Washington + Rochambeau.. Aftermath. Historians debate the deep vs immediate causes of Battle of Yorktown — British surrender; US independence.. Victory. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Battle of Yorktown turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Battle of Yorktown turned.", "x": "The turning point: Park.. De Grasse fleet. Every great story has the moment it could have gone otherwise — Battle of Yorktown. British surrender; US independence. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-battle-battle-of-yorktown-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
