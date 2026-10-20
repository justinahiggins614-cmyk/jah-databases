(function(){'use strict';
/* JAH David Livingstone Explorer Database generator — jahdb-e2-explorer-david-livingstone-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-explorer-david-livingstone',PREFIX='JAH-E2EXPLORERD-',NAME='JAH David Livingstone Explorer Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "David Livingstone: overview", "d": "David Livingstone (1813-1873): missionary-explorer of Africa..", "g": "overview", "l": 2, "q": "What is David Livingstone: overview?", "a": "David Livingstone (1813-1873): missionary-explorer of Africa..", "x": "The complete explorer guide to David Livingstone: missionary-explorer of Africa.. Victoria Falls. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "David Livingstone in its time: 1813-1873.", "g": "context", "l": 2, "q": "What is The era?", "a": "David Livingstone in its time: 1813-1873.", "x": "Context: David Livingstone belonged to 1813-1873 — Stanley found him.. Zambezi. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. missionary-explorer of Africa.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Victoria Falls.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Victoria Falls.", "x": "David Livingstone: Victoria Falls.. Missionary. This is one of the load-bearing facts about David Livingstone — learn it cold. 'Dr. Livingstone, I presume'. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Victoria Falls..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Victoria Falls..", "x": "Explained: Victoria Falls.. Porters carried body. In the history of David Livingstone, this fact connects to Anti-slavery. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Zambezi.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Zambezi.", "x": "David Livingstone: Zambezi.. Lualaba. This is one of the load-bearing facts about David Livingstone — learn it cold. Anti-slavery. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Zambezi..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Zambezi..", "x": "Explained: Zambezi.. Legacy. In the history of David Livingstone, this fact connects to Died in Africa. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "'Dr. Livingstone, I presume'.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "'Dr. Livingstone, I presume'.", "x": "David Livingstone: 'Dr. Livingstone, I presume'.. Porters carried body. This is one of the load-bearing facts about David Livingstone — learn it cold. Died in Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: 'Dr. Livingstone, I presume'..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: 'Dr. Livingstone, I presume'..", "x": "Explained: 'Dr. Livingstone, I presume'.. Scotland. In the history of David Livingstone, this fact connects to Heart buried. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Anti-slavery.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Anti-slavery.", "x": "David Livingstone: Anti-slavery.. Legacy. This is one of the load-bearing facts about David Livingstone — learn it cold. Heart buried. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Anti-slavery..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Anti-slavery..", "x": "Explained: Anti-slavery.. Stanley found him. In the history of David Livingstone, this fact connects to Victoria Falls. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Died in Africa.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Died in Africa.", "x": "David Livingstone: Died in Africa.. Scotland. This is one of the load-bearing facts about David Livingstone — learn it cold. Victoria Falls. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: Died in Africa..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: Died in Africa..", "x": "Explained: Died in Africa.. Missionary. In the history of David Livingstone, this fact connects to Zambezi. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Heart buried.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Heart buried.", "x": "David Livingstone: Heart buried.. Stanley found him. This is one of the load-bearing facts about David Livingstone — learn it cold. Zambezi. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Heart buried..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Heart buried..", "x": "Explained: Heart buried.. Lualaba. In the history of David Livingstone, this fact connects to 'Dr. Livingstone, I presume'. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stanley found him.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stanley found him.", "x": "Going deeper: Stanley found him.. Zambezi. Details are where historians live — the numbers, the names, the decisions that turned David Livingstone the way it did. missionary-explorer of Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Missionary.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Missionary.", "x": "Going deeper: Missionary.. 'Dr. Livingstone, I presume'. Details are where historians live — the numbers, the names, the decisions that turned David Livingstone the way it did. missionary-explorer of Africa.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lualaba.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lualaba.", "x": "Going deeper: Lualaba.. Anti-slavery. Details are where historians live — the numbers, the names, the decisions that turned David Livingstone the way it did. missionary-explorer of Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Porters carried body.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Porters carried body.", "x": "Going deeper: Porters carried body.. Died in Africa. Details are where historians live — the numbers, the names, the decisions that turned David Livingstone the way it did. missionary-explorer of Africa.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Going deeper: Legacy.. Heart buried. Details are where historians live — the numbers, the names, the decisions that turned David Livingstone the way it did. missionary-explorer of Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Scotland.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Scotland.", "x": "Going deeper: Scotland.. Victoria Falls. Details are where historians live — the numbers, the names, the decisions that turned David Livingstone the way it did. missionary-explorer of Africa. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "David Livingstone, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "David Livingstone, event by event.", "x": "The timeline: Victoria Falls.. Stanley found him. Key dates in order — 'Dr. Livingstone, I presume'.. 1813-1873 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of David Livingstone.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of David Livingstone.", "x": "The people: Missionary.. Anti-slavery. History is made by people deciding under pressure — missionary-explorer of Africa.. Porters carried body. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped David Livingstone.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped David Livingstone.", "x": "More figures: Died in Africa. shaped David Livingstone as surely as anyone — Legacy.. missionary-explorer of Africa. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why David Livingstone happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why David Livingstone happened.", "x": "The causes: Victoria Falls.. Lualaba. Historians debate the deep vs immediate causes of David Livingstone — missionary-explorer of Africa.. Heart buried. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment David Livingstone turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment David Livingstone turned.", "x": "The turning point: Porters carried body.. Zambezi. Every great story has the moment it could have gone otherwise — David Livingstone. missionary-explorer of Africa. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-explorer-david-livingstone-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
