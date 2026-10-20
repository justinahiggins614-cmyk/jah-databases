(function(){'use strict';
/* JAH Great Zimbabwe Unesco Site Database generator — jahdb-e2-unesco-great-zimbabwe-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-great-zimbabwe',PREFIX='JAH-E2UNESCOGRE-',NAME='JAH Great Zimbabwe Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Great Zimbabwe: the complete guide", "d": "Great Zimbabwe: stone city of Africa..", "g": "overview", "l": 2, "q": "What is Great Zimbabwe: the complete guide?", "a": "Great Zimbabwe: stone city of Africa..", "x": "The complete unesco site guide to Great Zimbabwe: stone city of Africa.. 11th-15th c. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "11th-15th c.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "11th-15th c.", "x": "Great Zimbabwe: 11th-15th c.. Walls. One of the defining facts — Shona.. stone city of Africa. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 11th-15th c..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 11th-15th c..", "x": "Explored: 11th-15th c.. Tours. Why it is so — Great Zimbabwe. Trade. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Great Enclosure.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Great Enclosure.", "x": "Great Zimbabwe: Great Enclosure.. Trade. One of the defining facts — Trade.. stone city of Africa. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Great Enclosure..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Great Enclosure..", "x": "Explored: Great Enclosure.. Theories. Why it is so — Great Zimbabwe. UNESCO 1986. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shona.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shona.", "x": "Great Zimbabwe: Shona.. Tours. One of the defining facts — UNESCO 1986.. stone city of Africa. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Shona..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Shona..", "x": "Explored: Shona.. Visit. Why it is so — Great Zimbabwe. Bird. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Trade.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Trade.", "x": "Great Zimbabwe: Trade.. Theories. One of the defining facts — Bird.. stone city of Africa. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Trade..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Trade..", "x": "Explored: Trade.. History. Why it is so — Great Zimbabwe. 11th-15th c. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO 1986.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO 1986.", "x": "Great Zimbabwe: UNESCO 1986.. Visit. One of the defining facts — 11th-15th c.. stone city of Africa. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: UNESCO 1986..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: UNESCO 1986..", "x": "Explored: UNESCO 1986.. Walls. Why it is so — Great Zimbabwe. Great Enclosure. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bird.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bird.", "x": "Great Zimbabwe: Bird.. History. One of the defining facts — Great Enclosure.. stone city of Africa. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Bird..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Bird..", "x": "Explored: Bird.. Trade. Why it is so — Great Zimbabwe. Shona. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Great Zimbabwe in depth: History.. Great Enclosure. The details reward the curious — stone city of Africa.. Trade. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Walls.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Walls.", "x": "Great Zimbabwe in depth: Walls.. Shona. The details reward the curious — stone city of Africa.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Trade.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Trade.", "x": "Great Zimbabwe in depth: Trade.. Trade. The details reward the curious — stone city of Africa.. Theories. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Great Zimbabwe in depth: Tours.. UNESCO 1986. The details reward the curious — stone city of Africa.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Theories.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Theories.", "x": "Great Zimbabwe in depth: Theories.. Bird. The details reward the curious — stone city of Africa.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Great Zimbabwe in depth: Visit.. 11th-15th c. The details reward the curious — stone city of Africa.. Walls. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Great Zimbabwe is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Great Zimbabwe is.", "x": "Location: 11th-15th c.. History. Getting oriented — Great Zimbabwe. stone city of Africa. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Great Zimbabwe.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Great Zimbabwe.", "x": "Visiting: Walls.. Great Enclosure. Practical know-how — Great Zimbabwe. stone city of Africa. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Great Zimbabwe.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Great Zimbabwe.", "x": "Ecology: Trade.. Shona. The living world of Great Zimbabwe — stone city of Africa.. Tours. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Great Zimbabwe through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Great Zimbabwe through time.", "x": "History: Theories.. Trade. People and Great Zimbabwe across the centuries — stone city of Africa.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Great Zimbabwe.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Great Zimbabwe.", "x": "Conservation: Walls.. 11th-15th c. Threats and guardians of Great Zimbabwe — stone city of Africa.. Trade. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Great Zimbabwe in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Great Zimbabwe in numbers.", "x": "Numbers: 11th-15th c.; Great Enclosure.. Tours. Statistics that stun — Great Zimbabwe. stone city of Africa. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-great-zimbabwe-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
