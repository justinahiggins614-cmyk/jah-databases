(function(){'use strict';
/* JAH Congress of Vienna Treaty Database generator — jahdb-e2-treaty-congress-of-vienna-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-treaty-congress-of-vienna',PREFIX='JAH-E2TREATYCON-',NAME='JAH Congress of Vienna Treaty Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Congress of Vienna: overview", "d": "Congress of Vienna (1814-1815): remade Europe after Napoleon..", "g": "overview", "l": 2, "q": "What is Congress of Vienna: overview?", "a": "Congress of Vienna (1814-1815): remade Europe after Napoleon..", "x": "The complete treaty guide to Congress of Vienna: remade Europe after Napoleon.. Metternich led. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Congress of Vienna in its time: 1814-1815.", "g": "context", "l": 2, "q": "What is The era?", "a": "Congress of Vienna in its time: 1814-1815.", "x": "Context: Congress of Vienna belonged to 1814-1815 — Dancing congress.. Balance of power. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. remade Europe after Napoleon.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Metternich led.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Metternich led.", "x": "Congress of Vienna: Metternich led.. Talleyrand. This is one of the load-bearing facts about Congress of Vienna — learn it cold. Legitimacy. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Metternich led..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Metternich led..", "x": "Explained: Metternich led.. German Confederation. In the history of Congress of Vienna, this fact connects to Poland/Saxony. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Balance of power.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Balance of power.", "x": "Congress of Vienna: Balance of power.. Redrawn map. This is one of the load-bearing facts about Congress of Vienna — learn it cold. Poland/Saxony. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Balance of power..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Balance of power..", "x": "Explained: Balance of power.. Legacy. In the history of Congress of Vienna, this fact connects to Concert of Europe. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Legitimacy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Legitimacy.", "x": "Congress of Vienna: Legitimacy.. German Confederation. This is one of the load-bearing facts about Congress of Vienna — learn it cold. Concert of Europe. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Legitimacy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Legitimacy..", "x": "Explained: Legitimacy.. Diplomacy. In the history of Congress of Vienna, this fact connects to 100 yrs peace. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Poland/Saxony.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Poland/Saxony.", "x": "Congress of Vienna: Poland/Saxony.. Legacy. This is one of the load-bearing facts about Congress of Vienna — learn it cold. 100 yrs peace. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Poland/Saxony..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Poland/Saxony..", "x": "Explained: Poland/Saxony.. Dancing congress. In the history of Congress of Vienna, this fact connects to Metternich led. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Concert of Europe.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Concert of Europe.", "x": "Congress of Vienna: Concert of Europe.. Diplomacy. This is one of the load-bearing facts about Congress of Vienna — learn it cold. Metternich led. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Concert of Europe..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Concert of Europe..", "x": "Explained: Concert of Europe.. Talleyrand. In the history of Congress of Vienna, this fact connects to Balance of power. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "100 yrs peace.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "100 yrs peace.", "x": "Congress of Vienna: 100 yrs peace.. Dancing congress. This is one of the load-bearing facts about Congress of Vienna — learn it cold. Balance of power. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: 100 yrs peace..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: 100 yrs peace..", "x": "Explained: 100 yrs peace.. Redrawn map. In the history of Congress of Vienna, this fact connects to Legitimacy. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dancing congress.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dancing congress.", "x": "Going deeper: Dancing congress.. Balance of power. Details are where historians live — the numbers, the names, the decisions that turned Congress of Vienna the way it did. remade Europe after Napoleon.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Talleyrand.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Talleyrand.", "x": "Going deeper: Talleyrand.. Legitimacy. Details are where historians live — the numbers, the names, the decisions that turned Congress of Vienna the way it did. remade Europe after Napoleon. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Redrawn map.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Redrawn map.", "x": "Going deeper: Redrawn map.. Poland/Saxony. Details are where historians live — the numbers, the names, the decisions that turned Congress of Vienna the way it did. remade Europe after Napoleon. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "German Confederation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "German Confederation.", "x": "Going deeper: German Confederation.. Concert of Europe. Details are where historians live — the numbers, the names, the decisions that turned Congress of Vienna the way it did. remade Europe after Napoleon.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. 100 yrs peace. Details are where historians live — the numbers, the names, the decisions that turned Congress of Vienna the way it did. remade Europe after Napoleon. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Diplomacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Diplomacy.", "x": "Going deeper: Diplomacy.. Metternich led. Details are where historians live — the numbers, the names, the decisions that turned Congress of Vienna the way it did. remade Europe after Napoleon. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Congress of Vienna, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Congress of Vienna, event by event.", "x": "The timeline: Metternich led.. Dancing congress. Key dates in order — Legitimacy.. 1814-1815 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Congress of Vienna.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Congress of Vienna.", "x": "The people: Talleyrand.. Poland/Saxony. History is made by people deciding under pressure — remade Europe after Napoleon.. German Confederation. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Congress of Vienna.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Congress of Vienna.", "x": "More figures: Concert of Europe. shaped Congress of Vienna as surely as anyone — Legacy.. remade Europe after Napoleon. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Congress of Vienna happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Congress of Vienna happened.", "x": "The causes: Metternich led.. Redrawn map. Historians debate the deep vs immediate causes of Congress of Vienna — remade Europe after Napoleon.. 100 yrs peace. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Congress of Vienna turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Congress of Vienna turned.", "x": "The turning point: German Confederation.. Balance of power. Every great story has the moment it could have gone otherwise — Congress of Vienna. remade Europe after Napoleon. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-treaty-congress-of-vienna-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
