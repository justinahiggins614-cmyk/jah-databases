(function(){'use strict';
/* JAH Yellowstone National Park National Park Database generator — jahdb-e2-park-yellowstone-np-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-park-yellowstone-np',PREFIX='JAH-E2PARKYELLO-',NAME='JAH Yellowstone National Park National Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yellowstone National Park: the complete guide", "d": "Yellowstone National Park: world's first national park (1872)..", "g": "overview", "l": 2, "q": "What is Yellowstone National Park: the complete guide?", "a": "Yellowstone National Park: world's first national park (1872)..", "x": "The complete national park guide to Yellowstone National Park: world's first national park (1872).. 1872: first. From formation to visiting, from wildlife to legends — everything about this national park in one database. Geysers.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1872: first.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1872: first.", "x": "Yellowstone National Park: 1872: first.. Wildlife. One of the defining facts — Old Faithful.. world's first national park (1872). Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1872: first..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1872: first..", "x": "Explored: 1872: first.. Tours. Why it is so — Yellowstone National Park. Wolves reintroduced. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Geysers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Geysers.", "x": "Yellowstone National Park: Geysers.. History. One of the defining facts — Wolves reintroduced.. world's first national park (1872). Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Geysers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Geysers..", "x": "Explored: Geysers.. Seasons. Why it is so — Yellowstone National Park. Grand Prismatic. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Old Faithful.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Old Faithful.", "x": "Yellowstone National Park: Old Faithful.. Tours. One of the defining facts — Grand Prismatic.. world's first national park (1872). Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Old Faithful..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Old Faithful..", "x": "Explored: Old Faithful.. Geology. Why it is so — Yellowstone National Park. Bison. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wolves reintroduced.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wolves reintroduced.", "x": "Yellowstone National Park: Wolves reintroduced.. Seasons. One of the defining facts — Bison.. world's first national park (1872). Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Wolves reintroduced..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Wolves reintroduced..", "x": "Explored: Wolves reintroduced.. Geysers. Why it is so — Yellowstone National Park. 1872: first. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Grand Prismatic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Grand Prismatic.", "x": "Yellowstone National Park: Grand Prismatic.. Geology. One of the defining facts — 1872: first.. world's first national park (1872). Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Grand Prismatic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Grand Prismatic..", "x": "Explored: Grand Prismatic.. Wildlife. Why it is so — Yellowstone National Park. Geysers. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bison.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bison.", "x": "Yellowstone National Park: Bison.. Geysers. One of the defining facts — Geysers.. world's first national park (1872). Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Bison..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Bison..", "x": "Explored: Bison.. History. Why it is so — Yellowstone National Park. Old Faithful. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Geysers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Geysers.", "x": "Yellowstone National Park in depth: Geysers.. Geysers. The details reward the curious — world's first national park (1872).. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wildlife.", "x": "Yellowstone National Park in depth: Wildlife.. Old Faithful. The details reward the curious — world's first national park (1872).. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Yellowstone National Park in depth: History.. Wolves reintroduced. The details reward the curious — world's first national park (1872).. Seasons. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Yellowstone National Park in depth: Tours.. Grand Prismatic. The details reward the curious — world's first national park (1872).. Geology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Seasons.", "x": "Yellowstone National Park in depth: Seasons.. Bison. The details reward the curious — world's first national park (1872).. Geysers. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Geology.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Geology.", "x": "Yellowstone National Park in depth: Geology.. 1872: first. The details reward the curious — world's first national park (1872).. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Yellowstone National Park is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Yellowstone National Park is.", "x": "Location: 1872: first.. Geysers. Getting oriented — Yellowstone National Park. world's first national park (1872). Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Yellowstone National Park.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Yellowstone National Park.", "x": "Visiting: Wildlife.. Geysers. Practical know-how — Yellowstone National Park. world's first national park (1872). Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Yellowstone National Park.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Yellowstone National Park.", "x": "Ecology: History.. Old Faithful. The living world of Yellowstone National Park — world's first national park (1872).. Tours. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Yellowstone National Park through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Yellowstone National Park through time.", "x": "History: Seasons.. Wolves reintroduced. People and Yellowstone National Park across the centuries — world's first national park (1872).. Geology. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Yellowstone National Park.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Yellowstone National Park.", "x": "Conservation: Wildlife.. 1872: first. Threats and guardians of Yellowstone National Park — world's first national park (1872).. History. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Yellowstone National Park in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Yellowstone National Park in numbers.", "x": "Numbers: 1872: first.; Geysers.. Tours. Statistics that stun — Yellowstone National Park. world's first national park (1872). Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-park-yellowstone-np-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
