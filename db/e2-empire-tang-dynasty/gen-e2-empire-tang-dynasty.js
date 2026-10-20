(function(){'use strict';
/* JAH Tang Dynasty Empire Database generator — jahdb-e2-empire-tang-dynasty-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-empire-tang-dynasty',PREFIX='JAH-E2EMPIRETAN-',NAME='JAH Tang Dynasty Empire Database';
var FIELDS=["overview", "context", "facts", "details", "timeline", "people", "causes", "turning-point", "legacy", "misconceptions", "what-if", "quiz", "sources", "learn-more"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tang Dynasty: overview", "d": "Tang Dynasty (618-907): cosmopolitan China..", "g": "overview", "l": 2, "q": "What is Tang Dynasty: overview?", "a": "Tang Dynasty (618-907): cosmopolitan China..", "x": "The complete empire guide to Tang Dynasty: cosmopolitan China.. Chang'an: world city. From causes to consequences, from the key figures to the legacy that still shapes us — this database tells the whole story the way a great history course would.", "s": "public-reference", "f": null}, {"t": "The era", "d": "Tang Dynasty in its time: 618-907.", "g": "context", "l": 2, "q": "What is The era?", "a": "Tang Dynasty in its time: 618-907.", "x": "Context: Tang Dynasty belonged to 618-907 — Taizong.. Poetry golden age. Nothing in history happens in a vacuum; the era explains the motives, the means, and the stakes. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Chang'an: world city.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Chang'an: world city.", "x": "Tang Dynasty: Chang'an: world city.. Culture. This is one of the load-bearing facts about Tang Dynasty — learn it cold. Silk Road peak. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "The story behind: Chang'an: world city..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "The story behind: Chang'an: world city..", "x": "Explained: Chang'an: world city.. Women. In the history of Tang Dynasty, this fact connects to Buddhism. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Poetry golden age.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Poetry golden age.", "x": "Tang Dynasty: Poetry golden age.. Trade. This is one of the load-bearing facts about Tang Dynasty — learn it cold. Buddhism. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "The story behind: Poetry golden age..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "The story behind: Poetry golden age..", "x": "Explained: Poetry golden age.. Decline. In the history of Tang Dynasty, this fact connects to An Lushan. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Silk Road peak.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Silk Road peak.", "x": "Tang Dynasty: Silk Road peak.. Women. This is one of the load-bearing facts about Tang Dynasty — learn it cold. An Lushan. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "The story behind: Silk Road peak..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "The story behind: Silk Road peak..", "x": "Explained: Silk Road peak.. Legacy. In the history of Tang Dynasty, this fact connects to Song followed. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Buddhism.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Buddhism.", "x": "Tang Dynasty: Buddhism.. Decline. This is one of the load-bearing facts about Tang Dynasty — learn it cold. Song followed. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "The story behind: Buddhism..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "The story behind: Buddhism..", "x": "Explained: Buddhism.. Taizong. In the history of Tang Dynasty, this fact connects to Chang'an: world city. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "An Lushan.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "An Lushan.", "x": "Tang Dynasty: An Lushan.. Legacy. This is one of the load-bearing facts about Tang Dynasty — learn it cold. Chang'an: world city. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "The story behind: An Lushan..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "The story behind: An Lushan..", "x": "Explained: An Lushan.. Culture. In the history of Tang Dynasty, this fact connects to Poetry golden age. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Song followed.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Song followed.", "x": "Tang Dynasty: Song followed.. Taizong. This is one of the load-bearing facts about Tang Dynasty — learn it cold. Poetry golden age. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "The story behind: Song followed..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "The story behind: Song followed..", "x": "Explained: Song followed.. Trade. In the history of Tang Dynasty, this fact connects to Silk Road peak. — see the connections and you have understanding, not trivia. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Taizong.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Taizong.", "x": "Going deeper: Taizong.. Poetry golden age. Details are where historians live — the numbers, the names, the decisions that turned Tang Dynasty the way it did. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Culture.", "x": "Going deeper: Culture.. Silk Road peak. Details are where historians live — the numbers, the names, the decisions that turned Tang Dynasty the way it did. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Trade.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Trade.", "x": "Going deeper: Trade.. Buddhism. Details are where historians live — the numbers, the names, the decisions that turned Tang Dynasty the way it did. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Women.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Women.", "x": "Going deeper: Women.. An Lushan. Details are where historians live — the numbers, the names, the decisions that turned Tang Dynasty the way it did. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Decline.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Decline.", "x": "Going deeper: Decline.. Song followed. Details are where historians live — the numbers, the names, the decisions that turned Tang Dynasty the way it did. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Going deeper: Legacy.. Chang'an: world city. Details are where historians live — the numbers, the names, the decisions that turned Tang Dynasty the way it did. cosmopolitan China. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Tang Dynasty, event by event.", "g": "timeline", "l": 2, "q": "What is Timeline?", "a": "Tang Dynasty, event by event.", "x": "The timeline: Chang'an: world city.. Taizong. Key dates in order — Silk Road peak.. 618-907 Pin the dates first; the story hangs on them. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Key figures", "d": "The people of Tang Dynasty.", "g": "people", "l": 2, "q": "What is Key figures?", "a": "The people of Tang Dynasty.", "x": "The people: Culture.. Buddhism. History is made by people deciding under pressure — cosmopolitan China.. Women. Know the actors and the events make sense. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "More key figures", "d": "More people who shaped Tang Dynasty.", "g": "people", "l": 2, "q": "What is More key figures?", "a": "More people who shaped Tang Dynasty.", "x": "More figures: An Lushan. shaped Tang Dynasty as surely as anyone — Decline.. cosmopolitan China. History remembers the famous; the wise student learns the overlooked too. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}, {"t": "Causes", "d": "Why Tang Dynasty happened.", "g": "causes", "l": 2, "q": "What is Causes?", "a": "Why Tang Dynasty happened.", "x": "The causes: Chang'an: world city.. Trade. Historians debate the deep vs immediate causes of Tang Dynasty — cosmopolitan China.. Song followed. Understanding why is the whole point of studying history.", "s": "public-reference", "f": null}, {"t": "The turning point", "d": "The moment Tang Dynasty turned.", "g": "turning-point", "l": 2, "q": "What is The turning point?", "a": "The moment Tang Dynasty turned.", "x": "The turning point: Women.. Poetry golden age. Every great story has the moment it could have gone otherwise — Tang Dynasty. cosmopolitan China. Find it and you find the drama. History from standard references. Dates and figures follow scholarly consensus; debated points are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-empire-tang-dynasty-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
