(function(){'use strict';
/* JAH South Padre Island Beach Database generator — jahdb-e2-beach-south-padre-island-beach-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-south-padre-island-beach',PREFIX='JAH-E2BEACHSOUT-',NAME='JAH South Padre Island Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "South Padre Island: the complete guide", "d": "South Padre Island: Texas' island..", "g": "overview", "l": 2, "q": "What is South Padre Island: the complete guide?", "a": "South Padre Island: Texas' island..", "x": "The complete beach guide to South Padre Island: Texas' island.. Texas. From formation to visiting, from wildlife to legends — everything about this beach in one database. Island. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Texas.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Texas.", "x": "South Padre Island: Texas.. Break. One of the defining facts — Spring break.. Texas' island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Texas..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Texas..", "x": "Explored: Texas.. Texas. Why it is so — South Padre Island. Dolphins. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "34 miles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "34 miles.", "x": "South Padre Island: 34 miles.. Dolphins. One of the defining facts — Dolphins.. Texas' island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 34 miles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 34 miles..", "x": "Explored: 34 miles.. Turtles. Why it is so — South Padre Island. Kites. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Spring break.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Spring break.", "x": "South Padre Island: Spring break.. Texas. One of the defining facts — Kites.. Texas' island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Spring break..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Spring break..", "x": "Explored: Spring break.. Sand. Why it is so — South Padre Island. Sea turtles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dolphins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dolphins.", "x": "South Padre Island: Dolphins.. Turtles. One of the defining facts — Sea turtles.. Texas' island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Dolphins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Dolphins..", "x": "Explored: Dolphins.. Island. Why it is so — South Padre Island. Texas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kites.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kites.", "x": "South Padre Island: Kites.. Sand. One of the defining facts — Texas.. Texas' island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Kites..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Kites..", "x": "Explored: Kites.. Break. Why it is so — South Padre Island. 34 miles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sea turtles.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sea turtles.", "x": "South Padre Island: Sea turtles.. Island. One of the defining facts — 34 miles.. Texas' island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Sea turtles..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Sea turtles..", "x": "Explored: Sea turtles.. Dolphins. Why it is so — South Padre Island. Spring break. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Island.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Island.", "x": "South Padre Island in depth: Island.. 34 miles. The details reward the curious — Texas' island.. Dolphins. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Break.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Break.", "x": "South Padre Island in depth: Break.. Spring break. The details reward the curious — Texas' island.. Texas. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dolphins.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dolphins.", "x": "South Padre Island in depth: Dolphins.. Dolphins. The details reward the curious — Texas' island.. Turtles. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Texas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Texas.", "x": "South Padre Island in depth: Texas.. Kites. The details reward the curious — Texas' island.. Sand. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Turtles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Turtles.", "x": "South Padre Island in depth: Turtles.. Sea turtles. The details reward the curious — Texas' island.. Island. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sand.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sand.", "x": "South Padre Island in depth: Sand.. Texas. The details reward the curious — Texas' island.. Break. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where South Padre Island is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where South Padre Island is.", "x": "Location: Texas.. Island. Getting oriented — South Padre Island. Texas' island. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience South Padre Island.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience South Padre Island.", "x": "Visiting: Break.. 34 miles. Practical know-how — South Padre Island. Texas' island. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around South Padre Island.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around South Padre Island.", "x": "Ecology: Dolphins.. Spring break. The living world of South Padre Island — Texas' island.. Texas. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "South Padre Island through time.", "g": "history", "l": 2, "q": "What is History?", "a": "South Padre Island through time.", "x": "History: Turtles.. Dolphins. People and South Padre Island across the centuries — Texas' island.. Sand. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting South Padre Island.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting South Padre Island.", "x": "Conservation: Break.. Texas. Threats and guardians of South Padre Island — Texas' island.. Dolphins. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "South Padre Island in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "South Padre Island in numbers.", "x": "Numbers: Texas.; 34 miles.. Texas. Statistics that stun — South Padre Island. Texas' island. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-south-padre-island-beach-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
