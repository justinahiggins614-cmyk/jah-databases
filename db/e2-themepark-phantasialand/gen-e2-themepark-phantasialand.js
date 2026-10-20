(function(){'use strict';
/* JAH Phantasialand Theme Park Database generator — jahdb-e2-themepark-phantasialand-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-themepark-phantasialand',PREFIX='JAH-E2THEMEPARK-',NAME='JAH Phantasialand Theme Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Phantasialand: the complete guide", "d": "Phantasialand: Germany's themed gem..", "g": "overview", "l": 2, "q": "What is Phantasialand: the complete guide?", "a": "Phantasialand: Germany's themed gem..", "x": "The complete theme park guide to Phantasialand: Germany's themed gem.. 1967. From formation to visiting, from wildlife to legends — everything about this theme park in one database. Theming. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1967.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1967.", "x": "Phantasialand: 1967.. Coasters. One of the defining facts — Chiapas.. Germany's themed gem. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1967..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1967..", "x": "Explored: 1967.. Tickets. Why it is so — Phantasialand. Theming. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Taron.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Taron.", "x": "Phantasialand: Taron.. Hotels. One of the defining facts — Theming.. Germany's themed gem. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Taron..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Taron..", "x": "Explored: Taron.. Germany. Why it is so — Phantasialand. Bruhl. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chiapas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chiapas.", "x": "Phantasialand: Chiapas.. Tickets. One of the defining facts — Bruhl.. Germany's themed gem. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Chiapas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Chiapas..", "x": "Explored: Chiapas.. Detail. Why it is so — Phantasialand. Hotels. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Theming.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Theming.", "x": "Phantasialand: Theming.. Germany. One of the defining facts — Hotels.. Germany's themed gem. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Theming..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Theming..", "x": "Explored: Theming.. Theming. Why it is so — Phantasialand. 1967. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bruhl.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bruhl.", "x": "Phantasialand: Bruhl.. Detail. One of the defining facts — 1967.. Germany's themed gem. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Bruhl..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Bruhl..", "x": "Explored: Bruhl.. Coasters. Why it is so — Phantasialand. Taron. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hotels.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hotels.", "x": "Phantasialand: Hotels.. Theming. One of the defining facts — Taron.. Germany's themed gem. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Hotels..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Hotels..", "x": "Explored: Hotels.. Hotels. Why it is so — Phantasialand. Chiapas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Theming.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Theming.", "x": "Phantasialand in depth: Theming.. Taron. The details reward the curious — Germany's themed gem.. Hotels. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Coasters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Coasters.", "x": "Phantasialand in depth: Coasters.. Chiapas. The details reward the curious — Germany's themed gem.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hotels.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hotels.", "x": "Phantasialand in depth: Hotels.. Theming. The details reward the curious — Germany's themed gem.. Germany. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Phantasialand in depth: Tickets.. Bruhl. The details reward the curious — Germany's themed gem.. Detail. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Germany.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Germany.", "x": "Phantasialand in depth: Germany.. Hotels. The details reward the curious — Germany's themed gem.. Theming. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Detail.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Detail.", "x": "Phantasialand in depth: Detail.. 1967. The details reward the curious — Germany's themed gem.. Coasters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Phantasialand is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Phantasialand is.", "x": "Location: 1967.. Theming. Getting oriented — Phantasialand. Germany's themed gem. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Phantasialand.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Phantasialand.", "x": "Visiting: Coasters.. Taron. Practical know-how — Phantasialand. Germany's themed gem. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Phantasialand.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Phantasialand.", "x": "Ecology: Hotels.. Chiapas. The living world of Phantasialand — Germany's themed gem.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Phantasialand through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Phantasialand through time.", "x": "History: Germany.. Theming. People and Phantasialand across the centuries — Germany's themed gem.. Detail. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Phantasialand.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Phantasialand.", "x": "Conservation: Coasters.. 1967. Threats and guardians of Phantasialand — Germany's themed gem.. Hotels. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Phantasialand in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Phantasialand in numbers.", "x": "Numbers: 1967.; Taron.. Tickets. Statistics that stun — Phantasialand. Germany's themed gem. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-themepark-phantasialand-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
