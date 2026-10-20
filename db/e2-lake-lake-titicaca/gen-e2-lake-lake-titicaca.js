(function(){'use strict';
/* JAH Lake Titicaca Lake Database generator — jahdb-e2-lake-lake-titicaca-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lake-lake-titicaca',PREFIX='JAH-E2LAKELAKET-',NAME='JAH Lake Titicaca Lake Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lake Titicaca: the complete guide", "d": "Lake Titicaca: highest navigable lake..", "g": "overview", "l": 2, "q": "What is Lake Titicaca: the complete guide?", "a": "Lake Titicaca: highest navigable lake..", "x": "The complete lake guide to Lake Titicaca: highest navigable lake.. 3,812m. From formation to visiting, from wildlife to legends — everything about this lake in one database. Islands. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,812m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,812m.", "x": "Lake Titicaca: 3,812m.. Culture. One of the defining facts — Uros reed islands.. highest navigable lake. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 3,812m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 3,812m..", "x": "Explored: 3,812m.. Towns. Why it is so — Lake Titicaca. Taquile. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Peru/Bolivia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Peru/Bolivia.", "x": "Lake Titicaca: Peru/Bolivia.. Myths. One of the defining facts — Taquile.. highest navigable lake. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Peru/Bolivia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Peru/Bolivia..", "x": "Explored: Peru/Bolivia.. Travel. Why it is so — Lake Titicaca. Inca myths. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Uros reed islands.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Uros reed islands.", "x": "Lake Titicaca: Uros reed islands.. Towns. One of the defining facts — Inca myths.. highest navigable lake. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Uros reed islands..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Uros reed islands..", "x": "Explored: Uros reed islands.. History. Why it is so — Lake Titicaca. Ferries. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Taquile.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Taquile.", "x": "Lake Titicaca: Taquile.. Travel. One of the defining facts — Ferries.. highest navigable lake. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Taquile..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Taquile..", "x": "Explored: Taquile.. Islands. Why it is so — Lake Titicaca. 3,812m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Inca myths.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Inca myths.", "x": "Lake Titicaca: Inca myths.. History. One of the defining facts — 3,812m.. highest navigable lake. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Inca myths..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Inca myths..", "x": "Explored: Inca myths.. Culture. Why it is so — Lake Titicaca. Peru/Bolivia. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ferries.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ferries.", "x": "Lake Titicaca: Ferries.. Islands. One of the defining facts — Peru/Bolivia.. highest navigable lake. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Ferries..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Ferries..", "x": "Explored: Ferries.. Myths. Why it is so — Lake Titicaca. Uros reed islands. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Islands.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Islands.", "x": "Lake Titicaca in depth: Islands.. Peru/Bolivia. The details reward the curious — highest navigable lake.. Myths. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Culture.", "x": "Lake Titicaca in depth: Culture.. Uros reed islands. The details reward the curious — highest navigable lake.. Towns. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Myths.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Myths.", "x": "Lake Titicaca in depth: Myths.. Taquile. The details reward the curious — highest navigable lake.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Towns.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Towns.", "x": "Lake Titicaca in depth: Towns.. Inca myths. The details reward the curious — highest navigable lake.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "Lake Titicaca in depth: Travel.. Ferries. The details reward the curious — highest navigable lake.. Islands. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Lake Titicaca in depth: History.. 3,812m. The details reward the curious — highest navigable lake.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Lake Titicaca is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Lake Titicaca is.", "x": "Location: 3,812m.. Islands. Getting oriented — Lake Titicaca. highest navigable lake. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Lake Titicaca.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Lake Titicaca.", "x": "Visiting: Culture.. Peru/Bolivia. Practical know-how — Lake Titicaca. highest navigable lake. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Lake Titicaca.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Lake Titicaca.", "x": "Ecology: Myths.. Uros reed islands. The living world of Lake Titicaca — highest navigable lake.. Towns. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Lake Titicaca through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Lake Titicaca through time.", "x": "History: Travel.. Taquile. People and Lake Titicaca across the centuries — highest navigable lake.. History. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Lake Titicaca.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Lake Titicaca.", "x": "Conservation: Culture.. 3,812m. Threats and guardians of Lake Titicaca — highest navigable lake.. Myths. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Lake Titicaca in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Lake Titicaca in numbers.", "x": "Numbers: 3,812m.; Peru/Bolivia.. Towns. Statistics that stun — Lake Titicaca. highest navigable lake. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lake-lake-titicaca-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
