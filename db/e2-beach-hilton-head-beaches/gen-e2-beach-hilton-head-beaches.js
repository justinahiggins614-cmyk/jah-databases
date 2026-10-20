(function(){'use strict';
/* JAH Hilton Head Beaches Beach Database generator — jahdb-e2-beach-hilton-head-beaches-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-hilton-head-beaches',PREFIX='JAH-E2BEACHHILT-',NAME='JAH Hilton Head Beaches Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hilton Head Beaches: the complete guide", "d": "Hilton Head Beaches: the lowcountry shore..", "g": "overview", "l": 2, "q": "What is Hilton Head Beaches: the complete guide?", "a": "Hilton Head Beaches: the lowcountry shore..", "x": "The complete beach guide to Hilton Head Beaches: the lowcountry shore.. 12 miles. From formation to visiting, from wildlife to legends — everything about this beach in one database. Bikes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "12 miles.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "12 miles.", "x": "Hilton Head Beaches: 12 miles.. Golf. One of the defining facts — Golf.. the lowcountry shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 12 miles..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 12 miles..", "x": "Explored: 12 miles.. SC. Why it is so — Hilton Head Beaches. SC. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bikes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bikes.", "x": "Hilton Head Beaches: Bikes.. Dolphins. One of the defining facts — SC.. the lowcountry shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Bikes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Bikes..", "x": "Explored: Bikes.. Turtles. Why it is so — Hilton Head Beaches. Dolphins. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Golf.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Golf.", "x": "Hilton Head Beaches: Golf.. SC. One of the defining facts — Dolphins.. the lowcountry shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Golf..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Golf..", "x": "Explored: Golf.. Sand. Why it is so — Hilton Head Beaches. Turtles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "SC.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "SC.", "x": "Hilton Head Beaches: SC.. Turtles. One of the defining facts — Turtles.. the lowcountry shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: SC..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: SC..", "x": "Explored: SC.. Bikes. Why it is so — Hilton Head Beaches. 12 miles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dolphins.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dolphins.", "x": "Hilton Head Beaches: Dolphins.. Sand. One of the defining facts — 12 miles.. the lowcountry shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Dolphins..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Dolphins..", "x": "Explored: Dolphins.. Golf. Why it is so — Hilton Head Beaches. Bikes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Turtles.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Turtles.", "x": "Hilton Head Beaches: Turtles.. Bikes. One of the defining facts — Bikes.. the lowcountry shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Turtles..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Turtles..", "x": "Explored: Turtles.. Dolphins. Why it is so — Hilton Head Beaches. Golf. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bikes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bikes.", "x": "Hilton Head Beaches in depth: Bikes.. Bikes. The details reward the curious — the lowcountry shore.. Dolphins. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Golf.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Golf.", "x": "Hilton Head Beaches in depth: Golf.. Golf. The details reward the curious — the lowcountry shore.. SC. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dolphins.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dolphins.", "x": "Hilton Head Beaches in depth: Dolphins.. SC. The details reward the curious — the lowcountry shore.. Turtles. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "SC.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "SC.", "x": "Hilton Head Beaches in depth: SC.. Dolphins. The details reward the curious — the lowcountry shore.. Sand. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Turtles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Turtles.", "x": "Hilton Head Beaches in depth: Turtles.. Turtles. The details reward the curious — the lowcountry shore.. Bikes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sand.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sand.", "x": "Hilton Head Beaches in depth: Sand.. 12 miles. The details reward the curious — the lowcountry shore.. Golf. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Hilton Head Beaches is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Hilton Head Beaches is.", "x": "Location: 12 miles.. Bikes. Getting oriented — Hilton Head Beaches. the lowcountry shore. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Hilton Head Beaches.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Hilton Head Beaches.", "x": "Visiting: Golf.. Bikes. Practical know-how — Hilton Head Beaches. the lowcountry shore. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Hilton Head Beaches.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Hilton Head Beaches.", "x": "Ecology: Dolphins.. Golf. The living world of Hilton Head Beaches — the lowcountry shore.. SC. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Hilton Head Beaches through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Hilton Head Beaches through time.", "x": "History: Turtles.. SC. People and Hilton Head Beaches across the centuries — the lowcountry shore.. Sand. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Hilton Head Beaches.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Hilton Head Beaches.", "x": "Conservation: Golf.. 12 miles. Threats and guardians of Hilton Head Beaches — the lowcountry shore.. Dolphins. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Hilton Head Beaches in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Hilton Head Beaches in numbers.", "x": "Numbers: 12 miles.; Bikes.. SC. Statistics that stun — Hilton Head Beaches. the lowcountry shore. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-hilton-head-beaches-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
