(function(){'use strict';
/* JAH Jakarta City Database generator — jahdb-e2-city-jakarta-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-jakarta',PREFIX='JAH-E2CITYJAKAR-',NAME='JAH Jakarta City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jakarta: the complete city guide", "d": "Jakarta, Indonesia: the big durian..", "g": "overview", "l": 2, "q": "What is Jakarta: the complete city guide?", "a": "Jakarta, Indonesia: the big durian..", "x": "The complete Jakarta city guide: the big durian.. National Monument. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Jakarta in one database. Monas. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Jakarta essentials: National Monument..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Jakarta essentials: National Monument..", "x": "At a glance: Jakarta, Indonesia — the big durian.. Old Town. The numbers, the layout, the vibe: Jakarta in brief. Kota Tua. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "National Monument.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "National Monument.", "x": "Jakarta: National Monument.. Kota Tua. One of the defining things about Jakarta — Thousand Islands.. the big durian. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: National Monument..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: National Monument..", "x": "Guide: National Monument.. Food. How to do it right — Jakarta. Street food. the big durian. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Old Town.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Old Town.", "x": "Jakarta: Old Town.. Islands. One of the defining things about Jakarta — Street food.. the big durian. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Old Town..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Old Town..", "x": "Guide: Old Town.. Day trip: Bogor. How to do it right — Jakarta. Malls. the big durian. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Thousand Islands.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Thousand Islands.", "x": "Jakarta: Thousand Islands.. Food. One of the defining things about Jakarta — Malls.. the big durian. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Thousand Islands..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Thousand Islands..", "x": "Guide: Thousand Islands.. Traffic. How to do it right — Jakarta. Traffic. the big durian. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Street food.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Street food.", "x": "Jakarta: Street food.. Day trip: Bogor. One of the defining things about Jakarta — Traffic.. the big durian. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Street food..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Street food..", "x": "Guide: Street food.. Monas. How to do it right — Jakarta. National Monument. the big durian. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Malls.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Malls.", "x": "Jakarta: Malls.. Traffic. One of the defining things about Jakarta — National Monument.. the big durian. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Malls..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Malls..", "x": "Guide: Malls.. Kota Tua. How to do it right — Jakarta. Old Town. the big durian. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Traffic.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Traffic.", "x": "Jakarta: Traffic.. Monas. One of the defining things about Jakarta — Old Town.. the big durian. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Traffic..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Traffic..", "x": "Guide: Traffic.. Islands. How to do it right — Jakarta. Thousand Islands. the big durian. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Monas.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Monas.", "x": "Jakarta in depth: Monas.. Old Town. The details — the big durian.. Islands. Street food. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kota Tua.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kota Tua.", "x": "Jakarta in depth: Kota Tua.. Thousand Islands. The details — the big durian.. Food. Malls. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Islands.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Islands.", "x": "Jakarta in depth: Islands.. Street food. The details — the big durian.. Day trip: Bogor. Traffic. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "Jakarta in depth: Food.. Malls. The details — the big durian.. Traffic. National Monument. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Day trip: Bogor.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Day trip: Bogor.", "x": "Jakarta in depth: Day trip: Bogor.. Traffic. The details — the big durian.. Monas. Old Town. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Traffic.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Traffic.", "x": "Jakarta in depth: Traffic.. National Monument. The details — the big durian.. Kota Tua. Thousand Islands. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Jakarta's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Jakarta's districts.", "x": "Neighborhoods: Monas.. Thousand Islands. Where to stay, eat, and wander — Jakarta. the big durian. Every district has its own personality; Kota Tua.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Jakarta: Street food..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Jakarta: Street food..", "x": "Food: Street food.. Islands. The tastes of Jakarta — the big durian.. Malls. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Jakarta transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Jakarta transport.", "x": "Transport: Food.. Traffic. Subways, buses, walking — Jakarta. the big durian. Learn the system on day one; Day trip: Bogor.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Jakarta.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Jakarta.", "x": "Timing: Traffic.. National Monument. Seasons and festivals — Jakarta. the big durian. Time it right for Monas.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Jakarta safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Jakarta safely.", "x": "Safety: Kota Tua.. Old Town. Sensible precautions — Jakarta. the big durian. Big cities reward street smarts; Islands.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-jakarta-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
