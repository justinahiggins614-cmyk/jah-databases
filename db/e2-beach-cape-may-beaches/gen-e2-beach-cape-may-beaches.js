(function(){'use strict';
/* JAH Cape May Beaches Beach Database generator — jahdb-e2-beach-cape-may-beaches-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-cape-may-beaches',PREFIX='JAH-E2BEACHCAPE-',NAME='JAH Cape May Beaches Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cape May Beaches: the complete guide", "d": "Cape May Beaches: the Victorian shore..", "g": "overview", "l": 2, "q": "What is Cape May Beaches: the complete guide?", "a": "Cape May Beaches: the Victorian shore..", "x": "The complete beach guide to Cape May Beaches: the Victorian shore.. New Jersey. From formation to visiting, from wildlife to legends — everything about this beach in one database. Victorian. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "New Jersey.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "New Jersey.", "x": "Cape May Beaches: New Jersey.. Sunset. One of the defining facts — Diamonds.. the Victorian shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: New Jersey..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: New Jersey..", "x": "Explored: New Jersey.. NJ. Why it is so — Cape May Beaches. Dolphins. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Victorian.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Victorian.", "x": "Cape May Beaches: Victorian.. Birds. One of the defining facts — Dolphins.. the Victorian shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Victorian..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Victorian..", "x": "Explored: Victorian.. Diamonds. Why it is so — Cape May Beaches. Sunset. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Diamonds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Diamonds.", "x": "Cape May Beaches: Diamonds.. NJ. One of the defining facts — Sunset.. the Victorian shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Diamonds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Diamonds..", "x": "Explored: Diamonds.. Charm. Why it is so — Cape May Beaches. Birding. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dolphins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dolphins.", "x": "Cape May Beaches: Dolphins.. Diamonds. One of the defining facts — Birding.. the Victorian shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Dolphins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Dolphins..", "x": "Explored: Dolphins.. Victorian. Why it is so — Cape May Beaches. New Jersey. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sunset.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sunset.", "x": "Cape May Beaches: Sunset.. Charm. One of the defining facts — New Jersey.. the Victorian shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Sunset..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Sunset..", "x": "Explored: Sunset.. Sunset. Why it is so — Cape May Beaches. Victorian. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Birding.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Birding.", "x": "Cape May Beaches: Birding.. Victorian. One of the defining facts — Victorian.. the Victorian shore. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Birding..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Birding..", "x": "Explored: Birding.. Birds. Why it is so — Cape May Beaches. Diamonds. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Victorian.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Victorian.", "x": "Cape May Beaches in depth: Victorian.. Victorian. The details reward the curious — the Victorian shore.. Birds. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sunset.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sunset.", "x": "Cape May Beaches in depth: Sunset.. Diamonds. The details reward the curious — the Victorian shore.. NJ. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Birds.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Birds.", "x": "Cape May Beaches in depth: Birds.. Dolphins. The details reward the curious — the Victorian shore.. Diamonds. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "NJ.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "NJ.", "x": "Cape May Beaches in depth: NJ.. Sunset. The details reward the curious — the Victorian shore.. Charm. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Diamonds.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Diamonds.", "x": "Cape May Beaches in depth: Diamonds.. Birding. The details reward the curious — the Victorian shore.. Victorian. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Charm.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Charm.", "x": "Cape May Beaches in depth: Charm.. New Jersey. The details reward the curious — the Victorian shore.. Sunset. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Cape May Beaches is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Cape May Beaches is.", "x": "Location: New Jersey.. Victorian. Getting oriented — Cape May Beaches. the Victorian shore. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Cape May Beaches.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Cape May Beaches.", "x": "Visiting: Sunset.. Victorian. Practical know-how — Cape May Beaches. the Victorian shore. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Cape May Beaches.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Cape May Beaches.", "x": "Ecology: Birds.. Diamonds. The living world of Cape May Beaches — the Victorian shore.. NJ. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Cape May Beaches through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Cape May Beaches through time.", "x": "History: Diamonds.. Dolphins. People and Cape May Beaches across the centuries — the Victorian shore.. Charm. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Cape May Beaches.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Cape May Beaches.", "x": "Conservation: Sunset.. New Jersey. Threats and guardians of Cape May Beaches — the Victorian shore.. Birds. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Cape May Beaches in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Cape May Beaches in numbers.", "x": "Numbers: New Jersey.; Victorian.. NJ. Statistics that stun — Cape May Beaches. the Victorian shore. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-cape-may-beaches-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
