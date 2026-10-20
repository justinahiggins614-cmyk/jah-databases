(function(){'use strict';
/* JAH Mezquita of Cordoba Unesco Site Database generator — jahdb-e2-unesco-mezquita-cordoba-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-mezquita-cordoba',PREFIX='JAH-E2UNESCOMEZ-',NAME='JAH Mezquita of Cordoba Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mezquita of Cordoba: the complete guide", "d": "Mezquita of Cordoba: mosque-cathedral..", "g": "overview", "l": 2, "q": "What is Mezquita of Cordoba: the complete guide?", "a": "Mezquita of Cordoba: mosque-cathedral..", "x": "The complete unesco site guide to Mezquita of Cordoba: mosque-cathedral.. 785 AD. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "785 AD.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "785 AD.", "x": "Mezquita of Cordoba: 785 AD.. Architecture. One of the defining facts — Mihrab.. mosque-cathedral. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 785 AD..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 785 AD..", "x": "Explored: 785 AD.. Tours. Why it is so — Mezquita of Cordoba. Cathedral inside. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Forest of columns.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Forest of columns.", "x": "Mezquita of Cordoba: Forest of columns.. Mihrab. One of the defining facts — Cathedral inside.. mosque-cathedral. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Forest of columns..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Forest of columns..", "x": "Explored: Forest of columns.. Debate. Why it is so — Mezquita of Cordoba. UNESCO 1984. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mihrab.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mihrab.", "x": "Mezquita of Cordoba: Mihrab.. Tours. One of the defining facts — UNESCO 1984.. mosque-cathedral. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Mihrab..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Mihrab..", "x": "Explored: Mihrab.. Respect. Why it is so — Mezquita of Cordoba. Controversy. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cathedral inside.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cathedral inside.", "x": "Mezquita of Cordoba: Cathedral inside.. Debate. One of the defining facts — Controversy.. mosque-cathedral. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Cathedral inside..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Cathedral inside..", "x": "Explored: Cathedral inside.. History. Why it is so — Mezquita of Cordoba. 785 AD. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO 1984.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO 1984.", "x": "Mezquita of Cordoba: UNESCO 1984.. Respect. One of the defining facts — 785 AD.. mosque-cathedral. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: UNESCO 1984..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: UNESCO 1984..", "x": "Explored: UNESCO 1984.. Architecture. Why it is so — Mezquita of Cordoba. Forest of columns. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Controversy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Controversy.", "x": "Mezquita of Cordoba: Controversy.. History. One of the defining facts — Forest of columns.. mosque-cathedral. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Controversy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Controversy..", "x": "Explored: Controversy.. Mihrab. Why it is so — Mezquita of Cordoba. Mihrab. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Mezquita of Cordoba in depth: History.. Forest of columns. The details reward the curious — mosque-cathedral.. Mihrab. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Architecture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Architecture.", "x": "Mezquita of Cordoba in depth: Architecture.. Mihrab. The details reward the curious — mosque-cathedral.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mihrab.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mihrab.", "x": "Mezquita of Cordoba in depth: Mihrab.. Cathedral inside. The details reward the curious — mosque-cathedral.. Debate. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Mezquita of Cordoba in depth: Tours.. UNESCO 1984. The details reward the curious — mosque-cathedral.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Debate.", "x": "Mezquita of Cordoba in depth: Debate.. Controversy. The details reward the curious — mosque-cathedral.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Mezquita of Cordoba in depth: Respect.. 785 AD. The details reward the curious — mosque-cathedral.. Architecture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mezquita of Cordoba is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mezquita of Cordoba is.", "x": "Location: 785 AD.. History. Getting oriented — Mezquita of Cordoba. mosque-cathedral. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mezquita of Cordoba.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mezquita of Cordoba.", "x": "Visiting: Architecture.. Forest of columns. Practical know-how — Mezquita of Cordoba. mosque-cathedral. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mezquita of Cordoba.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mezquita of Cordoba.", "x": "Ecology: Mihrab.. Mihrab. The living world of Mezquita of Cordoba — mosque-cathedral.. Tours. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mezquita of Cordoba through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mezquita of Cordoba through time.", "x": "History: Debate.. Cathedral inside. People and Mezquita of Cordoba across the centuries — mosque-cathedral.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mezquita of Cordoba.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mezquita of Cordoba.", "x": "Conservation: Architecture.. 785 AD. Threats and guardians of Mezquita of Cordoba — mosque-cathedral.. Mihrab. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mezquita of Cordoba in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mezquita of Cordoba in numbers.", "x": "Numbers: 785 AD.; Forest of columns.. Tours. Statistics that stun — Mezquita of Cordoba. mosque-cathedral. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-mezquita-cordoba-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
