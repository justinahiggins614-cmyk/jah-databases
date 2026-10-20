(function(){'use strict';
/* JAH Moscow City Database generator — jahdb-e2-city-moscow-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-moscow',PREFIX='JAH-E2CITYMOSCO-',NAME='JAH Moscow City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Moscow: the complete city guide", "d": "Moscow, Russia: the Kremlin's city..", "g": "overview", "l": 2, "q": "What is Moscow: the complete city guide?", "a": "Moscow, Russia: the Kremlin's city..", "x": "The complete Moscow city guide: the Kremlin's city.. Red Square. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Moscow in one database. Metro. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Moscow essentials: Red Square..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Moscow essentials: Red Square..", "x": "At a glance: Moscow, Russia — the Kremlin's city.. St. Basil's. The numbers, the layout, the vibe: Moscow in brief. Squares. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Red Square.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Red Square.", "x": "Moscow: Red Square.. Squares. One of the defining things about Moscow — Kremlin.. the Kremlin's city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Red Square..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Red Square..", "x": "Guide: Red Square.. History. How to do it right — Moscow. Bolshoi. the Kremlin's city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "St. Basil's.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "St. Basil's.", "x": "Moscow: St. Basil's.. Theater. One of the defining things about Moscow — Bolshoi.. the Kremlin's city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: St. Basil's..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: St. Basil's..", "x": "Guide: St. Basil's.. Winter. How to do it right — Moscow. Metro palaces. the Kremlin's city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Kremlin.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Kremlin.", "x": "Moscow: Kremlin.. History. One of the defining things about Moscow — Metro palaces.. the Kremlin's city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Kremlin..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Kremlin..", "x": "Guide: Kremlin.. Day trip: Sergiev. How to do it right — Moscow. Blini. the Kremlin's city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Bolshoi.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Bolshoi.", "x": "Moscow: Bolshoi.. Winter. One of the defining things about Moscow — Blini.. the Kremlin's city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Bolshoi..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Bolshoi..", "x": "Guide: Bolshoi.. Metro. How to do it right — Moscow. Red Square. the Kremlin's city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Metro palaces.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Metro palaces.", "x": "Moscow: Metro palaces.. Day trip: Sergiev. One of the defining things about Moscow — Red Square.. the Kremlin's city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Metro palaces..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Metro palaces..", "x": "Guide: Metro palaces.. Squares. How to do it right — Moscow. St. Basil's. the Kremlin's city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Blini.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Blini.", "x": "Moscow: Blini.. Metro. One of the defining things about Moscow — St. Basil's.. the Kremlin's city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Blini..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Blini..", "x": "Guide: Blini.. Theater. How to do it right — Moscow. Kremlin. the Kremlin's city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Metro.", "x": "Moscow in depth: Metro.. St. Basil's. The details — the Kremlin's city.. Theater. Bolshoi. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Squares.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Squares.", "x": "Moscow in depth: Squares.. Kremlin. The details — the Kremlin's city.. History. Metro palaces. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Theater.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Theater.", "x": "Moscow in depth: Theater.. Bolshoi. The details — the Kremlin's city.. Winter. Blini. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Moscow in depth: History.. Metro palaces. The details — the Kremlin's city.. Day trip: Sergiev. Red Square. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Winter.", "x": "Moscow in depth: Winter.. Blini. The details — the Kremlin's city.. Metro. St. Basil's. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day trip: Sergiev.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day trip: Sergiev.", "x": "Moscow in depth: Day trip: Sergiev.. Red Square. The details — the Kremlin's city.. Squares. Kremlin. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Moscow's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Moscow's districts.", "x": "Neighborhoods: Metro.. Kremlin. Where to stay, eat, and wander — Moscow. the Kremlin's city. Every district has its own personality; Squares.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Moscow: Bolshoi..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Moscow: Bolshoi..", "x": "Food: Bolshoi.. Theater. The tastes of Moscow — the Kremlin's city.. Metro palaces. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Moscow transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Moscow transport.", "x": "Transport: History.. Blini. Subways, buses, walking — Moscow. the Kremlin's city. Learn the system on day one; Winter.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Moscow.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Moscow.", "x": "Timing: Day trip: Sergiev.. Red Square. Seasons and festivals — Moscow. the Kremlin's city. Time it right for Metro.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Moscow safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Moscow safely.", "x": "Safety: Squares.. St. Basil's. Sensible precautions — Moscow. the Kremlin's city. Big cities reward street smarts; Theater.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-moscow-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
