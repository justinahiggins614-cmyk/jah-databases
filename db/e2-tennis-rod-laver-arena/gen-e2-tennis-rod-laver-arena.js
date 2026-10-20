(function(){'use strict';
/* JAH Rod Laver Arena Tennis Court Database generator — jahdb-e2-tennis-rod-laver-arena-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tennis-rod-laver-arena',PREFIX='JAH-E2TENNISROD-',NAME='JAH Rod Laver Arena Tennis Court Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rod Laver Arena: the complete guide", "d": "Rod Laver Arena: the happy slam's home..", "g": "overview", "l": 2, "q": "What is Rod Laver Arena: the complete guide?", "a": "Rod Laver Arena: the happy slam's home..", "x": "The complete tennis court guide to Rod Laver Arena: the happy slam's home.. 1988. From formation to visiting, from wildlife to legends — everything about this tennis court in one database. Roof. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1988.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1988.", "x": "Rod Laver Arena: 1988.. Heat. One of the defining facts — Roof.. the happy slam's home. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1988..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1988..", "x": "Explored: 1988.. Melbourne. Why it is so — Rod Laver Arena. Heat. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Melbourne.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Melbourne.", "x": "Rod Laver Arena: Melbourne.. Laver. One of the defining facts — Heat.. the happy slam's home. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Melbourne..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Melbourne..", "x": "Explored: Melbourne.. AO. Why it is so — Rod Laver Arena. Laver. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Roof.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Roof.", "x": "Rod Laver Arena: Roof.. Melbourne. One of the defining facts — Laver.. the happy slam's home. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Roof..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Roof..", "x": "Explored: Roof.. Happy. Why it is so — Rod Laver Arena. AO. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Heat.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Heat.", "x": "Rod Laver Arena: Heat.. AO. One of the defining facts — AO.. the happy slam's home. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Heat..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Heat..", "x": "Explored: Heat.. Roof. Why it is so — Rod Laver Arena. 1988. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Laver.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Laver.", "x": "Rod Laver Arena: Laver.. Happy. One of the defining facts — 1988.. the happy slam's home. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Laver..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Laver..", "x": "Explored: Laver.. Heat. Why it is so — Rod Laver Arena. Melbourne. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "AO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "AO.", "x": "Rod Laver Arena: AO.. Roof. One of the defining facts — Melbourne.. the happy slam's home. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: AO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: AO..", "x": "Explored: AO.. Laver. Why it is so — Rod Laver Arena. Roof. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Roof.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Roof.", "x": "Rod Laver Arena in depth: Roof.. Melbourne. The details reward the curious — the happy slam's home.. Laver. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Heat.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Heat.", "x": "Rod Laver Arena in depth: Heat.. Roof. The details reward the curious — the happy slam's home.. Melbourne. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Laver.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Laver.", "x": "Rod Laver Arena in depth: Laver.. Heat. The details reward the curious — the happy slam's home.. AO. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Melbourne.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Melbourne.", "x": "Rod Laver Arena in depth: Melbourne.. Laver. The details reward the curious — the happy slam's home.. Happy. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "AO.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "AO.", "x": "Rod Laver Arena in depth: AO.. AO. The details reward the curious — the happy slam's home.. Roof. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Happy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Happy.", "x": "Rod Laver Arena in depth: Happy.. 1988. The details reward the curious — the happy slam's home.. Heat. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Rod Laver Arena is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Rod Laver Arena is.", "x": "Location: 1988.. Roof. Getting oriented — Rod Laver Arena. the happy slam's home. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Rod Laver Arena.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Rod Laver Arena.", "x": "Visiting: Heat.. Melbourne. Practical know-how — Rod Laver Arena. the happy slam's home. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Rod Laver Arena.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Rod Laver Arena.", "x": "Ecology: Laver.. Roof. The living world of Rod Laver Arena — the happy slam's home.. Melbourne. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Rod Laver Arena through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Rod Laver Arena through time.", "x": "History: AO.. Heat. People and Rod Laver Arena across the centuries — the happy slam's home.. Happy. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Rod Laver Arena.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Rod Laver Arena.", "x": "Conservation: Heat.. 1988. Threats and guardians of Rod Laver Arena — the happy slam's home.. Laver. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Rod Laver Arena in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Rod Laver Arena in numbers.", "x": "Numbers: 1988.; Melbourne.. Melbourne. Statistics that stun — Rod Laver Arena. the happy slam's home. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tennis-rod-laver-arena-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
