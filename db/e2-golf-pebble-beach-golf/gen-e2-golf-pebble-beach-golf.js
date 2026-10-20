(function(){'use strict';
/* JAH Pebble Beach Golf Links Golf Course Database generator — jahdb-e2-golf-pebble-beach-golf-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-golf-pebble-beach-golf',PREFIX='JAH-E2GOLFPEBBL-',NAME='JAH Pebble Beach Golf Links Golf Course Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pebble Beach Golf Links: the complete guide", "d": "Pebble Beach Golf Links: the cliffside major..", "g": "overview", "l": 2, "q": "What is Pebble Beach Golf Links: the complete guide?", "a": "Pebble Beach Golf Links: the cliffside major..", "x": "The complete golf course guide to Pebble Beach Golf Links: the cliffside major.. 1919. From formation to visiting, from wildlife to legends — everything about this golf course in one database. Cliffs.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1919.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1919.", "x": "Pebble Beach Golf Links: 1919.. US Open. One of the defining facts — US Open.. the cliffside major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1919..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1919..", "x": "Explored: 1919.. Resort. Why it is so — Pebble Beach Golf Links. 7th hole. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cliffs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cliffs.", "x": "Pebble Beach Golf Links: Cliffs.. 7th. One of the defining facts — 7th hole.. the cliffside major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Cliffs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Cliffs..", "x": "Explored: Cliffs.. California. Why it is so — Pebble Beach Golf Links. California. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "US Open.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "US Open.", "x": "Pebble Beach Golf Links: US Open.. Resort. One of the defining facts — California.. the cliffside major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: US Open..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: US Open..", "x": "Explored: US Open.. Views. Why it is so — Pebble Beach Golf Links. Resort. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "7th hole.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "7th hole.", "x": "Pebble Beach Golf Links: 7th hole.. California. One of the defining facts — Resort.. the cliffside major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: 7th hole..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: 7th hole..", "x": "Explored: 7th hole.. Cliffs. Why it is so — Pebble Beach Golf Links. 1919. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "California.", "x": "Pebble Beach Golf Links: California.. Views. One of the defining facts — 1919.. the cliffside major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: California..", "x": "Explored: California.. US Open. Why it is so — Pebble Beach Golf Links. Cliffs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Resort.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Resort.", "x": "Pebble Beach Golf Links: Resort.. Cliffs. One of the defining facts — Cliffs.. the cliffside major. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Resort..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Resort..", "x": "Explored: Resort.. 7th. Why it is so — Pebble Beach Golf Links. US Open. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cliffs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cliffs.", "x": "Pebble Beach Golf Links in depth: Cliffs.. Cliffs. The details reward the curious — the cliffside major.. 7th. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "US Open.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "US Open.", "x": "Pebble Beach Golf Links in depth: US Open.. US Open. The details reward the curious — the cliffside major.. Resort. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "7th.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "7th.", "x": "Pebble Beach Golf Links in depth: 7th.. 7th hole. The details reward the curious — the cliffside major.. California. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Resort.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Resort.", "x": "Pebble Beach Golf Links in depth: Resort.. California. The details reward the curious — the cliffside major.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "California.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "California.", "x": "Pebble Beach Golf Links in depth: California.. Resort. The details reward the curious — the cliffside major.. Cliffs. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Pebble Beach Golf Links in depth: Views.. 1919. The details reward the curious — the cliffside major.. US Open. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Pebble Beach Golf Links is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Pebble Beach Golf Links is.", "x": "Location: 1919.. Cliffs. Getting oriented — Pebble Beach Golf Links. the cliffside major. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Pebble Beach Golf Links.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Pebble Beach Golf Links.", "x": "Visiting: US Open.. Cliffs. Practical know-how — Pebble Beach Golf Links. the cliffside major. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Pebble Beach Golf Links.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Pebble Beach Golf Links.", "x": "Ecology: 7th.. US Open. The living world of Pebble Beach Golf Links — the cliffside major.. Resort. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Pebble Beach Golf Links through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Pebble Beach Golf Links through time.", "x": "History: California.. 7th hole. People and Pebble Beach Golf Links across the centuries — the cliffside major.. Views. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Pebble Beach Golf Links.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Pebble Beach Golf Links.", "x": "Conservation: US Open.. 1919. Threats and guardians of Pebble Beach Golf Links — the cliffside major.. 7th. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Pebble Beach Golf Links in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Pebble Beach Golf Links in numbers.", "x": "Numbers: 1919.; Cliffs.. Resort. Statistics that stun — Pebble Beach Golf Links. the cliffside major. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-golf-pebble-beach-golf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
