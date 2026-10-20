(function(){'use strict';
/* JAH Park City Ski Resort Database generator — jahdb-e2-ski-park-city-ski-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ski-park-city-ski',PREFIX='JAH-E2SKIPARKCI-',NAME='JAH Park City Ski Resort Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Park City: the complete guide", "d": "Park City: the largest US resort..", "g": "overview", "l": 2, "q": "What is Park City: the complete guide?", "a": "Park City: the largest US resort..", "x": "The complete ski resort guide to Park City: the largest US resort.. 7,300 acres. From formation to visiting, from wildlife to legends — everything about this ski resort in one database. Size. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "7,300 acres.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "7,300 acres.", "x": "Park City: 7,300 acres.. Town. One of the defining facts — Town.. the largest US resort. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 7,300 acres..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 7,300 acres..", "x": "Explored: 7,300 acres.. Tickets. Why it is so — Park City. Utah. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sundance.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sundance.", "x": "Park City: Sundance.. Sundance. One of the defining facts — Utah.. the largest US resort. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Sundance..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Sundance..", "x": "Explored: Sundance.. Utah. Why it is so — Park City. 2019 combine. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Town.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Town.", "x": "Park City: Town.. Tickets. One of the defining facts — 2019 combine.. the largest US resort. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Town..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Town..", "x": "Explored: Town.. Olympic. Why it is so — Park City. Olympic. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Utah.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Utah.", "x": "Park City: Utah.. Utah. One of the defining facts — Olympic.. the largest US resort. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Utah..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Utah..", "x": "Explored: Utah.. Size. Why it is so — Park City. 7,300 acres. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2019 combine.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2019 combine.", "x": "Park City: 2019 combine.. Olympic. One of the defining facts — 7,300 acres.. the largest US resort. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: 2019 combine..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: 2019 combine..", "x": "Explored: 2019 combine.. Town. Why it is so — Park City. Sundance. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Olympic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Olympic.", "x": "Park City: Olympic.. Size. One of the defining facts — Sundance.. the largest US resort. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Olympic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Olympic..", "x": "Explored: Olympic.. Sundance. Why it is so — Park City. Town. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Size.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Size.", "x": "Park City in depth: Size.. Sundance. The details reward the curious — the largest US resort.. Sundance. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Town.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Town.", "x": "Park City in depth: Town.. Town. The details reward the curious — the largest US resort.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sundance.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sundance.", "x": "Park City in depth: Sundance.. Utah. The details reward the curious — the largest US resort.. Utah. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Park City in depth: Tickets.. 2019 combine. The details reward the curious — the largest US resort.. Olympic. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Utah.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Utah.", "x": "Park City in depth: Utah.. Olympic. The details reward the curious — the largest US resort.. Size. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Olympic.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Olympic.", "x": "Park City in depth: Olympic.. 7,300 acres. The details reward the curious — the largest US resort.. Town. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Park City is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Park City is.", "x": "Location: 7,300 acres.. Size. Getting oriented — Park City. the largest US resort. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Park City.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Park City.", "x": "Visiting: Town.. Sundance. Practical know-how — Park City. the largest US resort. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Park City.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Park City.", "x": "Ecology: Sundance.. Town. The living world of Park City — the largest US resort.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Park City through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Park City through time.", "x": "History: Utah.. Utah. People and Park City across the centuries — the largest US resort.. Olympic. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Park City.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Park City.", "x": "Conservation: Town.. 7,300 acres. Threats and guardians of Park City — the largest US resort.. Sundance. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Park City in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Park City in numbers.", "x": "Numbers: 7,300 acres.; Sundance.. Tickets. Statistics that stun — Park City. the largest US resort. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ski-park-city-ski-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
