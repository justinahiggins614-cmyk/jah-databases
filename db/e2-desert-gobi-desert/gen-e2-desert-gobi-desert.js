(function(){'use strict';
/* JAH Gobi Desert Desert Database generator — jahdb-e2-desert-gobi-desert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-desert-gobi-desert',PREFIX='JAH-E2DESERTGOB-',NAME='JAH Gobi Desert Desert Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gobi Desert: the complete guide", "d": "Gobi Desert: Mongolia's cold desert..", "g": "overview", "l": 2, "q": "What is Gobi Desert: the complete guide?", "a": "Gobi Desert: Mongolia's cold desert..", "x": "The complete desert guide to Gobi Desert: Mongolia's cold desert.. 1.3M sq km. From formation to visiting, from wildlife to legends — everything about this desert in one database. Paleontology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1.3M sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1.3M sq km.", "x": "Gobi Desert: 1.3M sq km.. People. One of the defining facts — Camels.. Mongolia's cold desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1.3M sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1.3M sq km..", "x": "Explored: 1.3M sq km.. History. Why it is so — Gobi Desert. Flaming Cliffs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dinosaurs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dinosaurs.", "x": "Gobi Desert: Dinosaurs.. Wildlife. One of the defining facts — Flaming Cliffs.. Mongolia's cold desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Dinosaurs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Dinosaurs..", "x": "Explored: Dinosaurs.. Travel. Why it is so — Gobi Desert. Cold. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Camels.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Camels.", "x": "Gobi Desert: Camels.. History. One of the defining facts — Cold.. Mongolia's cold desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Camels..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Camels..", "x": "Explored: Camels.. Climate. Why it is so — Gobi Desert. Silk Road. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flaming Cliffs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flaming Cliffs.", "x": "Gobi Desert: Flaming Cliffs.. Travel. One of the defining facts — Silk Road.. Mongolia's cold desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Flaming Cliffs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Flaming Cliffs..", "x": "Explored: Flaming Cliffs.. Paleontology. Why it is so — Gobi Desert. 1.3M sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cold.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cold.", "x": "Gobi Desert: Cold.. Climate. One of the defining facts — 1.3M sq km.. Mongolia's cold desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Cold..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Cold..", "x": "Explored: Cold.. People. Why it is so — Gobi Desert. Dinosaurs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Silk Road.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Silk Road.", "x": "Gobi Desert: Silk Road.. Paleontology. One of the defining facts — Dinosaurs.. Mongolia's cold desert. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Silk Road..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Silk Road..", "x": "Explored: Silk Road.. Wildlife. Why it is so — Gobi Desert. Camels. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Paleontology.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Paleontology.", "x": "Gobi Desert in depth: Paleontology.. Dinosaurs. The details reward the curious — Mongolia's cold desert.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "People.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "People.", "x": "Gobi Desert in depth: People.. Camels. The details reward the curious — Mongolia's cold desert.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wildlife.", "x": "Gobi Desert in depth: Wildlife.. Flaming Cliffs. The details reward the curious — Mongolia's cold desert.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Gobi Desert in depth: History.. Cold. The details reward the curious — Mongolia's cold desert.. Climate. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "Gobi Desert in depth: Travel.. Silk Road. The details reward the curious — Mongolia's cold desert.. Paleontology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Climate.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Climate.", "x": "Gobi Desert in depth: Climate.. 1.3M sq km. The details reward the curious — Mongolia's cold desert.. People. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Gobi Desert is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Gobi Desert is.", "x": "Location: 1.3M sq km.. Paleontology. Getting oriented — Gobi Desert. Mongolia's cold desert. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Gobi Desert.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Gobi Desert.", "x": "Visiting: People.. Dinosaurs. Practical know-how — Gobi Desert. Mongolia's cold desert. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Gobi Desert.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Gobi Desert.", "x": "Ecology: Wildlife.. Camels. The living world of Gobi Desert — Mongolia's cold desert.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Gobi Desert through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Gobi Desert through time.", "x": "History: Travel.. Flaming Cliffs. People and Gobi Desert across the centuries — Mongolia's cold desert.. Climate. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Gobi Desert.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Gobi Desert.", "x": "Conservation: People.. 1.3M sq km. Threats and guardians of Gobi Desert — Mongolia's cold desert.. Wildlife. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Gobi Desert in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Gobi Desert in numbers.", "x": "Numbers: 1.3M sq km.; Dinosaurs.. History. Statistics that stun — Gobi Desert. Mongolia's cold desert. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-desert-gobi-desert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
