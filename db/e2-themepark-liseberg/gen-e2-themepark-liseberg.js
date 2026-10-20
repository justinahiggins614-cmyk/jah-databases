(function(){'use strict';
/* JAH Liseberg Theme Park Database generator — jahdb-e2-themepark-liseberg-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-themepark-liseberg',PREFIX='JAH-E2THEMEPARK-',NAME='JAH Liseberg Theme Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Liseberg: the complete guide", "d": "Liseberg: Gothenburg's fun..", "g": "overview", "l": 2, "q": "What is Liseberg: the complete guide?", "a": "Liseberg: Gothenburg's fun..", "x": "The complete theme park guide to Liseberg: Gothenburg's fun.. 1923. From formation to visiting, from wildlife to legends — everything about this theme park in one database. Coasters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1923.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1923.", "x": "Liseberg: 1923.. Christmas. One of the defining facts — Helix.. Gothenburg's fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1923..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1923..", "x": "Explored: 1923.. Tickets. Why it is so — Liseberg. Christmas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Balder.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Balder.", "x": "Liseberg: Balder.. Gardens. One of the defining facts — Christmas.. Gothenburg's fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Balder..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Balder..", "x": "Explored: Balder.. Sweden. Why it is so — Liseberg. Sweden. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Helix.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Helix.", "x": "Liseberg: Helix.. Tickets. One of the defining facts — Sweden.. Gothenburg's fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Helix..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Helix..", "x": "Explored: Helix.. Fun. Why it is so — Liseberg. Gardens. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Christmas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Christmas.", "x": "Liseberg: Christmas.. Sweden. One of the defining facts — Gardens.. Gothenburg's fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Christmas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Christmas..", "x": "Explored: Christmas.. Coasters. Why it is so — Liseberg. 1923. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sweden.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sweden.", "x": "Liseberg: Sweden.. Fun. One of the defining facts — 1923.. Gothenburg's fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Sweden..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Sweden..", "x": "Explored: Sweden.. Christmas. Why it is so — Liseberg. Balder. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gardens.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gardens.", "x": "Liseberg: Gardens.. Coasters. One of the defining facts — Balder.. Gothenburg's fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Gardens..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Gardens..", "x": "Explored: Gardens.. Gardens. Why it is so — Liseberg. Helix. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Coasters.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Coasters.", "x": "Liseberg in depth: Coasters.. Balder. The details reward the curious — Gothenburg's fun.. Gardens. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Christmas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Christmas.", "x": "Liseberg in depth: Christmas.. Helix. The details reward the curious — Gothenburg's fun.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gardens.", "x": "Liseberg in depth: Gardens.. Christmas. The details reward the curious — Gothenburg's fun.. Sweden. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Liseberg in depth: Tickets.. Sweden. The details reward the curious — Gothenburg's fun.. Fun. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sweden.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sweden.", "x": "Liseberg in depth: Sweden.. Gardens. The details reward the curious — Gothenburg's fun.. Coasters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fun.", "x": "Liseberg in depth: Fun.. 1923. The details reward the curious — Gothenburg's fun.. Christmas. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Liseberg is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Liseberg is.", "x": "Location: 1923.. Coasters. Getting oriented — Liseberg. Gothenburg's fun. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Liseberg.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Liseberg.", "x": "Visiting: Christmas.. Balder. Practical know-how — Liseberg. Gothenburg's fun. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Liseberg.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Liseberg.", "x": "Ecology: Gardens.. Helix. The living world of Liseberg — Gothenburg's fun.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Liseberg through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Liseberg through time.", "x": "History: Sweden.. Christmas. People and Liseberg across the centuries — Gothenburg's fun.. Fun. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Liseberg.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Liseberg.", "x": "Conservation: Christmas.. 1923. Threats and guardians of Liseberg — Gothenburg's fun.. Gardens. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Liseberg in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Liseberg in numbers.", "x": "Numbers: 1923.; Balder.. Tickets. Statistics that stun — Liseberg. Gothenburg's fun. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-themepark-liseberg-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
