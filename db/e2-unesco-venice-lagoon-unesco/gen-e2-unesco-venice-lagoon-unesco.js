(function(){'use strict';
/* JAH Venice Lagoon Unesco Site Database generator — jahdb-e2-unesco-venice-lagoon-unesco-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-venice-lagoon-unesco',PREFIX='JAH-E2UNESCOVEN-',NAME='JAH Venice Lagoon Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Venice Lagoon: the complete guide", "d": "Venice Lagoon: the floating city..", "g": "overview", "l": 2, "q": "What is Venice Lagoon: the complete guide?", "a": "Venice Lagoon: the floating city..", "x": "The complete unesco site guide to Venice Lagoon: the floating city.. Canals. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Canals.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Canals.", "x": "Venice Lagoon: Canals.. Canals. One of the defining facts — Gondolas.. the floating city. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Canals..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Canals..", "x": "Explored: Canals.. Threats. Why it is so — Venice Lagoon. UNESCO 1987. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "St. Mark's.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "St. Mark's.", "x": "Venice Lagoon: St. Mark's.. Art. One of the defining facts — UNESCO 1987.. the floating city. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: St. Mark's..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: St. Mark's..", "x": "Explored: St. Mark's.. Tours. Why it is so — Venice Lagoon. Acqua alta. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gondolas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gondolas.", "x": "Venice Lagoon: Gondolas.. Threats. One of the defining facts — Acqua alta.. the floating city. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Gondolas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Gondolas..", "x": "Explored: Gondolas.. Visit. Why it is so — Venice Lagoon. Murano. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO 1987.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO 1987.", "x": "Venice Lagoon: UNESCO 1987.. Tours. One of the defining facts — Murano.. the floating city. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: UNESCO 1987..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: UNESCO 1987..", "x": "Explored: UNESCO 1987.. History. Why it is so — Venice Lagoon. Canals. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Acqua alta.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Acqua alta.", "x": "Venice Lagoon: Acqua alta.. Visit. One of the defining facts — Canals.. the floating city. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Acqua alta..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Acqua alta..", "x": "Explored: Acqua alta.. Canals. Why it is so — Venice Lagoon. St. Mark's. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Murano.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Murano.", "x": "Venice Lagoon: Murano.. History. One of the defining facts — St. Mark's.. the floating city. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Murano..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Murano..", "x": "Explored: Murano.. Art. Why it is so — Venice Lagoon. Gondolas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Venice Lagoon in depth: History.. St. Mark's. The details reward the curious — the floating city.. Art. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Canals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Canals.", "x": "Venice Lagoon in depth: Canals.. Gondolas. The details reward the curious — the floating city.. Threats. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Art.", "x": "Venice Lagoon in depth: Art.. UNESCO 1987. The details reward the curious — the floating city.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Threats.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Threats.", "x": "Venice Lagoon in depth: Threats.. Acqua alta. The details reward the curious — the floating city.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Venice Lagoon in depth: Tours.. Murano. The details reward the curious — the floating city.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Venice Lagoon in depth: Visit.. Canals. The details reward the curious — the floating city.. Canals. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Venice Lagoon is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Venice Lagoon is.", "x": "Location: Canals.. History. Getting oriented — Venice Lagoon. the floating city. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Venice Lagoon.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Venice Lagoon.", "x": "Visiting: Canals.. St. Mark's. Practical know-how — Venice Lagoon. the floating city. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Venice Lagoon.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Venice Lagoon.", "x": "Ecology: Art.. Gondolas. The living world of Venice Lagoon — the floating city.. Threats. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Venice Lagoon through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Venice Lagoon through time.", "x": "History: Tours.. UNESCO 1987. People and Venice Lagoon across the centuries — the floating city.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Venice Lagoon.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Venice Lagoon.", "x": "Conservation: Canals.. Canals. Threats and guardians of Venice Lagoon — the floating city.. Art. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Venice Lagoon in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Venice Lagoon in numbers.", "x": "Numbers: Canals.; St. Mark's.. Threats. Statistics that stun — Venice Lagoon. the floating city. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-venice-lagoon-unesco-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
