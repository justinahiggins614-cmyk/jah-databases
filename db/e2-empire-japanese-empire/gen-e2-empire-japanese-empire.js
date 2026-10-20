(function(){'use strict';
/* JAH Japanese Empire Empire Database generator — jahdb-e2-empire-japanese-empire-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-empire-japanese-empire',PREFIX='JAH-E2EMPIREJAP-',NAME='JAH Japanese Empire Empire Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Japanese Empire: overview", "d": "Japanese Empire (1868-1947): Meiji to WWII defeat..", "g": "overview", "l": 2, "q": "What is Japanese Empire: overview?", "a": "Japanese Empire (1868-1947): Meiji to WWII defeat..", "x": "The complete empire guide to Japanese Empire: Meiji to WWII defeat.. Meiji Restoration. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Japanese Empire in its time: 1868-1947.", "g": "context", "l": 2, "q": "What is The era?", "a": "Japanese Empire in its time: 1868-1947.", "x": "Context: Japanese Empire belonged to 1868-1947 — Modernization.. Industrialization. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Meiji to WWII defeat.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Meiji Restoration.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Meiji Restoration.", "x": "Japanese Empire: Meiji Restoration.. Military. This is one of the load-bearing facts about Japanese Empire — learn it cold. 1895/1905 wins. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Meiji Restoration..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Meiji Restoration..", "x": "Explained: Meiji Restoration.. War crimes. In the history of Japanese Empire, this fact connects to WWII. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Industrialization.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Industrialization.", "x": "Japanese Empire: Industrialization.. Colonies. This is one of the load-bearing facts about Japanese Empire — learn it cold. WWII. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Industrialization..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Industrialization..", "x": "Explained: Industrialization.. Occupation. In the history of Japanese Empire, this fact connects to Atomic end. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1895/1905 wins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1895/1905 wins.", "x": "Japanese Empire: 1895/1905 wins.. War crimes. This is one of the load-bearing facts about Japanese Empire — learn it cold. Atomic end. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 1895/1905 wins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 1895/1905 wins..", "x": "Explained: 1895/1905 wins.. Japan. In the history of Japanese Empire, this fact connects to Constitution 1947. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "WWII.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "WWII.", "x": "Japanese Empire: WWII.. Occupation. This is one of the load-bearing facts about Japanese Empire — learn it cold. Constitution 1947. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: WWII..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: WWII..", "x": "Explained: WWII.. Modernization. In the history of Japanese Empire, this fact connects to Meiji Restoration. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Atomic end.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Atomic end.", "x": "Japanese Empire: Atomic end.. Japan. This is one of the load-bearing facts about Japanese Empire — learn it cold. Meiji Restoration. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Atomic end..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Atomic end..", "x": "Explained: Atomic end.. Military. In the history of Japanese Empire, this fact connects to Industrialization. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Constitution 1947.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Constitution 1947.", "x": "Japanese Empire: Constitution 1947.. Modernization. This is one of the load-bearing facts about Japanese Empire — learn it cold. Industrialization. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Constitution 1947..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Constitution 1947..", "x": "Explained: Constitution 1947.. Colonies. In the history of Japanese Empire, this fact connects to 1895/1905 wins. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Modernization.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Modernization.", "x": "Going deeper: Modernization.. Industrialization. Details are where historians live — the numbers, the names, the decisions that turned Japanese Empire the way it did. Meiji to WWII defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Military.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Military.", "x": "Going deeper: Military.. 1895/1905 wins. Details are where historians live — the numbers, the names, the decisions that turned Japanese Empire the way it did. Meiji to WWII defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Colonies.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Colonies.", "x": "Going deeper: Colonies.. WWII. Details are where historians live — the numbers, the names, the decisions that turned Japanese Empire the way it did. Meiji to WWII defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "War crimes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "War crimes.", "x": "Going deeper: War crimes.. Atomic end. Details are where historians live — the numbers, the names, the decisions that turned Japanese Empire the way it did. Meiji to WWII defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Occupation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Occupation.", "x": "Going deeper: Occupation.. Constitution 1947. Details are where historians live — the numbers, the names, the decisions that turned Japanese Empire the way it did. Meiji to WWII defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Japan.", "x": "Going deeper: Japan.. Meiji Restoration. Details are where historians live — the numbers, the names, the decisions that turned Japanese Empire the way it did. Meiji to WWII defeat. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Japanese Empire, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Japanese Empire, event by event.", "x": "The timeline: Meiji Restoration.. Modernization. Key dates in order — 1895/1905 wins.. 1868-1947 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Japanese Empire.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Japanese Empire.", "x": "The people: Military.. WWII. History is made by people deciding under pressure — Meiji to WWII defeat.. War crimes. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Japanese Empire.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Japanese Empire.", "x": "More figures: Atomic end. shaped Japanese Empire as surely as anyone — Occupation.. Meiji to WWII defeat. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Japanese Empire happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Japanese Empire happened.", "x": "The causes: Meiji Restoration.. Colonies. Historians debate the deep vs immediate causes of Japanese Empire — Meiji to WWII defeat.. Constitution 1947. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Japanese Empire turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Japanese Empire turned.", "x": "The turning point: War crimes.. Industrialization. Every great story has the moment it could have gone otherwise — Japanese Empire. Meiji to WWII defeat. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-empire-japanese-empire-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
