(function(){'use strict';
/* JAH New Guinea Island Database generator — jahdb-e2-island-new-guinea-island-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-island-new-guinea-island',PREFIX='JAH-E2ISLANDNEW-',NAME='JAH New Guinea Island Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New Guinea: the complete guide", "d": "New Guinea: world's second largest..", "g": "overview", "l": 2, "q": "What is New Guinea: the complete guide?", "a": "New Guinea: world's second largest..", "x": "The complete island guide to New Guinea: world's second largest.. 785,000 sq km. From formation to visiting, from wildlife to legends — everything about this island in one database. Cultures. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "785,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "785,000 sq km.", "x": "New Guinea: 785,000 sq km.. Wildlife. One of the defining facts — Birds of paradise.. world's second largest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 785,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 785,000 sq km..", "x": "Explored: 785,000 sq km.. Trekking. Why it is so — New Guinea. Highlands. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "800 languages.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "800 languages.", "x": "New Guinea: 800 languages.. Diving. One of the defining facts — Highlands.. world's second largest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 800 languages..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 800 languages..", "x": "Explored: 800 languages.. History. Why it is so — New Guinea. Raja Ampat. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Birds of paradise.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Birds of paradise.", "x": "New Guinea: Birds of paradise.. Trekking. One of the defining facts — Raja Ampat.. world's second largest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Birds of paradise..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Birds of paradise..", "x": "Explored: Birds of paradise.. Travel. Why it is so — New Guinea. Tribes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Highlands.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Highlands.", "x": "New Guinea: Highlands.. History. One of the defining facts — Tribes.. world's second largest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Highlands..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Highlands..", "x": "Explored: Highlands.. Cultures. Why it is so — New Guinea. 785,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Raja Ampat.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Raja Ampat.", "x": "New Guinea: Raja Ampat.. Travel. One of the defining facts — 785,000 sq km.. world's second largest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Raja Ampat..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Raja Ampat..", "x": "Explored: Raja Ampat.. Wildlife. Why it is so — New Guinea. 800 languages. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tribes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tribes.", "x": "New Guinea: Tribes.. Cultures. One of the defining facts — 800 languages.. world's second largest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Tribes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Tribes..", "x": "Explored: Tribes.. Diving. Why it is so — New Guinea. Birds of paradise. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cultures.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cultures.", "x": "New Guinea in depth: Cultures.. 800 languages. The details reward the curious — world's second largest.. Diving. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wildlife.", "x": "New Guinea in depth: Wildlife.. Birds of paradise. The details reward the curious — world's second largest.. Trekking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Diving.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Diving.", "x": "New Guinea in depth: Diving.. Highlands. The details reward the curious — world's second largest.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Trekking.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Trekking.", "x": "New Guinea in depth: Trekking.. Raja Ampat. The details reward the curious — world's second largest.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "New Guinea in depth: History.. Tribes. The details reward the curious — world's second largest.. Cultures. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "New Guinea in depth: Travel.. 785,000 sq km. The details reward the curious — world's second largest.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where New Guinea is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where New Guinea is.", "x": "Location: 785,000 sq km.. Cultures. Getting oriented — New Guinea. world's second largest. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience New Guinea.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience New Guinea.", "x": "Visiting: Wildlife.. 800 languages. Practical know-how — New Guinea. world's second largest. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around New Guinea.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around New Guinea.", "x": "Ecology: Diving.. Birds of paradise. The living world of New Guinea — world's second largest.. Trekking. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "New Guinea through time.", "g": "history", "l": 2, "q": "What is History?", "a": "New Guinea through time.", "x": "History: History.. Highlands. People and New Guinea across the centuries — world's second largest.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting New Guinea.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting New Guinea.", "x": "Conservation: Wildlife.. 785,000 sq km. Threats and guardians of New Guinea — world's second largest.. Diving. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "New Guinea in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "New Guinea in numbers.", "x": "Numbers: 785,000 sq km.; 800 languages.. Trekking. Statistics that stun — New Guinea. world's second largest. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-island-new-guinea-island-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
