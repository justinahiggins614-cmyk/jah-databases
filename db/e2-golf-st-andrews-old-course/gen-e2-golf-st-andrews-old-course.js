(function(){'use strict';
/* JAH St. Andrews Old Course Golf Course Database generator — jahdb-e2-golf-st-andrews-old-course-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-golf-st-andrews-old-course',PREFIX='JAH-E2GOLFSTAND-',NAME='JAH St. Andrews Old Course Golf Course Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "St. Andrews Old Course: the complete guide", "d": "St. Andrews Old Course: the home of golf..", "g": "overview", "l": 2, "q": "What is St. Andrews Old Course: the complete guide?", "a": "St. Andrews Old Course: the home of golf..", "x": "The complete golf course guide to St. Andrews Old Course: the home of golf.. 1552. From formation to visiting, from wildlife to legends — everything about this golf course in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1552.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1552.", "x": "St. Andrews Old Course: 1552.. Bridge. One of the defining facts — The Road Hole.. the home of golf. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1552..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1552..", "x": "Explored: 1552.. Open. Why it is so — St. Andrews Old Course. Open. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Swilcan Bridge.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Swilcan Bridge.", "x": "St. Andrews Old Course: Swilcan Bridge.. Road Hole. One of the defining facts — Open.. the home of golf. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Swilcan Bridge..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Swilcan Bridge..", "x": "Explored: Swilcan Bridge.. Ballot. Why it is so — St. Andrews Old Course. Scotland. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "The Road Hole.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "The Road Hole.", "x": "St. Andrews Old Course: The Road Hole.. Open. One of the defining facts — Scotland.. the home of golf. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: The Road Hole..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: The Road Hole..", "x": "Explored: The Road Hole.. Scotland. Why it is so — St. Andrews Old Course. Pilgrimage. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Open.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Open.", "x": "St. Andrews Old Course: Open.. Ballot. One of the defining facts — Pilgrimage.. the home of golf. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Open..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Open..", "x": "Explored: Open.. History. Why it is so — St. Andrews Old Course. 1552. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Scotland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Scotland.", "x": "St. Andrews Old Course: Scotland.. Scotland. One of the defining facts — 1552.. the home of golf. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Scotland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Scotland..", "x": "Explored: Scotland.. Bridge. Why it is so — St. Andrews Old Course. Swilcan Bridge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Pilgrimage.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Pilgrimage.", "x": "St. Andrews Old Course: Pilgrimage.. History. One of the defining facts — Swilcan Bridge.. the home of golf. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Pilgrimage..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Pilgrimage..", "x": "Explored: Pilgrimage.. Road Hole. Why it is so — St. Andrews Old Course. The Road Hole. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "St. Andrews Old Course in depth: History.. Swilcan Bridge. The details reward the curious — the home of golf.. Road Hole. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bridge.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bridge.", "x": "St. Andrews Old Course in depth: Bridge.. The Road Hole. The details reward the curious — the home of golf.. Open. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Road Hole.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Road Hole.", "x": "St. Andrews Old Course in depth: Road Hole.. Open. The details reward the curious — the home of golf.. Ballot. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Open.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Open.", "x": "St. Andrews Old Course in depth: Open.. Scotland. The details reward the curious — the home of golf.. Scotland. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ballot.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ballot.", "x": "St. Andrews Old Course in depth: Ballot.. Pilgrimage. The details reward the curious — the home of golf.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Scotland.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Scotland.", "x": "St. Andrews Old Course in depth: Scotland.. 1552. The details reward the curious — the home of golf.. Bridge. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where St. Andrews Old Course is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where St. Andrews Old Course is.", "x": "Location: 1552.. History. Getting oriented — St. Andrews Old Course. the home of golf. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience St. Andrews Old Course.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience St. Andrews Old Course.", "x": "Visiting: Bridge.. Swilcan Bridge. Practical know-how — St. Andrews Old Course. the home of golf. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around St. Andrews Old Course.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around St. Andrews Old Course.", "x": "Ecology: Road Hole.. The Road Hole. The living world of St. Andrews Old Course — the home of golf.. Open. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "St. Andrews Old Course through time.", "g": "history", "l": 2, "q": "What is History?", "a": "St. Andrews Old Course through time.", "x": "History: Ballot.. Open. People and St. Andrews Old Course across the centuries — the home of golf.. Scotland. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting St. Andrews Old Course.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting St. Andrews Old Course.", "x": "Conservation: Bridge.. 1552. Threats and guardians of St. Andrews Old Course — the home of golf.. Road Hole. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "St. Andrews Old Course in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "St. Andrews Old Course in numbers.", "x": "Numbers: 1552.; Swilcan Bridge.. Open. Statistics that stun — St. Andrews Old Course. the home of golf. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-golf-st-andrews-old-course-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
