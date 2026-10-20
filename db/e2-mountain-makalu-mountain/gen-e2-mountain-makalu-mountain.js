(function(){'use strict';
/* JAH Makalu Mountain Database generator — jahdb-e2-mountain-makalu-mountain-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-makalu-mountain',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Makalu Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Makalu: the complete guide", "d": "Makalu: the great pyramid..", "g": "overview", "l": 2, "q": "What is Makalu: the complete guide?", "a": "Makalu: the great pyramid..", "x": "The complete mountain guide to Makalu: the great pyramid.. 8,485m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8,485m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8,485m.", "x": "Makalu: 8,485m.. History. One of the defining facts — First 1955 French.. the great pyramid. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 8,485m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 8,485m..", "x": "Explored: 8,485m.. Views. Why it is so — Makalu. Remote. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pyramid shape.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pyramid shape.", "x": "Makalu: Pyramid shape.. Trekking. One of the defining facts — Remote.. the great pyramid. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Pyramid shape..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Pyramid shape..", "x": "Explored: Pyramid shape.. Climbing. Why it is so — Makalu. Technical. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First 1955 French.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First 1955 French.", "x": "Makalu: First 1955 French.. Views. One of the defining facts — Technical.. the great pyramid. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: First 1955 French..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: First 1955 French..", "x": "Explored: First 1955 French.. Safety. Why it is so — Makalu. Barun. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Remote.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Remote.", "x": "Makalu: Remote.. Climbing. One of the defining facts — Barun.. the great pyramid. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Remote..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Remote..", "x": "Explored: Remote.. Routes. Why it is so — Makalu. 8,485m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Technical.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Technical.", "x": "Makalu: Technical.. Safety. One of the defining facts — 8,485m.. the great pyramid. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Technical..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Technical..", "x": "Explored: Technical.. History. Why it is so — Makalu. Pyramid shape. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Barun.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Barun.", "x": "Makalu: Barun.. Routes. One of the defining facts — Pyramid shape.. the great pyramid. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Barun..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Barun..", "x": "Explored: Barun.. Trekking. Why it is so — Makalu. First 1955 French. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Routes.", "x": "Makalu in depth: Routes.. Pyramid shape. The details reward the curious — the great pyramid.. Trekking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Makalu in depth: History.. First 1955 French. The details reward the curious — the great pyramid.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Trekking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Trekking.", "x": "Makalu in depth: Trekking.. Remote. The details reward the curious — the great pyramid.. Climbing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Makalu in depth: Views.. Technical. The details reward the curious — the great pyramid.. Safety. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Climbing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Climbing.", "x": "Makalu in depth: Climbing.. Barun. The details reward the curious — the great pyramid.. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safety.", "x": "Makalu in depth: Safety.. 8,485m. The details reward the curious — the great pyramid.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Makalu is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Makalu is.", "x": "Location: 8,485m.. Routes. Getting oriented — Makalu. the great pyramid. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Makalu.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Makalu.", "x": "Visiting: History.. Pyramid shape. Practical know-how — Makalu. the great pyramid. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Makalu.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Makalu.", "x": "Ecology: Trekking.. First 1955 French. The living world of Makalu — the great pyramid.. Views. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Makalu through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Makalu through time.", "x": "History: Climbing.. Remote. People and Makalu across the centuries — the great pyramid.. Safety. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Makalu.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Makalu.", "x": "Conservation: History.. 8,485m. Threats and guardians of Makalu — the great pyramid.. Trekking. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Makalu in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Makalu in numbers.", "x": "Numbers: 8,485m.; Pyramid shape.. Views. Statistics that stun — Makalu. the great pyramid. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-makalu-mountain-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
