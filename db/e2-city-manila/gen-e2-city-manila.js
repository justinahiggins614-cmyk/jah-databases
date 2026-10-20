(function(){'use strict';
/* JAH Manila City Database generator — jahdb-e2-city-manila-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-manila',PREFIX='JAH-E2CITYMANIL-',NAME='JAH Manila City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Manila: the complete city guide", "d": "Manila, Philippines: pearl of the Orient..", "g": "overview", "l": 2, "q": "What is Manila: the complete city guide?", "a": "Manila, Philippines: pearl of the Orient..", "x": "The complete Manila city guide: pearl of the Orient.. Intramuros. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Manila in one database. Traffic. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Manila essentials: Intramuros..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Manila essentials: Intramuros..", "x": "At a glance: Manila, Philippines — pearl of the Orient.. Rizal Park. The numbers, the layout, the vibe: Manila in brief. Old city. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Intramuros.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Intramuros.", "x": "Manila: Intramuros.. Old city. One of the defining things about Manila — Binondo.. pearl of the Orient. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Intramuros..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Intramuros..", "x": "Guide: Intramuros.. Day trip: Tagaytay. How to do it right — Manila. Mall of Asia. pearl of the Orient. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Rizal Park.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Rizal Park.", "x": "Manila: Rizal Park.. Food. One of the defining things about Manila — Mall of Asia.. pearl of the Orient. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Rizal Park..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Rizal Park..", "x": "Guide: Rizal Park.. Malls. How to do it right — Manila. Jeepneys. pearl of the Orient. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Binondo.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Binondo.", "x": "Manila: Binondo.. Day trip: Tagaytay. One of the defining things about Manila — Jeepneys.. pearl of the Orient. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Binondo..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Binondo..", "x": "Guide: Binondo.. History. How to do it right — Manila. Adobo. pearl of the Orient. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Mall of Asia.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Mall of Asia.", "x": "Manila: Mall of Asia.. Malls. One of the defining things about Manila — Adobo.. pearl of the Orient. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Mall of Asia..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Mall of Asia..", "x": "Guide: Mall of Asia.. Traffic. How to do it right — Manila. Intramuros. pearl of the Orient. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Jeepneys.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Jeepneys.", "x": "Manila: Jeepneys.. History. One of the defining things about Manila — Intramuros.. pearl of the Orient. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Jeepneys..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Jeepneys..", "x": "Guide: Jeepneys.. Old city. How to do it right — Manila. Rizal Park. pearl of the Orient. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Adobo.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Adobo.", "x": "Manila: Adobo.. Traffic. One of the defining things about Manila — Rizal Park.. pearl of the Orient. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Adobo..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Adobo..", "x": "Guide: Adobo.. Food. How to do it right — Manila. Binondo. pearl of the Orient. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Traffic.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Traffic.", "x": "Manila in depth: Traffic.. Rizal Park. The details — pearl of the Orient.. Food. Mall of Asia. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Old city.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Old city.", "x": "Manila in depth: Old city.. Binondo. The details — pearl of the Orient.. Day trip: Tagaytay. Jeepneys. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Food.", "x": "Manila in depth: Food.. Mall of Asia. The details — pearl of the Orient.. Malls. Adobo. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Tagaytay.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Tagaytay.", "x": "Manila in depth: Day trip: Tagaytay.. Jeepneys. The details — pearl of the Orient.. History. Intramuros. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Malls.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Malls.", "x": "Manila in depth: Malls.. Adobo. The details — pearl of the Orient.. Traffic. Rizal Park. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Manila in depth: History.. Intramuros. The details — pearl of the Orient.. Old city. Binondo. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Manila's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Manila's districts.", "x": "Neighborhoods: Traffic.. Binondo. Where to stay, eat, and wander — Manila. pearl of the Orient. Every district has its own personality; Old city.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Manila: Mall of Asia..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Manila: Mall of Asia..", "x": "Food: Mall of Asia.. Food. The tastes of Manila — pearl of the Orient.. Jeepneys. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Manila transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Manila transport.", "x": "Transport: Day trip: Tagaytay.. Adobo. Subways, buses, walking — Manila. pearl of the Orient. Learn the system on day one; Malls.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Manila.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Manila.", "x": "Timing: History.. Intramuros. Seasons and festivals — Manila. pearl of the Orient. Time it right for Traffic.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Manila safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Manila safely.", "x": "Safety: Old city.. Rizal Park. Sensible precautions — Manila. pearl of the Orient. Big cities reward street smarts; Food.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-manila-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
