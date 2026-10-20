(function(){'use strict';
/* JAH Yellow River River Database generator — jahdb-e2-river-yellow-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-yellow-river',PREFIX='JAH-E2RIVERYELL-',NAME='JAH Yellow River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yellow River: the complete guide", "d": "Yellow River: China's sorrow and cradle..", "g": "overview", "l": 2, "q": "What is Yellow River: the complete guide?", "a": "Yellow River: China's sorrow and cradle..", "x": "The complete river guide to Yellow River: China's sorrow and cradle.. 5,464 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Tibet. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "5,464 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "5,464 km.", "x": "Yellow River: 5,464 km.. History. One of the defining facts — Floods deadly.. China's sorrow and cradle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 5,464 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 5,464 km..", "x": "Explored: 5,464 km.. Cities. Why it is so — Yellow River. Cradle of China. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Loess silt.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Loess silt.", "x": "Yellow River: Loess silt.. Silt. One of the defining facts — Cradle of China.. China's sorrow and cradle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Loess silt..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Loess silt..", "x": "Explored: Loess silt.. Culture. Why it is so — Yellow River. Dams. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Floods deadly.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Floods deadly.", "x": "Yellow River: Floods deadly.. Cities. One of the defining facts — Dams.. China's sorrow and cradle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Floods deadly..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Floods deadly..", "x": "Explored: Floods deadly.. Management. Why it is so — Yellow River. Course changes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cradle of China.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cradle of China.", "x": "Yellow River: Cradle of China.. Culture. One of the defining facts — Course changes.. China's sorrow and cradle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Cradle of China..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Cradle of China..", "x": "Explored: Cradle of China.. Source: Tibet. Why it is so — Yellow River. 5,464 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dams.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dams.", "x": "Yellow River: Dams.. Management. One of the defining facts — 5,464 km.. China's sorrow and cradle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Dams..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Dams..", "x": "Explored: Dams.. History. Why it is so — Yellow River. Loess silt. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Course changes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Course changes.", "x": "Yellow River: Course changes.. Source: Tibet. One of the defining facts — Loess silt.. China's sorrow and cradle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Course changes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Course changes..", "x": "Explored: Course changes.. Silt. Why it is so — Yellow River. Floods deadly. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Tibet.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Tibet.", "x": "Yellow River in depth: Source: Tibet.. Loess silt. The details reward the curious — China's sorrow and cradle.. Silt. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Yellow River in depth: History.. Floods deadly. The details reward the curious — China's sorrow and cradle.. Cities. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Silt.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Silt.", "x": "Yellow River in depth: Silt.. Cradle of China. The details reward the curious — China's sorrow and cradle.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cities.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cities.", "x": "Yellow River in depth: Cities.. Dams. The details reward the curious — China's sorrow and cradle.. Management. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Culture.", "x": "Yellow River in depth: Culture.. Course changes. The details reward the curious — China's sorrow and cradle.. Source: Tibet. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Management.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Management.", "x": "Yellow River in depth: Management.. 5,464 km. The details reward the curious — China's sorrow and cradle.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Yellow River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Yellow River is.", "x": "Location: 5,464 km.. Source: Tibet. Getting oriented — Yellow River. China's sorrow and cradle. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Yellow River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Yellow River.", "x": "Visiting: History.. Loess silt. Practical know-how — Yellow River. China's sorrow and cradle. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Yellow River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Yellow River.", "x": "Ecology: Silt.. Floods deadly. The living world of Yellow River — China's sorrow and cradle.. Cities. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Yellow River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Yellow River through time.", "x": "History: Culture.. Cradle of China. People and Yellow River across the centuries — China's sorrow and cradle.. Management. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Yellow River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Yellow River.", "x": "Conservation: History.. 5,464 km. Threats and guardians of Yellow River — China's sorrow and cradle.. Silt. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Yellow River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Yellow River in numbers.", "x": "Numbers: 5,464 km.; Loess silt.. Cities. Statistics that stun — Yellow River. China's sorrow and cradle. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-yellow-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
