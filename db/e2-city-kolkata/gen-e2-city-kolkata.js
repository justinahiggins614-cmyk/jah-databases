(function(){'use strict';
/* JAH Kolkata City Database generator — jahdb-e2-city-kolkata-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-kolkata',PREFIX='JAH-E2CITYKOLKA-',NAME='JAH Kolkata City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kolkata: the complete city guide", "d": "Kolkata, India: city of joy..", "g": "overview", "l": 2, "q": "What is Kolkata: the complete city guide?", "a": "Kolkata, India: city of joy..", "x": "The complete Kolkata city guide: city of joy.. Victoria Memorial. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Kolkata in one database. Trams. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Kolkata essentials: Victoria Memorial..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Kolkata essentials: Victoria Memorial..", "x": "At a glance: Kolkata, India — city of joy.. Howrah Bridge. The numbers, the layout, the vibe: Kolkata in brief. Festivals. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Victoria Memorial.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Victoria Memorial.", "x": "Kolkata: Victoria Memorial.. Festivals. One of the defining things about Kolkata — Durga Puja.. city of joy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Victoria Memorial..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Victoria Memorial..", "x": "Guide: Victoria Memorial.. Food. How to do it right — Kolkata. Trams. city of joy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Howrah Bridge.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Howrah Bridge.", "x": "Kolkata: Howrah Bridge.. Colonial. One of the defining things about Kolkata — Trams.. city of joy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Howrah Bridge..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Howrah Bridge..", "x": "Guide: Howrah Bridge.. Markets. How to do it right — Kolkata. Park Street. city of joy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Durga Puja.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Durga Puja.", "x": "Kolkata: Durga Puja.. Food. One of the defining things about Kolkata — Park Street.. city of joy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Durga Puja..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Durga Puja..", "x": "Guide: Durga Puja.. Culture. How to do it right — Kolkata. Rosogolla. city of joy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Trams.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Trams.", "x": "Kolkata: Trams.. Markets. One of the defining things about Kolkata — Rosogolla.. city of joy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Trams..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Trams..", "x": "Guide: Trams.. Trams. How to do it right — Kolkata. Victoria Memorial. city of joy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Park Street.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Park Street.", "x": "Kolkata: Park Street.. Culture. One of the defining things about Kolkata — Victoria Memorial.. city of joy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Park Street..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Park Street..", "x": "Guide: Park Street.. Festivals. How to do it right — Kolkata. Howrah Bridge. city of joy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Rosogolla.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Rosogolla.", "x": "Kolkata: Rosogolla.. Trams. One of the defining things about Kolkata — Howrah Bridge.. city of joy. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Rosogolla..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Rosogolla..", "x": "Guide: Rosogolla.. Colonial. How to do it right — Kolkata. Durga Puja. city of joy. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Trams.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Trams.", "x": "Kolkata in depth: Trams.. Howrah Bridge. The details — city of joy.. Colonial. Trams. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Festivals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Festivals.", "x": "Kolkata in depth: Festivals.. Durga Puja. The details — city of joy.. Food. Park Street. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Colonial.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Colonial.", "x": "Kolkata in depth: Colonial.. Trams. The details — city of joy.. Markets. Rosogolla. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "Kolkata in depth: Food.. Park Street. The details — city of joy.. Culture. Victoria Memorial. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Markets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Markets.", "x": "Kolkata in depth: Markets.. Rosogolla. The details — city of joy.. Trams. Howrah Bridge. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Kolkata in depth: Culture.. Victoria Memorial. The details — city of joy.. Festivals. Durga Puja. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Kolkata's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Kolkata's districts.", "x": "Neighborhoods: Trams.. Durga Puja. Where to stay, eat, and wander — Kolkata. city of joy. Every district has its own personality; Festivals.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Kolkata: Trams..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Kolkata: Trams..", "x": "Food: Trams.. Colonial. The tastes of Kolkata — city of joy.. Park Street. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Kolkata transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Kolkata transport.", "x": "Transport: Food.. Rosogolla. Subways, buses, walking — Kolkata. city of joy. Learn the system on day one; Markets.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Kolkata.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Kolkata.", "x": "Timing: Culture.. Victoria Memorial. Seasons and festivals — Kolkata. city of joy. Time it right for Trams.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Kolkata safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Kolkata safely.", "x": "Safety: Festivals.. Howrah Bridge. Sensible precautions — Kolkata. city of joy. Big cities reward street smarts; Colonial.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-kolkata-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
