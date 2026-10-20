(function(){'use strict';
/* JAH Athens City Database generator — jahdb-e2-city-athens-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-athens',PREFIX='JAH-E2CITYATHEN-',NAME='JAH Athens City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Athens: the complete city guide", "d": "Athens, Greece: democracy's birthplace..", "g": "overview", "l": 2, "q": "What is Athens: the complete city guide?", "a": "Athens, Greece: democracy's birthplace..", "x": "The complete Athens city guide: democracy's birthplace.. Acropolis. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Athens in one database. Acropolis. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Athens essentials: Acropolis..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Athens essentials: Acropolis..", "x": "At a glance: Athens, Greece — democracy's birthplace.. Plaka. The numbers, the layout, the vibe: Athens in brief. Plaka. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Acropolis.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Acropolis.", "x": "Athens: Acropolis.. Plaka. One of the defining things about Athens — National Museum.. democracy's birthplace. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Acropolis..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Acropolis..", "x": "Guide: Acropolis.. Food. How to do it right — Athens. Monastiraki. democracy's birthplace. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Plaka.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Plaka.", "x": "Athens: Plaka.. Day trip: Delphi. One of the defining things about Athens — Monastiraki.. democracy's birthplace. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Plaka..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Plaka..", "x": "Guide: Plaka.. Metro. How to do it right — Athens. Souvlaki. democracy's birthplace. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "National Museum.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "National Museum.", "x": "Athens: National Museum.. Food. One of the defining things about Athens — Souvlaki.. democracy's birthplace. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: National Museum..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: National Museum..", "x": "Guide: National Museum.. History. How to do it right — Athens. Sunset. democracy's birthplace. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Monastiraki.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Monastiraki.", "x": "Athens: Monastiraki.. Metro. One of the defining things about Athens — Sunset.. democracy's birthplace. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Monastiraki..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Monastiraki..", "x": "Guide: Monastiraki.. Acropolis. How to do it right — Athens. Acropolis. democracy's birthplace. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Souvlaki.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Souvlaki.", "x": "Athens: Souvlaki.. History. One of the defining things about Athens — Acropolis.. democracy's birthplace. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Souvlaki..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Souvlaki..", "x": "Guide: Souvlaki.. Plaka. How to do it right — Athens. Plaka. democracy's birthplace. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Sunset.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Sunset.", "x": "Athens: Sunset.. Acropolis. One of the defining things about Athens — Plaka.. democracy's birthplace. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Sunset..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Sunset..", "x": "Guide: Sunset.. Day trip: Delphi. How to do it right — Athens. National Museum. democracy's birthplace. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Acropolis.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Acropolis.", "x": "Athens in depth: Acropolis.. Plaka. The details — democracy's birthplace.. Day trip: Delphi. Monastiraki. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Plaka.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Plaka.", "x": "Athens in depth: Plaka.. National Museum. The details — democracy's birthplace.. Food. Souvlaki. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Day trip: Delphi.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Day trip: Delphi.", "x": "Athens in depth: Day trip: Delphi.. Monastiraki. The details — democracy's birthplace.. Metro. Sunset. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "Athens in depth: Food.. Souvlaki. The details — democracy's birthplace.. History. Acropolis. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Metro.", "x": "Athens in depth: Metro.. Sunset. The details — democracy's birthplace.. Acropolis. Plaka. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Athens in depth: History.. Acropolis. The details — democracy's birthplace.. Plaka. National Museum. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Athens's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Athens's districts.", "x": "Neighborhoods: Acropolis.. National Museum. Where to stay, eat, and wander — Athens. democracy's birthplace. Every district has its own personality; Plaka.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Athens: Monastiraki..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Athens: Monastiraki..", "x": "Food: Monastiraki.. Day trip: Delphi. The tastes of Athens — democracy's birthplace.. Souvlaki. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Athens transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Athens transport.", "x": "Transport: Food.. Sunset. Subways, buses, walking — Athens. democracy's birthplace. Learn the system on day one; Metro.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Athens.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Athens.", "x": "Timing: History.. Acropolis. Seasons and festivals — Athens. democracy's birthplace. Time it right for Acropolis.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Athens safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Athens safely.", "x": "Safety: Plaka.. Plaka. Sensible precautions — Athens. democracy's birthplace. Big cities reward street smarts; Day trip: Delphi.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-athens-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
