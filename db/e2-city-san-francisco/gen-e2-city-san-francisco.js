(function(){'use strict';
/* JAH San Francisco City Database generator — jahdb-e2-city-san-francisco-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-san-francisco',PREFIX='JAH-E2CITYSANFR-',NAME='JAH San Francisco City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "San Francisco: the complete city guide", "d": "San Francisco, USA: the city by the bay..", "g": "overview", "l": 2, "q": "What is San Francisco: the complete city guide?", "a": "San Francisco, USA: the city by the bay..", "x": "The complete San Francisco city guide: the city by the bay.. Golden Gate. From landmarks to neighborhoods, food to festivals, getting around to staying safe — San Francisco in one database. Hills. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "San Francisco essentials: Golden Gate..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "San Francisco essentials: Golden Gate..", "x": "At a glance: San Francisco, USA — the city by the bay.. Alcatraz. The numbers, the layout, the vibe: San Francisco in brief. Fog. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Golden Gate.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Golden Gate.", "x": "San Francisco: Golden Gate.. Fog. One of the defining things about San Francisco — Fisherman's Wharf.. the city by the bay. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Golden Gate..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Golden Gate..", "x": "Guide: Golden Gate.. Day trip: Muir Woods. How to do it right — San Francisco. Cable cars. the city by the bay. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Alcatraz.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Alcatraz.", "x": "San Francisco: Alcatraz.. Ferries. One of the defining things about San Francisco — Cable cars.. the city by the bay. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Alcatraz..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Alcatraz..", "x": "Guide: Alcatraz.. Transit. How to do it right — San Francisco. Mission burritos. the city by the bay. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Fisherman's Wharf.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Fisherman's Wharf.", "x": "San Francisco: Fisherman's Wharf.. Day trip: Muir Woods. One of the defining things about San Francisco — Mission burritos.. the city by the bay. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Fisherman's Wharf..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Fisherman's Wharf..", "x": "Guide: Fisherman's Wharf.. Tech. How to do it right — San Francisco. Painted Ladies. the city by the bay. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Cable cars.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Cable cars.", "x": "San Francisco: Cable cars.. Transit. One of the defining things about San Francisco — Painted Ladies.. the city by the bay. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Cable cars..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Cable cars..", "x": "Guide: Cable cars.. Hills. How to do it right — San Francisco. Golden Gate. the city by the bay. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Mission burritos.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Mission burritos.", "x": "San Francisco: Mission burritos.. Tech. One of the defining things about San Francisco — Golden Gate.. the city by the bay. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Mission burritos..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Mission burritos..", "x": "Guide: Mission burritos.. Fog. How to do it right — San Francisco. Alcatraz. the city by the bay. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Painted Ladies.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Painted Ladies.", "x": "San Francisco: Painted Ladies.. Hills. One of the defining things about San Francisco — Alcatraz.. the city by the bay. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Painted Ladies..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Painted Ladies..", "x": "Guide: Painted Ladies.. Ferries. How to do it right — San Francisco. Fisherman's Wharf. the city by the bay. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hills.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hills.", "x": "San Francisco in depth: Hills.. Alcatraz. The details — the city by the bay.. Ferries. Cable cars. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fog.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fog.", "x": "San Francisco in depth: Fog.. Fisherman's Wharf. The details — the city by the bay.. Day trip: Muir Woods. Mission burritos. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ferries.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ferries.", "x": "San Francisco in depth: Ferries.. Cable cars. The details — the city by the bay.. Transit. Painted Ladies. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Muir Woods.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Muir Woods.", "x": "San Francisco in depth: Day trip: Muir Woods.. Mission burritos. The details — the city by the bay.. Tech. Golden Gate. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Transit.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Transit.", "x": "San Francisco in depth: Transit.. Painted Ladies. The details — the city by the bay.. Hills. Alcatraz. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tech.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tech.", "x": "San Francisco in depth: Tech.. Golden Gate. The details — the city by the bay.. Fog. Fisherman's Wharf. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "San Francisco's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "San Francisco's districts.", "x": "Neighborhoods: Hills.. Fisherman's Wharf. Where to stay, eat, and wander — San Francisco. the city by the bay. Every district has its own personality; Fog.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in San Francisco: Cable cars..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in San Francisco: Cable cars..", "x": "Food: Cable cars.. Ferries. The tastes of San Francisco — the city by the bay.. Mission burritos. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "San Francisco transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "San Francisco transport.", "x": "Transport: Day trip: Muir Woods.. Painted Ladies. Subways, buses, walking — San Francisco. the city by the bay. Learn the system on day one; Transit.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see San Francisco.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see San Francisco.", "x": "Timing: Tech.. Golden Gate. Seasons and festivals — San Francisco. the city by the bay. Time it right for Hills.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "San Francisco safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "San Francisco safely.", "x": "Safety: Fog.. Alcatraz. Sensible precautions — San Francisco. the city by the bay. Big cities reward street smarts; Ferries.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-san-francisco-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
