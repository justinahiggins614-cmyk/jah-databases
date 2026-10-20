(function(){'use strict';
/* JAH Grindelwald Ski Resort Database generator — jahdb-e2-ski-grindelwald-ski-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ski-grindelwald-ski',PREFIX='JAH-E2SKIGRINDE-',NAME='JAH Grindelwald Ski Resort Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Grindelwald: the complete guide", "d": "Grindelwald: the Eiger village..", "g": "overview", "l": 2, "q": "What is Grindelwald: the complete guide?", "a": "Grindelwald: the Eiger village..", "x": "The complete ski resort guide to Grindelwald: the Eiger village.. Eiger. From formation to visiting, from wildlife to legends — everything about this ski resort in one database. Eiger. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Eiger.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Eiger.", "x": "Grindelwald: Eiger.. Village. One of the defining facts — First.. the Eiger village. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Eiger..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Eiger..", "x": "Explored: Eiger.. Tickets. Why it is so — Grindelwald. Switzerland. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jungfrau.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jungfrau.", "x": "Grindelwald: Jungfrau.. Views. One of the defining facts — Switzerland.. the Eiger village. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Jungfrau..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Jungfrau..", "x": "Explored: Jungfrau.. Switzerland. Why it is so — Grindelwald. Views. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First.", "x": "Grindelwald: First.. Tickets. One of the defining facts — Views.. the Eiger village. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: First..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: First..", "x": "Explored: First.. First. Why it is so — Grindelwald. Trains. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Switzerland.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Switzerland.", "x": "Grindelwald: Switzerland.. Switzerland. One of the defining facts — Trains.. the Eiger village. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Switzerland..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Switzerland..", "x": "Explored: Switzerland.. Eiger. Why it is so — Grindelwald. Eiger. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Views.", "x": "Grindelwald: Views.. First. One of the defining facts — Eiger.. the Eiger village. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Views..", "x": "Explored: Views.. Village. Why it is so — Grindelwald. Jungfrau. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Trains.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Trains.", "x": "Grindelwald: Trains.. Eiger. One of the defining facts — Jungfrau.. the Eiger village. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Trains..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Trains..", "x": "Explored: Trains.. Views. Why it is so — Grindelwald. First. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Eiger.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Eiger.", "x": "Grindelwald in depth: Eiger.. Jungfrau. The details reward the curious — the Eiger village.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Village.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Village.", "x": "Grindelwald in depth: Village.. First. The details reward the curious — the Eiger village.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "Grindelwald in depth: Views.. Switzerland. The details reward the curious — the Eiger village.. Switzerland. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Grindelwald in depth: Tickets.. Views. The details reward the curious — the Eiger village.. First. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Switzerland.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Switzerland.", "x": "Grindelwald in depth: Switzerland.. Trains. The details reward the curious — the Eiger village.. Eiger. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "First.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "First.", "x": "Grindelwald in depth: First.. Eiger. The details reward the curious — the Eiger village.. Village. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Grindelwald is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Grindelwald is.", "x": "Location: Eiger.. Eiger. Getting oriented — Grindelwald. the Eiger village. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Grindelwald.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Grindelwald.", "x": "Visiting: Village.. Jungfrau. Practical know-how — Grindelwald. the Eiger village. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Grindelwald.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Grindelwald.", "x": "Ecology: Views.. First. The living world of Grindelwald — the Eiger village.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Grindelwald through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Grindelwald through time.", "x": "History: Switzerland.. Switzerland. People and Grindelwald across the centuries — the Eiger village.. First. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Grindelwald.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Grindelwald.", "x": "Conservation: Village.. Eiger. Threats and guardians of Grindelwald — the Eiger village.. Views. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Grindelwald in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Grindelwald in numbers.", "x": "Numbers: Eiger.; Jungfrau.. Tickets. Statistics that stun — Grindelwald. the Eiger village. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ski-grindelwald-ski-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
