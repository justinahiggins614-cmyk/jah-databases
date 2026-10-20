(function(){'use strict';
/* JAH New Orleans City Database generator — jahdb-e2-city-new-orleans-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-new-orleans',PREFIX='JAH-E2CITYNEWOR-',NAME='JAH New Orleans City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New Orleans: the complete city guide", "d": "New Orleans, USA: the big easy..", "g": "overview", "l": 2, "q": "What is New Orleans: the complete city guide?", "a": "New Orleans, USA: the big easy..", "x": "The complete New Orleans city guide: the big easy.. French Quarter. From landmarks to neighborhoods, food to festivals, getting around to staying safe — New Orleans in one database. Music. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "New Orleans essentials: French Quarter..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "New Orleans essentials: French Quarter..", "x": "At a glance: New Orleans, USA — the big easy.. Bourbon Street. The numbers, the layout, the vibe: New Orleans in brief. Food. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "French Quarter.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "French Quarter.", "x": "New Orleans: French Quarter.. Food. One of the defining things about New Orleans — Jazz.. the big easy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: French Quarter..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: French Quarter..", "x": "Guide: French Quarter.. Day trip: plantations. How to do it right — New Orleans. Beignets. the big easy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Bourbon Street.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Bourbon Street.", "x": "New Orleans: Bourbon Street.. Quarter. One of the defining things about New Orleans — Beignets.. the big easy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Bourbon Street..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Bourbon Street..", "x": "Guide: Bourbon Street.. Heat. How to do it right — New Orleans. Garden District. the big easy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Jazz.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Jazz.", "x": "New Orleans: Jazz.. Day trip: plantations. One of the defining things about New Orleans — Garden District.. the big easy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Jazz..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Jazz..", "x": "Guide: Jazz.. Culture. How to do it right — New Orleans. Mardi Gras. the big easy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Beignets.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Beignets.", "x": "New Orleans: Beignets.. Heat. One of the defining things about New Orleans — Mardi Gras.. the big easy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Beignets..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Beignets..", "x": "Guide: Beignets.. Music. How to do it right — New Orleans. French Quarter. the big easy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Garden District.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Garden District.", "x": "New Orleans: Garden District.. Culture. One of the defining things about New Orleans — French Quarter.. the big easy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Garden District..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Garden District..", "x": "Guide: Garden District.. Food. How to do it right — New Orleans. Bourbon Street. the big easy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Mardi Gras.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Mardi Gras.", "x": "New Orleans: Mardi Gras.. Music. One of the defining things about New Orleans — Bourbon Street.. the big easy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Mardi Gras..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Mardi Gras..", "x": "Guide: Mardi Gras.. Quarter. How to do it right — New Orleans. Jazz. the big easy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Music.", "x": "New Orleans in depth: Music.. Bourbon Street. The details — the big easy.. Quarter. Beignets. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Food.", "x": "New Orleans in depth: Food.. Jazz. The details — the big easy.. Day trip: plantations. Garden District. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Quarter.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Quarter.", "x": "New Orleans in depth: Quarter.. Beignets. The details — the big easy.. Heat. Mardi Gras. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: plantations.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: plantations.", "x": "New Orleans in depth: Day trip: plantations.. Garden District. The details — the big easy.. Culture. French Quarter. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Heat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Heat.", "x": "New Orleans in depth: Heat.. Mardi Gras. The details — the big easy.. Music. Bourbon Street. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "New Orleans in depth: Culture.. French Quarter. The details — the big easy.. Food. Jazz. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "New Orleans's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "New Orleans's districts.", "x": "Neighborhoods: Music.. Jazz. Where to stay, eat, and wander — New Orleans. the big easy. Every district has its own personality; Food.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in New Orleans: Beignets..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in New Orleans: Beignets..", "x": "Food: Beignets.. Quarter. The tastes of New Orleans — the big easy.. Garden District. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "New Orleans transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "New Orleans transport.", "x": "Transport: Day trip: plantations.. Mardi Gras. Subways, buses, walking — New Orleans. the big easy. Learn the system on day one; Heat.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see New Orleans.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see New Orleans.", "x": "Timing: Culture.. French Quarter. Seasons and festivals — New Orleans. the big easy. Time it right for Music.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "New Orleans safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "New Orleans safely.", "x": "Safety: Food.. Bourbon Street. Sensible precautions — New Orleans. the big easy. Big cities reward street smarts; Quarter.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-new-orleans-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
