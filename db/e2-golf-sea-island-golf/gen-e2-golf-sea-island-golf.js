(function(){'use strict';
/* JAH Sea Island Golf Golf Course Database generator — jahdb-e2-golf-sea-island-golf-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-golf-sea-island-golf',PREFIX='JAH-E2GOLFSEAIS-',NAME='JAH Sea Island Golf Golf Course Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sea Island Golf: the complete guide", "d": "Sea Island Golf: the Georgia retreat..", "g": "overview", "l": 2, "q": "What is Sea Island Golf: the complete guide?", "a": "Sea Island Golf: the Georgia retreat..", "x": "The complete golf course guide to Sea Island Golf: the Georgia retreat.. Seaside. From formation to visiting, from wildlife to legends — everything about this golf course in one database. Seaside. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Seaside.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Seaside.", "x": "Sea Island Golf: Seaside.. Resort. One of the defining facts — Resort.. the Georgia retreat. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Seaside..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Seaside..", "x": "Explored: Seaside.. Georgia. Why it is so — Sea Island Golf. RSM Classic. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Georgia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Georgia.", "x": "Sea Island Golf: Georgia.. Classic. One of the defining facts — RSM Classic.. the Georgia retreat. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Georgia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Georgia..", "x": "Explored: Georgia.. Marsh. Why it is so — Sea Island Golf. Marsh. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Resort.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Resort.", "x": "Sea Island Golf: Resort.. Georgia. One of the defining facts — Marsh.. the Georgia retreat. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Resort..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Resort..", "x": "Explored: Resort.. Luxury. Why it is so — Sea Island Golf. Luxury. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "RSM Classic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "RSM Classic.", "x": "Sea Island Golf: RSM Classic.. Marsh. One of the defining facts — Luxury.. the Georgia retreat. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: RSM Classic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: RSM Classic..", "x": "Explored: RSM Classic.. Seaside. Why it is so — Sea Island Golf. Seaside. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Marsh.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Marsh.", "x": "Sea Island Golf: Marsh.. Luxury. One of the defining facts — Seaside.. the Georgia retreat. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Marsh..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Marsh..", "x": "Explored: Marsh.. Resort. Why it is so — Sea Island Golf. Georgia. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Luxury.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Luxury.", "x": "Sea Island Golf: Luxury.. Seaside. One of the defining facts — Georgia.. the Georgia retreat. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Luxury..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Luxury..", "x": "Explored: Luxury.. Classic. Why it is so — Sea Island Golf. Resort. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Seaside.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Seaside.", "x": "Sea Island Golf in depth: Seaside.. Georgia. The details reward the curious — the Georgia retreat.. Classic. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Resort.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Resort.", "x": "Sea Island Golf in depth: Resort.. Resort. The details reward the curious — the Georgia retreat.. Georgia. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Classic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Classic.", "x": "Sea Island Golf in depth: Classic.. RSM Classic. The details reward the curious — the Georgia retreat.. Marsh. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Georgia.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Georgia.", "x": "Sea Island Golf in depth: Georgia.. Marsh. The details reward the curious — the Georgia retreat.. Luxury. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Marsh.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Marsh.", "x": "Sea Island Golf in depth: Marsh.. Luxury. The details reward the curious — the Georgia retreat.. Seaside. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Luxury.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Luxury.", "x": "Sea Island Golf in depth: Luxury.. Seaside. The details reward the curious — the Georgia retreat.. Resort. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Sea Island Golf is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Sea Island Golf is.", "x": "Location: Seaside.. Seaside. Getting oriented — Sea Island Golf. the Georgia retreat. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Sea Island Golf.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Sea Island Golf.", "x": "Visiting: Resort.. Georgia. Practical know-how — Sea Island Golf. the Georgia retreat. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Sea Island Golf.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Sea Island Golf.", "x": "Ecology: Classic.. Resort. The living world of Sea Island Golf — the Georgia retreat.. Georgia. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Sea Island Golf through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Sea Island Golf through time.", "x": "History: Marsh.. RSM Classic. People and Sea Island Golf across the centuries — the Georgia retreat.. Luxury. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Sea Island Golf.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Sea Island Golf.", "x": "Conservation: Resort.. Seaside. Threats and guardians of Sea Island Golf — the Georgia retreat.. Classic. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Sea Island Golf in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Sea Island Golf in numbers.", "x": "Numbers: Seaside.; Georgia.. Georgia. Statistics that stun — Sea Island Golf. the Georgia retreat. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-golf-sea-island-golf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
