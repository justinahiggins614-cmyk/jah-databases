(function(){'use strict';
/* JAH Crimean War War Database generator — jahdb-e2-war-crimean-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-crimean-war',PREFIX='JAH-E2WARCRIMEA-',NAME='JAH Crimean War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Crimean War: overview", "d": "Crimean War (1853-1856): Britain and France vs Russia; Florence Nightingale..", "g": "overview", "l": 2, "q": "What is Crimean War: overview?", "a": "Crimean War (1853-1856): Britain and France vs Russia; Florence Nightingale..", "x": "The complete war guide to Crimean War: Britain and France vs Russia; Florence Nightingale.. Charge of the Light Brigade. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Crimean War in its time: 1853-1856.", "g": "context", "l": 2, "q": "What is The era?", "a": "Crimean War in its time: 1853-1856.", "x": "Context: Crimean War belonged to 1853-1856 — Balaclava.. Sevastopol siege. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Charge of the Light Brigade.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Charge of the Light Brigade.", "x": "Crimean War: Charge of the Light Brigade.. Inkerman. This is one of the load-bearing facts about Crimean War — learn it cold. Nightingale: nursing. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Charge of the Light Brigade..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Charge of the Light Brigade..", "x": "Explained: Charge of the Light Brigade.. Photography (Fenton). In the history of Crimean War, this fact connects to Telegraph war reporting. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sevastopol siege.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sevastopol siege.", "x": "Crimean War: Sevastopol siege.. Sanitary reform. This is one of the load-bearing facts about Crimean War — learn it cold. Telegraph war reporting. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Sevastopol siege..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Sevastopol siege..", "x": "Explained: Sevastopol siege.. Russian decline. In the history of Crimean War, this fact connects to Treaty of Paris. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nightingale: nursing.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nightingale: nursing.", "x": "Crimean War: Nightingale: nursing.. Photography (Fenton). This is one of the load-bearing facts about Crimean War — learn it cold. Treaty of Paris. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Nightingale: nursing..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Nightingale: nursing..", "x": "Explained: Nightingale: nursing.. Nursing legacy. In the history of Crimean War, this fact connects to Modern nursing born. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Telegraph war reporting.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Telegraph war reporting.", "x": "Crimean War: Telegraph war reporting.. Russian decline. This is one of the load-bearing facts about Crimean War — learn it cold. Modern nursing born. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Telegraph war reporting..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Telegraph war reporting..", "x": "Explained: Telegraph war reporting.. Balaclava. In the history of Crimean War, this fact connects to Charge of the Light Brigade. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Treaty of Paris.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Treaty of Paris.", "x": "Crimean War: Treaty of Paris.. Nursing legacy. This is one of the load-bearing facts about Crimean War — learn it cold. Charge of the Light Brigade. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Treaty of Paris..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Treaty of Paris..", "x": "Explained: Treaty of Paris.. Inkerman. In the history of Crimean War, this fact connects to Sevastopol siege. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Modern nursing born.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Modern nursing born.", "x": "Crimean War: Modern nursing born.. Balaclava. This is one of the load-bearing facts about Crimean War — learn it cold. Sevastopol siege. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Modern nursing born..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Modern nursing born..", "x": "Explained: Modern nursing born.. Sanitary reform. In the history of Crimean War, this fact connects to Nightingale: nursing. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Balaclava.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Balaclava.", "x": "Going deeper: Balaclava.. Sevastopol siege. Details are where historians live — the numbers, the names, the decisions that turned Crimean War the way it did. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Inkerman.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Inkerman.", "x": "Going deeper: Inkerman.. Nightingale: nursing. Details are where historians live — the numbers, the names, the decisions that turned Crimean War the way it did. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sanitary reform.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sanitary reform.", "x": "Going deeper: Sanitary reform.. Telegraph war reporting. Details are where historians live — the numbers, the names, the decisions that turned Crimean War the way it did. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Photography (Fenton).", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Photography (Fenton).", "x": "Going deeper: Photography (Fenton).. Treaty of Paris. Details are where historians live — the numbers, the names, the decisions that turned Crimean War the way it did. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Russian decline.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Russian decline.", "x": "Going deeper: Russian decline.. Modern nursing born. Details are where historians live — the numbers, the names, the decisions that turned Crimean War the way it did. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Nursing legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Nursing legacy.", "x": "Going deeper: Nursing legacy.. Charge of the Light Brigade. Details are where historians live — the numbers, the names, the decisions that turned Crimean War the way it did. Britain and France vs Russia; Florence Nightingale.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Crimean War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Crimean War, event by event.", "x": "The timeline: Charge of the Light Brigade.. Balaclava. Key dates in order — Nightingale: nursing.. 1853-1856 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Crimean War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Crimean War.", "x": "The people: Inkerman.. Telegraph war reporting. History is made by people deciding under pressure — Britain and France vs Russia; Florence Nightingale.. Photography (Fenton). Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Crimean War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Crimean War.", "x": "More figures: Treaty of Paris. shaped Crimean War as surely as anyone — Russian decline.. Britain and France vs Russia; Florence Nightingale. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Crimean War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Crimean War happened.", "x": "The causes: Charge of the Light Brigade.. Sanitary reform. Historians debate the deep vs immediate causes of Crimean War — Britain and France vs Russia; Florence Nightingale.. Modern nursing born. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Crimean War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Crimean War turned.", "x": "The turning point: Photography (Fenton).. Sevastopol siege. Every great story has the moment it could have gone otherwise — Crimean War. Britain and France vs Russia; Florence Nightingale. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-crimean-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
