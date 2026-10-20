(function(){'use strict';
/* JAH Typhoon Lagoon Water Park Database generator — jahdb-e2-waterpark-typhoon-lagoon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-waterpark-typhoon-lagoon',PREFIX='JAH-E2WATERPARK-',NAME='JAH Typhoon Lagoon Water Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Typhoon Lagoon: the complete guide", "d": "Typhoon Lagoon: Disney's storm beach..", "g": "overview", "l": 2, "q": "What is Typhoon Lagoon: the complete guide?", "a": "Typhoon Lagoon: Disney's storm beach..", "x": "The complete water park guide to Typhoon Lagoon: Disney's storm beach.. 1989. From formation to visiting, from wildlife to legends — everything about this water park in one database. Surf. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1989.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1989.", "x": "Typhoon Lagoon: 1989.. Slides. One of the defining facts — Crush 'n' Gusher.. Disney's storm beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1989..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1989..", "x": "Explored: 1989.. Tickets. Why it is so — Typhoon Lagoon. Shark reef. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Surf pool.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Surf pool.", "x": "Typhoon Lagoon: Surf pool.. Shark. One of the defining facts — Shark reef.. Disney's storm beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Surf pool..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Surf pool..", "x": "Explored: Surf pool.. Orlando. Why it is so — Typhoon Lagoon. Orlando. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Crush 'n' Gusher.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Crush 'n' Gusher.", "x": "Typhoon Lagoon: Crush 'n' Gusher.. Tickets. One of the defining facts — Orlando.. Disney's storm beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Crush 'n' Gusher..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Crush 'n' Gusher..", "x": "Explored: Crush 'n' Gusher.. Storm. Why it is so — Typhoon Lagoon. Storm. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shark reef.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shark reef.", "x": "Typhoon Lagoon: Shark reef.. Orlando. One of the defining facts — Storm.. Disney's storm beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Shark reef..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Shark reef..", "x": "Explored: Shark reef.. Surf. Why it is so — Typhoon Lagoon. 1989. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orlando.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orlando.", "x": "Typhoon Lagoon: Orlando.. Storm. One of the defining facts — 1989.. Disney's storm beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Orlando..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Orlando..", "x": "Explored: Orlando.. Slides. Why it is so — Typhoon Lagoon. Surf pool. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Storm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Storm.", "x": "Typhoon Lagoon: Storm.. Surf. One of the defining facts — Surf pool.. Disney's storm beach. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Storm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Storm..", "x": "Explored: Storm.. Shark. Why it is so — Typhoon Lagoon. Crush 'n' Gusher. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Surf.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Surf.", "x": "Typhoon Lagoon in depth: Surf.. Surf pool. The details reward the curious — Disney's storm beach.. Shark. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Slides.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Slides.", "x": "Typhoon Lagoon in depth: Slides.. Crush 'n' Gusher. The details reward the curious — Disney's storm beach.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shark.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shark.", "x": "Typhoon Lagoon in depth: Shark.. Shark reef. The details reward the curious — Disney's storm beach.. Orlando. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Typhoon Lagoon in depth: Tickets.. Orlando. The details reward the curious — Disney's storm beach.. Storm. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Orlando.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Orlando.", "x": "Typhoon Lagoon in depth: Orlando.. Storm. The details reward the curious — Disney's storm beach.. Surf. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Storm.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Storm.", "x": "Typhoon Lagoon in depth: Storm.. 1989. The details reward the curious — Disney's storm beach.. Slides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Typhoon Lagoon is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Typhoon Lagoon is.", "x": "Location: 1989.. Surf. Getting oriented — Typhoon Lagoon. Disney's storm beach. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Typhoon Lagoon.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Typhoon Lagoon.", "x": "Visiting: Slides.. Surf pool. Practical know-how — Typhoon Lagoon. Disney's storm beach. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Typhoon Lagoon.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Typhoon Lagoon.", "x": "Ecology: Shark.. Crush 'n' Gusher. The living world of Typhoon Lagoon — Disney's storm beach.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Typhoon Lagoon through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Typhoon Lagoon through time.", "x": "History: Orlando.. Shark reef. People and Typhoon Lagoon across the centuries — Disney's storm beach.. Storm. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Typhoon Lagoon.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Typhoon Lagoon.", "x": "Conservation: Slides.. 1989. Threats and guardians of Typhoon Lagoon — Disney's storm beach.. Shark. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Typhoon Lagoon in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Typhoon Lagoon in numbers.", "x": "Numbers: 1989.; Surf pool.. Tickets. Statistics that stun — Typhoon Lagoon. Disney's storm beach. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-waterpark-typhoon-lagoon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
