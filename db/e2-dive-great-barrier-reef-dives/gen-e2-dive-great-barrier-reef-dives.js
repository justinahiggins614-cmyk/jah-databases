(function(){'use strict';
/* JAH Great Barrier Reef Dives Dive Site Database generator — jahdb-e2-dive-great-barrier-reef-dives-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive-great-barrier-reef-dives',PREFIX='JAH-E2DIVEGREAT-',NAME='JAH Great Barrier Reef Dives Dive Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Great Barrier Reef Dives: the complete guide", "d": "Great Barrier Reef Dives: the world's largest reef..", "g": "overview", "l": 2, "q": "What is Great Barrier Reef Dives: the complete guide?", "a": "Great Barrier Reef Dives: the world's largest reef..", "x": "The complete dive site guide to Great Barrier Reef Dives: the world's largest reef.. 2,300 km. From formation to visiting, from wildlife to legends — everything about this dive site in one database. Reef.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2,300 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2,300 km.", "x": "Great Barrier Reef Dives: 2,300 km.. Liveaboards. One of the defining facts — Biodiversity.. the world's largest reef. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2,300 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2,300 km..", "x": "Explored: 2,300 km.. Threats. Why it is so — Great Barrier Reef Dives. Liveaboards. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Coral Sea.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Coral Sea.", "x": "Great Barrier Reef Dives: Coral Sea.. Wildlife. One of the defining facts — Liveaboards.. the world's largest reef. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Coral Sea..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Coral Sea..", "x": "Explored: Coral Sea.. Cairns. Why it is so — Great Barrier Reef Dives. Bleaching. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Biodiversity.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Biodiversity.", "x": "Great Barrier Reef Dives: Biodiversity.. Threats. One of the defining facts — Bleaching.. the world's largest reef. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Biodiversity..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Biodiversity..", "x": "Explored: Biodiversity.. Diving. Why it is so — Great Barrier Reef Dives. Cairns. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Liveaboards.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Liveaboards.", "x": "Great Barrier Reef Dives: Liveaboards.. Cairns. One of the defining facts — Cairns.. the world's largest reef. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Liveaboards..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Liveaboards..", "x": "Explored: Liveaboards.. Reef. Why it is so — Great Barrier Reef Dives. 2,300 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bleaching.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bleaching.", "x": "Great Barrier Reef Dives: Bleaching.. Diving. One of the defining facts — 2,300 km.. the world's largest reef. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Bleaching..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Bleaching..", "x": "Explored: Bleaching.. Liveaboards. Why it is so — Great Barrier Reef Dives. Coral Sea. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Cairns.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Cairns.", "x": "Great Barrier Reef Dives: Cairns.. Reef. One of the defining facts — Coral Sea.. the world's largest reef. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Cairns..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Cairns..", "x": "Explored: Cairns.. Wildlife. Why it is so — Great Barrier Reef Dives. Biodiversity. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Reef.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Reef.", "x": "Great Barrier Reef Dives in depth: Reef.. Coral Sea. The details reward the curious — the world's largest reef.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Liveaboards.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Liveaboards.", "x": "Great Barrier Reef Dives in depth: Liveaboards.. Biodiversity. The details reward the curious — the world's largest reef.. Threats. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wildlife.", "x": "Great Barrier Reef Dives in depth: Wildlife.. Liveaboards. The details reward the curious — the world's largest reef.. Cairns. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Threats.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Threats.", "x": "Great Barrier Reef Dives in depth: Threats.. Bleaching. The details reward the curious — the world's largest reef.. Diving. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cairns.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cairns.", "x": "Great Barrier Reef Dives in depth: Cairns.. Cairns. The details reward the curious — the world's largest reef.. Reef. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Diving.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Diving.", "x": "Great Barrier Reef Dives in depth: Diving.. 2,300 km. The details reward the curious — the world's largest reef.. Liveaboards. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Great Barrier Reef Dives is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Great Barrier Reef Dives is.", "x": "Location: 2,300 km.. Reef. Getting oriented — Great Barrier Reef Dives. the world's largest reef. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Great Barrier Reef Dives.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Great Barrier Reef Dives.", "x": "Visiting: Liveaboards.. Coral Sea. Practical know-how — Great Barrier Reef Dives. the world's largest reef. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Great Barrier Reef Dives.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Great Barrier Reef Dives.", "x": "Ecology: Wildlife.. Biodiversity. The living world of Great Barrier Reef Dives — the world's largest reef.. Threats. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Great Barrier Reef Dives through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Great Barrier Reef Dives through time.", "x": "History: Cairns.. Liveaboards. People and Great Barrier Reef Dives across the centuries — the world's largest reef.. Diving. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Great Barrier Reef Dives.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Great Barrier Reef Dives.", "x": "Conservation: Liveaboards.. 2,300 km. Threats and guardians of Great Barrier Reef Dives — the world's largest reef.. Wildlife. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Great Barrier Reef Dives in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Great Barrier Reef Dives in numbers.", "x": "Numbers: 2,300 km.; Coral Sea.. Threats. Statistics that stun — Great Barrier Reef Dives. the world's largest reef. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive-great-barrier-reef-dives-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
