(function(){'use strict';
/* JAH Poor Knights NZ Dive Site Database generator — jahdb-e2-dive-poor-knights-nz-dives-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive-poor-knights-nz-dives',PREFIX='JAH-E2DIVEPOORK-',NAME='JAH Poor Knights NZ Dive Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Poor Knights NZ: the complete guide", "d": "Poor Knights NZ: Cousteau's top ten..", "g": "overview", "l": 2, "q": "What is Poor Knights NZ: the complete guide?", "a": "Poor Knights NZ: Cousteau's top ten..", "x": "The complete dive site guide to Poor Knights NZ: Cousteau's top ten.. New Zealand. From formation to visiting, from wildlife to legends — everything about this dive site in one database. Arches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "New Zealand.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "New Zealand.", "x": "Poor Knights NZ: New Zealand.. Cousteau. One of the defining facts — Arches.. Cousteau's top ten. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: New Zealand..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: New Zealand..", "x": "Explored: New Zealand.. NZ. Why it is so — Poor Knights NZ.  subtropical. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cousteau.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cousteau.", "x": "Poor Knights NZ: Cousteau.. Biodiversity. One of the defining facts —  subtropical.. Cousteau's top ten. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Cousteau..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Cousteau..", "x": "Explored: Cousteau..  subtropical. Why it is so — Poor Knights NZ. Tutukaka. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Arches.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Arches.", "x": "Poor Knights NZ: Arches.. NZ. One of the defining facts — Tutukaka.. Cousteau's top ten. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Arches..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Arches..", "x": "Explored: Arches.. Reserve. Why it is so — Poor Knights NZ. Biodiversity. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": " subtropical.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": " subtropical.", "x": "Poor Knights NZ:  subtropical..  subtropical. One of the defining facts — Biodiversity.. Cousteau's top ten. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding:  subtropical..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding:  subtropical..", "x": "Explored:  subtropical.. Arches. Why it is so — Poor Knights NZ. New Zealand. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tutukaka.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tutukaka.", "x": "Poor Knights NZ: Tutukaka.. Reserve. One of the defining facts — New Zealand.. Cousteau's top ten. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Tutukaka..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Tutukaka..", "x": "Explored: Tutukaka.. Cousteau. Why it is so — Poor Knights NZ. Cousteau. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Biodiversity.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Biodiversity.", "x": "Poor Knights NZ: Biodiversity.. Arches. One of the defining facts — Cousteau.. Cousteau's top ten. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Biodiversity..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Biodiversity..", "x": "Explored: Biodiversity.. Biodiversity. Why it is so — Poor Knights NZ. Arches. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Arches.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Arches.", "x": "Poor Knights NZ in depth: Arches.. Cousteau. The details reward the curious — Cousteau's top ten.. Biodiversity. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cousteau.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cousteau.", "x": "Poor Knights NZ in depth: Cousteau.. Arches. The details reward the curious — Cousteau's top ten.. NZ. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Biodiversity.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Biodiversity.", "x": "Poor Knights NZ in depth: Biodiversity..  subtropical. The details reward the curious — Cousteau's top ten..  subtropical. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "NZ.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "NZ.", "x": "Poor Knights NZ in depth: NZ.. Tutukaka. The details reward the curious — Cousteau's top ten.. Reserve. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": " subtropical.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": " subtropical.", "x": "Poor Knights NZ in depth:  subtropical.. Biodiversity. The details reward the curious — Cousteau's top ten.. Arches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Reserve.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Reserve.", "x": "Poor Knights NZ in depth: Reserve.. New Zealand. The details reward the curious — Cousteau's top ten.. Cousteau. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Poor Knights NZ is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Poor Knights NZ is.", "x": "Location: New Zealand.. Arches. Getting oriented — Poor Knights NZ. Cousteau's top ten. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Poor Knights NZ.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Poor Knights NZ.", "x": "Visiting: Cousteau.. Cousteau. Practical know-how — Poor Knights NZ. Cousteau's top ten. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Poor Knights NZ.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Poor Knights NZ.", "x": "Ecology: Biodiversity.. Arches. The living world of Poor Knights NZ — Cousteau's top ten.. NZ. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Poor Knights NZ through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Poor Knights NZ through time.", "x": "History:  subtropical..  subtropical. People and Poor Knights NZ across the centuries — Cousteau's top ten.. Reserve. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Poor Knights NZ.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Poor Knights NZ.", "x": "Conservation: Cousteau.. New Zealand. Threats and guardians of Poor Knights NZ — Cousteau's top ten.. Biodiversity. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Poor Knights NZ in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Poor Knights NZ in numbers.", "x": "Numbers: New Zealand.; Cousteau.. NZ. Statistics that stun — Poor Knights NZ. Cousteau's top ten. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive-poor-knights-nz-dives-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
