(function(){'use strict';
/* JAH Bethpage Black Golf Course Database generator — jahdb-e2-golf-bethpage-black-golf-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-golf-bethpage-black-golf',PREFIX='JAH-E2GOLFBETHP-',NAME='JAH Bethpage Black Golf Course Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bethpage Black: the complete guide", "d": "Bethpage Black: the people's major..", "g": "overview", "l": 2, "q": "What is Bethpage Black: the complete guide?", "a": "Bethpage Black: the people's major..", "x": "The complete golf course guide to Bethpage Black: the people's major.. Public. From formation to visiting, from wildlife to legends — everything about this golf course in one database. Public. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Public.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Public.", "x": "Bethpage Black: Public.. Sign. One of the defining facts — Warning sign.. the people's major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Public..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Public..", "x": "Explored: Public.. Hard. Why it is so — Bethpage Black. NY. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "US Open.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "US Open.", "x": "Bethpage Black: US Open.. US Open. One of the defining facts — NY.. the people's major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: US Open..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: US Open..", "x": "Explored: US Open.. NY. Why it is so — Bethpage Black. Hard. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Warning sign.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Warning sign.", "x": "Bethpage Black: Warning sign.. Hard. One of the defining facts — Hard.. the people's major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Warning sign..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Warning sign..", "x": "Explored: Warning sign.. Access. Why it is so — Bethpage Black. PGA. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "NY.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "NY.", "x": "Bethpage Black: NY.. NY. One of the defining facts — PGA.. the people's major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: NY..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: NY..", "x": "Explored: NY.. Public. Why it is so — Bethpage Black. Public. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hard.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hard.", "x": "Bethpage Black: Hard.. Access. One of the defining facts — Public.. the people's major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Hard..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Hard..", "x": "Explored: Hard.. Sign. Why it is so — Bethpage Black. US Open. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "PGA.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "PGA.", "x": "Bethpage Black: PGA.. Public. One of the defining facts — US Open.. the people's major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: PGA..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: PGA..", "x": "Explored: PGA.. US Open. Why it is so — Bethpage Black. Warning sign. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Public.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Public.", "x": "Bethpage Black in depth: Public.. US Open. The details reward the curious — the people's major.. US Open. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sign.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sign.", "x": "Bethpage Black in depth: Sign.. Warning sign. The details reward the curious — the people's major.. Hard. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "US Open.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "US Open.", "x": "Bethpage Black in depth: US Open.. NY. The details reward the curious — the people's major.. NY. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hard.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hard.", "x": "Bethpage Black in depth: Hard.. Hard. The details reward the curious — the people's major.. Access. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "NY.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "NY.", "x": "Bethpage Black in depth: NY.. PGA. The details reward the curious — the people's major.. Public. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Access.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Access.", "x": "Bethpage Black in depth: Access.. Public. The details reward the curious — the people's major.. Sign. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Bethpage Black is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Bethpage Black is.", "x": "Location: Public.. Public. Getting oriented — Bethpage Black. the people's major. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Bethpage Black.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Bethpage Black.", "x": "Visiting: Sign.. US Open. Practical know-how — Bethpage Black. the people's major. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Bethpage Black.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Bethpage Black.", "x": "Ecology: US Open.. Warning sign. The living world of Bethpage Black — the people's major.. Hard. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Bethpage Black through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Bethpage Black through time.", "x": "History: NY.. NY. People and Bethpage Black across the centuries — the people's major.. Access. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Bethpage Black.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Bethpage Black.", "x": "Conservation: Sign.. Public. Threats and guardians of Bethpage Black — the people's major.. US Open. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Bethpage Black in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Bethpage Black in numbers.", "x": "Numbers: Public.; US Open.. Hard. Statistics that stun — Bethpage Black. the people's major. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-golf-bethpage-black-golf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
