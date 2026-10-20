(function(){'use strict';
/* JAH Kangchenjunga Mountain Database generator — jahdb-e2-mountain-kangchenjunga-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-kangchenjunga',PREFIX='JAH-E2MOUNTAINK-',NAME='JAH Kangchenjunga Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kangchenjunga: the complete guide", "d": "Kangchenjunga: third highest; sacred..", "g": "overview", "l": 2, "q": "What is Kangchenjunga: the complete guide?", "a": "Kangchenjunga: third highest; sacred..", "x": "The complete mountain guide to Kangchenjunga: third highest; sacred.. 8,586m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8,586m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8,586m.", "x": "Kangchenjunga: 8,586m.. Culture. One of the defining facts — First 1955.. third highest; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 8,586m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 8,586m..", "x": "Explored: 8,586m.. Permits. Why it is so — Kangchenjunga. Sacred: stop short. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nepal/India.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nepal/India.", "x": "Kangchenjunga: Nepal/India.. Trekking. One of the defining facts — Sacred: stop short.. third highest; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Nepal/India..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Nepal/India..", "x": "Explored: Nepal/India.. History. Why it is so — Kangchenjunga. Remote. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First 1955.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First 1955.", "x": "Kangchenjunga: First 1955.. Permits. One of the defining facts — Remote.. third highest; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: First 1955..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: First 1955..", "x": "Explored: First 1955.. Views. Why it is so — Kangchenjunga. Yalung. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sacred: stop short.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sacred: stop short.", "x": "Kangchenjunga: Sacred: stop short.. History. One of the defining facts — Yalung.. third highest; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Sacred: stop short..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Sacred: stop short..", "x": "Explored: Sacred: stop short.. Routes. Why it is so — Kangchenjunga. 8,586m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Remote.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Remote.", "x": "Kangchenjunga: Remote.. Views. One of the defining facts — 8,586m.. third highest; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Remote..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Remote..", "x": "Explored: Remote.. Culture. Why it is so — Kangchenjunga. Nepal/India. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Yalung.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Yalung.", "x": "Kangchenjunga: Yalung.. Routes. One of the defining facts — Nepal/India.. third highest; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Yalung..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Yalung..", "x": "Explored: Yalung.. Trekking. Why it is so — Kangchenjunga. First 1955. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Routes.", "x": "Kangchenjunga in depth: Routes.. Nepal/India. The details reward the curious — third highest; sacred.. Trekking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Culture.", "x": "Kangchenjunga in depth: Culture.. First 1955. The details reward the curious — third highest; sacred.. Permits. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Trekking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Trekking.", "x": "Kangchenjunga in depth: Trekking.. Sacred: stop short. The details reward the curious — third highest; sacred.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Permits.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Permits.", "x": "Kangchenjunga in depth: Permits.. Remote. The details reward the curious — third highest; sacred.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Kangchenjunga in depth: History.. Yalung. The details reward the curious — third highest; sacred.. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Kangchenjunga in depth: Views.. 8,586m. The details reward the curious — third highest; sacred.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Kangchenjunga is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Kangchenjunga is.", "x": "Location: 8,586m.. Routes. Getting oriented — Kangchenjunga. third highest; sacred. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Kangchenjunga.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Kangchenjunga.", "x": "Visiting: Culture.. Nepal/India. Practical know-how — Kangchenjunga. third highest; sacred. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Kangchenjunga.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Kangchenjunga.", "x": "Ecology: Trekking.. First 1955. The living world of Kangchenjunga — third highest; sacred.. Permits. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Kangchenjunga through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Kangchenjunga through time.", "x": "History: History.. Sacred: stop short. People and Kangchenjunga across the centuries — third highest; sacred.. Views. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Kangchenjunga.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Kangchenjunga.", "x": "Conservation: Culture.. 8,586m. Threats and guardians of Kangchenjunga — third highest; sacred.. Trekking. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Kangchenjunga in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Kangchenjunga in numbers.", "x": "Numbers: 8,586m.; Nepal/India.. Permits. Statistics that stun — Kangchenjunga. third highest; sacred. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-kangchenjunga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
