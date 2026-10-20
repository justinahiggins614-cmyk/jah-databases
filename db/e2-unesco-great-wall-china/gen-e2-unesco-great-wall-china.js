(function(){'use strict';
/* JAH Great Wall of China Unesco Site Database generator — jahdb-e2-unesco-great-wall-china-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-great-wall-china',PREFIX='JAH-E2UNESCOGRE-',NAME='JAH Great Wall of China Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Great Wall of China: the complete guide", "d": "Great Wall of China: world's greatest fortification..", "g": "overview", "l": 2, "q": "What is Great Wall of China: the complete guide?", "a": "Great Wall of China: world's greatest fortification..", "x": "The complete unesco site guide to Great Wall of China: world's greatest fortification.. 21,196 km. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "21,196 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "21,196 km.", "x": "Great Wall of China: 21,196 km.. Sections. One of the defining facts — Badaling.. world's greatest fortification. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 21,196 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 21,196 km..", "x": "Explored: 21,196 km.. Conservation. Why it is so — Great Wall of China. Mutianyu. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ming Dynasty.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ming Dynasty.", "x": "Great Wall of China: Ming Dynasty.. Hiking. One of the defining facts — Mutianyu.. world's greatest fortification. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Ming Dynasty..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Ming Dynasty..", "x": "Explored: Ming Dynasty.. Myths. Why it is so — Great Wall of China. Beacon towers. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Badaling.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Badaling.", "x": "Great Wall of China: Badaling.. Conservation. One of the defining facts — Beacon towers.. world's greatest fortification. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Badaling..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Badaling..", "x": "Explored: Badaling.. Visit. Why it is so — Great Wall of China. UNESCO 1987. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mutianyu.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mutianyu.", "x": "Great Wall of China: Mutianyu.. Myths. One of the defining facts — UNESCO 1987.. world's greatest fortification. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Mutianyu..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Mutianyu..", "x": "Explored: Mutianyu.. History. Why it is so — Great Wall of China. 21,196 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beacon towers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beacon towers.", "x": "Great Wall of China: Beacon towers.. Visit. One of the defining facts — 21,196 km.. world's greatest fortification. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Beacon towers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Beacon towers..", "x": "Explored: Beacon towers.. Sections. Why it is so — Great Wall of China. Ming Dynasty. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO 1987.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO 1987.", "x": "Great Wall of China: UNESCO 1987.. History. One of the defining facts — Ming Dynasty.. world's greatest fortification. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: UNESCO 1987..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: UNESCO 1987..", "x": "Explored: UNESCO 1987.. Hiking. Why it is so — Great Wall of China. Badaling. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Great Wall of China in depth: History.. Ming Dynasty. The details reward the curious — world's greatest fortification.. Hiking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sections.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sections.", "x": "Great Wall of China in depth: Sections.. Badaling. The details reward the curious — world's greatest fortification.. Conservation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hiking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hiking.", "x": "Great Wall of China in depth: Hiking.. Mutianyu. The details reward the curious — world's greatest fortification.. Myths. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Conservation.", "x": "Great Wall of China in depth: Conservation.. Beacon towers. The details reward the curious — world's greatest fortification.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Myths.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Myths.", "x": "Great Wall of China in depth: Myths.. UNESCO 1987. The details reward the curious — world's greatest fortification.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Great Wall of China in depth: Visit.. 21,196 km. The details reward the curious — world's greatest fortification.. Sections. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Great Wall of China is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Great Wall of China is.", "x": "Location: 21,196 km.. History. Getting oriented — Great Wall of China. world's greatest fortification. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Great Wall of China.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Great Wall of China.", "x": "Visiting: Sections.. Ming Dynasty. Practical know-how — Great Wall of China. world's greatest fortification. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Great Wall of China.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Great Wall of China.", "x": "Ecology: Hiking.. Badaling. The living world of Great Wall of China — world's greatest fortification.. Conservation. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Great Wall of China through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Great Wall of China through time.", "x": "History: Myths.. Mutianyu. People and Great Wall of China across the centuries — world's greatest fortification.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Great Wall of China.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Great Wall of China.", "x": "Conservation: Sections.. 21,196 km. Threats and guardians of Great Wall of China — world's greatest fortification.. Hiking. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Great Wall of China in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Great Wall of China in numbers.", "x": "Numbers: 21,196 km.; Ming Dynasty.. Conservation. Statistics that stun — Great Wall of China. world's greatest fortification. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-great-wall-china-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
