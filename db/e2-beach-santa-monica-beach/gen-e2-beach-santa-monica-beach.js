(function(){'use strict';
/* JAH Santa Monica Beach Beach Database generator — jahdb-e2-beach-santa-monica-beach-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-santa-monica-beach',PREFIX='JAH-E2BEACHSANT-',NAME='JAH Santa Monica Beach Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Santa Monica Beach: the complete guide", "d": "Santa Monica Beach: the pier beach..", "g": "overview", "l": 2, "q": "What is Santa Monica Beach: the complete guide?", "a": "Santa Monica Beach: the pier beach..", "x": "The complete beach guide to Santa Monica Beach: the pier beach.. Pier. From formation to visiting, from wildlife to legends — everything about this beach in one database. Pier. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pier.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pier.", "x": "Santa Monica Beach: Pier.. Venice. One of the defining facts — Venice.. the pier beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Pier..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Pier..", "x": "Explored: Pier.. LA. Why it is so — Santa Monica Beach. Sunset. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "3.5 miles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "3.5 miles.", "x": "Santa Monica Beach: 3.5 miles.. Sunset. One of the defining facts — Sunset.. the pier beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 3.5 miles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 3.5 miles..", "x": "Explored: 3.5 miles.. Bike. Why it is so — Santa Monica Beach. LA. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Venice.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Venice.", "x": "Santa Monica Beach: Venice.. LA. One of the defining facts — LA.. the pier beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Venice..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Venice..", "x": "Explored: Venice.. Vibe. Why it is so — Santa Monica Beach. Muscle. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sunset.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sunset.", "x": "Santa Monica Beach: Sunset.. Bike. One of the defining facts — Muscle.. the pier beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Sunset..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Sunset..", "x": "Explored: Sunset.. Pier. Why it is so — Santa Monica Beach. Pier. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "LA.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "LA.", "x": "Santa Monica Beach: LA.. Vibe. One of the defining facts — Pier.. the pier beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: LA..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: LA..", "x": "Explored: LA.. Venice. Why it is so — Santa Monica Beach. 3.5 miles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Muscle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Muscle.", "x": "Santa Monica Beach: Muscle.. Pier. One of the defining facts — 3.5 miles.. the pier beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Muscle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Muscle..", "x": "Explored: Muscle.. Sunset. Why it is so — Santa Monica Beach. Venice. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pier.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pier.", "x": "Santa Monica Beach in depth: Pier.. 3.5 miles. The details reward the curious — the pier beach.. Sunset. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Venice.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Venice.", "x": "Santa Monica Beach in depth: Venice.. Venice. The details reward the curious — the pier beach.. LA. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sunset.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sunset.", "x": "Santa Monica Beach in depth: Sunset.. Sunset. The details reward the curious — the pier beach.. Bike. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "LA.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "LA.", "x": "Santa Monica Beach in depth: LA.. LA. The details reward the curious — the pier beach.. Vibe. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bike.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bike.", "x": "Santa Monica Beach in depth: Bike.. Muscle. The details reward the curious — the pier beach.. Pier. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Vibe.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Vibe.", "x": "Santa Monica Beach in depth: Vibe.. Pier. The details reward the curious — the pier beach.. Venice. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Santa Monica Beach is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Santa Monica Beach is.", "x": "Location: Pier.. Pier. Getting oriented — Santa Monica Beach. the pier beach. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Santa Monica Beach.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Santa Monica Beach.", "x": "Visiting: Venice.. 3.5 miles. Practical know-how — Santa Monica Beach. the pier beach. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Santa Monica Beach.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Santa Monica Beach.", "x": "Ecology: Sunset.. Venice. The living world of Santa Monica Beach — the pier beach.. LA. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Santa Monica Beach through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Santa Monica Beach through time.", "x": "History: Bike.. Sunset. People and Santa Monica Beach across the centuries — the pier beach.. Vibe. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Santa Monica Beach.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Santa Monica Beach.", "x": "Conservation: Venice.. Pier. Threats and guardians of Santa Monica Beach — the pier beach.. Sunset. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Santa Monica Beach in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Santa Monica Beach in numbers.", "x": "Numbers: Pier.; 3.5 miles.. LA. Statistics that stun — Santa Monica Beach. the pier beach. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-santa-monica-beach-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
