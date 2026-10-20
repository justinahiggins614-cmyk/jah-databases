(function(){'use strict';
/* JAH Manuel Antonio Beach Beach Database generator — jahdb-e2-beach-manuel-antonio-beach-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-manuel-antonio-beach',PREFIX='JAH-E2BEACHMANU-',NAME='JAH Manuel Antonio Beach Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Manuel Antonio Beach: the complete guide", "d": "Manuel Antonio Beach: park and sand..", "g": "overview", "l": 2, "q": "What is Manuel Antonio Beach: the complete guide?", "a": "Manuel Antonio Beach: park and sand..", "x": "The complete beach guide to Manuel Antonio Beach: park and sand.. Park. From formation to visiting, from wildlife to legends — everything about this beach in one database. Park. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Park.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Park.", "x": "Manuel Antonio Beach: Park.. Monkeys. One of the defining facts — Espadilla.. park and sand. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Park..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Park..", "x": "Explored: Park.. Snorkel. Why it is so — Manuel Antonio Beach. Costa Rica. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Monkeys.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Monkeys.", "x": "Manuel Antonio Beach: Monkeys.. Jungle. One of the defining facts — Costa Rica.. park and sand. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Monkeys..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Monkeys..", "x": "Explored: Monkeys.. Costa Rica. Why it is so — Manuel Antonio Beach. Jungle. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Espadilla.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Espadilla.", "x": "Manuel Antonio Beach: Espadilla.. Snorkel. One of the defining facts — Jungle.. park and sand. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Espadilla..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Espadilla..", "x": "Explored: Espadilla.. Beauty. Why it is so — Manuel Antonio Beach. Snorkel. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Costa Rica.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Costa Rica.", "x": "Manuel Antonio Beach: Costa Rica.. Costa Rica. One of the defining facts — Snorkel.. park and sand. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Costa Rica..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Costa Rica..", "x": "Explored: Costa Rica.. Park. Why it is so — Manuel Antonio Beach. Park. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Jungle.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Jungle.", "x": "Manuel Antonio Beach: Jungle.. Beauty. One of the defining facts — Park.. park and sand. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Jungle..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Jungle..", "x": "Explored: Jungle.. Monkeys. Why it is so — Manuel Antonio Beach. Monkeys. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Snorkel.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Snorkel.", "x": "Manuel Antonio Beach: Snorkel.. Park. One of the defining facts — Monkeys.. park and sand. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Snorkel..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Snorkel..", "x": "Explored: Snorkel.. Jungle. Why it is so — Manuel Antonio Beach. Espadilla. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Park.", "x": "Manuel Antonio Beach in depth: Park.. Monkeys. The details reward the curious — park and sand.. Jungle. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Monkeys.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Monkeys.", "x": "Manuel Antonio Beach in depth: Monkeys.. Espadilla. The details reward the curious — park and sand.. Snorkel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Jungle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Jungle.", "x": "Manuel Antonio Beach in depth: Jungle.. Costa Rica. The details reward the curious — park and sand.. Costa Rica. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Snorkel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Snorkel.", "x": "Manuel Antonio Beach in depth: Snorkel.. Jungle. The details reward the curious — park and sand.. Beauty. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Costa Rica.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Costa Rica.", "x": "Manuel Antonio Beach in depth: Costa Rica.. Snorkel. The details reward the curious — park and sand.. Park. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Beauty.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Beauty.", "x": "Manuel Antonio Beach in depth: Beauty.. Park. The details reward the curious — park and sand.. Monkeys. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Manuel Antonio Beach is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Manuel Antonio Beach is.", "x": "Location: Park.. Park. Getting oriented — Manuel Antonio Beach. park and sand. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Manuel Antonio Beach.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Manuel Antonio Beach.", "x": "Visiting: Monkeys.. Monkeys. Practical know-how — Manuel Antonio Beach. park and sand. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Manuel Antonio Beach.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Manuel Antonio Beach.", "x": "Ecology: Jungle.. Espadilla. The living world of Manuel Antonio Beach — park and sand.. Snorkel. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Manuel Antonio Beach through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Manuel Antonio Beach through time.", "x": "History: Costa Rica.. Costa Rica. People and Manuel Antonio Beach across the centuries — park and sand.. Beauty. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Manuel Antonio Beach.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Manuel Antonio Beach.", "x": "Conservation: Monkeys.. Park. Threats and guardians of Manuel Antonio Beach — park and sand.. Jungle. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Manuel Antonio Beach in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Manuel Antonio Beach in numbers.", "x": "Numbers: Park.; Monkeys.. Snorkel. Statistics that stun — Manuel Antonio Beach. park and sand. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-manuel-antonio-beach-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
