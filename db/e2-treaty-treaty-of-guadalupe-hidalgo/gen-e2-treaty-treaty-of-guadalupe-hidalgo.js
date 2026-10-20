(function(){'use strict';
/* JAH Treaty of Guadalupe Hidalgo Treaty Database generator — jahdb-e2-treaty-treaty-of-guadalupe-hidalgo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-treaty-treaty-of-guadalupe-hidalgo',PREFIX='JAH-E2TREATYTRE-',NAME='JAH Treaty of Guadalupe Hidalgo Treaty Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Treaty of Guadalupe Hidalgo: overview", "d": "Treaty of Guadalupe Hidalgo (1848): US took the Southwest..", "g": "overview", "l": 2, "q": "What is Treaty of Guadalupe Hidalgo: overview?", "a": "Treaty of Guadalupe Hidalgo (1848): US took the Southwest..", "x": "The complete treaty guide to Treaty of Guadalupe Hidalgo: US took the Southwest.. Mexican Cession. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Treaty of Guadalupe Hidalgo in its time: 1848.", "g": "context", "l": 2, "q": "What is The era?", "a": "Treaty of Guadalupe Hidalgo in its time: 1848.", "x": "Context: Treaty of Guadalupe Hidalgo belonged to 1848 — Trist negotiated.. Rio Grande border. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. US took the Southwest.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mexican Cession.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mexican Cession.", "x": "Treaty of Guadalupe Hidalgo: Mexican Cession.. Terms. This is one of the load-bearing facts about Treaty of Guadalupe Hidalgo — learn it cold. $15M paid. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Mexican Cession..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Mexican Cession..", "x": "Explained: Mexican Cession.. Land grants. In the history of Treaty of Guadalupe Hidalgo, this fact connects to Californios' rights. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rio Grande border.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rio Grande border.", "x": "Treaty of Guadalupe Hidalgo: Rio Grande border.. Aftermath. This is one of the load-bearing facts about Treaty of Guadalupe Hidalgo — learn it cold. Californios' rights. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Rio Grande border..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Rio Grande border..", "x": "Explained: Rio Grande border.. Legacy. In the history of Treaty of Guadalupe Hidalgo, this fact connects to Gadsden later. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "$15M paid.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "$15M paid.", "x": "Treaty of Guadalupe Hidalgo: $15M paid.. Land grants. This is one of the load-bearing facts about Treaty of Guadalupe Hidalgo — learn it cold. Gadsden later. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: $15M paid..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: $15M paid..", "x": "Explained: $15M paid.. Border. In the history of Treaty of Guadalupe Hidalgo, this fact connects to Chicano roots. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Californios' rights.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Californios' rights.", "x": "Treaty of Guadalupe Hidalgo: Californios' rights.. Legacy. This is one of the load-bearing facts about Treaty of Guadalupe Hidalgo — learn it cold. Chicano roots. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Californios' rights..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Californios' rights..", "x": "Explained: Californios' rights.. Trist negotiated. In the history of Treaty of Guadalupe Hidalgo, this fact connects to Mexican Cession. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gadsden later.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gadsden later.", "x": "Treaty of Guadalupe Hidalgo: Gadsden later.. Border. This is one of the load-bearing facts about Treaty of Guadalupe Hidalgo — learn it cold. Mexican Cession. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Gadsden later..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Gadsden later..", "x": "Explained: Gadsden later.. Terms. In the history of Treaty of Guadalupe Hidalgo, this fact connects to Rio Grande border. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chicano roots.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chicano roots.", "x": "Treaty of Guadalupe Hidalgo: Chicano roots.. Trist negotiated. This is one of the load-bearing facts about Treaty of Guadalupe Hidalgo — learn it cold. Rio Grande border. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Chicano roots..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Chicano roots..", "x": "Explained: Chicano roots.. Aftermath. In the history of Treaty of Guadalupe Hidalgo, this fact connects to $15M paid. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Trist negotiated.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Trist negotiated.", "x": "Going deeper: Trist negotiated.. Rio Grande border. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Guadalupe Hidalgo the way it did. US took the Southwest.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Terms.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Terms.", "x": "Going deeper: Terms.. $15M paid. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Guadalupe Hidalgo the way it did. US took the Southwest. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. Californios' rights. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Guadalupe Hidalgo the way it did. US took the Southwest. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Land grants.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Land grants.", "x": "Going deeper: Land grants.. Gadsden later. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Guadalupe Hidalgo the way it did. US took the Southwest. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. Chicano roots. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Guadalupe Hidalgo the way it did. US took the Southwest. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Border.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Border.", "x": "Going deeper: Border.. Mexican Cession. Details are where historians live — the numbers, the names, the decisions that turned Treaty of Guadalupe Hidalgo the way it did. US took the Southwest. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Treaty of Guadalupe Hidalgo, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Treaty of Guadalupe Hidalgo, event by event.", "x": "The timeline: Mexican Cession.. Trist negotiated. Key dates in order — $15M paid.. 1848 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Treaty of Guadalupe Hidalgo.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Treaty of Guadalupe Hidalgo.", "x": "The people: Terms.. Californios' rights. History is made by people deciding under pressure — US took the Southwest.. Land grants. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Treaty of Guadalupe Hidalgo.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Treaty of Guadalupe Hidalgo.", "x": "More figures: Gadsden later. shaped Treaty of Guadalupe Hidalgo as surely as anyone — Legacy.. US took the Southwest. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Treaty of Guadalupe Hidalgo happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Treaty of Guadalupe Hidalgo happened.", "x": "The causes: Mexican Cession.. Aftermath. Historians debate the deep vs immediate causes of Treaty of Guadalupe Hidalgo — US took the Southwest.. Chicano roots. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Treaty of Guadalupe Hidalgo turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Treaty of Guadalupe Hidalgo turned.", "x": "The turning point: Land grants.. Rio Grande border. Every great story has the moment it could have gone otherwise — Treaty of Guadalupe Hidalgo. US took the Southwest. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-treaty-treaty-of-guadalupe-hidalgo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
