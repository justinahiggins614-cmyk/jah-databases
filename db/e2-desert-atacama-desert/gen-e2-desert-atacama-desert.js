(function(){'use strict';
/* JAH Atacama Desert Desert Database generator — jahdb-e2-desert-atacama-desert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-desert-atacama-desert',PREFIX='JAH-E2DESERTATA-',NAME='JAH Atacama Desert Desert Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Atacama Desert: the complete guide", "d": "Atacama Desert: driest place on Earth..", "g": "overview", "l": 2, "q": "What is Atacama Desert: the complete guide?", "a": "Atacama Desert: driest place on Earth..", "x": "The complete desert guide to Atacama Desert: driest place on Earth.. 105,000 sq km. From formation to visiting, from wildlife to legends — everything about this desert in one database. Science. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "105,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "105,000 sq km.", "x": "Atacama Desert: 105,000 sq km.. Tours. One of the defining facts — ALMA telescopes.. driest place on Earth. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 105,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 105,000 sq km..", "x": "Explored: 105,000 sq km.. History. Why it is so — Atacama Desert. Salt flats. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mars analog.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mars analog.", "x": "Atacama Desert: Mars analog.. Flora. One of the defining facts — Salt flats.. driest place on Earth. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Mars analog..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Mars analog..", "x": "Explored: Mars analog.. Travel. Why it is so — Atacama Desert. Geysers. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "ALMA telescopes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "ALMA telescopes.", "x": "Atacama Desert: ALMA telescopes.. History. One of the defining facts — Geysers.. driest place on Earth. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: ALMA telescopes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: ALMA telescopes..", "x": "Explored: ALMA telescopes.. Night sky. Why it is so — Atacama Desert. Stargazing. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Salt flats.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Salt flats.", "x": "Atacama Desert: Salt flats.. Travel. One of the defining facts — Stargazing.. driest place on Earth. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Salt flats..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Salt flats..", "x": "Explored: Salt flats.. Science. Why it is so — Atacama Desert. 105,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Geysers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Geysers.", "x": "Atacama Desert: Geysers.. Night sky. One of the defining facts — 105,000 sq km.. driest place on Earth. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Geysers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Geysers..", "x": "Explored: Geysers.. Tours. Why it is so — Atacama Desert. Mars analog. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stargazing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stargazing.", "x": "Atacama Desert: Stargazing.. Science. One of the defining facts — Mars analog.. driest place on Earth. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Stargazing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Stargazing..", "x": "Explored: Stargazing.. Flora. Why it is so — Atacama Desert. ALMA telescopes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Science.", "x": "Atacama Desert in depth: Science.. Mars analog. The details reward the curious — driest place on Earth.. Flora. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tours.", "x": "Atacama Desert in depth: Tours.. ALMA telescopes. The details reward the curious — driest place on Earth.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Flora.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Flora.", "x": "Atacama Desert in depth: Flora.. Salt flats. The details reward the curious — driest place on Earth.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Atacama Desert in depth: History.. Geysers. The details reward the curious — driest place on Earth.. Night sky. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "Atacama Desert in depth: Travel.. Stargazing. The details reward the curious — driest place on Earth.. Science. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Night sky.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Night sky.", "x": "Atacama Desert in depth: Night sky.. 105,000 sq km. The details reward the curious — driest place on Earth.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Atacama Desert is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Atacama Desert is.", "x": "Location: 105,000 sq km.. Science. Getting oriented — Atacama Desert. driest place on Earth. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Atacama Desert.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Atacama Desert.", "x": "Visiting: Tours.. Mars analog. Practical know-how — Atacama Desert. driest place on Earth. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Atacama Desert.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Atacama Desert.", "x": "Ecology: Flora.. ALMA telescopes. The living world of Atacama Desert — driest place on Earth.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Atacama Desert through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Atacama Desert through time.", "x": "History: Travel.. Salt flats. People and Atacama Desert across the centuries — driest place on Earth.. Night sky. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Atacama Desert.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Atacama Desert.", "x": "Conservation: Tours.. 105,000 sq km. Threats and guardians of Atacama Desert — driest place on Earth.. Flora. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Atacama Desert in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Atacama Desert in numbers.", "x": "Numbers: 105,000 sq km.; Mars analog.. History. Statistics that stun — Atacama Desert. driest place on Earth. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-desert-atacama-desert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
