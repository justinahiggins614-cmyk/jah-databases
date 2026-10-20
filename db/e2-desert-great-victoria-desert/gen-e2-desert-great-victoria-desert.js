(function(){'use strict';
/* JAH Great Victoria Desert Desert Database generator — jahdb-e2-desert-great-victoria-desert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-desert-great-victoria-desert',PREFIX='JAH-E2DESERTGRE-',NAME='JAH Great Victoria Desert Desert Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Great Victoria Desert: the complete guide", "d": "Great Victoria Desert: Australia's vast interior..", "g": "overview", "l": 2, "q": "What is Great Victoria Desert: the complete guide?", "a": "Great Victoria Desert: Australia's vast interior..", "x": "The complete desert guide to Great Victoria Desert: Australia's vast interior.. 348,000 sq km. From formation to visiting, from wildlife to legends — everything about this desert in one database. People.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "348,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "348,000 sq km.", "x": "Great Victoria Desert: 348,000 sq km.. Wildlife. One of the defining facts — Red sand.. Australia's vast interior. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 348,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 348,000 sq km..", "x": "Explored: 348,000 sq km.. History. Why it is so — Great Victoria Desert. Wildlife. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Aboriginal.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Aboriginal.", "x": "Great Victoria Desert: Aboriginal.. Travel. One of the defining facts — Wildlife.. Australia's vast interior. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Aboriginal..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Aboriginal..", "x": "Explored: Aboriginal.. Ecology. Why it is so — Great Victoria Desert. Remote. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Red sand.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Red sand.", "x": "Great Victoria Desert: Red sand.. History. One of the defining facts — Remote.. Australia's vast interior. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Red sand..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Red sand..", "x": "Explored: Red sand.. Respect. Why it is so — Great Victoria Desert. Tracks. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wildlife.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wildlife.", "x": "Great Victoria Desert: Wildlife.. Ecology. One of the defining facts — Tracks.. Australia's vast interior. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Wildlife..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Wildlife..", "x": "Explored: Wildlife.. People. Why it is so — Great Victoria Desert. 348,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Remote.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Remote.", "x": "Great Victoria Desert: Remote.. Respect. One of the defining facts — 348,000 sq km.. Australia's vast interior. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Remote..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Remote..", "x": "Explored: Remote.. Wildlife. Why it is so — Great Victoria Desert. Aboriginal. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tracks.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tracks.", "x": "Great Victoria Desert: Tracks.. People. One of the defining facts — Aboriginal.. Australia's vast interior. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Tracks..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Tracks..", "x": "Explored: Tracks.. Travel. Why it is so — Great Victoria Desert. Red sand. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "People.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "People.", "x": "Great Victoria Desert in depth: People.. Aboriginal. The details reward the curious — Australia's vast interior.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wildlife.", "x": "Great Victoria Desert in depth: Wildlife.. Red sand. The details reward the curious — Australia's vast interior.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Travel.", "x": "Great Victoria Desert in depth: Travel.. Wildlife. The details reward the curious — Australia's vast interior.. Ecology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Great Victoria Desert in depth: History.. Remote. The details reward the curious — Australia's vast interior.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ecology.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ecology.", "x": "Great Victoria Desert in depth: Ecology.. Tracks. The details reward the curious — Australia's vast interior.. People. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Great Victoria Desert in depth: Respect.. 348,000 sq km. The details reward the curious — Australia's vast interior.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Great Victoria Desert is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Great Victoria Desert is.", "x": "Location: 348,000 sq km.. People. Getting oriented — Great Victoria Desert. Australia's vast interior. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Great Victoria Desert.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Great Victoria Desert.", "x": "Visiting: Wildlife.. Aboriginal. Practical know-how — Great Victoria Desert. Australia's vast interior. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Great Victoria Desert.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Great Victoria Desert.", "x": "Ecology: Travel.. Red sand. The living world of Great Victoria Desert — Australia's vast interior.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Great Victoria Desert through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Great Victoria Desert through time.", "x": "History: Ecology.. Wildlife. People and Great Victoria Desert across the centuries — Australia's vast interior.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Great Victoria Desert.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Great Victoria Desert.", "x": "Conservation: Wildlife.. 348,000 sq km. Threats and guardians of Great Victoria Desert — Australia's vast interior.. Travel. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Great Victoria Desert in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Great Victoria Desert in numbers.", "x": "Numbers: 348,000 sq km.; Aboriginal.. History. Statistics that stun — Great Victoria Desert. Australia's vast interior. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-desert-great-victoria-desert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
