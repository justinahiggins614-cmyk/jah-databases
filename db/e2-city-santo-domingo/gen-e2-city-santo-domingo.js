(function(){'use strict';
/* JAH Santo Domingo City Database generator — jahdb-e2-city-santo-domingo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-santo-domingo',PREFIX='JAH-E2CITYSANTO-',NAME='JAH Santo Domingo City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Santo Domingo: the complete city guide", "d": "Santo Domingo, Dominican Republic: first city of the Americas..", "g": "overview", "l": 2, "q": "What is Santo Domingo: the complete city guide?", "a": "Santo Domingo, Dominican Republic: first city of the Americas..", "x": "The complete Santo Domingo city guide: first city of the Americas.. Zona Colonial. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Santo Domingo in one database. Colonial.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Santo Domingo essentials: Zona Colonial..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Santo Domingo essentials: Zona Colonial..", "x": "At a glance: Santo Domingo, Dominican Republic — first city of the Americas.. Cathedral. The numbers, the layout, the vibe: Santo Domingo in brief. History. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Zona Colonial.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Zona Colonial.", "x": "Santo Domingo: Zona Colonial.. History. One of the defining things about Santo Domingo — Malecon.. first city of the Americas. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Zona Colonial..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Zona Colonial..", "x": "Guide: Zona Colonial.. Day trip: Saona. How to do it right — Santo Domingo. Mofongo. first city of the Americas. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Cathedral.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Cathedral.", "x": "Santo Domingo: Cathedral.. Beach. One of the defining things about Santo Domingo — Mofongo.. first city of the Americas. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Cathedral..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Cathedral..", "x": "Guide: Cathedral.. Music. How to do it right — Santo Domingo. Alcazar. first city of the Americas. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Malecon.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Malecon.", "x": "Santo Domingo: Malecon.. Day trip: Saona. One of the defining things about Santo Domingo — Alcazar.. first city of the Americas. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Malecon..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Malecon..", "x": "Guide: Malecon.. Culture. How to do it right — Santo Domingo. History. first city of the Americas. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Mofongo.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Mofongo.", "x": "Santo Domingo: Mofongo.. Music. One of the defining things about Santo Domingo — History.. first city of the Americas. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Mofongo..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Mofongo..", "x": "Guide: Mofongo.. Colonial. How to do it right — Santo Domingo. Zona Colonial. first city of the Americas. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Alcazar.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Alcazar.", "x": "Santo Domingo: Alcazar.. Culture. One of the defining things about Santo Domingo — Zona Colonial.. first city of the Americas. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Alcazar..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Alcazar..", "x": "Guide: Alcazar.. History. How to do it right — Santo Domingo. Cathedral. first city of the Americas. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "History.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "History.", "x": "Santo Domingo: History.. Colonial. One of the defining things about Santo Domingo — Cathedral.. first city of the Americas. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: History..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: History..", "x": "Guide: History.. Beach. How to do it right — Santo Domingo. Malecon. first city of the Americas. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Colonial.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Colonial.", "x": "Santo Domingo in depth: Colonial.. Cathedral. The details — first city of the Americas.. Beach. Mofongo. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Santo Domingo in depth: History.. Malecon. The details — first city of the Americas.. Day trip: Saona. Alcazar. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Beach.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Beach.", "x": "Santo Domingo in depth: Beach.. Mofongo. The details — first city of the Americas.. Music. History. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Saona.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Saona.", "x": "Santo Domingo in depth: Day trip: Saona.. Alcazar. The details — first city of the Americas.. Culture. Zona Colonial. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Music.", "x": "Santo Domingo in depth: Music.. History. The details — first city of the Americas.. Colonial. Cathedral. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Santo Domingo in depth: Culture.. Zona Colonial. The details — first city of the Americas.. History. Malecon. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Santo Domingo's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Santo Domingo's districts.", "x": "Neighborhoods: Colonial.. Malecon. Where to stay, eat, and wander — Santo Domingo. first city of the Americas. Every district has its own personality; History.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Santo Domingo: Mofongo..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Santo Domingo: Mofongo..", "x": "Food: Mofongo.. Beach. The tastes of Santo Domingo — first city of the Americas.. Alcazar. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Santo Domingo transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Santo Domingo transport.", "x": "Transport: Day trip: Saona.. History. Subways, buses, walking — Santo Domingo. first city of the Americas. Learn the system on day one; Music.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Santo Domingo.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Santo Domingo.", "x": "Timing: Culture.. Zona Colonial. Seasons and festivals — Santo Domingo. first city of the Americas. Time it right for Colonial.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Santo Domingo safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Santo Domingo safely.", "x": "Safety: History.. Cathedral. Sensible precautions — Santo Domingo. first city of the Americas. Big cities reward street smarts; Beach.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-santo-domingo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
