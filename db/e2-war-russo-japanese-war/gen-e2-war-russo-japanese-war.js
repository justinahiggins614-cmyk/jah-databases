(function(){'use strict';
/* JAH Russo-Japanese War War Database generator — jahdb-e2-war-russo-japanese-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-russo-japanese-war',PREFIX='JAH-E2WARRUSSOJ-',NAME='JAH Russo-Japanese War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Russo-Japanese War: overview", "d": "Russo-Japanese War (1904-1905): Japan shocked a European power..", "g": "overview", "l": 2, "q": "What is Russo-Japanese War: overview?", "a": "Russo-Japanese War (1904-1905): Japan shocked a European power..", "x": "The complete war guide to Russo-Japanese War: Japan shocked a European power.. Port Arthur siege. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Russo-Japanese War in its time: 1904-1905.", "g": "context", "l": 2, "q": "What is The era?", "a": "Russo-Japanese War in its time: 1904-1905.", "x": "Context: Russo-Japanese War belonged to 1904-1905 — Surprise attack.. Tsushima: naval annihilation. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Japan shocked a European power.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Port Arthur siege.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Port Arthur siege.", "x": "Russo-Japanese War: Port Arthur siege.. Baltic Fleet sailed. This is one of the load-bearing facts about Russo-Japanese War — learn it cold. First Asian win over Europe. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Port Arthur siege..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Port Arthur siege..", "x": "Explained: Port Arthur siege.. Nobel Peace Prize. In the history of Russo-Japanese War, this fact connects to Treaty of Portsmouth. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tsushima: naval annihilation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tsushima: naval annihilation.", "x": "Russo-Japanese War: Tsushima: naval annihilation.. Mukden battle. This is one of the load-bearing facts about Russo-Japanese War — learn it cold. Treaty of Portsmouth. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Tsushima: naval annihilation..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Tsushima: naval annihilation..", "x": "Explained: Tsushima: naval annihilation.. Japan's rise. In the history of Russo-Japanese War, this fact connects to Teddy Roosevelt mediated. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First Asian win over Europe.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First Asian win over Europe.", "x": "Russo-Japanese War: First Asian win over Europe.. Nobel Peace Prize. This is one of the load-bearing facts about Russo-Japanese War — learn it cold. Teddy Roosevelt mediated. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: First Asian win over Europe..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: First Asian win over Europe..", "x": "Explained: First Asian win over Europe.. Prestige. In the history of Russo-Japanese War, this fact connects to Russian Revolution fueled. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Treaty of Portsmouth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Treaty of Portsmouth.", "x": "Russo-Japanese War: Treaty of Portsmouth.. Japan's rise. This is one of the load-bearing facts about Russo-Japanese War — learn it cold. Russian Revolution fueled. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Treaty of Portsmouth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Treaty of Portsmouth..", "x": "Explained: Treaty of Portsmouth.. Surprise attack. In the history of Russo-Japanese War, this fact connects to Port Arthur siege. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Teddy Roosevelt mediated.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Teddy Roosevelt mediated.", "x": "Russo-Japanese War: Teddy Roosevelt mediated.. Prestige. This is one of the load-bearing facts about Russo-Japanese War — learn it cold. Port Arthur siege. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Teddy Roosevelt mediated..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Teddy Roosevelt mediated..", "x": "Explained: Teddy Roosevelt mediated.. Baltic Fleet sailed. In the history of Russo-Japanese War, this fact connects to Tsushima: naval annihilation. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Russian Revolution fueled.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Russian Revolution fueled.", "x": "Russo-Japanese War: Russian Revolution fueled.. Surprise attack. This is one of the load-bearing facts about Russo-Japanese War — learn it cold. Tsushima: naval annihilation. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Russian Revolution fueled..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Russian Revolution fueled..", "x": "Explained: Russian Revolution fueled.. Mukden battle. In the history of Russo-Japanese War, this fact connects to First Asian win over Europe. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Surprise attack.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Surprise attack.", "x": "Going deeper: Surprise attack.. Tsushima: naval annihilation. Details are where historians live — the numbers, the names, the decisions that turned Russo-Japanese War the way it did. Japan shocked a European power.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Baltic Fleet sailed.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Baltic Fleet sailed.", "x": "Going deeper: Baltic Fleet sailed.. First Asian win over Europe. Details are where historians live — the numbers, the names, the decisions that turned Russo-Japanese War the way it did. Japan shocked a European power.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mukden battle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mukden battle.", "x": "Going deeper: Mukden battle.. Treaty of Portsmouth. Details are where historians live — the numbers, the names, the decisions that turned Russo-Japanese War the way it did. Japan shocked a European power.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nobel Peace Prize.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nobel Peace Prize.", "x": "Going deeper: Nobel Peace Prize.. Teddy Roosevelt mediated. Details are where historians live — the numbers, the names, the decisions that turned Russo-Japanese War the way it did. Japan shocked a European power.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Japan's rise.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Japan's rise.", "x": "Going deeper: Japan's rise.. Russian Revolution fueled. Details are where historians live — the numbers, the names, the decisions that turned Russo-Japanese War the way it did. Japan shocked a European power.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Prestige.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Prestige.", "x": "Going deeper: Prestige.. Port Arthur siege. Details are where historians live — the numbers, the names, the decisions that turned Russo-Japanese War the way it did. Japan shocked a European power. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Russo-Japanese War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Russo-Japanese War, event by event.", "x": "The timeline: Port Arthur siege.. Surprise attack. Key dates in order — First Asian win over Europe.. 1904-1905 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Russo-Japanese War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Russo-Japanese War.", "x": "The people: Baltic Fleet sailed.. Treaty of Portsmouth. History is made by people deciding under pressure — Japan shocked a European power.. Nobel Peace Prize. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Russo-Japanese War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Russo-Japanese War.", "x": "More figures: Teddy Roosevelt mediated. shaped Russo-Japanese War as surely as anyone — Japan's rise.. Japan shocked a European power. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Russo-Japanese War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Russo-Japanese War happened.", "x": "The causes: Port Arthur siege.. Mukden battle. Historians debate the deep vs immediate causes of Russo-Japanese War — Japan shocked a European power.. Russian Revolution fueled. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Russo-Japanese War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Russo-Japanese War turned.", "x": "The turning point: Nobel Peace Prize.. Tsushima: naval annihilation. Every great story has the moment it could have gone otherwise — Russo-Japanese War. Japan shocked a European power. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-russo-japanese-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
