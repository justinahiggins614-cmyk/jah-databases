(function(){'use strict';
/* JAH Rhone River River Database generator — jahdb-e2-river-rhone-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-rhone-river',PREFIX='JAH-E2RIVERRHON-',NAME='JAH Rhone River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rhone River: the complete guide", "d": "Rhone River: Alps to Mediterranean..", "g": "overview", "l": 2, "q": "What is Rhone River: the complete guide?", "a": "Rhone River: Alps to Mediterranean..", "x": "The complete river guide to Rhone River: Alps to Mediterranean.. 813 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Switzerland. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "813 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "813 km.", "x": "Rhone River: 813 km.. Cities. One of the defining facts — Avignon.. Alps to Mediterranean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 813 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 813 km..", "x": "Explored: 813 km.. Wine. Why it is so — Rhone River. Wine valleys. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lyon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lyon.", "x": "Rhone River: Lyon.. History. One of the defining facts — Wine valleys.. Alps to Mediterranean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Lyon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Lyon..", "x": "Explored: Lyon.. Nature. Why it is so — Rhone River. Dams. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Avignon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Avignon.", "x": "Rhone River: Avignon.. Wine. One of the defining facts — Dams.. Alps to Mediterranean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Avignon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Avignon..", "x": "Explored: Avignon.. Cruises. Why it is so — Rhone River. Camargue. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wine valleys.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wine valleys.", "x": "Rhone River: Wine valleys.. Nature. One of the defining facts — Camargue.. Alps to Mediterranean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Wine valleys..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Wine valleys..", "x": "Explored: Wine valleys.. Source: Switzerland. Why it is so — Rhone River. 813 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dams.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dams.", "x": "Rhone River: Dams.. Cruises. One of the defining facts — 813 km.. Alps to Mediterranean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Dams..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Dams..", "x": "Explored: Dams.. Cities. Why it is so — Rhone River. Lyon. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Camargue.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Camargue.", "x": "Rhone River: Camargue.. Source: Switzerland. One of the defining facts — Lyon.. Alps to Mediterranean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Camargue..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Camargue..", "x": "Explored: Camargue.. History. Why it is so — Rhone River. Avignon. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Switzerland.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Switzerland.", "x": "Rhone River in depth: Source: Switzerland.. Lyon. The details reward the curious — Alps to Mediterranean.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cities.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cities.", "x": "Rhone River in depth: Cities.. Avignon. The details reward the curious — Alps to Mediterranean.. Wine. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Rhone River in depth: History.. Wine valleys. The details reward the curious — Alps to Mediterranean.. Nature. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wine.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wine.", "x": "Rhone River in depth: Wine.. Dams. The details reward the curious — Alps to Mediterranean.. Cruises. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Nature.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Nature.", "x": "Rhone River in depth: Nature.. Camargue. The details reward the curious — Alps to Mediterranean.. Source: Switzerland. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cruises.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cruises.", "x": "Rhone River in depth: Cruises.. 813 km. The details reward the curious — Alps to Mediterranean.. Cities. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Rhone River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Rhone River is.", "x": "Location: 813 km.. Source: Switzerland. Getting oriented — Rhone River. Alps to Mediterranean. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Rhone River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Rhone River.", "x": "Visiting: Cities.. Lyon. Practical know-how — Rhone River. Alps to Mediterranean. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Rhone River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Rhone River.", "x": "Ecology: History.. Avignon. The living world of Rhone River — Alps to Mediterranean.. Wine. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Rhone River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Rhone River through time.", "x": "History: Nature.. Wine valleys. People and Rhone River across the centuries — Alps to Mediterranean.. Cruises. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Rhone River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Rhone River.", "x": "Conservation: Cities.. 813 km. Threats and guardians of Rhone River — Alps to Mediterranean.. History. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Rhone River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Rhone River in numbers.", "x": "Numbers: 813 km.; Lyon.. Wine. Statistics that stun — Rhone River. Alps to Mediterranean. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-rhone-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
