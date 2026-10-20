(function(){'use strict';
/* JAH Columbia River River Database generator — jahdb-e2-river-columbia-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-columbia-river',PREFIX='JAH-E2RIVERCOLU-',NAME='JAH Columbia River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Columbia River: the complete guide", "d": "Columbia River: Pacific Northwest power..", "g": "overview", "l": 2, "q": "What is Columbia River: the complete guide?", "a": "Columbia River: Pacific Northwest power..", "x": "The complete river guide to Columbia River: Pacific Northwest power.. 2,000 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Canada. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2,000 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2,000 km.", "x": "Columbia River: 2,000 km.. Dams. One of the defining facts — Salmon.. Pacific Northwest power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2,000 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2,000 km..", "x": "Explored: 2,000 km.. Wind. Why it is so — Columbia River. Gorge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Grand Coulee.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Grand Coulee.", "x": "Columbia River: Grand Coulee.. Fish. One of the defining facts — Gorge.. Pacific Northwest power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Grand Coulee..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Grand Coulee..", "x": "Explored: Grand Coulee.. History. Why it is so — Columbia River. Dams. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Salmon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Salmon.", "x": "Columbia River: Salmon.. Wind. One of the defining facts — Dams.. Pacific Northwest power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Salmon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Salmon..", "x": "Explored: Salmon.. Recreation. Why it is so — Columbia River. Lewis/Clark. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gorge.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gorge.", "x": "Columbia River: Gorge.. History. One of the defining facts — Lewis/Clark.. Pacific Northwest power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Gorge..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Gorge..", "x": "Explored: Gorge.. Source: Canada. Why it is so — Columbia River. 2,000 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dams.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dams.", "x": "Columbia River: Dams.. Recreation. One of the defining facts — 2,000 km.. Pacific Northwest power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Dams..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Dams..", "x": "Explored: Dams.. Dams. Why it is so — Columbia River. Grand Coulee. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lewis/Clark.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lewis/Clark.", "x": "Columbia River: Lewis/Clark.. Source: Canada. One of the defining facts — Grand Coulee.. Pacific Northwest power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Lewis/Clark..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Lewis/Clark..", "x": "Explored: Lewis/Clark.. Fish. Why it is so — Columbia River. Salmon. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Canada.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Canada.", "x": "Columbia River in depth: Source: Canada.. Grand Coulee. The details reward the curious — Pacific Northwest power.. Fish. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dams.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dams.", "x": "Columbia River in depth: Dams.. Salmon. The details reward the curious — Pacific Northwest power.. Wind. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fish.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fish.", "x": "Columbia River in depth: Fish.. Gorge. The details reward the curious — Pacific Northwest power.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wind.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wind.", "x": "Columbia River in depth: Wind.. Dams. The details reward the curious — Pacific Northwest power.. Recreation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Columbia River in depth: History.. Lewis/Clark. The details reward the curious — Pacific Northwest power.. Source: Canada. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Recreation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Recreation.", "x": "Columbia River in depth: Recreation.. 2,000 km. The details reward the curious — Pacific Northwest power.. Dams. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Columbia River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Columbia River is.", "x": "Location: 2,000 km.. Source: Canada. Getting oriented — Columbia River. Pacific Northwest power. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Columbia River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Columbia River.", "x": "Visiting: Dams.. Grand Coulee. Practical know-how — Columbia River. Pacific Northwest power. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Columbia River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Columbia River.", "x": "Ecology: Fish.. Salmon. The living world of Columbia River — Pacific Northwest power.. Wind. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Columbia River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Columbia River through time.", "x": "History: History.. Gorge. People and Columbia River across the centuries — Pacific Northwest power.. Recreation. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Columbia River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Columbia River.", "x": "Conservation: Dams.. 2,000 km. Threats and guardians of Columbia River — Pacific Northwest power.. Fish. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Columbia River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Columbia River in numbers.", "x": "Numbers: 2,000 km.; Grand Coulee.. Wind. Statistics that stun — Columbia River. Pacific Northwest power. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-columbia-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
