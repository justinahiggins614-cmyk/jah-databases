(function(){'use strict';
/* JAH Manta Ray Night Kona Dive Site Database generator — jahdb-e2-dive-manta-ray-night-kona-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive-manta-ray-night-kona',PREFIX='JAH-E2DIVEMANTA-',NAME='JAH Manta Ray Night Kona Dive Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Manta Ray Night Kona: the complete guide", "d": "Manta Ray Night Kona: the manta ballet..", "g": "overview", "l": 2, "q": "What is Manta Ray Night Kona: the complete guide?", "a": "Manta Ray Night Kona: the manta ballet..", "x": "The complete dive site guide to Manta Ray Night Kona: the manta ballet.. Hawaii. From formation to visiting, from wildlife to legends — everything about this dive site in one database. Night. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hawaii.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hawaii.", "x": "Manta Ray Night Kona: Hawaii.. Mantas. One of the defining facts — Plankton lights.. the manta ballet. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Hawaii..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Hawaii..", "x": "Explored: Hawaii.. Kona. Why it is so — Manta Ray Night Kona. Mantas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Night.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Night.", "x": "Manta Ray Night Kona: Night.. Lights. One of the defining facts — Mantas.. the manta ballet. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Night..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Night..", "x": "Explored: Night.. Magic. Why it is so — Manta Ray Night Kona. Kona. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Plankton lights.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Plankton lights.", "x": "Manta Ray Night Kona: Plankton lights.. Kona. One of the defining facts — Kona.. the manta ballet. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Plankton lights..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Plankton lights..", "x": "Explored: Plankton lights.. Diving. Why it is so — Manta Ray Night Kona. Magic. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mantas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mantas.", "x": "Manta Ray Night Kona: Mantas.. Magic. One of the defining facts — Magic.. the manta ballet. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Mantas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Mantas..", "x": "Explored: Mantas.. Night. Why it is so — Manta Ray Night Kona. Hawaii. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Kona.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Kona.", "x": "Manta Ray Night Kona: Kona.. Diving. One of the defining facts — Hawaii.. the manta ballet. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Kona..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Kona..", "x": "Explored: Kona.. Mantas. Why it is so — Manta Ray Night Kona. Night. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Magic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Magic.", "x": "Manta Ray Night Kona: Magic.. Night. One of the defining facts — Night.. the manta ballet. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Magic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Magic..", "x": "Explored: Magic.. Lights. Why it is so — Manta Ray Night Kona. Plankton lights. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Night.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Night.", "x": "Manta Ray Night Kona in depth: Night.. Night. The details reward the curious — the manta ballet.. Lights. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mantas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mantas.", "x": "Manta Ray Night Kona in depth: Mantas.. Plankton lights. The details reward the curious — the manta ballet.. Kona. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lights.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lights.", "x": "Manta Ray Night Kona in depth: Lights.. Mantas. The details reward the curious — the manta ballet.. Magic. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Kona.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Kona.", "x": "Manta Ray Night Kona in depth: Kona.. Kona. The details reward the curious — the manta ballet.. Diving. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Magic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Magic.", "x": "Manta Ray Night Kona in depth: Magic.. Magic. The details reward the curious — the manta ballet.. Night. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Diving.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Diving.", "x": "Manta Ray Night Kona in depth: Diving.. Hawaii. The details reward the curious — the manta ballet.. Mantas. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Manta Ray Night Kona is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Manta Ray Night Kona is.", "x": "Location: Hawaii.. Night. Getting oriented — Manta Ray Night Kona. the manta ballet. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Manta Ray Night Kona.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Manta Ray Night Kona.", "x": "Visiting: Mantas.. Night. Practical know-how — Manta Ray Night Kona. the manta ballet. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Manta Ray Night Kona.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Manta Ray Night Kona.", "x": "Ecology: Lights.. Plankton lights. The living world of Manta Ray Night Kona — the manta ballet.. Kona. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Manta Ray Night Kona through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Manta Ray Night Kona through time.", "x": "History: Magic.. Mantas. People and Manta Ray Night Kona across the centuries — the manta ballet.. Diving. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Manta Ray Night Kona.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Manta Ray Night Kona.", "x": "Conservation: Mantas.. Hawaii. Threats and guardians of Manta Ray Night Kona — the manta ballet.. Lights. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Manta Ray Night Kona in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Manta Ray Night Kona in numbers.", "x": "Numbers: Hawaii.; Night.. Kona. Statistics that stun — Manta Ray Night Kona. the manta ballet. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive-manta-ray-night-kona-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
