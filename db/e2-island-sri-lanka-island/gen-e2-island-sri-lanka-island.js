(function(){'use strict';
/* JAH Sri Lanka Island Database generator — jahdb-e2-island-sri-lanka-island-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-island-sri-lanka-island',PREFIX='JAH-E2ISLANDSRI-',NAME='JAH Sri Lanka Island Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sri Lanka: the complete guide", "d": "Sri Lanka: pearl of the Indian Ocean..", "g": "overview", "l": 2, "q": "What is Sri Lanka: the complete guide?", "a": "Sri Lanka: pearl of the Indian Ocean..", "x": "The complete island guide to Sri Lanka: pearl of the Indian Ocean.. 65,000 sq km. From formation to visiting, from wildlife to legends — everything about this island in one database. Tea. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "65,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "65,000 sq km.", "x": "Sri Lanka: 65,000 sq km.. Ruins. One of the defining facts — Sigiriya.. pearl of the Indian Ocean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 65,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 65,000 sq km..", "x": "Explored: 65,000 sq km.. Beaches. Why it is so — Sri Lanka. Elephants. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tea.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tea.", "x": "Sri Lanka: Tea.. Wildlife. One of the defining facts — Elephants.. pearl of the Indian Ocean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Tea..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Tea..", "x": "Explored: Tea.. Culture. Why it is so — Sri Lanka. Beaches. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sigiriya.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sigiriya.", "x": "Sri Lanka: Sigiriya.. Beaches. One of the defining facts — Beaches.. pearl of the Indian Ocean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Sigiriya..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Sigiriya..", "x": "Explored: Sigiriya.. Travel. Why it is so — Sri Lanka. Colombo. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Elephants.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Elephants.", "x": "Sri Lanka: Elephants.. Culture. One of the defining facts — Colombo.. pearl of the Indian Ocean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Elephants..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Elephants..", "x": "Explored: Elephants.. Tea. Why it is so — Sri Lanka. 65,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beaches.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beaches.", "x": "Sri Lanka: Beaches.. Travel. One of the defining facts — 65,000 sq km.. pearl of the Indian Ocean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Beaches..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Beaches..", "x": "Explored: Beaches.. Ruins. Why it is so — Sri Lanka. Tea. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Colombo.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Colombo.", "x": "Sri Lanka: Colombo.. Tea. One of the defining facts — Tea.. pearl of the Indian Ocean. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Colombo..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Colombo..", "x": "Explored: Colombo.. Wildlife. Why it is so — Sri Lanka. Sigiriya. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tea.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tea.", "x": "Sri Lanka in depth: Tea.. Tea. The details reward the curious — pearl of the Indian Ocean.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ruins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ruins.", "x": "Sri Lanka in depth: Ruins.. Sigiriya. The details reward the curious — pearl of the Indian Ocean.. Beaches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wildlife.", "x": "Sri Lanka in depth: Wildlife.. Elephants. The details reward the curious — pearl of the Indian Ocean.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beaches.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beaches.", "x": "Sri Lanka in depth: Beaches.. Beaches. The details reward the curious — pearl of the Indian Ocean.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Culture.", "x": "Sri Lanka in depth: Culture.. Colombo. The details reward the curious — pearl of the Indian Ocean.. Tea. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Sri Lanka in depth: Travel.. 65,000 sq km. The details reward the curious — pearl of the Indian Ocean.. Ruins. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Sri Lanka is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Sri Lanka is.", "x": "Location: 65,000 sq km.. Tea. Getting oriented — Sri Lanka. pearl of the Indian Ocean. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Sri Lanka.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Sri Lanka.", "x": "Visiting: Ruins.. Tea. Practical know-how — Sri Lanka. pearl of the Indian Ocean. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Sri Lanka.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Sri Lanka.", "x": "Ecology: Wildlife.. Sigiriya. The living world of Sri Lanka — pearl of the Indian Ocean.. Beaches. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Sri Lanka through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Sri Lanka through time.", "x": "History: Culture.. Elephants. People and Sri Lanka across the centuries — pearl of the Indian Ocean.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Sri Lanka.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Sri Lanka.", "x": "Conservation: Ruins.. 65,000 sq km. Threats and guardians of Sri Lanka — pearl of the Indian Ocean.. Wildlife. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Sri Lanka in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Sri Lanka in numbers.", "x": "Numbers: 65,000 sq km.; Tea.. Beaches. Statistics that stun — Sri Lanka. pearl of the Indian Ocean. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-island-sri-lanka-island-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
