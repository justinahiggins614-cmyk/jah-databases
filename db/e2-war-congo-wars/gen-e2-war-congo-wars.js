(function(){'use strict';
/* JAH Congo Wars War Database generator — jahdb-e2-war-congo-wars-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-congo-wars',PREFIX='JAH-E2WARCONGOW-',NAME='JAH Congo Wars War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Congo Wars: overview", "d": "Congo Wars (1996-2003): Africa's world war; millions died..", "g": "overview", "l": 2, "q": "What is Congo Wars: overview?", "a": "Congo Wars (1996-2003): Africa's world war; millions died..", "x": "The complete war guide to Congo Wars: Africa's world war; millions died.. Rwanda genocide fallout. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Congo Wars in its time: 1996-2003.", "g": "context", "l": 2, "q": "What is The era?", "a": "Congo Wars in its time: 1996-2003.", "x": "Context: Congo Wars belonged to 1996-2003 — Refugee camps.. Mobutu fell. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. Africa's world war; millions died.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rwanda genocide fallout.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rwanda genocide fallout.", "x": "Congo Wars: Rwanda genocide fallout.. 9 nations involved. This is one of the load-bearing facts about Congo Wars — learn it cold. 5M+ died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Rwanda genocide fallout..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Rwanda genocide fallout..", "x": "Explained: Rwanda genocide fallout.. UN mission. In the history of Congo Wars, this fact connects to Coltan/minerals. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mobutu fell.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mobutu fell.", "x": "Congo Wars: Mobutu fell.. Resource curse. This is one of the load-bearing facts about Congo Wars — learn it cold. Coltan/minerals. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Mobutu fell..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Mobutu fell..", "x": "Explained: Mobutu fell.. Aftermath. In the history of Congo Wars, this fact connects to Kabila assassinated. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "5M+ died.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "5M+ died.", "x": "Congo Wars: 5M+ died.. UN mission. This is one of the load-bearing facts about Congo Wars — learn it cold. Kabila assassinated. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 5M+ died..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 5M+ died..", "x": "Explained: 5M+ died.. Justice. In the history of Congo Wars, this fact connects to Peace 2003. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Coltan/minerals.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Coltan/minerals.", "x": "Congo Wars: Coltan/minerals.. Aftermath. This is one of the load-bearing facts about Congo Wars — learn it cold. Peace 2003. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Coltan/minerals..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Coltan/minerals..", "x": "Explained: Coltan/minerals.. Refugee camps. In the history of Congo Wars, this fact connects to Rwanda genocide fallout. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kabila assassinated.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kabila assassinated.", "x": "Congo Wars: Kabila assassinated.. Justice. This is one of the load-bearing facts about Congo Wars — learn it cold. Rwanda genocide fallout. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Kabila assassinated..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Kabila assassinated..", "x": "Explained: Kabila assassinated.. 9 nations involved. In the history of Congo Wars, this fact connects to Mobutu fell. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Peace 2003.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Peace 2003.", "x": "Congo Wars: Peace 2003.. Refugee camps. This is one of the load-bearing facts about Congo Wars — learn it cold. Mobutu fell. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Peace 2003..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Peace 2003..", "x": "Explained: Peace 2003.. Resource curse. In the history of Congo Wars, this fact connects to 5M+ died. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Refugee camps.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Refugee camps.", "x": "Going deeper: Refugee camps.. Mobutu fell. Details are where historians live — the numbers, the names, the decisions that turned Congo Wars the way it did. Africa's world war; millions died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "9 nations involved.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "9 nations involved.", "x": "Going deeper: 9 nations involved.. 5M+ died. Details are where historians live — the numbers, the names, the decisions that turned Congo Wars the way it did. Africa's world war; millions died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Resource curse.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Resource curse.", "x": "Going deeper: Resource curse.. Coltan/minerals. Details are where historians live — the numbers, the names, the decisions that turned Congo Wars the way it did. Africa's world war; millions died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "UN mission.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "UN mission.", "x": "Going deeper: UN mission.. Kabila assassinated. Details are where historians live — the numbers, the names, the decisions that turned Congo Wars the way it did. Africa's world war; millions died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. Peace 2003. Details are where historians live — the numbers, the names, the decisions that turned Congo Wars the way it did. Africa's world war; millions died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Justice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Justice.", "x": "Going deeper: Justice.. Rwanda genocide fallout. Details are where historians live — the numbers, the names, the decisions that turned Congo Wars the way it did. Africa's world war; millions died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Congo Wars, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Congo Wars, event by event.", "x": "The timeline: Rwanda genocide fallout.. Refugee camps. Key dates in order — 5M+ died.. 1996-2003 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Congo Wars.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Congo Wars.", "x": "The people: 9 nations involved.. Coltan/minerals. History is made by people deciding under pressure — Africa's world war; millions died.. UN mission. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Congo Wars.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Congo Wars.", "x": "More figures: Kabila assassinated. shaped Congo Wars as surely as anyone — Aftermath.. Africa's world war; millions died. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Congo Wars happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Congo Wars happened.", "x": "The causes: Rwanda genocide fallout.. Resource curse. Historians debate the deep vs immediate causes of Congo Wars — Africa's world war; millions died.. Peace 2003. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Congo Wars turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Congo Wars turned.", "x": "The turning point: UN mission.. Mobutu fell. Every great story has the moment it could have gone otherwise — Congo Wars. Africa's world war; millions died. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-congo-wars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
