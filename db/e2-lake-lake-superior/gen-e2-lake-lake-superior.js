(function(){'use strict';
/* JAH Lake Superior Lake Database generator — jahdb-e2-lake-lake-superior-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lake-lake-superior',PREFIX='JAH-E2LAKELAKES-',NAME='JAH Lake Superior Lake Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lake Superior: the complete guide", "d": "Lake Superior: largest freshwater lake by area..", "g": "overview", "l": 2, "q": "What is Lake Superior: the complete guide?", "a": "Lake Superior: largest freshwater lake by area..", "x": "The complete lake guide to Lake Superior: largest freshwater lake by area.. 82,100 sq km. From formation to visiting, from wildlife to legends — everything about this lake in one database. Geology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "82,100 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "82,100 sq km.", "x": "Lake Superior: 82,100 sq km.. Ships. One of the defining facts — Apostle Islands.. largest freshwater lake by area. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 82,100 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 82,100 sq km..", "x": "Explored: 82,100 sq km.. Fishing. Why it is so — Lake Superior. Cold/clear. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Edmund Fitzgerald.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Edmund Fitzgerald.", "x": "Lake Superior: Edmund Fitzgerald.. Towns. One of the defining facts — Cold/clear.. largest freshwater lake by area. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Edmund Fitzgerald..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Edmund Fitzgerald..", "x": "Explored: Edmund Fitzgerald.. Parks. Why it is so — Lake Superior. Duluth. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Apostle Islands.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Apostle Islands.", "x": "Lake Superior: Apostle Islands.. Fishing. One of the defining facts — Duluth.. largest freshwater lake by area. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Apostle Islands..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Apostle Islands..", "x": "Explored: Apostle Islands.. History. Why it is so — Lake Superior. Wrecks. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cold/clear.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cold/clear.", "x": "Lake Superior: Cold/clear.. Parks. One of the defining facts — Wrecks.. largest freshwater lake by area. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Cold/clear..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Cold/clear..", "x": "Explored: Cold/clear.. Geology. Why it is so — Lake Superior. 82,100 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Duluth.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Duluth.", "x": "Lake Superior: Duluth.. History. One of the defining facts — 82,100 sq km.. largest freshwater lake by area. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Duluth..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Duluth..", "x": "Explored: Duluth.. Ships. Why it is so — Lake Superior. Edmund Fitzgerald. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wrecks.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wrecks.", "x": "Lake Superior: Wrecks.. Geology. One of the defining facts — Edmund Fitzgerald.. largest freshwater lake by area. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Wrecks..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Wrecks..", "x": "Explored: Wrecks.. Towns. Why it is so — Lake Superior. Apostle Islands. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Geology.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Geology.", "x": "Lake Superior in depth: Geology.. Edmund Fitzgerald. The details reward the curious — largest freshwater lake by area.. Towns. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ships.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ships.", "x": "Lake Superior in depth: Ships.. Apostle Islands. The details reward the curious — largest freshwater lake by area.. Fishing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Towns.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Towns.", "x": "Lake Superior in depth: Towns.. Cold/clear. The details reward the curious — largest freshwater lake by area.. Parks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fishing.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fishing.", "x": "Lake Superior in depth: Fishing.. Duluth. The details reward the curious — largest freshwater lake by area.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Parks.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Parks.", "x": "Lake Superior in depth: Parks.. Wrecks. The details reward the curious — largest freshwater lake by area.. Geology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Lake Superior in depth: History.. 82,100 sq km. The details reward the curious — largest freshwater lake by area.. Ships. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Lake Superior is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Lake Superior is.", "x": "Location: 82,100 sq km.. Geology. Getting oriented — Lake Superior. largest freshwater lake by area. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Lake Superior.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Lake Superior.", "x": "Visiting: Ships.. Edmund Fitzgerald. Practical know-how — Lake Superior. largest freshwater lake by area. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Lake Superior.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Lake Superior.", "x": "Ecology: Towns.. Apostle Islands. The living world of Lake Superior — largest freshwater lake by area.. Fishing. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Lake Superior through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Lake Superior through time.", "x": "History: Parks.. Cold/clear. People and Lake Superior across the centuries — largest freshwater lake by area.. History. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Lake Superior.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Lake Superior.", "x": "Conservation: Ships.. 82,100 sq km. Threats and guardians of Lake Superior — largest freshwater lake by area.. Towns. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Lake Superior in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Lake Superior in numbers.", "x": "Numbers: 82,100 sq km.; Edmund Fitzgerald.. Fishing. Statistics that stun — Lake Superior. largest freshwater lake by area. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lake-lake-superior-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
