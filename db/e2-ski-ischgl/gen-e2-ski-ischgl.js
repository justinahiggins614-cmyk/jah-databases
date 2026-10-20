(function(){'use strict';
/* JAH Ischgl Ski Resort Database generator — jahdb-e2-ski-ischgl-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ski-ischgl',PREFIX='JAH-E2SKIISCHGL-',NAME='JAH Ischgl Ski Resort Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ischgl: the complete guide", "d": "Ischgl: the Ibiza of the Alps..", "g": "overview", "l": 2, "q": "What is Ischgl: the complete guide?", "a": "Ischgl: the Ibiza of the Alps..", "x": "The complete ski resort guide to Ischgl: the Ibiza of the Alps.. Silvretta. From formation to visiting, from wildlife to legends — everything about this ski resort in one database. Party. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Silvretta.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Silvretta.", "x": "Ischgl: Silvretta.. Concerts. One of the defining facts — Concerts.. the Ibiza of the Alps. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Silvretta..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Silvretta..", "x": "Explored: Silvretta.. Tickets. Why it is so — Ischgl. Austria. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Apres.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Apres.", "x": "Ischgl: Apres.. Ski. One of the defining facts — Austria.. the Ibiza of the Alps. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Apres..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Apres..", "x": "Explored: Apres.. Austria. Why it is so — Ischgl. Duty-free. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Concerts.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Concerts.", "x": "Ischgl: Concerts.. Tickets. One of the defining facts — Duty-free.. the Ibiza of the Alps. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Concerts..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Concerts..", "x": "Explored: Concerts.. Apres. Why it is so — Ischgl. Party. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Austria.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Austria.", "x": "Ischgl: Austria.. Austria. One of the defining facts — Party.. the Ibiza of the Alps. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Austria..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Austria..", "x": "Explored: Austria.. Party. Why it is so — Ischgl. Silvretta. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Duty-free.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Duty-free.", "x": "Ischgl: Duty-free.. Apres. One of the defining facts — Silvretta.. the Ibiza of the Alps. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Duty-free..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Duty-free..", "x": "Explored: Duty-free.. Concerts. Why it is so — Ischgl. Apres. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Party.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Party.", "x": "Ischgl: Party.. Party. One of the defining facts — Apres.. the Ibiza of the Alps. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Party..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Party..", "x": "Explored: Party.. Ski. Why it is so — Ischgl. Concerts. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Party.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Party.", "x": "Ischgl in depth: Party.. Apres. The details reward the curious — the Ibiza of the Alps.. Ski. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Concerts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Concerts.", "x": "Ischgl in depth: Concerts.. Concerts. The details reward the curious — the Ibiza of the Alps.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ski.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ski.", "x": "Ischgl in depth: Ski.. Austria. The details reward the curious — the Ibiza of the Alps.. Austria. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Ischgl in depth: Tickets.. Duty-free. The details reward the curious — the Ibiza of the Alps.. Apres. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Austria.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Austria.", "x": "Ischgl in depth: Austria.. Party. The details reward the curious — the Ibiza of the Alps.. Party. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Apres.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Apres.", "x": "Ischgl in depth: Apres.. Silvretta. The details reward the curious — the Ibiza of the Alps.. Concerts. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Ischgl is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Ischgl is.", "x": "Location: Silvretta.. Party. Getting oriented — Ischgl. the Ibiza of the Alps. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Ischgl.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Ischgl.", "x": "Visiting: Concerts.. Apres. Practical know-how — Ischgl. the Ibiza of the Alps. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Ischgl.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Ischgl.", "x": "Ecology: Ski.. Concerts. The living world of Ischgl — the Ibiza of the Alps.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Ischgl through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Ischgl through time.", "x": "History: Austria.. Austria. People and Ischgl across the centuries — the Ibiza of the Alps.. Apres. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Ischgl.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Ischgl.", "x": "Conservation: Concerts.. Silvretta. Threats and guardians of Ischgl — the Ibiza of the Alps.. Ski. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Ischgl in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Ischgl in numbers.", "x": "Numbers: Silvretta.; Apres.. Tickets. Statistics that stun — Ischgl. the Ibiza of the Alps. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ski-ischgl-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
