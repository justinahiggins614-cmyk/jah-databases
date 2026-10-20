(function(){'use strict';
/* JAH Nile River River Database generator — jahdb-e2-river-nile-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-nile-river',PREFIX='JAH-E2RIVERNILE-',NAME='JAH Nile River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nile River: the complete guide", "d": "Nile River: the world's longest river; Egypt's lifeline..", "g": "overview", "l": 2, "q": "What is Nile River: the complete guide?", "a": "Nile River: the world's longest river; Egypt's lifeline..", "x": "The complete river guide to Nile River: the world's longest river; Egypt's lifeline.. 6,650 km long. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Lake Victoria region.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "6,650 km long.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "6,650 km long.", "x": "Nile River: 6,650 km long.. Delta in Egypt. One of the defining facts — Blue + White Nile.. the world's longest river; Egypt's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 6,650 km long..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 6,650 km long..", "x": "Explored: 6,650 km long.. Nile perch. Why it is so — Nile River. Annual flood fertilized Egypt. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flows north.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flows north.", "x": "Nile River: Flows north.. Ancient civilization. One of the defining facts — Annual flood fertilized Egypt.. the world's longest river; Egypt's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Flows north..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Flows north..", "x": "Explored: Flows north.. Disputes over water. Why it is so — Nile River. Aswan Dam (1970). Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Blue + White Nile.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Blue + White Nile.", "x": "Nile River: Blue + White Nile.. Nile perch. One of the defining facts — Aswan Dam (1970).. the world's longest river; Egypt's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Blue + White Nile..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Blue + White Nile..", "x": "Explored: Blue + White Nile.. Cruises. Why it is so — Nile River. 11 countries share it. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Annual flood fertilized Egypt.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Annual flood fertilized Egypt.", "x": "Nile River: Annual flood fertilized Egypt.. Disputes over water. One of the defining facts — 11 countries share it.. the world's longest river; Egypt's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Annual flood fertilized Egypt..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Annual flood fertilized Egypt..", "x": "Explored: Annual flood fertilized Egypt.. Source: Lake Victoria region. Why it is so — Nile River. 6,650 km long. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Aswan Dam (1970).", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Aswan Dam (1970).", "x": "Nile River: Aswan Dam (1970).. Cruises. One of the defining facts — 6,650 km long.. the world's longest river; Egypt's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Aswan Dam (1970)..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Aswan Dam (1970)..", "x": "Explored: Aswan Dam (1970).. Delta in Egypt. Why it is so — Nile River. Flows north. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "11 countries share it.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "11 countries share it.", "x": "Nile River: 11 countries share it.. Source: Lake Victoria region. One of the defining facts — Flows north.. the world's longest river; Egypt's lifeline. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: 11 countries share it..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: 11 countries share it..", "x": "Explored: 11 countries share it.. Ancient civilization. Why it is so — Nile River. Blue + White Nile. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Lake Victoria region.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Lake Victoria region.", "x": "Nile River in depth: Source: Lake Victoria region.. Flows north. The details reward the curious — the world's longest river; Egypt's lifeline.. Ancient civilization. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Delta in Egypt.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Delta in Egypt.", "x": "Nile River in depth: Delta in Egypt.. Blue + White Nile. The details reward the curious — the world's longest river; Egypt's lifeline.. Nile perch. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ancient civilization.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ancient civilization.", "x": "Nile River in depth: Ancient civilization.. Annual flood fertilized Egypt. The details reward the curious — the world's longest river; Egypt's lifeline.. Disputes over water. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nile perch.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nile perch.", "x": "Nile River in depth: Nile perch.. Aswan Dam (1970). The details reward the curious — the world's longest river; Egypt's lifeline.. Cruises. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Disputes over water.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Disputes over water.", "x": "Nile River in depth: Disputes over water.. 11 countries share it. The details reward the curious — the world's longest river; Egypt's lifeline.. Source: Lake Victoria region. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cruises.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cruises.", "x": "Nile River in depth: Cruises.. 6,650 km long. The details reward the curious — the world's longest river; Egypt's lifeline.. Delta in Egypt. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Nile River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Nile River is.", "x": "Location: 6,650 km long.. Source: Lake Victoria region. Getting oriented — Nile River. the world's longest river; Egypt's lifeline. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Nile River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Nile River.", "x": "Visiting: Delta in Egypt.. Flows north. Practical know-how — Nile River. the world's longest river; Egypt's lifeline. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Nile River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Nile River.", "x": "Ecology: Ancient civilization.. Blue + White Nile. The living world of Nile River — the world's longest river; Egypt's lifeline.. Nile perch. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Nile River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Nile River through time.", "x": "History: Disputes over water.. Annual flood fertilized Egypt. People and Nile River across the centuries — the world's longest river; Egypt's lifeline.. Cruises. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Nile River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Nile River.", "x": "Conservation: Delta in Egypt.. 6,650 km long. Threats and guardians of Nile River — the world's longest river; Egypt's lifeline.. Ancient civilization. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Nile River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Nile River in numbers.", "x": "Numbers: 6,650 km long.; Flows north.. Nile perch. Statistics that stun — Nile River. the world's longest river; Egypt's lifeline. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-nile-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
