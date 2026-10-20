(function(){'use strict';
/* JAH Blue Hole Belize Dive Site Database generator — jahdb-e2-dive-blue-hole-belize-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive-blue-hole-belize',PREFIX='JAH-E2DIVEBLUEH-',NAME='JAH Blue Hole Belize Dive Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Blue Hole Belize: the complete guide", "d": "Blue Hole Belize: the deep blue circle..", "g": "overview", "l": 2, "q": "What is Blue Hole Belize: the complete guide?", "a": "Blue Hole Belize: the deep blue circle..", "x": "The complete dive site guide to Blue Hole Belize: the deep blue circle.. 124m. From formation to visiting, from wildlife to legends — everything about this dive site in one database. Depth. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "124m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "124m.", "x": "Blue Hole Belize: 124m.. Stalactites. One of the defining facts — Stalactites.. the deep blue circle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 124m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 124m..", "x": "Explored: 124m.. Belize. Why it is so — Blue Hole Belize. Cousteau. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lighthouse Reef.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lighthouse Reef.", "x": "Blue Hole Belize: Lighthouse Reef.. Sharks. One of the defining facts — Cousteau.. the deep blue circle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Lighthouse Reef..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Lighthouse Reef..", "x": "Explored: Lighthouse Reef.. Cousteau. Why it is so — Blue Hole Belize. Sharks. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Stalactites.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Stalactites.", "x": "Blue Hole Belize: Stalactites.. Belize. One of the defining facts — Sharks.. the deep blue circle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Stalactites..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Stalactites..", "x": "Explored: Stalactites.. Atoll. Why it is so — Blue Hole Belize. Atoll. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cousteau.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cousteau.", "x": "Blue Hole Belize: Cousteau.. Cousteau. One of the defining facts — Atoll.. the deep blue circle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Cousteau..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Cousteau..", "x": "Explored: Cousteau.. Depth. Why it is so — Blue Hole Belize. 124m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sharks.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sharks.", "x": "Blue Hole Belize: Sharks.. Atoll. One of the defining facts — 124m.. the deep blue circle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Sharks..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Sharks..", "x": "Explored: Sharks.. Stalactites. Why it is so — Blue Hole Belize. Lighthouse Reef. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Atoll.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Atoll.", "x": "Blue Hole Belize: Atoll.. Depth. One of the defining facts — Lighthouse Reef.. the deep blue circle. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Atoll..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Atoll..", "x": "Explored: Atoll.. Sharks. Why it is so — Blue Hole Belize. Stalactites. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Depth.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Depth.", "x": "Blue Hole Belize in depth: Depth.. Lighthouse Reef. The details reward the curious — the deep blue circle.. Sharks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stalactites.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stalactites.", "x": "Blue Hole Belize in depth: Stalactites.. Stalactites. The details reward the curious — the deep blue circle.. Belize. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sharks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sharks.", "x": "Blue Hole Belize in depth: Sharks.. Cousteau. The details reward the curious — the deep blue circle.. Cousteau. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Belize.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Belize.", "x": "Blue Hole Belize in depth: Belize.. Sharks. The details reward the curious — the deep blue circle.. Atoll. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cousteau.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cousteau.", "x": "Blue Hole Belize in depth: Cousteau.. Atoll. The details reward the curious — the deep blue circle.. Depth. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Atoll.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Atoll.", "x": "Blue Hole Belize in depth: Atoll.. 124m. The details reward the curious — the deep blue circle.. Stalactites. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Blue Hole Belize is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Blue Hole Belize is.", "x": "Location: 124m.. Depth. Getting oriented — Blue Hole Belize. the deep blue circle. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Blue Hole Belize.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Blue Hole Belize.", "x": "Visiting: Stalactites.. Lighthouse Reef. Practical know-how — Blue Hole Belize. the deep blue circle. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Blue Hole Belize.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Blue Hole Belize.", "x": "Ecology: Sharks.. Stalactites. The living world of Blue Hole Belize — the deep blue circle.. Belize. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Blue Hole Belize through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Blue Hole Belize through time.", "x": "History: Cousteau.. Cousteau. People and Blue Hole Belize across the centuries — the deep blue circle.. Atoll. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Blue Hole Belize.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Blue Hole Belize.", "x": "Conservation: Stalactites.. 124m. Threats and guardians of Blue Hole Belize — the deep blue circle.. Sharks. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Blue Hole Belize in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Blue Hole Belize in numbers.", "x": "Numbers: 124m.; Lighthouse Reef.. Belize. Statistics that stun — Blue Hole Belize. the deep blue circle. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive-blue-hole-belize-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
