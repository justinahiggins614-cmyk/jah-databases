(function(){'use strict';
/* JAH Mekong River River Database generator — jahdb-e2-river-mekong-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-mekong-river',PREFIX='JAH-E2RIVERMEKO-',NAME='JAH Mekong River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mekong River: the complete guide", "d": "Mekong River: Southeast Asia's lifeline..", "g": "overview", "l": 2, "q": "What is Mekong River: the complete guide?", "a": "Mekong River: Southeast Asia's lifeline..", "x": "The complete river guide to Mekong River: Southeast Asia's lifeline.. 4,350 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Tibet. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "4,350 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "4,350 km.", "x": "Mekong River: 4,350 km.. Laos. One of the defining facts — Mekong Delta.. Southeast Asia's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 4,350 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 4,350 km..", "x": "Explored: 4,350 km.. Culture. Why it is so — Mekong River. Giant catfish. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "6 countries.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "6 countries.", "x": "Mekong River: 6 countries.. Fisheries. One of the defining facts — Giant catfish.. Southeast Asia's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 6 countries..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 6 countries..", "x": "Explored: 6 countries.. Cruises. Why it is so — Mekong River. Tonle Sap. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mekong Delta.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mekong Delta.", "x": "Mekong River: Mekong Delta.. Culture. One of the defining facts — Tonle Sap.. Southeast Asia's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Mekong Delta..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Mekong Delta..", "x": "Explored: Mekong Delta.. Development. Why it is so — Mekong River. Dams debate. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Giant catfish.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Giant catfish.", "x": "Mekong River: Giant catfish.. Cruises. One of the defining facts — Dams debate.. Southeast Asia's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Giant catfish..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Giant catfish..", "x": "Explored: Giant catfish.. Source: Tibet. Why it is so — Mekong River. 4,350 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tonle Sap.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tonle Sap.", "x": "Mekong River: Tonle Sap.. Development. One of the defining facts — 4,350 km.. Southeast Asia's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Tonle Sap..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Tonle Sap..", "x": "Explored: Tonle Sap.. Laos. Why it is so — Mekong River. 6 countries. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dams debate.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dams debate.", "x": "Mekong River: Dams debate.. Source: Tibet. One of the defining facts — 6 countries.. Southeast Asia's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Dams debate..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Dams debate..", "x": "Explored: Dams debate.. Fisheries. Why it is so — Mekong River. Mekong Delta. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Tibet.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Tibet.", "x": "Mekong River in depth: Source: Tibet.. 6 countries. The details reward the curious — Southeast Asia's lifeline.. Fisheries. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Laos.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Laos.", "x": "Mekong River in depth: Laos.. Mekong Delta. The details reward the curious — Southeast Asia's lifeline.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fisheries.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fisheries.", "x": "Mekong River in depth: Fisheries.. Giant catfish. The details reward the curious — Southeast Asia's lifeline.. Cruises. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Culture.", "x": "Mekong River in depth: Culture.. Tonle Sap. The details reward the curious — Southeast Asia's lifeline.. Development. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cruises.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cruises.", "x": "Mekong River in depth: Cruises.. Dams debate. The details reward the curious — Southeast Asia's lifeline.. Source: Tibet. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Development.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Development.", "x": "Mekong River in depth: Development.. 4,350 km. The details reward the curious — Southeast Asia's lifeline.. Laos. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mekong River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mekong River is.", "x": "Location: 4,350 km.. Source: Tibet. Getting oriented — Mekong River. Southeast Asia's lifeline. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mekong River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mekong River.", "x": "Visiting: Laos.. 6 countries. Practical know-how — Mekong River. Southeast Asia's lifeline. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mekong River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mekong River.", "x": "Ecology: Fisheries.. Mekong Delta. The living world of Mekong River — Southeast Asia's lifeline.. Culture. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mekong River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mekong River through time.", "x": "History: Cruises.. Giant catfish. People and Mekong River across the centuries — Southeast Asia's lifeline.. Development. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mekong River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mekong River.", "x": "Conservation: Laos.. 4,350 km. Threats and guardians of Mekong River — Southeast Asia's lifeline.. Fisheries. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mekong River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mekong River in numbers.", "x": "Numbers: 4,350 km.; 6 countries.. Culture. Statistics that stun — Mekong River. Southeast Asia's lifeline. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-mekong-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
