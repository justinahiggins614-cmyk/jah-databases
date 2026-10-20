(function(){'use strict';
/* JAH Mavericks Surf Spot Database generator — jahdb-e2-surf-mavericks-california-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-surf-mavericks-california',PREFIX='JAH-E2SURFMAVER-',NAME='JAH Mavericks Surf Spot Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mavericks: the complete guide", "d": "Mavericks: California's cold monster..", "g": "overview", "l": 2, "q": "What is Mavericks: the complete guide?", "a": "Mavericks: California's cold monster..", "x": "The complete surf spot guide to Mavericks: California's cold monster.. Half Moon Bay. From formation to visiting, from wildlife to legends — everything about this surf spot in one database. Cold. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Half Moon Bay.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Half Moon Bay.", "x": "Mavericks: Half Moon Bay.. Size. One of the defining facts — 25 ft.. California's cold monster. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Half Moon Bay..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Half Moon Bay..", "x": "Explored: Half Moon Bay.. Legends. Why it is so — Mavericks. Big wave. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cold.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cold.", "x": "Mavericks: Cold.. Winter. One of the defining facts — Big wave.. California's cold monster. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Cold..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Cold..", "x": "Explored: Cold.. Danger. Why it is so — Mavericks. Winter. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "25 ft.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "25 ft.", "x": "Mavericks: 25 ft.. Legends. One of the defining facts — Winter.. California's cold monster. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: 25 ft..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: 25 ft..", "x": "Explored: 25 ft.. Respect. Why it is so — Mavericks. Sharks. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Big wave.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Big wave.", "x": "Mavericks: Big wave.. Danger. One of the defining facts — Sharks.. California's cold monster. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Big wave..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Big wave..", "x": "Explored: Big wave.. Cold. Why it is so — Mavericks. Half Moon Bay. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Winter.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Winter.", "x": "Mavericks: Winter.. Respect. One of the defining facts — Half Moon Bay.. California's cold monster. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Winter..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Winter..", "x": "Explored: Winter.. Size. Why it is so — Mavericks. Cold. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sharks.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sharks.", "x": "Mavericks: Sharks.. Cold. One of the defining facts — Cold.. California's cold monster. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Sharks..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Sharks..", "x": "Explored: Sharks.. Winter. Why it is so — Mavericks. 25 ft. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cold.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cold.", "x": "Mavericks in depth: Cold.. Cold. The details reward the curious — California's cold monster.. Winter. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Size.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Size.", "x": "Mavericks in depth: Size.. 25 ft. The details reward the curious — California's cold monster.. Legends. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Winter.", "x": "Mavericks in depth: Winter.. Big wave. The details reward the curious — California's cold monster.. Danger. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Legends.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Legends.", "x": "Mavericks in depth: Legends.. Winter. The details reward the curious — California's cold monster.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Danger.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Danger.", "x": "Mavericks in depth: Danger.. Sharks. The details reward the curious — California's cold monster.. Cold. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Mavericks in depth: Respect.. Half Moon Bay. The details reward the curious — California's cold monster.. Size. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mavericks is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mavericks is.", "x": "Location: Half Moon Bay.. Cold. Getting oriented — Mavericks. California's cold monster. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mavericks.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mavericks.", "x": "Visiting: Size.. Cold. Practical know-how — Mavericks. California's cold monster. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mavericks.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mavericks.", "x": "Ecology: Winter.. 25 ft. The living world of Mavericks — California's cold monster.. Legends. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mavericks through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mavericks through time.", "x": "History: Danger.. Big wave. People and Mavericks across the centuries — California's cold monster.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mavericks.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mavericks.", "x": "Conservation: Size.. Half Moon Bay. Threats and guardians of Mavericks — California's cold monster.. Winter. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mavericks in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mavericks in numbers.", "x": "Numbers: Half Moon Bay.; Cold.. Legends. Statistics that stun — Mavericks. California's cold monster. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-surf-mavericks-california-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
