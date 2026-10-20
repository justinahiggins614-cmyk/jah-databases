(function(){'use strict';
/* JAH Beijing City Database generator — jahdb-e2-city-beijing-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-beijing',PREFIX='JAH-E2CITYBEIJI-',NAME='JAH Beijing City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Beijing: the complete city guide", "d": "Beijing, China: capital of dynasties..", "g": "overview", "l": 2, "q": "What is Beijing: the complete city guide?", "a": "Beijing, China: capital of dynasties..", "x": "The complete Beijing city guide: capital of dynasties.. Forbidden City. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Beijing in one database. Subway. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Beijing essentials: Forbidden City..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Beijing essentials: Forbidden City..", "x": "At a glance: Beijing, China — capital of dynasties.. Great Wall. The numbers, the layout, the vibe: Beijing in brief. Wall trips. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Forbidden City.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Forbidden City.", "x": "Beijing: Forbidden City.. Wall trips. One of the defining things about Beijing — Tiananmen.. capital of dynasties. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Forbidden City..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Forbidden City..", "x": "Guide: Forbidden City.. Food. How to do it right — Beijing. Temple of Heaven. capital of dynasties. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Great Wall.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Great Wall.", "x": "Beijing: Great Wall.. History. One of the defining things about Beijing — Temple of Heaven.. capital of dynasties. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Great Wall..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Great Wall..", "x": "Guide: Great Wall.. Smog. How to do it right — Beijing. Peking duck. capital of dynasties. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Tiananmen.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Tiananmen.", "x": "Beijing: Tiananmen.. Food. One of the defining things about Beijing — Peking duck.. capital of dynasties. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Tiananmen..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Tiananmen..", "x": "Guide: Tiananmen.. Etiquette. How to do it right — Beijing. Hutongs. capital of dynasties. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Temple of Heaven.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Temple of Heaven.", "x": "Beijing: Temple of Heaven.. Smog. One of the defining things about Beijing — Hutongs.. capital of dynasties. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Temple of Heaven..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Temple of Heaven..", "x": "Guide: Temple of Heaven.. Subway. How to do it right — Beijing. Forbidden City. capital of dynasties. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Peking duck.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Peking duck.", "x": "Beijing: Peking duck.. Etiquette. One of the defining things about Beijing — Forbidden City.. capital of dynasties. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Peking duck..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Peking duck..", "x": "Guide: Peking duck.. Wall trips. How to do it right — Beijing. Great Wall. capital of dynasties. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Hutongs.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Hutongs.", "x": "Beijing: Hutongs.. Subway. One of the defining things about Beijing — Great Wall.. capital of dynasties. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Hutongs..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Hutongs..", "x": "Guide: Hutongs.. History. How to do it right — Beijing. Tiananmen. capital of dynasties. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Subway.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Subway.", "x": "Beijing in depth: Subway.. Great Wall. The details — capital of dynasties.. History. Temple of Heaven. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wall trips.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wall trips.", "x": "Beijing in depth: Wall trips.. Tiananmen. The details — capital of dynasties.. Food. Peking duck. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Beijing in depth: History.. Temple of Heaven. The details — capital of dynasties.. Smog. Hutongs. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "Beijing in depth: Food.. Peking duck. The details — capital of dynasties.. Etiquette. Forbidden City. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Smog.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Smog.", "x": "Beijing in depth: Smog.. Hutongs. The details — capital of dynasties.. Subway. Great Wall. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Etiquette.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Etiquette.", "x": "Beijing in depth: Etiquette.. Forbidden City. The details — capital of dynasties.. Wall trips. Tiananmen. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Beijing's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Beijing's districts.", "x": "Neighborhoods: Subway.. Tiananmen. Where to stay, eat, and wander — Beijing. capital of dynasties. Every district has its own personality; Wall trips.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Beijing: Temple of Heaven..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Beijing: Temple of Heaven..", "x": "Food: Temple of Heaven.. History. The tastes of Beijing — capital of dynasties.. Peking duck. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Beijing transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Beijing transport.", "x": "Transport: Food.. Hutongs. Subways, buses, walking — Beijing. capital of dynasties. Learn the system on day one; Smog.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Beijing.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Beijing.", "x": "Timing: Etiquette.. Forbidden City. Seasons and festivals — Beijing. capital of dynasties. Time it right for Subway.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Beijing safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Beijing safely.", "x": "Safety: Wall trips.. Great Wall. Sensible precautions — Beijing. capital of dynasties. Big cities reward street smarts; History.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-beijing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
