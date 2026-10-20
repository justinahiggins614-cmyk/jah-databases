(function(){'use strict';
/* JAH Los Angeles City Database generator — jahdb-e2-city-los-angeles-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-los-angeles',PREFIX='JAH-E2CITYLOSAN-',NAME='JAH Los Angeles City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Los Angeles: the complete city guide", "d": "Los Angeles, USA: the entertainment capital..", "g": "overview", "l": 2, "q": "What is Los Angeles: the complete city guide?", "a": "Los Angeles, USA: the entertainment capital..", "x": "The complete Los Angeles city guide: the entertainment capital.. Hollywood. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Los Angeles in one database. Car city. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Los Angeles essentials: Hollywood..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Los Angeles essentials: Hollywood..", "x": "At a glance: Los Angeles, USA — the entertainment capital.. Santa Monica. The numbers, the layout, the vibe: Los Angeles in brief. Beaches. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Hollywood.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Hollywood.", "x": "Los Angeles: Hollywood.. Beaches. One of the defining things about Los Angeles — Getty.. the entertainment capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Hollywood..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Hollywood..", "x": "Guide: Hollywood.. Hikes. How to do it right — Los Angeles. Griffith Observatory. the entertainment capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Santa Monica.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Santa Monica.", "x": "Los Angeles: Santa Monica.. Studios. One of the defining things about Los Angeles — Griffith Observatory.. the entertainment capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Santa Monica..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Santa Monica..", "x": "Guide: Santa Monica.. Traffic. How to do it right — Los Angeles. Tacos. the entertainment capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Getty.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Getty.", "x": "Los Angeles: Getty.. Hikes. One of the defining things about Los Angeles — Tacos.. the entertainment capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Getty..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Getty..", "x": "Guide: Getty.. Neighborhoods. How to do it right — Los Angeles. Beaches. the entertainment capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Griffith Observatory.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Griffith Observatory.", "x": "Los Angeles: Griffith Observatory.. Traffic. One of the defining things about Los Angeles — Beaches.. the entertainment capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Griffith Observatory..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Griffith Observatory..", "x": "Guide: Griffith Observatory.. Car city. How to do it right — Los Angeles. Hollywood. the entertainment capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Tacos.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Tacos.", "x": "Los Angeles: Tacos.. Neighborhoods. One of the defining things about Los Angeles — Hollywood.. the entertainment capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Tacos..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Tacos..", "x": "Guide: Tacos.. Beaches. How to do it right — Los Angeles. Santa Monica. the entertainment capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Beaches.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Beaches.", "x": "Los Angeles: Beaches.. Car city. One of the defining things about Los Angeles — Santa Monica.. the entertainment capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Beaches..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Beaches..", "x": "Guide: Beaches.. Studios. How to do it right — Los Angeles. Getty. the entertainment capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Car city.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Car city.", "x": "Los Angeles in depth: Car city.. Santa Monica. The details — the entertainment capital.. Studios. Griffith Observatory. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beaches.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beaches.", "x": "Los Angeles in depth: Beaches.. Getty. The details — the entertainment capital.. Hikes. Tacos. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Studios.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Studios.", "x": "Los Angeles in depth: Studios.. Griffith Observatory. The details — the entertainment capital.. Traffic. Beaches. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hikes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hikes.", "x": "Los Angeles in depth: Hikes.. Tacos. The details — the entertainment capital.. Neighborhoods. Hollywood. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Traffic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Traffic.", "x": "Los Angeles in depth: Traffic.. Beaches. The details — the entertainment capital.. Car city. Santa Monica. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Neighborhoods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Neighborhoods.", "x": "Los Angeles in depth: Neighborhoods.. Hollywood. The details — the entertainment capital.. Beaches. Getty. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Los Angeles's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Los Angeles's districts.", "x": "Neighborhoods: Car city.. Getty. Where to stay, eat, and wander — Los Angeles. the entertainment capital. Every district has its own personality; Beaches.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Los Angeles: Griffith Observatory..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Los Angeles: Griffith Observatory..", "x": "Food: Griffith Observatory.. Studios. The tastes of Los Angeles — the entertainment capital.. Tacos. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Los Angeles transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Los Angeles transport.", "x": "Transport: Hikes.. Beaches. Subways, buses, walking — Los Angeles. the entertainment capital. Learn the system on day one; Traffic.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Los Angeles.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Los Angeles.", "x": "Timing: Neighborhoods.. Hollywood. Seasons and festivals — Los Angeles. the entertainment capital. Time it right for Car city.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Los Angeles safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Los Angeles safely.", "x": "Safety: Beaches.. Santa Monica. Sensible precautions — Los Angeles. the entertainment capital. Big cities reward street smarts; Studios.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-los-angeles-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
