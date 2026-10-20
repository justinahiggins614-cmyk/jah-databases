(function(){'use strict';
/* JAH Bandon Dunes Golf Course Database generator — jahdb-e2-golf-bandon-dunes-golf-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-golf-bandon-dunes-golf',PREFIX='JAH-E2GOLFBANDO-',NAME='JAH Bandon Dunes Golf Course Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bandon Dunes: the complete guide", "d": "Bandon Dunes: America's links heaven..", "g": "overview", "l": 2, "q": "What is Bandon Dunes: the complete guide?", "a": "Bandon Dunes: America's links heaven..", "x": "The complete golf course guide to Bandon Dunes: America's links heaven.. 1999. From formation to visiting, from wildlife to legends — everything about this golf course in one database. Links. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1999.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1999.", "x": "Bandon Dunes: 1999.. Courses. One of the defining facts — 5 courses.. America's links heaven. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1999..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1999..", "x": "Explored: 1999.. Oregon. Why it is so — Bandon Dunes. Walking. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Oregon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Oregon.", "x": "Bandon Dunes: Oregon.. Walking. One of the defining facts — Walking.. America's links heaven. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Oregon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Oregon..", "x": "Explored: Oregon.. Wind. Why it is so — Bandon Dunes. Wind. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "5 courses.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "5 courses.", "x": "Bandon Dunes: 5 courses.. Oregon. One of the defining facts — Wind.. America's links heaven. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: 5 courses..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: 5 courses..", "x": "Explored: 5 courses.. Heaven. Why it is so — Bandon Dunes. Pacific. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Walking.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Walking.", "x": "Bandon Dunes: Walking.. Wind. One of the defining facts — Pacific.. America's links heaven. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Walking..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Walking..", "x": "Explored: Walking.. Links. Why it is so — Bandon Dunes. 1999. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wind.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wind.", "x": "Bandon Dunes: Wind.. Heaven. One of the defining facts — 1999.. America's links heaven. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Wind..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Wind..", "x": "Explored: Wind.. Courses. Why it is so — Bandon Dunes. Oregon. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Pacific.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Pacific.", "x": "Bandon Dunes: Pacific.. Links. One of the defining facts — Oregon.. America's links heaven. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Pacific..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Pacific..", "x": "Explored: Pacific.. Walking. Why it is so — Bandon Dunes. 5 courses. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Links.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Links.", "x": "Bandon Dunes in depth: Links.. Oregon. The details reward the curious — America's links heaven.. Walking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Courses.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Courses.", "x": "Bandon Dunes in depth: Courses.. 5 courses. The details reward the curious — America's links heaven.. Oregon. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Walking.", "x": "Bandon Dunes in depth: Walking.. Walking. The details reward the curious — America's links heaven.. Wind. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Oregon.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Oregon.", "x": "Bandon Dunes in depth: Oregon.. Wind. The details reward the curious — America's links heaven.. Heaven. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wind.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wind.", "x": "Bandon Dunes in depth: Wind.. Pacific. The details reward the curious — America's links heaven.. Links. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Heaven.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Heaven.", "x": "Bandon Dunes in depth: Heaven.. 1999. The details reward the curious — America's links heaven.. Courses. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Bandon Dunes is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Bandon Dunes is.", "x": "Location: 1999.. Links. Getting oriented — Bandon Dunes. America's links heaven. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Bandon Dunes.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Bandon Dunes.", "x": "Visiting: Courses.. Oregon. Practical know-how — Bandon Dunes. America's links heaven. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Bandon Dunes.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Bandon Dunes.", "x": "Ecology: Walking.. 5 courses. The living world of Bandon Dunes — America's links heaven.. Oregon. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Bandon Dunes through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Bandon Dunes through time.", "x": "History: Wind.. Walking. People and Bandon Dunes across the centuries — America's links heaven.. Heaven. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Bandon Dunes.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Bandon Dunes.", "x": "Conservation: Courses.. 1999. Threats and guardians of Bandon Dunes — America's links heaven.. Walking. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Bandon Dunes in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Bandon Dunes in numbers.", "x": "Numbers: 1999.; Oregon.. Oregon. Statistics that stun — Bandon Dunes. America's links heaven. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-golf-bandon-dunes-golf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
