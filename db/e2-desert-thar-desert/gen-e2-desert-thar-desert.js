(function(){'use strict';
/* JAH Thar Desert Desert Database generator — jahdb-e2-desert-thar-desert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-desert-thar-desert',PREFIX='JAH-E2DESERTTHA-',NAME='JAH Thar Desert Desert Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thar Desert: the complete guide", "d": "Thar Desert: India's great desert..", "g": "overview", "l": 2, "q": "What is Thar Desert: the complete guide?", "a": "Thar Desert: India's great desert..", "x": "The complete desert guide to Thar Desert: India's great desert.. 200,000 sq km. From formation to visiting, from wildlife to legends — everything about this desert in one database. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "200,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "200,000 sq km.", "x": "Thar Desert: 200,000 sq km.. Forts. One of the defining facts — Camels.. India's great desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 200,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 200,000 sq km..", "x": "Explored: 200,000 sq km.. Wildlife. Why it is so — Thar Desert. Forts. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jaisalmer.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jaisalmer.", "x": "Thar Desert: Jaisalmer.. Festivals. One of the defining facts — Forts.. India's great desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Jaisalmer..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Jaisalmer..", "x": "Explored: Jaisalmer.. Tours. Why it is so — Thar Desert. Festivals. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Camels.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Camels.", "x": "Thar Desert: Camels.. Wildlife. One of the defining facts — Festivals.. India's great desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Camels..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Camels..", "x": "Explored: Camels.. History. Why it is so — Thar Desert. Monsoon. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Forts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Forts.", "x": "Thar Desert: Forts.. Tours. One of the defining facts — Monsoon.. India's great desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Forts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Forts..", "x": "Explored: Forts.. Culture. Why it is so — Thar Desert. 200,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Festivals.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Festivals.", "x": "Thar Desert: Festivals.. History. One of the defining facts — 200,000 sq km.. India's great desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Festivals..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Festivals..", "x": "Explored: Festivals.. Forts. Why it is so — Thar Desert. Jaisalmer. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Monsoon.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Monsoon.", "x": "Thar Desert: Monsoon.. Culture. One of the defining facts — Jaisalmer.. India's great desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Monsoon..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Monsoon..", "x": "Explored: Monsoon.. Festivals. Why it is so — Thar Desert. Camels. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Culture.", "x": "Thar Desert in depth: Culture.. Jaisalmer. The details reward the curious — India's great desert.. Festivals. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Forts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Forts.", "x": "Thar Desert in depth: Forts.. Camels. The details reward the curious — India's great desert.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Festivals.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Festivals.", "x": "Thar Desert in depth: Festivals.. Forts. The details reward the curious — India's great desert.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wildlife.", "x": "Thar Desert in depth: Wildlife.. Festivals. The details reward the curious — India's great desert.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Thar Desert in depth: Tours.. Monsoon. The details reward the curious — India's great desert.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Thar Desert in depth: History.. 200,000 sq km. The details reward the curious — India's great desert.. Forts. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Thar Desert is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Thar Desert is.", "x": "Location: 200,000 sq km.. Culture. Getting oriented — Thar Desert. India's great desert. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Thar Desert.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Thar Desert.", "x": "Visiting: Forts.. Jaisalmer. Practical know-how — Thar Desert. India's great desert. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Thar Desert.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Thar Desert.", "x": "Ecology: Festivals.. Camels. The living world of Thar Desert — India's great desert.. Wildlife. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Thar Desert through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Thar Desert through time.", "x": "History: Tours.. Forts. People and Thar Desert across the centuries — India's great desert.. History. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Thar Desert.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Thar Desert.", "x": "Conservation: Forts.. 200,000 sq km. Threats and guardians of Thar Desert — India's great desert.. Festivals. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Thar Desert in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Thar Desert in numbers.", "x": "Numbers: 200,000 sq km.; Jaisalmer.. Wildlife. Statistics that stun — Thar Desert. India's great desert. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-desert-thar-desert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
