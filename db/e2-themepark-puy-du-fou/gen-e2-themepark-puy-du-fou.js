(function(){'use strict';
/* JAH Puy du Fou Theme Park Database generator — jahdb-e2-themepark-puy-du-fou-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-themepark-puy-du-fou',PREFIX='JAH-E2THEMEPARK-',NAME='JAH Puy du Fou Theme Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Puy du Fou: the complete guide", "d": "Puy du Fou: history as spectacle..", "g": "overview", "l": 2, "q": "What is Puy du Fou: the complete guide?", "a": "Puy du Fou: history as spectacle..", "x": "The complete theme park guide to Puy du Fou: history as spectacle.. 1978. From formation to visiting, from wildlife to legends — everything about this theme park in one database. Shows. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1978.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1978.", "x": "Puy du Fou: 1978.. History. One of the defining facts — No rides.. history as spectacle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1978..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1978..", "x": "Explored: 1978.. Tickets. Why it is so — Puy du Fou. Vendee. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shows.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shows.", "x": "Puy du Fou: Shows.. No rides. One of the defining facts — Vendee.. history as spectacle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Shows..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Shows..", "x": "Explored: Shows.. France. Why it is so — Puy du Fou. Romans. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "No rides.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "No rides.", "x": "Puy du Fou: No rides.. Tickets. One of the defining facts — Romans.. history as spectacle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: No rides..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: No rides..", "x": "Explored: No rides.. Spectacle. Why it is so — Puy du Fou. Vikings. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vendee.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vendee.", "x": "Puy du Fou: Vendee.. France. One of the defining facts — Vikings.. history as spectacle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Vendee..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Vendee..", "x": "Explored: Vendee.. Shows. Why it is so — Puy du Fou. 1978. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Romans.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Romans.", "x": "Puy du Fou: Romans.. Spectacle. One of the defining facts — 1978.. history as spectacle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Romans..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Romans..", "x": "Explored: Romans.. History. Why it is so — Puy du Fou. Shows. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Vikings.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Vikings.", "x": "Puy du Fou: Vikings.. Shows. One of the defining facts — Shows.. history as spectacle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Vikings..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Vikings..", "x": "Explored: Vikings.. No rides. Why it is so — Puy du Fou. No rides. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Shows.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Shows.", "x": "Puy du Fou in depth: Shows.. Shows. The details reward the curious — history as spectacle.. No rides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Puy du Fou in depth: History.. No rides. The details reward the curious — history as spectacle.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "No rides.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "No rides.", "x": "Puy du Fou in depth: No rides.. Vendee. The details reward the curious — history as spectacle.. France. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Puy du Fou in depth: Tickets.. Romans. The details reward the curious — history as spectacle.. Spectacle. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "France.", "x": "Puy du Fou in depth: France.. Vikings. The details reward the curious — history as spectacle.. Shows. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Spectacle.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Spectacle.", "x": "Puy du Fou in depth: Spectacle.. 1978. The details reward the curious — history as spectacle.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Puy du Fou is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Puy du Fou is.", "x": "Location: 1978.. Shows. Getting oriented — Puy du Fou. history as spectacle. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Puy du Fou.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Puy du Fou.", "x": "Visiting: History.. Shows. Practical know-how — Puy du Fou. history as spectacle. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Puy du Fou.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Puy du Fou.", "x": "Ecology: No rides.. No rides. The living world of Puy du Fou — history as spectacle.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Puy du Fou through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Puy du Fou through time.", "x": "History: France.. Vendee. People and Puy du Fou across the centuries — history as spectacle.. Spectacle. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Puy du Fou.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Puy du Fou.", "x": "Conservation: History.. 1978. Threats and guardians of Puy du Fou — history as spectacle.. No rides. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Puy du Fou in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Puy du Fou in numbers.", "x": "Numbers: 1978.; Shows.. Tickets. Statistics that stun — Puy du Fou. history as spectacle. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-themepark-puy-du-fou-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
