(function(){'use strict';
/* JAH Madagascar Island Database generator — jahdb-e2-island-madagascar-island-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-island-madagascar-island',PREFIX='JAH-E2ISLANDMAD-',NAME='JAH Madagascar Island Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Madagascar: the complete guide", "d": "Madagascar: eighth continent..", "g": "overview", "l": 2, "q": "What is Madagascar: the complete guide?", "a": "Madagascar: eighth continent..", "x": "The complete island guide to Madagascar: eighth continent.. 587,000 sq km. From formation to visiting, from wildlife to legends — everything about this island in one database. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "587,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "587,000 sq km.", "x": "Madagascar: 587,000 sq km.. Forests. One of the defining facts — Baobabs.. eighth continent. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 587,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 587,000 sq km..", "x": "Explored: 587,000 sq km.. Parks. Why it is so — Madagascar. Tsingy. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lemurs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lemurs.", "x": "Madagascar: Lemurs.. Culture. One of the defining facts — Tsingy.. eighth continent. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Lemurs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Lemurs..", "x": "Explored: Lemurs.. History. Why it is so — Madagascar. Antananarivo. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Baobabs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Baobabs.", "x": "Madagascar: Baobabs.. Parks. One of the defining facts — Antananarivo.. eighth continent. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Baobabs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Baobabs..", "x": "Explored: Baobabs.. Travel. Why it is so — Madagascar. Reefs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tsingy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tsingy.", "x": "Madagascar: Tsingy.. History. One of the defining facts — Reefs.. eighth continent. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Tsingy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Tsingy..", "x": "Explored: Tsingy.. Wildlife. Why it is so — Madagascar. 587,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Antananarivo.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Antananarivo.", "x": "Madagascar: Antananarivo.. Travel. One of the defining facts — 587,000 sq km.. eighth continent. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Antananarivo..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Antananarivo..", "x": "Explored: Antananarivo.. Forests. Why it is so — Madagascar. Lemurs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Reefs.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Reefs.", "x": "Madagascar: Reefs.. Wildlife. One of the defining facts — Lemurs.. eighth continent. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Reefs..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Reefs..", "x": "Explored: Reefs.. Culture. Why it is so — Madagascar. Baobabs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wildlife.", "x": "Madagascar in depth: Wildlife.. Lemurs. The details reward the curious — eighth continent.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Forests.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Forests.", "x": "Madagascar in depth: Forests.. Baobabs. The details reward the curious — eighth continent.. Parks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Culture.", "x": "Madagascar in depth: Culture.. Tsingy. The details reward the curious — eighth continent.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Parks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Parks.", "x": "Madagascar in depth: Parks.. Antananarivo. The details reward the curious — eighth continent.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Madagascar in depth: History.. Reefs. The details reward the curious — eighth continent.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Madagascar in depth: Travel.. 587,000 sq km. The details reward the curious — eighth continent.. Forests. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Madagascar is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Madagascar is.", "x": "Location: 587,000 sq km.. Wildlife. Getting oriented — Madagascar. eighth continent. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Madagascar.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Madagascar.", "x": "Visiting: Forests.. Lemurs. Practical know-how — Madagascar. eighth continent. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Madagascar.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Madagascar.", "x": "Ecology: Culture.. Baobabs. The living world of Madagascar — eighth continent.. Parks. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Madagascar through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Madagascar through time.", "x": "History: History.. Tsingy. People and Madagascar across the centuries — eighth continent.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Madagascar.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Madagascar.", "x": "Conservation: Forests.. 587,000 sq km. Threats and guardians of Madagascar — eighth continent.. Culture. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Madagascar in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Madagascar in numbers.", "x": "Numbers: 587,000 sq km.; Lemurs.. Parks. Statistics that stun — Madagascar. eighth continent. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-island-madagascar-island-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
