(function(){'use strict';
/* JAH American Civil War War Database generator — jahdb-e2-war-american-civil-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-american-civil-war',PREFIX='JAH-E2WARAMERIC-',NAME='JAH American Civil War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "American Civil War: overview", "d": "American Civil War (1861-1865): America's bloodiest war; ended slavery..", "g": "overview", "l": 2, "q": "What is American Civil War: overview?", "a": "American Civil War (1861-1865): America's bloodiest war; ended slavery..", "x": "The complete war guide to American Civil War: America's bloodiest war; ended slavery.. Fort Sumter: first shots (1861). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "American Civil War in its time: 1861-1865.", "g": "context", "l": 2, "q": "What is The era?", "a": "American Civil War in its time: 1861-1865.", "x": "Context: American Civil War belonged to 1861-1865 — North vs South economies.. Emancipation Proclamation (1863). Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fort Sumter: first shots (1861).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fort Sumter: first shots (1861).", "x": "American Civil War: Fort Sumter: first shots (1861).. Grant vs Lee. This is one of the load-bearing facts about American Civil War — learn it cold. Gettysburg: turning point. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Fort Sumter: first shots (1861)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Fort Sumter: first shots (1861)..", "x": "Explained: Fort Sumter: first shots (1861).. Sherman's March. In the history of American Civil War, this fact connects to Lincoln assassinated (1865). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Emancipation Proclamation (1863).", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Emancipation Proclamation (1863).", "x": "American Civil War: Emancipation Proclamation (1863).. Antietam: bloodiest day. This is one of the load-bearing facts about American Civil War — learn it cold. Lincoln assassinated (1865). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Emancipation Proclamation (1863)..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Emancipation Proclamation (1863)..", "x": "Explained: Emancipation Proclamation (1863).. Reconstruction. In the history of American Civil War, this fact connects to 620,000+ died. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gettysburg: turning point.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gettysburg: turning point.", "x": "American Civil War: Gettysburg: turning point.. Sherman's March. This is one of the load-bearing facts about American Civil War — learn it cold. 620,000+ died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Gettysburg: turning point..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Gettysburg: turning point..", "x": "Explained: Gettysburg: turning point.. Battlefields preserved. In the history of American Civil War, this fact connects to 13th Amendment abolished slavery. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lincoln assassinated (1865).", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lincoln assassinated (1865).", "x": "American Civil War: Lincoln assassinated (1865).. Reconstruction. This is one of the load-bearing facts about American Civil War — learn it cold. 13th Amendment abolished slavery. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Lincoln assassinated (1865)..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Lincoln assassinated (1865)..", "x": "Explained: Lincoln assassinated (1865).. North vs South economies. In the history of American Civil War, this fact connects to Fort Sumter: first shots (1861). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "620,000+ died.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "620,000+ died.", "x": "American Civil War: 620,000+ died.. Battlefields preserved. This is one of the load-bearing facts about American Civil War — learn it cold. Fort Sumter: first shots (1861). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 620,000+ died..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 620,000+ died..", "x": "Explained: 620,000+ died.. Grant vs Lee. In the history of American Civil War, this fact connects to Emancipation Proclamation (1863). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "13th Amendment abolished slavery.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "13th Amendment abolished slavery.", "x": "American Civil War: 13th Amendment abolished slavery.. North vs South economies. This is one of the load-bearing facts about American Civil War — learn it cold. Emancipation Proclamation (1863). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 13th Amendment abolished slavery..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 13th Amendment abolished slavery..", "x": "Explained: 13th Amendment abolished slavery.. Antietam: bloodiest day. In the history of American Civil War, this fact connects to Gettysburg: turning point. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "North vs South economies.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "North vs South economies.", "x": "Going deeper: North vs South economies.. Emancipation Proclamation (1863). Details are where historians live — the numbers, the names, the decisions that turned American Civil War the way it did. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Grant vs Lee.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Grant vs Lee.", "x": "Going deeper: Grant vs Lee.. Gettysburg: turning point. Details are where historians live — the numbers, the names, the decisions that turned American Civil War the way it did. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Antietam: bloodiest day.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Antietam: bloodiest day.", "x": "Going deeper: Antietam: bloodiest day.. Lincoln assassinated (1865). Details are where historians live — the numbers, the names, the decisions that turned American Civil War the way it did. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sherman's March.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sherman's March.", "x": "Going deeper: Sherman's March.. 620,000+ died. Details are where historians live — the numbers, the names, the decisions that turned American Civil War the way it did. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reconstruction.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reconstruction.", "x": "Going deeper: Reconstruction.. 13th Amendment abolished slavery. Details are where historians live — the numbers, the names, the decisions that turned American Civil War the way it did. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Battlefields preserved.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Battlefields preserved.", "x": "Going deeper: Battlefields preserved.. Fort Sumter: first shots (1861). Details are where historians live — the numbers, the names, the decisions that turned American Civil War the way it did. America's bloodiest war; ended slavery.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "American Civil War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "American Civil War, event by event.", "x": "The timeline: Fort Sumter: first shots (1861).. North vs South economies. Key dates in order — Gettysburg: turning point.. 1861-1865 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of American Civil War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of American Civil War.", "x": "The people: Grant vs Lee.. Lincoln assassinated (1865). History is made by people deciding under pressure — America's bloodiest war; ended slavery.. Sherman's March. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped American Civil War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped American Civil War.", "x": "More figures: 620,000+ died. shaped American Civil War as surely as anyone — Reconstruction.. America's bloodiest war; ended slavery. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why American Civil War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why American Civil War happened.", "x": "The causes: Fort Sumter: first shots (1861).. Antietam: bloodiest day. Historians debate the deep vs immediate causes of American Civil War — America's bloodiest war; ended slavery.. 13th Amendment abolished slavery. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment American Civil War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment American Civil War turned.", "x": "The turning point: Sherman's March.. Emancipation Proclamation (1863). Every great story has the moment it could have gone otherwise — American Civil War. America's bloodiest war; ended slavery. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-american-civil-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
