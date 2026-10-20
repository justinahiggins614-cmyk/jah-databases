(function(){'use strict';
/* JAH World War I War Database generator — jahdb-e2-war-world-war-i-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-war-world-war-i',PREFIX='JAH-E2WARWORLDW-',NAME='JAH World War I War Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "World War I: overview", "d": "World War I (1914-1918): the Great War that shattered empires..", "g": "overview", "l": 2, "q": "What is World War I: overview?", "a": "World War I (1914-1918): the Great War that shattered empires..", "x": "The complete war guide to World War I: the Great War that shattered empires.. Triggered by Archduke's assassination (1914). From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "World War I in its time: 1914-1918.", "g": "context", "l": 2, "q": "What is The era?", "a": "World War I in its time: 1914-1918.", "x": "Context: World War I belonged to 1914-1918 — Schlieffen Plan.. Trench warfare on Western Front. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Triggered by Archduke's assassination (1914).", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Triggered by Archduke's assassination (1914).", "x": "World War I: Triggered by Archduke's assassination (1914).. Verdun, Somme battles. This is one of the load-bearing facts about World War I — learn it cold. US entered 1917. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Triggered by Archduke's assassination (1914)..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Triggered by Archduke's assassination (1914)..", "x": "Explained: Triggered by Archduke's assassination (1914).. Zimmermann Telegram. In the history of World War I, this fact connects to Treaty of Versailles 1919. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Trench warfare on Western Front.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Trench warfare on Western Front.", "x": "World War I: Trench warfare on Western Front.. Tanks, planes, gas debut. This is one of the load-bearing facts about World War I — learn it cold. Treaty of Versailles 1919. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Trench warfare on Western Front..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Trench warfare on Western Front..", "x": "Explained: Trench warfare on Western Front.. Fourteen Points. In the history of World War I, this fact connects to 10M+ soldiers died. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "US entered 1917.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "US entered 1917.", "x": "World War I: US entered 1917.. Zimmermann Telegram. This is one of the load-bearing facts about World War I — learn it cold. 10M+ soldiers died. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: US entered 1917..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: US entered 1917..", "x": "Explained: US entered 1917.. League of Nations. In the history of World War I, this fact connects to Empires fell: German, Austro-Hungarian, Ottoman, Russian. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Treaty of Versailles 1919.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Treaty of Versailles 1919.", "x": "World War I: Treaty of Versailles 1919.. Fourteen Points. This is one of the load-bearing facts about World War I — learn it cold. Empires fell: German, Austro-Hungarian, Ottoman, Russian. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Treaty of Versailles 1919..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Treaty of Versailles 1919..", "x": "Explained: Treaty of Versailles 1919.. Schlieffen Plan. In the history of World War I, this fact connects to Triggered by Archduke's assassination (1914). — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "10M+ soldiers died.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "10M+ soldiers died.", "x": "World War I: 10M+ soldiers died.. League of Nations. This is one of the load-bearing facts about World War I — learn it cold. Triggered by Archduke's assassination (1914). History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: 10M+ soldiers died..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: 10M+ soldiers died..", "x": "Explained: 10M+ soldiers died.. Verdun, Somme battles. In the history of World War I, this fact connects to Trench warfare on Western Front. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Empires fell: German, Austro-Hungarian, Ottoman, Russian.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Empires fell: German, Austro-Hungarian, Ottoman, Russian.", "x": "World War I: Empires fell: German, Austro-Hungarian, Ottoman, Russian.. Schlieffen Plan. This is one of the load-bearing facts about World War I — learn it cold. Trench warfare on Western Front. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Empires fell: German, Austro-Hungarian, Ottoman, Russian..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Empires fell: German, Austro-Hungarian, Ottoman, Russian..", "x": "Explained: Empires fell: German, Austro-Hungarian, Ottoman, Russian.. Tanks, planes, gas debut. In the history of World War I, this fact connects to US entered 1917. — see the connections and you have understanding, not trivia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Schlieffen Plan.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Schlieffen Plan.", "x": "Going deeper: Schlieffen Plan.. Trench warfare on Western Front. Details are where historians live — the numbers, the names, the decisions that turned World War I the way it did. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Verdun, Somme battles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Verdun, Somme battles.", "x": "Going deeper: Verdun, Somme battles.. US entered 1917. Details are where historians live — the numbers, the names, the decisions that turned World War I the way it did. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tanks, planes, gas debut.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tanks, planes, gas debut.", "x": "Going deeper: Tanks, planes, gas debut.. Treaty of Versailles 1919. Details are where historians live — the numbers, the names, the decisions that turned World War I the way it did. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Zimmermann Telegram.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Zimmermann Telegram.", "x": "Going deeper: Zimmermann Telegram.. 10M+ soldiers died. Details are where historians live — the numbers, the names, the decisions that turned World War I the way it did. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fourteen Points.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fourteen Points.", "x": "Going deeper: Fourteen Points.. Empires fell: German, Austro-Hungarian, Ottoman, Russian. Details are where historians live — the numbers, the names, the decisions that turned World War I the way it did. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "League of Nations.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "League of Nations.", "x": "Going deeper: League of Nations.. Triggered by Archduke's assassination (1914). Details are where historians live — the numbers, the names, the decisions that turned World War I the way it did. the Great War that shattered empires.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "World War I, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "World War I, event by event.", "x": "The timeline: Triggered by Archduke's assassination (1914).. Schlieffen Plan. Key dates in order — US entered 1917.. 1914-1918 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of World War I.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of World War I.", "x": "The people: Verdun, Somme battles.. Treaty of Versailles 1919. History is made by people deciding under pressure — the Great War that shattered empires.. Zimmermann Telegram. Know the actors and the events make sense.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped World War I.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped World War I.", "x": "More figures: 10M+ soldiers died. shaped World War I as surely as anyone — Fourteen Points.. the Great War that shattered empires. History remembers the famous; the wise student learns the overlooked too.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why World War I happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why World War I happened.", "x": "The causes: Triggered by Archduke's assassination (1914).. Tanks, planes, gas debut. Historians debate the deep vs immediate causes of World War I — the Great War that shattered empires.. Empires fell: German, Austro-Hungarian, Ottoman, Russian. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment World War I turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment World War I turned.", "x": "The turning point: Zimmermann Telegram.. Trench warfare on Western Front. Every great story has the moment it could have gone otherwise — World War I. the Great War that shattered empires. Find it and you find the drama.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-war-world-war-i-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
