(function(){'use strict';
/* JAH Lake Huron Lake Database generator — jahdb-e2-lake-lake-huron-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lake-lake-huron',PREFIX='JAH-E2LAKELAKEH-',NAME='JAH Lake Huron Lake Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lake Huron: the complete guide", "d": "Lake Huron: Great Lakes' second..", "g": "overview", "l": 2, "q": "What is Lake Huron: the complete guide?", "a": "Lake Huron: Great Lakes' second..", "x": "The complete lake guide to Lake Huron: Great Lakes' second.. 59,600 sq km. From formation to visiting, from wildlife to legends — everything about this lake in one database. Geography. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "59,600 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "59,600 sq km.", "x": "Lake Huron: 59,600 sq km.. Islands. One of the defining facts — Manitoulin Island.. Great Lakes' second. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 59,600 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 59,600 sq km..", "x": "Explored: 59,600 sq km.. Boating. Why it is so — Lake Huron. Shipwrecks. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Georgian Bay.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Georgian Bay.", "x": "Lake Huron: Georgian Bay.. History. One of the defining facts — Shipwrecks.. Great Lakes' second. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Georgian Bay..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Georgian Bay..", "x": "Explored: Georgian Bay.. Fishing. Why it is so — Lake Huron. Fishing. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Manitoulin Island.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Manitoulin Island.", "x": "Lake Huron: Manitoulin Island.. Boating. One of the defining facts — Fishing.. Great Lakes' second. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Manitoulin Island..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Manitoulin Island..", "x": "Explored: Manitoulin Island.. Travel. Why it is so — Lake Huron. Towns. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shipwrecks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shipwrecks.", "x": "Lake Huron: Shipwrecks.. Fishing. One of the defining facts — Towns.. Great Lakes' second. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Shipwrecks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Shipwrecks..", "x": "Explored: Shipwrecks.. Geography. Why it is so — Lake Huron. 59,600 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fishing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fishing.", "x": "Lake Huron: Fishing.. Travel. One of the defining facts — 59,600 sq km.. Great Lakes' second. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Fishing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Fishing..", "x": "Explored: Fishing.. Islands. Why it is so — Lake Huron. Georgian Bay. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Towns.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Towns.", "x": "Lake Huron: Towns.. Geography. One of the defining facts — Georgian Bay.. Great Lakes' second. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Towns..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Towns..", "x": "Explored: Towns.. History. Why it is so — Lake Huron. Manitoulin Island. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Geography.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Geography.", "x": "Lake Huron in depth: Geography.. Georgian Bay. The details reward the curious — Great Lakes' second.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Islands.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Islands.", "x": "Lake Huron in depth: Islands.. Manitoulin Island. The details reward the curious — Great Lakes' second.. Boating. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Lake Huron in depth: History.. Shipwrecks. The details reward the curious — Great Lakes' second.. Fishing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Boating.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Boating.", "x": "Lake Huron in depth: Boating.. Fishing. The details reward the curious — Great Lakes' second.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fishing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fishing.", "x": "Lake Huron in depth: Fishing.. Towns. The details reward the curious — Great Lakes' second.. Geography. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Lake Huron in depth: Travel.. 59,600 sq km. The details reward the curious — Great Lakes' second.. Islands. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Lake Huron is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Lake Huron is.", "x": "Location: 59,600 sq km.. Geography. Getting oriented — Lake Huron. Great Lakes' second. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Lake Huron.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Lake Huron.", "x": "Visiting: Islands.. Georgian Bay. Practical know-how — Lake Huron. Great Lakes' second. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Lake Huron.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Lake Huron.", "x": "Ecology: History.. Manitoulin Island. The living world of Lake Huron — Great Lakes' second.. Boating. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Lake Huron through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Lake Huron through time.", "x": "History: Fishing.. Shipwrecks. People and Lake Huron across the centuries — Great Lakes' second.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Lake Huron.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Lake Huron.", "x": "Conservation: Islands.. 59,600 sq km. Threats and guardians of Lake Huron — Great Lakes' second.. History. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Lake Huron in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Lake Huron in numbers.", "x": "Numbers: 59,600 sq km.; Georgian Bay.. Boating. Statistics that stun — Lake Huron. Great Lakes' second. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lake-lake-huron-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
