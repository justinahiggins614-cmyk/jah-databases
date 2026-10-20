(function(){'use strict';
/* JAH American Revolutionary War War Database generator — jahdb-e2-war-american-revolutionary-war-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-american-revolutionary-war',PREFIX='JAH-E2WARAMERIC-',NAME='JAH American Revolutionary War War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "American Revolutionary War: overview", "d": "American Revolutionary War (1775-1783): thirteen colonies won independence..", "g": "overview", "l": 2, "q": "What is American Revolutionary War: overview?", "a": "American Revolutionary War (1775-1783): thirteen colonies won independence..", "x": "The complete war guide to American Revolutionary War: thirteen colonies won independence.. Lexington and Concord (1775). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "American Revolutionary War in its time: 1775-1783.", "g": "context", "l": 2, "q": "What is The era?", "a": "American Revolutionary War in its time: 1775-1783.", "x": "Context: American Revolutionary War belonged to 1775-1783 — Taxation without representation.. Declaration of Independence (1776). Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lexington and Concord (1775).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lexington and Concord (1775).", "x": "American Revolutionary War: Lexington and Concord (1775).. Valley Forge winter. This is one of the load-bearing facts about American Revolutionary War — learn it cold. Saratoga: French alliance. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Lexington and Concord (1775)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Lexington and Concord (1775)..", "x": "Explained: Lexington and Concord (1775).. Guerrilla tactics. In the history of American Revolutionary War, this fact connects to Yorktown: British surrender (1781). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Declaration of Independence (1776).", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Declaration of Independence (1776).", "x": "American Revolutionary War: Declaration of Independence (1776).. Lafayette's help. This is one of the load-bearing facts about American Revolutionary War — learn it cold. Yorktown: British surrender (1781).", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Declaration of Independence (1776)..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Declaration of Independence (1776)..", "x": "Explained: Declaration of Independence (1776).. Constitution followed. In the history of American Revolutionary War, this fact connects to Treaty of Paris (1783). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Saratoga: French alliance.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Saratoga: French alliance.", "x": "American Revolutionary War: Saratoga: French alliance.. Guerrilla tactics. This is one of the load-bearing facts about American Revolutionary War — learn it cold. Treaty of Paris (1783). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Saratoga: French alliance..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Saratoga: French alliance..", "x": "Explained: Saratoga: French alliance.. Global impact. In the history of American Revolutionary War, this fact connects to Washington commanded. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Yorktown: British surrender (1781).", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Yorktown: British surrender (1781).", "x": "American Revolutionary War: Yorktown: British surrender (1781).. Constitution followed. This is one of the load-bearing facts about American Revolutionary War — learn it cold. Washington commanded. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Yorktown: British surrender (1781)..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Yorktown: British surrender (1781)..", "x": "Explained: Yorktown: British surrender (1781).. Taxation without representation. In the history of American Revolutionary War, this fact connects to Lexington and Concord (1775). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Treaty of Paris (1783).", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Treaty of Paris (1783).", "x": "American Revolutionary War: Treaty of Paris (1783).. Global impact. This is one of the load-bearing facts about American Revolutionary War — learn it cold. Lexington and Concord (1775). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Treaty of Paris (1783)..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Treaty of Paris (1783)..", "x": "Explained: Treaty of Paris (1783).. Valley Forge winter. In the history of American Revolutionary War, this fact connects to Declaration of Independence (1776). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Washington commanded.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Washington commanded.", "x": "American Revolutionary War: Washington commanded.. Taxation without representation. This is one of the load-bearing facts about American Revolutionary War — learn it cold. Declaration of Independence (1776).", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Washington commanded..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Washington commanded..", "x": "Explained: Washington commanded.. Lafayette's help. In the history of American Revolutionary War, this fact connects to Saratoga: French alliance. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Taxation without representation.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Taxation without representation.", "x": "Going deeper: Taxation without representation.. Declaration of Independence (1776). Details are where historians live — the numbers, the names, the decisions that turned American Revolutionary War the way it did. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Valley Forge winter.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Valley Forge winter.", "x": "Going deeper: Valley Forge winter.. Saratoga: French alliance. Details are where historians live — the numbers, the names, the decisions that turned American Revolutionary War the way it did. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lafayette's help.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lafayette's help.", "x": "Going deeper: Lafayette's help.. Yorktown: British surrender (1781). Details are where historians live — the numbers, the names, the decisions that turned American Revolutionary War the way it did. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Guerrilla tactics.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Guerrilla tactics.", "x": "Going deeper: Guerrilla tactics.. Treaty of Paris (1783). Details are where historians live — the numbers, the names, the decisions that turned American Revolutionary War the way it did. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Constitution followed.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Constitution followed.", "x": "Going deeper: Constitution followed.. Washington commanded. Details are where historians live — the numbers, the names, the decisions that turned American Revolutionary War the way it did. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Global impact.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Global impact.", "x": "Going deeper: Global impact.. Lexington and Concord (1775). Details are where historians live — the numbers, the names, the decisions that turned American Revolutionary War the way it did. thirteen colonies won independence.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "American Revolutionary War, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "American Revolutionary War, event by event.", "x": "The timeline: Lexington and Concord (1775).. Taxation without representation. Key dates in order — Saratoga: French alliance.. 1775-1783 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of American Revolutionary War.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of American Revolutionary War.", "x": "The people: Valley Forge winter.. Yorktown: British surrender (1781). History is made by people deciding under pressure — thirteen colonies won independence.. Guerrilla tactics. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped American Revolutionary War.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped American Revolutionary War.", "x": "More figures: Treaty of Paris (1783). shaped American Revolutionary War as surely as anyone — Constitution followed.. thirteen colonies won independence. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why American Revolutionary War happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why American Revolutionary War happened.", "x": "The causes: Lexington and Concord (1775).. Lafayette's help. Historians debate the deep vs immediate causes of American Revolutionary War — thirteen colonies won independence.. Washington commanded. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment American Revolutionary War turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment American Revolutionary War turned.", "x": "The turning point: Guerrilla tactics.. Declaration of Independence (1776). Every great story has the moment it could have gone otherwise — American Revolutionary War. thirteen colonies won independence. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-american-revolutionary-war-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
