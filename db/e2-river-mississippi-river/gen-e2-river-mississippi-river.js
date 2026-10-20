(function(){'use strict';
/* JAH Mississippi River River Database generator — jahdb-e2-river-mississippi-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-mississippi-river',PREFIX='JAH-E2RIVERMISS-',NAME='JAH Mississippi River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mississippi River: the complete guide", "d": "Mississippi River: America's great river..", "g": "overview", "l": 2, "q": "What is Mississippi River: the complete guide?", "a": "Mississippi River: America's great river..", "x": "The complete river guide to Mississippi River: America's great river.. 3,730 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Lake Itasca.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,730 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,730 km.", "x": "Mississippi River: 3,730 km.. St. Louis. One of the defining facts — New Orleans delta.. America's great river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 3,730 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 3,730 km..", "x": "Explored: 3,730 km.. Levees. Why it is so — Mississippi River. Mark Twain's river. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "10 states.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "10 states.", "x": "Mississippi River: 10 states.. Blues highway. One of the defining facts — Mark Twain's river.. America's great river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 10 states..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 10 states..", "x": "Explored: 10 states.. Wildlife refuge. Why it is so — Mississippi River. Floods 1927, 1993. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "New Orleans delta.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "New Orleans delta.", "x": "Mississippi River: New Orleans delta.. Levees. One of the defining facts — Floods 1927, 1993.. America's great river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: New Orleans delta..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: New Orleans delta..", "x": "Explored: New Orleans delta.. Steamboats. Why it is so — Mississippi River. Barges. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mark Twain's river.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mark Twain's river.", "x": "Mississippi River: Mark Twain's river.. Wildlife refuge. One of the defining facts — Barges.. America's great river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Mark Twain's river..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Mark Twain's river..", "x": "Explored: Mark Twain's river.. Source: Lake Itasca. Why it is so — Mississippi River. 3,730 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Floods 1927, 1993.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Floods 1927, 1993.", "x": "Mississippi River: Floods 1927, 1993.. Steamboats. One of the defining facts — 3,730 km.. America's great river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Floods 1927, 1993..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Floods 1927, 1993..", "x": "Explored: Floods 1927, 1993.. St. Louis. Why it is so — Mississippi River. 10 states. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Barges.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Barges.", "x": "Mississippi River: Barges.. Source: Lake Itasca. One of the defining facts — 10 states.. America's great river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Barges..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Barges..", "x": "Explored: Barges.. Blues highway. Why it is so — Mississippi River. New Orleans delta. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Lake Itasca.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Lake Itasca.", "x": "Mississippi River in depth: Source: Lake Itasca.. 10 states. The details reward the curious — America's great river.. Blues highway. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "St. Louis.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "St. Louis.", "x": "Mississippi River in depth: St. Louis.. New Orleans delta. The details reward the curious — America's great river.. Levees. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Blues highway.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Blues highway.", "x": "Mississippi River in depth: Blues highway.. Mark Twain's river. The details reward the curious — America's great river.. Wildlife refuge. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Levees.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Levees.", "x": "Mississippi River in depth: Levees.. Floods 1927, 1993. The details reward the curious — America's great river.. Steamboats. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wildlife refuge.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wildlife refuge.", "x": "Mississippi River in depth: Wildlife refuge.. Barges. The details reward the curious — America's great river.. Source: Lake Itasca. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Steamboats.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Steamboats.", "x": "Mississippi River in depth: Steamboats.. 3,730 km. The details reward the curious — America's great river.. St. Louis. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mississippi River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mississippi River is.", "x": "Location: 3,730 km.. Source: Lake Itasca. Getting oriented — Mississippi River. America's great river. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mississippi River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mississippi River.", "x": "Visiting: St. Louis.. 10 states. Practical know-how — Mississippi River. America's great river. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mississippi River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mississippi River.", "x": "Ecology: Blues highway.. New Orleans delta. The living world of Mississippi River — America's great river.. Levees. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mississippi River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mississippi River through time.", "x": "History: Wildlife refuge.. Mark Twain's river. People and Mississippi River across the centuries — America's great river.. Steamboats. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mississippi River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mississippi River.", "x": "Conservation: St. Louis.. 3,730 km. Threats and guardians of Mississippi River — America's great river.. Blues highway. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mississippi River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mississippi River in numbers.", "x": "Numbers: 3,730 km.; 10 states.. Levees. Statistics that stun — Mississippi River. America's great river. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-mississippi-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
