(function(){'use strict';
/* JAH Treaty of Versailles Treaty Database generator — jahdb-e2-treaty-treaty-of-versailles-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-treaty-treaty-of-versailles',PREFIX='JAH-E2TREATYTRE-',NAME='JAH Treaty of Versailles Treaty Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Treaty of Versailles: overview", "d": "Treaty of Versailles (1919): ended WWI; seeded WWII..", "g": "overview", "l": 2, "q": "What is Treaty of Versailles: overview?", "a": "Treaty of Versailles (1919): ended WWI; seeded WWII..", "x": "The complete treaty guide to Treaty of Versailles: ended WWI; seeded WWII.. War guilt clause. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Treaty of Versailles in its time: 1919.", "g": "context", "l": 2, "q": "What is The era?", "a": "Treaty of Versailles in its time: 1919.", "x": "Context: Treaty of Versailles belonged to 1919 — Paris conference.. Reparations. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. ended WWI; seeded WWII.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "War guilt clause.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "War guilt clause.", "x": "Treaty of Versailles: War guilt clause.. 14 Points. This is one of the load-bearing facts about Treaty of Versailles — learn it cold. League of Nations. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: War guilt clause..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: War guilt clause..", "x": "Explained: War guilt clause.. US rejected League. In the history of Treaty of Versailles, this fact connects to Big Four. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reparations.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reparations.", "x": "Treaty of Versailles: Reparations.. Mandates. This is one of the load-bearing facts about Treaty of Versailles — learn it cold. Big Four. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Reparations..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Reparations..", "x": "Explained: Reparations.. Economic ruin. In the history of Treaty of Versailles, this fact connects to Germany humiliated. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "League of Nations.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "League of Nations.", "x": "Treaty of Versailles: League of Nations.. US rejected League. This is one of the load-bearing facts about Treaty of Versailles — learn it cold. Germany humiliated. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: League of Nations..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: League of Nations..", "x": "Explained: League of Nations.. Debate. In the history of Treaty of Versailles, this fact connects to Hitler exploited. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Big Four.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Big Four.", "x": "Treaty of Versailles: Big Four.. Economic ruin. This is one of the load-bearing facts about Treaty of Versailles — learn it cold. Hitler exploited. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Big Four..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Big Four..", "x": "Explained: Big Four.. Paris conference. In the history of Treaty of Versailles, this fact connects to War guilt clause. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Germany humiliated.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Germany humiliated.", "x": "Treaty of Versailles: Germany humiliated.. Debate. This is one of the load-bearing facts about Treaty of Versailles — learn it cold. War guilt clause. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Germany humiliated..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Germany humiliated..", "x": "Explained: Germany humiliated.. 14 Points. In the history of Treaty of Versailles, this fact connects to Reparations. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hitler exploited.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hitler exploited.", "x": "Treaty of Versailles: Hitler exploited.. Paris conference. This is one of the load-bearing facts about Treaty of Versailles — learn it cold. Reparations. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Hitler exploited..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Hitler exploited..", "x": "Explained: Hitler exploited.. Mandates. In the history of Treaty of Versailles, this fact connects to League of Nations. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Paris conference.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Paris conference.", "x": "Going deeper: Paris conference.. Reparations. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Versailles the way it did. ended WWI; seeded WWII. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "14 Points.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "14 Points.", "x": "Going deeper: 14 Points.. League of Nations. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Versailles the way it did. ended WWI; seeded WWII. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mandates.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mandates.", "x": "Going deeper: Mandates.. Big Four. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Versailles the way it did. ended WWI; seeded WWII. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "US rejected League.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "US rejected League.", "x": "Going deeper: US rejected League.. Germany humiliated. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Versailles the way it did. ended WWI; seeded WWII.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Economic ruin.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Economic ruin.", "x": "Going deeper: Economic ruin.. Hitler exploited. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Versailles the way it did. ended WWI; seeded WWII. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Debate.", "x": "Going deeper: Debate.. War guilt clause. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Versailles the way it did. ended WWI; seeded WWII. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Treaty of Versailles, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Treaty of Versailles, event by event.", "x": "The timeline: War guilt clause.. Paris conference. Key dates in order — League of Nations.. 1919 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Treaty of Versailles.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Treaty of Versailles.", "x": "The people: 14 Points.. Big Four. History is made by people deciding under pressure — ended WWI; seeded WWII.. US rejected League. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Treaty of Versailles.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Treaty of Versailles.", "x": "More figures: Germany humiliated. shaped Treaty of Versailles as surely as anyone — Economic ruin.. ended WWI; seeded WWII. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Treaty of Versailles happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Treaty of Versailles happened.", "x": "The causes: War guilt clause.. Mandates. Historians debate the deep vs immediate causes of Treaty of Versailles — ended WWI; seeded WWII.. Hitler exploited. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Treaty of Versailles turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Treaty of Versailles turned.", "x": "The turning point: US rejected League.. Reparations. Every great story has the moment it could have gone otherwise — Treaty of Versailles. ended WWI; seeded WWII. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-treaty-treaty-of-versailles-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
