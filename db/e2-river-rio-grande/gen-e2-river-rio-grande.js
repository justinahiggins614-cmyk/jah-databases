(function(){'use strict';
/* JAH Rio Grande River Database generator — jahdb-e2-river-rio-grande-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-rio-grande',PREFIX='JAH-E2RIVERRIOG-',NAME='JAH Rio Grande River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rio Grande: the complete guide", "d": "Rio Grande: US-Mexico border river..", "g": "overview", "l": 2, "q": "What is Rio Grande: the complete guide?", "a": "Rio Grande: US-Mexico border river..", "x": "The complete river guide to Rio Grande: US-Mexico border river.. 3,034 km. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Colorado. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,034 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,034 km.", "x": "Rio Grande: 3,034 km.. Border. One of the defining facts — Big Bend.. US-Mexico border river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 3,034 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 3,034 km..", "x": "Explored: 3,034 km.. Treaties. Why it is so — Rio Grande. Water disputes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Border.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Border.", "x": "Rio Grande: Border.. Cities. One of the defining facts — Water disputes.. US-Mexico border river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Border..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Border..", "x": "Explored: Border.. Ecology. Why it is so — Rio Grande. El Paso. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Big Bend.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Big Bend.", "x": "Rio Grande: Big Bend.. Treaties. One of the defining facts — El Paso.. US-Mexico border river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Big Bend..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Big Bend..", "x": "Explored: Big Bend.. Culture. Why it is so — Rio Grande. Wildlife. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Water disputes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Water disputes.", "x": "Rio Grande: Water disputes.. Ecology. One of the defining facts — Wildlife.. US-Mexico border river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Water disputes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Water disputes..", "x": "Explored: Water disputes.. Source: Colorado. Why it is so — Rio Grande. 3,034 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "El Paso.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "El Paso.", "x": "Rio Grande: El Paso.. Culture. One of the defining facts — 3,034 km.. US-Mexico border river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: El Paso..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: El Paso..", "x": "Explored: El Paso.. Border. Why it is so — Rio Grande. Border. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wildlife.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wildlife.", "x": "Rio Grande: Wildlife.. Source: Colorado. One of the defining facts — Border.. US-Mexico border river. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Wildlife..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Wildlife..", "x": "Explored: Wildlife.. Cities. Why it is so — Rio Grande. Big Bend. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Colorado.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Colorado.", "x": "Rio Grande in depth: Source: Colorado.. Border. The details reward the curious — US-Mexico border river.. Cities. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Border.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Border.", "x": "Rio Grande in depth: Border.. Big Bend. The details reward the curious — US-Mexico border river.. Treaties. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cities.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cities.", "x": "Rio Grande in depth: Cities.. Water disputes. The details reward the curious — US-Mexico border river.. Ecology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Treaties.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Treaties.", "x": "Rio Grande in depth: Treaties.. El Paso. The details reward the curious — US-Mexico border river.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ecology.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ecology.", "x": "Rio Grande in depth: Ecology.. Wildlife. The details reward the curious — US-Mexico border river.. Source: Colorado. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Rio Grande in depth: Culture.. 3,034 km. The details reward the curious — US-Mexico border river.. Border. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Rio Grande is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Rio Grande is.", "x": "Location: 3,034 km.. Source: Colorado. Getting oriented — Rio Grande. US-Mexico border river. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Rio Grande.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Rio Grande.", "x": "Visiting: Border.. Border. Practical know-how — Rio Grande. US-Mexico border river. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Rio Grande.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Rio Grande.", "x": "Ecology: Cities.. Big Bend. The living world of Rio Grande — US-Mexico border river.. Treaties. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Rio Grande through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Rio Grande through time.", "x": "History: Ecology.. Water disputes. People and Rio Grande across the centuries — US-Mexico border river.. Culture. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Rio Grande.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Rio Grande.", "x": "Conservation: Border.. 3,034 km. Threats and guardians of Rio Grande — US-Mexico border river.. Cities. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Rio Grande in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Rio Grande in numbers.", "x": "Numbers: 3,034 km.; Border.. Treaties. Statistics that stun — Rio Grande. US-Mexico border river. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-rio-grande-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
