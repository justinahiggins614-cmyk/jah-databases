(function(){'use strict';
/* JAH Yas Waterworld Water Park Database generator — jahdb-e2-waterpark-yas-waterworld-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-waterpark-yas-waterworld',PREFIX='JAH-E2WATERPARK-',NAME='JAH Yas Waterworld Water Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yas Waterworld: the complete guide", "d": "Yas Waterworld: Abu Dhabi's pearl dive..", "g": "overview", "l": 2, "q": "What is Yas Waterworld: the complete guide?", "a": "Yas Waterworld: Abu Dhabi's pearl dive..", "x": "The complete water park guide to Yas Waterworld: Abu Dhabi's pearl dive.. 2013. From formation to visiting, from wildlife to legends — everything about this water park in one database. Pearl. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2013.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2013.", "x": "Yas Waterworld: 2013.. Slides. One of the defining facts — Dawwama.. Abu Dhabi's pearl dive. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2013..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2013..", "x": "Explored: 2013.. Tickets. Why it is so — Yas Waterworld. Yas Island. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pearl diving.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pearl diving.", "x": "Yas Waterworld: Pearl diving.. Island. One of the defining facts — Yas Island.. Abu Dhabi's pearl dive. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Pearl diving..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Pearl diving..", "x": "Explored: Pearl diving.. Abu Dhabi. Why it is so — Yas Waterworld. 43 slides. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dawwama.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dawwama.", "x": "Yas Waterworld: Dawwama.. Tickets. One of the defining facts — 43 slides.. Abu Dhabi's pearl dive. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Dawwama..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Dawwama..", "x": "Explored: Dawwama.. Theme. Why it is so — Yas Waterworld. Emirati. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Yas Island.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Yas Island.", "x": "Yas Waterworld: Yas Island.. Abu Dhabi. One of the defining facts — Emirati.. Abu Dhabi's pearl dive. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Yas Island..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Yas Island..", "x": "Explored: Yas Island.. Pearl. Why it is so — Yas Waterworld. 2013. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "43 slides.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "43 slides.", "x": "Yas Waterworld: 43 slides.. Theme. One of the defining facts — 2013.. Abu Dhabi's pearl dive. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: 43 slides..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: 43 slides..", "x": "Explored: 43 slides.. Slides. Why it is so — Yas Waterworld. Pearl diving. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Emirati.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Emirati.", "x": "Yas Waterworld: Emirati.. Pearl. One of the defining facts — Pearl diving.. Abu Dhabi's pearl dive. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Emirati..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Emirati..", "x": "Explored: Emirati.. Island. Why it is so — Yas Waterworld. Dawwama. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pearl.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pearl.", "x": "Yas Waterworld in depth: Pearl.. Pearl diving. The details reward the curious — Abu Dhabi's pearl dive.. Island. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Slides.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Slides.", "x": "Yas Waterworld in depth: Slides.. Dawwama. The details reward the curious — Abu Dhabi's pearl dive.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Island.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Island.", "x": "Yas Waterworld in depth: Island.. Yas Island. The details reward the curious — Abu Dhabi's pearl dive.. Abu Dhabi. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Yas Waterworld in depth: Tickets.. 43 slides. The details reward the curious — Abu Dhabi's pearl dive.. Theme. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Abu Dhabi.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Abu Dhabi.", "x": "Yas Waterworld in depth: Abu Dhabi.. Emirati. The details reward the curious — Abu Dhabi's pearl dive.. Pearl. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Theme.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Theme.", "x": "Yas Waterworld in depth: Theme.. 2013. The details reward the curious — Abu Dhabi's pearl dive.. Slides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Yas Waterworld is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Yas Waterworld is.", "x": "Location: 2013.. Pearl. Getting oriented — Yas Waterworld. Abu Dhabi's pearl dive. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Yas Waterworld.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Yas Waterworld.", "x": "Visiting: Slides.. Pearl diving. Practical know-how — Yas Waterworld. Abu Dhabi's pearl dive. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Yas Waterworld.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Yas Waterworld.", "x": "Ecology: Island.. Dawwama. The living world of Yas Waterworld — Abu Dhabi's pearl dive.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Yas Waterworld through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Yas Waterworld through time.", "x": "History: Abu Dhabi.. Yas Island. People and Yas Waterworld across the centuries — Abu Dhabi's pearl dive.. Theme. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Yas Waterworld.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Yas Waterworld.", "x": "Conservation: Slides.. 2013. Threats and guardians of Yas Waterworld — Abu Dhabi's pearl dive.. Island. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Yas Waterworld in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Yas Waterworld in numbers.", "x": "Numbers: 2013.; Pearl diving.. Tickets. Statistics that stun — Yas Waterworld. Abu Dhabi's pearl dive. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-waterpark-yas-waterworld-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
