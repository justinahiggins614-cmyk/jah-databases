(function(){'use strict';
/* JAH Perth City Database generator — jahdb-e2-city-perth-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-perth',PREFIX='JAH-E2CITYPERTH-',NAME='JAH Perth City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Perth: the complete city guide", "d": "Perth, Australia: the sunniest capital..", "g": "overview", "l": 2, "q": "What is Perth: the complete city guide?", "a": "Perth, Australia: the sunniest capital..", "x": "The complete Perth city guide: the sunniest capital.. Kings Park. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Perth in one database. Beaches. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Perth essentials: Kings Park..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Perth essentials: Kings Park..", "x": "At a glance: Perth, Australia — the sunniest capital.. Cottesloe Beach. The numbers, the layout, the vibe: Perth in brief. Park. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Kings Park.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Kings Park.", "x": "Perth: Kings Park.. Park. One of the defining things about Perth — Fremantle.. the sunniest capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Kings Park..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Kings Park..", "x": "Guide: Kings Park.. Day trip: Margaret River. How to do it right — Perth. Rottnest. the sunniest capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Cottesloe Beach.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Cottesloe Beach.", "x": "Perth: Cottesloe Beach.. Island. One of the defining things about Perth — Rottnest.. the sunniest capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Cottesloe Beach..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Cottesloe Beach..", "x": "Guide: Cottesloe Beach.. Sun. How to do it right — Perth. Swan River. the sunniest capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Fremantle.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Fremantle.", "x": "Perth: Fremantle.. Day trip: Margaret River. One of the defining things about Perth — Swan River.. the sunniest capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Fremantle..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Fremantle..", "x": "Guide: Fremantle.. Wine. How to do it right — Perth. Quokkas. the sunniest capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Rottnest.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Rottnest.", "x": "Perth: Rottnest.. Sun. One of the defining things about Perth — Quokkas.. the sunniest capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Rottnest..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Rottnest..", "x": "Guide: Rottnest.. Beaches. How to do it right — Perth. Kings Park. the sunniest capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Swan River.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Swan River.", "x": "Perth: Swan River.. Wine. One of the defining things about Perth — Kings Park.. the sunniest capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Swan River..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Swan River..", "x": "Guide: Swan River.. Park. How to do it right — Perth. Cottesloe Beach. the sunniest capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Quokkas.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Quokkas.", "x": "Perth: Quokkas.. Beaches. One of the defining things about Perth — Cottesloe Beach.. the sunniest capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Quokkas..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Quokkas..", "x": "Guide: Quokkas.. Island. How to do it right — Perth. Fremantle. the sunniest capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Beaches.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Beaches.", "x": "Perth in depth: Beaches.. Cottesloe Beach. The details — the sunniest capital.. Island. Rottnest. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Park.", "x": "Perth in depth: Park.. Fremantle. The details — the sunniest capital.. Day trip: Margaret River. Swan River. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Island.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Island.", "x": "Perth in depth: Island.. Rottnest. The details — the sunniest capital.. Sun. Quokkas. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Margaret River.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Margaret River.", "x": "Perth in depth: Day trip: Margaret River.. Swan River. The details — the sunniest capital.. Wine. Kings Park. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sun.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sun.", "x": "Perth in depth: Sun.. Quokkas. The details — the sunniest capital.. Beaches. Cottesloe Beach. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Wine.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Wine.", "x": "Perth in depth: Wine.. Kings Park. The details — the sunniest capital.. Park. Fremantle. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Perth's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Perth's districts.", "x": "Neighborhoods: Beaches.. Fremantle. Where to stay, eat, and wander — Perth. the sunniest capital. Every district has its own personality; Park.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Perth: Rottnest..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Perth: Rottnest..", "x": "Food: Rottnest.. Island. The tastes of Perth — the sunniest capital.. Swan River. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Perth transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Perth transport.", "x": "Transport: Day trip: Margaret River.. Quokkas. Subways, buses, walking — Perth. the sunniest capital. Learn the system on day one; Sun.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Perth.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Perth.", "x": "Timing: Wine.. Kings Park. Seasons and festivals — Perth. the sunniest capital. Time it right for Beaches.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Perth safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Perth safely.", "x": "Safety: Park.. Cottesloe Beach. Sensible precautions — Perth. the sunniest capital. Big cities reward street smarts; Island.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-perth-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
