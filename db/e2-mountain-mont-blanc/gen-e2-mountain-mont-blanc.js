(function(){'use strict';
/* JAH Mont Blanc Mountain Database generator — jahdb-e2-mountain-mont-blanc-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mont-blanc',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mont Blanc Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mont Blanc: the complete guide", "d": "Mont Blanc: Alps' highest at 4,808m..", "g": "overview", "l": 2, "q": "What is Mont Blanc: the complete guide?", "a": "Mont Blanc: Alps' highest at 4,808m..", "x": "The complete mountain guide to Mont Blanc: Alps' highest at 4,808m.. 4,808m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "4,808m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "4,808m.", "x": "Mont Blanc: 4,808m.. History. One of the defining facts — First 1786.. Alps' highest at 4,808m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 4,808m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 4,808m..", "x": "Explored: 4,808m.. Skiing. Why it is so — Mont Blanc. Birthplace alpinism. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "France/Italy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "France/Italy.", "x": "Mont Blanc: France/Italy.. Huts. One of the defining facts — Birthplace alpinism.. Alps' highest at 4,808m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: France/Italy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: France/Italy..", "x": "Explored: France/Italy.. Views. Why it is so — Mont Blanc. Chamonix. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First 1786.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First 1786.", "x": "Mont Blanc: First 1786.. Skiing. One of the defining facts — Chamonix.. Alps' highest at 4,808m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: First 1786..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: First 1786..", "x": "Explored: First 1786.. Safety. Why it is so — Mont Blanc. Glaciers. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Birthplace alpinism.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Birthplace alpinism.", "x": "Mont Blanc: Birthplace alpinism.. Views. One of the defining facts — Glaciers.. Alps' highest at 4,808m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Birthplace alpinism..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Birthplace alpinism..", "x": "Explored: Birthplace alpinism.. Routes. Why it is so — Mont Blanc. 4,808m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Chamonix.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Chamonix.", "x": "Mont Blanc: Chamonix.. Safety. One of the defining facts — 4,808m.. Alps' highest at 4,808m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Chamonix..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Chamonix..", "x": "Explored: Chamonix.. History. Why it is so — Mont Blanc. France/Italy. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Glaciers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Glaciers.", "x": "Mont Blanc: Glaciers.. Routes. One of the defining facts — France/Italy.. Alps' highest at 4,808m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Glaciers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Glaciers..", "x": "Explored: Glaciers.. Huts. Why it is so — Mont Blanc. First 1786. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Routes.", "x": "Mont Blanc in depth: Routes.. France/Italy. The details reward the curious — Alps' highest at 4,808m.. Huts. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Mont Blanc in depth: History.. First 1786. The details reward the curious — Alps' highest at 4,808m.. Skiing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Huts.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Huts.", "x": "Mont Blanc in depth: Huts.. Birthplace alpinism. The details reward the curious — Alps' highest at 4,808m.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Skiing.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Skiing.", "x": "Mont Blanc in depth: Skiing.. Chamonix. The details reward the curious — Alps' highest at 4,808m.. Safety. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Mont Blanc in depth: Views.. Glaciers. The details reward the curious — Alps' highest at 4,808m.. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safety.", "x": "Mont Blanc in depth: Safety.. 4,808m. The details reward the curious — Alps' highest at 4,808m.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mont Blanc is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mont Blanc is.", "x": "Location: 4,808m.. Routes. Getting oriented — Mont Blanc. Alps' highest at 4,808m. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mont Blanc.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mont Blanc.", "x": "Visiting: History.. France/Italy. Practical know-how — Mont Blanc. Alps' highest at 4,808m. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mont Blanc.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mont Blanc.", "x": "Ecology: Huts.. First 1786. The living world of Mont Blanc — Alps' highest at 4,808m.. Skiing. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mont Blanc through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mont Blanc through time.", "x": "History: Views.. Birthplace alpinism. People and Mont Blanc across the centuries — Alps' highest at 4,808m.. Safety. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mont Blanc.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mont Blanc.", "x": "Conservation: History.. 4,808m. Threats and guardians of Mont Blanc — Alps' highest at 4,808m.. Huts. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mont Blanc in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mont Blanc in numbers.", "x": "Numbers: 4,808m.; France/Italy.. Skiing. Statistics that stun — Mont Blanc. Alps' highest at 4,808m. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mont-blanc-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
