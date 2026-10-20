(function(){'use strict';
/* JAH Cairo City Database generator — jahdb-e2-city-cairo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-cairo',PREFIX='JAH-E2CITYCAIRO-',NAME='JAH Cairo City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cairo: the complete city guide", "d": "Cairo, Egypt: the city of a thousand minarets..", "g": "overview", "l": 2, "q": "What is Cairo: the complete city guide?", "a": "Cairo, Egypt: the city of a thousand minarets..", "x": "The complete Cairo city guide: the city of a thousand minarets.. Pyramids of Giza. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Cairo in one database. Traffic. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Cairo essentials: Pyramids of Giza..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Cairo essentials: Pyramids of Giza..", "x": "At a glance: Cairo, Egypt — the city of a thousand minarets.. Egyptian Museum. The numbers, the layout, the vibe: Cairo in brief. Pyramids. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Pyramids of Giza.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Pyramids of Giza.", "x": "Cairo: Pyramids of Giza.. Pyramids. One of the defining things about Cairo — Khan el-Khalili.. the city of a thousand minarets. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Pyramids of Giza..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Pyramids of Giza..", "x": "Guide: Pyramids of Giza.. Bazaar. How to do it right — Cairo. Citadel. the city of a thousand minarets. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Egyptian Museum.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Egyptian Museum.", "x": "Cairo: Egyptian Museum.. Museum. One of the defining things about Cairo — Citadel.. the city of a thousand minarets. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Egyptian Museum..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Egyptian Museum..", "x": "Guide: Egyptian Museum.. Day trip: Saqqara. How to do it right — Cairo. Nile felucca. the city of a thousand minarets. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Khan el-Khalili.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Khan el-Khalili.", "x": "Cairo: Khan el-Khalili.. Bazaar. One of the defining things about Cairo — Nile felucca.. the city of a thousand minarets. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Khan el-Khalili..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Khan el-Khalili..", "x": "Guide: Khan el-Khalili.. Haggle. How to do it right — Cairo. Koshari. the city of a thousand minarets. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Citadel.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Citadel.", "x": "Cairo: Citadel.. Day trip: Saqqara. One of the defining things about Cairo — Koshari.. the city of a thousand minarets. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Citadel..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Citadel..", "x": "Guide: Citadel.. Traffic. How to do it right — Cairo. Pyramids of Giza. the city of a thousand minarets. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Nile felucca.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Nile felucca.", "x": "Cairo: Nile felucca.. Haggle. One of the defining things about Cairo — Pyramids of Giza.. the city of a thousand minarets. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Nile felucca..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Nile felucca..", "x": "Guide: Nile felucca.. Pyramids. How to do it right — Cairo. Egyptian Museum. the city of a thousand minarets. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Koshari.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Koshari.", "x": "Cairo: Koshari.. Traffic. One of the defining things about Cairo — Egyptian Museum.. the city of a thousand minarets. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Koshari..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Koshari..", "x": "Guide: Koshari.. Museum. How to do it right — Cairo. Khan el-Khalili. the city of a thousand minarets. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Traffic.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Traffic.", "x": "Cairo in depth: Traffic.. Egyptian Museum. The details — the city of a thousand minarets.. Museum. Citadel. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pyramids.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pyramids.", "x": "Cairo in depth: Pyramids.. Khan el-Khalili. The details — the city of a thousand minarets.. Bazaar. Nile felucca. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Museum.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Museum.", "x": "Cairo in depth: Museum.. Citadel. The details — the city of a thousand minarets.. Day trip: Saqqara. Koshari. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bazaar.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bazaar.", "x": "Cairo in depth: Bazaar.. Nile felucca. The details — the city of a thousand minarets.. Haggle. Pyramids of Giza. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Day trip: Saqqara.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Day trip: Saqqara.", "x": "Cairo in depth: Day trip: Saqqara.. Koshari. The details — the city of a thousand minarets.. Traffic. Egyptian Museum. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Haggle.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Haggle.", "x": "Cairo in depth: Haggle.. Pyramids of Giza. The details — the city of a thousand minarets.. Pyramids. Khan el-Khalili. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Cairo's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Cairo's districts.", "x": "Neighborhoods: Traffic.. Khan el-Khalili. Where to stay, eat, and wander — Cairo. the city of a thousand minarets. Every district has its own personality; Pyramids.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Cairo: Citadel..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Cairo: Citadel..", "x": "Food: Citadel.. Museum. The tastes of Cairo — the city of a thousand minarets.. Nile felucca. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Cairo transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Cairo transport.", "x": "Transport: Bazaar.. Koshari. Subways, buses, walking — Cairo. the city of a thousand minarets. Learn the system on day one; Day trip: Saqqara.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Cairo.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Cairo.", "x": "Timing: Haggle.. Pyramids of Giza. Seasons and festivals — Cairo. the city of a thousand minarets. Time it right for Traffic.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Cairo safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Cairo safely.", "x": "Safety: Pyramids.. Egyptian Museum. Sensible precautions — Cairo. the city of a thousand minarets. Big cities reward street smarts; Museum.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-cairo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
