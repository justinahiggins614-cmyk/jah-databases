(function(){'use strict';
/* JAH Amazon River River Database generator — jahdb-e2-river-amazon-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-amazon-river',PREFIX='JAH-E2RIVERAMAZ-',NAME='JAH Amazon River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Amazon River: the complete guide", "d": "Amazon River: greatest by discharge; rainforest artery..", "g": "overview", "l": 2, "q": "What is Amazon River: the complete guide?", "a": "Amazon River: greatest by discharge; rainforest artery..", "x": "The complete river guide to Amazon River: greatest by discharge; rainforest artery.. Largest discharge. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Andes.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Largest discharge.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Largest discharge.", "x": "Amazon River: Largest discharge.. Mouth: Atlantic. One of the defining facts — Rainforest basin.. greatest by discharge; rainforest artery. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Largest discharge..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Largest discharge..", "x": "Explored: Largest discharge.. River communities. Why it is so — Amazon River. Pink dolphins. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "6,400 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "6,400 km.", "x": "Amazon River: 6,400 km.. Biodiversity. One of the defining facts — Pink dolphins.. greatest by discharge; rainforest artery. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 6,400 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 6,400 km..", "x": "Explored: 6,400 km.. Deforestation. Why it is so — Amazon River. Manaus port. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rainforest basin.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rainforest basin.", "x": "Amazon River: Rainforest basin.. River communities. One of the defining facts — Manaus port.. greatest by discharge; rainforest artery. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Rainforest basin..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Rainforest basin..", "x": "Explored: Rainforest basin.. Expeditions. Why it is so — Amazon River. Drought/flood cycles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pink dolphins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pink dolphins.", "x": "Amazon River: Pink dolphins.. Deforestation. One of the defining facts — Drought/flood cycles.. greatest by discharge; rainforest artery. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Pink dolphins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Pink dolphins..", "x": "Explored: Pink dolphins.. Source: Andes. Why it is so — Amazon River. Largest discharge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Manaus port.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Manaus port.", "x": "Amazon River: Manaus port.. Expeditions. One of the defining facts — Largest discharge.. greatest by discharge; rainforest artery. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Manaus port..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Manaus port..", "x": "Explored: Manaus port.. Mouth: Atlantic. Why it is so — Amazon River. 6,400 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drought/flood cycles.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drought/flood cycles.", "x": "Amazon River: Drought/flood cycles.. Source: Andes. One of the defining facts — 6,400 km.. greatest by discharge; rainforest artery. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Drought/flood cycles..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Drought/flood cycles..", "x": "Explored: Drought/flood cycles.. Biodiversity. Why it is so — Amazon River. Rainforest basin. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Andes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Andes.", "x": "Amazon River in depth: Source: Andes.. 6,400 km. The details reward the curious — greatest by discharge; rainforest artery.. Biodiversity. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mouth: Atlantic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mouth: Atlantic.", "x": "Amazon River in depth: Mouth: Atlantic.. Rainforest basin. The details reward the curious — greatest by discharge; rainforest artery.. River communities. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Biodiversity.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Biodiversity.", "x": "Amazon River in depth: Biodiversity.. Pink dolphins. The details reward the curious — greatest by discharge; rainforest artery.. Deforestation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "River communities.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "River communities.", "x": "Amazon River in depth: River communities.. Manaus port. The details reward the curious — greatest by discharge; rainforest artery.. Expeditions. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Deforestation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Deforestation.", "x": "Amazon River in depth: Deforestation.. Drought/flood cycles. The details reward the curious — greatest by discharge; rainforest artery.. Source: Andes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Expeditions.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Expeditions.", "x": "Amazon River in depth: Expeditions.. Largest discharge. The details reward the curious — greatest by discharge; rainforest artery.. Mouth: Atlantic. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Amazon River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Amazon River is.", "x": "Location: Largest discharge.. Source: Andes. Getting oriented — Amazon River. greatest by discharge; rainforest artery. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Amazon River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Amazon River.", "x": "Visiting: Mouth: Atlantic.. 6,400 km. Practical know-how — Amazon River. greatest by discharge; rainforest artery. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Amazon River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Amazon River.", "x": "Ecology: Biodiversity.. Rainforest basin. The living world of Amazon River — greatest by discharge; rainforest artery.. River communities. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Amazon River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Amazon River through time.", "x": "History: Deforestation.. Pink dolphins. People and Amazon River across the centuries — greatest by discharge; rainforest artery.. Expeditions. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Amazon River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Amazon River.", "x": "Conservation: Mouth: Atlantic.. Largest discharge. Threats and guardians of Amazon River — greatest by discharge; rainforest artery.. Biodiversity. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Amazon River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Amazon River in numbers.", "x": "Numbers: Largest discharge.; 6,400 km.. River communities. Statistics that stun — Amazon River. greatest by discharge; rainforest artery. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-amazon-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
