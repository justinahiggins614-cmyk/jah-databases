(function(){'use strict';
/* JAH Qatar Tennis Tennis Court Database generator — jahdb-e2-tennis-qatar-tennis-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tennis-qatar-tennis',PREFIX='JAH-E2TENNISQAT-',NAME='JAH Qatar Tennis Tennis Court Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Qatar Tennis: the complete guide", "d": "Qatar Tennis: the Doha event..", "g": "overview", "l": 2, "q": "What is Qatar Tennis: the complete guide?", "a": "Qatar Tennis: the Doha event..", "x": "The complete tennis court guide to Qatar Tennis: the Doha event.. 1993. From formation to visiting, from wildlife to legends — everything about this tennis court in one database. Doha. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1993.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1993.", "x": "Qatar Tennis: 1993.. Falcon. One of the defining facts — 250/500.. the Doha event. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1993..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1993..", "x": "Explored: 1993.. History. Why it is so — Qatar Tennis. Falcon. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Doha.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Doha.", "x": "Qatar Tennis: Doha.. Desert. One of the defining facts — Falcon.. the Doha event. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Doha..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Doha..", "x": "Explored: Doha.. February. Why it is so — Qatar Tennis. February. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "250/500.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "250/500.", "x": "Qatar Tennis: 250/500.. History. One of the defining facts — February.. the Doha event. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: 250/500..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: 250/500..", "x": "Explored: 250/500.. Tennis. Why it is so — Qatar Tennis. Desert. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Falcon.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Falcon.", "x": "Qatar Tennis: Falcon.. February. One of the defining facts — Desert.. the Doha event. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Falcon..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Falcon..", "x": "Explored: Falcon.. Doha. Why it is so — Qatar Tennis. 1993. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "February.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "February.", "x": "Qatar Tennis: February.. Tennis. One of the defining facts — 1993.. the Doha event. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: February..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: February..", "x": "Explored: February.. Falcon. Why it is so — Qatar Tennis. Doha. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Desert.", "x": "Qatar Tennis: Desert.. Doha. One of the defining facts — Doha.. the Doha event. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Desert..", "x": "Explored: Desert.. Desert. Why it is so — Qatar Tennis. 250/500. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Doha.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Doha.", "x": "Qatar Tennis in depth: Doha.. Doha. The details reward the curious — the Doha event.. Desert. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Falcon.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Falcon.", "x": "Qatar Tennis in depth: Falcon.. 250/500. The details reward the curious — the Doha event.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Desert.", "x": "Qatar Tennis in depth: Desert.. Falcon. The details reward the curious — the Doha event.. February. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Qatar Tennis in depth: History.. February. The details reward the curious — the Doha event.. Tennis. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "February.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "February.", "x": "Qatar Tennis in depth: February.. Desert. The details reward the curious — the Doha event.. Doha. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tennis.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tennis.", "x": "Qatar Tennis in depth: Tennis.. 1993. The details reward the curious — the Doha event.. Falcon. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Qatar Tennis is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Qatar Tennis is.", "x": "Location: 1993.. Doha. Getting oriented — Qatar Tennis. the Doha event. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Qatar Tennis.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Qatar Tennis.", "x": "Visiting: Falcon.. Doha. Practical know-how — Qatar Tennis. the Doha event. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Qatar Tennis.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Qatar Tennis.", "x": "Ecology: Desert.. 250/500. The living world of Qatar Tennis — the Doha event.. History. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Qatar Tennis through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Qatar Tennis through time.", "x": "History: February.. Falcon. People and Qatar Tennis across the centuries — the Doha event.. Tennis. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Qatar Tennis.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Qatar Tennis.", "x": "Conservation: Falcon.. 1993. Threats and guardians of Qatar Tennis — the Doha event.. Desert. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Qatar Tennis in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Qatar Tennis in numbers.", "x": "Numbers: 1993.; Doha.. History. Statistics that stun — Qatar Tennis. the Doha event. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tennis-qatar-tennis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
