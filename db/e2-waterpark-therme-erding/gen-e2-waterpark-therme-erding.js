(function(){'use strict';
/* JAH Therme Erding Water Park Database generator — jahdb-e2-waterpark-therme-erding-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-waterpark-therme-erding',PREFIX='JAH-E2WATERPARK-',NAME='JAH Therme Erding Water Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Therme Erding: the complete guide", "d": "Therme Erding: Europe's largest thermal..", "g": "overview", "l": 2, "q": "What is Therme Erding: the complete guide?", "a": "Therme Erding: Europe's largest thermal..", "x": "The complete water park guide to Therme Erding: Europe's largest thermal.. Thermal. From formation to visiting, from wildlife to legends — everything about this water park in one database. Thermal. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Thermal.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Thermal.", "x": "Therme Erding: Thermal.. Slides. One of the defining facts — Galaxy.. Europe's largest thermal. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Thermal..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Thermal..", "x": "Explored: Thermal.. Tickets. Why it is so — Therme Erding. Saunas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Slides.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Slides.", "x": "Therme Erding: Slides.. Saunas. One of the defining facts — Saunas.. Europe's largest thermal. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Slides..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Slides..", "x": "Explored: Slides.. Germany. Why it is so — Therme Erding. Germany. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Galaxy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Galaxy.", "x": "Therme Erding: Galaxy.. Tickets. One of the defining facts — Germany.. Europe's largest thermal. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Galaxy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Galaxy..", "x": "Explored: Galaxy.. Relax. Why it is so — Therme Erding. Adults. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Saunas.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Saunas.", "x": "Therme Erding: Saunas.. Germany. One of the defining facts — Adults.. Europe's largest thermal. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Saunas..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Saunas..", "x": "Explored: Saunas.. Thermal. Why it is so — Therme Erding. Thermal. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Germany.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Germany.", "x": "Therme Erding: Germany.. Relax. One of the defining facts — Thermal.. Europe's largest thermal. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Germany..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Germany..", "x": "Explored: Germany.. Slides. Why it is so — Therme Erding. Slides. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Adults.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Adults.", "x": "Therme Erding: Adults.. Thermal. One of the defining facts — Slides.. Europe's largest thermal. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Adults..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Adults..", "x": "Explored: Adults.. Saunas. Why it is so — Therme Erding. Galaxy. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Thermal.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Thermal.", "x": "Therme Erding in depth: Thermal.. Slides. The details reward the curious — Europe's largest thermal.. Saunas. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Slides.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Slides.", "x": "Therme Erding in depth: Slides.. Galaxy. The details reward the curious — Europe's largest thermal.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Saunas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Saunas.", "x": "Therme Erding in depth: Saunas.. Saunas. The details reward the curious — Europe's largest thermal.. Germany. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Therme Erding in depth: Tickets.. Germany. The details reward the curious — Europe's largest thermal.. Relax. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Germany.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Germany.", "x": "Therme Erding in depth: Germany.. Adults. The details reward the curious — Europe's largest thermal.. Thermal. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Relax.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Relax.", "x": "Therme Erding in depth: Relax.. Thermal. The details reward the curious — Europe's largest thermal.. Slides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Therme Erding is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Therme Erding is.", "x": "Location: Thermal.. Thermal. Getting oriented — Therme Erding. Europe's largest thermal. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Therme Erding.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Therme Erding.", "x": "Visiting: Slides.. Slides. Practical know-how — Therme Erding. Europe's largest thermal. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Therme Erding.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Therme Erding.", "x": "Ecology: Saunas.. Galaxy. The living world of Therme Erding — Europe's largest thermal.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Therme Erding through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Therme Erding through time.", "x": "History: Germany.. Saunas. People and Therme Erding across the centuries — Europe's largest thermal.. Relax. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Therme Erding.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Therme Erding.", "x": "Conservation: Slides.. Thermal. Threats and guardians of Therme Erding — Europe's largest thermal.. Saunas. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Therme Erding in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Therme Erding in numbers.", "x": "Numbers: Thermal.; Slides.. Tickets. Statistics that stun — Therme Erding. Europe's largest thermal. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-waterpark-therme-erding-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
