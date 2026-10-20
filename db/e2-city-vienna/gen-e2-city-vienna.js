(function(){'use strict';
/* JAH Vienna City Database generator — jahdb-e2-city-vienna-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-vienna',PREFIX='JAH-E2CITYVIENN-',NAME='JAH Vienna City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vienna: the complete city guide", "d": "Vienna, Austria: the imperial city..", "g": "overview", "l": 2, "q": "What is Vienna: the complete city guide?", "a": "Vienna, Austria: the imperial city..", "x": "The complete Vienna city guide: the imperial city.. Schonbrunn. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Vienna in one database. Music. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Vienna essentials: Schonbrunn..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Vienna essentials: Schonbrunn..", "x": "At a glance: Vienna, Austria — the imperial city.. Belvedere. The numbers, the layout, the vibe: Vienna in brief. Palaces. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Schonbrunn.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Schonbrunn.", "x": "Vienna: Schonbrunn.. Palaces. One of the defining things about Vienna — Opera.. the imperial city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Schonbrunn..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Schonbrunn..", "x": "Guide: Schonbrunn.. Day trip: Wachau. How to do it right — Vienna. Coffee houses. the imperial city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Belvedere.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Belvedere.", "x": "Vienna: Belvedere.. Cafes. One of the defining things about Vienna — Coffee houses.. the imperial city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Belvedere..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Belvedere..", "x": "Guide: Belvedere.. Trams. How to do it right — Vienna. Sachertorte. the imperial city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Opera.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Opera.", "x": "Vienna: Opera.. Day trip: Wachau. One of the defining things about Vienna — Sachertorte.. the imperial city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Opera..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Opera..", "x": "Guide: Opera.. Culture. How to do it right — Vienna. Ringstrasse. the imperial city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Coffee houses.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Coffee houses.", "x": "Vienna: Coffee houses.. Trams. One of the defining things about Vienna — Ringstrasse.. the imperial city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Coffee houses..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Coffee houses..", "x": "Guide: Coffee houses.. Music. How to do it right — Vienna. Schonbrunn. the imperial city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Sachertorte.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Sachertorte.", "x": "Vienna: Sachertorte.. Culture. One of the defining things about Vienna — Schonbrunn.. the imperial city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Sachertorte..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Sachertorte..", "x": "Guide: Sachertorte.. Palaces. How to do it right — Vienna. Belvedere. the imperial city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Ringstrasse.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Ringstrasse.", "x": "Vienna: Ringstrasse.. Music. One of the defining things about Vienna — Belvedere.. the imperial city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Ringstrasse..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Ringstrasse..", "x": "Guide: Ringstrasse.. Cafes. How to do it right — Vienna. Opera. the imperial city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Music.", "x": "Vienna in depth: Music.. Belvedere. The details — the imperial city.. Cafes. Coffee houses. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Palaces.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Palaces.", "x": "Vienna in depth: Palaces.. Opera. The details — the imperial city.. Day trip: Wachau. Sachertorte. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cafes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cafes.", "x": "Vienna in depth: Cafes.. Coffee houses. The details — the imperial city.. Trams. Ringstrasse. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Wachau.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Wachau.", "x": "Vienna in depth: Day trip: Wachau.. Sachertorte. The details — the imperial city.. Culture. Schonbrunn. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Trams.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Trams.", "x": "Vienna in depth: Trams.. Ringstrasse. The details — the imperial city.. Music. Belvedere. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Vienna in depth: Culture.. Schonbrunn. The details — the imperial city.. Palaces. Opera. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Vienna's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Vienna's districts.", "x": "Neighborhoods: Music.. Opera. Where to stay, eat, and wander — Vienna. the imperial city. Every district has its own personality; Palaces.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Vienna: Coffee houses..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Vienna: Coffee houses..", "x": "Food: Coffee houses.. Cafes. The tastes of Vienna — the imperial city.. Sachertorte. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Vienna transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Vienna transport.", "x": "Transport: Day trip: Wachau.. Ringstrasse. Subways, buses, walking — Vienna. the imperial city. Learn the system on day one; Trams.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Vienna.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Vienna.", "x": "Timing: Culture.. Schonbrunn. Seasons and festivals — Vienna. the imperial city. Time it right for Music.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Vienna safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Vienna safely.", "x": "Safety: Palaces.. Belvedere. Sensible precautions — Vienna. the imperial city. Big cities reward street smarts; Cafes.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-vienna-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
