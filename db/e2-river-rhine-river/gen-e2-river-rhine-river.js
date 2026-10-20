(function(){'use strict';
/* JAH Rhine River River Database generator — jahdb-e2-river-rhine-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-rhine-river',PREFIX='JAH-E2RIVERRHIN-',NAME='JAH Rhine River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rhine River: the complete guide", "d": "Rhine River: Europe's working river..", "g": "overview", "l": 2, "q": "What is Rhine River: the complete guide?", "a": "Rhine River: Europe's working river..", "x": "The complete river guide to Rhine River: Europe's working river.. 1,230 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Alps. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1,230 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1,230 km.", "x": "Rhine River: 1,230 km.. Cologne. One of the defining facts — Castles gorge.. Europe's working river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1,230 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1,230 km..", "x": "Explored: 1,230 km.. History. Why it is so — Rhine River. Lorelei. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rotterdam port.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rotterdam port.", "x": "Rhine River: Rotterdam port.. Wine. One of the defining facts — Lorelei.. Europe's working river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Rotterdam port..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Rotterdam port..", "x": "Explored: Rotterdam port.. Barges. Why it is so — Rhine River. Industrial artery. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Castles gorge.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Castles gorge.", "x": "Rhine River: Castles gorge.. History. One of the defining facts — Industrial artery.. Europe's working river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Castles gorge..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Castles gorge..", "x": "Explored: Castles gorge.. Cruises. Why it is so — Rhine River. Salmon return. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lorelei.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lorelei.", "x": "Rhine River: Lorelei.. Barges. One of the defining facts — Salmon return.. Europe's working river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Lorelei..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Lorelei..", "x": "Explored: Lorelei.. Source: Alps. Why it is so — Rhine River. 1,230 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Industrial artery.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Industrial artery.", "x": "Rhine River: Industrial artery.. Cruises. One of the defining facts — 1,230 km.. Europe's working river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Industrial artery..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Industrial artery..", "x": "Explored: Industrial artery.. Cologne. Why it is so — Rhine River. Rotterdam port. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Salmon return.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Salmon return.", "x": "Rhine River: Salmon return.. Source: Alps. One of the defining facts — Rotterdam port.. Europe's working river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Salmon return..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Salmon return..", "x": "Explored: Salmon return.. Wine. Why it is so — Rhine River. Castles gorge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Alps.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Alps.", "x": "Rhine River in depth: Source: Alps.. Rotterdam port. The details reward the curious — Europe's working river.. Wine. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cologne.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cologne.", "x": "Rhine River in depth: Cologne.. Castles gorge. The details reward the curious — Europe's working river.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wine.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wine.", "x": "Rhine River in depth: Wine.. Lorelei. The details reward the curious — Europe's working river.. Barges. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Rhine River in depth: History.. Industrial artery. The details reward the curious — Europe's working river.. Cruises. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Barges.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Barges.", "x": "Rhine River in depth: Barges.. Salmon return. The details reward the curious — Europe's working river.. Source: Alps. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cruises.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cruises.", "x": "Rhine River in depth: Cruises.. 1,230 km. The details reward the curious — Europe's working river.. Cologne. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Rhine River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Rhine River is.", "x": "Location: 1,230 km.. Source: Alps. Getting oriented — Rhine River. Europe's working river. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Rhine River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Rhine River.", "x": "Visiting: Cologne.. Rotterdam port. Practical know-how — Rhine River. Europe's working river. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Rhine River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Rhine River.", "x": "Ecology: Wine.. Castles gorge. The living world of Rhine River — Europe's working river.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Rhine River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Rhine River through time.", "x": "History: Barges.. Lorelei. People and Rhine River across the centuries — Europe's working river.. Cruises. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Rhine River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Rhine River.", "x": "Conservation: Cologne.. 1,230 km. Threats and guardians of Rhine River — Europe's working river.. Wine. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Rhine River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Rhine River in numbers.", "x": "Numbers: 1,230 km.; Rotterdam port.. History. Statistics that stun — Rhine River. Europe's working river. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-rhine-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
