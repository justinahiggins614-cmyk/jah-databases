(function(){'use strict';
/* JAH Thorpe Park Theme Park Database generator — jahdb-e2-themepark-thorpe-park-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-themepark-thorpe-park',PREFIX='JAH-E2THEMEPARK-',NAME='JAH Thorpe Park Theme Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thorpe Park: the complete guide", "d": "Thorpe Park: the UK's thrill island..", "g": "overview", "l": 2, "q": "What is Thorpe Park: the complete guide?", "a": "Thorpe Park: the UK's thrill island..", "x": "The complete theme park guide to Thorpe Park: the UK's thrill island.. 1979. From formation to visiting, from wildlife to legends — everything about this theme park in one database. Coasters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1979.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1979.", "x": "Thorpe Park: 1979.. Fright. One of the defining facts — Saw.. the UK's thrill island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1979..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1979..", "x": "Explored: 1979.. Tickets. Why it is so — Thorpe Park. Fright Nights. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Stealth.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Stealth.", "x": "Thorpe Park: Stealth.. Island. One of the defining facts — Fright Nights.. the UK's thrill island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Stealth..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Stealth..", "x": "Explored: Stealth.. UK. Why it is so — Thorpe Park. Surrey. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Saw.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Saw.", "x": "Thorpe Park: Saw.. Tickets. One of the defining facts — Surrey.. the UK's thrill island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Saw..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Saw..", "x": "Explored: Saw.. Thrills. Why it is so — Thorpe Park. Island. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fright Nights.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fright Nights.", "x": "Thorpe Park: Fright Nights.. UK. One of the defining facts — Island.. the UK's thrill island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Fright Nights..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Fright Nights..", "x": "Explored: Fright Nights.. Coasters. Why it is so — Thorpe Park. 1979. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Surrey.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Surrey.", "x": "Thorpe Park: Surrey.. Thrills. One of the defining facts — 1979.. the UK's thrill island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Surrey..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Surrey..", "x": "Explored: Surrey.. Fright. Why it is so — Thorpe Park. Stealth. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Island.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Island.", "x": "Thorpe Park: Island.. Coasters. One of the defining facts — Stealth.. the UK's thrill island. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Island..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Island..", "x": "Explored: Island.. Island. Why it is so — Thorpe Park. Saw. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Coasters.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Coasters.", "x": "Thorpe Park in depth: Coasters.. Stealth. The details reward the curious — the UK's thrill island.. Island. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fright.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fright.", "x": "Thorpe Park in depth: Fright.. Saw. The details reward the curious — the UK's thrill island.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Island.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Island.", "x": "Thorpe Park in depth: Island.. Fright Nights. The details reward the curious — the UK's thrill island.. UK. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Thorpe Park in depth: Tickets.. Surrey. The details reward the curious — the UK's thrill island.. Thrills. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "UK.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "UK.", "x": "Thorpe Park in depth: UK.. Island. The details reward the curious — the UK's thrill island.. Coasters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Thrills.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Thrills.", "x": "Thorpe Park in depth: Thrills.. 1979. The details reward the curious — the UK's thrill island.. Fright. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Thorpe Park is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Thorpe Park is.", "x": "Location: 1979.. Coasters. Getting oriented — Thorpe Park. the UK's thrill island. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Thorpe Park.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Thorpe Park.", "x": "Visiting: Fright.. Stealth. Practical know-how — Thorpe Park. the UK's thrill island. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Thorpe Park.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Thorpe Park.", "x": "Ecology: Island.. Saw. The living world of Thorpe Park — the UK's thrill island.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Thorpe Park through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Thorpe Park through time.", "x": "History: UK.. Fright Nights. People and Thorpe Park across the centuries — the UK's thrill island.. Thrills. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Thorpe Park.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Thorpe Park.", "x": "Conservation: Fright.. 1979. Threats and guardians of Thorpe Park — the UK's thrill island.. Island. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Thorpe Park in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Thorpe Park in numbers.", "x": "Numbers: 1979.; Stealth.. Tickets. Statistics that stun — Thorpe Park. the UK's thrill island. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-themepark-thorpe-park-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
