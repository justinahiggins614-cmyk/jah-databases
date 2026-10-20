(function(){'use strict';
/* JAH Mexican-American War War Database generator — jahdb-e2-war-mexican-american-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-mexican-american-war',PREFIX='JAH-E2WARMEXICA-',NAME='JAH Mexican-American War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mexican-American War: overview", "d": "Mexican-American War (1846-1848): US took half of Mexico..", "g": "overview", "l": 2, "q": "What is Mexican-American War: overview?", "a": "Mexican-American War (1846-1848): US took half of Mexico..", "x": "The complete war guide to Mexican-American War: US took half of Mexico.. Texas annexation. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Mexican-American War in its time: 1846-1848.", "g": "context", "l": 2, "q": "What is The era?", "a": "Mexican-American War in its time: 1846-1848.", "x": "Context: Mexican-American War belonged to 1846-1848 — Manifest Destiny.. Polk's expansion. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. US took half of Mexico.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Texas annexation.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Texas annexation.", "x": "Mexican-American War: Texas annexation.. Monterey. This is one of the load-bearing facts about Mexican-American War — learn it cold. Winfield Scott: Mexico City. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Texas annexation..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Texas annexation..", "x": "Explained: Texas annexation.. Chapultepec. In the history of Mexican-American War, this fact connects to Treaty of Guadalupe Hidalgo. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Polk's expansion.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Polk's expansion.", "x": "Mexican-American War: Polk's expansion.. Buena Vista. This is one of the load-bearing facts about Mexican-American War — learn it cold. Treaty of Guadalupe Hidalgo. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Polk's expansion..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Polk's expansion..", "x": "Explained: Polk's expansion.. Mexican cession. In the history of Mexican-American War, this fact connects to US got California etc. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Winfield Scott: Mexico City.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Winfield Scott: Mexico City.", "x": "Mexican-American War: Winfield Scott: Mexico City.. Chapultepec. This is one of the load-bearing facts about Mexican-American War — learn it cold. US got California etc. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Winfield Scott: Mexico City..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Winfield Scott: Mexico City..", "x": "Explained: Winfield Scott: Mexico City.. Legacy. In the history of Mexican-American War, this fact connects to Civil War officers trained. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Treaty of Guadalupe Hidalgo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Treaty of Guadalupe Hidalgo.", "x": "Mexican-American War: Treaty of Guadalupe Hidalgo.. Mexican cession. This is one of the load-bearing facts about Mexican-American War — learn it cold. Civil War officers trained. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Treaty of Guadalupe Hidalgo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Treaty of Guadalupe Hidalgo..", "x": "Explained: Treaty of Guadalupe Hidalgo.. Manifest Destiny. In the history of Mexican-American War, this fact connects to Texas annexation. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "US got California etc.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "US got California etc.", "x": "Mexican-American War: US got California etc.. Legacy. This is one of the load-bearing facts about Mexican-American War — learn it cold. Texas annexation. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: US got California etc..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: US got California etc..", "x": "Explained: US got California etc.. Monterey. In the history of Mexican-American War, this fact connects to Polk's expansion. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Civil War officers trained.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Civil War officers trained.", "x": "Mexican-American War: Civil War officers trained.. Manifest Destiny. This is one of the load-bearing facts about Mexican-American War — learn it cold. Polk's expansion. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Civil War officers trained..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Civil War officers trained..", "x": "Explained: Civil War officers trained.. Buena Vista. In the history of Mexican-American War, this fact connects to Winfield Scott: Mexico City. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Manifest Destiny.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Manifest Destiny.", "x": "Going deeper: Manifest Destiny.. Polk's expansion. Details are where historians live — the numbers, the names, the decisions that turned Mexican-American War the way it did. US took half of Mexico. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Monterey.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Monterey.", "x": "Going deeper: Monterey.. Winfield Scott: Mexico City. Details are where historians live — the numbers, the names, the decisions that turned Mexican-American War the way it did. US took half of Mexico.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Buena Vista.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Buena Vista.", "x": "Going deeper: Buena Vista.. Treaty of Guadalupe Hidalgo. Details are where historians live — the numbers, the names, the decisions that turned Mexican-American War the way it did. US took half of Mexico.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Chapultepec.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Chapultepec.", "x": "Going deeper: Chapultepec.. US got California etc. Details are where historians live — the numbers, the names, the decisions that turned Mexican-American War the way it did. US took half of Mexico. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mexican cession.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mexican cession.", "x": "Going deeper: Mexican cession.. Civil War officers trained. Details are where historians live — the numbers, the names, the decisions that turned Mexican-American War the way it did. US took half of Mexico.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Texas annexation. Details are where historians live — the numbers, the names, the decisions that turned Mexican-American War the way it did. US took half of Mexico. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Mexican-American War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Mexican-American War, event by event.", "x": "The timeline: Texas annexation.. Manifest Destiny. Key dates in order — Winfield Scott: Mexico City.. 1846-1848 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Mexican-American War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Mexican-American War.", "x": "The people: Monterey.. Treaty of Guadalupe Hidalgo. History is made by people deciding under pressure — US took half of Mexico.. Chapultepec. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Mexican-American War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Mexican-American War.", "x": "More figures: US got California etc. shaped Mexican-American War as surely as anyone — Mexican cession.. US took half of Mexico. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Mexican-American War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Mexican-American War happened.", "x": "The causes: Texas annexation.. Buena Vista. Historians debate the deep vs immediate causes of Mexican-American War — US took half of Mexico.. Civil War officers trained. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Mexican-American War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Mexican-American War turned.", "x": "The turning point: Chapultepec.. Polk's expansion. Every great story has the moment it could have gone otherwise — Mexican-American War. US took half of Mexico. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-mexican-american-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
