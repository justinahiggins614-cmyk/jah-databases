(function(){'use strict';
/* JAH K2 Mountain Database generator — jahdb-e2-mountain-k2-mountain-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-k2-mountain',PREFIX='JAH-E2MOUNTAINK-',NAME='JAH K2 Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "K2: the complete guide", "d": "K2: the savage mountain; hardest 8,000er..", "g": "overview", "l": 2, "q": "What is K2: the complete guide?", "a": "K2: the savage mountain; hardest 8,000er..", "x": "The complete mountain guide to K2: the savage mountain; hardest 8,000er.. 8,611m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Abruzzi Ridge. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8,611m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8,611m.", "x": "K2: 8,611m.. Weather. One of the defining facts — Harder than Everest.. the savage mountain; hardest 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 8,611m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 8,611m..", "x": "Explored: 8,611m.. Baltoro. Why it is so — K2. First: 1954 Italians. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pakistan/China.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pakistan/China.", "x": "K2: Pakistan/China.. Climbers. One of the defining facts — First: 1954 Italians.. the savage mountain; hardest 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Pakistan/China..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Pakistan/China..", "x": "Explored: Pakistan/China.. Records. Why it is so — K2. High fatality. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Harder than Everest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Harder than Everest.", "x": "K2: Harder than Everest.. Baltoro. One of the defining facts — High fatality.. the savage mountain; hardest 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Harder than Everest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Harder than Everest..", "x": "Explored: Harder than Everest.. Respect. Why it is so — K2. No winter till 2021. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "First: 1954 Italians.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "First: 1954 Italians.", "x": "K2: First: 1954 Italians.. Records. One of the defining facts — No winter till 2021.. the savage mountain; hardest 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: First: 1954 Italians..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: First: 1954 Italians..", "x": "Explored: First: 1954 Italians.. Abruzzi Ridge. Why it is so — K2. 8,611m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "High fatality.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "High fatality.", "x": "K2: High fatality.. Respect. One of the defining facts — 8,611m.. the savage mountain; hardest 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: High fatality..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: High fatality..", "x": "Explored: High fatality.. Weather. Why it is so — K2. Pakistan/China. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "No winter till 2021.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "No winter till 2021.", "x": "K2: No winter till 2021.. Abruzzi Ridge. One of the defining facts — Pakistan/China.. the savage mountain; hardest 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: No winter till 2021..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: No winter till 2021..", "x": "Explored: No winter till 2021.. Climbers. Why it is so — K2. Harder than Everest. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Abruzzi Ridge.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Abruzzi Ridge.", "x": "K2 in depth: Abruzzi Ridge.. Pakistan/China. The details reward the curious — the savage mountain; hardest 8,000er.. Climbers. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Weather.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Weather.", "x": "K2 in depth: Weather.. Harder than Everest. The details reward the curious — the savage mountain; hardest 8,000er.. Baltoro. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Climbers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Climbers.", "x": "K2 in depth: Climbers.. First: 1954 Italians. The details reward the curious — the savage mountain; hardest 8,000er.. Records. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Baltoro.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Baltoro.", "x": "K2 in depth: Baltoro.. High fatality. The details reward the curious — the savage mountain; hardest 8,000er.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Records.", "x": "K2 in depth: Records.. No winter till 2021. The details reward the curious — the savage mountain; hardest 8,000er.. Abruzzi Ridge. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "K2 in depth: Respect.. 8,611m. The details reward the curious — the savage mountain; hardest 8,000er.. Weather. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where K2 is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where K2 is.", "x": "Location: 8,611m.. Abruzzi Ridge. Getting oriented — K2. the savage mountain; hardest 8,000er. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience K2.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience K2.", "x": "Visiting: Weather.. Pakistan/China. Practical know-how — K2. the savage mountain; hardest 8,000er. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around K2.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around K2.", "x": "Ecology: Climbers.. Harder than Everest. The living world of K2 — the savage mountain; hardest 8,000er.. Baltoro. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "K2 through time.", "g": "history", "l": 2, "q": "What is History?", "a": "K2 through time.", "x": "History: Records.. First: 1954 Italians. People and K2 across the centuries — the savage mountain; hardest 8,000er.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting K2.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting K2.", "x": "Conservation: Weather.. 8,611m. Threats and guardians of K2 — the savage mountain; hardest 8,000er.. Climbers. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "K2 in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "K2 in numbers.", "x": "Numbers: 8,611m.; Pakistan/China.. Baltoro. Statistics that stun — K2. the savage mountain; hardest 8,000er. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-k2-mountain-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
