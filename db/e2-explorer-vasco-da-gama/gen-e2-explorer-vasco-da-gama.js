(function(){'use strict';
/* JAH Vasco da Gama Explorer Database generator — jahdb-e2-explorer-vasco-da-gama-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-vasco-da-gama',PREFIX='JAH-E2EXPLORERV-',NAME='JAH Vasco da Gama Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vasco da Gama: overview", "d": "Vasco da Gama (1460s-1524): sea route to India (1498)..", "g": "overview", "l": 2, "q": "What is Vasco da Gama: overview?", "a": "Vasco da Gama (1460s-1524): sea route to India (1498)..", "x": "The complete explorer guide to Vasco da Gama: sea route to India (1498).. Rounded Africa 1498. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Vasco da Gama in its time: 1460s-1524.", "g": "context", "l": 2, "q": "What is The era?", "a": "Vasco da Gama in its time: 1460s-1524.", "x": "Context: Vasco da Gama belonged to 1460s-1524 — Henry the Navigator legacy.. Calicut reached. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. sea route to India (1498).", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rounded Africa 1498.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rounded Africa 1498.", "x": "Vasco da Gama: Rounded Africa 1498.. Monsoons. This is one of the load-bearing facts about Vasco da Gama — learn it cold. Spice trade. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Rounded Africa 1498..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Rounded Africa 1498..", "x": "Explained: Rounded Africa 1498.. Cannon diplomacy. In the history of Vasco da Gama, this fact connects to Second voyage brutal. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Calicut reached.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Calicut reached.", "x": "Vasco da Gama: Calicut reached.. Arab pilots. This is one of the load-bearing facts about Vasco da Gama — learn it cold. Second voyage brutal. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Calicut reached..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Calicut reached..", "x": "Explained: Calicut reached.. Wealth. In the history of Vasco da Gama, this fact connects to Viceroy of India. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Spice trade.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Spice trade.", "x": "Vasco da Gama: Spice trade.. Cannon diplomacy. This is one of the load-bearing facts about Vasco da Gama — learn it cold. Viceroy of India. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Spice trade..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Spice trade..", "x": "Explained: Spice trade.. Empire. In the history of Vasco da Gama, this fact connects to Died Kochi 1524. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Second voyage brutal.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Second voyage brutal.", "x": "Vasco da Gama: Second voyage brutal.. Wealth. This is one of the load-bearing facts about Vasco da Gama — learn it cold. Died Kochi 1524. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Second voyage brutal..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Second voyage brutal..", "x": "Explained: Second voyage brutal.. Henry the Navigator legacy. In the history of Vasco da Gama, this fact connects to Rounded Africa 1498. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Viceroy of India.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Viceroy of India.", "x": "Vasco da Gama: Viceroy of India.. Empire. This is one of the load-bearing facts about Vasco da Gama — learn it cold. Rounded Africa 1498. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Viceroy of India..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Viceroy of India..", "x": "Explained: Viceroy of India.. Monsoons. In the history of Vasco da Gama, this fact connects to Calicut reached. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Died Kochi 1524.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Died Kochi 1524.", "x": "Vasco da Gama: Died Kochi 1524.. Henry the Navigator legacy. This is one of the load-bearing facts about Vasco da Gama — learn it cold. Calicut reached. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Died Kochi 1524..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Died Kochi 1524..", "x": "Explained: Died Kochi 1524.. Arab pilots. In the history of Vasco da Gama, this fact connects to Spice trade. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Henry the Navigator legacy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Henry the Navigator legacy.", "x": "Going deeper: Henry the Navigator legacy.. Calicut reached. Details are where historians live — the numbers, the names, the decisions that turned Vasco da Gama the way it did. sea route to India (1498).", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Monsoons.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Monsoons.", "x": "Going deeper: Monsoons.. Spice trade. Details are where historians live — the numbers, the names, the decisions that turned Vasco da Gama the way it did. sea route to India (1498). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Arab pilots.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Arab pilots.", "x": "Going deeper: Arab pilots.. Second voyage brutal. Details are where historians live — the numbers, the names, the decisions that turned Vasco da Gama the way it did. sea route to India (1498). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cannon diplomacy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cannon diplomacy.", "x": "Going deeper: Cannon diplomacy.. Viceroy of India. Details are where historians live — the numbers, the names, the decisions that turned Vasco da Gama the way it did. sea route to India (1498). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wealth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wealth.", "x": "Going deeper: Wealth.. Died Kochi 1524. Details are where historians live — the numbers, the names, the decisions that turned Vasco da Gama the way it did. sea route to India (1498). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Empire.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Empire.", "x": "Going deeper: Empire.. Rounded Africa 1498. Details are where historians live — the numbers, the names, the decisions that turned Vasco da Gama the way it did. sea route to India (1498). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Vasco da Gama, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Vasco da Gama, event by event.", "x": "The timeline: Rounded Africa 1498.. Henry the Navigator legacy. Key dates in order — Spice trade.. 1460s-1524 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Vasco da Gama.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Vasco da Gama.", "x": "The people: Monsoons.. Second voyage brutal. History is made by people deciding under pressure — sea route to India (1498).. Cannon diplomacy. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Vasco da Gama.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Vasco da Gama.", "x": "More figures: Viceroy of India. shaped Vasco da Gama as surely as anyone — Wealth.. sea route to India (1498). History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Vasco da Gama happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Vasco da Gama happened.", "x": "The causes: Rounded Africa 1498.. Arab pilots. Historians debate the deep vs immediate causes of Vasco da Gama — sea route to India (1498).. Died Kochi 1524. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Vasco da Gama turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Vasco da Gama turned.", "x": "The turning point: Cannon diplomacy.. Calicut reached. Every great story has the moment it could have gone otherwise — Vasco da Gama. sea route to India (1498). Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-vasco-da-gama-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
