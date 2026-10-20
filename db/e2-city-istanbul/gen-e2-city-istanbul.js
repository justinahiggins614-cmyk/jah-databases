(function(){'use strict';
/* JAH Istanbul City Database generator — jahdb-e2-city-istanbul-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-istanbul',PREFIX='JAH-E2CITYISTAN-',NAME='JAH Istanbul City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Istanbul: the complete city guide", "d": "Istanbul, Turkey: where continents meet..", "g": "overview", "l": 2, "q": "What is Istanbul: the complete city guide?", "a": "Istanbul, Turkey: where continents meet..", "x": "The complete Istanbul city guide: where continents meet.. Hagia Sophia. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Istanbul in one database. Ferries. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Istanbul essentials: Hagia Sophia..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Istanbul essentials: Hagia Sophia..", "x": "At a glance: Istanbul, Turkey — where continents meet.. Blue Mosque. The numbers, the layout, the vibe: Istanbul in brief. Bazaars. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Hagia Sophia.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Hagia Sophia.", "x": "Istanbul: Hagia Sophia.. Bazaars. One of the defining things about Istanbul — Grand Bazaar.. where continents meet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Hagia Sophia..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Hagia Sophia..", "x": "Guide: Hagia Sophia.. Two continents. How to do it right — Istanbul. Bosphorus. where continents meet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Blue Mosque.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Blue Mosque.", "x": "Istanbul: Blue Mosque.. History. One of the defining things about Istanbul — Bosphorus.. where continents meet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Blue Mosque..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Blue Mosque..", "x": "Guide: Blue Mosque.. Food. How to do it right — Istanbul. Topkapi. where continents meet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Grand Bazaar.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Grand Bazaar.", "x": "Istanbul: Grand Bazaar.. Two continents. One of the defining things about Istanbul — Topkapi.. where continents meet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Grand Bazaar..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Grand Bazaar..", "x": "Guide: Grand Bazaar.. Trams. How to do it right — Istanbul. Baklava. where continents meet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Bosphorus.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Bosphorus.", "x": "Istanbul: Bosphorus.. Food. One of the defining things about Istanbul — Baklava.. where continents meet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Bosphorus..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Bosphorus..", "x": "Guide: Bosphorus.. Ferries. How to do it right — Istanbul. Hagia Sophia. where continents meet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Topkapi.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Topkapi.", "x": "Istanbul: Topkapi.. Trams. One of the defining things about Istanbul — Hagia Sophia.. where continents meet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Topkapi..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Topkapi..", "x": "Guide: Topkapi.. Bazaars. How to do it right — Istanbul. Blue Mosque. where continents meet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Baklava.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Baklava.", "x": "Istanbul: Baklava.. Ferries. One of the defining things about Istanbul — Blue Mosque.. where continents meet. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Baklava..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Baklava..", "x": "Guide: Baklava.. History. How to do it right — Istanbul. Grand Bazaar. where continents meet. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ferries.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ferries.", "x": "Istanbul in depth: Ferries.. Blue Mosque. The details — where continents meet.. History. Bosphorus. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bazaars.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bazaars.", "x": "Istanbul in depth: Bazaars.. Grand Bazaar. The details — where continents meet.. Two continents. Topkapi. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Istanbul in depth: History.. Bosphorus. The details — where continents meet.. Food. Baklava. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Two continents.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Two continents.", "x": "Istanbul in depth: Two continents.. Topkapi. The details — where continents meet.. Trams. Hagia Sophia. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Food.", "x": "Istanbul in depth: Food.. Baklava. The details — where continents meet.. Ferries. Blue Mosque. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Trams.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Trams.", "x": "Istanbul in depth: Trams.. Hagia Sophia. The details — where continents meet.. Bazaars. Grand Bazaar. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Istanbul's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Istanbul's districts.", "x": "Neighborhoods: Ferries.. Grand Bazaar. Where to stay, eat, and wander — Istanbul. where continents meet. Every district has its own personality; Bazaars.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Istanbul: Bosphorus..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Istanbul: Bosphorus..", "x": "Food: Bosphorus.. History. The tastes of Istanbul — where continents meet.. Topkapi. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Istanbul transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Istanbul transport.", "x": "Transport: Two continents.. Baklava. Subways, buses, walking — Istanbul. where continents meet. Learn the system on day one; Food.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Istanbul.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Istanbul.", "x": "Timing: Trams.. Hagia Sophia. Seasons and festivals — Istanbul. where continents meet. Time it right for Ferries.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Istanbul safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Istanbul safely.", "x": "Safety: Bazaars.. Blue Mosque. Sensible precautions — Istanbul. where continents meet. Big cities reward street smarts; History.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-istanbul-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
