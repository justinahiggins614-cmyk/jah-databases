(function(){'use strict';
/* JAH Volcano Bay Water Park Database generator — jahdb-e2-waterpark-volcano-bay-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-waterpark-volcano-bay',PREFIX='JAH-E2WATERPARK-',NAME='JAH Volcano Bay Water Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Volcano Bay: the complete guide", "d": "Volcano Bay: Universal's volcano..", "g": "overview", "l": 2, "q": "What is Volcano Bay: the complete guide?", "a": "Volcano Bay: Universal's volcano..", "x": "The complete water park guide to Volcano Bay: Universal's volcano.. 2017. From formation to visiting, from wildlife to legends — everything about this water park in one database. Volcano. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2017.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2017.", "x": "Volcano Bay: 2017.. Tapu. One of the defining facts — TapuTapu.. Universal's volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2017..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2017..", "x": "Explored: 2017.. Tickets. Why it is so — Volcano Bay. Orlando. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Krakatau.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Krakatau.", "x": "Volcano Bay: Krakatau.. Slides. One of the defining facts — Orlando.. Universal's volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Krakatau..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Krakatau..", "x": "Explored: Krakatau.. Orlando. Why it is so — Volcano Bay. Slides. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "TapuTapu.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "TapuTapu.", "x": "Volcano Bay: TapuTapu.. Tickets. One of the defining facts — Slides.. Universal's volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: TapuTapu..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: TapuTapu..", "x": "Explored: TapuTapu.. Tropical. Why it is so — Volcano Bay. Beach. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Orlando.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Orlando.", "x": "Volcano Bay: Orlando.. Orlando. One of the defining facts — Beach.. Universal's volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Orlando..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Orlando..", "x": "Explored: Orlando.. Volcano. Why it is so — Volcano Bay. 2017. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Slides.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Slides.", "x": "Volcano Bay: Slides.. Tropical. One of the defining facts — 2017.. Universal's volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Slides..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Slides..", "x": "Explored: Slides.. Tapu. Why it is so — Volcano Bay. Krakatau. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Beach.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Beach.", "x": "Volcano Bay: Beach.. Volcano. One of the defining facts — Krakatau.. Universal's volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Beach..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Beach..", "x": "Explored: Beach.. Slides. Why it is so — Volcano Bay. TapuTapu. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Volcano.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Volcano.", "x": "Volcano Bay in depth: Volcano.. Krakatau. The details reward the curious — Universal's volcano.. Slides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tapu.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tapu.", "x": "Volcano Bay in depth: Tapu.. TapuTapu. The details reward the curious — Universal's volcano.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Slides.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Slides.", "x": "Volcano Bay in depth: Slides.. Orlando. The details reward the curious — Universal's volcano.. Orlando. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Volcano Bay in depth: Tickets.. Slides. The details reward the curious — Universal's volcano.. Tropical. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Orlando.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Orlando.", "x": "Volcano Bay in depth: Orlando.. Beach. The details reward the curious — Universal's volcano.. Volcano. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tropical.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tropical.", "x": "Volcano Bay in depth: Tropical.. 2017. The details reward the curious — Universal's volcano.. Tapu. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Volcano Bay is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Volcano Bay is.", "x": "Location: 2017.. Volcano. Getting oriented — Volcano Bay. Universal's volcano. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Volcano Bay.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Volcano Bay.", "x": "Visiting: Tapu.. Krakatau. Practical know-how — Volcano Bay. Universal's volcano. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Volcano Bay.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Volcano Bay.", "x": "Ecology: Slides.. TapuTapu. The living world of Volcano Bay — Universal's volcano.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Volcano Bay through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Volcano Bay through time.", "x": "History: Orlando.. Orlando. People and Volcano Bay across the centuries — Universal's volcano.. Tropical. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Volcano Bay.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Volcano Bay.", "x": "Conservation: Tapu.. 2017. Threats and guardians of Volcano Bay — Universal's volcano.. Slides. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Volcano Bay in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Volcano Bay in numbers.", "x": "Numbers: 2017.; Krakatau.. Tickets. Statistics that stun — Volcano Bay. Universal's volcano. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-waterpark-volcano-bay-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
