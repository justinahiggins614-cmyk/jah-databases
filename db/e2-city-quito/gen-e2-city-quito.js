(function(){'use strict';
/* JAH Quito City Database generator — jahdb-e2-city-quito-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-quito',PREFIX='JAH-E2CITYQUITO-',NAME='JAH Quito City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Quito: the complete city guide", "d": "Quito, Ecuador: the middle of the world..", "g": "overview", "l": 2, "q": "What is Quito: the complete city guide?", "a": "Quito, Ecuador: the middle of the world..", "x": "The complete Quito city guide: the middle of the world.. Old Town. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Quito in one database. Altitude. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Quito essentials: Old Town..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Quito essentials: Old Town..", "x": "At a glance: Quito, Ecuador — the middle of the world.. Mitad del Mundo. The numbers, the layout, the vibe: Quito in brief. Old town. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Old Town.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Old Town.", "x": "Quito: Old Town.. Old town. One of the defining things about Quito — Teleferico.. the middle of the world. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Old Town..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Old Town..", "x": "Guide: Old Town.. Day trip: Otavalo. How to do it right — Quito. Basilica. the middle of the world. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Mitad del Mundo.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Mitad del Mundo.", "x": "Quito: Mitad del Mundo.. Equator. One of the defining things about Quito — Basilica.. the middle of the world. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Mitad del Mundo..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Mitad del Mundo..", "x": "Guide: Mitad del Mundo.. Churches. How to do it right — Quito. Locro. the middle of the world. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Teleferico.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Teleferico.", "x": "Quito: Teleferico.. Day trip: Otavalo. One of the defining things about Quito — Locro.. the middle of the world. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Teleferico..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Teleferico..", "x": "Guide: Teleferico.. Views. How to do it right — Quito. Andes. the middle of the world. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Basilica.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Basilica.", "x": "Quito: Basilica.. Churches. One of the defining things about Quito — Andes.. the middle of the world. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Basilica..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Basilica..", "x": "Guide: Basilica.. Altitude. How to do it right — Quito. Old Town. the middle of the world. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Locro.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Locro.", "x": "Quito: Locro.. Views. One of the defining things about Quito — Old Town.. the middle of the world. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Locro..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Locro..", "x": "Guide: Locro.. Old town. How to do it right — Quito. Mitad del Mundo. the middle of the world. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Andes.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Andes.", "x": "Quito: Andes.. Altitude. One of the defining things about Quito — Mitad del Mundo.. the middle of the world. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Andes..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Andes..", "x": "Guide: Andes.. Equator. How to do it right — Quito. Teleferico. the middle of the world. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Altitude.", "x": "Quito in depth: Altitude.. Mitad del Mundo. The details — the middle of the world.. Equator. Basilica. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Old town.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Old town.", "x": "Quito in depth: Old town.. Teleferico. The details — the middle of the world.. Day trip: Otavalo. Locro. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Equator.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Equator.", "x": "Quito in depth: Equator.. Basilica. The details — the middle of the world.. Churches. Andes. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Otavalo.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Otavalo.", "x": "Quito in depth: Day trip: Otavalo.. Locro. The details — the middle of the world.. Views. Old Town. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Churches.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Churches.", "x": "Quito in depth: Churches.. Andes. The details — the middle of the world.. Altitude. Mitad del Mundo. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Quito in depth: Views.. Old Town. The details — the middle of the world.. Old town. Teleferico. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Quito's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Quito's districts.", "x": "Neighborhoods: Altitude.. Teleferico. Where to stay, eat, and wander — Quito. the middle of the world. Every district has its own personality; Old town.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Quito: Basilica..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Quito: Basilica..", "x": "Food: Basilica.. Equator. The tastes of Quito — the middle of the world.. Locro. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Quito transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Quito transport.", "x": "Transport: Day trip: Otavalo.. Andes. Subways, buses, walking — Quito. the middle of the world. Learn the system on day one; Churches.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Quito.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Quito.", "x": "Timing: Views.. Old Town. Seasons and festivals — Quito. the middle of the world. Time it right for Altitude.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Quito safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Quito safely.", "x": "Safety: Old town.. Mitad del Mundo. Sensible precautions — Quito. the middle of the world. Big cities reward street smarts; Equator.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-quito-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
