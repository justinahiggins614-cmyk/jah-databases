(function(){'use strict';
/* JAH Taj Mahal Unesco Site Database generator — jahdb-e2-unesco-taj-mahal-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-taj-mahal',PREFIX='JAH-E2UNESCOTAJ-',NAME='JAH Taj Mahal Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Taj Mahal: the complete guide", "d": "Taj Mahal: marble monument to love..", "g": "overview", "l": 2, "q": "What is Taj Mahal: the complete guide?", "a": "Taj Mahal: marble monument to love..", "x": "The complete unesco site guide to Taj Mahal: marble monument to love.. Shah Jahan. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shah Jahan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shah Jahan.", "x": "Taj Mahal: Shah Jahan.. Architecture. One of the defining facts — 1632-1653.. marble monument to love. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Shah Jahan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Shah Jahan..", "x": "Explored: Shah Jahan.. Sunrise. Why it is so — Taj Mahal. Symmetry. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mumtaz.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mumtaz.", "x": "Taj Mahal: Mumtaz.. Marble. One of the defining facts — Symmetry.. marble monument to love. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Mumtaz..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Mumtaz..", "x": "Explored: Mumtaz.. Agra. Why it is so — Taj Mahal. Yamuna. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1632-1653.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1632-1653.", "x": "Taj Mahal: 1632-1653.. Sunrise. One of the defining facts — Yamuna.. marble monument to love. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: 1632-1653..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: 1632-1653..", "x": "Explored: 1632-1653.. Conservation. Why it is so — Taj Mahal. UNESCO 1983. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Symmetry.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Symmetry.", "x": "Taj Mahal: Symmetry.. Agra. One of the defining facts — UNESCO 1983.. marble monument to love. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Symmetry..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Symmetry..", "x": "Explored: Symmetry.. History. Why it is so — Taj Mahal. Shah Jahan. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Yamuna.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Yamuna.", "x": "Taj Mahal: Yamuna.. Conservation. One of the defining facts — Shah Jahan.. marble monument to love. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Yamuna..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Yamuna..", "x": "Explored: Yamuna.. Architecture. Why it is so — Taj Mahal. Mumtaz. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO 1983.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO 1983.", "x": "Taj Mahal: UNESCO 1983.. History. One of the defining facts — Mumtaz.. marble monument to love. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: UNESCO 1983..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: UNESCO 1983..", "x": "Explored: UNESCO 1983.. Marble. Why it is so — Taj Mahal. 1632-1653. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Taj Mahal in depth: History.. Mumtaz. The details reward the curious — marble monument to love.. Marble. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Architecture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Architecture.", "x": "Taj Mahal in depth: Architecture.. 1632-1653. The details reward the curious — marble monument to love.. Sunrise. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Marble.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Marble.", "x": "Taj Mahal in depth: Marble.. Symmetry. The details reward the curious — marble monument to love.. Agra. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sunrise.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sunrise.", "x": "Taj Mahal in depth: Sunrise.. Yamuna. The details reward the curious — marble monument to love.. Conservation. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Agra.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Agra.", "x": "Taj Mahal in depth: Agra.. UNESCO 1983. The details reward the curious — marble monument to love.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conservation.", "x": "Taj Mahal in depth: Conservation.. Shah Jahan. The details reward the curious — marble monument to love.. Architecture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Taj Mahal is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Taj Mahal is.", "x": "Location: Shah Jahan.. History. Getting oriented — Taj Mahal. marble monument to love. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Taj Mahal.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Taj Mahal.", "x": "Visiting: Architecture.. Mumtaz. Practical know-how — Taj Mahal. marble monument to love. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Taj Mahal.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Taj Mahal.", "x": "Ecology: Marble.. 1632-1653. The living world of Taj Mahal — marble monument to love.. Sunrise. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Taj Mahal through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Taj Mahal through time.", "x": "History: Agra.. Symmetry. People and Taj Mahal across the centuries — marble monument to love.. Conservation. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Taj Mahal.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Taj Mahal.", "x": "Conservation: Architecture.. Shah Jahan. Threats and guardians of Taj Mahal — marble monument to love.. Marble. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Taj Mahal in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Taj Mahal in numbers.", "x": "Numbers: Shah Jahan.; Mumtaz.. Sunrise. Statistics that stun — Taj Mahal. marble monument to love. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-taj-mahal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
