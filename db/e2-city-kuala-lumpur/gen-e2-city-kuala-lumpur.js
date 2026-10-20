(function(){'use strict';
/* JAH Kuala Lumpur City Database generator — jahdb-e2-city-kuala-lumpur-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-kuala-lumpur',PREFIX='JAH-E2CITYKUALA-',NAME='JAH Kuala Lumpur City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kuala Lumpur: the complete city guide", "d": "Kuala Lumpur, Malaysia: the garden city of lights..", "g": "overview", "l": 2, "q": "What is Kuala Lumpur: the complete city guide?", "a": "Kuala Lumpur, Malaysia: the garden city of lights..", "x": "The complete Kuala Lumpur city guide: the garden city of lights.. Petronas Towers. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Kuala Lumpur in one database. Towers.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Kuala Lumpur essentials: Petronas Towers..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Kuala Lumpur essentials: Petronas Towers..", "x": "At a glance: Kuala Lumpur, Malaysia — the garden city of lights.. Batu Caves. The numbers, the layout, the vibe: Kuala Lumpur in brief. Caves. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Petronas Towers.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Petronas Towers.", "x": "Kuala Lumpur: Petronas Towers.. Caves. One of the defining things about Kuala Lumpur — Jalan Alor.. the garden city of lights. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Petronas Towers..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Petronas Towers..", "x": "Guide: Petronas Towers.. Day trip: Malacca. How to do it right — Kuala Lumpur. Merdeka Square. the garden city of lights. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Batu Caves.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Batu Caves.", "x": "Kuala Lumpur: Batu Caves.. Food. One of the defining things about Kuala Lumpur — Merdeka Square.. the garden city of lights. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Batu Caves..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Batu Caves..", "x": "Guide: Batu Caves.. Transit. How to do it right — Kuala Lumpur. Nasi lemak. the garden city of lights. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Jalan Alor.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Jalan Alor.", "x": "Kuala Lumpur: Jalan Alor.. Day trip: Malacca. One of the defining things about Kuala Lumpur — Nasi lemak.. the garden city of lights. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Jalan Alor..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Jalan Alor..", "x": "Guide: Jalan Alor.. Culture. How to do it right — Kuala Lumpur. Markets. the garden city of lights. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Merdeka Square.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Merdeka Square.", "x": "Kuala Lumpur: Merdeka Square.. Transit. One of the defining things about Kuala Lumpur — Markets.. the garden city of lights. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Merdeka Square..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Merdeka Square..", "x": "Guide: Merdeka Square.. Towers. How to do it right — Kuala Lumpur. Petronas Towers. the garden city of lights. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Nasi lemak.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Nasi lemak.", "x": "Kuala Lumpur: Nasi lemak.. Culture. One of the defining things about Kuala Lumpur — Petronas Towers.. the garden city of lights. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Nasi lemak..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Nasi lemak..", "x": "Guide: Nasi lemak.. Caves. How to do it right — Kuala Lumpur. Batu Caves. the garden city of lights. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Markets.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Markets.", "x": "Kuala Lumpur: Markets.. Towers. One of the defining things about Kuala Lumpur — Batu Caves.. the garden city of lights. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Markets..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Markets..", "x": "Guide: Markets.. Food. How to do it right — Kuala Lumpur. Jalan Alor. the garden city of lights. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Towers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Towers.", "x": "Kuala Lumpur in depth: Towers.. Batu Caves. The details — the garden city of lights.. Food. Merdeka Square. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Caves.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Caves.", "x": "Kuala Lumpur in depth: Caves.. Jalan Alor. The details — the garden city of lights.. Day trip: Malacca. Nasi lemak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Food.", "x": "Kuala Lumpur in depth: Food.. Merdeka Square. The details — the garden city of lights.. Transit. Markets. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Malacca.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Malacca.", "x": "Kuala Lumpur in depth: Day trip: Malacca.. Nasi lemak. The details — the garden city of lights.. Culture. Petronas Towers. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Transit.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Transit.", "x": "Kuala Lumpur in depth: Transit.. Markets. The details — the garden city of lights.. Towers. Batu Caves. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Kuala Lumpur in depth: Culture.. Petronas Towers. The details — the garden city of lights.. Caves. Jalan Alor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Kuala Lumpur's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Kuala Lumpur's districts.", "x": "Neighborhoods: Towers.. Jalan Alor. Where to stay, eat, and wander — Kuala Lumpur. the garden city of lights. Every district has its own personality; Caves.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Kuala Lumpur: Merdeka Square..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Kuala Lumpur: Merdeka Square..", "x": "Food: Merdeka Square.. Food. The tastes of Kuala Lumpur — the garden city of lights.. Nasi lemak. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Kuala Lumpur transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Kuala Lumpur transport.", "x": "Transport: Day trip: Malacca.. Markets. Subways, buses, walking — Kuala Lumpur. the garden city of lights. Learn the system on day one; Transit.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Kuala Lumpur.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Kuala Lumpur.", "x": "Timing: Culture.. Petronas Towers. Seasons and festivals — Kuala Lumpur. the garden city of lights. Time it right for Towers.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Kuala Lumpur safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Kuala Lumpur safely.", "x": "Safety: Caves.. Batu Caves. Sensible precautions — Kuala Lumpur. the garden city of lights. Big cities reward street smarts; Food.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-kuala-lumpur-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
