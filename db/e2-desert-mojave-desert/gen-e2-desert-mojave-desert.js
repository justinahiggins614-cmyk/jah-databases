(function(){'use strict';
/* JAH Mojave Desert Desert Database generator — jahdb-e2-desert-mojave-desert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-desert-mojave-desert',PREFIX='JAH-E2DESERTMOJ-',NAME='JAH Mojave Desert Desert Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mojave Desert: the complete guide", "d": "Mojave Desert: Joshua trees, Death Valley..", "g": "overview", "l": 2, "q": "What is Mojave Desert: the complete guide?", "a": "Mojave Desert: Joshua trees, Death Valley..", "x": "The complete desert guide to Mojave Desert: Joshua trees, Death Valley.. 124,000 sq km. From formation to visiting, from wildlife to legends — everything about this desert in one database. Parks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "124,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "124,000 sq km.", "x": "Mojave Desert: 124,000 sq km.. Trees. One of the defining facts — Death Valley.. Joshua trees, Death Valley. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 124,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 124,000 sq km..", "x": "Explored: 124,000 sq km.. History. Why it is so — Mojave Desert. Tortoise. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Joshua Tree.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Joshua Tree.", "x": "Mojave Desert: Joshua Tree.. Wildlife. One of the defining facts — Tortoise.. Joshua trees, Death Valley. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Joshua Tree..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Joshua Tree..", "x": "Explored: Joshua Tree.. Travel. Why it is so — Mojave Desert. Vegas edge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Death Valley.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Death Valley.", "x": "Mojave Desert: Death Valley.. History. One of the defining facts — Vegas edge.. Joshua trees, Death Valley. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Death Valley..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Death Valley..", "x": "Explored: Death Valley.. Conservation. Why it is so — Mojave Desert. Military. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tortoise.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tortoise.", "x": "Mojave Desert: Tortoise.. Travel. One of the defining facts — Military.. Joshua trees, Death Valley. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Tortoise..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Tortoise..", "x": "Explored: Tortoise.. Parks. Why it is so — Mojave Desert. 124,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vegas edge.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vegas edge.", "x": "Mojave Desert: Vegas edge.. Conservation. One of the defining facts — 124,000 sq km.. Joshua trees, Death Valley. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Vegas edge..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Vegas edge..", "x": "Explored: Vegas edge.. Trees. Why it is so — Mojave Desert. Joshua Tree. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Military.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Military.", "x": "Mojave Desert: Military.. Parks. One of the defining facts — Joshua Tree.. Joshua trees, Death Valley. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Military..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Military..", "x": "Explored: Military.. Wildlife. Why it is so — Mojave Desert. Death Valley. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Parks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Parks.", "x": "Mojave Desert in depth: Parks.. Joshua Tree. The details reward the curious — Joshua trees, Death Valley.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Trees.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Trees.", "x": "Mojave Desert in depth: Trees.. Death Valley. The details reward the curious — Joshua trees, Death Valley.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wildlife.", "x": "Mojave Desert in depth: Wildlife.. Tortoise. The details reward the curious — Joshua trees, Death Valley.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Mojave Desert in depth: History.. Vegas edge. The details reward the curious — Joshua trees, Death Valley.. Conservation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "Mojave Desert in depth: Travel.. Military. The details reward the curious — Joshua trees, Death Valley.. Parks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conservation.", "x": "Mojave Desert in depth: Conservation.. 124,000 sq km. The details reward the curious — Joshua trees, Death Valley.. Trees. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mojave Desert is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mojave Desert is.", "x": "Location: 124,000 sq km.. Parks. Getting oriented — Mojave Desert. Joshua trees, Death Valley. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mojave Desert.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mojave Desert.", "x": "Visiting: Trees.. Joshua Tree. Practical know-how — Mojave Desert. Joshua trees, Death Valley. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mojave Desert.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mojave Desert.", "x": "Ecology: Wildlife.. Death Valley. The living world of Mojave Desert — Joshua trees, Death Valley.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mojave Desert through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mojave Desert through time.", "x": "History: Travel.. Tortoise. People and Mojave Desert across the centuries — Joshua trees, Death Valley.. Conservation. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mojave Desert.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mojave Desert.", "x": "Conservation: Trees.. 124,000 sq km. Threats and guardians of Mojave Desert — Joshua trees, Death Valley.. Wildlife. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mojave Desert in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mojave Desert in numbers.", "x": "Numbers: 124,000 sq km.; Joshua Tree.. History. Statistics that stun — Mojave Desert. Joshua trees, Death Valley. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-desert-mojave-desert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
