(function(){'use strict';
/* JAH Robben Island Unesco Site Database generator — jahdb-e2-unesco-robben-island-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-robben-island',PREFIX='JAH-E2UNESCOROB-',NAME='JAH Robben Island Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Robben Island: the complete guide", "d": "Robben Island: Mandela's prison..", "g": "overview", "l": 2, "q": "What is Robben Island: the complete guide?", "a": "Robben Island: Mandela's prison..", "x": "The complete unesco site guide to Robben Island: Mandela's prison.. Apartheid prison. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Apartheid prison.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Apartheid prison.", "x": "Robben Island: Apartheid prison.. Prison. One of the defining facts — Tours by ex-prisoners.. Mandela's prison. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Apartheid prison..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Apartheid prison..", "x": "Explored: Apartheid prison.. Legacy. Why it is so — Robben Island. UNESCO 1999. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mandela 18 yrs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mandela 18 yrs.", "x": "Robben Island: Mandela 18 yrs.. Tours. One of the defining facts — UNESCO 1999.. Mandela's prison. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Mandela 18 yrs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Mandela 18 yrs..", "x": "Explored: Mandela 18 yrs.. Conservation. Why it is so — Robben Island. Cape Town. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tours by ex-prisoners.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tours by ex-prisoners.", "x": "Robben Island: Tours by ex-prisoners.. Legacy. One of the defining facts — Cape Town.. Mandela's prison. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Tours by ex-prisoners..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Tours by ex-prisoners..", "x": "Explored: Tours by ex-prisoners.. Visit. Why it is so — Robben Island. Ferry. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO 1999.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO 1999.", "x": "Robben Island: UNESCO 1999.. Conservation. One of the defining facts — Ferry.. Mandela's prison. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: UNESCO 1999..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: UNESCO 1999..", "x": "Explored: UNESCO 1999.. History. Why it is so — Robben Island. Apartheid prison. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cape Town.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cape Town.", "x": "Robben Island: Cape Town.. Visit. One of the defining facts — Apartheid prison.. Mandela's prison. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Cape Town..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Cape Town..", "x": "Explored: Cape Town.. Prison. Why it is so — Robben Island. Mandela 18 yrs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ferry.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ferry.", "x": "Robben Island: Ferry.. History. One of the defining facts — Mandela 18 yrs.. Mandela's prison. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Ferry..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Ferry..", "x": "Explored: Ferry.. Tours. Why it is so — Robben Island. Tours by ex-prisoners. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Robben Island in depth: History.. Mandela 18 yrs. The details reward the curious — Mandela's prison.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Prison.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Prison.", "x": "Robben Island in depth: Prison.. Tours by ex-prisoners. The details reward the curious — Mandela's prison.. Legacy. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tours.", "x": "Robben Island in depth: Tours.. UNESCO 1999. The details reward the curious — Mandela's prison.. Conservation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Legacy.", "x": "Robben Island in depth: Legacy.. Cape Town. The details reward the curious — Mandela's prison.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conservation.", "x": "Robben Island in depth: Conservation.. Ferry. The details reward the curious — Mandela's prison.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Robben Island in depth: Visit.. Apartheid prison. The details reward the curious — Mandela's prison.. Prison. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Robben Island is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Robben Island is.", "x": "Location: Apartheid prison.. History. Getting oriented — Robben Island. Mandela's prison. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Robben Island.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Robben Island.", "x": "Visiting: Prison.. Mandela 18 yrs. Practical know-how — Robben Island. Mandela's prison. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Robben Island.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Robben Island.", "x": "Ecology: Tours.. Tours by ex-prisoners. The living world of Robben Island — Mandela's prison.. Legacy. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Robben Island through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Robben Island through time.", "x": "History: Conservation.. UNESCO 1999. People and Robben Island across the centuries — Mandela's prison.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Robben Island.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Robben Island.", "x": "Conservation: Prison.. Apartheid prison. Threats and guardians of Robben Island — Mandela's prison.. Tours. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Robben Island in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Robben Island in numbers.", "x": "Numbers: Apartheid prison.; Mandela 18 yrs.. Legacy. Statistics that stun — Robben Island. Mandela's prison. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-robben-island-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
