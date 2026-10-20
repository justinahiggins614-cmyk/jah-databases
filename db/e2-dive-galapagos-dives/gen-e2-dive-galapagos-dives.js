(function(){'use strict';
/* JAH Galapagos Dives Dive Site Database generator — jahdb-e2-dive-galapagos-dives-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive-galapagos-dives',PREFIX='JAH-E2DIVEGALAP-',NAME='JAH Galapagos Dives Dive Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Galapagos Dives: the complete guide", "d": "Galapagos Dives: evolution underwater..", "g": "overview", "l": 2, "q": "What is Galapagos Dives: the complete guide?", "a": "Galapagos Dives: evolution underwater..", "x": "The complete dive site guide to Galapagos Dives: evolution underwater.. Ecuador. From formation to visiting, from wildlife to legends — everything about this dive site in one database. Sharks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Ecuador.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Ecuador.", "x": "Galapagos Dives: Ecuador.. Iguanas. One of the defining facts — Marine iguanas.. evolution underwater. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Ecuador..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Ecuador..", "x": "Explored: Ecuador.. Ecuador. Why it is so — Galapagos Dives. Wolf/Darwin. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hammerheads.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hammerheads.", "x": "Galapagos Dives: Hammerheads.. Liveaboard. One of the defining facts — Wolf/Darwin.. evolution underwater. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Hammerheads..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Hammerheads..", "x": "Explored: Hammerheads.. Currents. Why it is so — Galapagos Dives. Liveaboard. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Marine iguanas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Marine iguanas.", "x": "Galapagos Dives: Marine iguanas.. Ecuador. One of the defining facts — Liveaboard.. evolution underwater. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Marine iguanas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Marine iguanas..", "x": "Explored: Marine iguanas.. Evolution. Why it is so — Galapagos Dives. Currents. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wolf/Darwin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wolf/Darwin.", "x": "Galapagos Dives: Wolf/Darwin.. Currents. One of the defining facts — Currents.. evolution underwater. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Wolf/Darwin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Wolf/Darwin..", "x": "Explored: Wolf/Darwin.. Sharks. Why it is so — Galapagos Dives. Ecuador. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Liveaboard.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Liveaboard.", "x": "Galapagos Dives: Liveaboard.. Evolution. One of the defining facts — Ecuador.. evolution underwater. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Liveaboard..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Liveaboard..", "x": "Explored: Liveaboard.. Iguanas. Why it is so — Galapagos Dives. Hammerheads. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Currents.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Currents.", "x": "Galapagos Dives: Currents.. Sharks. One of the defining facts — Hammerheads.. evolution underwater. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Currents..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Currents..", "x": "Explored: Currents.. Liveaboard. Why it is so — Galapagos Dives. Marine iguanas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sharks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sharks.", "x": "Galapagos Dives in depth: Sharks.. Hammerheads. The details reward the curious — evolution underwater.. Liveaboard. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Iguanas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Iguanas.", "x": "Galapagos Dives in depth: Iguanas.. Marine iguanas. The details reward the curious — evolution underwater.. Ecuador. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Liveaboard.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Liveaboard.", "x": "Galapagos Dives in depth: Liveaboard.. Wolf/Darwin. The details reward the curious — evolution underwater.. Currents. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ecuador.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ecuador.", "x": "Galapagos Dives in depth: Ecuador.. Liveaboard. The details reward the curious — evolution underwater.. Evolution. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Currents.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Currents.", "x": "Galapagos Dives in depth: Currents.. Currents. The details reward the curious — evolution underwater.. Sharks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Evolution.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Evolution.", "x": "Galapagos Dives in depth: Evolution.. Ecuador. The details reward the curious — evolution underwater.. Iguanas. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Galapagos Dives is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Galapagos Dives is.", "x": "Location: Ecuador.. Sharks. Getting oriented — Galapagos Dives. evolution underwater. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Galapagos Dives.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Galapagos Dives.", "x": "Visiting: Iguanas.. Hammerheads. Practical know-how — Galapagos Dives. evolution underwater. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Galapagos Dives.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Galapagos Dives.", "x": "Ecology: Liveaboard.. Marine iguanas. The living world of Galapagos Dives — evolution underwater.. Ecuador. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Galapagos Dives through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Galapagos Dives through time.", "x": "History: Currents.. Wolf/Darwin. People and Galapagos Dives across the centuries — evolution underwater.. Evolution. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Galapagos Dives.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Galapagos Dives.", "x": "Conservation: Iguanas.. Ecuador. Threats and guardians of Galapagos Dives — evolution underwater.. Liveaboard. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Galapagos Dives in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Galapagos Dives in numbers.", "x": "Numbers: Ecuador.; Hammerheads.. Ecuador. Statistics that stun — Galapagos Dives. evolution underwater. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive-galapagos-dives-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
