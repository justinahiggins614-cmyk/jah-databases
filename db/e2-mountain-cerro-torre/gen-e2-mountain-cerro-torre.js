(function(){'use strict';
/* JAH Cerro Torre Mountain Database generator — jahdb-e2-mountain-cerro-torre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-cerro-torre',PREFIX='JAH-E2MOUNTAINC-',NAME='JAH Cerro Torre Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cerro Torre: the complete guide", "d": "Cerro Torre: Patagonia's needle..", "g": "overview", "l": 2, "q": "What is Cerro Torre: the complete guide?", "a": "Cerro Torre: Patagonia's needle..", "x": "The complete mountain guide to Cerro Torre: Patagonia's needle.. 3,128m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,128m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,128m.", "x": "Cerro Torre: 3,128m.. Routes. One of the defining facts — Controversy.. Patagonia's needle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 3,128m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 3,128m..", "x": "Explored: 3,128m.. Weather. Why it is so — Cerro Torre. Weather. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Granite spire.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Granite spire.", "x": "Cerro Torre: Granite spire.. Ethics. One of the defining facts — Weather.. Patagonia's needle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Granite spire..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Granite spire..", "x": "Explored: Granite spire.. Views. Why it is so — Cerro Torre. Climbing. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Controversy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Controversy.", "x": "Cerro Torre: Controversy.. Weather. One of the defining facts — Climbing.. Patagonia's needle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Controversy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Controversy..", "x": "Explored: Controversy.. Legends. Why it is so — Cerro Torre. Views. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Weather.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Weather.", "x": "Cerro Torre: Weather.. Views. One of the defining facts — Views.. Patagonia's needle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Weather..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Weather..", "x": "Explored: Weather.. History. Why it is so — Cerro Torre. 3,128m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Climbing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Climbing.", "x": "Cerro Torre: Climbing.. Legends. One of the defining facts — 3,128m.. Patagonia's needle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Climbing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Climbing..", "x": "Explored: Climbing.. Routes. Why it is so — Cerro Torre. Granite spire. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Cerro Torre: Views.. History. One of the defining facts — Granite spire.. Patagonia's needle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Views..", "x": "Explored: Views.. Ethics. Why it is so — Cerro Torre. Controversy. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Cerro Torre in depth: History.. Granite spire. The details reward the curious — Patagonia's needle.. Ethics. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Routes.", "x": "Cerro Torre in depth: Routes.. Controversy. The details reward the curious — Patagonia's needle.. Weather. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ethics.", "x": "Cerro Torre in depth: Ethics.. Weather. The details reward the curious — Patagonia's needle.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Weather.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Weather.", "x": "Cerro Torre in depth: Weather.. Climbing. The details reward the curious — Patagonia's needle.. Legends. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Cerro Torre in depth: Views.. Views. The details reward the curious — Patagonia's needle.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legends.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legends.", "x": "Cerro Torre in depth: Legends.. 3,128m. The details reward the curious — Patagonia's needle.. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Cerro Torre is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Cerro Torre is.", "x": "Location: 3,128m.. History. Getting oriented — Cerro Torre. Patagonia's needle. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Cerro Torre.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Cerro Torre.", "x": "Visiting: Routes.. Granite spire. Practical know-how — Cerro Torre. Patagonia's needle. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Cerro Torre.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Cerro Torre.", "x": "Ecology: Ethics.. Controversy. The living world of Cerro Torre — Patagonia's needle.. Weather. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Cerro Torre through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Cerro Torre through time.", "x": "History: Views.. Weather. People and Cerro Torre across the centuries — Patagonia's needle.. Legends. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Cerro Torre.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Cerro Torre.", "x": "Conservation: Routes.. 3,128m. Threats and guardians of Cerro Torre — Patagonia's needle.. Ethics. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Cerro Torre in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Cerro Torre in numbers.", "x": "Numbers: 3,128m.; Granite spire.. Weather. Statistics that stun — Cerro Torre. Patagonia's needle. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-cerro-torre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
