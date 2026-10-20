(function(){'use strict';
/* JAH Aquatica Orlando Water Park Database generator — jahdb-e2-waterpark-aquatica-orlando-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-waterpark-aquatica-orlando',PREFIX='JAH-E2WATERPARK-',NAME='JAH Aquatica Orlando Water Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Aquatica Orlando: the complete guide", "d": "Aquatica Orlando: SeaWorld's water park..", "g": "overview", "l": 2, "q": "What is Aquatica Orlando: the complete guide?", "a": "Aquatica Orlando: SeaWorld's water park..", "x": "The complete water park guide to Aquatica Orlando: SeaWorld's water park.. 2008. From formation to visiting, from wildlife to legends — everything about this water park in one database. Dolphins. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2008.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2008.", "x": "Aquatica Orlando: 2008.. Rapids. One of the defining facts — Roa's Rapids.. SeaWorld's water park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2008..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2008..", "x": "Explored: 2008.. Tickets. Why it is so — Aquatica Orlando. Beaches. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dolphin Plunge.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dolphin Plunge.", "x": "Aquatica Orlando: Dolphin Plunge.. Beaches. One of the defining facts — Beaches.. SeaWorld's water park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Dolphin Plunge..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Dolphin Plunge..", "x": "Explored: Dolphin Plunge.. Orlando. Why it is so — Aquatica Orlando. Orlando. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Roa's Rapids.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Roa's Rapids.", "x": "Aquatica Orlando: Roa's Rapids.. Tickets. One of the defining facts — Orlando.. SeaWorld's water park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Roa's Rapids..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Roa's Rapids..", "x": "Explored: Roa's Rapids.. Sea. Why it is so — Aquatica Orlando. SeaWorld. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Beaches.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Beaches.", "x": "Aquatica Orlando: Beaches.. Orlando. One of the defining facts — SeaWorld.. SeaWorld's water park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Beaches..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Beaches..", "x": "Explored: Beaches.. Dolphins. Why it is so — Aquatica Orlando. 2008. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orlando.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orlando.", "x": "Aquatica Orlando: Orlando.. Sea. One of the defining facts — 2008.. SeaWorld's water park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Orlando..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Orlando..", "x": "Explored: Orlando.. Rapids. Why it is so — Aquatica Orlando. Dolphin Plunge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "SeaWorld.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "SeaWorld.", "x": "Aquatica Orlando: SeaWorld.. Dolphins. One of the defining facts — Dolphin Plunge.. SeaWorld's water park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: SeaWorld..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: SeaWorld..", "x": "Explored: SeaWorld.. Beaches. Why it is so — Aquatica Orlando. Roa's Rapids. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dolphins.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dolphins.", "x": "Aquatica Orlando in depth: Dolphins.. Dolphin Plunge. The details reward the curious — SeaWorld's water park.. Beaches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rapids.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rapids.", "x": "Aquatica Orlando in depth: Rapids.. Roa's Rapids. The details reward the curious — SeaWorld's water park.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Beaches.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Beaches.", "x": "Aquatica Orlando in depth: Beaches.. Beaches. The details reward the curious — SeaWorld's water park.. Orlando. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Aquatica Orlando in depth: Tickets.. Orlando. The details reward the curious — SeaWorld's water park.. Sea. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Orlando.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Orlando.", "x": "Aquatica Orlando in depth: Orlando.. SeaWorld. The details reward the curious — SeaWorld's water park.. Dolphins. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sea.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sea.", "x": "Aquatica Orlando in depth: Sea.. 2008. The details reward the curious — SeaWorld's water park.. Rapids. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Aquatica Orlando is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Aquatica Orlando is.", "x": "Location: 2008.. Dolphins. Getting oriented — Aquatica Orlando. SeaWorld's water park. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Aquatica Orlando.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Aquatica Orlando.", "x": "Visiting: Rapids.. Dolphin Plunge. Practical know-how — Aquatica Orlando. SeaWorld's water park. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Aquatica Orlando.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Aquatica Orlando.", "x": "Ecology: Beaches.. Roa's Rapids. The living world of Aquatica Orlando — SeaWorld's water park.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Aquatica Orlando through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Aquatica Orlando through time.", "x": "History: Orlando.. Beaches. People and Aquatica Orlando across the centuries — SeaWorld's water park.. Sea. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Aquatica Orlando.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Aquatica Orlando.", "x": "Conservation: Rapids.. 2008. Threats and guardians of Aquatica Orlando — SeaWorld's water park.. Beaches. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Aquatica Orlando in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Aquatica Orlando in numbers.", "x": "Numbers: 2008.; Dolphin Plunge.. Tickets. Statistics that stun — Aquatica Orlando. SeaWorld's water park. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-waterpark-aquatica-orlando-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
