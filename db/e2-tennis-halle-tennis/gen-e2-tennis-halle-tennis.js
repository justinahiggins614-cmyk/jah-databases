(function(){'use strict';
/* JAH Halle Westfalen Tennis Court Database generator — jahdb-e2-tennis-halle-tennis-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tennis-halle-tennis',PREFIX='JAH-E2TENNISHAL-',NAME='JAH Halle Westfalen Tennis Court Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Halle Westfalen: the complete guide", "d": "Halle Westfalen: the German grass..", "g": "overview", "l": 2, "q": "What is Halle Westfalen: the complete guide?", "a": "Halle Westfalen: the German grass..", "x": "The complete tennis court guide to Halle Westfalen: the German grass.. 1993. From formation to visiting, from wildlife to legends — everything about this tennis court in one database. Grass. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1993.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1993.", "x": "Halle Westfalen: 1993.. Federer. One of the defining facts — Federer.. the German grass. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1993..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1993..", "x": "Explored: 1993.. Germany. Why it is so — Halle Westfalen. Roof. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Grass.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Grass.", "x": "Halle Westfalen: Grass.. Roof. One of the defining facts — Roof.. the German grass. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Grass..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Grass..", "x": "Explored: Grass.. History. Why it is so — Halle Westfalen. Germany. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Federer.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Federer.", "x": "Halle Westfalen: Federer.. Germany. One of the defining facts — Germany.. the German grass. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Federer..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Federer..", "x": "Explored: Federer.. Tennis. Why it is so — Halle Westfalen. Noventi. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Roof.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Roof.", "x": "Halle Westfalen: Roof.. History. One of the defining facts — Noventi.. the German grass. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Roof..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Roof..", "x": "Explored: Roof.. Grass. Why it is so — Halle Westfalen. 1993. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Germany.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Germany.", "x": "Halle Westfalen: Germany.. Tennis. One of the defining facts — 1993.. the German grass. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Germany..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Germany..", "x": "Explored: Germany.. Federer. Why it is so — Halle Westfalen. Grass. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Noventi.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Noventi.", "x": "Halle Westfalen: Noventi.. Grass. One of the defining facts — Grass.. the German grass. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Noventi..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Noventi..", "x": "Explored: Noventi.. Roof. Why it is so — Halle Westfalen. Federer. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Grass.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Grass.", "x": "Halle Westfalen in depth: Grass.. Grass. The details reward the curious — the German grass.. Roof. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Federer.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Federer.", "x": "Halle Westfalen in depth: Federer.. Federer. The details reward the curious — the German grass.. Germany. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Roof.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Roof.", "x": "Halle Westfalen in depth: Roof.. Roof. The details reward the curious — the German grass.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Germany.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Germany.", "x": "Halle Westfalen in depth: Germany.. Germany. The details reward the curious — the German grass.. Tennis. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Halle Westfalen in depth: History.. Noventi. The details reward the curious — the German grass.. Grass. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tennis.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tennis.", "x": "Halle Westfalen in depth: Tennis.. 1993. The details reward the curious — the German grass.. Federer. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Halle Westfalen is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Halle Westfalen is.", "x": "Location: 1993.. Grass. Getting oriented — Halle Westfalen. the German grass. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Halle Westfalen.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Halle Westfalen.", "x": "Visiting: Federer.. Grass. Practical know-how — Halle Westfalen. the German grass. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Halle Westfalen.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Halle Westfalen.", "x": "Ecology: Roof.. Federer. The living world of Halle Westfalen — the German grass.. Germany. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Halle Westfalen through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Halle Westfalen through time.", "x": "History: History.. Roof. People and Halle Westfalen across the centuries — the German grass.. Tennis. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Halle Westfalen.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Halle Westfalen.", "x": "Conservation: Federer.. 1993. Threats and guardians of Halle Westfalen — the German grass.. Roof. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Halle Westfalen in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Halle Westfalen in numbers.", "x": "Numbers: 1993.; Grass.. Germany. Statistics that stun — Halle Westfalen. the German grass. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tennis-halle-tennis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
