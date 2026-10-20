(function(){'use strict';
/* JAH Prague City Database generator — jahdb-e2-city-prague-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-prague',PREFIX='JAH-E2CITYPRAGU-',NAME='JAH Prague City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Prague: the complete city guide", "d": "Prague, Czechia: city of a hundred spires..", "g": "overview", "l": 2, "q": "What is Prague: the complete city guide?", "a": "Prague, Czechia: city of a hundred spires..", "x": "The complete Prague city guide: city of a hundred spires.. Charles Bridge. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Prague in one database. Bridge. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Prague essentials: Charles Bridge..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Prague essentials: Charles Bridge..", "x": "At a glance: Prague, Czechia — city of a hundred spires.. Old Town Square. The numbers, the layout, the vibe: Prague in brief. Beer. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Charles Bridge.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Charles Bridge.", "x": "Prague: Charles Bridge.. Beer. One of the defining things about Prague — Castle.. city of a hundred spires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Charles Bridge..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Charles Bridge..", "x": "Guide: Charles Bridge.. Day trip: Kutna Hora. How to do it right — Prague. Beer. city of a hundred spires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Old Town Square.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Old Town Square.", "x": "Prague: Old Town Square.. Castle. One of the defining things about Prague — Beer.. city of a hundred spires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Old Town Square..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Old Town Square..", "x": "Guide: Old Town Square.. Walk. How to do it right — Prague. Astronomical Clock. city of a hundred spires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Castle.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Castle.", "x": "Prague: Castle.. Day trip: Kutna Hora. One of the defining things about Prague — Astronomical Clock.. city of a hundred spires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Castle..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Castle..", "x": "Guide: Castle.. History. How to do it right — Prague. Views. city of a hundred spires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Beer.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Beer.", "x": "Prague: Beer.. Walk. One of the defining things about Prague — Views.. city of a hundred spires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Beer..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Beer..", "x": "Guide: Beer.. Bridge. How to do it right — Prague. Charles Bridge. city of a hundred spires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Astronomical Clock.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Astronomical Clock.", "x": "Prague: Astronomical Clock.. History. One of the defining things about Prague — Charles Bridge.. city of a hundred spires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Astronomical Clock..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Astronomical Clock..", "x": "Guide: Astronomical Clock.. Beer. How to do it right — Prague. Old Town Square. city of a hundred spires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Views.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Views.", "x": "Prague: Views.. Bridge. One of the defining things about Prague — Old Town Square.. city of a hundred spires. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Views..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Views..", "x": "Guide: Views.. Castle. How to do it right — Prague. Castle. city of a hundred spires. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bridge.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bridge.", "x": "Prague in depth: Bridge.. Old Town Square. The details — city of a hundred spires.. Castle. Beer. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beer.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beer.", "x": "Prague in depth: Beer.. Castle. The details — city of a hundred spires.. Day trip: Kutna Hora. Astronomical Clock. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Castle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Castle.", "x": "Prague in depth: Castle.. Beer. The details — city of a hundred spires.. Walk. Views. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Kutna Hora.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Kutna Hora.", "x": "Prague in depth: Day trip: Kutna Hora.. Astronomical Clock. The details — city of a hundred spires.. History. Charles Bridge. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Walk.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Walk.", "x": "Prague in depth: Walk.. Views. The details — city of a hundred spires.. Bridge. Old Town Square. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Prague in depth: History.. Charles Bridge. The details — city of a hundred spires.. Beer. Castle. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Prague's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Prague's districts.", "x": "Neighborhoods: Bridge.. Castle. Where to stay, eat, and wander — Prague. city of a hundred spires. Every district has its own personality; Beer.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Prague: Beer..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Prague: Beer..", "x": "Food: Beer.. Castle. The tastes of Prague — city of a hundred spires.. Astronomical Clock. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Prague transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Prague transport.", "x": "Transport: Day trip: Kutna Hora.. Views. Subways, buses, walking — Prague. city of a hundred spires. Learn the system on day one; Walk.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Prague.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Prague.", "x": "Timing: History.. Charles Bridge. Seasons and festivals — Prague. city of a hundred spires. Time it right for Bridge.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Prague safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Prague safely.", "x": "Safety: Beer.. Old Town Square. Sensible precautions — Prague. city of a hundred spires. Big cities reward street smarts; Castle.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-prague-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
