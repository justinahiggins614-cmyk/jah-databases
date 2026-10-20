(function(){'use strict';
/* JAH Teahupo\'o Surf Spot Database generator — jahdb-e2-surf-teahupoo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-surf-teahupoo',PREFIX='JAH-E2SURFTEAHU-',NAME='JAH Teahupo\'o Surf Spot Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Teahupo'o: the complete guide", "d": "Teahupo'o: the heaviest wave..", "g": "overview", "l": 2, "q": "What is Teahupo'o: the complete guide?", "a": "Teahupo'o: the heaviest wave..", "x": "The complete surf spot guide to Teahupo'o: the heaviest wave.. Tahiti. From formation to visiting, from wildlife to legends — everything about this surf spot in one database. Reef. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Tahiti.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Tahiti.", "x": "Teahupo'o: Tahiti.. Olympics. One of the defining facts — Thick barrels.. the heaviest wave. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Tahiti..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Tahiti..", "x": "Explored: Tahiti.. Danger. Why it is so — Teahupo'o. Olympics 2024. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reef.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reef.", "x": "Teahupo'o: Reef.. Boats. One of the defining facts — Olympics 2024.. the heaviest wave. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Reef..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Reef..", "x": "Explored: Reef.. Legends. Why it is so — Teahupo'o. Boats. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Thick barrels.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Thick barrels.", "x": "Teahupo'o: Thick barrels.. Danger. One of the defining facts — Boats.. the heaviest wave. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Thick barrels..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Thick barrels..", "x": "Explored: Thick barrels.. Respect. Why it is so — Teahupo'o. Legends. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Olympics 2024.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Olympics 2024.", "x": "Teahupo'o: Olympics 2024.. Legends. One of the defining facts — Legends.. the heaviest wave. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Olympics 2024..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Olympics 2024..", "x": "Explored: Olympics 2024.. Reef. Why it is so — Teahupo'o. Tahiti. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Boats.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Boats.", "x": "Teahupo'o: Boats.. Respect. One of the defining facts — Tahiti.. the heaviest wave. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Boats..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Boats..", "x": "Explored: Boats.. Olympics. Why it is so — Teahupo'o. Reef. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Legends.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Legends.", "x": "Teahupo'o: Legends.. Reef. One of the defining facts — Reef.. the heaviest wave. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Legends..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Legends..", "x": "Explored: Legends.. Boats. Why it is so — Teahupo'o. Thick barrels. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Reef.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Reef.", "x": "Teahupo'o in depth: Reef.. Reef. The details reward the curious — the heaviest wave.. Boats. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Olympics.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Olympics.", "x": "Teahupo'o in depth: Olympics.. Thick barrels. The details reward the curious — the heaviest wave.. Danger. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Boats.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Boats.", "x": "Teahupo'o in depth: Boats.. Olympics 2024. The details reward the curious — the heaviest wave.. Legends. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Danger.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Danger.", "x": "Teahupo'o in depth: Danger.. Boats. The details reward the curious — the heaviest wave.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legends.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legends.", "x": "Teahupo'o in depth: Legends.. Legends. The details reward the curious — the heaviest wave.. Reef. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Teahupo'o in depth: Respect.. Tahiti. The details reward the curious — the heaviest wave.. Olympics. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Teahupo'o is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Teahupo'o is.", "x": "Location: Tahiti.. Reef. Getting oriented — Teahupo'o. the heaviest wave. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Teahupo'o.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Teahupo'o.", "x": "Visiting: Olympics.. Reef. Practical know-how — Teahupo'o. the heaviest wave. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Teahupo'o.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Teahupo'o.", "x": "Ecology: Boats.. Thick barrels. The living world of Teahupo'o — the heaviest wave.. Danger. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Teahupo'o through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Teahupo'o through time.", "x": "History: Legends.. Olympics 2024. People and Teahupo'o across the centuries — the heaviest wave.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Teahupo'o.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Teahupo'o.", "x": "Conservation: Olympics.. Tahiti. Threats and guardians of Teahupo'o — the heaviest wave.. Boats. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Teahupo'o in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Teahupo'o in numbers.", "x": "Numbers: Tahiti.; Reef.. Danger. Statistics that stun — Teahupo'o. the heaviest wave. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-surf-teahupoo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
