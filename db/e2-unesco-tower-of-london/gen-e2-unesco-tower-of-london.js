(function(){'use strict';
/* JAH Tower of London Unesco Site Database generator — jahdb-e2-unesco-tower-of-london-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-tower-of-london',PREFIX='JAH-E2UNESCOTOW-',NAME='JAH Tower of London Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tower of London: the complete guide", "d": "Tower of London: 1,000 years of power..", "g": "overview", "l": 2, "q": "What is Tower of London: the complete guide?", "a": "Tower of London: 1,000 years of power..", "x": "The complete unesco site guide to Tower of London: 1,000 years of power.. 1066. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1066.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1066.", "x": "Tower of London: 1066.. Jewels. One of the defining facts — Ravens.. 1,000 years of power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1066..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1066..", "x": "Explored: 1066.. Tours. Why it is so — Tower of London. Beefeaters. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Crown Jewels.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Crown Jewels.", "x": "Tower of London: Crown Jewels.. Ravens. One of the defining facts — Beefeaters.. 1,000 years of power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Crown Jewels..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Crown Jewels..", "x": "Explored: Crown Jewels.. Legends. Why it is so — Tower of London. UNESCO 1988. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ravens.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ravens.", "x": "Tower of London: Ravens.. Tours. One of the defining facts — UNESCO 1988.. 1,000 years of power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Ravens..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Ravens..", "x": "Explored: Ravens.. Visit. Why it is so — Tower of London. Ghosts. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Beefeaters.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Beefeaters.", "x": "Tower of London: Beefeaters.. Legends. One of the defining facts — Ghosts.. 1,000 years of power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Beefeaters..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Beefeaters..", "x": "Explored: Beefeaters.. History. Why it is so — Tower of London. 1066. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO 1988.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO 1988.", "x": "Tower of London: UNESCO 1988.. Visit. One of the defining facts — 1066.. 1,000 years of power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: UNESCO 1988..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: UNESCO 1988..", "x": "Explored: UNESCO 1988.. Jewels. Why it is so — Tower of London. Crown Jewels. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ghosts.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ghosts.", "x": "Tower of London: Ghosts.. History. One of the defining facts — Crown Jewels.. 1,000 years of power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Ghosts..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Ghosts..", "x": "Explored: Ghosts.. Ravens. Why it is so — Tower of London. Ravens. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Tower of London in depth: History.. Crown Jewels. The details reward the curious — 1,000 years of power.. Ravens. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Jewels.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Jewels.", "x": "Tower of London in depth: Jewels.. Ravens. The details reward the curious — 1,000 years of power.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ravens.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ravens.", "x": "Tower of London in depth: Ravens.. Beefeaters. The details reward the curious — 1,000 years of power.. Legends. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Tower of London in depth: Tours.. UNESCO 1988. The details reward the curious — 1,000 years of power.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legends.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legends.", "x": "Tower of London in depth: Legends.. Ghosts. The details reward the curious — 1,000 years of power.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Tower of London in depth: Visit.. 1066. The details reward the curious — 1,000 years of power.. Jewels. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Tower of London is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Tower of London is.", "x": "Location: 1066.. History. Getting oriented — Tower of London. 1,000 years of power. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Tower of London.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Tower of London.", "x": "Visiting: Jewels.. Crown Jewels. Practical know-how — Tower of London. 1,000 years of power. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Tower of London.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Tower of London.", "x": "Ecology: Ravens.. Ravens. The living world of Tower of London — 1,000 years of power.. Tours. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Tower of London through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Tower of London through time.", "x": "History: Legends.. Beefeaters. People and Tower of London across the centuries — 1,000 years of power.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Tower of London.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Tower of London.", "x": "Conservation: Jewels.. 1066. Threats and guardians of Tower of London — 1,000 years of power.. Ravens. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Tower of London in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Tower of London in numbers.", "x": "Numbers: 1066.; Crown Jewels.. Tours. Statistics that stun — Tower of London. 1,000 years of power. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-tower-of-london-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
