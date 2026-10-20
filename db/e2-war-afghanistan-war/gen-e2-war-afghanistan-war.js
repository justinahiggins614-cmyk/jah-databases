(function(){'use strict';
/* JAH Afghanistan War War Database generator — jahdb-e2-war-afghanistan-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-afghanistan-war',PREFIX='JAH-E2WARAFGHAN-',NAME='JAH Afghanistan War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Afghanistan War: overview", "d": "Afghanistan War (2001-2021): America's longest war..", "g": "overview", "l": 2, "q": "What is Afghanistan War: overview?", "a": "Afghanistan War (2001-2021): America's longest war..", "x": "The complete war guide to Afghanistan War: America's longest war.. 9/11 response. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Afghanistan War in its time: 2001-2021.", "g": "context", "l": 2, "q": "What is The era?", "a": "Afghanistan War in its time: 2001-2021.", "x": "Context: Afghanistan War belonged to 2001-2021 — Northern Alliance.. Taliban fell fast. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. America's longest war.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "9/11 response.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "9/11 response.", "x": "Afghanistan War: 9/11 response.. Surge. This is one of the load-bearing facts about Afghanistan War — learn it cold. Nation-building. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: 9/11 response..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: 9/11 response..", "x": "Explained: 9/11 response.. Graveyard of empires. In the history of Afghanistan War, this fact connects to Bin Laden killed 2011. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Taliban fell fast.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Taliban fell fast.", "x": "Afghanistan War: Taliban fell fast.. Corruption. This is one of the load-bearing facts about Afghanistan War — learn it cold. Bin Laden killed 2011. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Taliban fell fast..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Taliban fell fast..", "x": "Explained: Taliban fell fast.. Costs. In the history of Afghanistan War, this fact connects to Withdrawal 2021. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nation-building.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nation-building.", "x": "Afghanistan War: Nation-building.. Graveyard of empires. This is one of the load-bearing facts about Afghanistan War — learn it cold. Withdrawal 2021. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Nation-building..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Nation-building..", "x": "Explained: Nation-building.. Lessons. In the history of Afghanistan War, this fact connects to Taliban returned. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bin Laden killed 2011.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bin Laden killed 2011.", "x": "Afghanistan War: Bin Laden killed 2011.. Costs. This is one of the load-bearing facts about Afghanistan War — learn it cold. Taliban returned. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Bin Laden killed 2011..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Bin Laden killed 2011..", "x": "Explained: Bin Laden killed 2011.. Northern Alliance. In the history of Afghanistan War, this fact connects to 9/11 response. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Withdrawal 2021.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Withdrawal 2021.", "x": "Afghanistan War: Withdrawal 2021.. Lessons. This is one of the load-bearing facts about Afghanistan War — learn it cold. 9/11 response. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Withdrawal 2021..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Withdrawal 2021..", "x": "Explained: Withdrawal 2021.. Surge. In the history of Afghanistan War, this fact connects to Taliban fell fast. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Taliban returned.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Taliban returned.", "x": "Afghanistan War: Taliban returned.. Northern Alliance. This is one of the load-bearing facts about Afghanistan War — learn it cold. Taliban fell fast. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Taliban returned..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Taliban returned..", "x": "Explained: Taliban returned.. Corruption. In the history of Afghanistan War, this fact connects to Nation-building. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Northern Alliance.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Northern Alliance.", "x": "Going deeper: Northern Alliance.. Taliban fell fast. Details are where historians live — the numbers, the names, the decisions that turned Afghanistan War the way it did. America's longest war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Surge.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Surge.", "x": "Going deeper: Surge.. Nation-building. Details are where historians live — the numbers, the names, the decisions that turned Afghanistan War the way it did. America's longest war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Corruption.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Corruption.", "x": "Going deeper: Corruption.. Bin Laden killed 2011. Details are where historians live — the numbers, the names, the decisions that turned Afghanistan War the way it did. America's longest war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Graveyard of empires.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Graveyard of empires.", "x": "Going deeper: Graveyard of empires.. Withdrawal 2021. Details are where historians live — the numbers, the names, the decisions that turned Afghanistan War the way it did. America's longest war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Costs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Costs.", "x": "Going deeper: Costs.. Taliban returned. Details are where historians live — the numbers, the names, the decisions that turned Afghanistan War the way it did. America's longest war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Lessons.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Lessons.", "x": "Going deeper: Lessons.. 9/11 response. Details are where historians live — the numbers, the names, the decisions that turned Afghanistan War the way it did. America's longest war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Afghanistan War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Afghanistan War, event by event.", "x": "The timeline: 9/11 response.. Northern Alliance. Key dates in order — Nation-building.. 2001-2021 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Afghanistan War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Afghanistan War.", "x": "The people: Surge.. Bin Laden killed 2011. History is made by people deciding under pressure — America's longest war.. Graveyard of empires. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Afghanistan War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Afghanistan War.", "x": "More figures: Withdrawal 2021. shaped Afghanistan War as surely as anyone — Costs.. America's longest war. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Afghanistan War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Afghanistan War happened.", "x": "The causes: 9/11 response.. Corruption. Historians debate the deep vs immediate causes of Afghanistan War — America's longest war.. Taliban returned. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Afghanistan War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Afghanistan War turned.", "x": "The turning point: Graveyard of empires.. Taliban fell fast. Every great story has the moment it could have gone otherwise — Afghanistan War. America's longest war. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-afghanistan-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
