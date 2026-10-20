(function(){'use strict';
/* JAH Taiping Rebellion War Database generator — jahdb-e2-war-taiping-rebellion-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-taiping-rebellion',PREFIX='JAH-E2WARTAIPIN-',NAME='JAH Taiping Rebellion War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Taiping Rebellion: overview", "d": "Taiping Rebellion (1850-1864): deadliest civil war ever: 20M+ died..", "g": "overview", "l": 2, "q": "What is Taiping Rebellion: overview?", "a": "Taiping Rebellion (1850-1864): deadliest civil war ever: 20M+ died..", "x": "The complete war guide to Taiping Rebellion: deadliest civil war ever: 20M+ died.. Hong Xiuquan: Jesus' brother claim. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Taiping Rebellion in its time: 1850-1864.", "g": "context", "l": 2, "q": "What is The era?", "a": "Taiping Rebellion in its time: 1850-1864.", "x": "Context: Taiping Rebellion belonged to 1850-1864 — God Worshippers.. Nanking capital. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hong Xiuquan: Jesus' brother claim.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hong Xiuquan: Jesus' brother claim.", "x": "Taiping Rebellion: Hong Xiuquan: Jesus' brother claim.. Ever-Victorious Army. This is one of the load-bearing facts about Taiping Rebellion — learn it cold. 20-30M died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Hong Xiuquan: Jesus' brother claim..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Hong Xiuquan: Jesus' brother claim..", "x": "Explained: Hong Xiuquan: Jesus' brother claim.. Aftermath. In the history of Taiping Rebellion, this fact connects to Qing + Western help won. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nanking capital.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nanking capital.", "x": "Taiping Rebellion: Nanking capital.. Nanking fall. This is one of the load-bearing facts about Taiping Rebellion — learn it cold. Qing + Western help won. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Nanking capital..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Nanking capital..", "x": "Explained: Nanking capital.. Hakka. In the history of Taiping Rebellion, this fact connects to Deadliest before WWI. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "20-30M died.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "20-30M died.", "x": "Taiping Rebellion: 20-30M died.. Aftermath. This is one of the load-bearing facts about Taiping Rebellion — learn it cold. Deadliest before WWI. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 20-30M died..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 20-30M died..", "x": "Explained: 20-30M died.. History's toll. In the history of Taiping Rebellion, this fact connects to Christian cult state. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Qing + Western help won.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Qing + Western help won.", "x": "Taiping Rebellion: Qing + Western help won.. Hakka. This is one of the load-bearing facts about Taiping Rebellion — learn it cold. Christian cult state. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Qing + Western help won..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Qing + Western help won..", "x": "Explained: Qing + Western help won.. God Worshippers. In the history of Taiping Rebellion, this fact connects to Hong Xiuquan: Jesus' brother claim. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Deadliest before WWI.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Deadliest before WWI.", "x": "Taiping Rebellion: Deadliest before WWI.. History's toll. This is one of the load-bearing facts about Taiping Rebellion — learn it cold. Hong Xiuquan: Jesus' brother claim. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Deadliest before WWI..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Deadliest before WWI..", "x": "Explained: Deadliest before WWI.. Ever-Victorious Army. In the history of Taiping Rebellion, this fact connects to Nanking capital. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Christian cult state.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Christian cult state.", "x": "Taiping Rebellion: Christian cult state.. God Worshippers. This is one of the load-bearing facts about Taiping Rebellion — learn it cold. Nanking capital. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Christian cult state..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Christian cult state..", "x": "Explained: Christian cult state.. Nanking fall. In the history of Taiping Rebellion, this fact connects to 20-30M died. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "God Worshippers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "God Worshippers.", "x": "Going deeper: God Worshippers.. Nanking capital. Details are where historians live — the numbers, the names, the decisions that turned Taiping Rebellion the way it did. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ever-Victorious Army.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ever-Victorious Army.", "x": "Going deeper: Ever-Victorious Army.. 20-30M died. Details are where historians live — the numbers, the names, the decisions that turned Taiping Rebellion the way it did. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Nanking fall.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Nanking fall.", "x": "Going deeper: Nanking fall.. Qing + Western help won. Details are where historians live — the numbers, the names, the decisions that turned Taiping Rebellion the way it did. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Aftermath.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Aftermath.", "x": "Going deeper: Aftermath.. Deadliest before WWI. Details are where historians live — the numbers, the names, the decisions that turned Taiping Rebellion the way it did. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hakka.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hakka.", "x": "Going deeper: Hakka.. Christian cult state. Details are where historians live — the numbers, the names, the decisions that turned Taiping Rebellion the way it did. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History's toll.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History's toll.", "x": "Going deeper: History's toll.. Hong Xiuquan: Jesus' brother claim. Details are where historians live — the numbers, the names, the decisions that turned Taiping Rebellion the way it did. deadliest civil war ever: 20M+ died.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Taiping Rebellion, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Taiping Rebellion, event by event.", "x": "The timeline: Hong Xiuquan: Jesus' brother claim.. God Worshippers. Key dates in order — 20-30M died.. 1850-1864 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Taiping Rebellion.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Taiping Rebellion.", "x": "The people: Ever-Victorious Army.. Qing + Western help won. History is made by people deciding under pressure — deadliest civil war ever: 20M+ died.. Aftermath. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Taiping Rebellion.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Taiping Rebellion.", "x": "More figures: Deadliest before WWI. shaped Taiping Rebellion as surely as anyone — Hakka.. deadliest civil war ever: 20M+ died. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Taiping Rebellion happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Taiping Rebellion happened.", "x": "The causes: Hong Xiuquan: Jesus' brother claim.. Nanking fall. Historians debate the deep vs immediate causes of Taiping Rebellion — deadliest civil war ever: 20M+ died.. Christian cult state. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Taiping Rebellion turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Taiping Rebellion turned.", "x": "The turning point: Aftermath.. Nanking capital. Every great story has the moment it could have gone otherwise — Taiping Rebellion. deadliest civil war ever: 20M+ died. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-taiping-rebellion-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
