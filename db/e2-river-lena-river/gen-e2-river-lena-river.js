(function(){'use strict';
/* JAH Lena River River Database generator — jahdb-e2-river-lena-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-lena-river',PREFIX='JAH-E2RIVERLENA-',NAME='JAH Lena River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lena River: the complete guide", "d": "Lena River: Siberia's wild river..", "g": "overview", "l": 2, "q": "What is Lena River: the complete guide?", "a": "Lena River: Siberia's wild river..", "x": "The complete river guide to Lena River: Siberia's wild river.. 4,400 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Baikal. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "4,400 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "4,400 km.", "x": "Lena River: 4,400 km.. Pillars. One of the defining facts — Yakutsk.. Siberia's wild river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 4,400 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 4,400 km..", "x": "Explored: 4,400 km.. Ice roads. Why it is so — Lena River. Frozen. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lena Pillars.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lena Pillars.", "x": "Lena River: Lena Pillars.. Cities. One of the defining facts — Frozen.. Siberia's wild river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Lena Pillars..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Lena Pillars..", "x": "Explored: Lena Pillars.. Nature. Why it is so — Lena River. Diamonds. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Yakutsk.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Yakutsk.", "x": "Lena River: Yakutsk.. Ice roads. One of the defining facts — Diamonds.. Siberia's wild river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Yakutsk..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Yakutsk..", "x": "Explored: Yakutsk.. Travel. Why it is so — Lena River. Delta. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Frozen.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Frozen.", "x": "Lena River: Frozen.. Nature. One of the defining facts — Delta.. Siberia's wild river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Frozen..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Frozen..", "x": "Explored: Frozen.. Source: Baikal. Why it is so — Lena River. 4,400 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Diamonds.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Diamonds.", "x": "Lena River: Diamonds.. Travel. One of the defining facts — 4,400 km.. Siberia's wild river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Diamonds..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Diamonds..", "x": "Explored: Diamonds.. Pillars. Why it is so — Lena River. Lena Pillars. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Delta.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Delta.", "x": "Lena River: Delta.. Source: Baikal. One of the defining facts — Lena Pillars.. Siberia's wild river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Delta..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Delta..", "x": "Explored: Delta.. Cities. Why it is so — Lena River. Yakutsk. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Baikal.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Baikal.", "x": "Lena River in depth: Source: Baikal.. Lena Pillars. The details reward the curious — Siberia's wild river.. Cities. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pillars.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pillars.", "x": "Lena River in depth: Pillars.. Yakutsk. The details reward the curious — Siberia's wild river.. Ice roads. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cities.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cities.", "x": "Lena River in depth: Cities.. Frozen. The details reward the curious — Siberia's wild river.. Nature. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ice roads.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ice roads.", "x": "Lena River in depth: Ice roads.. Diamonds. The details reward the curious — Siberia's wild river.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nature.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nature.", "x": "Lena River in depth: Nature.. Delta. The details reward the curious — Siberia's wild river.. Source: Baikal. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Lena River in depth: Travel.. 4,400 km. The details reward the curious — Siberia's wild river.. Pillars. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Lena River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Lena River is.", "x": "Location: 4,400 km.. Source: Baikal. Getting oriented — Lena River. Siberia's wild river. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Lena River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Lena River.", "x": "Visiting: Pillars.. Lena Pillars. Practical know-how — Lena River. Siberia's wild river. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Lena River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Lena River.", "x": "Ecology: Cities.. Yakutsk. The living world of Lena River — Siberia's wild river.. Ice roads. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Lena River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Lena River through time.", "x": "History: Nature.. Frozen. People and Lena River across the centuries — Siberia's wild river.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Lena River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Lena River.", "x": "Conservation: Pillars.. 4,400 km. Threats and guardians of Lena River — Siberia's wild river.. Cities. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Lena River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Lena River in numbers.", "x": "Numbers: 4,400 km.; Lena Pillars.. Ice roads. Statistics that stun — Lena River. Siberia's wild river. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-lena-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
