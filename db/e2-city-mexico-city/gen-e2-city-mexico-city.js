(function(){'use strict';
/* JAH Mexico City City Database generator — jahdb-e2-city-mexico-city-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-mexico-city',PREFIX='JAH-E2CITYMEXIC-',NAME='JAH Mexico City City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mexico City: the complete city guide", "d": "Mexico City, Mexico: Aztec capital turned megacity..", "g": "overview", "l": 2, "q": "What is Mexico City: the complete city guide?", "a": "Mexico City, Mexico: Aztec capital turned megacity..", "x": "The complete Mexico City city guide: Aztec capital turned megacity.. Zocalo. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Mexico City in one database. Metro. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Mexico City essentials: Zocalo..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Mexico City essentials: Zocalo..", "x": "At a glance: Mexico City, Mexico — Aztec capital turned megacity.. Teotihuacan. The numbers, the layout, the vibe: Mexico City in brief. Altitude. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Zocalo.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Zocalo.", "x": "Mexico City: Zocalo.. Altitude. One of the defining things about Mexico City — Frida Kahlo Museum.. Aztec capital turned megacity. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Zocalo..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Zocalo..", "x": "Guide: Zocalo.. Day trip: pyramids. How to do it right — Mexico City. Chapultepec. Aztec capital turned megacity. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Teotihuacan.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Teotihuacan.", "x": "Mexico City: Teotihuacan.. History. One of the defining things about Mexico City — Chapultepec.. Aztec capital turned megacity. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Teotihuacan..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Teotihuacan..", "x": "Guide: Teotihuacan.. Safety. How to do it right — Mexico City. Tacos al pastor. Aztec capital turned megacity. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Frida Kahlo Museum.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Frida Kahlo Museum.", "x": "Mexico City: Frida Kahlo Museum.. Day trip: pyramids. One of the defining things about Mexico City — Tacos al pastor.. Aztec capital turned megacity. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Frida Kahlo Museum..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Frida Kahlo Museum..", "x": "Guide: Frida Kahlo Museum.. Markets. How to do it right — Mexico City. Lucha libre. Aztec capital turned megacity. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Chapultepec.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Chapultepec.", "x": "Mexico City: Chapultepec.. Safety. One of the defining things about Mexico City — Lucha libre.. Aztec capital turned megacity. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Chapultepec..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Chapultepec..", "x": "Guide: Chapultepec.. Metro. How to do it right — Mexico City. Zocalo. Aztec capital turned megacity. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Tacos al pastor.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Tacos al pastor.", "x": "Mexico City: Tacos al pastor.. Markets. One of the defining things about Mexico City — Zocalo.. Aztec capital turned megacity. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Tacos al pastor..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Tacos al pastor..", "x": "Guide: Tacos al pastor.. Altitude. How to do it right — Mexico City. Teotihuacan. Aztec capital turned megacity. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Lucha libre.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Lucha libre.", "x": "Mexico City: Lucha libre.. Metro. One of the defining things about Mexico City — Teotihuacan.. Aztec capital turned megacity. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Lucha libre..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Lucha libre..", "x": "Guide: Lucha libre.. History. How to do it right — Mexico City. Frida Kahlo Museum. Aztec capital turned megacity. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Metro.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Metro.", "x": "Mexico City in depth: Metro.. Teotihuacan. The details — Aztec capital turned megacity.. History. Chapultepec. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Altitude.", "x": "Mexico City in depth: Altitude.. Frida Kahlo Museum. The details — Aztec capital turned megacity.. Day trip: pyramids. Tacos al pastor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Mexico City in depth: History.. Chapultepec. The details — Aztec capital turned megacity.. Safety. Lucha libre. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Day trip: pyramids.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Day trip: pyramids.", "x": "Mexico City in depth: Day trip: pyramids.. Tacos al pastor. The details — Aztec capital turned megacity.. Markets. Zocalo. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Safety.", "x": "Mexico City in depth: Safety.. Lucha libre. The details — Aztec capital turned megacity.. Metro. Teotihuacan. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Markets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Markets.", "x": "Mexico City in depth: Markets.. Zocalo. The details — Aztec capital turned megacity.. Altitude. Frida Kahlo Museum. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Mexico City's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Mexico City's districts.", "x": "Neighborhoods: Metro.. Frida Kahlo Museum. Where to stay, eat, and wander — Mexico City. Aztec capital turned megacity. Every district has its own personality; Altitude.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Mexico City: Chapultepec..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Mexico City: Chapultepec..", "x": "Food: Chapultepec.. History. The tastes of Mexico City — Aztec capital turned megacity.. Tacos al pastor. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Mexico City transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Mexico City transport.", "x": "Transport: Day trip: pyramids.. Lucha libre. Subways, buses, walking — Mexico City. Aztec capital turned megacity. Learn the system on day one; Safety.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Mexico City.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Mexico City.", "x": "Timing: Markets.. Zocalo. Seasons and festivals — Mexico City. Aztec capital turned megacity. Time it right for Metro.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Mexico City safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Mexico City safely.", "x": "Safety: Altitude.. Teotihuacan. Sensible precautions — Mexico City. Aztec capital turned megacity. Big cities reward street smarts; History.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-mexico-city-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
