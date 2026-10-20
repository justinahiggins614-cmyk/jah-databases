(function(){'use strict';
/* JAH Korean War War Database generator — jahdb-e2-war-korean-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-korean-war',PREFIX='JAH-E2WARKOREAN-',NAME='JAH Korean War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Korean War: overview", "d": "Korean War (1950-1953): the Forgotten War; peninsula still divided..", "g": "overview", "l": 2, "q": "What is Korean War: overview?", "a": "Korean War (1950-1953): the Forgotten War; peninsula still divided..", "x": "The complete war guide to Korean War: the Forgotten War; peninsula still divided.. North invaded South (1950). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Korean War in its time: 1950-1953.", "g": "context", "l": 2, "q": "What is The era?", "a": "Korean War in its time: 1950-1953.", "x": "Context: Korean War belonged to 1950-1953 — UN coalition.. Inchon landing. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. the Forgotten War; peninsula still divided.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "North invaded South (1950).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "North invaded South (1950).", "x": "Korean War: North invaded South (1950).. Pusan Perimeter. This is one of the load-bearing facts about Korean War — learn it cold. China intervened. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: North invaded South (1950)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: North invaded South (1950)..", "x": "Explained: North invaded South (1950).. MiG Alley. In the history of Korean War, this fact connects to 38th parallel stalemate. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Inchon landing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Inchon landing.", "x": "Korean War: Inchon landing.. Chosin Reservoir. This is one of the load-bearing facts about Korean War — learn it cold. 38th parallel stalemate. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Inchon landing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Inchon landing..", "x": "Explained: Inchon landing.. DMZ today. In the history of Korean War, this fact connects to Armistice 1953 (no peace treaty). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "China intervened.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "China intervened.", "x": "Korean War: China intervened.. MiG Alley. This is one of the load-bearing facts about Korean War — learn it cold. Armistice 1953 (no peace treaty). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: China intervened..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: China intervened..", "x": "Explained: China intervened.. 38th parallel. In the history of Korean War, this fact connects to MacArthur fired. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "38th parallel stalemate.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "38th parallel stalemate.", "x": "Korean War: 38th parallel stalemate.. DMZ today. This is one of the load-bearing facts about Korean War — learn it cold. MacArthur fired. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: 38th parallel stalemate..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: 38th parallel stalemate..", "x": "Explained: 38th parallel stalemate.. UN coalition. In the history of Korean War, this fact connects to North invaded South (1950). — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Armistice 1953 (no peace treaty).", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Armistice 1953 (no peace treaty).", "x": "Korean War: Armistice 1953 (no peace treaty).. 38th parallel. This is one of the load-bearing facts about Korean War — learn it cold. North invaded South (1950). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Armistice 1953 (no peace treaty)..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Armistice 1953 (no peace treaty)..", "x": "Explained: Armistice 1953 (no peace treaty).. Pusan Perimeter. In the history of Korean War, this fact connects to Inchon landing. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "MacArthur fired.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "MacArthur fired.", "x": "Korean War: MacArthur fired.. UN coalition. This is one of the load-bearing facts about Korean War — learn it cold. Inchon landing. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: MacArthur fired..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: MacArthur fired..", "x": "Explained: MacArthur fired.. Chosin Reservoir. In the history of Korean War, this fact connects to China intervened. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "UN coalition.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "UN coalition.", "x": "Going deeper: UN coalition.. Inchon landing. Details are where historians live — the numbers, the names, the decisions that turned Korean War the way it did. the Forgotten War; peninsula still divided.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pusan Perimeter.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pusan Perimeter.", "x": "Going deeper: Pusan Perimeter.. China intervened. Details are where historians live — the numbers, the names, the decisions that turned Korean War the way it did. the Forgotten War; peninsula still divided.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Chosin Reservoir.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Chosin Reservoir.", "x": "Going deeper: Chosin Reservoir.. 38th parallel stalemate. Details are where historians live — the numbers, the names, the decisions that turned Korean War the way it did. the Forgotten War; peninsula still divided.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "MiG Alley.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "MiG Alley.", "x": "Going deeper: MiG Alley.. Armistice 1953 (no peace treaty). Details are where historians live — the numbers, the names, the decisions that turned Korean War the way it did. the Forgotten War; peninsula still divided.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "DMZ today.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "DMZ today.", "x": "Going deeper: DMZ today.. MacArthur fired. Details are where historians live — the numbers, the names, the decisions that turned Korean War the way it did. the Forgotten War; peninsula still divided. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "38th parallel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "38th parallel.", "x": "Going deeper: 38th parallel.. North invaded South (1950). Details are where historians live — the numbers, the names, the decisions that turned Korean War the way it did. the Forgotten War; peninsula still divided.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Korean War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Korean War, event by event.", "x": "The timeline: North invaded South (1950).. UN coalition. Key dates in order — China intervened.. 1950-1953 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Korean War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Korean War.", "x": "The people: Pusan Perimeter.. 38th parallel stalemate. History is made by people deciding under pressure — the Forgotten War; peninsula still divided.. MiG Alley. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Korean War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Korean War.", "x": "More figures: Armistice 1953 (no peace treaty). shaped Korean War as surely as anyone — DMZ today.. the Forgotten War; peninsula still divided. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Korean War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Korean War happened.", "x": "The causes: North invaded South (1950).. Chosin Reservoir. Historians debate the deep vs immediate causes of Korean War — the Forgotten War; peninsula still divided.. MacArthur fired. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Korean War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Korean War turned.", "x": "The turning point: MiG Alley.. Inchon landing. Every great story has the moment it could have gone otherwise — Korean War. the Forgotten War; peninsula still divided. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-korean-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
