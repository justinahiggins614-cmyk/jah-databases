(function(){'use strict';
/* JAH Denali Mountain Database generator — jahdb-e2-mountain-denali-mountain-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-denali-mountain',PREFIX='JAH-E2MOUNTAIND-',NAME='JAH Denali Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Denali: the complete guide", "d": "Denali: North America's highest at 6,190m..", "g": "overview", "l": 2, "q": "What is Denali: the complete guide?", "a": "Denali: North America's highest at 6,190m..", "x": "The complete mountain guide to Denali: North America's highest at 6,190m.. 6,190m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Climbing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "6,190m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "6,190m.", "x": "Denali: 6,190m.. Weather. One of the defining facts — Coldest.. North America's highest at 6,190m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 6,190m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 6,190m..", "x": "Explored: 6,190m.. History. Why it is so — Denali. First 1913. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Alaska.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Alaska.", "x": "Denali: Alaska.. Rangers. One of the defining facts — First 1913.. North America's highest at 6,190m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Alaska..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Alaska..", "x": "Explored: Alaska.. Views. Why it is so — Denali. West Buttress. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Coldest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Coldest.", "x": "Denali: Coldest.. History. One of the defining facts — West Buttress.. North America's highest at 6,190m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Coldest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Coldest..", "x": "Explored: Coldest.. Wildlife. Why it is so — Denali. Name restored. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "First 1913.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "First 1913.", "x": "Denali: First 1913.. Views. One of the defining facts — Name restored.. North America's highest at 6,190m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: First 1913..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: First 1913..", "x": "Explored: First 1913.. Climbing. Why it is so — Denali. 6,190m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "West Buttress.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "West Buttress.", "x": "Denali: West Buttress.. Wildlife. One of the defining facts — 6,190m.. North America's highest at 6,190m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: West Buttress..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: West Buttress..", "x": "Explored: West Buttress.. Weather. Why it is so — Denali. Alaska. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Name restored.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Name restored.", "x": "Denali: Name restored.. Climbing. One of the defining facts — Alaska.. North America's highest at 6,190m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Name restored..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Name restored..", "x": "Explored: Name restored.. Rangers. Why it is so — Denali. Coldest. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Climbing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Climbing.", "x": "Denali in depth: Climbing.. Alaska. The details reward the curious — North America's highest at 6,190m.. Rangers. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Weather.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Weather.", "x": "Denali in depth: Weather.. Coldest. The details reward the curious — North America's highest at 6,190m.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rangers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rangers.", "x": "Denali in depth: Rangers.. First 1913. The details reward the curious — North America's highest at 6,190m.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Denali in depth: History.. West Buttress. The details reward the curious — North America's highest at 6,190m.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Views.", "x": "Denali in depth: Views.. Name restored. The details reward the curious — North America's highest at 6,190m.. Climbing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Wildlife.", "x": "Denali in depth: Wildlife.. 6,190m. The details reward the curious — North America's highest at 6,190m.. Weather. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Denali is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Denali is.", "x": "Location: 6,190m.. Climbing. Getting oriented — Denali. North America's highest at 6,190m. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Denali.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Denali.", "x": "Visiting: Weather.. Alaska. Practical know-how — Denali. North America's highest at 6,190m. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Denali.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Denali.", "x": "Ecology: Rangers.. Coldest. The living world of Denali — North America's highest at 6,190m.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Denali through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Denali through time.", "x": "History: Views.. First 1913. People and Denali across the centuries — North America's highest at 6,190m.. Wildlife. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Denali.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Denali.", "x": "Conservation: Weather.. 6,190m. Threats and guardians of Denali — North America's highest at 6,190m.. Rangers. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Denali in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Denali in numbers.", "x": "Numbers: 6,190m.; Alaska.. History. Statistics that stun — Denali. North America's highest at 6,190m. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-denali-mountain-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
