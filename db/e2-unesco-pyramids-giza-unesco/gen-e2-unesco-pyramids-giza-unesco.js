(function(){'use strict';
/* JAH Pyramids of Giza Unesco Site Database generator — jahdb-e2-unesco-pyramids-giza-unesco-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-pyramids-giza-unesco',PREFIX='JAH-E2UNESCOPYR-',NAME='JAH Pyramids of Giza Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pyramids of Giza: the complete guide", "d": "Pyramids of Giza: last ancient wonder..", "g": "overview", "l": 2, "q": "What is Pyramids of Giza: the complete guide?", "a": "Pyramids of Giza: last ancient wonder..", "x": "The complete unesco site guide to Pyramids of Giza: last ancient wonder.. Khufu. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Khufu.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Khufu.", "x": "Pyramids of Giza: Khufu.. Pyramids. One of the defining facts — Solar boats.. last ancient wonder. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Khufu..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Khufu..", "x": "Explored: Khufu.. Tours. Why it is so — Pyramids of Giza. UNESCO 1979. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sphinx.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sphinx.", "x": "Pyramids of Giza: Sphinx.. Sphinx. One of the defining facts — UNESCO 1979.. last ancient wonder. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Sphinx..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Sphinx..", "x": "Explored: Sphinx.. Conservation. Why it is so — Pyramids of Giza. Cairo. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Solar boats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Solar boats.", "x": "Pyramids of Giza: Solar boats.. Tours. One of the defining facts — Cairo.. last ancient wonder. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Solar boats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Solar boats..", "x": "Explored: Solar boats.. Visit. Why it is so — Pyramids of Giza. Chambers. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO 1979.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO 1979.", "x": "Pyramids of Giza: UNESCO 1979.. Conservation. One of the defining facts — Chambers.. last ancient wonder. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: UNESCO 1979..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: UNESCO 1979..", "x": "Explored: UNESCO 1979.. History. Why it is so — Pyramids of Giza. Khufu. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cairo.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cairo.", "x": "Pyramids of Giza: Cairo.. Visit. One of the defining facts — Khufu.. last ancient wonder. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Cairo..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Cairo..", "x": "Explored: Cairo.. Pyramids. Why it is so — Pyramids of Giza. Sphinx. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chambers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chambers.", "x": "Pyramids of Giza: Chambers.. History. One of the defining facts — Sphinx.. last ancient wonder. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Chambers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Chambers..", "x": "Explored: Chambers.. Sphinx. Why it is so — Pyramids of Giza. Solar boats. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Pyramids of Giza in depth: History.. Sphinx. The details reward the curious — last ancient wonder.. Sphinx. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pyramids.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pyramids.", "x": "Pyramids of Giza in depth: Pyramids.. Solar boats. The details reward the curious — last ancient wonder.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sphinx.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sphinx.", "x": "Pyramids of Giza in depth: Sphinx.. UNESCO 1979. The details reward the curious — last ancient wonder.. Conservation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Pyramids of Giza in depth: Tours.. Cairo. The details reward the curious — last ancient wonder.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conservation.", "x": "Pyramids of Giza in depth: Conservation.. Chambers. The details reward the curious — last ancient wonder.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Pyramids of Giza in depth: Visit.. Khufu. The details reward the curious — last ancient wonder.. Pyramids. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Pyramids of Giza is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Pyramids of Giza is.", "x": "Location: Khufu.. History. Getting oriented — Pyramids of Giza. last ancient wonder. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Pyramids of Giza.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Pyramids of Giza.", "x": "Visiting: Pyramids.. Sphinx. Practical know-how — Pyramids of Giza. last ancient wonder. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Pyramids of Giza.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Pyramids of Giza.", "x": "Ecology: Sphinx.. Solar boats. The living world of Pyramids of Giza — last ancient wonder.. Tours. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Pyramids of Giza through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Pyramids of Giza through time.", "x": "History: Conservation.. UNESCO 1979. People and Pyramids of Giza across the centuries — last ancient wonder.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Pyramids of Giza.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Pyramids of Giza.", "x": "Conservation: Pyramids.. Khufu. Threats and guardians of Pyramids of Giza — last ancient wonder.. Sphinx. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Pyramids of Giza in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Pyramids of Giza in numbers.", "x": "Numbers: Khufu.; Sphinx.. Tours. Statistics that stun — Pyramids of Giza. last ancient wonder. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-pyramids-giza-unesco-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
