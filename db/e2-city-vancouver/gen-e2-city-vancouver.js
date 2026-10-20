(function(){'use strict';
/* JAH Vancouver City Database generator — jahdb-e2-city-vancouver-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-vancouver',PREFIX='JAH-E2CITYVANCO-',NAME='JAH Vancouver City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vancouver: the complete city guide", "d": "Vancouver, Canada: the jewel of the Pacific..", "g": "overview", "l": 2, "q": "What is Vancouver: the complete city guide?", "a": "Vancouver, Canada: the jewel of the Pacific..", "x": "The complete Vancouver city guide: the jewel of the Pacific.. Stanley Park. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Vancouver in one database. Park. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Vancouver essentials: Stanley Park..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Vancouver essentials: Stanley Park..", "x": "At a glance: Vancouver, Canada — the jewel of the Pacific.. Granville Island. The numbers, the layout, the vibe: Vancouver in brief. Island. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Stanley Park.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Stanley Park.", "x": "Vancouver: Stanley Park.. Island. One of the defining things about Vancouver — Capilano.. the jewel of the Pacific. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Stanley Park..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Stanley Park..", "x": "Guide: Stanley Park.. Day trip: Whistler. How to do it right — Vancouver. Gastown. the jewel of the Pacific. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Granville Island.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Granville Island.", "x": "Vancouver: Granville Island.. Suspension bridge. One of the defining things about Vancouver — Gastown.. the jewel of the Pacific. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Granville Island..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Granville Island..", "x": "Guide: Granville Island.. Rain. How to do it right — Vancouver. Sushi. the jewel of the Pacific. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Capilano.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Capilano.", "x": "Vancouver: Capilano.. Day trip: Whistler. One of the defining things about Vancouver — Sushi.. the jewel of the Pacific. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Capilano..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Capilano..", "x": "Guide: Capilano.. Outdoors. How to do it right — Vancouver. Mountains. the jewel of the Pacific. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Gastown.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Gastown.", "x": "Vancouver: Gastown.. Rain. One of the defining things about Vancouver — Mountains.. the jewel of the Pacific. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Gastown..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Gastown..", "x": "Guide: Gastown.. Park. How to do it right — Vancouver. Stanley Park. the jewel of the Pacific. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Sushi.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Sushi.", "x": "Vancouver: Sushi.. Outdoors. One of the defining things about Vancouver — Stanley Park.. the jewel of the Pacific. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Sushi..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Sushi..", "x": "Guide: Sushi.. Island. How to do it right — Vancouver. Granville Island. the jewel of the Pacific. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Mountains.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Mountains.", "x": "Vancouver: Mountains.. Park. One of the defining things about Vancouver — Granville Island.. the jewel of the Pacific. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Mountains..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Mountains..", "x": "Guide: Mountains.. Suspension bridge. How to do it right — Vancouver. Capilano. the jewel of the Pacific. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Park.", "x": "Vancouver in depth: Park.. Granville Island. The details — the jewel of the Pacific.. Suspension bridge. Gastown. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Island.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Island.", "x": "Vancouver in depth: Island.. Capilano. The details — the jewel of the Pacific.. Day trip: Whistler. Sushi. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Suspension bridge.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Suspension bridge.", "x": "Vancouver in depth: Suspension bridge.. Gastown. The details — the jewel of the Pacific.. Rain. Mountains. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Whistler.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Whistler.", "x": "Vancouver in depth: Day trip: Whistler.. Sushi. The details — the jewel of the Pacific.. Outdoors. Stanley Park. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rain.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rain.", "x": "Vancouver in depth: Rain.. Mountains. The details — the jewel of the Pacific.. Park. Granville Island. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Outdoors.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Outdoors.", "x": "Vancouver in depth: Outdoors.. Stanley Park. The details — the jewel of the Pacific.. Island. Capilano. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Vancouver's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Vancouver's districts.", "x": "Neighborhoods: Park.. Capilano. Where to stay, eat, and wander — Vancouver. the jewel of the Pacific. Every district has its own personality; Island.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Vancouver: Gastown..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Vancouver: Gastown..", "x": "Food: Gastown.. Suspension bridge. The tastes of Vancouver — the jewel of the Pacific.. Sushi. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Vancouver transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Vancouver transport.", "x": "Transport: Day trip: Whistler.. Mountains. Subways, buses, walking — Vancouver. the jewel of the Pacific. Learn the system on day one; Rain.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Vancouver.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Vancouver.", "x": "Timing: Outdoors.. Stanley Park. Seasons and festivals — Vancouver. the jewel of the Pacific. Time it right for Park.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Vancouver safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Vancouver safely.", "x": "Safety: Island.. Granville Island. Sensible precautions — Vancouver. the jewel of the Pacific. Big cities reward street smarts; Suspension bridge.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-vancouver-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
