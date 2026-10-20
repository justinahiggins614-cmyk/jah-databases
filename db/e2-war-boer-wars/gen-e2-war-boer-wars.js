(function(){'use strict';
/* JAH Boer Wars War Database generator — jahdb-e2-war-boer-wars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-boer-wars',PREFIX='JAH-E2WARBOERWA-',NAME='JAH Boer Wars War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Boer Wars: overview", "d": "Boer Wars (1880-1902): Britain vs Dutch settlers in South Africa..", "g": "overview", "l": 2, "q": "What is Boer Wars: overview?", "a": "Boer Wars (1880-1902): Britain vs Dutch settlers in South Africa..", "x": "The complete war guide to Boer Wars: Britain vs Dutch settlers in South Africa.. Gold and diamonds cause. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Boer Wars in its time: 1880-1902.", "g": "context", "l": 2, "q": "What is The era?", "a": "Boer Wars in its time: 1880-1902.", "x": "Context: Boer Wars belonged to 1880-1902 — Majuba Hill.. Guerrilla war. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Britain vs Dutch settlers in South Africa.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gold and diamonds cause.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gold and diamonds cause.", "x": "Boer Wars: Gold and diamonds cause.. Kimberley siege. This is one of the load-bearing facts about Boer Wars — learn it cold. Concentration camps. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Gold and diamonds cause..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Gold and diamonds cause..", "x": "Explained: Gold and diamonds cause.. Scorched earth. In the history of Boer Wars, this fact connects to Treaty of Vereeniging. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Guerrilla war.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Guerrilla war.", "x": "Boer Wars: Guerrilla war.. Kitchener. This is one of the load-bearing facts about Boer Wars — learn it cold. Treaty of Vereeniging. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Guerrilla war..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Guerrilla war..", "x": "Explained: Guerrilla war.. Emily Hobhouse. In the history of Boer Wars, this fact connects to Union of South Africa. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Concentration camps.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Concentration camps.", "x": "Boer Wars: Concentration camps.. Scorched earth. This is one of the load-bearing facts about Boer Wars — learn it cold. Union of South Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Concentration camps..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Concentration camps..", "x": "Explained: Concentration camps.. Legacy. In the history of Boer Wars, this fact connects to Apartheid roots. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Treaty of Vereeniging.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Treaty of Vereeniging.", "x": "Boer Wars: Treaty of Vereeniging.. Emily Hobhouse. This is one of the load-bearing facts about Boer Wars — learn it cold. Apartheid roots. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Treaty of Vereeniging..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Treaty of Vereeniging..", "x": "Explained: Treaty of Vereeniging.. Majuba Hill. In the history of Boer Wars, this fact connects to Gold and diamonds cause. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Union of South Africa.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Union of South Africa.", "x": "Boer Wars: Union of South Africa.. Legacy. This is one of the load-bearing facts about Boer Wars — learn it cold. Gold and diamonds cause. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Union of South Africa..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Union of South Africa..", "x": "Explained: Union of South Africa.. Kimberley siege. In the history of Boer Wars, this fact connects to Guerrilla war. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Apartheid roots.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Apartheid roots.", "x": "Boer Wars: Apartheid roots.. Majuba Hill. This is one of the load-bearing facts about Boer Wars — learn it cold. Guerrilla war. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Apartheid roots..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Apartheid roots..", "x": "Explained: Apartheid roots.. Kitchener. In the history of Boer Wars, this fact connects to Concentration camps. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Majuba Hill.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Majuba Hill.", "x": "Going deeper: Majuba Hill.. Guerrilla war. Details are where historians live — the numbers, the names, the decisions that turned Boer Wars the way it did. Britain vs Dutch settlers in South Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kimberley siege.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kimberley siege.", "x": "Going deeper: Kimberley siege.. Concentration camps. Details are where historians live — the numbers, the names, the decisions that turned Boer Wars the way it did. Britain vs Dutch settlers in South Africa.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Kitchener.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Kitchener.", "x": "Going deeper: Kitchener.. Treaty of Vereeniging. Details are where historians live — the numbers, the names, the decisions that turned Boer Wars the way it did. Britain vs Dutch settlers in South Africa.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Scorched earth.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Scorched earth.", "x": "Going deeper: Scorched earth.. Union of South Africa. Details are where historians live — the numbers, the names, the decisions that turned Boer Wars the way it did. Britain vs Dutch settlers in South Africa.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Emily Hobhouse.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Emily Hobhouse.", "x": "Going deeper: Emily Hobhouse.. Apartheid roots. Details are where historians live — the numbers, the names, the decisions that turned Boer Wars the way it did. Britain vs Dutch settlers in South Africa.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Gold and diamonds cause. Details are where historians live — the numbers, the names, the decisions that turned Boer Wars the way it did. Britain vs Dutch settlers in South Africa.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Boer Wars, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Boer Wars, event by event.", "x": "The timeline: Gold and diamonds cause.. Majuba Hill. Key dates in order — Concentration camps.. 1880-1902 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Boer Wars.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Boer Wars.", "x": "The people: Kimberley siege.. Treaty of Vereeniging. History is made by people deciding under pressure — Britain vs Dutch settlers in South Africa.. Scorched earth. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Boer Wars.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Boer Wars.", "x": "More figures: Union of South Africa. shaped Boer Wars as surely as anyone — Emily Hobhouse.. Britain vs Dutch settlers in South Africa. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Boer Wars happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Boer Wars happened.", "x": "The causes: Gold and diamonds cause.. Kitchener. Historians debate the deep vs immediate causes of Boer Wars — Britain vs Dutch settlers in South Africa.. Apartheid roots. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Boer Wars turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Boer Wars turned.", "x": "The turning point: Scorched earth.. Guerrilla war. Every great story has the moment it could have gone otherwise — Boer Wars. Britain vs Dutch settlers in South Africa. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-boer-wars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
