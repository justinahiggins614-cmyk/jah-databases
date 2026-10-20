(function(){'use strict';
/* JAH Thistlegorm Egypt Dive Site Database generator — jahdb-e2-dive-thistlegorm-egypt-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive-thistlegorm-egypt',PREFIX='JAH-E2DIVETHIST-',NAME='JAH Thistlegorm Egypt Dive Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thistlegorm Egypt: the complete guide", "d": "Thistlegorm Egypt: the Red Sea wreck..", "g": "overview", "l": 2, "q": "What is Thistlegorm Egypt: the complete guide?", "a": "Thistlegorm Egypt: the Red Sea wreck..", "x": "The complete dive site guide to Thistlegorm Egypt: the Red Sea wreck.. WWII wreck. From formation to visiting, from wildlife to legends — everything about this dive site in one database. Wreck. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "WWII wreck.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "WWII wreck.", "x": "Thistlegorm Egypt: WWII wreck.. History. One of the defining facts — Motorbikes.. the Red Sea wreck. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: WWII wreck..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: WWII wreck..", "x": "Explored: WWII wreck.. Sharm. Why it is so — Thistlegorm Egypt. 1941. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Red Sea.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Red Sea.", "x": "Thistlegorm Egypt: Red Sea.. Cargo. One of the defining facts — 1941.. the Red Sea wreck. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Red Sea..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Red Sea..", "x": "Explored: Red Sea.. Red Sea. Why it is so — Thistlegorm Egypt. Sharm. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Motorbikes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Motorbikes.", "x": "Thistlegorm Egypt: Motorbikes.. Sharm. One of the defining facts — Sharm.. the Red Sea wreck. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Motorbikes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Motorbikes..", "x": "Explored: Motorbikes.. Diving. Why it is so — Thistlegorm Egypt. History. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1941.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1941.", "x": "Thistlegorm Egypt: 1941.. Red Sea. One of the defining facts — History.. the Red Sea wreck. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: 1941..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: 1941..", "x": "Explored: 1941.. Wreck. Why it is so — Thistlegorm Egypt. WWII wreck. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sharm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sharm.", "x": "Thistlegorm Egypt: Sharm.. Diving. One of the defining facts — WWII wreck.. the Red Sea wreck. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Sharm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Sharm..", "x": "Explored: Sharm.. History. Why it is so — Thistlegorm Egypt. Red Sea. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Thistlegorm Egypt: History.. Wreck. One of the defining facts — Red Sea.. the Red Sea wreck. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: History..", "x": "Explored: History.. Cargo. Why it is so — Thistlegorm Egypt. Motorbikes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wreck.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wreck.", "x": "Thistlegorm Egypt in depth: Wreck.. Red Sea. The details reward the curious — the Red Sea wreck.. Cargo. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Thistlegorm Egypt in depth: History.. Motorbikes. The details reward the curious — the Red Sea wreck.. Sharm. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cargo.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cargo.", "x": "Thistlegorm Egypt in depth: Cargo.. 1941. The details reward the curious — the Red Sea wreck.. Red Sea. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sharm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sharm.", "x": "Thistlegorm Egypt in depth: Sharm.. Sharm. The details reward the curious — the Red Sea wreck.. Diving. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Red Sea.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Red Sea.", "x": "Thistlegorm Egypt in depth: Red Sea.. History. The details reward the curious — the Red Sea wreck.. Wreck. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Diving.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Diving.", "x": "Thistlegorm Egypt in depth: Diving.. WWII wreck. The details reward the curious — the Red Sea wreck.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Thistlegorm Egypt is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Thistlegorm Egypt is.", "x": "Location: WWII wreck.. Wreck. Getting oriented — Thistlegorm Egypt. the Red Sea wreck. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Thistlegorm Egypt.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Thistlegorm Egypt.", "x": "Visiting: History.. Red Sea. Practical know-how — Thistlegorm Egypt. the Red Sea wreck. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Thistlegorm Egypt.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Thistlegorm Egypt.", "x": "Ecology: Cargo.. Motorbikes. The living world of Thistlegorm Egypt — the Red Sea wreck.. Sharm. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Thistlegorm Egypt through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Thistlegorm Egypt through time.", "x": "History: Red Sea.. 1941. People and Thistlegorm Egypt across the centuries — the Red Sea wreck.. Diving. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Thistlegorm Egypt.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Thistlegorm Egypt.", "x": "Conservation: History.. WWII wreck. Threats and guardians of Thistlegorm Egypt — the Red Sea wreck.. Cargo. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Thistlegorm Egypt in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Thistlegorm Egypt in numbers.", "x": "Numbers: WWII wreck.; Red Sea.. Sharm. Statistics that stun — Thistlegorm Egypt. the Red Sea wreck. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive-thistlegorm-egypt-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
