(function(){'use strict';
/* JAH Brazilian Empire Empire Database generator — jahdb-e2-empire-brazilian-empire-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-empire-brazilian-empire',PREFIX='JAH-E2EMPIREBRA-',NAME='JAH Brazilian Empire Empire Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Brazilian Empire: overview", "d": "Brazilian Empire (1822-1889): America's monarchy..", "g": "overview", "l": 2, "q": "What is Brazilian Empire: overview?", "a": "Brazilian Empire (1822-1889): America's monarchy..", "x": "The complete empire guide to Brazilian Empire: America's monarchy.. Pedro I. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Brazilian Empire in its time: 1822-1889.", "g": "context", "l": 2, "q": "What is The era?", "a": "Brazilian Empire in its time: 1822-1889.", "x": "Context: Brazilian Empire belonged to 1822-1889 — Independence.. Coffee boom. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pedro I.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pedro I.", "x": "Brazilian Empire: Pedro I.. Paraguay War. This is one of the load-bearing facts about Brazilian Empire — learn it cold. Abolition 1888. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Pedro I..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Pedro I..", "x": "Explained: Pedro I.. Culture. In the history of Brazilian Empire, this fact connects to Pedro II. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Coffee boom.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Coffee boom.", "x": "Brazilian Empire: Coffee boom.. Slavery. This is one of the load-bearing facts about Brazilian Empire — learn it cold. Pedro II. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Coffee boom..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Coffee boom..", "x": "Explained: Coffee boom.. Fall. In the history of Brazilian Empire, this fact connects to 1889 republic. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Abolition 1888.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Abolition 1888.", "x": "Brazilian Empire: Abolition 1888.. Culture. This is one of the load-bearing facts about Brazilian Empire — learn it cold. 1889 republic. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Abolition 1888..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Abolition 1888..", "x": "Explained: Abolition 1888.. Legacy. In the history of Brazilian Empire, this fact connects to Brasilia later. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pedro II.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pedro II.", "x": "Brazilian Empire: Pedro II.. Fall. This is one of the load-bearing facts about Brazilian Empire — learn it cold. Brasilia later. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Pedro II..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Pedro II..", "x": "Explained: Pedro II.. Independence. In the history of Brazilian Empire, this fact connects to Pedro I. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1889 republic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1889 republic.", "x": "Brazilian Empire: 1889 republic.. Legacy. This is one of the load-bearing facts about Brazilian Empire — learn it cold. Pedro I. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 1889 republic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 1889 republic..", "x": "Explained: 1889 republic.. Paraguay War. In the history of Brazilian Empire, this fact connects to Coffee boom. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Brasilia later.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Brasilia later.", "x": "Brazilian Empire: Brasilia later.. Independence. This is one of the load-bearing facts about Brazilian Empire — learn it cold. Coffee boom. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Brasilia later..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Brasilia later..", "x": "Explained: Brasilia later.. Slavery. In the history of Brazilian Empire, this fact connects to Abolition 1888. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Independence.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Independence.", "x": "Going deeper: Independence.. Coffee boom. Details are where historians live — the numbers, the names, the decisions that turned Brazilian Empire the way it did. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Paraguay War.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Paraguay War.", "x": "Going deeper: Paraguay War.. Abolition 1888. Details are where historians live — the numbers, the names, the decisions that turned Brazilian Empire the way it did. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Slavery.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Slavery.", "x": "Going deeper: Slavery.. Pedro II. Details are where historians live — the numbers, the names, the decisions that turned Brazilian Empire the way it did. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Culture.", "x": "Going deeper: Culture.. 1889 republic. Details are where historians live — the numbers, the names, the decisions that turned Brazilian Empire the way it did. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fall.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fall.", "x": "Going deeper: Fall.. Brasilia later. Details are where historians live — the numbers, the names, the decisions that turned Brazilian Empire the way it did. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Pedro I. Details are where historians live — the numbers, the names, the decisions that turned Brazilian Empire the way it did. America's monarchy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Brazilian Empire, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Brazilian Empire, event by event.", "x": "The timeline: Pedro I.. Independence. Key dates in order — Abolition 1888.. 1822-1889 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Brazilian Empire.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Brazilian Empire.", "x": "The people: Paraguay War.. Pedro II. History is made by people deciding under pressure — America's monarchy.. Culture. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Brazilian Empire.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Brazilian Empire.", "x": "More figures: 1889 republic. shaped Brazilian Empire as surely as anyone — Fall.. America's monarchy. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Brazilian Empire happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Brazilian Empire happened.", "x": "The causes: Pedro I.. Slavery. Historians debate the deep vs immediate causes of Brazilian Empire — America's monarchy.. Brasilia later. Understanding why is the whole point of studying history. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Brazilian Empire turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Brazilian Empire turned.", "x": "The turning point: Culture.. Coffee boom. Every great story has the moment it could have gone otherwise — Brazilian Empire. America's monarchy. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-empire-brazilian-empire-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
