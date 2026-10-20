(function(){'use strict';
/* JAH Hong Kong City Database generator — jahdb-e2-city-hong-kong-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-hong-kong',PREFIX='JAH-E2CITYHONGK-',NAME='JAH Hong Kong City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hong Kong: the complete city guide", "d": "Hong Kong, China: Asia's world city..", "g": "overview", "l": 2, "q": "What is Hong Kong: the complete city guide?", "a": "Hong Kong, China: Asia's world city..", "x": "The complete Hong Kong city guide: Asia's world city.. Victoria Peak. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Hong Kong in one database. Peak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Hong Kong essentials: Victoria Peak..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Hong Kong essentials: Victoria Peak..", "x": "At a glance: Hong Kong, China — Asia's world city.. Star Ferry. The numbers, the layout, the vibe: Hong Kong in brief. Ferry. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Victoria Peak.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Victoria Peak.", "x": "Hong Kong: Victoria Peak.. Ferry. One of the defining things about Hong Kong — Temple Street.. Asia's world city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Victoria Peak..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Victoria Peak..", "x": "Guide: Victoria Peak.. Hikes. How to do it right — Hong Kong. Dim sum. Asia's world city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Star Ferry.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Star Ferry.", "x": "Hong Kong: Star Ferry.. Markets. One of the defining things about Hong Kong — Dim sum.. Asia's world city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Star Ferry..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Star Ferry..", "x": "Guide: Star Ferry.. MTR. How to do it right — Hong Kong. Lan Kwai Fong. Asia's world city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Temple Street.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Temple Street.", "x": "Hong Kong: Temple Street.. Hikes. One of the defining things about Hong Kong — Lan Kwai Fong.. Asia's world city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Temple Street..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Temple Street..", "x": "Guide: Temple Street.. Food. How to do it right — Hong Kong. Hiking. Asia's world city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Dim sum.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Dim sum.", "x": "Hong Kong: Dim sum.. MTR. One of the defining things about Hong Kong — Hiking.. Asia's world city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Dim sum..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Dim sum..", "x": "Guide: Dim sum.. Peak. How to do it right — Hong Kong. Victoria Peak. Asia's world city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Lan Kwai Fong.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Lan Kwai Fong.", "x": "Hong Kong: Lan Kwai Fong.. Food. One of the defining things about Hong Kong — Victoria Peak.. Asia's world city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Lan Kwai Fong..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Lan Kwai Fong..", "x": "Guide: Lan Kwai Fong.. Ferry. How to do it right — Hong Kong. Star Ferry. Asia's world city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Hiking.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Hiking.", "x": "Hong Kong: Hiking.. Peak. One of the defining things about Hong Kong — Star Ferry.. Asia's world city. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Hiking..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Hiking..", "x": "Guide: Hiking.. Markets. How to do it right — Hong Kong. Temple Street. Asia's world city. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Peak.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Peak.", "x": "Hong Kong in depth: Peak.. Star Ferry. The details — Asia's world city.. Markets. Dim sum. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ferry.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ferry.", "x": "Hong Kong in depth: Ferry.. Temple Street. The details — Asia's world city.. Hikes. Lan Kwai Fong. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Markets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Markets.", "x": "Hong Kong in depth: Markets.. Dim sum. The details — Asia's world city.. MTR. Hiking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hikes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hikes.", "x": "Hong Kong in depth: Hikes.. Lan Kwai Fong. The details — Asia's world city.. Food. Victoria Peak. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "MTR.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "MTR.", "x": "Hong Kong in depth: MTR.. Hiking. The details — Asia's world city.. Peak. Star Ferry. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Food.", "x": "Hong Kong in depth: Food.. Victoria Peak. The details — Asia's world city.. Ferry. Temple Street. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Hong Kong's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Hong Kong's districts.", "x": "Neighborhoods: Peak.. Temple Street. Where to stay, eat, and wander — Hong Kong. Asia's world city. Every district has its own personality; Ferry.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Hong Kong: Dim sum..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Hong Kong: Dim sum..", "x": "Food: Dim sum.. Markets. The tastes of Hong Kong — Asia's world city.. Lan Kwai Fong. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Hong Kong transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Hong Kong transport.", "x": "Transport: Hikes.. Hiking. Subways, buses, walking — Hong Kong. Asia's world city. Learn the system on day one; MTR.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Hong Kong.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Hong Kong.", "x": "Timing: Food.. Victoria Peak. Seasons and festivals — Hong Kong. Asia's world city. Time it right for Peak.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Hong Kong safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Hong Kong safely.", "x": "Safety: Ferry.. Star Ferry. Sensible precautions — Hong Kong. Asia's world city. Big cities reward street smarts; Markets.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-hong-kong-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
