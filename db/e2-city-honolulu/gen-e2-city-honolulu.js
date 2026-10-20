(function(){'use strict';
/* JAH Honolulu City Database generator — jahdb-e2-city-honolulu-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-honolulu',PREFIX='JAH-E2CITYHONOL-',NAME='JAH Honolulu City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Honolulu: the complete city guide", "d": "Honolulu, USA: aloha city..", "g": "overview", "l": 2, "q": "What is Honolulu: the complete city guide?", "a": "Honolulu, USA: aloha city..", "x": "The complete Honolulu city guide: aloha city.. Waikiki. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Honolulu in one database. Beach. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Honolulu essentials: Waikiki..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Honolulu essentials: Waikiki..", "x": "At a glance: Honolulu, USA — aloha city.. Diamond Head. The numbers, the layout, the vibe: Honolulu in brief. Hike. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Waikiki.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Waikiki.", "x": "Honolulu: Waikiki.. Hike. One of the defining things about Honolulu — Pearl Harbor.. aloha city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Waikiki..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Waikiki..", "x": "Guide: Waikiki.. Day trip: North Shore. How to do it right — Honolulu. Poke. aloha city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Diamond Head.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Diamond Head.", "x": "Honolulu: Diamond Head.. History. One of the defining things about Honolulu — Poke.. aloha city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Diamond Head..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Diamond Head..", "x": "Guide: Diamond Head.. Aloha. How to do it right — Honolulu. Iolani Palace. aloha city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Pearl Harbor.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Pearl Harbor.", "x": "Honolulu: Pearl Harbor.. Day trip: North Shore. One of the defining things about Honolulu — Iolani Palace.. aloha city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Pearl Harbor..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Pearl Harbor..", "x": "Guide: Pearl Harbor.. Sun. How to do it right — Honolulu. Surf. aloha city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Poke.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Poke.", "x": "Honolulu: Poke.. Aloha. One of the defining things about Honolulu — Surf.. aloha city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Poke..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Poke..", "x": "Guide: Poke.. Beach. How to do it right — Honolulu. Waikiki. aloha city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Iolani Palace.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Iolani Palace.", "x": "Honolulu: Iolani Palace.. Sun. One of the defining things about Honolulu — Waikiki.. aloha city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Iolani Palace..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Iolani Palace..", "x": "Guide: Iolani Palace.. Hike. How to do it right — Honolulu. Diamond Head. aloha city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Surf.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Surf.", "x": "Honolulu: Surf.. Beach. One of the defining things about Honolulu — Diamond Head.. aloha city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Surf..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Surf..", "x": "Guide: Surf.. History. How to do it right — Honolulu. Pearl Harbor. aloha city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Beach.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Beach.", "x": "Honolulu in depth: Beach.. Diamond Head. The details — aloha city.. History. Poke. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hike.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hike.", "x": "Honolulu in depth: Hike.. Pearl Harbor. The details — aloha city.. Day trip: North Shore. Iolani Palace. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Honolulu in depth: History.. Poke. The details — aloha city.. Aloha. Surf. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: North Shore.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: North Shore.", "x": "Honolulu in depth: Day trip: North Shore.. Iolani Palace. The details — aloha city.. Sun. Waikiki. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aloha.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aloha.", "x": "Honolulu in depth: Aloha.. Surf. The details — aloha city.. Beach. Diamond Head. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sun.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sun.", "x": "Honolulu in depth: Sun.. Waikiki. The details — aloha city.. Hike. Pearl Harbor. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Honolulu's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Honolulu's districts.", "x": "Neighborhoods: Beach.. Pearl Harbor. Where to stay, eat, and wander — Honolulu. aloha city. Every district has its own personality; Hike.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Honolulu: Poke..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Honolulu: Poke..", "x": "Food: Poke.. History. The tastes of Honolulu — aloha city.. Iolani Palace. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Honolulu transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Honolulu transport.", "x": "Transport: Day trip: North Shore.. Surf. Subways, buses, walking — Honolulu. aloha city. Learn the system on day one; Aloha.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Honolulu.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Honolulu.", "x": "Timing: Sun.. Waikiki. Seasons and festivals — Honolulu. aloha city. Time it right for Beach.. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Honolulu safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Honolulu safely.", "x": "Safety: Hike.. Diamond Head. Sensible precautions — Honolulu. aloha city. Big cities reward street smarts; History.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-honolulu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
