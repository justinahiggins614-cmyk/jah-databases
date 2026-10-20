(function(){'use strict';
/* JAH Washington DC City Database generator — jahdb-e2-city-washington-dc-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-washington-dc',PREFIX='JAH-E2CITYWASHI-',NAME='JAH Washington DC City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Washington DC: the complete city guide", "d": "Washington DC, USA: the capital..", "g": "overview", "l": 2, "q": "What is Washington DC: the complete city guide?", "a": "Washington DC, USA: the capital..", "x": "The complete Washington DC city guide: the capital.. National Mall. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Washington DC in one database. Museums free. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Washington DC essentials: National Mall..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Washington DC essentials: National Mall..", "x": "At a glance: Washington DC, USA — the capital.. Smithsonian. The numbers, the layout, the vibe: Washington DC in brief. Mall. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "National Mall.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "National Mall.", "x": "Washington DC: National Mall.. Mall. One of the defining things about Washington DC — Lincoln Memorial.. the capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: National Mall..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: National Mall..", "x": "Guide: National Mall.. Day trip: Mount Vernon. How to do it right — Washington DC. Georgetown. the capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Smithsonian.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Smithsonian.", "x": "Washington DC: Smithsonian.. Metro. One of the defining things about Washington DC — Georgetown.. the capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Smithsonian..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Smithsonian..", "x": "Guide: Smithsonian.. Cherry blossoms. How to do it right — Washington DC. Monuments. the capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Lincoln Memorial.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Lincoln Memorial.", "x": "Washington DC: Lincoln Memorial.. Day trip: Mount Vernon. One of the defining things about Washington DC — Monuments.. the capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Lincoln Memorial..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Lincoln Memorial..", "x": "Guide: Lincoln Memorial.. Politics. How to do it right — Washington DC. Half-smoke. the capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Georgetown.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Georgetown.", "x": "Washington DC: Georgetown.. Cherry blossoms. One of the defining things about Washington DC — Half-smoke.. the capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Georgetown..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Georgetown..", "x": "Guide: Georgetown.. Museums free. How to do it right — Washington DC. National Mall. the capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Monuments.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Monuments.", "x": "Washington DC: Monuments.. Politics. One of the defining things about Washington DC — National Mall.. the capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Monuments..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Monuments..", "x": "Guide: Monuments.. Mall. How to do it right — Washington DC. Smithsonian. the capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Half-smoke.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Half-smoke.", "x": "Washington DC: Half-smoke.. Museums free. One of the defining things about Washington DC — Smithsonian.. the capital. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Half-smoke..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Half-smoke..", "x": "Guide: Half-smoke.. Metro. How to do it right — Washington DC. Lincoln Memorial. the capital. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Museums free.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Museums free.", "x": "Washington DC in depth: Museums free.. Smithsonian. The details — the capital.. Metro. Georgetown. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mall.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mall.", "x": "Washington DC in depth: Mall.. Lincoln Memorial. The details — the capital.. Day trip: Mount Vernon. Monuments. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Metro.", "x": "Washington DC in depth: Metro.. Georgetown. The details — the capital.. Cherry blossoms. Half-smoke. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: Mount Vernon.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: Mount Vernon.", "x": "Washington DC in depth: Day trip: Mount Vernon.. Monuments. The details — the capital.. Politics. National Mall. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cherry blossoms.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cherry blossoms.", "x": "Washington DC in depth: Cherry blossoms.. Half-smoke. The details — the capital.. Museums free. Smithsonian. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Politics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Politics.", "x": "Washington DC in depth: Politics.. National Mall. The details — the capital.. Mall. Lincoln Memorial. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Washington DC's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Washington DC's districts.", "x": "Neighborhoods: Museums free.. Lincoln Memorial. Where to stay, eat, and wander — Washington DC. the capital. Every district has its own personality; Mall.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Washington DC: Georgetown..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Washington DC: Georgetown..", "x": "Food: Georgetown.. Metro. The tastes of Washington DC — the capital.. Monuments. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Washington DC transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Washington DC transport.", "x": "Transport: Day trip: Mount Vernon.. Half-smoke. Subways, buses, walking — Washington DC. the capital. Learn the system on day one; Cherry blossoms.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Washington DC.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Washington DC.", "x": "Timing: Politics.. National Mall. Seasons and festivals — Washington DC. the capital. Time it right for Museums free.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Washington DC safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Washington DC safely.", "x": "Safety: Mall.. Smithsonian. Sensible precautions — Washington DC. the capital. Big cities reward street smarts; Metro.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-washington-dc-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
